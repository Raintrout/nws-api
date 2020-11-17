# openapi-client
weather.gov API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https:////.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https:////.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weather.gov"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    area = 'area_example' # str | 

    try:
        api_instance.alerts_active_area_area_get(area)
    except ApiException as e:
        print("Exception when calling DefaultApi->alerts_active_area_area_get: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://api.weather.gov*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**alerts_active_area_area_get**](docs/DefaultApi.md#alerts_active_area_area_get) | **GET** /alerts/active/area/{area} | 
*DefaultApi* | [**alerts_active_count_get**](docs/DefaultApi.md#alerts_active_count_get) | **GET** /alerts/active/count | 
*DefaultApi* | [**alerts_active_get**](docs/DefaultApi.md#alerts_active_get) | **GET** /alerts/active | 
*DefaultApi* | [**alerts_active_region_region_get**](docs/DefaultApi.md#alerts_active_region_region_get) | **GET** /alerts/active/region/{region} | 
*DefaultApi* | [**alerts_active_zone_zone_id_get**](docs/DefaultApi.md#alerts_active_zone_zone_id_get) | **GET** /alerts/active/zone/{zoneId} | 
*DefaultApi* | [**alerts_get**](docs/DefaultApi.md#alerts_get) | **GET** /alerts | 
*DefaultApi* | [**alerts_id_get**](docs/DefaultApi.md#alerts_id_get) | **GET** /alerts/{id} | 
*DefaultApi* | [**alerts_types_get**](docs/DefaultApi.md#alerts_types_get) | **GET** /alerts/types | 
*DefaultApi* | [**glossary_get**](docs/DefaultApi.md#glossary_get) | **GET** /glossary | 
*DefaultApi* | [**gridpoints_wfo_xy_forecast_get**](docs/DefaultApi.md#gridpoints_wfo_xy_forecast_get) | **GET** /gridpoints/{wfo}/{x},{y}/forecast | 
*DefaultApi* | [**gridpoints_wfo_xy_forecast_hourly_get**](docs/DefaultApi.md#gridpoints_wfo_xy_forecast_hourly_get) | **GET** /gridpoints/{wfo}/{x},{y}/forecast/hourly | 
*DefaultApi* | [**gridpoints_wfo_xy_get**](docs/DefaultApi.md#gridpoints_wfo_xy_get) | **GET** /gridpoints/{wfo}/{x},{y} | 
*DefaultApi* | [**gridpoints_wfo_xy_stations_get**](docs/DefaultApi.md#gridpoints_wfo_xy_stations_get) | **GET** /gridpoints/{wfo}/{x},{y}/stations | 
*DefaultApi* | [**icons_get**](docs/DefaultApi.md#icons_get) | **GET** /icons | 
*DefaultApi* | [**icons_set_time_of_day_first_second_get**](docs/DefaultApi.md#icons_set_time_of_day_first_second_get) | **GET** /icons/{set}/{timeOfDay}/{first}/{second} | 
*DefaultApi* | [**offices_office_id_get**](docs/DefaultApi.md#offices_office_id_get) | **GET** /offices/{officeId} | 
*DefaultApi* | [**offices_office_id_headlines_get**](docs/DefaultApi.md#offices_office_id_headlines_get) | **GET** /offices/{officeId}/headlines | 
*DefaultApi* | [**offices_office_id_headlines_headline_id_get**](docs/DefaultApi.md#offices_office_id_headlines_headline_id_get) | **GET** /offices/{officeId}/headlines/{headlineId} | 
*DefaultApi* | [**points_point_forecast_get**](docs/DefaultApi.md#points_point_forecast_get) | **GET** /points/{point}/forecast | 
*DefaultApi* | [**points_point_forecast_hourly_get**](docs/DefaultApi.md#points_point_forecast_hourly_get) | **GET** /points/{point}/forecast/hourly | 
*DefaultApi* | [**points_point_get**](docs/DefaultApi.md#points_point_get) | **GET** /points/{point} | 
*DefaultApi* | [**points_point_stations_get**](docs/DefaultApi.md#points_point_stations_get) | **GET** /points/{point}/stations | 
*DefaultApi* | [**products_get**](docs/DefaultApi.md#products_get) | **GET** /products | 
*DefaultApi* | [**products_locations_get**](docs/DefaultApi.md#products_locations_get) | **GET** /products/locations | 
*DefaultApi* | [**products_locations_location_id_types_get**](docs/DefaultApi.md#products_locations_location_id_types_get) | **GET** /products/locations/{locationId}/types | 
*DefaultApi* | [**products_product_id_get**](docs/DefaultApi.md#products_product_id_get) | **GET** /products/{productId} | 
*DefaultApi* | [**products_types_get**](docs/DefaultApi.md#products_types_get) | **GET** /products/types | 
*DefaultApi* | [**products_types_type_id_get**](docs/DefaultApi.md#products_types_type_id_get) | **GET** /products/types/{typeId} | 
*DefaultApi* | [**products_types_type_id_locations_get**](docs/DefaultApi.md#products_types_type_id_locations_get) | **GET** /products/types/{typeId}/locations | 
*DefaultApi* | [**products_types_type_id_locations_location_id_get**](docs/DefaultApi.md#products_types_type_id_locations_location_id_get) | **GET** /products/types/{typeId}/locations/{locationId} | 
*DefaultApi* | [**radar_profilers_station_id_get**](docs/DefaultApi.md#radar_profilers_station_id_get) | **GET** /radar/profilers/{stationId} | 
*DefaultApi* | [**radar_queues_host_get**](docs/DefaultApi.md#radar_queues_host_get) | **GET** /radar/queues/{host} | 
*DefaultApi* | [**radar_servers_get**](docs/DefaultApi.md#radar_servers_get) | **GET** /radar/servers | 
*DefaultApi* | [**radar_servers_id_get**](docs/DefaultApi.md#radar_servers_id_get) | **GET** /radar/servers/{id} | 
*DefaultApi* | [**radar_stations_get**](docs/DefaultApi.md#radar_stations_get) | **GET** /radar/stations | 
*DefaultApi* | [**radar_stations_station_id_alarms_get**](docs/DefaultApi.md#radar_stations_station_id_alarms_get) | **GET** /radar/stations/{stationId}/alarms | 
*DefaultApi* | [**radar_stations_station_id_get**](docs/DefaultApi.md#radar_stations_station_id_get) | **GET** /radar/stations/{stationId} | 
*DefaultApi* | [**stations_get**](docs/DefaultApi.md#stations_get) | **GET** /stations | 
*DefaultApi* | [**stations_station_id_get**](docs/DefaultApi.md#stations_station_id_get) | **GET** /stations/{stationId} | 
*DefaultApi* | [**stations_station_id_observations_current_get**](docs/DefaultApi.md#stations_station_id_observations_current_get) | **GET** /stations/{stationId}/observations/current | 
*DefaultApi* | [**stations_station_id_observations_get**](docs/DefaultApi.md#stations_station_id_observations_get) | **GET** /stations/{stationId}/observations | 
*DefaultApi* | [**stations_station_id_observations_latest_get**](docs/DefaultApi.md#stations_station_id_observations_latest_get) | **GET** /stations/{stationId}/observations/latest | 
*DefaultApi* | [**stations_station_id_observations_time_get**](docs/DefaultApi.md#stations_station_id_observations_time_get) | **GET** /stations/{stationId}/observations/{time} | 
*DefaultApi* | [**thumbnails_satellite_area_get**](docs/DefaultApi.md#thumbnails_satellite_area_get) | **GET** /thumbnails/satellite/{area} | 
*DefaultApi* | [**zones_forecast_zone_id_observations_get**](docs/DefaultApi.md#zones_forecast_zone_id_observations_get) | **GET** /zones/forecast/{zoneId}/observations | 
*DefaultApi* | [**zones_forecast_zone_id_stations_get**](docs/DefaultApi.md#zones_forecast_zone_id_stations_get) | **GET** /zones/forecast/{zoneId}/stations | 
*DefaultApi* | [**zones_get**](docs/DefaultApi.md#zones_get) | **GET** /zones | 
*DefaultApi* | [**zones_type_get**](docs/DefaultApi.md#zones_type_get) | **GET** /zones/{type} | 
*DefaultApi* | [**zones_type_zone_id_forecast_get**](docs/DefaultApi.md#zones_type_zone_id_forecast_get) | **GET** /zones/{type}/{zoneId}/forecast | 
*DefaultApi* | [**zones_type_zone_id_get**](docs/DefaultApi.md#zones_type_zone_id_get) | **GET** /zones/{type}/{zoneId} | 


## Documentation For Models

 - [Error](docs/Error.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




