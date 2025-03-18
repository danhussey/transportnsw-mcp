# ParentLocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disassembled_name** | **str** | This is the short version of the location name, which does not include the suburb or other information.  | [optional] 
**id** | **str** | This is a unique ID for the returned location. Certain types of ID can be used for subsequent searches performed with &#x60;stop_finder&#x60;, or can be used as the origin or destination in an &#x60;trip&#x60; request. The format of a location ID differs greatly, depending on the type of location it is.  | [optional] 
**name** | **str** | This is the long version of the location name, which may include the suburb or other information.  | [optional] 
**parent** | [**ParentLocation**](ParentLocation.md) | In some cases, a parent location will also contain its parent (in other words, the grandparent of the initial location)  | [optional] 
**type** | **str** | This is the type of location being returned. It may represent a stop or platform that a public transport service physically stops at for passenger boarding, or it may represent somebody&#39;s house. A value of &#x60;unknown&#x60; likely indicates bad data coming from the server. If a location is returned with this type, you can safely ignore it.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


