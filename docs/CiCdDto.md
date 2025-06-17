# CiCdDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_type** | **str** | Registration type for the CI/CD setup. | 
**stack_name** | **str** | Name of the project. | 
**routing_rules** | [**list[Criterion]**](Criterion.md) | Routing rules for artifact promotion. | 
**promotion_hierarchies** | [**list[WorkflowHierarchy]**](WorkflowHierarchy.md) | Promotion workflow hierarchies. | 
**ci_system** | **str** | CI system used. | [optional] 
**map_to_all_cis** | **bool** | Indicate whether to map to all CI systems. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

