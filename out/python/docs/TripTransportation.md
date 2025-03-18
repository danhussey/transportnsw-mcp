# TripTransportation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Contains a description of this route.  | [optional] 
**destination** | [**TripTransportationDestination**](TripTransportationDestination.md) |  | [optional] 
**disassembled_name** | **str** | Contains a very short name for the route.  | [optional] 
**icon_id** | **int** | Contains an ID for the icon that can be used for this route. Different values here are used to differentiate differents types of the same route type. For example, private ferries have a different wayfinding icon to ferries operated by Sydney Ferries.  * &#x60;1&#x60;: Sydney Trains (product class &#x60;1&#x60;) * &#x60;2&#x60;: Intercity Trains (product class &#x60;1&#x60;) * &#x60;3&#x60;: Regional Trains (product class &#x60;1&#x60;) * &#x60;19&#x60;: Temporary Trains (product class &#x60;1&#x60;)  * &#x60;24&#x60;: Sydney Metro (product class &#x60;2&#x60;)  * &#x60;13&#x60;: Sydney Light Rail (product class &#x60;4&#x60;) * &#x60;20&#x60;: Temporary Light Rail (product class &#x60;4&#x60;) * &#x60;21&#x60;: Newcastle Light Rail (product class &#x60;4&#x60;)  * &#x60;4&#x60;: Blue Mountains Buses (product class &#x60;5&#x60;) * &#x60;5&#x60;: Sydney Buses (product class &#x60;5&#x60;) * &#x60;6&#x60;: Central Coast Buses (product class &#x60;5&#x60;) * &#x60;14&#x60;: Temporary Buses (product class &#x60;5&#x60;) * &#x60;15&#x60;: Hunter Buses (product class &#x60;5&#x60;) * &#x60;23&#x60;: On Demand (product class &#x60;5&#x60;) * &#x60;31&#x60;: Central West and Orana (product class &#x60;5&#x60;) * &#x60;32&#x60;: Far West (product class &#x60;5&#x60;) * &#x60;33&#x60;: New England North West (product class &#x60;5&#x60;) * &#x60;34&#x60;: Newcastle and Hunter (product class &#x60;5&#x60;) * &#x60;35&#x60;: North Coast (product class &#x60;5&#x60;) * &#x60;36&#x60;: Riverina Murray (product class &#x60;5&#x60;) * &#x60;37&#x60;: South East and Tablelands (product class &#x60;5&#x60;) * &#x60;38&#x60;: Sydney and Surrounds (product class &#x60;5&#x60;)  * &#x60;9&#x60;: Private Buses (product class &#x60;5&#x60;) * &#x60;17&#x60;: Private Coaches (product class &#x60;5&#x60;)  * &#x60;7&#x60;: Regional Coaches (product class &#x60;7&#x60;) * &#x60;22&#x60;: Temporary Coaches (product class &#x60;7&#x60;)  * &#x60;10&#x60;: Sydney Ferries (product class &#x60;9&#x60;) * &#x60;11&#x60;: Newcastle Ferries (product class &#x60;9&#x60;) * &#x60;12&#x60;: Private Ferries (product class &#x60;9&#x60;) * &#x60;18&#x60;: Temporary Ferries (product class &#x60;9&#x60;)  * &#x60;8&#x60;: School Buses (product class &#x60;11&#x60;)  | [optional] 
**id** | **str** | This is an ID that uniquely identifies this route.  | [optional] 
**name** | **str** | This contains the full name of the route.  | [optional] 
**number** | **str** | Contains a short name for the route.  | [optional] 
**operator** | [**TripTransportationOperator**](TripTransportationOperator.md) |  | [optional] 
**product** | [**RouteProduct**](RouteProduct.md) | This element contains additional properties about the route. | [optional] 
**properties** | [**TripTransportationProperties**](TripTransportationProperties.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


