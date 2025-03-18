# DepartureMonitorResponseStopEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**departure_time_planned** | **str** | A timestamp in &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; format | [optional] 
**infos** | [**list[TripRequestResponseJourneyLegStopInfo]**](TripRequestResponseJourneyLegStopInfo.md) | Contains a number of service alert messages relating to this stop event. Information returned here is also available using the &#x60;add_info&#x60; API endpoint.  | [optional] 
**location** | [**StopFinderLocation**](StopFinderLocation.md) | This element contains a single location associated with this stop time.  | [optional] 
**transportation** | [**TripTransportation**](TripTransportation.md) | This element describes the mode of transportation and/or the specific route or trip used for this stop time.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


