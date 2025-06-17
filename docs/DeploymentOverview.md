# DeploymentOverview

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** |  | [optional] 
**down_stream_cluster_names** | **list[str]** |  | [optional] 
**current_signed_off_deployment** | [**DeploymentLog**](DeploymentLog.md) |  | [optional] 
**stack** | [**Stack**](Stack.md) |  | [optional] 
**deployments_stats** | [**DeploymentsStats**](DeploymentsStats.md) |  | [optional] 
**next_execution_time** | **str** |  | [optional] 
**time_to_next_execution** | **str** |  | [optional] 
**latest_deployment** | [**DeploymentLog**](DeploymentLog.md) |  | [optional] 
**in_progress_deployments** | [**list[DeploymentLog]**](DeploymentLog.md) |  | [optional] 
**cluster** | [**AbstractCluster**](AbstractCluster.md) |  | [optional] 
**is_scheduled_releases_paused** | **bool** |  | [optional] 
**queued_releases** | [**list[QueuedRelease]**](QueuedRelease.md) |  | [optional] 
**execution_time** | [**dict(str, ExecutionTime)**](ExecutionTime.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

