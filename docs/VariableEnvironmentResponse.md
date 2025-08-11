# VariableEnvironmentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable_name** | **str** | Name of the variable/secret | [optional] 
**is_secret** | **bool** | Whether this is a secret or regular variable | [optional] 
**description** | **str** | Description of the variable/secret | [optional] 
**_global** | **bool** | Whether this is a global variable | [optional] 
**stack_default** | **str** | Default value defined at stack level | [optional] 
**environment_values** | [**list[EnvironmentVariableValue]**](EnvironmentVariableValue.md) | Values across different environments | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

