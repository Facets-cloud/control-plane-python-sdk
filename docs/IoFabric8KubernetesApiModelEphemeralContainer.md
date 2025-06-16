# IoFabric8KubernetesApiModelEphemeralContainer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **list[str]** |  | [optional] 
**command** | **list[str]** |  | [optional] 
**env** | [**list[IoFabric8KubernetesApiModelEnvVar]**](IoFabric8KubernetesApiModelEnvVar.md) |  | [optional] 
**env_from** | [**list[IoFabric8KubernetesApiModelEnvFromSource]**](IoFabric8KubernetesApiModelEnvFromSource.md) |  | [optional] 
**image** | **str** |  | [optional] 
**image_pull_policy** | **str** |  | [optional] 
**lifecycle** | [**IoFabric8KubernetesApiModelLifecycle**](IoFabric8KubernetesApiModelLifecycle.md) |  | [optional] 
**liveness_probe** | [**IoFabric8KubernetesApiModelProbe**](IoFabric8KubernetesApiModelProbe.md) |  | [optional] 
**name** | **str** |  | [optional] 
**ports** | [**list[IoFabric8KubernetesApiModelContainerPort]**](IoFabric8KubernetesApiModelContainerPort.md) |  | [optional] 
**readiness_probe** | [**IoFabric8KubernetesApiModelProbe**](IoFabric8KubernetesApiModelProbe.md) |  | [optional] 
**resources** | [**IoFabric8KubernetesApiModelResourceRequirements**](IoFabric8KubernetesApiModelResourceRequirements.md) |  | [optional] 
**security_context** | [**IoFabric8KubernetesApiModelSecurityContext**](IoFabric8KubernetesApiModelSecurityContext.md) |  | [optional] 
**startup_probe** | [**IoFabric8KubernetesApiModelProbe**](IoFabric8KubernetesApiModelProbe.md) |  | [optional] 
**stdin** | **bool** |  | [optional] 
**stdin_once** | **bool** |  | [optional] 
**target_container_name** | **str** |  | [optional] 
**termination_message_path** | **str** |  | [optional] 
**termination_message_policy** | **str** |  | [optional] 
**tty** | **bool** |  | [optional] 
**volume_devices** | [**list[IoFabric8KubernetesApiModelVolumeDevice]**](IoFabric8KubernetesApiModelVolumeDevice.md) |  | [optional] 
**volume_mounts** | [**list[IoFabric8KubernetesApiModelVolumeMount]**](IoFabric8KubernetesApiModelVolumeMount.md) |  | [optional] 
**working_dir** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

