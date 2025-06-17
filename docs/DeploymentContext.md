# DeploymentContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifacts** | **dict(str, dict(str, Artifact))** |  | [optional] 
**artifactory_details** | [**list[Artifactory]**](Artifactory.md) |  | [optional] 
**overrides** | [**list[OverrideObject]**](OverrideObject.md) |  | [optional] 
**snapshots** | **dict(str, dict(str, SnapshotInfo))** |  | [optional] 
**extra_env** | **dict(str, str)** |  | [optional] 
**provided_resources** | [**ProvidedResources**](ProvidedResources.md) |  | [optional] 
**settings** | **dict(str, dict(str, object))** |  | [optional] 
**template_inputs** | **dict(str, list[StackTemplateInput])** |  | [optional] 
**stack_source_version** | **str** |  | [optional] 
**tf_version** | [**TfVersion**](TfVersion.md) |  | [optional] 
**resource_metadata** | **dict(str, list[ResourceMetadata])** |  | [optional] 
**provided_secrets_id** | **str** |  | [optional] 
**can_skip_approval** | **bool** |  | [optional] 
**resources** | [**dict(str, MatchedResourceDTO)**](MatchedResourceDTO.md) |  | [optional] 
**modules** | [**dict(str, ModuleDTO)**](ModuleDTO.md) |  | [optional] 
**maintenance_window** | [**MaintenanceWindowDTO**](MaintenanceWindowDTO.md) |  | [optional] 
**secrets_context** | [**SecretsContextDTO**](SecretsContextDTO.md) |  | [optional] 
**parallel_release** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

