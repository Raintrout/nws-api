# Error

An API Problem (RFC7807) document
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | A URI reference (RFC3986) that identifies the problem type | [optional] [default to 'about:blank']
**title** | **str** | A short, human-readable summary of the problem type | 
**status** | **float** | The HTTP status code (RFC7231, Section 6) generated by the origin server for this occurrence of the problem | [optional] 
**detail** | **str** | A human-readable explanation specific to this occurrence of the problem | [optional] 
**instance** | **str** | A URI reference that identifies the specific occurrence of the problem | [optional] 
**correlation_id** | **str** | A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


