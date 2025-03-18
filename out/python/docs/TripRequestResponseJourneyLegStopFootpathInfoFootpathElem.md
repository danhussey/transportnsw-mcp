# TripRequestResponseJourneyLegStopFootpathInfoFootpathElem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Contains additional information about this instruction, but is generally unused.  | [optional] 
**destination** | [**TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation**](TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.md) | Indicates the starting location for this leg, in terms of locations in the system such as stops or places of interest. Typically, since these instructions indicate how to travel within a stop or station, the &#x60;origin&#x60; and &#x60;destination&#x60; will both reference the same stop, but the coordinate will be specific to this instruction.  | [optional] 
**level** | **str** | Indicates the direction of travel for this instruction. Generally a ramp, escalator or stairs will go &#x60;UP&#x60; or &#x60;DOWN&#x60; to a different floor. This value will be &#x60;LEVEL&#x60; when the &#x60;type&#x60; field is also &#x60;LEVEL&#x60;.  | [optional] 
**level_from** | **int** | Indicates the floor number the instruction is starting from. If the &#x60;type&#x60; is &#x60;LEVEL&#x60;, then the &#x60;levelFrom&#x60; and &#x60;levelTo&#x60; values should be the same.  | [optional] 
**level_to** | **int** | Indicates the floor number the instruction ends of. If the &#x60;type&#x60; is &#x60;LEVEL&#x60;, then the &#x60;levelFrom&#x60; and &#x60;levelTo&#x60; values should be the same.  | [optional] 
**origin** | [**TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation**](TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.md) | Indicates the starting location for this leg, in terms of locations in the system such as stops or places of interest. Typically, since these instructions indicate how to travel within a stop or station, the &#x60;origin&#x60; and &#x60;destination&#x60; will both reference the same stop, but the coordinate will be specific to this instruction.  | [optional] 
**type** | **str** | This indicates the type of \&quot;terrain\&quot; for this instruction. &#x60;LEVEL&#x60; indicates a normal flat surface.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


