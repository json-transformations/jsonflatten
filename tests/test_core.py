"""Test module for the jsonflatten.core functions."""

import pytest

from jsonflatten.core import flatten_all
from jsonflatten.core import flatten_by_keys
from jsonflatten.core import generate_rows
from jsonflatten.core import get_key_content

from jsoncut.exceptions import KeyNotFound

from sample_data import FORECAST
from sample_data import FORECAST_FLAT
from sample_data import FORECAST_ROWS


##############################################################################
# TESTS flatten_all
##############################################################################

def test_flatten_all():
    """
    GIVEN a json-serialzed document converted to a python dict
    WHEN the user requests to flatten the entire document
    THEN assert is it flattened and in the correct format
    """
    flattened = flatten_all(FORECAST)
    assert flattened == FORECAST_FLAT


def test_flatten_all_nested_sequenceOfOneDict():
    """
    GIVEN a json-serialzed document converted to a python dict
    WHEN the user requests to flatten the entire document with a nested
        list of only one dict
    THEN assert is it flattened and in the correct format
    """
    data = {'k1': {'k2': [{'k3': 'test'}]}}
    assert flatten_all(data) == {'k1.k2': [{'k3': 'test'}]}


def test_flatten_all_nested_sequenceOfMultipleDicts():
    """
    GIVEN a json-serialzed document converted to a python dict
    WHEN the user requests to flatten the entire document with a nested
        list of multiple dicts
    THEN assert is it flattened and in the correct format
    """
    data = {'k1': {'k2': [{'k3': 'test'}, {'k4': 'TEST'}]}}
    assert flatten_all(data) == {'k1.k2': [{'k3': 'test'}, {'k4': 'TEST'}]}


def test_flatten_all_nested_sequenceOfOneNonDicts():
    """
    GIVEN a json-serialzed document converted to a python dict
    WHEN the user requests to flatten the entire document with a nested
        list of one non-dict item
    THEN assert is it flattened and in the correct format
    """
    data = {'k1': {'k2': ['item1']}}
    assert flatten_all(data) == {'k1.k2': ['item1']}


def test_flatten_all_nested_sequenceOfMultNonDicts():
    """
    GIVEN a json-serialzed document converted to a python dict
    WHEN the user requests to flatten the entire document with a nested
        list of multiple non-dict items
    THEN assert is it flattened and in the correct format
    """
    data = {'k1': {'k2': ['item1', 'item2']}}
    assert flatten_all(data) == {'k1.k2': ['item1', 'item2']}


##############################################################################
# TESTS flatten_by_keys
##############################################################################

def test_flatten_by_keys_all():
    """
    GIVEN a json-serialzed document converted to a python dict
    WHEN the user requests to flatten but does not list keys
    THEN assert it flattens the entire document
    """
    flattened = flatten_by_keys(FORECAST)
    assert flattened == FORECAST_FLAT


def test_flatten_by_keys_validList():
    """
    GIVEN a json-serialzed document converted to a python dict
    WHEN the user requests to flatten and specifies a list of keys
    THEN assert it flattens only the specified keys
    """
    flattened = flatten_by_keys(FORECAST, keys=['city', 'coord.lat'])
    assert flattened == {'city': 'jacksonville', 'coord.lat': 30.332}


def test_flatten_by_keys_KeyNotFound():
    """
    GIVEN a json-serialzed document converted to a python dict
    WHEN the user requests to flatten with a key that does not exist
    THEN assert jsoncut.exceptions.KeyNotFound is raised
    """
    with pytest.raises(KeyNotFound):
        flatten_by_keys(FORECAST, keys=['not.a.real.key'])


def test_flatten_by_keys_valIsList():
    """
    GIVEN a json-serialzed document converted to a python dict
    WHEN the user requests to flatten with a key who's value is an array of
        non-dict values
    THEN assert it is flattened appropriately
    """
    data = {'key1': 'val1', 'key2': {'key3': [1, 2, 3]}}
    flattened = flatten_by_keys(data)
    assert flattened == {'key1': 'val1', 'key2.key3': [1, 2, 3]}


def test_flatten_by_keys_rootKey():
    """
    """
    flattened = flatten_by_keys(FORECAST, keys=['coord'])
    assert flattened == {'coord.lat': 30.332, 'coord.lon': -81.655}


##############################################################################
# TESTS generate_rows
##############################################################################

def test_generate_rows():
    """
    GIVEN a json-serialzed document converted to a python dict
    WHEN the user requests to generate rows of data items with prepended
        sources
    THEN assert the rows are generated
    """
    row = generate_rows(FORECAST, 'forecast', ['city',
                        'coord.lat', 'coord.lon'])
    assert next(row) == FORECAST_ROWS[0]
    assert next(row) == FORECAST_ROWS[1]


def test_generate_rows_invalid_rootkey():
    """
    GIVEN a json-serialzed document converted to a python dict
    WHEN the user requests to generate rows of data from an invalid root_key
    THEN assert jsoncut.exceptions.KeyNotFound is raised
    """
    with pytest.raises(KeyNotFound):
        next(generate_rows(FORECAST, 'bad_key', ['city']))


def test_generate_rows_invalid_prependkey():
    """
    GIVEN a json-serialzed document converted to a python dict
    WHEN the user requests to generate rows of data from a valid root_key, but
        with invalid prepend_keys
    THEN assert jsoncut.exceptions.KeyNotFound is raised
    """
    with pytest.raises(KeyNotFound):
        next(generate_rows(FORECAST, 'forecast', ['bad_key']))


##############################################################################
# TESTS get_content
##############################################################################

@pytest.mark.parametrize('key',
                         ['city',
                          'date',
                          'coord.lat',
                          'coord.lon',
                          'jacket_weather',
                          'sunscreen_required',
                          'sunspot_activity'])
def test_get_content_validKey(key):
    """
    GIVEN a json-serialzed document converted to a python dict
    WHEN the user requests the value of a jsoncut-style key
    THEN assert only that key is returned
    """
    content = get_key_content(FORECAST, key)
    assert content == FORECAST_FLAT[key]


def test_get_content_invalidKey():
    """
    GIVEN a json-serialzed document converted to a python dict
    WHEN the user requests to flatten an invalid key
    THEN assert jsoncut.exceptions.KeyNotFound is raised
    """
    with pytest.raises(KeyNotFound):
        get_key_content(FORECAST, 'not.a.real.key')


def test_get_content_keyValueIsDict():
    """
    GIVEN a json-serialzed document converted to a python dict
    WHEN the user requests to flatten a key whose value is another dict
    THEN assert a dict is returned
    """
    content = get_key_content(FORECAST['forecast'][0], 'wind')
    assert content == FORECAST['forecast'][0]['wind']
