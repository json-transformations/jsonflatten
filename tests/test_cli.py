"""Test module for the jsonflatten.cli functions."""

import sys
from unittest.mock import patch

import pytest

import click._termui_impl
from click import Context
from click.testing import CliRunner

from jsonflatten.cli import get_results
from jsonflatten.cli import main

from sample_data import FORECAST
from sample_data import FORECAST_FLAT


##############################################################################
# TESTS get_results
##############################################################################

def test_get_results_flatten_all():
    """
    GIVEN a json-serialized document converted to a python dict
    WHEN get_results() is called with kwds['flatten']=None
    THEN assert the entire document is flattened
    """
    kwds = {'flatten': None}
    assert get_results(FORECAST, kwds) == FORECAST_FLAT


def test_get_results_flatten_specified_comma():
    """
    GIVEN a json-serialized document converted to a python dict
    WHEN get_results() is called with kwds['flatten'] specified by the
        user as a comma-separated list (i.e. -f1,6)
    THEN assert the specified keys are flattened
    """
    kwds = {'flatten': ('1,6',), 'slice_': False, 'quotechar': '"'}
    assert get_results(FORECAST, kwds) == {'city': FORECAST_FLAT['city'],
                                        'forecast': FORECAST_FLAT['forecast']}


def test_get_results_flatten_specified_multi():
    """
    GIVEN a json-serialized document converted to a python dict
    WHEN get_results() is called with kwds['flatten'] specified by the
        user with multiple -f options (i.e. -f1 -f6)
    THEN assert the specified keys are flattened
    """
    kwds = {'flatten': ('1', '6'), 'slice_': False, 'quotechar': '"'}
    assert get_results(FORECAST, kwds) == {'city': FORECAST_FLAT['city'],
                                        'forecast': FORECAST_FLAT['forecast']}


##############################################################################
# TESTS main
##############################################################################

class Config:
    """Used to pass ctx for click applications."""
    def __init__(self):
        self.color = False


@patch('jsonflatten.cli.load_json')
def test_main_mapping(loadjson_mock):
    """
    GIVEN a json-serialized document converted to a python dict
    WHEN the cli.main() function is invoked for an input of type Mapping
    THEN assert entire input is flattened and outputted in the expected
        format
    """
    kwds = {'jsonfile': 'testfile'}
    ctx = Context(main, obj=Config())
    loadjson_mock.return_value = {'testfile': {'k1': 'v1', 'k2': 'v2'}}

    runner = CliRunner()
    result = runner.invoke(main, ['kwds'])
    expected_output = ['{\n', '"testfile.k1": "v1"', '"testfile.k2": "v2"', '}']

    assert all([item in result.output for item in expected_output])


@patch('jsonflatten.cli.load_json')
def test_main_sequence(loadjson_mock):
    """
    GIVEN a json-serialized document converted to a python dict
    WHEN the cli.main() function is invoked for an input of type Sequence
    THEN assert entire input is flattened and outputted in the expected
        format
    """
    kwds = {'jsonfile': 'testfile'}
    ctx = Context(main, obj=Config())
    loadjson_mock.return_value = [{'testONE': {'k1': 'v1', 'k2': 'v2'}},
                                  {'testTWO': {'k3': 'v3', 'k4': 'v4'}}]

    runner = CliRunner()
    result = runner.invoke(main, ['kwds'])
    expected_output = ['{\n', '"testONE.k1": "v1"', '"testONE.k2": "v2"',
                       '"testTWO.k3": "v3"', '"testTWO.k4": "v4"', '}']

    assert all([item in result.output for item in expected_output])


def test_main_no_jsonfile(monkeypatch):
    """
    GIVEN a call to jsonflatten
    WHEN no jsonfile is given
    THEN assert the usage information is properly printed
    """
    kwds = {'jsonfile': None}
    ctx = Context(main, obj=Config())
    ctx.command.name = 'jsonflatten'

    monkeypatch.setattr(click._termui_impl, 'isatty', lambda x: True)

    runner = CliRunner()
    result = runner.invoke(main)
    expected_output = ('Usage: jsonflatten [OPTIONS] [JSONFILE]\n'
                       'Try `jsonflatten --help` for more information.\n')

    print(result.output)
    assert result.output == expected_output
