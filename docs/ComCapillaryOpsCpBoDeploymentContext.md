# ComCapillaryOpsCpBoDeploymentContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifacts** | **dict(str, dict(str, ComCapillaryOpsCpBoArtifact))** |  | [optional] 
**artifactory_details** | [**list[ComCapillaryOpsCpBoArtifactory]**](ComCapillaryOpsCpBoArtifactory.md) |  | [optional] 
**overrides** | [**list[ComCapillaryOpsCpBoOverrideObject]**](ComCapillaryOpsCpBoOverrideObject.md) |  | [optional] 
**snapshots** | **dict(str, dict(str, ComCapillaryOpsCpBoSnapshotInfo))** |  | [optional] 
**extra_env** | **dict(str, str)** |  | [optional] 
**provided_resources** | [**ComCapillaryOpsCpBoProvidedresourcesProvidedResources**](ComCapillaryOpsCpBoProvidedresourcesProvidedResources.md) |  | [optional] 
**settings** | **dict(str, dict(str, object))** |  | [optional] 
**template_inputs** | **dict(str, list[ComCapillaryOpsCpBoStackTemplateInput])** |  | [optional] 
**stack_source_version** | **str** |  | [optional] 
**tf_version** | [**ComCapillaryOpsCpBoTfVersion**](ComCapillaryOpsCpBoTfVersion.md) |  | [optional] 
**resource_metadata** | **dict(str, list[ComCapillaryOpsCpBoResoucesResourceMetadata])** |  | [optional] 
**provided_secrets_id** | **str** |  | [optional] 
**can_skip_approval** | **bool** |  | [optional] 
**resources** | [**dict(str, ComCapillaryOpsCpV2RegistryMatchedResourceDTO)**](ComCapillaryOpsCpV2RegistryMatchedResourceDTO.md) |  | [optional] 
**modules** | [**dict(str, ComCapillaryOpsCpV2RegistryModuleDTO)**](ComCapillaryOpsCpV2RegistryModuleDTO.md) |  | [optional] 
**maintenance_window** | [**ComCapillaryOpsCpV2MaintenancewindowBoMaintenanceWindowDTO**](ComCapillaryOpsCpV2MaintenancewindowBoMaintenanceWindowDTO.md) |  | [optional] 
**secrets_context** | [**ComCapillaryOpsCpBoSecretsSecretsContextDTO**](ComCapillaryOpsCpBoSecretsSecretsContextDTO.md) |  | [optional] 
**parallel_release** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

