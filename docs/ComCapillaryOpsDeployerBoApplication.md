# ComCapillaryOpsDeployerBoApplication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**application_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**vcs_provider** | **str** |  | 
**repository_url** | **str** |  | 
**repository_default_branch** | **str** |  | [optional] 
**application_root_directory** | **str** |  | 
**ports** | [**list[ComCapillaryOpsDeployerBoPort]**](ComCapillaryOpsDeployerBoPort.md) |  | 
**load_balancer_type** | **str** |  | [optional] 
**pvc_list** | [**list[ComCapillaryOpsDeployerBoPVC]**](ComCapillaryOpsDeployerBoPVC.md) |  | [optional] 
**build_type** | **str** |  | 
**application_family** | **str** |  | 
**dns_prefix** | **str** |  | [optional] 
**health_check** | [**ComCapillaryOpsDeployerBoHealthCheck**](ComCapillaryOpsDeployerBoHealthCheck.md) |  | [optional] 
**dns_type** | **str** |  | [optional] 
**common_configs** | **dict(str, str)** |  | [optional] 
**ci_enabled** | **bool** |  | [optional] 
**webhook_id** | **str** |  | [optional] 
**deployment_strategy** | **str** |  | [optional] 
**elb_idle_timeout_seconds** | **int** |  | [optional] 
**strict_git_flow_mode_enabled** | **bool** |  | [optional] 
**status_callback_url** | **str** |  | [optional] 
**new_relic_alert_recipients** | **str** |  | [optional] 
**tag_build_repository_ids** | **list[str]** |  | [optional] 
**branch_build_repository_ids** | **list[str]** |  | [optional] 
**resource_allocation_strategy** | **str** |  | [optional] 
**status_callback_urls** | **list[str]** |  | [optional] 
**sonar_branch_wise_analysis_supported** | **bool** |  | [optional] 
**sonar_project_key** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

