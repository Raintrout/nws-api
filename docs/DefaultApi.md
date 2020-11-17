# openapi_client.DefaultApi

All URIs are relative to *https://api.weather.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alerts_active_area_area_get**](DefaultApi.md#alerts_active_area_area_get) | **GET** /alerts/active/area/{area} | 
[**alerts_active_count_get**](DefaultApi.md#alerts_active_count_get) | **GET** /alerts/active/count | 
[**alerts_active_get**](DefaultApi.md#alerts_active_get) | **GET** /alerts/active | 
[**alerts_active_region_region_get**](DefaultApi.md#alerts_active_region_region_get) | **GET** /alerts/active/region/{region} | 
[**alerts_active_zone_zone_id_get**](DefaultApi.md#alerts_active_zone_zone_id_get) | **GET** /alerts/active/zone/{zoneId} | 
[**alerts_get**](DefaultApi.md#alerts_get) | **GET** /alerts | 
[**alerts_id_get**](DefaultApi.md#alerts_id_get) | **GET** /alerts/{id} | 
[**alerts_types_get**](DefaultApi.md#alerts_types_get) | **GET** /alerts/types | 
[**glossary_get**](DefaultApi.md#glossary_get) | **GET** /glossary | 
[**gridpoints_wfo_xy_forecast_get**](DefaultApi.md#gridpoints_wfo_xy_forecast_get) | **GET** /gridpoints/{wfo}/{x},{y}/forecast | 
[**gridpoints_wfo_xy_forecast_hourly_get**](DefaultApi.md#gridpoints_wfo_xy_forecast_hourly_get) | **GET** /gridpoints/{wfo}/{x},{y}/forecast/hourly | 
[**gridpoints_wfo_xy_get**](DefaultApi.md#gridpoints_wfo_xy_get) | **GET** /gridpoints/{wfo}/{x},{y} | 
[**gridpoints_wfo_xy_stations_get**](DefaultApi.md#gridpoints_wfo_xy_stations_get) | **GET** /gridpoints/{wfo}/{x},{y}/stations | 
[**icons_get**](DefaultApi.md#icons_get) | **GET** /icons | 
[**icons_set_time_of_day_first_second_get**](DefaultApi.md#icons_set_time_of_day_first_second_get) | **GET** /icons/{set}/{timeOfDay}/{first}/{second} | 
[**offices_office_id_get**](DefaultApi.md#offices_office_id_get) | **GET** /offices/{officeId} | 
[**offices_office_id_headlines_get**](DefaultApi.md#offices_office_id_headlines_get) | **GET** /offices/{officeId}/headlines | 
[**offices_office_id_headlines_headline_id_get**](DefaultApi.md#offices_office_id_headlines_headline_id_get) | **GET** /offices/{officeId}/headlines/{headlineId} | 
[**points_point_forecast_get**](DefaultApi.md#points_point_forecast_get) | **GET** /points/{point}/forecast | 
[**points_point_forecast_hourly_get**](DefaultApi.md#points_point_forecast_hourly_get) | **GET** /points/{point}/forecast/hourly | 
[**points_point_get**](DefaultApi.md#points_point_get) | **GET** /points/{point} | 
[**points_point_stations_get**](DefaultApi.md#points_point_stations_get) | **GET** /points/{point}/stations | 
[**products_get**](DefaultApi.md#products_get) | **GET** /products | 
[**products_locations_get**](DefaultApi.md#products_locations_get) | **GET** /products/locations | 
[**products_locations_location_id_types_get**](DefaultApi.md#products_locations_location_id_types_get) | **GET** /products/locations/{locationId}/types | 
[**products_product_id_get**](DefaultApi.md#products_product_id_get) | **GET** /products/{productId} | 
[**products_types_get**](DefaultApi.md#products_types_get) | **GET** /products/types | 
[**products_types_type_id_get**](DefaultApi.md#products_types_type_id_get) | **GET** /products/types/{typeId} | 
[**products_types_type_id_locations_get**](DefaultApi.md#products_types_type_id_locations_get) | **GET** /products/types/{typeId}/locations | 
[**products_types_type_id_locations_location_id_get**](DefaultApi.md#products_types_type_id_locations_location_id_get) | **GET** /products/types/{typeId}/locations/{locationId} | 
[**radar_profilers_station_id_get**](DefaultApi.md#radar_profilers_station_id_get) | **GET** /radar/profilers/{stationId} | 
[**radar_queues_host_get**](DefaultApi.md#radar_queues_host_get) | **GET** /radar/queues/{host} | 
[**radar_servers_get**](DefaultApi.md#radar_servers_get) | **GET** /radar/servers | 
[**radar_servers_id_get**](DefaultApi.md#radar_servers_id_get) | **GET** /radar/servers/{id} | 
[**radar_stations_get**](DefaultApi.md#radar_stations_get) | **GET** /radar/stations | 
[**radar_stations_station_id_alarms_get**](DefaultApi.md#radar_stations_station_id_alarms_get) | **GET** /radar/stations/{stationId}/alarms | 
[**radar_stations_station_id_get**](DefaultApi.md#radar_stations_station_id_get) | **GET** /radar/stations/{stationId} | 
[**stations_get**](DefaultApi.md#stations_get) | **GET** /stations | 
[**stations_station_id_get**](DefaultApi.md#stations_station_id_get) | **GET** /stations/{stationId} | 
[**stations_station_id_observations_current_get**](DefaultApi.md#stations_station_id_observations_current_get) | **GET** /stations/{stationId}/observations/current | 
[**stations_station_id_observations_get**](DefaultApi.md#stations_station_id_observations_get) | **GET** /stations/{stationId}/observations | 
[**stations_station_id_observations_latest_get**](DefaultApi.md#stations_station_id_observations_latest_get) | **GET** /stations/{stationId}/observations/latest | 
[**stations_station_id_observations_time_get**](DefaultApi.md#stations_station_id_observations_time_get) | **GET** /stations/{stationId}/observations/{time} | 
[**thumbnails_satellite_area_get**](DefaultApi.md#thumbnails_satellite_area_get) | **GET** /thumbnails/satellite/{area} | 
[**zones_forecast_zone_id_observations_get**](DefaultApi.md#zones_forecast_zone_id_observations_get) | **GET** /zones/forecast/{zoneId}/observations | 
[**zones_forecast_zone_id_stations_get**](DefaultApi.md#zones_forecast_zone_id_stations_get) | **GET** /zones/forecast/{zoneId}/stations | 
[**zones_get**](DefaultApi.md#zones_get) | **GET** /zones | 
[**zones_type_get**](DefaultApi.md#zones_type_get) | **GET** /zones/{type} | 
[**zones_type_zone_id_forecast_get**](DefaultApi.md#zones_type_zone_id_forecast_get) | **GET** /zones/{type}/{zoneId}/forecast | 
[**zones_type_zone_id_get**](DefaultApi.md#zones_type_zone_id_get) | **GET** /zones/{type}/{zoneId} | 


# **alerts_active_area_area_get**
> alerts_active_area_area_get(area)



Returns active alerts for the given area (state or marine area)

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    area = 'area_example' # str | 

    try:
        api_instance.alerts_active_area_area_get(area)
    except ApiException as e:
        print("Exception when calling DefaultApi->alerts_active_area_area_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/atom+xml, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_active_count_get**
> alerts_active_count_get()



Returns info on the number of active alerts

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    
    try:
        api_instance.alerts_active_count_get()
    except ApiException as e:
        print("Exception when calling DefaultApi->alerts_active_count_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_active_get**
> alerts_active_get(status=status, message_type=message_type, event=event, code=code, region_type=region_type, point=point, region=region, area=area, zone=zone, urgency=urgency, severity=severity, certainty=certainty, limit=limit)



Returns all currently active alerts

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    status = ['status_example'] # list[str] | Status (actual, exercise, system, test, draft) (optional)
message_type = ['message_type_example'] # list[str] | Message type (alert, update, cancel) (optional)
event = ['event_example'] # list[str] | Event name (optional)
code = ['code_example'] # list[str] | Event code (optional)
region_type = 'region_type_example' # str | Region type (land or marine)  This parameter is incompatible with the following parameters: area, point, region, zone (optional)
point = 'point_example' # str | Point (latitude,longitude)  This parameter is incompatible with the following parameters: area, region, region_type, zone (optional)
region = ['region_example'] # list[str] | Marine region code  This parameter is incompatible with the following parameters: area, point, region_type, zone (optional)
area = ['area_example'] # list[str] | State/marine area code  This parameter is incompatible with the following parameters: point, region, region_type, zone (optional)
zone = ['zone_example'] # list[str] | Zone ID (forecast or county)  This parameter is incompatible with the following parameters: area, point, region, region_type (optional)
urgency = ['urgency_example'] # list[str] | Urgency (immediate, expected, future, past, unknown) (optional)
severity = ['severity_example'] # list[str] | Severity (extreme, severe, moderate, minor, unknown) (optional)
certainty = ['certainty_example'] # list[str] | Certainty (observed, likely, possible, unlikely, unknown) (optional)
limit = 56 # int | Limit (optional)

    try:
        api_instance.alerts_active_get(status=status, message_type=message_type, event=event, code=code, region_type=region_type, point=point, region=region, area=area, zone=zone, urgency=urgency, severity=severity, certainty=certainty, limit=limit)
    except ApiException as e:
        print("Exception when calling DefaultApi->alerts_active_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**list[str]**](str.md)| Status (actual, exercise, system, test, draft) | [optional] 
 **message_type** | [**list[str]**](str.md)| Message type (alert, update, cancel) | [optional] 
 **event** | [**list[str]**](str.md)| Event name | [optional] 
 **code** | [**list[str]**](str.md)| Event code | [optional] 
 **region_type** | **str**| Region type (land or marine)  This parameter is incompatible with the following parameters: area, point, region, zone | [optional] 
 **point** | **str**| Point (latitude,longitude)  This parameter is incompatible with the following parameters: area, region, region_type, zone | [optional] 
 **region** | [**list[str]**](str.md)| Marine region code  This parameter is incompatible with the following parameters: area, point, region_type, zone | [optional] 
 **area** | [**list[str]**](str.md)| State/marine area code  This parameter is incompatible with the following parameters: point, region, region_type, zone | [optional] 
 **zone** | [**list[str]**](str.md)| Zone ID (forecast or county)  This parameter is incompatible with the following parameters: area, point, region, region_type | [optional] 
 **urgency** | [**list[str]**](str.md)| Urgency (immediate, expected, future, past, unknown) | [optional] 
 **severity** | [**list[str]**](str.md)| Severity (extreme, severe, moderate, minor, unknown) | [optional] 
 **certainty** | [**list[str]**](str.md)| Certainty (observed, likely, possible, unlikely, unknown) | [optional] 
 **limit** | **int**| Limit | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/atom+xml, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_active_region_region_get**
> alerts_active_region_region_get(region)



Returns active alerts for the given marine region

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    region = 'region_example' # str | 

    try:
        api_instance.alerts_active_region_region_get(region)
    except ApiException as e:
        print("Exception when calling DefaultApi->alerts_active_region_region_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/atom+xml, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_active_zone_zone_id_get**
> alerts_active_zone_zone_id_get(zone_id)



Returns active alerts for the given zone

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    zone_id = 'zone_id_example' # str | 

    try:
        api_instance.alerts_active_zone_zone_id_get(zone_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->alerts_active_zone_zone_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/atom+xml, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_get**
> alerts_get(active=active, start=start, end=end, status=status, message_type=message_type, event=event, code=code, region_type=region_type, point=point, region=region, area=area, zone=zone, urgency=urgency, severity=severity, certainty=certainty, limit=limit, cursor=cursor)



Returns all alerts

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    active = True # bool | Active alerts (optional)
start = '2013-10-20T19:20:30+01:00' # datetime | Start time (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | End time (optional)
status = ['status_example'] # list[str] | Status (actual, exercise, system, test, draft) (optional)
message_type = ['message_type_example'] # list[str] | Message type (alert, update, cancel) (optional)
event = ['event_example'] # list[str] | Event name (optional)
code = ['code_example'] # list[str] | Event code (optional)
region_type = 'region_type_example' # str | Region type (land or marine)  This parameter is incompatible with the following parameters: area, point, region, zone (optional)
point = 'point_example' # str | Point (latitude,longitude)  This parameter is incompatible with the following parameters: area, region, region_type, zone (optional)
region = ['region_example'] # list[str] | Marine region code  This parameter is incompatible with the following parameters: area, point, region_type, zone (optional)
area = ['area_example'] # list[str] | State/marine area code  This parameter is incompatible with the following parameters: point, region, region_type, zone (optional)
zone = ['zone_example'] # list[str] | Zone ID (forecast or county)  This parameter is incompatible with the following parameters: area, point, region, region_type (optional)
urgency = ['urgency_example'] # list[str] | Urgency (immediate, expected, future, past, unknown) (optional)
severity = ['severity_example'] # list[str] | Severity (extreme, severe, moderate, minor, unknown) (optional)
certainty = ['certainty_example'] # list[str] | Certainty (observed, likely, possible, unlikely, unknown) (optional)
limit = 56 # int | Limit (optional)
cursor = 'cursor_example' # str | Pagination cursor (optional)

    try:
        api_instance.alerts_get(active=active, start=start, end=end, status=status, message_type=message_type, event=event, code=code, region_type=region_type, point=point, region=region, area=area, zone=zone, urgency=urgency, severity=severity, certainty=certainty, limit=limit, cursor=cursor)
    except ApiException as e:
        print("Exception when calling DefaultApi->alerts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**| Active alerts | [optional] 
 **start** | **datetime**| Start time | [optional] 
 **end** | **datetime**| End time | [optional] 
 **status** | [**list[str]**](str.md)| Status (actual, exercise, system, test, draft) | [optional] 
 **message_type** | [**list[str]**](str.md)| Message type (alert, update, cancel) | [optional] 
 **event** | [**list[str]**](str.md)| Event name | [optional] 
 **code** | [**list[str]**](str.md)| Event code | [optional] 
 **region_type** | **str**| Region type (land or marine)  This parameter is incompatible with the following parameters: area, point, region, zone | [optional] 
 **point** | **str**| Point (latitude,longitude)  This parameter is incompatible with the following parameters: area, region, region_type, zone | [optional] 
 **region** | [**list[str]**](str.md)| Marine region code  This parameter is incompatible with the following parameters: area, point, region_type, zone | [optional] 
 **area** | [**list[str]**](str.md)| State/marine area code  This parameter is incompatible with the following parameters: point, region, region_type, zone | [optional] 
 **zone** | [**list[str]**](str.md)| Zone ID (forecast or county)  This parameter is incompatible with the following parameters: area, point, region, region_type | [optional] 
 **urgency** | [**list[str]**](str.md)| Urgency (immediate, expected, future, past, unknown) | [optional] 
 **severity** | [**list[str]**](str.md)| Severity (extreme, severe, moderate, minor, unknown) | [optional] 
 **certainty** | [**list[str]**](str.md)| Certainty (observed, likely, possible, unlikely, unknown) | [optional] 
 **limit** | **int**| Limit | [optional] 
 **cursor** | **str**| Pagination cursor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/atom+xml, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_id_get**
> alerts_id_get(id)



Returns a specific alert

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.alerts_id_get(id)
    except ApiException as e:
        print("Exception when calling DefaultApi->alerts_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/cap+xml, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_types_get**
> alerts_types_get()



Returns a list of alert types

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    
    try:
        api_instance.alerts_types_get()
    except ApiException as e:
        print("Exception when calling DefaultApi->alerts_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **glossary_get**
> glossary_get()



Returns glossary terms

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    
    try:
        api_instance.glossary_get()
    except ApiException as e:
        print("Exception when calling DefaultApi->glossary_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gridpoints_wfo_xy_forecast_get**
> gridpoints_wfo_xy_forecast_get(wfo, x, y, feature_flags=feature_flags, units=units)



Returns a textual forecast for a 2.5km grid area

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    wfo = 'wfo_example' # str | 
x = 56 # int | 
y = 56 # int | 
feature_flags = ['feature_flags_example'] # list[str] | Enable future and experimental features (see documentation for more info):  * forecast_temperature_qv: Represent temperature as QuantitativeValue * forecast_wind_speed_qv: Represent wind speed as QuantitativeValue (optional)
units = 'us' # str | Use US customary or SI (metric) units in textual output (optional) (default to 'us')

    try:
        api_instance.gridpoints_wfo_xy_forecast_get(wfo, x, y, feature_flags=feature_flags, units=units)
    except ApiException as e:
        print("Exception when calling DefaultApi->gridpoints_wfo_xy_forecast_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wfo** | **str**|  | 
 **x** | **int**|  | 
 **y** | **int**|  | 
 **feature_flags** | [**list[str]**](str.md)| Enable future and experimental features (see documentation for more info):  * forecast_temperature_qv: Represent temperature as QuantitativeValue * forecast_wind_speed_qv: Represent wind speed as QuantitativeValue | [optional] 
 **units** | **str**| Use US customary or SI (metric) units in textual output | [optional] [default to &#39;us&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/vnd.noaa.dwml+xml, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gridpoints_wfo_xy_forecast_hourly_get**
> gridpoints_wfo_xy_forecast_hourly_get(wfo, x, y, feature_flags=feature_flags, units=units)



Returns a textual hourly forecast for a 2.5km grid area

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    wfo = 'wfo_example' # str | 
x = 56 # int | 
y = 56 # int | 
feature_flags = ['feature_flags_example'] # list[str] | Enable future and experimental features (see documentation for more info):  * forecast_temperature_qv: Represent temperature as QuantitativeValue * forecast_wind_speed_qv: Represent wind speed as QuantitativeValue (optional)
units = 'us' # str | Use US customary or SI (metric) units in textual output (optional) (default to 'us')

    try:
        api_instance.gridpoints_wfo_xy_forecast_hourly_get(wfo, x, y, feature_flags=feature_flags, units=units)
    except ApiException as e:
        print("Exception when calling DefaultApi->gridpoints_wfo_xy_forecast_hourly_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wfo** | **str**|  | 
 **x** | **int**|  | 
 **y** | **int**|  | 
 **feature_flags** | [**list[str]**](str.md)| Enable future and experimental features (see documentation for more info):  * forecast_temperature_qv: Represent temperature as QuantitativeValue * forecast_wind_speed_qv: Represent wind speed as QuantitativeValue | [optional] 
 **units** | **str**| Use US customary or SI (metric) units in textual output | [optional] [default to &#39;us&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/vnd.noaa.dwml+xml, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gridpoints_wfo_xy_get**
> gridpoints_wfo_xy_get(wfo, x, y)



Returns raw numerical forecast data for a 2.5km grid area

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    wfo = 'wfo_example' # str | 
x = 56 # int | 
y = 56 # int | 

    try:
        api_instance.gridpoints_wfo_xy_get(wfo, x, y)
    except ApiException as e:
        print("Exception when calling DefaultApi->gridpoints_wfo_xy_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wfo** | **str**|  | 
 **x** | **int**|  | 
 **y** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gridpoints_wfo_xy_stations_get**
> gridpoints_wfo_xy_stations_get(wfo, x, y)



Returns a list of observation stations usable for a given 2.5km grid area

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    wfo = 'wfo_example' # str | 
x = 56 # int | 
y = 56 # int | 

    try:
        api_instance.gridpoints_wfo_xy_stations_get(wfo, x, y)
    except ApiException as e:
        print("Exception when calling DefaultApi->gridpoints_wfo_xy_stations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wfo** | **str**|  | 
 **x** | **int**|  | 
 **y** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **icons_get**
> icons_get()



Returns a list of icon codes and textual descriptions

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    
    try:
        api_instance.icons_get()
    except ApiException as e:
        print("Exception when calling DefaultApi->icons_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **icons_set_time_of_day_first_second_get**
> icons_set_time_of_day_first_second_get(set, time_of_day, first, second, size=size, fontsize=fontsize)



Returns a forecast icon

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    set = 'set_example' # str | 
time_of_day = 'time_of_day_example' # str | 
first = 'first_example' # str | 
second = 'second_example' # str | 
size = openapi_client.AnyOfstringinteger() # AnyOfstringinteger | Font size (optional)
fontsize = 56 # int | Font size (optional)

    try:
        api_instance.icons_set_time_of_day_first_second_get(set, time_of_day, first, second, size=size, fontsize=fontsize)
    except ApiException as e:
        print("Exception when calling DefaultApi->icons_set_time_of_day_first_second_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set** | **str**|  | 
 **time_of_day** | **str**|  | 
 **first** | **str**|  | 
 **second** | **str**|  | 
 **size** | [**AnyOfstringinteger**](.md)| Font size | [optional] 
 **fontsize** | **int**| Font size | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **offices_office_id_get**
> offices_office_id_get(office_id)



Returns metadata about a NWS forecast office

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    office_id = 'office_id_example' # str | 

    try:
        api_instance.offices_office_id_get(office_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->offices_office_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **offices_office_id_headlines_get**
> offices_office_id_headlines_get(office_id)



Returns a list of news headlines for a given NWS office

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    office_id = 'office_id_example' # str | 

    try:
        api_instance.offices_office_id_headlines_get(office_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->offices_office_id_headlines_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **offices_office_id_headlines_headline_id_get**
> offices_office_id_headlines_headline_id_get(office_id, headline_id)



Returns a specific news headline for a given NWS office

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    office_id = 'office_id_example' # str | 
headline_id = 'headline_id_example' # str | 

    try:
        api_instance.offices_office_id_headlines_headline_id_get(office_id, headline_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->offices_office_id_headlines_headline_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**|  | 
 **headline_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **points_point_forecast_get**
> points_point_forecast_get(point)



Returns a textual forecast for a given point

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    point = 'point_example' # str | 

    try:
        api_instance.points_point_forecast_get(point)
    except ApiException as e:
        print("Exception when calling DefaultApi->points_point_forecast_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/vnd.noaa.dwml+xml, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **points_point_forecast_hourly_get**
> points_point_forecast_hourly_get(point)



Returns a textual hourly forecast for a given point

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    point = 'point_example' # str | 

    try:
        api_instance.points_point_forecast_hourly_get(point)
    except ApiException as e:
        print("Exception when calling DefaultApi->points_point_forecast_hourly_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/vnd.noaa.dwml+xml, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **points_point_get**
> points_point_get(point)



Returns metadata about a given latitude/longitude point

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    point = 'point_example' # str | 

    try:
        api_instance.points_point_get(point)
    except ApiException as e:
        print("Exception when calling DefaultApi->points_point_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **points_point_stations_get**
> points_point_stations_get(point)



Returns a list of observation stations for a given point

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    point = 'point_example' # str | 

    try:
        api_instance.points_point_stations_get(point)
    except ApiException as e:
        print("Exception when calling DefaultApi->points_point_stations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_get**
> products_get(location=location, start=start, end=end, office=office, wmoid=wmoid, type=type, limit=limit)



Returns a list of text products

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    location = ['location_example'] # list[str] | Location id (optional)
start = '2013-10-20T19:20:30+01:00' # datetime | Start time (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | End time (optional)
office = ['office_example'] # list[str] | Issuing office (optional)
wmoid = ['wmoid_example'] # list[str] | WMO id code (optional)
type = ['type_example'] # list[str] | Product code (optional)
limit = 56 # int | Limit (optional)

    try:
        api_instance.products_get(location=location, start=start, end=end, office=office, wmoid=wmoid, type=type, limit=limit)
    except ApiException as e:
        print("Exception when calling DefaultApi->products_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | [**list[str]**](str.md)| Location id | [optional] 
 **start** | **datetime**| Start time | [optional] 
 **end** | **datetime**| End time | [optional] 
 **office** | [**list[str]**](str.md)| Issuing office | [optional] 
 **wmoid** | [**list[str]**](str.md)| WMO id code | [optional] 
 **type** | [**list[str]**](str.md)| Product code | [optional] 
 **limit** | **int**| Limit | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_locations_get**
> products_locations_get()



Returns a list of valid text product issuance locations

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    
    try:
        api_instance.products_locations_get()
    except ApiException as e:
        print("Exception when calling DefaultApi->products_locations_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_locations_location_id_types_get**
> products_locations_location_id_types_get(location_id)



Returns a list of valid text product types for a given issuance location

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    location_id = 'location_id_example' # str | 

    try:
        api_instance.products_locations_location_id_types_get(location_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->products_locations_location_id_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_get**
> products_product_id_get(product_id)



Returns a specific text product

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    product_id = 'product_id_example' # str | 

    try:
        api_instance.products_product_id_get(product_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->products_product_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_types_get**
> products_types_get()



Returns a list of valid text product types and codes

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    
    try:
        api_instance.products_types_get()
    except ApiException as e:
        print("Exception when calling DefaultApi->products_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_types_type_id_get**
> products_types_type_id_get(type_id)



Returns a list of text products of a given type

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    type_id = 'type_id_example' # str | 

    try:
        api_instance.products_types_type_id_get(type_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->products_types_type_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_types_type_id_locations_get**
> products_types_type_id_locations_get(type_id)



Returns a list of valid text product issuance locations for a given product type

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    type_id = 'type_id_example' # str | 

    try:
        api_instance.products_types_type_id_locations_get(type_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->products_types_type_id_locations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_types_type_id_locations_location_id_get**
> products_types_type_id_locations_location_id_get(type_id, location_id)



Returns a list of text products of a given type for a given issuance location

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    type_id = 'type_id_example' # str | 
location_id = 'location_id_example' # str | 

    try:
        api_instance.products_types_type_id_locations_location_id_get(type_id, location_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->products_types_type_id_locations_location_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**|  | 
 **location_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radar_profilers_station_id_get**
> radar_profilers_station_id_get(station_id, time=time, interval=interval)



Returns metadata about a given radar wind profiler

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    station_id = 'station_id_example' # str | 
time = 'time_example' # str | Time interval (optional)
interval = 'interval_example' # str | Averaging interval (optional)

    try:
        api_instance.radar_profilers_station_id_get(station_id, time=time, interval=interval)
    except ApiException as e:
        print("Exception when calling DefaultApi->radar_profilers_station_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**|  | 
 **time** | **str**| Time interval | [optional] 
 **interval** | **str**| Averaging interval | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radar_queues_host_get**
> radar_queues_host_get(host, limit=limit, arrived=arrived, created=created, published=published, station=station, type=type, feed=feed, resolution=resolution)



Returns metadata about a given radar queue

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    host = 'host_example' # str | 
limit = 56 # int | Record limit (optional)
arrived = 'arrived_example' # str | Range for arrival time (optional)
created = 'created_example' # str | Range for creation time (optional)
published = 'published_example' # str | Range for publish time (optional)
station = 'station_example' # str | Station identifier (optional)
type = 'type_example' # str | Record type (optional)
feed = 'feed_example' # str | Originating product feed (optional)
resolution = 56 # int | Resolution version (optional)

    try:
        api_instance.radar_queues_host_get(host, limit=limit, arrived=arrived, created=created, published=published, station=station, type=type, feed=feed, resolution=resolution)
    except ApiException as e:
        print("Exception when calling DefaultApi->radar_queues_host_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**|  | 
 **limit** | **int**| Record limit | [optional] 
 **arrived** | **str**| Range for arrival time | [optional] 
 **created** | **str**| Range for creation time | [optional] 
 **published** | **str**| Range for publish time | [optional] 
 **station** | **str**| Station identifier | [optional] 
 **type** | **str**| Record type | [optional] 
 **feed** | **str**| Originating product feed | [optional] 
 **resolution** | **int**| Resolution version | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radar_servers_get**
> radar_servers_get(reporting_host=reporting_host)



Returns a list of radar servers

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    reporting_host = 'reporting_host_example' # str | Show records from specific reporting host (optional)

    try:
        api_instance.radar_servers_get(reporting_host=reporting_host)
    except ApiException as e:
        print("Exception when calling DefaultApi->radar_servers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reporting_host** | **str**| Show records from specific reporting host | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radar_servers_id_get**
> radar_servers_id_get(id, reporting_host=reporting_host)



Returns metadata about a given radar server

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 'id_example' # str | 
reporting_host = 'reporting_host_example' # str | Show records from specific reporting host (optional)

    try:
        api_instance.radar_servers_id_get(id, reporting_host=reporting_host)
    except ApiException as e:
        print("Exception when calling DefaultApi->radar_servers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **reporting_host** | **str**| Show records from specific reporting host | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radar_stations_get**
> radar_stations_get(station_type=station_type, reporting_host=reporting_host, host=host)



Returns a list of radar stations

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    station_type = ['station_type_example'] # list[str] | Limit results to a specific station type or types (optional)
reporting_host = 'reporting_host_example' # str | Show RDA and latency info from specific reporting host (optional)
host = 'host_example' # str | Show latency info from specific LDM host (optional)

    try:
        api_instance.radar_stations_get(station_type=station_type, reporting_host=reporting_host, host=host)
    except ApiException as e:
        print("Exception when calling DefaultApi->radar_stations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_type** | [**list[str]**](str.md)| Limit results to a specific station type or types | [optional] 
 **reporting_host** | **str**| Show RDA and latency info from specific reporting host | [optional] 
 **host** | **str**| Show latency info from specific LDM host | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radar_stations_station_id_alarms_get**
> radar_stations_station_id_alarms_get(station_id)



Returns metadata about a given radar station alarms

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    station_id = 'station_id_example' # str | 

    try:
        api_instance.radar_stations_station_id_alarms_get(station_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->radar_stations_station_id_alarms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radar_stations_station_id_get**
> radar_stations_station_id_get(station_id, reporting_host=reporting_host, host=host)



Returns metadata about a given radar station

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    station_id = 'station_id_example' # str | 
reporting_host = 'reporting_host_example' # str | Show RDA and latency info from specific reporting host (optional)
host = 'host_example' # str | Show latency info from specific LDM host (optional)

    try:
        api_instance.radar_stations_station_id_get(station_id, reporting_host=reporting_host, host=host)
    except ApiException as e:
        print("Exception when calling DefaultApi->radar_stations_station_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**|  | 
 **reporting_host** | **str**| Show RDA and latency info from specific reporting host | [optional] 
 **host** | **str**| Show latency info from specific LDM host | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stations_get**
> stations_get(id=id, state=state, limit=limit)



Returns a list of observation stations

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = ['id_example'] # list[str] | State abbreviation (optional)
state = ['state_example'] # list[str] | State/marine area code (optional)
limit = 56 # int | Limit (optional)

    try:
        api_instance.stations_get(id=id, state=state, limit=limit)
    except ApiException as e:
        print("Exception when calling DefaultApi->stations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| State abbreviation | [optional] 
 **state** | [**list[str]**](str.md)| State/marine area code | [optional] 
 **limit** | **int**| Limit | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stations_station_id_get**
> stations_station_id_get(station_id)



Returns metadata about a given observation station

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    station_id = 'station_id_example' # str | 

    try:
        api_instance.stations_station_id_get(station_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->stations_station_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stations_station_id_observations_current_get**
> stations_station_id_observations_current_get(station_id, require_qc=require_qc)



Returns the latest observation for a station (use '/latest' instead)

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    station_id = 'station_id_example' # str | 
require_qc = True # bool | Require QC (optional)

    try:
        api_instance.stations_station_id_observations_current_get(station_id, require_qc=require_qc)
    except ApiException as e:
        print("Exception when calling DefaultApi->stations_station_id_observations_current_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**|  | 
 **require_qc** | **bool**| Require QC | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/vnd.noaa.obs+xml, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stations_station_id_observations_get**
> stations_station_id_observations_get(station_id, station=station, start=start, end=end, limit=limit)



Returns a list of observations for a given station

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    station_id = 'station_id_example' # str | 
station = ['station_example'] # list[str] | Station ID (optional)
start = '2013-10-20T19:20:30+01:00' # datetime | Start date/time (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | End date/time (optional)
limit = 56 # int | Limit (optional)

    try:
        api_instance.stations_station_id_observations_get(station_id, station=station, start=start, end=end, limit=limit)
    except ApiException as e:
        print("Exception when calling DefaultApi->stations_station_id_observations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**|  | 
 **station** | [**list[str]**](str.md)| Station ID | [optional] 
 **start** | **datetime**| Start date/time | [optional] 
 **end** | **datetime**| End date/time | [optional] 
 **limit** | **int**| Limit | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stations_station_id_observations_latest_get**
> stations_station_id_observations_latest_get(station_id, require_qc=require_qc)



Returns the latest observation for a station

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    station_id = 'station_id_example' # str | 
require_qc = True # bool | Require QC (optional)

    try:
        api_instance.stations_station_id_observations_latest_get(station_id, require_qc=require_qc)
    except ApiException as e:
        print("Exception when calling DefaultApi->stations_station_id_observations_latest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**|  | 
 **require_qc** | **bool**| Require QC | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/vnd.noaa.obs+xml, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stations_station_id_observations_time_get**
> stations_station_id_observations_time_get(station_id, time)



Returns a single observation

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    station_id = 'station_id_example' # str | 
time = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        api_instance.stations_station_id_observations_time_get(station_id, time)
    except ApiException as e:
        print("Exception when calling DefaultApi->stations_station_id_observations_time_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**|  | 
 **time** | **datetime**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **thumbnails_satellite_area_get**
> thumbnails_satellite_area_get(area)



Returns a thumbnail image for a satellite region

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    area = 'area_example' # str | 

    try:
        api_instance.thumbnails_satellite_area_get(area)
    except ApiException as e:
        print("Exception when calling DefaultApi->thumbnails_satellite_area_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_forecast_zone_id_observations_get**
> zones_forecast_zone_id_observations_get(zone_id, start=start, end=end, limit=limit)



Returns a list of observations for a given zone

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    zone_id = 'zone_id_example' # str | 
start = '2013-10-20T19:20:30+01:00' # datetime | Start date/time (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | End date/time (optional)
limit = 56 # int | Limit (optional)

    try:
        api_instance.zones_forecast_zone_id_observations_get(zone_id, start=start, end=end, limit=limit)
    except ApiException as e:
        print("Exception when calling DefaultApi->zones_forecast_zone_id_observations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 
 **start** | **datetime**| Start date/time | [optional] 
 **end** | **datetime**| End date/time | [optional] 
 **limit** | **int**| Limit | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_forecast_zone_id_stations_get**
> zones_forecast_zone_id_stations_get(zone_id)



Returns a list of observation stations for a given zone

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    zone_id = 'zone_id_example' # str | 

    try:
        api_instance.zones_forecast_zone_id_stations_get(zone_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->zones_forecast_zone_id_stations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_get**
> zones_get(id=id, area=area, region=region, type=type, point=point, include_geometry=include_geometry, limit=limit, effective=effective)



Returns a list of zones

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = ['id_example'] # list[str] | Zone ID (forecast or county) (optional)
area = ['area_example'] # list[str] | State/marine area code (optional)
region = ['region_example'] # list[str] | Region code (optional)
type = ['type_example'] # list[str] | Zone type (optional)
point = 'point_example' # str | Point (latitude,longitude) (optional)
include_geometry = True # bool | Include geometry in results (true/false) (optional)
limit = 56 # int | Limit (optional)
effective = '2013-10-20T19:20:30+01:00' # datetime | Effective date/time (optional)

    try:
        api_instance.zones_get(id=id, area=area, region=region, type=type, point=point, include_geometry=include_geometry, limit=limit, effective=effective)
    except ApiException as e:
        print("Exception when calling DefaultApi->zones_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| Zone ID (forecast or county) | [optional] 
 **area** | [**list[str]**](str.md)| State/marine area code | [optional] 
 **region** | [**list[str]**](str.md)| Region code | [optional] 
 **type** | [**list[str]**](str.md)| Zone type | [optional] 
 **point** | **str**| Point (latitude,longitude) | [optional] 
 **include_geometry** | **bool**| Include geometry in results (true/false) | [optional] 
 **limit** | **int**| Limit | [optional] 
 **effective** | **datetime**| Effective date/time | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_type_get**
> zones_type_get(type, id=id, area=area, region=region, type2=type2, point=point, include_geometry=include_geometry, limit=limit, effective=effective)



Returns a list of zones of a given type

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    type = 'type_example' # str | 
id = ['id_example'] # list[str] | Zone ID (forecast or county) (optional)
area = ['area_example'] # list[str] | State/marine area code (optional)
region = ['region_example'] # list[str] | Region code (optional)
type2 = ['type_example'] # list[str] | Zone type (optional)
point = 'point_example' # str | Point (latitude,longitude) (optional)
include_geometry = True # bool | Include geometry in results (true/false) (optional)
limit = 56 # int | Limit (optional)
effective = '2013-10-20T19:20:30+01:00' # datetime | Effective date/time (optional)

    try:
        api_instance.zones_type_get(type, id=id, area=area, region=region, type2=type2, point=point, include_geometry=include_geometry, limit=limit, effective=effective)
    except ApiException as e:
        print("Exception when calling DefaultApi->zones_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | [**list[str]**](str.md)| Zone ID (forecast or county) | [optional] 
 **area** | [**list[str]**](str.md)| State/marine area code | [optional] 
 **region** | [**list[str]**](str.md)| Region code | [optional] 
 **type2** | [**list[str]**](str.md)| Zone type | [optional] 
 **point** | **str**| Point (latitude,longitude) | [optional] 
 **include_geometry** | **bool**| Include geometry in results (true/false) | [optional] 
 **limit** | **int**| Limit | [optional] 
 **effective** | **datetime**| Effective date/time | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_type_zone_id_forecast_get**
> zones_type_zone_id_forecast_get(type, zone_id)



Returns the current zone forecast for a given zone

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    type = 'type_example' # str | 
zone_id = 'zone_id_example' # str | 

    try:
        api_instance.zones_type_zone_id_forecast_get(type, zone_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->zones_type_zone_id_forecast_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **zone_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_type_zone_id_get**
> zones_type_zone_id_get(type, zone_id, effective=effective)



Returns metadata about a given zone

### Example

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
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    type = 'type_example' # str | 
zone_id = 'zone_id_example' # str | 
effective = '2013-10-20T19:20:30+01:00' # datetime | Effective date/time (optional)

    try:
        api_instance.zones_type_zone_id_get(type, zone_id, effective=effective)
    except ApiException as e:
        print("Exception when calling DefaultApi->zones_type_zone_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **zone_id** | **str**|  | 
 **effective** | **datetime**| Effective date/time | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

