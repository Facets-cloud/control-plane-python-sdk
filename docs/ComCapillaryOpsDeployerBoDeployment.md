# ComCapillaryOpsDeployerBoDeployment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**application_family** | **str** |  | [optional] 
**application_id** | **str** |  | [optional] 
**build_id** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 
**configurations** | [**list[ComCapillaryOpsDeployerBoEnvironmentVariable]**](ComCapillaryOpsDeployerBoEnvironmentVariable.md) |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**pod_size** | **str** |  | [optional] 
**horizontal_pod_autoscaler** | [**ComCapillaryOpsDeployerBoHPA**](ComCapillaryOpsDeployerBoHPA.md) |  | [optional] 
**schedule** | **str** |  | [optional] 
**rollback_enabled** | **bool** |  | [optional] 
**deployed_by** | **str** |  | [optional] 
**replicas** | **int** |  | [optional] 
**configurations_map** | **dict(str, str)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

