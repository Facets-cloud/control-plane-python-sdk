# TFModule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Account identifier | [optional] 
**alias_flavors** | **list[str]** | Alias flavors for the module | [optional] 
**allowed_test_projects** | **list[str]** | List of test projects where this module will be available. If absent, it is available globally. | [optional] 
**clouds** | **list[str]** | Supported cloud providers for this module | [optional] 
**contains_overridable_fields** | **bool** |  | [optional] 
**created_by** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**facets_yaml** | **str** | Facets YAML content | [optional] 
**feature_branch** | **bool** |  | [optional] 
**flavor** | **str** | Flavor of the TF Module | [optional] 
**git_ref** | **str** | Reference to a specific GIT branch or commit | [optional] 
**git_url** | **str** | URL of the GIT repository | [optional] 
**id** | **str** |  | [optional] 
**inputs** | [**dict(str, Input)**](Input.md) | Input parameters for this module | [optional] 
**intent** | **str** | Intent of the TF Module | [optional] 
**last_modified_by** | **str** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**metadata** | **str** |  | [optional] 
**number_of_versions** | **int** |  | [optional] 
**outputs** | [**list[IntentOutput]**](IntentOutput.md) |  | [optional] 
**path** | [**TFModulePath**](TFModulePath.md) | Path information related to TF Module | [optional] 
**readme_md** | **str** |  | [optional] 
**relative_path** | **str** | Relative path within the repository | [optional] 
**sample_json** | **str** | Sample JSON configuration | [optional] 
**source** | **str** | Source of the module | [optional] 
**spec** | **str** | Specification details of the module | [optional] 
**spec_modeled** | **bool** |  | [optional] 
**stage** | **str** | Stage of the TF Module in its lifecycle | [optional] 
**tags** | **list[str]** |  | [optional] 
**type** | **str** | Type of the TF Module | [optional] 
**version** | **str** | Version of the TF Module | [optional] 
**versioning_key** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


