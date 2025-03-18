# AdditionalInfoResponseAffectedStop

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This the unique ID of the stop that is affected. It is the same ID that is used elsewhere in the system, such as in &#x60;trip&#x60; or &#x60;stop_finder&#x60;.  | [optional] 
**name** | **str** | This is the title of the affected stop. | [optional] 
**parent** | [**ParentLocation**](ParentLocation.md) | If available, contains information about this location&#39;s parent location. For example, if the stop has a type of &#x60;platform&#x60;, then this field may contain information about the station in which the platform is located.  | [optional] 
**type** | **str** | The type of the location that is affected. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


