# DeploymentContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifactory_details** | [**list[Artifactory]**](Artifactory.md) |  | [optional] 
**artifacts** | **dict(str, dict(str, Artifact))** |  | [optional] 
**can_skip_approval** | **bool** |  | [optional] 
**extra_env** | **dict(str, str)** |  | [optional] 
**maintenance_window** | [**MaintenanceWindowDTO**](MaintenanceWindowDTO.md) |  | [optional] 
**modules** | [**dict(str, ModuleDTO)**](ModuleDTO.md) |  | [optional] 
**overrides** | [**list[OverrideObject]**](OverrideObject.md) |  | [optional] 
**parallel_release** | **bool** |  | [optional] 
**provided_resources** | [**ProvidedResources**](ProvidedResources.md) |  | [optional] 
**provided_secrets_id** | **str** |  | [optional] 
**resource_metadata** | **dict(str, list[ResourceMetadata])** |  | [optional] 
**resources** | [**dict(str, MatchedResourceDTO)**](MatchedResourceDTO.md) |  | [optional] 
**secrets_context** | [**SecretsContextDTO**](SecretsContextDTO.md) |  | [optional] 
**settings** | **dict(str, dict(str, object))** |  | [optional] 
**snapshots** | **dict(str, dict(str, SnapshotInfo))** |  | [optional] 
**stack_source_version** | **str** |  | [optional] 
**template_inputs** | **dict(str, list[StackTemplateInput])** |  | [optional] 
**tf_version** | [**TfVersion**](TfVersion.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

