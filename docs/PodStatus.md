# PodStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[PodCondition]**](PodCondition.md) |  | [optional] 
**container_statuses** | [**list[ContainerStatus]**](ContainerStatus.md) |  | [optional] 
**ephemeral_container_statuses** | [**list[ContainerStatus]**](ContainerStatus.md) |  | [optional] 
**host_ip** | **str** |  | [optional] 
**init_container_statuses** | [**list[ContainerStatus]**](ContainerStatus.md) |  | [optional] 
**message** | **str** |  | [optional] 
**nominated_node_name** | **str** |  | [optional] 
**phase** | **str** |  | [optional] 
**pod_ip** | **str** |  | [optional] 
**pod_ips** | [**list[PodIP]**](PodIP.md) |  | [optional] 
**qos_class** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**start_time** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


