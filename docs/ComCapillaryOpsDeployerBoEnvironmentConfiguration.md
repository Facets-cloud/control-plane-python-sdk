# ComCapillaryOpsDeployerBoEnvironmentConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubernetes_token** | **str** |  | [optional] 
**node_group** | **str** |  | [optional] 
**kubernetes_api_endpoint** | **str** |  | [optional] 
**private_dns_configuration** | [**ComCapillaryOpsDeployerBoExternalDnsConfiguration**](ComCapillaryOpsDeployerBoExternalDnsConfiguration.md) |  | [optional] 
**public_dns_configuration** | [**ComCapillaryOpsDeployerBoExternalDnsConfiguration**](ComCapillaryOpsDeployerBoExternalDnsConfiguration.md) |  | [optional] 
**s3_dump_aws_config** | [**ComCapillaryOpsDeployerBoS3DumpAwsConfig**](ComCapillaryOpsDeployerBoS3DumpAwsConfig.md) |  | [optional] 
**common_configs** | **dict(str, str)** |  | [optional] 
**common_credentials** | **dict(str, str)** |  | [optional] 
**ssl_configs** | [**ComCapillaryOpsDeployerBoSSLConfigs**](ComCapillaryOpsDeployerBoSSLConfigs.md) |  | [optional] 
**ecr_mirror_repo** | **str** |  | [optional] 
**k8s_logging_configuration** | [**ComCapillaryOpsDeployerBoK8sLoggingConfiguration**](ComCapillaryOpsDeployerBoK8sLoggingConfiguration.md) |  | [optional] 
**kube2_iam_configuration** | [**ComCapillaryOpsDeployerBoKube2IamConfiguration**](ComCapillaryOpsDeployerBoKube2IamConfiguration.md) |  | [optional] 
**spot_termination_handling_enabled** | **bool** |  | [optional] 
**new_relic_cluster_name** | **str** |  | [optional] 
**metric_server_enabled** | **bool** |  | [optional] 
**cluster_autoscaler_configuration** | [**ComCapillaryOpsDeployerBoClusterAutoscalerConfiguration**](ComCapillaryOpsDeployerBoClusterAutoscalerConfiguration.md) |  | [optional] 
**pre_deploy_task_enabled** | **bool** |  | [optional] 
**jmx_side_car_enabled** | **bool** |  | [optional] 
**resource_allocation_strategy_definition** | **dict(str, float)** |  | [optional] 
**requests_to_limits_ratio** | **float** |  | [optional] 
**filebeat_enabled** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

