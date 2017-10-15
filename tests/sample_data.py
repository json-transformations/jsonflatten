"""Sample data used in various testing modules."""

from jsoncut.treecrawler import Node


##############################################################################
# SAMPLE Weather Forecast API data
##############################################################################

FORECAST = {
    'city': 'jacksonville',
    'date': '2017-09-15',
    'status_code': 200,
    'jacket_weather': False,
    'sunscreen_required': True,
    'sunspot_activity': None,
    'coord': {
        'lat': 30.332,
        'lon': -81.655,
    },
    'forecast': [{
        'day': 'Monday',
        'temp': {
            'hi': 80,
            'low': 70,
        },
        'wind': {
            'mph': 12,
            'direction': 'ENE',
        },
    }, {
        'day': 'Tuesday',
        'temp': {
            'hi': 82,
            'low': 71,
        },
        'wind': {
            'mph': 13,
            'direction': 'S',
        },
    },
    ]
}

FORECAST_FLAT = {
    'city': 'jacksonville',
    'date': '2017-09-15',
    'status_code': 200,
    'coord.lat': 30.332,
    'coord.lon': -81.655,
    'jacket_weather': False,
    'sunscreen_required': True,
    'sunspot_activity': None,
    'forecast': [{
        'day': 'Monday',
        'temp.hi': 80,
        'temp.low': 70,
        'wind.mph': 12,
        'wind.direction': 'ENE'
    }, {
        'day': 'Tuesday',
        'temp.hi': 82,
        'temp.low': 71,
        'wind.mph': 13,
        'wind.direction': 'S'
    },
    ]
}

FORECAST_ROWS = [
    {'city': 'jacksonville',
     'coord.lat': 30.332,
     'coord.lon': -81.655,
     'day': 'Monday',
     'temp.hi': 80,
     'temp.low': 70,
     'wind.mph': 12,
     'wind.direction': 'ENE'},
    {'city': 'jacksonville',
     'coord.lat': 30.332,
     'coord.lon': -81.655,
     'day': 'Tuesday',
     'temp.hi': 82,
     'temp.low': 71,
     'wind.mph': 13,
     'wind.direction': 'S'},
]

FORECAST_NODES_MAPPING = [
    Node(path='.city', obj='jacksonville'),
    Node(path='.date', obj='2017-09-15'),
    Node(path='.status_code', obj=200),
    Node(path='.jacket_weather', obj=False),
    Node(path='.sunscreen_required', obj=True),
    Node(path='.sunspot_activity', obj=None),
    Node(path='.coord', obj={'lat': 30.332, 'lon': -81.655}),
    Node(path='.forecast', obj=[{'day': 'Monday', 'temp': {'hi': 80,
         'low': 70}, 'wind': {'mph': 12, 'direction': 'ENE'}}, {'day':
         'Tuesday', 'temp': {'hi': 82, 'low': 71}, 'wind': {'mph': 13,
         'direction': 'S'}}])]

FORECAST_NODES_SEQUENCE = [
    Node(path='.#', obj={'day': 'Monday', 'temp': {'hi': 80, 'low': 70},
        'wind': {'mph': 12, 'direction': 'ENE'}}),
    Node(path='.#', obj={'day': 'Tuesday', 'temp': {'hi': 82, 'low': 71},
        'wind': {'mph': 13, 'direction': 'S'}})]
