# swagger_client.DefaultApi

All URIs are relative to *https://api.transport.nsw.gov.au/v1/tp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tfnsw_addinfo_request**](DefaultApi.md#tfnsw_addinfo_request) | **GET** /add_info | Provides capability to display all public transport service status and incident information (as published from the Service Alert Messaging System).
[**tfnsw_coord_request**](DefaultApi.md#tfnsw_coord_request) | **GET** /coord | When given a specific geographical location, this API finds public transport stops, stations, wharfs and points of interest around that location.
[**tfnsw_dm_request**](DefaultApi.md#tfnsw_dm_request) | **GET** /departure_mon | Provides capability to provide NSW public transport departure information from a stop, station or wharf including real-time.
[**tfnsw_stopfinder_request**](DefaultApi.md#tfnsw_stopfinder_request) | **GET** /stop_finder | Provides capability to return all NSW public transport stop, station, wharf, points of interest and known addresses to be used for auto-suggest/auto-complete (to be used with the Trip planner and Departure board APIs).
[**tfnsw_trip_request2**](DefaultApi.md#tfnsw_trip_request2) | **GET** /trip | Provides capability to provide NSW public transport trip plan options, including walking and driving legs and real-time information.


# **tfnsw_addinfo_request**
> AdditionalInfoResponse tfnsw_addinfo_request(output_format, filter_date_valid=filter_date_valid, filter_mot_type=filter_mot_type, filter_publication_status=filter_publication_status, itd_l_pxx_sel_stop=itd_l_pxx_sel_stop, itd_l_pxx_sel_line=itd_l_pxx_sel_line, itd_l_pxx_sel_operator=itd_l_pxx_sel_operator, filter_pn_line_dir=filter_pn_line_dir, filter_pn_line_sub=filter_pn_line_sub, version=version)

Provides capability to display all public transport service status and incident information (as published from the Service Alert Messaging System).

This endpoint returns a list of service alerts or additional information about travelling on the public transport network. This list can be filtered by date, route type, route, operator or stop. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
output_format = 'output_format_example' # str | Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the `outputFormat` value to `rapidJSON` is required to enable JSON output. 
filter_date_valid = '01-10-2016' # str | This parameter allows you to filter the returned items that are only valid on the specified date. The format of this field is `DD-MM-YYYY`. For example, 12 September 2016 would be represented by `12-09-2016`.  (optional) (default to 01-10-2016)
filter_mot_type = 56 # int | This parameter allows you to filter the returned items by the modes of transport they affected. Available modes include:  * `1`: Train * `2`: Metro * `4`: Light Rail * `5`: Bus * `7`: Coach * `9`: Ferry * `11`: School Bus  To search for more than one mode, include the parameter multiple times.  (optional)
filter_publication_status = 'filter_publication_status_example' # str | This field can be used so only current alerts are returned, and not historic alerts.  (optional)
itd_l_pxx_sel_stop = 'itd_l_pxx_sel_stop_example' # str | This parameter allows you to filter the returned items by its stop ID or global stop ID. For example, to retrieve items that are only relevant to Central Station, you would set this value to `10111010` (stop ID) or `200060` (global stop ID). You can use the `stop_finder` API call to determine the ID for a particular stop.  (optional)
itd_l_pxx_sel_line = 'itd_l_pxx_sel_line_example' # str | This parameter allows you to filter the returned items by line number. For example, `020T1`. You can use this parameter multiple times if you want to search for more than one line number.  (optional)
itd_l_pxx_sel_operator = 'itd_l_pxx_sel_operator_example' # str | This parameter allows you to filter the returned items by operator ID. You can use this parameter multiple times if you want to search for more than one line number.  (optional)
filter_pn_line_dir = 'filter_pn_line_dir_example' # str | This parameter allows you to filter the returned items by specific routes. The route is provided in the format `NNN:LLLLL:D`, (NNN: subnet, LLLLL: Route number, D: direction `H`/`R`). You can use this parameter multiple times if you want to search for more than one line number.  (optional)
filter_pn_line_sub = 'filter_pn_line_sub_example' # str | This parameter allows you to filter the returned items by specific routes. The route is provided in the format `NNN:LLLLL:E`, (NNN: subnet, LLLLL: Route number, E: supplement). You can use this parameter multiple times if you want to search for more than one line number.  (optional)
version = '10.2.1.42' # str | Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  (optional) (default to 10.2.1.42)

try:
    # Provides capability to display all public transport service status and incident information (as published from the Service Alert Messaging System).
    api_response = api_instance.tfnsw_addinfo_request(output_format, filter_date_valid=filter_date_valid, filter_mot_type=filter_mot_type, filter_publication_status=filter_publication_status, itd_l_pxx_sel_stop=itd_l_pxx_sel_stop, itd_l_pxx_sel_line=itd_l_pxx_sel_line, itd_l_pxx_sel_operator=itd_l_pxx_sel_operator, filter_pn_line_dir=filter_pn_line_dir, filter_pn_line_sub=filter_pn_line_sub, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tfnsw_addinfo_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_format** | **str**| Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the &#x60;outputFormat&#x60; value to &#x60;rapidJSON&#x60; is required to enable JSON output.  | 
 **filter_date_valid** | **str**| This parameter allows you to filter the returned items that are only valid on the specified date. The format of this field is &#x60;DD-MM-YYYY&#x60;. For example, 12 September 2016 would be represented by &#x60;12-09-2016&#x60;.  | [optional] [default to 01-10-2016]
 **filter_mot_type** | **int**| This parameter allows you to filter the returned items by the modes of transport they affected. Available modes include:  * &#x60;1&#x60;: Train * &#x60;2&#x60;: Metro * &#x60;4&#x60;: Light Rail * &#x60;5&#x60;: Bus * &#x60;7&#x60;: Coach * &#x60;9&#x60;: Ferry * &#x60;11&#x60;: School Bus  To search for more than one mode, include the parameter multiple times.  | [optional] 
 **filter_publication_status** | **str**| This field can be used so only current alerts are returned, and not historic alerts.  | [optional] 
 **itd_l_pxx_sel_stop** | **str**| This parameter allows you to filter the returned items by its stop ID or global stop ID. For example, to retrieve items that are only relevant to Central Station, you would set this value to &#x60;10111010&#x60; (stop ID) or &#x60;200060&#x60; (global stop ID). You can use the &#x60;stop_finder&#x60; API call to determine the ID for a particular stop.  | [optional] 
 **itd_l_pxx_sel_line** | **str**| This parameter allows you to filter the returned items by line number. For example, &#x60;020T1&#x60;. You can use this parameter multiple times if you want to search for more than one line number.  | [optional] 
 **itd_l_pxx_sel_operator** | **str**| This parameter allows you to filter the returned items by operator ID. You can use this parameter multiple times if you want to search for more than one line number.  | [optional] 
 **filter_pn_line_dir** | **str**| This parameter allows you to filter the returned items by specific routes. The route is provided in the format &#x60;NNN:LLLLL:D&#x60;, (NNN: subnet, LLLLL: Route number, D: direction &#x60;H&#x60;/&#x60;R&#x60;). You can use this parameter multiple times if you want to search for more than one line number.  | [optional] 
 **filter_pn_line_sub** | **str**| This parameter allows you to filter the returned items by specific routes. The route is provided in the format &#x60;NNN:LLLLL:E&#x60;, (NNN: subnet, LLLLL: Route number, E: supplement). You can use this parameter multiple times if you want to search for more than one line number.  | [optional] 
 **version** | **str**| Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  | [optional] [default to 10.2.1.42]

### Return type

[**AdditionalInfoResponse**](AdditionalInfoResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tfnsw_coord_request**
> CoordRequestResponse tfnsw_coord_request(output_format, coord, coord_output_format, incl_filter, type_1, radius_1, incl_draw_classes_1=incl_draw_classes_1, pois_on_map_macro=pois_on_map_macro, version=version)

When given a specific geographical location, this API finds public transport stops, stations, wharfs and points of interest around that location.

This endpoint returns places of interest based on the given coordinate and a radius. The types of POIs can be controlled, so if, for example, you only want Opal resellers returned, you can do so. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
output_format = 'output_format_example' # str | Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the `outputFormat` value to `rapidJSON` is required to enable JSON output. 
coord = '151.206290:-33.884080:EPSG:4326' # str | The coordinate is in the format `LONGITUDE:LATITUDE:EPSG:4326` (Note that longitude is first). For example, the following `coord` value can be used to search around Central Station: `151.206290:-33.884080:EPSG:4326`.  (default to 151.206290:-33.884080:EPSG:4326)
coord_output_format = 'coord_output_format_example' # str | This specifies the format the coordinates are returned in. While other variations are available, the `EPSG:4326` format will return the widely-used format. 
incl_filter = 1 # int | This enables \"advanced filter mode\" on the server, which is required to enable searching using coordinates.  (default to 1)
type_1 = 'GIS_POINT' # str | This specifies the type of items to return.  * `GIS_POINT`: GIS points, including Opal resellers (see `inclDrawClasses_1`) * `BUS_POINT`: Stops/stations * `POI_POINT`: Places of interest  The `_1` suffix is an index for this particular filter. You can specify multiple filters by incrementing the suffix for each combination of `type`, `radius` and `inclDrawClasses`. For example, `type_1` means the first filter, `type_2` refers to the second, and so on.  (default to GIS_POINT)
radius_1 = 1000 # int | This indicates the maximum number of metres to search in all directions from the location specified in `coord`. For example, if you use a value of `500`, a `type_1` value of `GIS_POINT` and `inclDrawClasses_1` with a value of `74`, all Opal resellers within 500 metres will be returned. The suffix of `_1` indicates this radius value corresponds to the `type_1` value. If multiple filters are to be included, the appropriate suffix should be updated accordingly.  (default to 1000)
incl_draw_classes_1 = 56 # int | This flag changes the list of POIs that are returned. To return Opal resellers, set this value to `74` and `type_1` to `GIS_POINT`.The suffix of `_1` indicates this radius value corresponds to the `type_1` value. If multiple filters are to be included, the appropriate suffix should be updated accordingly.  (optional)
pois_on_map_macro = 'true' # str | This field indicates how the returned data is to be used, which in turn impacts whether or not certain locations are returned.  (optional) (default to true)
version = '10.2.1.42' # str | Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  (optional) (default to 10.2.1.42)

try:
    # When given a specific geographical location, this API finds public transport stops, stations, wharfs and points of interest around that location.
    api_response = api_instance.tfnsw_coord_request(output_format, coord, coord_output_format, incl_filter, type_1, radius_1, incl_draw_classes_1=incl_draw_classes_1, pois_on_map_macro=pois_on_map_macro, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tfnsw_coord_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_format** | **str**| Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the &#x60;outputFormat&#x60; value to &#x60;rapidJSON&#x60; is required to enable JSON output.  | 
 **coord** | **str**| The coordinate is in the format &#x60;LONGITUDE:LATITUDE:EPSG:4326&#x60; (Note that longitude is first). For example, the following &#x60;coord&#x60; value can be used to search around Central Station: &#x60;151.206290:-33.884080:EPSG:4326&#x60;.  | [default to 151.206290:-33.884080:EPSG:4326]
 **coord_output_format** | **str**| This specifies the format the coordinates are returned in. While other variations are available, the &#x60;EPSG:4326&#x60; format will return the widely-used format.  | 
 **incl_filter** | **int**| This enables \&quot;advanced filter mode\&quot; on the server, which is required to enable searching using coordinates.  | [default to 1]
 **type_1** | **str**| This specifies the type of items to return.  * &#x60;GIS_POINT&#x60;: GIS points, including Opal resellers (see &#x60;inclDrawClasses_1&#x60;) * &#x60;BUS_POINT&#x60;: Stops/stations * &#x60;POI_POINT&#x60;: Places of interest  The &#x60;_1&#x60; suffix is an index for this particular filter. You can specify multiple filters by incrementing the suffix for each combination of &#x60;type&#x60;, &#x60;radius&#x60; and &#x60;inclDrawClasses&#x60;. For example, &#x60;type_1&#x60; means the first filter, &#x60;type_2&#x60; refers to the second, and so on.  | [default to GIS_POINT]
 **radius_1** | **int**| This indicates the maximum number of metres to search in all directions from the location specified in &#x60;coord&#x60;. For example, if you use a value of &#x60;500&#x60;, a &#x60;type_1&#x60; value of &#x60;GIS_POINT&#x60; and &#x60;inclDrawClasses_1&#x60; with a value of &#x60;74&#x60;, all Opal resellers within 500 metres will be returned. The suffix of &#x60;_1&#x60; indicates this radius value corresponds to the &#x60;type_1&#x60; value. If multiple filters are to be included, the appropriate suffix should be updated accordingly.  | [default to 1000]
 **incl_draw_classes_1** | **int**| This flag changes the list of POIs that are returned. To return Opal resellers, set this value to &#x60;74&#x60; and &#x60;type_1&#x60; to &#x60;GIS_POINT&#x60;.The suffix of &#x60;_1&#x60; indicates this radius value corresponds to the &#x60;type_1&#x60; value. If multiple filters are to be included, the appropriate suffix should be updated accordingly.  | [optional] 
 **pois_on_map_macro** | **str**| This field indicates how the returned data is to be used, which in turn impacts whether or not certain locations are returned.  | [optional] [default to true]
 **version** | **str**| Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  | [optional] [default to 10.2.1.42]

### Return type

[**CoordRequestResponse**](CoordRequestResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tfnsw_dm_request**
> DepartureMonitorResponse tfnsw_dm_request(output_format, coord_output_format, type_dm, name_dm, mode=mode, name_key_dm=name_key_dm, itd_date=itd_date, itd_time=itd_time, departure_monitor_macro=departure_monitor_macro, excluded_means=excluded_means, excl_mot_1=excl_mot_1, excl_mot_2=excl_mot_2, excl_mot_4=excl_mot_4, excl_mot_5=excl_mot_5, excl_mot_7=excl_mot_7, excl_mot_9=excl_mot_9, excl_mot_11=excl_mot_11, tf_nswdm=tf_nswdm, version=version)

Provides capability to provide NSW public transport departure information from a stop, station or wharf including real-time.

This endpoint returns a list of departures for a given location based on the date and time specified. This data can be used to display a \"upcoming departures\" board for a stop. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
output_format = 'output_format_example' # str | Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the `outputFormat` value to `rapidJSON` is required to enable JSON output. 
coord_output_format = 'coord_output_format_example' # str | This specifies the format the coordinates are returned in. While other variations are available, the `EPSG:4326` format will return the widely-used format.
type_dm = 'stop' # str | This specifies the type of results expected based on the search input in `name_dm`. By specifying `any`, locations of all types can be returned. Typically, this API call is used for a specific stop, so `stop` should be used along with a stop ID or global stop ID in `name_dm`.  (default to stop)
name_dm = '10111010' # str | This is the search term that will be used to find locations. If the combination of this value and `type_dm` results in more than one location found - or `mode` is not set to `direct`, then a list of stops and no departures will be returned. If `type_dm` is set to `stop` then this value can take a stop ID or a global stop ID.  (default to 10111010)
mode = 'direct' # str | This allows the departure board to display directly without going through the stop verification process. Use this when the stop is known. This relies on the given combination of `type_dm` and `name_dm` returning only a single result, otherwise a list of stops and no departures shall be returned.  (optional) (default to direct)
name_key_dm = 'name_key_dm_example' # str | Setting this parameter to `$USEPOINT$` enables you to request departures for a specific platform within a station. If this isn't used, then departures for all platforms at the stop specified in `name_dm` are returned.  (optional)
itd_date = '20161001' # str | The reference date used when searching trips, in `YYYYMMDD` format. For instance, 20160901 refers to 1 September 2016. Works in conjunction with the `itdTime` value. If not specified, the current server date is used.  (optional) (default to 20161001)
itd_time = '1200' # str | The reference time used when searching trips, in `HHMM` 24-hour format. For instance, 2215 refers to 10:15 PM. | Works in conjunction with the `itdDate` value. If not specified, the current server time is used.  (optional) (default to 1200)
departure_monitor_macro = 'true' # str | Including this parameter enables a number of options that result in the departure monitor operating in the same way as the Transport for NSW Trip Planner web site. It is recommended this is enabled, along with the `TfNSWDM` parameter.  (optional) (default to true)
excluded_means = 'excluded_means_example' # str | This parameter which means of transport to exclude from the departure monitor. To exclude one means, select one of the following: `1` = train, `2` = metro, `4` = light rail, `5` = bus, `7` = coach, `9` = ferry, `11` = school bus. `checkbox` allows you to exclude more than one means of transport when used in conjunction with the `exclMOT_<ID>` parameters.  (optional)
excl_mot_1 = 'excl_mot_1_example' # str | Excludes train services from the departure monitor.  Must be used in conjunction with `excludedMeans=checkbox`  (optional)
excl_mot_2 = 'excl_mot_2_example' # str | Excludes metro services from the departure monitor.  Must be used in conjunction with `excludedMeans=checkbox`  (optional)
excl_mot_4 = 'excl_mot_4_example' # str | Excludes light rail services from the departure monitor.  Must be used in conjunction with `excludedMeans=checkbox`  (optional)
excl_mot_5 = 'excl_mot_5_example' # str | Excludes bus services from the departure monitor.  Must be used in conjunction with `excludedMeans=checkbox`  (optional)
excl_mot_7 = 'excl_mot_7_example' # str | Excludes coach services from the departure monitor.  Must be used in conjunction with `excludedMeans=checkbox`  (optional)
excl_mot_9 = 'excl_mot_9_example' # str | Excludes ferry services from the departure monitor.  Must be used in conjunction with `excludedMeans=checkbox`  (optional)
excl_mot_11 = 'excl_mot_11_example' # str | Excludes school bus services from the departure monitor.  Must be used in conjunction with `excludedMeans=checkbox`  (optional)
tf_nswdm = 'true' # str | Including this parameter enables a number of options that result in the departure monitor operating in the same way as the Transport for NSW Trip Planner web site, including enabling real-time data. It is recommended this is enabled, along with the `departureMonitorMacro` parameter.  (optional) (default to true)
version = '10.2.1.42' # str | Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  (optional) (default to 10.2.1.42)

try:
    # Provides capability to provide NSW public transport departure information from a stop, station or wharf including real-time.
    api_response = api_instance.tfnsw_dm_request(output_format, coord_output_format, type_dm, name_dm, mode=mode, name_key_dm=name_key_dm, itd_date=itd_date, itd_time=itd_time, departure_monitor_macro=departure_monitor_macro, excluded_means=excluded_means, excl_mot_1=excl_mot_1, excl_mot_2=excl_mot_2, excl_mot_4=excl_mot_4, excl_mot_5=excl_mot_5, excl_mot_7=excl_mot_7, excl_mot_9=excl_mot_9, excl_mot_11=excl_mot_11, tf_nswdm=tf_nswdm, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tfnsw_dm_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_format** | **str**| Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the &#x60;outputFormat&#x60; value to &#x60;rapidJSON&#x60; is required to enable JSON output.  | 
 **coord_output_format** | **str**| This specifies the format the coordinates are returned in. While other variations are available, the &#x60;EPSG:4326&#x60; format will return the widely-used format. | 
 **type_dm** | **str**| This specifies the type of results expected based on the search input in &#x60;name_dm&#x60;. By specifying &#x60;any&#x60;, locations of all types can be returned. Typically, this API call is used for a specific stop, so &#x60;stop&#x60; should be used along with a stop ID or global stop ID in &#x60;name_dm&#x60;.  | [default to stop]
 **name_dm** | **str**| This is the search term that will be used to find locations. If the combination of this value and &#x60;type_dm&#x60; results in more than one location found - or &#x60;mode&#x60; is not set to &#x60;direct&#x60;, then a list of stops and no departures will be returned. If &#x60;type_dm&#x60; is set to &#x60;stop&#x60; then this value can take a stop ID or a global stop ID.  | [default to 10111010]
 **mode** | **str**| This allows the departure board to display directly without going through the stop verification process. Use this when the stop is known. This relies on the given combination of &#x60;type_dm&#x60; and &#x60;name_dm&#x60; returning only a single result, otherwise a list of stops and no departures shall be returned.  | [optional] [default to direct]
 **name_key_dm** | **str**| Setting this parameter to &#x60;$USEPOINT$&#x60; enables you to request departures for a specific platform within a station. If this isn&#39;t used, then departures for all platforms at the stop specified in &#x60;name_dm&#x60; are returned.  | [optional] 
 **itd_date** | **str**| The reference date used when searching trips, in &#x60;YYYYMMDD&#x60; format. For instance, 20160901 refers to 1 September 2016. Works in conjunction with the &#x60;itdTime&#x60; value. If not specified, the current server date is used.  | [optional] [default to 20161001]
 **itd_time** | **str**| The reference time used when searching trips, in &#x60;HHMM&#x60; 24-hour format. For instance, 2215 refers to 10:15 PM. | Works in conjunction with the &#x60;itdDate&#x60; value. If not specified, the current server time is used.  | [optional] [default to 1200]
 **departure_monitor_macro** | **str**| Including this parameter enables a number of options that result in the departure monitor operating in the same way as the Transport for NSW Trip Planner web site. It is recommended this is enabled, along with the &#x60;TfNSWDM&#x60; parameter.  | [optional] [default to true]
 **excluded_means** | **str**| This parameter which means of transport to exclude from the departure monitor. To exclude one means, select one of the following: &#x60;1&#x60; &#x3D; train, &#x60;2&#x60; &#x3D; metro, &#x60;4&#x60; &#x3D; light rail, &#x60;5&#x60; &#x3D; bus, &#x60;7&#x60; &#x3D; coach, &#x60;9&#x60; &#x3D; ferry, &#x60;11&#x60; &#x3D; school bus. &#x60;checkbox&#x60; allows you to exclude more than one means of transport when used in conjunction with the &#x60;exclMOT_&lt;ID&gt;&#x60; parameters.  | [optional] 
 **excl_mot_1** | **str**| Excludes train services from the departure monitor.  Must be used in conjunction with &#x60;excludedMeans&#x3D;checkbox&#x60;  | [optional] 
 **excl_mot_2** | **str**| Excludes metro services from the departure monitor.  Must be used in conjunction with &#x60;excludedMeans&#x3D;checkbox&#x60;  | [optional] 
 **excl_mot_4** | **str**| Excludes light rail services from the departure monitor.  Must be used in conjunction with &#x60;excludedMeans&#x3D;checkbox&#x60;  | [optional] 
 **excl_mot_5** | **str**| Excludes bus services from the departure monitor.  Must be used in conjunction with &#x60;excludedMeans&#x3D;checkbox&#x60;  | [optional] 
 **excl_mot_7** | **str**| Excludes coach services from the departure monitor.  Must be used in conjunction with &#x60;excludedMeans&#x3D;checkbox&#x60;  | [optional] 
 **excl_mot_9** | **str**| Excludes ferry services from the departure monitor.  Must be used in conjunction with &#x60;excludedMeans&#x3D;checkbox&#x60;  | [optional] 
 **excl_mot_11** | **str**| Excludes school bus services from the departure monitor.  Must be used in conjunction with &#x60;excludedMeans&#x3D;checkbox&#x60;  | [optional] 
 **tf_nswdm** | **str**| Including this parameter enables a number of options that result in the departure monitor operating in the same way as the Transport for NSW Trip Planner web site, including enabling real-time data. It is recommended this is enabled, along with the &#x60;departureMonitorMacro&#x60; parameter.  | [optional] [default to true]
 **version** | **str**| Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  | [optional] [default to 10.2.1.42]

### Return type

[**DepartureMonitorResponse**](DepartureMonitorResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tfnsw_stopfinder_request**
> StopFinderResponse tfnsw_stopfinder_request(output_format, name_sf, coord_output_format, type_sf=type_sf, tf_nswsf=tf_nswsf, version=version)

Provides capability to return all NSW public transport stop, station, wharf, points of interest and known addresses to be used for auto-suggest/auto-complete (to be used with the Trip planner and Departure board APIs).

This endpoint returns info about stops that match the search criteria. Matches can be sorted on `matchQuality` to determine the best matches for the given input, while the best match will be indicated by the `isBest` value. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
output_format = 'output_format_example' # str | Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the `outputFormat` value to `rapidJSON` is required to enable JSON output. 
name_sf = 'Circular Quay' # str | This is the search term that will be used to find locations. To lookup a coordinate, set `type_sf` to `coord`, and use the following format: `LONGITUDE:LATITUDE:EPSG:4326` (Note that longitude is first). For example, `151.206290:-33.884080:EPSG:4326`. To lookup a stop set `type_sf` to  `stop` and enter the stop id or global stop ID. For example, `10101100`  (default to Circular Quay)
coord_output_format = 'coord_output_format_example' # str | This specifies the format the coordinates are returned in. While other variations are available, the `EPSG:4326` format will return the widely-used format.
type_sf = 'type_sf_example' # str | This specifies the type of results expected in the list of returned stops. By specifying `any`, locations of all types can be returned. If you specifically know that you're searching using a coord, specify `coord`. Likewise, if you're using a stop ID or global stop ID as an input, use `stop` for more accurate results.  (optional)
tf_nswsf = 'true' # str | Including this parameter enables a number of options that result in the stop finder operating in the same way as the Transport for NSW Trip Planner web site.  (optional) (default to true)
version = '10.2.1.42' # str | Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  (optional) (default to 10.2.1.42)

try:
    # Provides capability to return all NSW public transport stop, station, wharf, points of interest and known addresses to be used for auto-suggest/auto-complete (to be used with the Trip planner and Departure board APIs).
    api_response = api_instance.tfnsw_stopfinder_request(output_format, name_sf, coord_output_format, type_sf=type_sf, tf_nswsf=tf_nswsf, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tfnsw_stopfinder_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_format** | **str**| Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the &#x60;outputFormat&#x60; value to &#x60;rapidJSON&#x60; is required to enable JSON output.  | 
 **name_sf** | **str**| This is the search term that will be used to find locations. To lookup a coordinate, set &#x60;type_sf&#x60; to &#x60;coord&#x60;, and use the following format: &#x60;LONGITUDE:LATITUDE:EPSG:4326&#x60; (Note that longitude is first). For example, &#x60;151.206290:-33.884080:EPSG:4326&#x60;. To lookup a stop set &#x60;type_sf&#x60; to  &#x60;stop&#x60; and enter the stop id or global stop ID. For example, &#x60;10101100&#x60;  | [default to Circular Quay]
 **coord_output_format** | **str**| This specifies the format the coordinates are returned in. While other variations are available, the &#x60;EPSG:4326&#x60; format will return the widely-used format. | 
 **type_sf** | **str**| This specifies the type of results expected in the list of returned stops. By specifying &#x60;any&#x60;, locations of all types can be returned. If you specifically know that you&#39;re searching using a coord, specify &#x60;coord&#x60;. Likewise, if you&#39;re using a stop ID or global stop ID as an input, use &#x60;stop&#x60; for more accurate results.  | [optional] 
 **tf_nswsf** | **str**| Including this parameter enables a number of options that result in the stop finder operating in the same way as the Transport for NSW Trip Planner web site.  | [optional] [default to true]
 **version** | **str**| Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  | [optional] [default to 10.2.1.42]

### Return type

[**StopFinderResponse**](StopFinderResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tfnsw_trip_request2**
> TripRequestResponse tfnsw_trip_request2(output_format, coord_output_format, dep_arr_macro, type_origin, name_origin, type_destination, name_destination, itd_date=itd_date, itd_time=itd_time, calc_number_of_trips=calc_number_of_trips, wheelchair=wheelchair, excluded_means=excluded_means, excl_mot_1=excl_mot_1, excl_mot_2=excl_mot_2, excl_mot_4=excl_mot_4, excl_mot_5=excl_mot_5, excl_mot_7=excl_mot_7, excl_mot_9=excl_mot_9, excl_mot_11=excl_mot_11, tf_nswtr=tf_nswtr, version=version, it_options_active=it_options_active, compute_monomodal_trip_bicycle=compute_monomodal_trip_bicycle, cycle_speed=cycle_speed, bike_prof_speed=bike_prof_speed, max_time_bicycle=max_time_bicycle, only_it_bicycle=only_it_bicycle, use_elevation_data=use_elevation_data, elev_fac=elev_fac)

Provides capability to provide NSW public transport trip plan options, including walking and driving legs and real-time information.

This endpoint is used to find a list of journeys between two locations at the specified date and time. For example, if the user is at the Airport and wants to get to Manly using public transport but isn't sure how exactly, this call will tell them exactly which train, bus, ferry or light rail to catch, and between which stops. It is extremely detailed, and includes the the specific path the vehicle(s) will take. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
output_format = 'output_format_example' # str | Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the `outputFormat` value to `rapidJSON` is required to enable JSON output. 
coord_output_format = 'coord_output_format_example' # str | This specifies the format the coordinates are returned in. While other variations are available, the `EPSG:4326` format will return the widely-used format.
dep_arr_macro = 'dep_arr_macro_example' # str | This value anchors the requested date time. If set to `dep`, then trips *departing after* the specified date/time *at the specified location* are included. If set to `arr`, then trips *arriving before* the specified time *at its destination stop* are included. Works in conjunctions with the `itdDate` and `itdTime` values. 
type_origin = 'any' # str | This is the type of data specified in the `name_origin` field. The origin indicates the starting point when searching for journeys. The best way to use the trip planner is to use use `any` for this field then specify a valid location ID in `type_origin`, or to use `coord` in this field and a correctly formatted coordinate in `type_origin`.  (default to any)
name_origin = '10101331' # str | This value is used to indicate the starting point when searching for journeys. This value can be one of three things: A valid location/stop ID (for example, `10101100` indicates Central Station - this can be determined using `stop_finder`). A valid global stop ID (for example, `200060` indicates Central Station - this can be determined using `stop_finder`) Coordinates in the format `LONGITUDE:LATITUDE:EPSG:4326` (Note that longitude is first).  (default to 10101331)
type_destination = 'any' # str | This is the type of data specified in the `name_destination` field. The origin indicates the finishing point when searching for journeys. The best way to use the trip planner is to use use `any` for this field then specify a valid location ID in `type_destination`, or to use `coord` in this field and a correctly formatted coordinate in `type_destination`.  (default to any)
name_destination = '10102027' # str | This value is used to indicate the finishing point when searching for journeys. This value can be one of three things: A valid location/stop ID (for example, `10101100` indicates Central Station - this can be determined using `stop_finder`). A valid global stop ID (for example, `200060` indicates Central Station - this can be determined using `stop_finder`) Coordinates in the format `LONGITUDE:LATITUDE:EPSG:4326` (Note that longitude is first).  (default to 10102027)
itd_date = '20161001' # str | The reference date used when searching trips, in `YYYYMMDD` format. For instance, `20160901` refers to 1 September 2016. Works in conjunction with the `itdTime` and `depArrMacro` values. If not specified, the current server date is used.  (optional) (default to 20161001)
itd_time = '1200' # str | The reference time used when searching trips, in `HHMM` 24-hour format. For instance, `2215` refers to 10:15 PM. | Works in conjunction with the `itdDate` and `depArrMacro` values. If not specified, the current server time is used.  (optional) (default to 1200)
calc_number_of_trips = 6 # int | This parameter indicates the maximum number of trips to returned. Fewer trips may be returned anyway, depending on the available public transport services.  (optional) (default to 6)
wheelchair = 'wheelchair_example' # str | Including this parameter (regardless of its value) ensures that only wheelchair-accessible options are returned.  (optional)
excluded_means = 'excluded_means_example' # str | This parameter which means of transport to exclude from the trip plan. To exclude one means, select one of the following: `1` = train, `2` = metro, `4` = light rail, `5` = bus, `7` = coach, `9` = ferry, `11` = school bus. `checkbox` allows you to exclude more than one means of transport when used in conjunction with the `exclMOT_<ID>` parameters.  (optional)
excl_mot_1 = 'excl_mot_1_example' # str | Excludes train services from the trip plan.  Must be used in conjunction with `excludedMeans=checkbox`  (optional)
excl_mot_2 = 'excl_mot_2_example' # str | Excludes metro services from the trip plan.  Must be used in conjunction with `excludedMeans=checkbox`  (optional)
excl_mot_4 = 'excl_mot_4_example' # str | Excludes light rail services from the trip plan.  Must be used in conjunction with `excludedMeans=checkbox`  (optional)
excl_mot_5 = 'excl_mot_5_example' # str | Excludes bus services from the trip plan.  Must be used in conjunction with `excludedMeans=checkbox`  (optional)
excl_mot_7 = 'excl_mot_7_example' # str | Excludes coach services from the trip plan.  Must be used in conjunction with `excludedMeans=checkbox`  (optional)
excl_mot_9 = 'excl_mot_9_example' # str | Excludes ferry services from the trip plan.  Must be used in conjunction with `excludedMeans=checkbox`  (optional)
excl_mot_11 = 'excl_mot_11_example' # str | Excludes school bus services from the trip plan.  Must be used in conjunction with `excludedMeans=checkbox`  (optional)
tf_nswtr = 'true' # str | Including this parameter enables a number of options that result in this API call operating in the same way as the Transport for NSW Trip Planner web site, including enabling real-time data.  (optional) (default to true)
version = '10.2.1.42' # str | Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  (optional) (default to 10.2.1.42)
it_options_active = 1 # int | This parameter activates the options for individual transport. If the parameter is disabled, the parameters concerning individual transport will not be taken into account. possible values are 0 and 1  (optional) (default to 1)
compute_monomodal_trip_bicycle = true # bool | Activates the calculation of a monomodal trip, i.e., a trip that takes place exclusively with the means of transport <means of transport>, e.g., with bicycle. Note 1: In order to use this parameter, the options for individual transport must be activated with itOptionsActive=1. Note 2: If no monomodal trip with the means of transport <means of transport> is calculated despite the parameter, the maximum time is often set too low. The parameter MaxITTime applies to all means of transport, the parameter MaxITTime<means of transport>to the means of transport <means of transport> (e.g., MaxITTime107). These parameters are located in the [Parameters] section or are added to it. The configuration can be alternatively overridden bythe maxTime<Transport means> parameter.  (optional)
cycle_speed = 16 # int | The value of the <speed> parameter is used to specify the speed of cycle travel in kilometers per hour.Note: In order to use this parameter, the options for individual transport must be activated with itOptionsActive=1. If the parameter is to be specified together with a profile, the bikeProfSpeed parameter can be used.The parameter “'cycleSpeed” specifies the desired real speed of the user for the bike route, which overwrites the speed in the SpeedSettings of the corresponding “bikeProfSpeed”.  (optional) (default to 16)
bike_prof_speed = 'bike_prof_speed_example' # str | With the parameter 'bikeProfSpeed' a bike profile name is passed  (optional)
max_time_bicycle = 56 # int | The value of the this parameter sets the maximum time to be covered by the means of cycling. The time is specified in minutes. Note: To use this parameter, the options for individual transport must be enabled with itOptionsActive=1  (optional)
only_it_bicycle = 56 # int | Restricts the calculation to trips with the bikes only. Note: To be able to use this parameter, the options for individual transport must be activated with itOptionsActive=1. Possible values are 1, true, on  (optional)
use_elevation_data = 56 # int | If this parameter is active, the elevation data is taken into account in the trip calculation for all means of transport and output in a route description for each individual transport section. Note: To be able to use this parameter, the options for individual transport must be activated with itOptionsActive=1. Possible values are 1, true, on  (optional)
elev_fac = 56 # int | This parameter specifies the maximum slope for bike routes. Roads with a slope greater than the specified?? one are avoided. The slope is specified by a factor <factor> whose value range is [0..100]. By default, the value of the parameter is 50  (optional)

try:
    # Provides capability to provide NSW public transport trip plan options, including walking and driving legs and real-time information.
    api_response = api_instance.tfnsw_trip_request2(output_format, coord_output_format, dep_arr_macro, type_origin, name_origin, type_destination, name_destination, itd_date=itd_date, itd_time=itd_time, calc_number_of_trips=calc_number_of_trips, wheelchair=wheelchair, excluded_means=excluded_means, excl_mot_1=excl_mot_1, excl_mot_2=excl_mot_2, excl_mot_4=excl_mot_4, excl_mot_5=excl_mot_5, excl_mot_7=excl_mot_7, excl_mot_9=excl_mot_9, excl_mot_11=excl_mot_11, tf_nswtr=tf_nswtr, version=version, it_options_active=it_options_active, compute_monomodal_trip_bicycle=compute_monomodal_trip_bicycle, cycle_speed=cycle_speed, bike_prof_speed=bike_prof_speed, max_time_bicycle=max_time_bicycle, only_it_bicycle=only_it_bicycle, use_elevation_data=use_elevation_data, elev_fac=elev_fac)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->tfnsw_trip_request2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_format** | **str**| Used to set the response data type. This documentation only covers responses that use the JSON format. Setting the &#x60;outputFormat&#x60; value to &#x60;rapidJSON&#x60; is required to enable JSON output.  | 
 **coord_output_format** | **str**| This specifies the format the coordinates are returned in. While other variations are available, the &#x60;EPSG:4326&#x60; format will return the widely-used format. | 
 **dep_arr_macro** | **str**| This value anchors the requested date time. If set to &#x60;dep&#x60;, then trips *departing after* the specified date/time *at the specified location* are included. If set to &#x60;arr&#x60;, then trips *arriving before* the specified time *at its destination stop* are included. Works in conjunctions with the &#x60;itdDate&#x60; and &#x60;itdTime&#x60; values.  | 
 **type_origin** | **str**| This is the type of data specified in the &#x60;name_origin&#x60; field. The origin indicates the starting point when searching for journeys. The best way to use the trip planner is to use use &#x60;any&#x60; for this field then specify a valid location ID in &#x60;type_origin&#x60;, or to use &#x60;coord&#x60; in this field and a correctly formatted coordinate in &#x60;type_origin&#x60;.  | [default to any]
 **name_origin** | **str**| This value is used to indicate the starting point when searching for journeys. This value can be one of three things: A valid location/stop ID (for example, &#x60;10101100&#x60; indicates Central Station - this can be determined using &#x60;stop_finder&#x60;). A valid global stop ID (for example, &#x60;200060&#x60; indicates Central Station - this can be determined using &#x60;stop_finder&#x60;) Coordinates in the format &#x60;LONGITUDE:LATITUDE:EPSG:4326&#x60; (Note that longitude is first).  | [default to 10101331]
 **type_destination** | **str**| This is the type of data specified in the &#x60;name_destination&#x60; field. The origin indicates the finishing point when searching for journeys. The best way to use the trip planner is to use use &#x60;any&#x60; for this field then specify a valid location ID in &#x60;type_destination&#x60;, or to use &#x60;coord&#x60; in this field and a correctly formatted coordinate in &#x60;type_destination&#x60;.  | [default to any]
 **name_destination** | **str**| This value is used to indicate the finishing point when searching for journeys. This value can be one of three things: A valid location/stop ID (for example, &#x60;10101100&#x60; indicates Central Station - this can be determined using &#x60;stop_finder&#x60;). A valid global stop ID (for example, &#x60;200060&#x60; indicates Central Station - this can be determined using &#x60;stop_finder&#x60;) Coordinates in the format &#x60;LONGITUDE:LATITUDE:EPSG:4326&#x60; (Note that longitude is first).  | [default to 10102027]
 **itd_date** | **str**| The reference date used when searching trips, in &#x60;YYYYMMDD&#x60; format. For instance, &#x60;20160901&#x60; refers to 1 September 2016. Works in conjunction with the &#x60;itdTime&#x60; and &#x60;depArrMacro&#x60; values. If not specified, the current server date is used.  | [optional] [default to 20161001]
 **itd_time** | **str**| The reference time used when searching trips, in &#x60;HHMM&#x60; 24-hour format. For instance, &#x60;2215&#x60; refers to 10:15 PM. | Works in conjunction with the &#x60;itdDate&#x60; and &#x60;depArrMacro&#x60; values. If not specified, the current server time is used.  | [optional] [default to 1200]
 **calc_number_of_trips** | **int**| This parameter indicates the maximum number of trips to returned. Fewer trips may be returned anyway, depending on the available public transport services.  | [optional] [default to 6]
 **wheelchair** | **str**| Including this parameter (regardless of its value) ensures that only wheelchair-accessible options are returned.  | [optional] 
 **excluded_means** | **str**| This parameter which means of transport to exclude from the trip plan. To exclude one means, select one of the following: &#x60;1&#x60; &#x3D; train, &#x60;2&#x60; &#x3D; metro, &#x60;4&#x60; &#x3D; light rail, &#x60;5&#x60; &#x3D; bus, &#x60;7&#x60; &#x3D; coach, &#x60;9&#x60; &#x3D; ferry, &#x60;11&#x60; &#x3D; school bus. &#x60;checkbox&#x60; allows you to exclude more than one means of transport when used in conjunction with the &#x60;exclMOT_&lt;ID&gt;&#x60; parameters.  | [optional] 
 **excl_mot_1** | **str**| Excludes train services from the trip plan.  Must be used in conjunction with &#x60;excludedMeans&#x3D;checkbox&#x60;  | [optional] 
 **excl_mot_2** | **str**| Excludes metro services from the trip plan.  Must be used in conjunction with &#x60;excludedMeans&#x3D;checkbox&#x60;  | [optional] 
 **excl_mot_4** | **str**| Excludes light rail services from the trip plan.  Must be used in conjunction with &#x60;excludedMeans&#x3D;checkbox&#x60;  | [optional] 
 **excl_mot_5** | **str**| Excludes bus services from the trip plan.  Must be used in conjunction with &#x60;excludedMeans&#x3D;checkbox&#x60;  | [optional] 
 **excl_mot_7** | **str**| Excludes coach services from the trip plan.  Must be used in conjunction with &#x60;excludedMeans&#x3D;checkbox&#x60;  | [optional] 
 **excl_mot_9** | **str**| Excludes ferry services from the trip plan.  Must be used in conjunction with &#x60;excludedMeans&#x3D;checkbox&#x60;  | [optional] 
 **excl_mot_11** | **str**| Excludes school bus services from the trip plan.  Must be used in conjunction with &#x60;excludedMeans&#x3D;checkbox&#x60;  | [optional] 
 **tf_nswtr** | **str**| Including this parameter enables a number of options that result in this API call operating in the same way as the Transport for NSW Trip Planner web site, including enabling real-time data.  | [optional] [default to true]
 **version** | **str**| Indicates which version of the API the caller is expecting for both request and response data. Note that if this version differs from the version listed above then the returned data may not be as expected.  | [optional] [default to 10.2.1.42]
 **it_options_active** | **int**| This parameter activates the options for individual transport. If the parameter is disabled, the parameters concerning individual transport will not be taken into account. possible values are 0 and 1  | [optional] [default to 1]
 **compute_monomodal_trip_bicycle** | **bool**| Activates the calculation of a monomodal trip, i.e., a trip that takes place exclusively with the means of transport &lt;means of transport&gt;, e.g., with bicycle. Note 1: In order to use this parameter, the options for individual transport must be activated with itOptionsActive&#x3D;1. Note 2: If no monomodal trip with the means of transport &lt;means of transport&gt; is calculated despite the parameter, the maximum time is often set too low. The parameter MaxITTime applies to all means of transport, the parameter MaxITTime&lt;means of transport&gt;to the means of transport &lt;means of transport&gt; (e.g., MaxITTime107). These parameters are located in the [Parameters] section or are added to it. The configuration can be alternatively overridden bythe maxTime&lt;Transport means&gt; parameter.  | [optional] 
 **cycle_speed** | **int**| The value of the &lt;speed&gt; parameter is used to specify the speed of cycle travel in kilometers per hour.Note: In order to use this parameter, the options for individual transport must be activated with itOptionsActive&#x3D;1. If the parameter is to be specified together with a profile, the bikeProfSpeed parameter can be used.The parameter “&#39;cycleSpeed” specifies the desired real speed of the user for the bike route, which overwrites the speed in the SpeedSettings of the corresponding “bikeProfSpeed”.  | [optional] [default to 16]
 **bike_prof_speed** | **str**| With the parameter &#39;bikeProfSpeed&#39; a bike profile name is passed  | [optional] 
 **max_time_bicycle** | **int**| The value of the this parameter sets the maximum time to be covered by the means of cycling. The time is specified in minutes. Note: To use this parameter, the options for individual transport must be enabled with itOptionsActive&#x3D;1  | [optional] 
 **only_it_bicycle** | **int**| Restricts the calculation to trips with the bikes only. Note: To be able to use this parameter, the options for individual transport must be activated with itOptionsActive&#x3D;1. Possible values are 1, true, on  | [optional] 
 **use_elevation_data** | **int**| If this parameter is active, the elevation data is taken into account in the trip calculation for all means of transport and output in a route description for each individual transport section. Note: To be able to use this parameter, the options for individual transport must be activated with itOptionsActive&#x3D;1. Possible values are 1, true, on  | [optional] 
 **elev_fac** | **int**| This parameter specifies the maximum slope for bike routes. Roads with a slope greater than the specified?? one are avoided. The slope is specified by a factor &lt;factor&gt; whose value range is [0..100]. By default, the value of the parameter is 50  | [optional] 

### Return type

[**TripRequestResponse**](TripRequestResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

