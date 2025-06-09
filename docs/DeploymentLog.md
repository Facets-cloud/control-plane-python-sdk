# DeploymentLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_destroy** | **bool** |  | [optional] 
**app_deployments** | [**list[AppDeployment]**](AppDeployment.md) |  | [optional] 
**approved_release_id** | **str** |  | [optional] 
**changes_applied** | [**list[TerraformChange]**](TerraformChange.md) |  | [optional] 
**codebuild_id** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**deployment_context_file_path** | **str** |  | [optional] 
**deployment_context_version** | **str** |  | [optional] 
**deployment_job_type** | **str** |  | [optional] 
**deployment_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**error_logs** | [**list[RawError]**](RawError.md) |  | [optional] 
**finished_on** | **datetime** |  | [optional] 
**force_release** | **bool** |  | [optional] 
**hotfix_resources** | [**list[FacetsResource]**](FacetsResource.md) |  | [optional] 
**id** | **str** |  | [optional] 
**integration_test** | **bool** |  | [optional] 
**is_destroy** | **bool** |  | [optional] 
**migration_scripts_run** | [**list[MigrationScriptMetadata]**](MigrationScriptMetadata.md) |  | [optional] 
**override_build_steps** | **list[str]** |  | [optional] 
**parallel_release** | **bool** |  | [optional] 
**release_comment** | **str** |  | [optional] 
**release_reviewed_by** | **str** |  | [optional] 
**release_trace_id** | **str** |  | [optional] 
**release_type** | **str** |  | [optional] 
**rollback_deployment_id** | **str** |  | [optional] 
**signed_off** | **bool** |  | [optional] 
**stack_version** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**tf_version** | **str** |  | [optional] 
**time_taken_in_seconds** | **int** |  | [optional] 
**triggered_by** | **str** |  | [optional] 
**validation_responses** | [**list[ValidationResponse]**](ValidationResponse.md) |  | [optional] 
**validation_result** | [**ValidationResult**](ValidationResult.md) |  | [optional] 
**with_refresh** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

