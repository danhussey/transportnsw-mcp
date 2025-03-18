# StopFinderResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ApiErrorResponse**](ApiErrorResponse.md) | If an error has occurred, this element contains information about the error.  | [optional] 
**locations** | [**list[StopFinderLocation]**](StopFinderLocation.md) | An array of all locations that were found using the specified search input. To display the results in a way that makes sense to the end user, you can sort this list by &#x60;matchQuality&#x60;. Alternatively, you can group the results by their type and/or sort them alphabetically.  | [optional] 
**version** | **str** | The version of the API that provided the response. Note that if this value is different to above, then the returned data may be different than expected. You can set the expected version using the &#x60;version&#x60; request parameter.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


