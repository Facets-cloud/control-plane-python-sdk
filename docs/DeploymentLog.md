# DeploymentLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deployment_job_type** | **str** |  | [optional] 
**codebuild_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**finished_on** | **datetime** |  | [optional] 
**time_taken_in_seconds** | **int** |  | [optional] 
**release_type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**changes_applied** | [**list[TerraformChange]**](TerraformChange.md) |  | [optional] 
**app_deployments** | [**list[AppDeployment]**](AppDeployment.md) |  | [optional] 
**migration_scripts_run** | [**list[MigrationScriptMetadata]**](MigrationScriptMetadata.md) |  | [optional] 
**error_logs** | [**list[RawError]**](RawError.md) |  | [optional] 
**deployment_type** | **str** |  | [optional] 
**stack_version** | **str** |  | [optional] 
**tf_version** | **str** |  | [optional] 
**signed_off** | **bool** |  | [optional] 
**deployment_context_version** | **str** |  | [optional] 
**triggered_by** | **str** |  | [optional] 
**override_build_steps** | **list[str]** |  | [optional] 
**integration_test** | **bool** |  | [optional] 
**with_refresh** | **bool** |  | [optional] 
**is_destroy** | **bool** |  | [optional] 
**allow_destroy** | **bool** |  | [optional] 
**force_release** | **bool** |  | [optional] 
**validation_result** | [**ValidationResult**](ValidationResult.md) |  | [optional] 
**deployment_context_file_path** | **str** |  | [optional] 
**release_comment** | **str** |  | [optional] 
**hotfix_resources** | [**list[FacetsResource]**](FacetsResource.md) |  | [optional] 
**release_reviewed_by** | **str** |  | [optional] 
**approved_release_id** | **str** |  | [optional] 
**validation_responses** | [**list[ValidationResponse]**](ValidationResponse.md) |  | [optional] 
**release_trace_id** | **str** |  | [optional] 
**rollback_deployment_id** | **str** |  | [optional] 
**parallel_release** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

