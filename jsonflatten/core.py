"""
JSON File Flattener

Functions used to flatten a json-serialized document in the jsoncut list
format.

Functions:
    1.  flatten_all -> flatten the entire document
    2.  flatten_by_keys -> only flatten user-specified keys
    3.  generate_rows -> create rows of data from the json document for use
        as a dataframe or for other data analysis uses
"""

from collections import Sequence
from collections import Mapping

from jsoncut.core import get_items
from jsoncut.treecrawler import find_keys


def flatten_all(d):
    """
    Flattens the entire json-serialized document in the jsoncut list format.

    Args:
        d (dict): json-serialized document converted to a python dict.

    Returns:
        dict: flat dict with each key being in the jsoncut style.

    Example:
        d = {'key1': 'item1', 'key2': {'key3': 'item3'}}
        returns: {'key1': 'item1', 'key2.key3': 'item3'}
    """
    return flatten_by_keys(d)


def flatten_by_keys(d, keys=None):
    """
    Flattens the specified keys in the json-serialized document.  If key has
    an array as the value with more key-value pairs, then each index in the
    array is flattened, as well.  If the key is a root key with a dict as a
    value, then recursively flattens that branch.

    Args:
        d (dict): json-serialized document converted to a python dict.
        keys (str or [str1, str2,...]): singleton or list of jsoncut-style
            keys.  If not specified, or set to None, the entire document is
            flattened.

    Returs:
        dict: dictionary with the flattened content.

    Example:
        d = {'key1': 'item1', 'key2': {'key3': 'item3'}}
        keys = ['key2.key3']
        returns: {'key2.key3': 'item3'}
    """
    flattened = {}
    if keys is None:
        keys = find_keys(d)
    for key in keys:
        content = get_key_content(d, key)

        # flatten each item in an array, as well.
        if (content and isinstance(content, Sequence) and
                isinstance(content[0], Mapping) and len(content) > 1):

            flattened[key] = []
            array_content = get_items(d, key.split('.'), fullpath=True,
                                      any=False)

            for item in array_content[key]:
                array_keys = find_keys(item)
                flattened[key].append(flatten_by_keys(item, array_keys))

        elif not isinstance(content, Mapping):
            flattened[key] = content

        elif isinstance(content, Mapping):
            flattened.update({'.'.join([key, k]): v for k, v in
                             flatten_by_keys(content).items()})

    return flattened


def generate_rows(d, root_key, prepend_keys=None):
    """
    Generator function that generates rows of data from multiple entries in
    the root_key, with the option to prepend columns.  Useful when waning to
    create dataframes, or rows to export to a CSV file for data analysis.

    Args:
        d (dict): json-serialized document converted to a python dict.
        root_key (str): jsoncut-style key that specifies the root where all
            data is to be collected for the rows.
        prepend_keys (str): optional list of jsoncut-style keys that will
            prepend the data rows, such as data that is not part of the
            root_key data.

    Yields:
        dict: row of data

    Example:
        d = {'key1': 'item1', 'key2': [{'date':'today'}, {'date': 'tomorrow'}]}
        root_key = 'key2'
        prepend_keys = ['key1']
        yield:
            {'key1':'item1', 'date': 'today'}
            {'key1':'item1', 'date': 'tomorrow'}
    """
    # add prepended data if requested
    prepend_data = {}
    if prepend_keys is not None:
        prepend_data.update(flatten_by_keys(d, prepend_keys))

    # get the content and create individual rows
    content_array = get_items(d, [root_key], fullpath=True, any=False)
    for item in content_array[root_key]:
        row = {}
        row.update(prepend_data)
        keys = find_keys(item)
        row.update(flatten_by_keys(item, keys))

        yield row


def get_key_content(d, key):
    """
    Utility function that returns the content of a jsoncut-style key.

    Args:
        d (dict): json-serialized document converted to a python dict.
        key (str): a jsoncut style key.

    Returns:
        value: the value stored in the given key

    Raises:
        jsoncut.exceptions.KeyNotFound via jsoncut.core.get_items()
        if invalid key.

    Example:
        d = {'key1': 'item1', 'key2': {'key3': 'item3'}}
        key = 'key2.key3'
        returns 'item3'
    """
    items = get_items(d, key.split('.'), fullpath=True, any=False)
    return items[key]
