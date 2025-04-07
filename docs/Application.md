# Application

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_family** | **str** |  | [optional] 
**application_root_directory** | **str** |  | [optional] 
**application_type** | **str** |  | [optional] 
**branch_build_repository_ids** | **list[str]** |  | [optional] 
**build_type** | **str** |  | [optional] 
**ci_enabled** | **bool** |  | [optional] 
**common_configs** | **dict(str, str)** |  | [optional] 
**deployment_strategy** | **str** |  | [optional] 
**dns_prefix** | **str** |  | [optional] 
**dns_type** | **str** |  | [optional] 
**elb_idle_timeout_seconds** | **int** |  | [optional] 
**health_check** | [**HealthCheck**](HealthCheck.md) |  | [optional] 
**id** | **str** |  | [optional] 
**load_balancer_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**new_relic_alert_recipients** | **str** |  | [optional] 
**ports** | [**list[Port]**](Port.md) |  | [optional] 
**pvc_list** | [**list[PVC]**](PVC.md) |  | [optional] 
**repository_default_branch** | **str** |  | [optional] 
**repository_url** | **str** |  | [optional] 
**resource_allocation_strategy** | **str** |  | [optional] 
**sonar_branch_wise_analysis_supported** | **bool** |  | [optional] 
**sonar_project_key** | **str** |  | [optional] 
**status_callback_url** | **str** |  | [optional] 
**status_callback_urls** | **list[str]** |  | [optional] 
**strict_git_flow_mode_enabled** | **bool** |  | [optional] 
**tag_build_repository_ids** | **list[str]** |  | [optional] 
**vcs_provider** | **str** |  | [optional] 
**webhook_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


