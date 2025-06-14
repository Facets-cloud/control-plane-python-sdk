# swagger_client.UiCommonClusterControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cluster_schedules_using_post**](UiCommonClusterControllerApi.md#add_cluster_schedules_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/schedule | addClusterSchedules
[**add_tools_config_using_post**](UiCommonClusterControllerApi.md#add_tools_config_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/tools-config | addToolsConfig
[**attach_image_using_post**](UiCommonClusterControllerApi.md#attach_image_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/attach-image | attachImage
[**bulk_enable_disable_resources_using_put**](UiCommonClusterControllerApi.md#bulk_enable_disable_resources_using_put) | **PUT** /cc-ui/v1/clusters/{clusterId}/resource-enable-disable | bulkEnableDisableResources
[**copy_configurations_selective_using_put**](UiCommonClusterControllerApi.md#copy_configurations_selective_using_put) | **PUT** /cc-ui/v1/clusters/{clusterId}/copy-configurations-selective | Copy configurations from one cluster to another selectively
[**create_availability_schedule_using_post**](UiCommonClusterControllerApi.md#create_availability_schedule_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/availability-schedule | createAvailabilitySchedule
[**create_cluster_tf_details_using_post**](UiCommonClusterControllerApi.md#create_cluster_tf_details_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/tfRunConfigurations | createClusterTFDetails
[**create_draft_cluster_using_post**](UiCommonClusterControllerApi.md#create_draft_cluster_using_post) | **POST** /cc-ui/v1/clusters/draft-cluster | createDraftCluster
[**create_snapshot_using_post**](UiCommonClusterControllerApi.md#create_snapshot_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/dr/{resourceType}/snapshots/{instanceName} | createSnapshot
[**create_template_inputs_using_post**](UiCommonClusterControllerApi.md#create_template_inputs_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/templateInputs/{inputType}/items | createTemplateInputs
[**delete_availability_schedule_using_delete**](UiCommonClusterControllerApi.md#delete_availability_schedule_using_delete) | **DELETE** /cc-ui/v1/clusters/{clusterId}/availability-schedule/{availabilityScheduleId} | deleteAvailabilitySchedule
[**delete_cluster_force_using_delete**](UiCommonClusterControllerApi.md#delete_cluster_force_using_delete) | **DELETE** /cc-ui/v1/clusters/{clusterId}/force | deleteClusterForce
[**delete_cluster_schedule_using_delete**](UiCommonClusterControllerApi.md#delete_cluster_schedule_using_delete) | **DELETE** /cc-ui/v1/clusters/{clusterId}/schedule/{clusterScheduleId} | deleteClusterSchedule
[**delete_cluster_tf_details_using_delete**](UiCommonClusterControllerApi.md#delete_cluster_tf_details_using_delete) | **DELETE** /cc-ui/v1/clusters/{clusterId}/tfRunConfigurations | deleteClusterTFDetails
[**delete_cluster_using_delete1**](UiCommonClusterControllerApi.md#delete_cluster_using_delete1) | **DELETE** /cc-ui/v1/clusters/{clusterId} | deleteCluster
[**delete_overrides_using_delete**](UiCommonClusterControllerApi.md#delete_overrides_using_delete) | **DELETE** /cc-ui/v1/clusters/{clusterId}/overrides/{resourceType}/{resourceName} | deleteOverrides
[**delete_template_inputs_using_delete**](UiCommonClusterControllerApi.md#delete_template_inputs_using_delete) | **DELETE** /cc-ui/v1/clusters/{clusterId}/templateInputs/{inputType}/items/{uid} | deleteTemplateInputs
[**delete_tools_config_using_delete**](UiCommonClusterControllerApi.md#delete_tools_config_using_delete) | **DELETE** /cc-ui/v1/clusters/{clusterId}/tools-config | deleteToolsConfig
[**detach_image_using_delete**](UiCommonClusterControllerApi.md#detach_image_using_delete) | **DELETE** /cc-ui/v1/clusters/{clusterId}/detachImage | detachImage
[**edit_tools_config_using_put**](UiCommonClusterControllerApi.md#edit_tools_config_using_put) | **PUT** /cc-ui/v1/clusters/{clusterId}/tools-config/{toolsConfigId} | editToolsConfig
[**get_alerts_using_get**](UiCommonClusterControllerApi.md#get_alerts_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/alerts | getAlerts
[**get_all_template_inputs_using_get**](UiCommonClusterControllerApi.md#get_all_template_inputs_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/templateInputs/ | getAllTemplateInputs
[**get_availability_schedules_using_get**](UiCommonClusterControllerApi.md#get_availability_schedules_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/availability-schedule | getAvailabilitySchedules
[**get_cluster_common_using_get**](UiCommonClusterControllerApi.md#get_cluster_common_using_get) | **GET** /cc-ui/v1/clusters/{clusterId} | getClusterCommon
[**get_cluster_info_using_get**](UiCommonClusterControllerApi.md#get_cluster_info_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/info | getClusterInfo
[**get_cluster_metadata_using_get**](UiCommonClusterControllerApi.md#get_cluster_metadata_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/cluster-metadata | getClusterMetadata
[**get_cluster_schedules_using_get**](UiCommonClusterControllerApi.md#get_cluster_schedules_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/schedule | getClusterSchedules
[**get_cluster_tf_details_using_get**](UiCommonClusterControllerApi.md#get_cluster_tf_details_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/tfRunConfigurations | getClusterTFDetails
[**get_k8s_credentials_using_get**](UiCommonClusterControllerApi.md#get_k8s_credentials_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8sCredentials | getK8sCredentials
[**get_kube_config_using_get**](UiCommonClusterControllerApi.md#get_kube_config_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/kubeconfig | getKubeConfig
[**get_matched_modules_using_get**](UiCommonClusterControllerApi.md#get_matched_modules_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/match-modules | getMatchedModules
[**get_namespaces_in_use_by_dependent_clusters_using_get**](UiCommonClusterControllerApi.md#get_namespaces_in_use_by_dependent_clusters_using_get) | **GET** /cc-ui/v1/clusters/{baseClusterId}/base-env-in-use-namespaces | getNamespacesInUseByDependentClusters
[**get_open_alerts_using_get**](UiCommonClusterControllerApi.md#get_open_alerts_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/open-alerts | getOpenAlerts
[**get_overrides_using_get1**](UiCommonClusterControllerApi.md#get_overrides_using_get1) | **GET** /cc-ui/v1/clusters/{clusterId}/overrides | getOverrides
[**get_pinned_snapshot_using_get1**](UiCommonClusterControllerApi.md#get_pinned_snapshot_using_get1) | **GET** /cc-ui/v1/clusters/{clusterId}/dr/{resourceType}/snapshots/{instanceName}/pinnedSnapshot | getPinnedSnapshot
[**get_provided_resources_using_get**](UiCommonClusterControllerApi.md#get_provided_resources_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/providedResources | getProvidedResources
[**get_release_impacts_using_get**](UiCommonClusterControllerApi.md#get_release_impacts_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName}/release-impacts | getReleaseImpacts
[**get_resource_stats_using_get**](UiCommonClusterControllerApi.md#get_resource_stats_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/resource-stats | getResourceStats
[**get_template_input_by_uid_using_get**](UiCommonClusterControllerApi.md#get_template_input_by_uid_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/templateInputs/{inputType}/items/{uid} | getTemplateInputByUid
[**get_template_inputs_using_get**](UiCommonClusterControllerApi.md#get_template_inputs_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/templateInputs/{inputType}/items | getTemplateInputs
[**get_tools_config_using_get**](UiCommonClusterControllerApi.md#get_tools_config_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/tools-config | getToolsConfig
[**get_variable_counts_using_get**](UiCommonClusterControllerApi.md#get_variable_counts_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/variable-counts | getVariableCounts
[**get_vars_using_get**](UiCommonClusterControllerApi.md#get_vars_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/vars | getVars
[**get_vars_with_secrets_using_get**](UiCommonClusterControllerApi.md#get_vars_with_secrets_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/vars-with-secrets | getVarsWithSecrets
[**get_vars_with_status_using_get**](UiCommonClusterControllerApi.md#get_vars_with_status_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/varsWithStatus | getVarsWithStatus
[**get_vpn_profile_using_get**](UiCommonClusterControllerApi.md#get_vpn_profile_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/vpn-profile | getVPNProfile
[**list_snapshots_using_get1**](UiCommonClusterControllerApi.md#list_snapshots_using_get1) | **GET** /cc-ui/v1/clusters/{clusterId}/dr/{resourceType}/snapshots/{instanceName} | listSnapshots
[**override_sizing_using_post1**](UiCommonClusterControllerApi.md#override_sizing_using_post1) | **POST** /cc-ui/v1/clusters/{clusterId}/overrides | overrideSizing
[**pause_release_using_post**](UiCommonClusterControllerApi.md#pause_release_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/pause-release | pauseRelease
[**pin_snapshot_using_post1**](UiCommonClusterControllerApi.md#pin_snapshot_using_post1) | **POST** /cc-ui/v1/clusters/{clusterId}/dr/{resourceType}/snapshots/{instanceName}/pinnedSnapshot | pinSnapshot
[**refresh_kube_config_using_get**](UiCommonClusterControllerApi.md#refresh_kube_config_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/kubeconfig/refresh | refreshKubeConfig
[**remove_silence_using_delete**](UiCommonClusterControllerApi.md#remove_silence_using_delete) | **DELETE** /cc-ui/v1/clusters/{clusterId}/alerts/silence/{silenceId} | removeSilence
[**resource_details_using_get**](UiCommonClusterControllerApi.md#resource_details_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceDetails | resourceDetails
[**set_cluster_code_using_post**](UiCommonClusterControllerApi.md#set_cluster_code_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/setClusterCode | setClusterCode
[**silence_alerts_using_post**](UiCommonClusterControllerApi.md#silence_alerts_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/silence-alerts | silenceAlerts
[**update_availability_schedules_using_put**](UiCommonClusterControllerApi.md#update_availability_schedules_using_put) | **PUT** /cc-ui/v1/clusters/{clusterId}/availability-schedule/{scheduleId} | updateAvailabilitySchedules
[**update_cluster_branch_using_patch**](UiCommonClusterControllerApi.md#update_cluster_branch_using_patch) | **PATCH** /cc-ui/v1/clusters/{clusterId}/branch | updateClusterBranch
[**update_cluster_schedules_using_put**](UiCommonClusterControllerApi.md#update_cluster_schedules_using_put) | **PUT** /cc-ui/v1/clusters/{clusterId}/schedule/{clusterScheduleId} | updateClusterSchedules
[**update_cluster_tf_details_using_put**](UiCommonClusterControllerApi.md#update_cluster_tf_details_using_put) | **PUT** /cc-ui/v1/clusters/{clusterId}/tfRunConfigurations | updateClusterTFDetails
[**update_draft_cluster_using_put**](UiCommonClusterControllerApi.md#update_draft_cluster_using_put) | **PUT** /cc-ui/v1/clusters/draft-cluster/{clusterId} | updateDraftCluster
[**update_template_input_using_put**](UiCommonClusterControllerApi.md#update_template_input_using_put) | **PUT** /cc-ui/v1/clusters/{clusterId}/templateInputs/{inputType}/items/{uid} | updateTemplateInput
[**upsert_provided_resources_using_post**](UiCommonClusterControllerApi.md#upsert_provided_resources_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/providedResources | upsertProvidedResources
[**upsert_vars_using_post1**](UiCommonClusterControllerApi.md#upsert_vars_using_post1) | **POST** /cc-ui/v1/clusters/{clusterId}/vars/upsert | upsertVars

# **add_cluster_schedules_using_post**
> list[ClusterSchedule] add_cluster_schedules_using_post(body, cluster_id)

addClusterSchedules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScheduleRequest() # ScheduleRequest | request
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # addClusterSchedules
    api_response = api_instance.add_cluster_schedules_using_post(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->add_cluster_schedules_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScheduleRequest**](ScheduleRequest.md)| request | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**list[ClusterSchedule]**](ClusterSchedule.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tools_config_using_post**
> ToolsConfig add_tools_config_using_post(body, cluster_id)

addToolsConfig

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ToolsConfig() # ToolsConfig | toolsConfig
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # addToolsConfig
    api_response = api_instance.add_tools_config_using_post(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->add_tools_config_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ToolsConfig**](ToolsConfig.md)| toolsConfig | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**ToolsConfig**](ToolsConfig.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_image_using_post**
> attach_image_using_post(body, cluster_id)

attachImage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ImageOverrideRequest() # ImageOverrideRequest | request
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # attachImage
    api_instance.attach_image_using_post(body, cluster_id)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->attach_image_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageOverrideRequest**](ImageOverrideRequest.md)| request | 
 **cluster_id** | **str**| clusterId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_enable_disable_resources_using_put**
> bulk_enable_disable_resources_using_put(body, cluster_id)

bulkEnableDisableResources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ResourceEnableDisableRequest()] # list[ResourceEnableDisableRequest] | resourceEnableDisableRequestList
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # bulkEnableDisableResources
    api_instance.bulk_enable_disable_resources_using_put(body, cluster_id)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->bulk_enable_disable_resources_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ResourceEnableDisableRequest]**](ResourceEnableDisableRequest.md)| resourceEnableDisableRequestList | 
 **cluster_id** | **str**| clusterId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_configurations_selective_using_put**
> AbstractCluster copy_configurations_selective_using_put(body, cluster_id)

Copy configurations from one cluster to another selectively

Copies configurations from the source cluster to the target cluster. When mode is INCLUDE: Only specified configuration types are copied. When mode is EXCLUDE: All configuration types are copied except the specified ones.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CopyConfigurationsRequest() # CopyConfigurationsRequest | Request containing source cluster ID, selection mode (INCLUDE/EXCLUDE), and set of configuration types
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # Copy configurations from one cluster to another selectively
    api_response = api_instance.copy_configurations_selective_using_put(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->copy_configurations_selective_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CopyConfigurationsRequest**](CopyConfigurationsRequest.md)| Request containing source cluster ID, selection mode (INCLUDE/EXCLUDE), and set of configuration types | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**AbstractCluster**](AbstractCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_availability_schedule_using_post**
> create_availability_schedule_using_post(body, cluster_id)

createAvailabilitySchedule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ScheduleRequest()] # list[ScheduleRequest] | schedules
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # createAvailabilitySchedule
    api_instance.create_availability_schedule_using_post(body, cluster_id)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->create_availability_schedule_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ScheduleRequest]**](ScheduleRequest.md)| schedules | 
 **cluster_id** | **str**| clusterId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_tf_details_using_post**
> TFRunConfigurations create_cluster_tf_details_using_post(body, cluster_id)

createClusterTFDetails

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.TFRunConfigurations() # TFRunConfigurations | tfRunConfigurations
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # createClusterTFDetails
    api_response = api_instance.create_cluster_tf_details_using_post(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->create_cluster_tf_details_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TFRunConfigurations**](TFRunConfigurations.md)| tfRunConfigurations | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**TFRunConfigurations**](TFRunConfigurations.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_draft_cluster_using_post**
> AbstractCluster create_draft_cluster_using_post(body)

createDraftCluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.DraftClusterRequest() # DraftClusterRequest | clusterRequest

try:
    # createDraftCluster
    api_response = api_instance.create_draft_cluster_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->create_draft_cluster_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DraftClusterRequest**](DraftClusterRequest.md)| clusterRequest | 

### Return type

[**AbstractCluster**](AbstractCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snapshot_using_post**
> bool create_snapshot_using_post(cluster_id, instance_name, resource_type)

createSnapshot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
instance_name = 'instance_name_example' # str | instanceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # createSnapshot
    api_response = api_instance.create_snapshot_using_post(cluster_id, instance_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->create_snapshot_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **instance_name** | **str**| instanceName | 
 **resource_type** | **str**| resourceType | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_inputs_using_post**
> dict(str, list[StackTemplateInput]) create_template_inputs_using_post(body, cluster_id, input_type)

createTemplateInputs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.StackTemplateInput()] # list[StackTemplateInput] | templateInputs
cluster_id = 'cluster_id_example' # str | clusterId
input_type = 'input_type_example' # str | inputType

try:
    # createTemplateInputs
    api_response = api_instance.create_template_inputs_using_post(body, cluster_id, input_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->create_template_inputs_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[StackTemplateInput]**](StackTemplateInput.md)| templateInputs | 
 **cluster_id** | **str**| clusterId | 
 **input_type** | **str**| inputType | 

### Return type

**dict(str, list[StackTemplateInput])**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_availability_schedule_using_delete**
> delete_availability_schedule_using_delete(availability_schedule_id, cluster_id)

deleteAvailabilitySchedule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
availability_schedule_id = 'availability_schedule_id_example' # str | availabilityScheduleId
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # deleteAvailabilitySchedule
    api_instance.delete_availability_schedule_using_delete(availability_schedule_id, cluster_id)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_availability_schedule_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **availability_schedule_id** | **str**| availabilityScheduleId | 
 **cluster_id** | **str**| clusterId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_force_using_delete**
> bool delete_cluster_force_using_delete(cluster_id)

deleteClusterForce

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # deleteClusterForce
    api_response = api_instance.delete_cluster_force_using_delete(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_cluster_force_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_schedule_using_delete**
> list[ClusterSchedule] delete_cluster_schedule_using_delete(cluster_id, cluster_schedule_id)

deleteClusterSchedule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
cluster_schedule_id = 'cluster_schedule_id_example' # str | clusterScheduleId

try:
    # deleteClusterSchedule
    api_response = api_instance.delete_cluster_schedule_using_delete(cluster_id, cluster_schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_cluster_schedule_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **cluster_schedule_id** | **str**| clusterScheduleId | 

### Return type

[**list[ClusterSchedule]**](ClusterSchedule.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_tf_details_using_delete**
> TFRunConfigurations delete_cluster_tf_details_using_delete(cluster_id)

deleteClusterTFDetails

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # deleteClusterTFDetails
    api_response = api_instance.delete_cluster_tf_details_using_delete(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_cluster_tf_details_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**TFRunConfigurations**](TFRunConfigurations.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_using_delete1**
> bool delete_cluster_using_delete1(cluster_id)

deleteCluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # deleteCluster
    api_response = api_instance.delete_cluster_using_delete1(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_cluster_using_delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_overrides_using_delete**
> list[OverrideObject] delete_overrides_using_delete(cluster_id, resource_name, resource_type)

deleteOverrides

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # deleteOverrides
    api_response = api_instance.delete_overrides_using_delete(cluster_id, resource_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_overrides_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 

### Return type

[**list[OverrideObject]**](OverrideObject.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_inputs_using_delete**
> StackTemplateInput delete_template_inputs_using_delete(cluster_id, input_type, uid)

deleteTemplateInputs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
input_type = 'input_type_example' # str | inputType
uid = 'uid_example' # str | uid

try:
    # deleteTemplateInputs
    api_response = api_instance.delete_template_inputs_using_delete(cluster_id, input_type, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_template_inputs_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **input_type** | **str**| inputType | 
 **uid** | **str**| uid | 

### Return type

[**StackTemplateInput**](StackTemplateInput.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tools_config_using_delete**
> delete_tools_config_using_delete(cluster_id)

deleteToolsConfig

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # deleteToolsConfig
    api_instance.delete_tools_config_using_delete(cluster_id)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_tools_config_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_image_using_delete**
> detach_image_using_delete(body, cluster_id)

detachImage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ImageOverrideRequest() # ImageOverrideRequest | request
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # detachImage
    api_instance.detach_image_using_delete(body, cluster_id)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->detach_image_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageOverrideRequest**](ImageOverrideRequest.md)| request | 
 **cluster_id** | **str**| clusterId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_tools_config_using_put**
> ToolsConfig edit_tools_config_using_put(body, cluster_id, tools_config_id)

editToolsConfig

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ToolsConfig() # ToolsConfig | toolsConfig
cluster_id = 'cluster_id_example' # str | clusterId
tools_config_id = 'tools_config_id_example' # str | toolsConfigId

try:
    # editToolsConfig
    api_response = api_instance.edit_tools_config_using_put(body, cluster_id, tools_config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->edit_tools_config_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ToolsConfig**](ToolsConfig.md)| toolsConfig | 
 **cluster_id** | **str**| clusterId | 
 **tools_config_id** | **str**| toolsConfigId | 

### Return type

[**ToolsConfig**](ToolsConfig.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts_using_get**
> dict(str, object) get_alerts_using_get(cluster_id)

getAlerts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getAlerts
    api_response = api_instance.get_alerts_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_alerts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

**dict(str, object)**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_inputs_using_get**
> dict(str, list[StackTemplateInput]) get_all_template_inputs_using_get(cluster_id)

getAllTemplateInputs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getAllTemplateInputs
    api_response = api_instance.get_all_template_inputs_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_all_template_inputs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

**dict(str, list[StackTemplateInput])**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_availability_schedules_using_get**
> AvailabilitySchedule get_availability_schedules_using_get(cluster_id)

getAvailabilitySchedules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getAvailabilitySchedules
    api_response = api_instance.get_availability_schedules_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_availability_schedules_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**AvailabilitySchedule**](AvailabilitySchedule.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_common_using_get**
> AbstractCluster get_cluster_common_using_get(cluster_id)

getClusterCommon

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getClusterCommon
    api_response = api_instance.get_cluster_common_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_cluster_common_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**AbstractCluster**](AbstractCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_info_using_get**
> ClusterResponse get_cluster_info_using_get(cluster_id)

getClusterInfo

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getClusterInfo
    api_response = api_instance.get_cluster_info_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_cluster_info_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_metadata_using_get**
> ClusterMetadata get_cluster_metadata_using_get(cluster_id)

getClusterMetadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getClusterMetadata
    api_response = api_instance.get_cluster_metadata_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_cluster_metadata_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**ClusterMetadata**](ClusterMetadata.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_schedules_using_get**
> list[ClusterSchedule] get_cluster_schedules_using_get(cluster_id)

getClusterSchedules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getClusterSchedules
    api_response = api_instance.get_cluster_schedules_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_cluster_schedules_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**list[ClusterSchedule]**](ClusterSchedule.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_tf_details_using_get**
> TFRunConfigurations get_cluster_tf_details_using_get(cluster_id)

getClusterTFDetails

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getClusterTFDetails
    api_response = api_instance.get_cluster_tf_details_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_cluster_tf_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**TFRunConfigurations**](TFRunConfigurations.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_k8s_credentials_using_get**
> KubernetesCredential get_k8s_credentials_using_get(cluster_id, refresh_permissions=refresh_permissions)

getK8sCredentials

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
refresh_permissions = true # bool | refreshPermissions (optional) (default to true)

try:
    # getK8sCredentials
    api_response = api_instance.get_k8s_credentials_using_get(cluster_id, refresh_permissions=refresh_permissions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_k8s_credentials_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **refresh_permissions** | **bool**| refreshPermissions | [optional] [default to true]

### Return type

[**KubernetesCredential**](KubernetesCredential.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kube_config_using_get**
> str get_kube_config_using_get(cluster_id)

getKubeConfig

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getKubeConfig
    api_response = api_instance.get_kube_config_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_kube_config_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_matched_modules_using_get**
> MatchedModuleDTO get_matched_modules_using_get(cluster_id)

getMatchedModules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getMatchedModules
    api_response = api_instance.get_matched_modules_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_matched_modules_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**MatchedModuleDTO**](MatchedModuleDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaces_in_use_by_dependent_clusters_using_get**
> dict(str, str) get_namespaces_in_use_by_dependent_clusters_using_get(base_cluster_id)

getNamespacesInUseByDependentClusters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
base_cluster_id = 'base_cluster_id_example' # str | baseClusterId

try:
    # getNamespacesInUseByDependentClusters
    api_response = api_instance.get_namespaces_in_use_by_dependent_clusters_using_get(base_cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_namespaces_in_use_by_dependent_clusters_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_cluster_id** | **str**| baseClusterId | 

### Return type

**dict(str, str)**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_alerts_using_get**
> dict(str, object) get_open_alerts_using_get(cluster_id)

getOpenAlerts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getOpenAlerts
    api_response = api_instance.get_open_alerts_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_open_alerts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

**dict(str, object)**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overrides_using_get1**
> list[OverrideObject] get_overrides_using_get1(cluster_id)

getOverrides

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getOverrides
    api_response = api_instance.get_overrides_using_get1(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_overrides_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**list[OverrideObject]**](OverrideObject.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pinned_snapshot_using_get1**
> SnapshotInfo get_pinned_snapshot_using_get1(cluster_id, instance_name, resource_type)

getPinnedSnapshot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
instance_name = 'instance_name_example' # str | instanceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # getPinnedSnapshot
    api_response = api_instance.get_pinned_snapshot_using_get1(cluster_id, instance_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_pinned_snapshot_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **instance_name** | **str**| instanceName | 
 **resource_type** | **str**| resourceType | 

### Return type

[**SnapshotInfo**](SnapshotInfo.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provided_resources_using_get**
> ProvidedResources get_provided_resources_using_get(cluster_id)

getProvidedResources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getProvidedResources
    api_response = api_instance.get_provided_resources_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_provided_resources_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**ProvidedResources**](ProvidedResources.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_impacts_using_get**
> PageResourceReleaseImpact get_release_impacts_using_get(cluster_id, resource_name, resource_type, attribute=attribute, change_type=change_type, end=end, page_number=page_number, page_size=page_size, release_type=release_type, start=start, triggered_by=triggered_by)

getReleaseImpacts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
attribute = 'attribute_example' # str | attribute (optional)
change_type = 'change_type_example' # str | changeType (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | end (optional)
page_number = 0 # int | pageNumber (optional) (default to 0)
page_size = 50 # int | pageSize (optional) (default to 50)
release_type = 'release_type_example' # str | releaseType (optional)
start = '2013-10-20T19:20:30+01:00' # datetime | start (optional)
triggered_by = 'triggered_by_example' # str | triggeredBy (optional)

try:
    # getReleaseImpacts
    api_response = api_instance.get_release_impacts_using_get(cluster_id, resource_name, resource_type, attribute=attribute, change_type=change_type, end=end, page_number=page_number, page_size=page_size, release_type=release_type, start=start, triggered_by=triggered_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_release_impacts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **attribute** | **str**| attribute | [optional] 
 **change_type** | **str**| changeType | [optional] 
 **end** | **datetime**| end | [optional] 
 **page_number** | **int**| pageNumber | [optional] [default to 0]
 **page_size** | **int**| pageSize | [optional] [default to 50]
 **release_type** | **str**| releaseType | [optional] 
 **start** | **datetime**| start | [optional] 
 **triggered_by** | **str**| triggeredBy | [optional] 

### Return type

[**PageResourceReleaseImpact**](PageResourceReleaseImpact.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_stats_using_get**
> BlueprintFileSummaryDto get_resource_stats_using_get(cluster_id)

getResourceStats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getResourceStats
    api_response = api_instance.get_resource_stats_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_resource_stats_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**BlueprintFileSummaryDto**](BlueprintFileSummaryDto.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_input_by_uid_using_get**
> StackTemplateInput get_template_input_by_uid_using_get(cluster_id, input_type, uid)

getTemplateInputByUid

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
input_type = 'input_type_example' # str | inputType
uid = 'uid_example' # str | uid

try:
    # getTemplateInputByUid
    api_response = api_instance.get_template_input_by_uid_using_get(cluster_id, input_type, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_template_input_by_uid_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **input_type** | **str**| inputType | 
 **uid** | **str**| uid | 

### Return type

[**StackTemplateInput**](StackTemplateInput.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_inputs_using_get**
> list[StackTemplateInput] get_template_inputs_using_get(cluster_id, input_type)

getTemplateInputs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
input_type = 'input_type_example' # str | inputType

try:
    # getTemplateInputs
    api_response = api_instance.get_template_inputs_using_get(cluster_id, input_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_template_inputs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **input_type** | **str**| inputType | 

### Return type

[**list[StackTemplateInput]**](StackTemplateInput.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tools_config_using_get**
> ToolsConfig get_tools_config_using_get(cluster_id)

getToolsConfig

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getToolsConfig
    api_response = api_instance.get_tools_config_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_tools_config_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**ToolsConfig**](ToolsConfig.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variable_counts_using_get**
> VariableCountDto get_variable_counts_using_get(cluster_id)

getVariableCounts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getVariableCounts
    api_response = api_instance.get_variable_counts_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_variable_counts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**VariableCountDto**](VariableCountDto.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vars_using_get**
> AbstractCluster get_vars_using_get(cluster_id)

getVars

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getVars
    api_response = api_instance.get_vars_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_vars_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**AbstractCluster**](AbstractCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vars_with_secrets_using_get**
> AbstractCluster get_vars_with_secrets_using_get(cluster_id)

getVarsWithSecrets

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getVarsWithSecrets
    api_response = api_instance.get_vars_with_secrets_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_vars_with_secrets_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**AbstractCluster**](AbstractCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vars_with_status_using_get**
> dict(str, Variables) get_vars_with_status_using_get(cluster_id)

getVarsWithStatus

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getVarsWithStatus
    api_response = api_instance.get_vars_with_status_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_vars_with_status_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**dict(str, Variables)**](Variables.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpn_profile_using_get**
> str get_vpn_profile_using_get(cluster_id)

getVPNProfile

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getVPNProfile
    api_response = api_instance.get_vpn_profile_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_vpn_profile_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshots_using_get1**
> list[SnapshotInfo] list_snapshots_using_get1(cluster_id, instance_name, resource_type)

listSnapshots

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
instance_name = 'instance_name_example' # str | instanceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # listSnapshots
    api_response = api_instance.list_snapshots_using_get1(cluster_id, instance_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->list_snapshots_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **instance_name** | **str**| instanceName | 
 **resource_type** | **str**| resourceType | 

### Return type

[**list[SnapshotInfo]**](SnapshotInfo.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **override_sizing_using_post1**
> list[OverrideObject] override_sizing_using_post1(body, cluster_id)

overrideSizing

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.OverrideRequest()] # list[OverrideRequest] | request
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # overrideSizing
    api_response = api_instance.override_sizing_using_post1(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->override_sizing_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[OverrideRequest]**](OverrideRequest.md)| request | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**list[OverrideObject]**](OverrideObject.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_release_using_post**
> str pause_release_using_post(body, cluster_id)

pauseRelease

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.PauseReleaseRequest() # PauseReleaseRequest | pauseReleaseRequest
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # pauseRelease
    api_response = api_instance.pause_release_using_post(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->pause_release_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PauseReleaseRequest**](PauseReleaseRequest.md)| pauseReleaseRequest | 
 **cluster_id** | **str**| clusterId | 

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pin_snapshot_using_post1**
> SnapshotInfo pin_snapshot_using_post1(body, cluster_id, instance_name, resource_type)

pinSnapshot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.SnapshotInfo() # SnapshotInfo | snapshotInfo
cluster_id = 'cluster_id_example' # str | clusterId
instance_name = 'instance_name_example' # str | instanceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # pinSnapshot
    api_response = api_instance.pin_snapshot_using_post1(body, cluster_id, instance_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->pin_snapshot_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SnapshotInfo**](SnapshotInfo.md)| snapshotInfo | 
 **cluster_id** | **str**| clusterId | 
 **instance_name** | **str**| instanceName | 
 **resource_type** | **str**| resourceType | 

### Return type

[**SnapshotInfo**](SnapshotInfo.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_kube_config_using_get**
> bool refresh_kube_config_using_get(cluster_id)

refreshKubeConfig

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # refreshKubeConfig
    api_response = api_instance.refresh_kube_config_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->refresh_kube_config_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_silence_using_delete**
> dict(str, object) remove_silence_using_delete(cluster_id, silence_id)

removeSilence

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
silence_id = 'silence_id_example' # str | silenceId

try:
    # removeSilence
    api_response = api_instance.remove_silence_using_delete(cluster_id, silence_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->remove_silence_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **silence_id** | **str**| silenceId | 

### Return type

**dict(str, object)**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_details_using_get**
> list[ResourceDetails] resource_details_using_get(cluster_id)

resourceDetails

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # resourceDetails
    api_response = api_instance.resource_details_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->resource_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**list[ResourceDetails]**](ResourceDetails.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cluster_code_using_post**
> bool set_cluster_code_using_post(cluster_id)

setClusterCode

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # setClusterCode
    api_response = api_instance.set_cluster_code_using_post(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->set_cluster_code_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **silence_alerts_using_post**
> dict(str, object) silence_alerts_using_post(body, cluster_id)

silenceAlerts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.SilenceAlarmRequest() # SilenceAlarmRequest | request
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # silenceAlerts
    api_response = api_instance.silence_alerts_using_post(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->silence_alerts_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SilenceAlarmRequest**](SilenceAlarmRequest.md)| request | 
 **cluster_id** | **str**| clusterId | 

### Return type

**dict(str, object)**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_availability_schedules_using_put**
> update_availability_schedules_using_put(body, cluster_id, schedule_id)

updateAvailabilitySchedules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ScheduleRequest()] # list[ScheduleRequest] | schedules
cluster_id = 'cluster_id_example' # str | clusterId
schedule_id = 'schedule_id_example' # str | scheduleId

try:
    # updateAvailabilitySchedules
    api_instance.update_availability_schedules_using_put(body, cluster_id, schedule_id)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->update_availability_schedules_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ScheduleRequest]**](ScheduleRequest.md)| schedules | 
 **cluster_id** | **str**| clusterId | 
 **schedule_id** | **str**| scheduleId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_branch_using_patch**
> AbstractCluster update_cluster_branch_using_patch(body, cluster_id)

updateClusterBranch

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.BranchUpdateRequest() # BranchUpdateRequest | req
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # updateClusterBranch
    api_response = api_instance.update_cluster_branch_using_patch(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->update_cluster_branch_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BranchUpdateRequest**](BranchUpdateRequest.md)| req | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**AbstractCluster**](AbstractCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_schedules_using_put**
> list[ClusterSchedule] update_cluster_schedules_using_put(body, cluster_id, cluster_schedule_id)

updateClusterSchedules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScheduleRequest() # ScheduleRequest | request
cluster_id = 'cluster_id_example' # str | clusterId
cluster_schedule_id = 'cluster_schedule_id_example' # str | clusterScheduleId

try:
    # updateClusterSchedules
    api_response = api_instance.update_cluster_schedules_using_put(body, cluster_id, cluster_schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->update_cluster_schedules_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScheduleRequest**](ScheduleRequest.md)| request | 
 **cluster_id** | **str**| clusterId | 
 **cluster_schedule_id** | **str**| clusterScheduleId | 

### Return type

[**list[ClusterSchedule]**](ClusterSchedule.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_tf_details_using_put**
> TFRunConfigurations update_cluster_tf_details_using_put(body, cluster_id)

updateClusterTFDetails

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.TFRunConfigurations() # TFRunConfigurations | tfRunConfigurations
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # updateClusterTFDetails
    api_response = api_instance.update_cluster_tf_details_using_put(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->update_cluster_tf_details_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TFRunConfigurations**](TFRunConfigurations.md)| tfRunConfigurations | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**TFRunConfigurations**](TFRunConfigurations.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_draft_cluster_using_put**
> AbstractCluster update_draft_cluster_using_put(body, cluster_id)

updateDraftCluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.DraftClusterRequest() # DraftClusterRequest | clusterRequest
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # updateDraftCluster
    api_response = api_instance.update_draft_cluster_using_put(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->update_draft_cluster_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DraftClusterRequest**](DraftClusterRequest.md)| clusterRequest | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**AbstractCluster**](AbstractCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_input_using_put**
> StackTemplateInput update_template_input_using_put(body, cluster_id, input_type, uid)

updateTemplateInput

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.StackTemplateInput() # StackTemplateInput | templateInput
cluster_id = 'cluster_id_example' # str | clusterId
input_type = 'input_type_example' # str | inputType
uid = 'uid_example' # str | uid

try:
    # updateTemplateInput
    api_response = api_instance.update_template_input_using_put(body, cluster_id, input_type, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->update_template_input_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StackTemplateInput**](StackTemplateInput.md)| templateInput | 
 **cluster_id** | **str**| clusterId | 
 **input_type** | **str**| inputType | 
 **uid** | **str**| uid | 

### Return type

[**StackTemplateInput**](StackTemplateInput.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_provided_resources_using_post**
> ProvidedResources upsert_provided_resources_using_post(body, cluster_id)

upsertProvidedResources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProvidedResources() # ProvidedResources | providedResources
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # upsertProvidedResources
    api_response = api_instance.upsert_provided_resources_using_post(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->upsert_provided_resources_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProvidedResources**](ProvidedResources.md)| providedResources | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**ProvidedResources**](ProvidedResources.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_vars_using_post1**
> AbstractCluster upsert_vars_using_post1(body, cluster_id)

upsertVars

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, str) | clusterVars
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # upsertVars
    api_response = api_instance.upsert_vars_using_post1(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->upsert_vars_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, str)**](dict.md)| clusterVars | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**AbstractCluster**](AbstractCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

