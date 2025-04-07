# EnvironmentConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_autoscaler_configuration** | [**ClusterAutoscalerConfiguration**](ClusterAutoscalerConfiguration.md) |  | [optional] 
**common_configs** | **dict(str, str)** |  | [optional] 
**common_credentials** | **dict(str, str)** |  | [optional] 
**ecr_mirror_repo** | **str** |  | [optional] 
**filebeat_enabled** | **bool** |  | [optional] 
**jmx_side_car_enabled** | **bool** |  | [optional] 
**k8s_logging_configuration** | [**K8sLoggingConfiguration**](K8sLoggingConfiguration.md) |  | [optional] 
**kube2_iam_configuration** | [**Kube2IamConfiguration**](Kube2IamConfiguration.md) |  | [optional] 
**kubernetes_api_endpoint** | **str** |  | [optional] 
**kubernetes_token** | **str** |  | [optional] 
**metric_server_enabled** | **bool** |  | [optional] 
**new_relic_cluster_name** | **str** |  | [optional] 
**node_group** | **str** |  | [optional] 
**pre_deploy_task_enabled** | **bool** |  | [optional] 
**private_dns_configuration** | [**ExternalDnsConfiguration**](ExternalDnsConfiguration.md) |  | [optional] 
**public_dns_configuration** | [**ExternalDnsConfiguration**](ExternalDnsConfiguration.md) |  | [optional] 
**requests_to_limits_ratio** | **float** |  | [optional] 
**resource_allocation_strategy_definition** | **dict(str, float)** |  | [optional] 
**s3_dump_aws_config** | [**S3DumpAwsConfig**](S3DumpAwsConfig.md) |  | [optional] 
**spot_termination_handling_enabled** | **bool** |  | [optional] 
**ssl_configs** | [**SSLConfigs**](SSLConfigs.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


