# TripRequestResponseJourneyLegStop

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrival_time_estimated** | **str** | A timestamp in &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; format that indicates the estimated arrival time. If real-time information is available then this timestamp is the real-time estimate, otherwise it is the same as the value in &#x60;arrivalTimePlanned&#x60;.  | [optional] 
**arrival_time_planned** | **str** | A timestamp in &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; format that indicates the planned arrival time. This is the original scheduled time.  | [optional] 
**coord** | **list[float]** | Contains exactly two values: the first value is the latitude, the second value is the longitude.  | [optional] 
**departure_time_estimated** | **str** | A timestamp in &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; format that indicates the estimated departure time. If real-time information is available then this timestamp is the real-time estimate, otherwise it is the same as the value in &#x60;departureTimePlanned&#x60;.  | [optional] 
**departure_time_planned** | **str** | A timestamp in &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60; format that indicates the planned departure time. This is the original scheduled time.  | [optional] 
**disassembled_name** | **str** | This is the short version of the location name, which does not include the suburb or other information.  | [optional] 
**id** | **str** | This is a unique ID for the returned location. Certain types of ID can be used for subsequent searches performed with &#x60;stop_finder&#x60;, or can be used as the origin or destination in an &#x60;trip&#x60; request. The format of a location ID differs greatly, depending on the type of location it is.  | [optional] 
**name** | **str** | This is the long version of the location name, which may include the suburb or other information.  | [optional] 
**parent** | [**ParentLocation**](ParentLocation.md) | If available, contains information about this location&#39;s parent location. For example, if the stop has a type of &#x60;platform&#x60;, then this field may contain information about the station in which the platform is located.  | [optional] 
**properties** | [**TripRequestResponseJourneyLegStopProperties**](TripRequestResponseJourneyLegStopProperties.md) |  | [optional] 
**type** | **str** | This is the type of location being returned. It will typically represent a specific stop or platform.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


