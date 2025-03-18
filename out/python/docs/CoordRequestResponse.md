# CoordRequestResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ApiErrorResponse**](ApiErrorResponse.md) | If an error has occurred, this element contains information about the error.  | [optional] 
**locations** | [**list[CoordRequestResponseLocation]**](CoordRequestResponseLocation.md) | This contains a list of all of the stops, reload points and places of interest found based on the given request.  | [optional] 
**version** | **str** | The version of the API that provided the response. Note that if this value is different to above, then the returned data may be different than expected. You can set the expected version using the &#x60;version&#x60; request parameter.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


