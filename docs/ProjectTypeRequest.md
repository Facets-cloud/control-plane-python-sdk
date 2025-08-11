# ProjectTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the project type | 
**allowed_clouds** | **list[str]** | Set of allowed clouds | 
**description** | **str** | Description of the project type | [optional] 
**template_git_details** | [**TemplateGitDetails**](TemplateGitDetails.md) |  | 
**use_branch** | **bool** | Use branch flag | [optional] 
**base_project_name** | **str** | Base project name | [optional] 
**mapped_resources** | [**list[ProjectTypeMappedResource]**](ProjectTypeMappedResource.md) | Allowed modules for the project | [optional] 
**iac_tool** | **str** | IAC tool used for the project | 
**iac_tool_version** | **str** |  | [optional] 
**dynamic_launch** | **bool** |  | [optional] 
**enable_no_cloud_environment** | **bool** |  | [optional] 
**legacy** | **bool** | Whether this is a legacy project type | [optional] 
**include_tooling_provider** | **bool** | Whether to include tooling provider | [optional] 
**include_cp_k8s_provider** | **bool** | Whether to include CPK8s provider | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

