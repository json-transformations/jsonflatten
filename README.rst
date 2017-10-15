JSON Flatten
============

.. image:: https://img.shields.io/pypi/v/jsonflatten.svg
    :target: https://pypi.python.org/pypi/jsonflatten
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/borntyping/cookiecutter-pypackage-minimal.png
   :target: https://travis-ci.org/borntyping/cookiecutter-pypackage-minimal
   :alt: Latest Travis CI build status

A JSON document flattening tool

.. code-block:: console

  $ jsonflatten --help

  Usage: jsonflatten [OPTIONS] [JSONFILE]

    Specify which keys or whole document to flatten

  Options:
    -f, --flatten TEXT    Flatten only those specified keys generated from
                          `jsoncut -l` option as a comma-separated list or
                          idividually, i.e.  `-f7,9` or `-f7 -f9`
    -n, --nocolor         Disable syntax highlighting
    -q, --quotechar TEXT  Quote character used in serialized data, defaults to
                          '"'
    -s, --slice           Disable sequencer
    --version             Show the version and exit.
    --help                Show this message and exit.

Installation
------------
.. code-block:: console

  $ pip install git+https://github.com/json-transformations/jsonflatten

Usage
-----
* **Python 3 support only**; *jsonflatten is not currently supported under Python 2*.
* jsonflatten is meant to be used alongside `jsoncut <https://github.com/json-transformations/jsoncut>`_.
* Flatten the entire JSON document by not setting any command-line options.
* Flatten specified keys in the JSON document using the -f option.

Sample Data
-----------
* forecast.json - three day weather forecast API data
.. code-block:: console

  {
    "status":"200",
    "datetime": "2017-09-09 11:49",
    "request_type": "3-day Forecast",
    "list": [
      {
        "date": "2017-09-09",
        "sunrise": "07:04",
        "sunset": "19:31",
        "moonrise": "22:07",
        "moonset": "10:11",
        "temp_f_min": 81,
        "temp_f_max": 85,
        "day": {
          "humidity_pct": 82,
          "uv_index": 5,
          "weather": {
            "description": "Heavy Rain/Wind",
            "summary": "Tropical storm conditions likely. Rain showers will bring heavy downpours and strong gusty winds at times.",
            "icon":"04d"
          }, "wind": {
            "speed_ave_mph": 49,
            "speed_low_mph": 40,
            "speed_high_mph": 60,
            "direction": "ENE"
          }, "rain": {
            "precip_pct": 100,
            "low_inches": 1,
            "high_inches": 2
          }
        }, "night": {
          "humidity_pct": 82,
          "weather": {
            "description": "Heavy Rain/Wind",
            "summary": "Major hurricane conditions likely. Bands of heavy rain containing strong gusty winds at times.",
            "icon":"04d"
          }, "wind": {
            "speed_ave_mph": 120,
            "speed_low_mph": 115,
            "speed_mph": 130,
            "direction": "ENE"
          }, "rain": {
            "precip_pct": 100,
            "low_inches": 5,
            "high_inches": 8
          }
        }
      }, {
        "date": "2017-10-09",
        "sunrise": "07:04",
        "sunset": "19:30",
        "moonrise": "22:51",
        "moonset": "11:12",
        "temp_f_min": 79,
        "temp_f_max": 85,
        "day": {
          "humidity_pct": 84,
          "uv_index": 5,
          "weather": {
            "description": "Heavy Rain/Wind",
            "summary": "Major hurricane conditions likely. Bands of heavy rain containing strong gusty winds at times.",
            "icon":"04d"
          }, "wind": {
            "speed_ave_mph": 117,
            "speed_low_mph": 115,
            "speed_mph": 130,
            "direction": "SE"
          }, "rain": {
            "precip_pct": 100,
            "low_inches": 1,
            "high_inches": 2
          }
        }, "night": {
          "humidity_pct": 83,
          "weather": {
            "description": "Thunderstorms/Wind",
            "summary": "Tropical storm conditions likely.  Windy with bands of heavy rain showers and thunderstorms.",
            "icon":"04d"
          }, "wind": {
            "speed_ave_mph": 71,
            "speed_low_mph": 60,
            "speed_mph": 80,
            "direction": "SSW"
          }, "rain": {
            "precip_pct": 100,
            "low_inches": 1,
            "high_inches": 2
          }
        }
      }, {
        "date": "2017-11-09",
        "sunrise": "0705",
        "sunset": "1929",
        "moonrise": "2339",
        "moonset": "1213",
        "temp_f_min": 77,
        "temp_f_max": 90,
        "day": {
          "humidity_pct": 72,
          "uv_index": 9,
          "weather": {
            "description": "Partly Cloudy/Wind",
            "summary": "Windy. Mostly cloudy skies will become partly cloudy in the afternoon.",
            "icon":"03d"
          }, "wind": {
            "speed_ave_mph": 16,
            "speed_low_mph": 10,
            "speed_high_mph": 20,
            "direction": "WSW"
            }, "rain": {
            "precip_pct": 20,
            "low_inches": 1,
            "high_inches": 2
          }
        }, "night": {
          "humidity_pct": 82,
          "weather": {
            "description": "Partly cloudy",
            "summary": "A few clouds.",
            "icon":"04d"
          }, "wind": {
            "speed_ave_mph": 16,
            "speed_low_mph": 10,
            "speed_mph": 20,
            "direction": "WSW"
          }, "rain": {
            "precip_pct": 10,
            "low_inches": null,
            "high_inches": null
          }
        }
      }
    ], "city": {
      "id": 4164138,
      "name": "Miami",
      "coord": {
        "lat": 25.7743,
        "lon": -80.1937
      },
      "country": "US"
    }
  }

Flatten Entire JSON Document
----------------------------
.. code-block:: console

  $ jsonflatten forecast.json

.. code-block:: console

  {
      "city.coord.lat": 25.7743,
      "city.coord.lon": -80.1937,
      "city.country": "US",
      "city.id": 4164138,
      "city.name": "Miami",
      "datetime": "2017-09-09 11:49",
      "list": [
          {
              "date": "2017-09-09",
              "day.humidity_pct": 82,
              "day.rain.high_inches": 2,
              "day.rain.low_inches": 1,
              "day.rain.precip_pct": 100,
              "day.uv_index": 5,
              "day.weather.description": "Heavy Rain/Wind",
              "day.weather.icon": "04d",
              "day.weather.summary": "Tropical storm conditions likely. Rain showers will bring heavy downpours and strong gusty winds at times.",
              "day.wind.direction": "ENE",
              "day.wind.speed_ave_mph": 49,
              "day.wind.speed_high_mph": 60,
              "day.wind.speed_low_mph": 40,
              "moonrise": "22:07",
              "moonset": "10:11",
              "night.humidity_pct": 82,
              "night.rain.high_inches": 8,
              "night.rain.low_inches": 5,
              "night.rain.precip_pct": 100,
              "night.weather.description": "Heavy Rain/Wind",
              "night.weather.icon": "04d",
              "night.weather.summary": "Major hurricane conditions likely. Bands of heavy rain containing strong gusty winds at times.",
              "night.wind.direction": "ENE",
              "night.wind.speed_ave_mph": 120,
              "night.wind.speed_low_mph": 115,
              "night.wind.speed_mph": 130,
              "sunrise": "07:04",
              "sunset": "19:31",
              "temp_f_max": 85,
              "temp_f_min": 81
          },
          {
              "date": "2017-10-09",
              "day.humidity_pct": 84,
              "day.rain.high_inches": 2,
              "day.rain.low_inches": 1,
              "day.rain.precip_pct": 100,
              "day.uv_index": 5,
              "day.weather.description": "Heavy Rain/Wind",
              "day.weather.icon": "04d",
              "day.weather.summary": "Major hurricane conditions likely. Bands of heavy rain containing strong gusty winds at times.",
              "day.wind.direction": "SE",
              "day.wind.speed_ave_mph": 117,
              "day.wind.speed_low_mph": 115,
              "day.wind.speed_mph": 130,
              "moonrise": "22:51",
              "moonset": "11:12",
              "night.humidity_pct": 83,
              "night.rain.high_inches": 2,
              "night.rain.low_inches": 1,
              "night.rain.precip_pct": 100,
              "night.weather.description": "Thunderstorms/Wind",
              "night.weather.icon": "04d",
              "night.weather.summary": "Tropical storm conditions likely.  Windy with bands of heavy rain showers and thunderstorms.",
              "night.wind.direction": "SSW",
              "night.wind.speed_ave_mph": 71,
              "night.wind.speed_low_mph": 60,
              "night.wind.speed_mph": 80,
              "sunrise": "07:04",
              "sunset": "19:30",
              "temp_f_max": 85,
              "temp_f_min": 79
          },
          {
              "date": "2017-11-09",
              "day.humidity_pct": 72,
              "day.rain.high_inches": 2,
              "day.rain.low_inches": 1,
              "day.rain.precip_pct": 20,
              "day.uv_index": 9,
              "day.weather.description": "Partly Cloudy/Wind",
              "day.weather.icon": "03d",
              "day.weather.summary": "Windy. Mostly cloudy skies will become partly cloudy in the afternoon.",
              "day.wind.direction": "WSW",
              "day.wind.speed_ave_mph": 16,
              "day.wind.speed_high_mph": 20,
              "day.wind.speed_low_mph": 10,
              "moonrise": "2339",
              "moonset": "1213",
              "night.humidity_pct": 82,
              "night.rain.high_inches": null,
              "night.rain.low_inches": null,
              "night.rain.precip_pct": 10,
              "night.weather.description": "Partly cloudy",
              "night.weather.icon": "04d",
              "night.weather.summary": "A few clouds.",
              "night.wind.direction": "WSW",
              "night.wind.speed_ave_mph": 16,
              "night.wind.speed_low_mph": 10,
              "night.wind.speed_mph": 20,
              "sunrise": "0705",
              "sunset": "1929",
              "temp_f_max": 90,
              "temp_f_min": 77
          }
      ],
      "request_type": "3-day Forecast",
      "status": "200"
  }

Flatten Only Specific Keys
--------------------------
.. code-block:: console

  $ cat forecast.json | jsoncut -l
   1 city
   2 city.coord
   3 city.coord.lat
   4 city.coord.lon
   5 city.country
   6 city.id
   7 city.name
   8 datetime
   9 list
  10 request_type
  11 status

.. code-block:: console

  $ cat forecast.json | jsonflatten -f3,4,7
  {
    "city.coord.lat": 25.7743,
    "city.coord.lon": -80.1937,
    "city.name": "Miami"
  }

.. code-block:: console

  $ cat forecast.json | jsonflatten -f7 -f9
  {
    "city.name": "Miami",
    "list": [
        {
            "date": "2017-09-09",
            "day.humidity_pct": 82,
            "day.rain.high_inches": 2,
            "day.rain.low_inches": 1,
            "day.rain.precip_pct": 100,
            "day.uv_index": 5,
            "day.weather.description": "Heavy Rain/Wind",
            "day.weather.icon": "04d",
            "day.weather.summary": "Tropical storm conditions likely. Rain showers will bring heavy downpours and strong gusty winds at times.",
            "day.wind.direction": "ENE",
            "day.wind.speed_ave_mph": 49,
            "day.wind.speed_high_mph": 60,
            "day.wind.speed_low_mph": 40,
            "moonrise": "22:07",
            "moonset": "10:11",
            "night.humidity_pct": 82,
            "night.rain.high_inches": 8,
            "night.rain.low_inches": 5,
            "night.rain.precip_pct": 100,
            "night.weather.description": "Heavy Rain/Wind",
            "night.weather.icon": "04d",
            "night.weather.summary": "Major hurricane conditions likely. Bands of heavy rain containing strong gusty winds at times.",
            "night.wind.direction": "ENE",
            "night.wind.speed_ave_mph": 120,
            "night.wind.speed_low_mph": 115,
            "night.wind.speed_mph": 130,
            "sunrise": "07:04",
            "sunset": "19:31",
            "temp_f_max": 85,
            "temp_f_min": 81
        },
        {
            "date": "2017-10-09",
            "day.humidity_pct": 84,
            "day.rain.high_inches": 2,
            "day.rain.low_inches": 1,
            "day.rain.precip_pct": 100,
            "day.uv_index": 5,
            "day.weather.description": "Heavy Rain/Wind",
            "day.weather.icon": "04d",
            "day.weather.summary": "Major hurricane conditions likely. Bands of heavy rain containing strong gusty winds at times.",
            "day.wind.direction": "SE",
            "day.wind.speed_ave_mph": 117,
            "day.wind.speed_low_mph": 115,
            "day.wind.speed_mph": 130,
            "moonrise": "22:51",
            "moonset": "11:12",
            "night.humidity_pct": 83,
            "night.rain.high_inches": 2,
            "night.rain.low_inches": 1,
            "night.rain.precip_pct": 100,
            "night.weather.description": "Thunderstorms/Wind",
            "night.weather.icon": "04d",
            "night.weather.summary": "Tropical storm conditions likely.  Windy with bands of heavy rain showers and thunderstorms.",
            "night.wind.direction": "SSW",
            "night.wind.speed_ave_mph": 71,
            "night.wind.speed_low_mph": 60,
            "night.wind.speed_mph": 80,
            "sunrise": "07:04",
            "sunset": "19:30",
            "temp_f_max": 85,
            "temp_f_min": 79
        },
        {
            "date": "2017-11-09",
            "day.humidity_pct": 72,
            "day.rain.high_inches": 2,
            "day.rain.low_inches": 1,
            "day.rain.precip_pct": 20,
            "day.uv_index": 9,
            "day.weather.description": "Partly Cloudy/Wind",
            "day.weather.icon": "03d",
            "day.weather.summary": "Windy. Mostly cloudy skies will become partly cloudy in the afternoon.",
            "day.wind.direction": "WSW",
            "day.wind.speed_ave_mph": 16,
            "day.wind.speed_high_mph": 20,
            "day.wind.speed_low_mph": 10,
            "moonrise": "2339",
            "moonset": "1213",
            "night.humidity_pct": 82,
            "night.rain.high_inches": null,
            "night.rain.low_inches": null,
            "night.rain.precip_pct": 10,
            "night.weather.description": "Partly cloudy",
            "night.weather.icon": "04d",
            "night.weather.summary": "A few clouds.",
            "night.wind.direction": "WSW",
            "night.wind.speed_ave_mph": 16,
            "night.wind.speed_low_mph": 10,
            "night.wind.speed_mph": 20,
            "sunrise": "0705",
            "sunset": "1929",
            "temp_f_max": 90,
            "temp_f_min": 77
        }
    ]
  }


Authors
-------

`jsonflatten` was written by `Tim Phillips <phillipstr@gmail.com>`_.

Credits
-------
Brian Peterson `bpeterso2000 <https://github.com/bpeterso2000>`_, creator of JSON Transformations `<https://github.com/json-transformations>`_
