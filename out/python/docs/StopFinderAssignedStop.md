# StopFinderAssignedStop

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connecting_mode** | **int** | This is the mode of transport that is used to connect to this stop. The following values are available:  * &#x60;1&#x60;: Train * &#x60;2&#x60;: Metro * &#x60;4&#x60;: Light Rail * &#x60;5&#x60;: Bus * &#x60;7&#x60;: Coach * &#x60;9&#x60;: Ferry * &#x60;11&#x60;: School Bus * &#x60;97&#x60;: Remain On-Board * &#x60;99&#x60;: Walking * &#x60;100&#x60;: Walking (Footpath) * &#x60;101&#x60;: Bicycle * &#x60;102&#x60;: Take Bicycle On Public Transport * &#x60;103&#x60;: Kiss &amp; Ride * &#x60;104&#x60;: Park &amp; Ride * &#x60;105&#x60;: Taxi * &#x60;106&#x60;: Car  | [optional] 
**coord** | **list[float]** | Contains exactly two values: the first value is the latitude, the second value is the longitude.  | [optional] 
**disassembled_name** | **str** | This is the short version of the location name, which does not include the suburb or other information.  | [optional] 
**distance** | **int** | This is the distance in metres to this stop from the location to which it is assigned. | [optional] 
**duration** | **int** | This is the number of minutes it would take to reach this stop from the location to which it is assigned. | [optional] 
**id** | **str** | This is a unique ID for the returned location. Certain types of ID can be used for subsequent searches performed with &#x60;stop_finder&#x60;, or can be used as the origin or destination in an &#x60;trip&#x60; request. The format of a location ID differs greatly, depending on the type of location it is.  | [optional] 
**modes** | **list[int]** | This is included only if the &#x60;type&#x60; value is set to &#x60;stop&#x60;. Contains a list of modes of transport that service this stop. This can be useful for showing relevant wayfinding icons when presenting users with a list of matching stops to choose from.  The following values may be present:  * &#x60;1&#x60;: Train * &#x60;2&#x60;: Metro * &#x60;4&#x60;: Light Rail * &#x60;5&#x60;: Bus * &#x60;7&#x60;: Coach * &#x60;9&#x60;: Ferry * &#x60;11&#x60;: School Bus  | [optional] 
**name** | **str** | This is the long version of the location name, which may include the suburb or other information.  | [optional] 
**parent** | [**ParentLocation**](ParentLocation.md) | If available, contains information about this location&#39;s parent location. For example, if the stop has a type of &#x60;platform&#x60;, then this field may contain information about the station in which the platform is located.  | [optional] 
**type** | **str** | A value of &#x60;unknown&#x60; likely indicates bad data. If a location is returned with this type, you can safely ignore it.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


