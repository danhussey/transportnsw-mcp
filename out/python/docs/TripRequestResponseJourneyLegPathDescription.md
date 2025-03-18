# TripRequestResponseJourneyLegPathDescription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coord** | **list[float]** | Contains exactly two values: the first value is the latitude, the second value is the longitude. This is the location where the instruction occurs.  | [optional] 
**cum_distance** | **int** | This is the cumulative distance travelled in metres at the point of this step. | [optional] 
**cum_duration** | **int** | This is the cumulative duration in seconds at the point of this step.  | [optional] 
**distance** | **int** | This is the distance travelled in this step in metres.  | [optional] 
**distance_down** | **int** | This is the distance travelled downward in this step in metres  | [optional] 
**distance_up** | **int** | This is the distance travelled upward in this step in metres  | [optional] 
**duration** | **int** | This is the duration of this step in seconds.  | [optional] 
**from_coords_index** | **int** | This field enables you to retrieve multiple coordinates from the &#x60;coords&#x60; property, starting from this index.  | [optional] 
**manoeuvre** | **str** | Indicates what you have to do (in addition the turn &#x60;turnDirection&#x60;) to execute this step of the path description.  | [optional] 
**name** | **str** | This is a specific description of what to do. In some cases, this information is required in addition to the other properties provided in this step.  | [optional] 
**sky_direction** | **int** | The direction in degrees (0-359) of the skyDirection | [optional] 
**to_coords_index** | **int** | This field enables you to retrieve multiple coordinates from the &#x60;coords&#x60; property, ending at this index.  | [optional] 
**turn_direction** | **str** | Indicates the way you need to turn to execute this step of the path description.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


