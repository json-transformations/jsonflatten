"""Command-Line Interface."""

import click
from click import argument
from click import option
from click import version_option

from jsoncut.cli import load_json
from jsoncut.cli import output
from jsoncut.sequencer import Items
from jsoncut.tokenizer import SLICE_RE, parse_defaults, parse_keystr
from jsoncut.treecrawler import find_keys

from jsonflatten.core import flatten_by_keys
from jsonflatten.core import generate_rows


def get_results(data, kwds):
    """ Dispatch to correct function(s) """
    if kwds['Flatten']:
        results = flatten_by_keys(data, keys=None)
    elif kwds['flatten'] is not None:
        data_ = Items([data] if kwds['slice_'] else data)
        keys = find_keys(data_.value, fullscan=True)
        keylists = parse_keystr(kwds['flatten'], data.items, quotechar='"',
                                keys=keys)
        results = flatten_by_keys(data_.value, keys=['.'.join(key) for
                                  key in keylists])
    return results


@click.command()
@argument('jsonfile', type=click.Path(readable=True), required=False)
@option('-F', '--Flatten', 'Flatten', is_flag=True,
        help='Flatten entire json document.')
@option('-f', '--flatten', 'flatten',
        help='Flatten only those specified keys as a comma-separated list ' +
        'generated from `jsoncut -l` option.')
@option('-g', '--genrows', 'genrows', is_flag=True,
        help='If set, generates flattened rows of output if one of the ' +
        'keys is a Sequence, specified with the -f option, or ' +
        'automatically if used with the -F option.')
@option('-n', '--nocolor', is_flag=True, help='disable syntax highlighting')
@option('-s', '--slice', 'slice_', is_flag=True, help='disable sequencer')
@version_option(version='0.0', prog_name='JSON Flatten')
@click.pass_context
def main(ctx, **kwds):
    """Parse command-line args"""
    ctx.color = False if kwds['nocolor'] else True
    data = load_json(ctx, kwds['jsonfile'])
    results = get_results(data, kwds)
    output(ctx, results, indent=4, is_json=True)


if __name__ == '__main__':
    main()
