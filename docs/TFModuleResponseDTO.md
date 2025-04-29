# TFModuleResponseDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias_flavors** | **list[str]** | Alias flavors for the module | [optional] 
**allowed_test_projects** | **list[str]** | List of test projects where this module will be available. If absent, it is available globally. | [optional] 
**clouds** | **list[str]** | Supported cloud providers | [optional] 
**created_by** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**description** | **str** | Module description | [optional] 
**feature_branch** | **bool** |  | [optional] 
**flavor** | **str** | Flavor of the TF Module | [optional] 
**git_ref** | **str** | Reference to a specific GIT branch or commit | [optional] 
**git_url** | **str** | URL of the GIT repository | [optional] 
**id** | **str** |  | [optional] 
**inputs** | [**dict(str, Input)**](Input.md) | Input parameters for this module | [optional] 
**intent** | **str** | Intent of the TF Module | [optional] 
**intent_details** | [**IntentResponseDTO**](IntentResponseDTO.md) |  | [optional] 
**last_modified_by** | **str** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**latest_version** | [**OtherVersion**](OtherVersion.md) |  | [optional] 
**metadata** | **str** | Metadata of the module | [optional] 
**other_versions** | [**list[OtherVersion]**](OtherVersion.md) |  | [optional] 
**outputs** | [**list[IntentOutput]**](IntentOutput.md) |  | [optional] 
**preview_module_id** | **str** |  | [optional] 
**published_module_id** | **str** |  | [optional] 
**readme_md** | **str** | Readme content in markdown format | [optional] 
**sample_json** | **str** | Sample JSON configuration | [optional] 
**source** | **str** | Source of the TF Module | [optional] 
**spec** | **str** | Specification details of the module | [optional] 
**stage** | **str** | Stage of the TF Module in its lifecycle | [optional] 
**tags** | **list[str]** | Tags associated with the module | [optional] 
**type** | **str** | Type of the TF Module | [optional] 
**version** | **str** | Version of the TF Module | [optional] 
**versioning_key** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

