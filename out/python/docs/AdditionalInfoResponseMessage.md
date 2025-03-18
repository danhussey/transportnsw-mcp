# AdditionalInfoResponseMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**AdditionalInfoResponseMessageAffected**](AdditionalInfoResponseMessageAffected.md) |  | [optional] 
**content** | **str** | This is the descriptive alert content. It may contain HTML tags and/or HTML entities.  | [optional] 
**id** | **str** | This is a unique identifier for this particular service alert.  | [optional] 
**priority** | **str** | This value indicates how important the service alert is. A value of &#x60;high&#x60; or &#x60;veryHigh&#x60; likely indicates that the alert will correspond to an event that impacts the ability to travel for relevant users, while &#x60;low&#x60; or &#x60;veryLow&#x60; might be more of an informational message.  | [optional] 
**properties** | [**AdditionalInfoResponseMessageProperties**](AdditionalInfoResponseMessageProperties.md) |  | [optional] 
**subtitle** | **str** | This is short summary that can be used as a heading for the alert content. It may contain HTML tags and/or HTML entities.  | [optional] 
**timestamps** | [**AdditionalInfoResponseTimestamps**](AdditionalInfoResponseTimestamps.md) | This contains a number of timestamps that describe when the alert was created, and when the described alert actually takes place and/or is relevant.  | [optional] 
**type** | **str** | This indicates the category of the service alert. For example, if this value is &#x60;stopInfo&#x60;, then the alert is related to an issue affecting a stop. It is then likely that the affected lines would be those that stop at the affected stop.  * &#x60;routeInfo&#x60;: The alert is related to a specific route * &#x60;stopInfo&#x60;: The alert is related to a specific stop * &#x60;stopBlocking&#x60;: This alert is related to a stop closure * &#x60;lineInfo&#x60;: The alert is related to a specific journey * &#x60;bannerInfo&#x60;: The alert of high importance and potentially has a network-wide impact.  | [optional] 
**url** | **str** | This field contains a URL that contains additional information about the alert. | [optional] 
**url_text** | **str** | This field contains a title that can be used when displaying the &#x60;infoLinkURL&#x60; URL. | [optional] 
**version** | **int** | This number indicates the version of this alert. Initially when it is created it has version &#x60;1&#x60;, but if it is then updated it will have a new &#x60;lastModification&#x60; value and the version will now be &#x60;2&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


