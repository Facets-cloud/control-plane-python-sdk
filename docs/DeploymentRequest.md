# DeploymentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_type** | **str** | CUSTOM | [optional] 
**extra_env** | **dict(str, str)** |  | [optional] 
**override_build_steps** | **list[str]** |  | 
**allow_destroy** | **bool** | false | [optional] 
**with_refresh** | **bool** | false | [optional] 
**force_release** | **bool** | true | [optional] 
**tf_version** | [**TfVersion**](TfVersion.md) |  | [optional] 
**release_comment** | **str** |  | [optional] 
**plan_code_build_id** | **str** |  | [optional] 
**hotfix_resources** | [**list[FacetsResource]**](FacetsResource.md) |  | [optional] 
**lock_id** | **str** |  | [optional] 
**can_queue** | **bool** |  | [optional] 
**parallel_release** | **bool** |  | [optional] [default to False]
**release_trace_id** | **str** |  | [optional] 
**queued_release_id** | **str** |  | [optional] 
**rollback_deployment_id** | **str** |  | [optional] 
**skip_state_check** | **bool** |  | [optional] 
**alpha** | **bool** |  | [optional] 
**approved_release** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

