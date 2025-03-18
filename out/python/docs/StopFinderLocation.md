# StopFinderLocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_stops** | [**list[StopFinderAssignedStop]**](StopFinderAssignedStop.md) | This is a list of stops that are assigned to this location. This means if you&#39;re in the current location and want to catch public transport, these assigned stops are directly available to you.  | [optional] 
**building_number** | **str** | This is the number of the property, included only if the &#x60;type&#x60; value is set to &#x60;singlehouse&#x60;. Note that it is a string, as it may include non-numeric characters.  | [optional] 
**coord** | **list[float]** | Contains exactly two values: the first value is the latitude, the second value is the longitude.  | [optional] 
**disassembled_name** | **str** | This is the short version of the location name, which does not include the suburb or other information.  | [optional] 
**id** | **str** | This is a unique ID for the returned location. Certain types of ID can be used for subsequent searches performed with &#x60;stop_finder&#x60;, or can be used as the origin or destination in an &#x60;trip&#x60; request. The format of a location ID differs greatly, depending on the type of location it is.  | [optional] 
**is_best** | **bool** | Indicates whether or not this is the best match out of all the returned locations. | [optional] 
**is_global_id** | **bool** | This determines whether the id property is a global stop id or not  | [optional] 
**match_quality** | **int** | This value indicates how well the returned stop matches the search query. A higher number indicates a better match. | [optional] 
**modes** | **list[int]** | This is included only if the &#x60;type&#x60; value is set to &#x60;stop&#x60;. Contains a list of modes of transport that service this stop. This can be useful for showing relevant wayfinding icons when presenting users with a list of matching stops to choose from.  The following values may be present:  * &#x60;1&#x60;: Train * &#x60;2&#x60;: Metro * &#x60;4&#x60;: Light Rail * &#x60;5&#x60;: Bus * &#x60;7&#x60;: Coach * &#x60;9&#x60;: Ferry * &#x60;11&#x60;: School Bus  | [optional] 
**name** | **str** | This is the long version of the location name, which may include the suburb or other information.  | [optional] 
**parent** | [**ParentLocation**](ParentLocation.md) | If available, contains information about this location&#39;s parent location. For example, if the stop has a type of &#x60;platform&#x60;, then this field may contain information about the station in which the platform is located.  | [optional] 
**street_name** | **str** | This is included only if the &#x60;type&#x60; value is set to &#x60;street&#x60; or &#x60;singlehouse&#x60;. | [optional] 
**type** | **str** | This is the type of location being returned. It may represent a stop or platform that a public transport service physically stops at for passenger boarding, or it may represent somebody&#39;s house. A value of &#x60;unknown&#x60; likely indicates bad data coming from the server. If a location is returned with this type, you can safely ignore it.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


