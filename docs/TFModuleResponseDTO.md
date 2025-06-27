# TFModuleResponseDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**last_modified_by** | **str** |  | [optional] 
**intent_details** | [**IntentResponseDTO**](IntentResponseDTO.md) |  | [optional] 
**intent** | **str** | Intent of the TF Module | [optional] 
**flavor** | **str** | Flavor of the TF Module | [optional] 
**alias_flavors** | **list[str]** | Alias flavors for the module | [optional] 
**version** | **str** | Version of the TF Module | [optional] 
**clouds** | **list[str]** | Supported cloud providers | [optional] 
**source** | **str** | Source of the TF Module | [optional] 
**stage** | **str** | Stage of the TF Module in its lifecycle | [optional] 
**preview_module_id** | **str** |  | [optional] 
**published_module_id** | **str** |  | [optional] 
**type** | **str** | Type of the TF Module | [optional] 
**git_url** | **str** | URL of the GIT repository | [optional] 
**git_ref** | **str** | Reference to a specific GIT branch or commit | [optional] 
**sample_json** | **str** | Sample JSON configuration | [optional] 
**spec** | **str** | Specification details of the module | [optional] 
**metadata** | **str** | Metadata of the module | [optional] 
**inputs** | [**dict(str, Input)**](Input.md) | Input parameters for this module | [optional] 
**outputs** | [**list[IntentOutput]**](IntentOutput.md) |  | [optional] 
**versioning_key** | **str** |  | [optional] 
**description** | **str** | Module description | [optional] 
**readme_md** | **str** | Readme content in markdown format | [optional] 
**other_versions** | [**list[OtherVersion]**](OtherVersion.md) |  | [optional] 
**latest_version** | [**OtherVersion**](OtherVersion.md) |  | [optional] 
**tags** | **list[str]** | Tags associated with the module | [optional] 
**allowed_test_projects** | **list[str]** | List of test projects where this module will be available. If absent, it is available globally. | [optional] 
**iac_tool** | **list[str]** |  | [optional] 
**name_length_limit** | **int** | Maximum allowed length for resource names using this module | [optional] 
**feature_branch** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

