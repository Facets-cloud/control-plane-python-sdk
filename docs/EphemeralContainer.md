# EphemeralContainer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **list[str]** |  | [optional] 
**command** | **list[str]** |  | [optional] 
**env** | [**list[EnvVar]**](EnvVar.md) |  | [optional] 
**env_from** | [**list[EnvFromSource]**](EnvFromSource.md) |  | [optional] 
**image** | **str** |  | [optional] 
**image_pull_policy** | **str** |  | [optional] 
**lifecycle** | [**Lifecycle**](Lifecycle.md) |  | [optional] 
**liveness_probe** | [**Probe**](Probe.md) |  | [optional] 
**name** | **str** |  | [optional] 
**ports** | [**list[ContainerPort]**](ContainerPort.md) |  | [optional] 
**readiness_probe** | [**Probe**](Probe.md) |  | [optional] 
**resources** | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 
**security_context** | [**SecurityContext**](SecurityContext.md) |  | [optional] 
**startup_probe** | [**Probe**](Probe.md) |  | [optional] 
**stdin** | **bool** |  | [optional] 
**stdin_once** | **bool** |  | [optional] 
**target_container_name** | **str** |  | [optional] 
**termination_message_path** | **str** |  | [optional] 
**termination_message_policy** | **str** |  | [optional] 
**tty** | **bool** |  | [optional] 
**volume_devices** | [**list[VolumeDevice]**](VolumeDevice.md) |  | [optional] 
**volume_mounts** | [**list[VolumeMount]**](VolumeMount.md) |  | [optional] 
**working_dir** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


