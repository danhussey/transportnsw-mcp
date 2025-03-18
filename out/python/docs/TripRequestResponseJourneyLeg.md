# TripRequestResponseJourneyLeg

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coords** | **list[list[float]]** | This elements contains a list of coordinates that this journey leg follows. A line between can be plotted between these coordinates in order when representing the journey on a map in order to show where the vehicle travels (or for a walking leg, the path to be walked).  | [optional] 
**destination** | [**TripRequestResponseJourneyLegStop**](TripRequestResponseJourneyLegStop.md) | This is the finishing location of the leg. | [optional] 
**distance** | **int** | The approximate distance in metres travelled to complete this journey leg. | [optional] 
**duration** | **int** | The approximate amount of time in seconds required to complete this journey leg. | [optional] 
**foot_path_info** | [**list[TripRequestResponseJourneyLegStopFootpathInfo]**](TripRequestResponseJourneyLegStopFootpathInfo.md) | If the leg corresponds to a walking leg, this element contains walking directions.  | [optional] 
**hints** | [**list[TripRequestResponseJourneyLegHints]**](TripRequestResponseJourneyLegHints.md) | Contains a number of additional informational messages that may be useful for travellers. | [optional] 
**infos** | [**list[TripRequestResponseJourneyLegStopInfo]**](TripRequestResponseJourneyLegStopInfo.md) | Contains a number of service alert messages relating to this journey leg. Information returned here is also available using the &#x60;add_info&#x60; API endpoint.  | [optional] 
**interchange** | [**TripRequestResponseJourneyLegInterchange**](TripRequestResponseJourneyLegInterchange.md) | Contains information for how to interchange between the end of one leg to the next journey leg.  | [optional] 
**is_realtime_controlled** | **bool** | This indicates whether or not real-time data has been used to calculate the departure/arrival timestamps | [optional] 
**origin** | [**TripRequestResponseJourneyLegStop**](TripRequestResponseJourneyLegStop.md) | This is the starting location of the leg. | [optional] 
**path_descriptions** | [**list[TripRequestResponseJourneyLegPathDescription]**](TripRequestResponseJourneyLegPathDescription.md) | Contains walking information for completing this journey leg. | [optional] 
**properties** | [**TripRequestResponseJourneyLegProperties**](TripRequestResponseJourneyLegProperties.md) |  | [optional] 
**stop_sequence** | [**list[TripRequestResponseJourneyLegStop]**](TripRequestResponseJourneyLegStop.md) | This is a list of all stops that are made for this leg. It is sorted in order of its stopping sequence. If the leg is a walking leg between two stops, then this will contain these two stops in order.  | [optional] 
**transportation** | [**TripTransportation**](TripTransportation.md) | This element contains information about the mode of transport and/or route used to complete this journey leg.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


