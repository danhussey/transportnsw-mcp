# DepartureMonitorResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ApiErrorResponse**](ApiErrorResponse.md) | If an error has occurred, this element contains information about the error.  | [optional] 
**locations** | [**list[StopFinderLocation]**](StopFinderLocation.md) | Contains a list of stops that were matched based on the supplied &#x60;type_dm&#x60; and &#x60;name_dm&#x60; request values. There must be exactly one location present for the &#x60;stopEvents&#x60; response data to be populated. Additionally, the &#x60;mode&#x60; request value must be set to &#x60;direct&#x60;.  | [optional] 
**stop_events** | [**list[DepartureMonitorResponseStopEvent]**](DepartureMonitorResponseStopEvent.md) | Contains a list of departures/arrivals for the stop included in the &#x60;location&#x60; property of the response.  | [optional] 
**version** | **str** | The version of the API that provided the response. Note that if this value is different to above, then the returned data may be different than expected. You can set the expected version using the &#x60;version&#x60; request parameter.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


