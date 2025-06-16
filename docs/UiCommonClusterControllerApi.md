# swagger_client.UiCommonClusterControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cluster_schedules**](UiCommonClusterControllerApi.md#add_cluster_schedules) | **POST** /cc-ui/v1/clusters/{clusterId}/schedule | 
[**add_tools_config**](UiCommonClusterControllerApi.md#add_tools_config) | **POST** /cc-ui/v1/clusters/{clusterId}/tools-config | 
[**attach_image**](UiCommonClusterControllerApi.md#attach_image) | **POST** /cc-ui/v1/clusters/{clusterId}/attach-image | 
[**bulk_enable_disable_resources**](UiCommonClusterControllerApi.md#bulk_enable_disable_resources) | **PUT** /cc-ui/v1/clusters/{clusterId}/resource-enable-disable | 
[**copy_configurations_selective**](UiCommonClusterControllerApi.md#copy_configurations_selective) | **PUT** /cc-ui/v1/clusters/{clusterId}/copy-configurations-selective | Copy configurations from one cluster to another selectively
[**create_availability_schedule**](UiCommonClusterControllerApi.md#create_availability_schedule) | **POST** /cc-ui/v1/clusters/{clusterId}/availability-schedule | 
[**create_cluster_tf_details**](UiCommonClusterControllerApi.md#create_cluster_tf_details) | **POST** /cc-ui/v1/clusters/{clusterId}/tfRunConfigurations | 
[**create_draft_cluster1**](UiCommonClusterControllerApi.md#create_draft_cluster1) | **POST** /cc-ui/v1/clusters/draft-cluster | 
[**create_snapshot**](UiCommonClusterControllerApi.md#create_snapshot) | **POST** /cc-ui/v1/clusters/{clusterId}/dr/{resourceType}/snapshots/{instanceName} | 
[**create_template_inputs**](UiCommonClusterControllerApi.md#create_template_inputs) | **POST** /cc-ui/v1/clusters/{clusterId}/templateInputs/{inputType}/items | 
[**delete_availability_schedule**](UiCommonClusterControllerApi.md#delete_availability_schedule) | **DELETE** /cc-ui/v1/clusters/{clusterId}/availability-schedule/{availabilityScheduleId} | 
[**delete_cluster1**](UiCommonClusterControllerApi.md#delete_cluster1) | **DELETE** /cc-ui/v1/clusters/{clusterId} | 
[**delete_cluster_force**](UiCommonClusterControllerApi.md#delete_cluster_force) | **DELETE** /cc-ui/v1/clusters/{clusterId}/force | 
[**delete_cluster_schedule**](UiCommonClusterControllerApi.md#delete_cluster_schedule) | **DELETE** /cc-ui/v1/clusters/{clusterId}/schedule/{clusterScheduleId} | 
[**delete_cluster_tf_details**](UiCommonClusterControllerApi.md#delete_cluster_tf_details) | **DELETE** /cc-ui/v1/clusters/{clusterId}/tfRunConfigurations | 
[**delete_overrides**](UiCommonClusterControllerApi.md#delete_overrides) | **DELETE** /cc-ui/v1/clusters/{clusterId}/overrides/{resourceType}/{resourceName} | 
[**delete_template_inputs**](UiCommonClusterControllerApi.md#delete_template_inputs) | **DELETE** /cc-ui/v1/clusters/{clusterId}/templateInputs/{inputType}/items/{uid} | 
[**delete_tools_config**](UiCommonClusterControllerApi.md#delete_tools_config) | **DELETE** /cc-ui/v1/clusters/{clusterId}/tools-config | 
[**detach_image**](UiCommonClusterControllerApi.md#detach_image) | **DELETE** /cc-ui/v1/clusters/{clusterId}/detachImage | 
[**edit_tools_config**](UiCommonClusterControllerApi.md#edit_tools_config) | **PUT** /cc-ui/v1/clusters/{clusterId}/tools-config/{toolsConfigId} | 
[**get_alerts**](UiCommonClusterControllerApi.md#get_alerts) | **GET** /cc-ui/v1/clusters/{clusterId}/alerts | 
[**get_all_template_inputs**](UiCommonClusterControllerApi.md#get_all_template_inputs) | **GET** /cc-ui/v1/clusters/{clusterId}/templateInputs/ | 
[**get_availability_schedules**](UiCommonClusterControllerApi.md#get_availability_schedules) | **GET** /cc-ui/v1/clusters/{clusterId}/availability-schedule | 
[**get_cluster_common**](UiCommonClusterControllerApi.md#get_cluster_common) | **GET** /cc-ui/v1/clusters/{clusterId} | 
[**get_cluster_info**](UiCommonClusterControllerApi.md#get_cluster_info) | **GET** /cc-ui/v1/clusters/{clusterId}/info | 
[**get_cluster_metadata**](UiCommonClusterControllerApi.md#get_cluster_metadata) | **GET** /cc-ui/v1/clusters/{clusterId}/cluster-metadata | 
[**get_cluster_schedules**](UiCommonClusterControllerApi.md#get_cluster_schedules) | **GET** /cc-ui/v1/clusters/{clusterId}/schedule | 
[**get_cluster_tf_details**](UiCommonClusterControllerApi.md#get_cluster_tf_details) | **GET** /cc-ui/v1/clusters/{clusterId}/tfRunConfigurations | 
[**get_k8s_credentials**](UiCommonClusterControllerApi.md#get_k8s_credentials) | **GET** /cc-ui/v1/clusters/{clusterId}/k8sCredentials | 
[**get_kube_config**](UiCommonClusterControllerApi.md#get_kube_config) | **GET** /cc-ui/v1/clusters/{clusterId}/kubeconfig | 
[**get_matched_modules**](UiCommonClusterControllerApi.md#get_matched_modules) | **GET** /cc-ui/v1/clusters/{clusterId}/match-modules | 
[**get_namespaces_in_use_by_dependent_clusters**](UiCommonClusterControllerApi.md#get_namespaces_in_use_by_dependent_clusters) | **GET** /cc-ui/v1/clusters/{baseClusterId}/base-env-in-use-namespaces | 
[**get_open_alerts**](UiCommonClusterControllerApi.md#get_open_alerts) | **GET** /cc-ui/v1/clusters/{clusterId}/open-alerts | 
[**get_overrides2**](UiCommonClusterControllerApi.md#get_overrides2) | **GET** /cc-ui/v1/clusters/{clusterId}/overrides | 
[**get_pinned_snapshot1**](UiCommonClusterControllerApi.md#get_pinned_snapshot1) | **GET** /cc-ui/v1/clusters/{clusterId}/dr/{resourceType}/snapshots/{instanceName}/pinnedSnapshot | 
[**get_provided_resources**](UiCommonClusterControllerApi.md#get_provided_resources) | **GET** /cc-ui/v1/clusters/{clusterId}/providedResources | 
[**get_release_impacts**](UiCommonClusterControllerApi.md#get_release_impacts) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName}/release-impacts | 
[**get_resource_stats**](UiCommonClusterControllerApi.md#get_resource_stats) | **GET** /cc-ui/v1/clusters/{clusterId}/resource-stats | 
[**get_template_input_by_uid**](UiCommonClusterControllerApi.md#get_template_input_by_uid) | **GET** /cc-ui/v1/clusters/{clusterId}/templateInputs/{inputType}/items/{uid} | 
[**get_template_inputs**](UiCommonClusterControllerApi.md#get_template_inputs) | **GET** /cc-ui/v1/clusters/{clusterId}/templateInputs/{inputType}/items | 
[**get_tools_config**](UiCommonClusterControllerApi.md#get_tools_config) | **GET** /cc-ui/v1/clusters/{clusterId}/tools-config | 
[**get_variable_counts**](UiCommonClusterControllerApi.md#get_variable_counts) | **GET** /cc-ui/v1/clusters/{clusterId}/variable-counts | 
[**get_vars**](UiCommonClusterControllerApi.md#get_vars) | **GET** /cc-ui/v1/clusters/{clusterId}/vars | 
[**get_vars_with_secrets**](UiCommonClusterControllerApi.md#get_vars_with_secrets) | **GET** /cc-ui/v1/clusters/{clusterId}/vars-with-secrets | 
[**get_vars_with_status**](UiCommonClusterControllerApi.md#get_vars_with_status) | **GET** /cc-ui/v1/clusters/{clusterId}/varsWithStatus | 
[**get_vpn_profile**](UiCommonClusterControllerApi.md#get_vpn_profile) | **GET** /cc-ui/v1/clusters/{clusterId}/vpn-profile | 
[**list_snapshots1**](UiCommonClusterControllerApi.md#list_snapshots1) | **GET** /cc-ui/v1/clusters/{clusterId}/dr/{resourceType}/snapshots/{instanceName} | 
[**override_sizing1**](UiCommonClusterControllerApi.md#override_sizing1) | **POST** /cc-ui/v1/clusters/{clusterId}/overrides | 
[**pause_release**](UiCommonClusterControllerApi.md#pause_release) | **POST** /cc-ui/v1/clusters/{clusterId}/pause-release | 
[**pin_snapshot1**](UiCommonClusterControllerApi.md#pin_snapshot1) | **POST** /cc-ui/v1/clusters/{clusterId}/dr/{resourceType}/snapshots/{instanceName}/pinnedSnapshot | 
[**refresh_kube_config**](UiCommonClusterControllerApi.md#refresh_kube_config) | **GET** /cc-ui/v1/clusters/{clusterId}/kubeconfig/refresh | 
[**remove_silence**](UiCommonClusterControllerApi.md#remove_silence) | **DELETE** /cc-ui/v1/clusters/{clusterId}/alerts/silence/{silenceId} | 
[**resource_details**](UiCommonClusterControllerApi.md#resource_details) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceDetails | 
[**set_cluster_code**](UiCommonClusterControllerApi.md#set_cluster_code) | **POST** /cc-ui/v1/clusters/{clusterId}/setClusterCode | 
[**silence_alerts**](UiCommonClusterControllerApi.md#silence_alerts) | **POST** /cc-ui/v1/clusters/{clusterId}/silence-alerts | 
[**update_availability_schedules**](UiCommonClusterControllerApi.md#update_availability_schedules) | **PUT** /cc-ui/v1/clusters/{clusterId}/availability-schedule/{scheduleId} | 
[**update_cluster_branch**](UiCommonClusterControllerApi.md#update_cluster_branch) | **PATCH** /cc-ui/v1/clusters/{clusterId}/branch | 
[**update_cluster_schedules**](UiCommonClusterControllerApi.md#update_cluster_schedules) | **PUT** /cc-ui/v1/clusters/{clusterId}/schedule/{clusterScheduleId} | 
[**update_cluster_tf_details**](UiCommonClusterControllerApi.md#update_cluster_tf_details) | **PUT** /cc-ui/v1/clusters/{clusterId}/tfRunConfigurations | 
[**update_draft_cluster**](UiCommonClusterControllerApi.md#update_draft_cluster) | **PUT** /cc-ui/v1/clusters/draft-cluster/{clusterId} | 
[**update_template_input**](UiCommonClusterControllerApi.md#update_template_input) | **PUT** /cc-ui/v1/clusters/{clusterId}/templateInputs/{inputType}/items/{uid} | 
[**upsert_provided_resources**](UiCommonClusterControllerApi.md#upsert_provided_resources) | **POST** /cc-ui/v1/clusters/{clusterId}/providedResources | 
[**upsert_vars1**](UiCommonClusterControllerApi.md#upsert_vars1) | **POST** /cc-ui/v1/clusters/{clusterId}/vars/upsert | 

# **add_cluster_schedules**
> list[ComCapillaryOpsCpBoClusterSchedule] add_cluster_schedules(body, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsScheduleRequest() # ComCapillaryOpsCpBoRequestsScheduleRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.add_cluster_schedules(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->add_cluster_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsScheduleRequest**](ComCapillaryOpsCpBoRequestsScheduleRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoClusterSchedule]**](ComCapillaryOpsCpBoClusterSchedule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tools_config**
> ComCapillaryOpsCpBoToolsConfig add_tools_config(body, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoToolsConfig() # ComCapillaryOpsCpBoToolsConfig | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.add_tools_config(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->add_tools_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoToolsConfig**](ComCapillaryOpsCpBoToolsConfig.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoToolsConfig**](ComCapillaryOpsCpBoToolsConfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_image**
> attach_image(body, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsImageOverrideRequest() # ComCapillaryOpsCpBoRequestsImageOverrideRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_instance.attach_image(body, cluster_id)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->attach_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsImageOverrideRequest**](ComCapillaryOpsCpBoRequestsImageOverrideRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_enable_disable_resources**
> bulk_enable_disable_resources(body, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ComCapillaryOpsCpBoResoucesResourceEnableDisableRequest()] # list[ComCapillaryOpsCpBoResoucesResourceEnableDisableRequest] | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_instance.bulk_enable_disable_resources(body, cluster_id)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->bulk_enable_disable_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ComCapillaryOpsCpBoResoucesResourceEnableDisableRequest]**](ComCapillaryOpsCpBoResoucesResourceEnableDisableRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_configurations_selective**
> ComCapillaryOpsCpBoAbstractCluster copy_configurations_selective(body, cluster_id)

Copy configurations from one cluster to another selectively

Copies configurations from the source cluster to the target cluster. When mode is INCLUDE: Only specified configuration types are copied. When mode is EXCLUDE: All configuration types are copied except the specified ones.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsCopyConfigurationsRequest() # ComCapillaryOpsCpBoRequestsCopyConfigurationsRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    # Copy configurations from one cluster to another selectively
    api_response = api_instance.copy_configurations_selective(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->copy_configurations_selective: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsCopyConfigurationsRequest**](ComCapillaryOpsCpBoRequestsCopyConfigurationsRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAbstractCluster**](ComCapillaryOpsCpBoAbstractCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_availability_schedule**
> create_availability_schedule(body, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ComCapillaryOpsCpBoRequestsScheduleRequest()] # list[ComCapillaryOpsCpBoRequestsScheduleRequest] | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_instance.create_availability_schedule(body, cluster_id)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->create_availability_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ComCapillaryOpsCpBoRequestsScheduleRequest]**](ComCapillaryOpsCpBoRequestsScheduleRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_tf_details**
> ComCapillaryOpsCpBoTFRunConfigurations create_cluster_tf_details(body, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoTFRunConfigurations() # ComCapillaryOpsCpBoTFRunConfigurations | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.create_cluster_tf_details(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->create_cluster_tf_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoTFRunConfigurations**](ComCapillaryOpsCpBoTFRunConfigurations.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoTFRunConfigurations**](ComCapillaryOpsCpBoTFRunConfigurations.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_draft_cluster1**
> ComCapillaryOpsCpBoAbstractCluster create_draft_cluster1(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsDraftClusterRequest() # ComCapillaryOpsCpBoRequestsDraftClusterRequest | 

try:
    api_response = api_instance.create_draft_cluster1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->create_draft_cluster1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsDraftClusterRequest**](ComCapillaryOpsCpBoRequestsDraftClusterRequest.md)|  | 

### Return type

[**ComCapillaryOpsCpBoAbstractCluster**](ComCapillaryOpsCpBoAbstractCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snapshot**
> bool create_snapshot(cluster_id, resource_type, instance_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
instance_name = 'instance_name_example' # str | 

try:
    api_response = api_instance.create_snapshot(cluster_id, resource_type, instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->create_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **instance_name** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_inputs**
> dict(str, list[ComCapillaryOpsCpBoStackTemplateInput]) create_template_inputs(body, cluster_id, input_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ComCapillaryOpsCpBoStackTemplateInput()] # list[ComCapillaryOpsCpBoStackTemplateInput] | 
cluster_id = 'cluster_id_example' # str | 
input_type = 'input_type_example' # str | 

try:
    api_response = api_instance.create_template_inputs(body, cluster_id, input_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->create_template_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ComCapillaryOpsCpBoStackTemplateInput]**](ComCapillaryOpsCpBoStackTemplateInput.md)|  | 
 **cluster_id** | **str**|  | 
 **input_type** | **str**|  | 

### Return type

**dict(str, list[ComCapillaryOpsCpBoStackTemplateInput])**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_availability_schedule**
> delete_availability_schedule(cluster_id, availability_schedule_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
availability_schedule_id = 'availability_schedule_id_example' # str | 

try:
    api_instance.delete_availability_schedule(cluster_id, availability_schedule_id)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_availability_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **availability_schedule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster1**
> bool delete_cluster1(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.delete_cluster1(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_cluster1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_force**
> bool delete_cluster_force(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.delete_cluster_force(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_cluster_force: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_schedule**
> list[ComCapillaryOpsCpBoClusterSchedule] delete_cluster_schedule(cluster_id, cluster_schedule_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
cluster_schedule_id = 'cluster_schedule_id_example' # str | 

try:
    api_response = api_instance.delete_cluster_schedule(cluster_id, cluster_schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_cluster_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **cluster_schedule_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoClusterSchedule]**](ComCapillaryOpsCpBoClusterSchedule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_tf_details**
> ComCapillaryOpsCpBoTFRunConfigurations delete_cluster_tf_details(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.delete_cluster_tf_details(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_cluster_tf_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoTFRunConfigurations**](ComCapillaryOpsCpBoTFRunConfigurations.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_overrides**
> list[ComCapillaryOpsCpBoOverrideObject] delete_overrides(cluster_id, resource_type, resource_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.delete_overrides(cluster_id, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_overrides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoOverrideObject]**](ComCapillaryOpsCpBoOverrideObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_inputs**
> ComCapillaryOpsCpBoStackTemplateInput delete_template_inputs(cluster_id, input_type, uid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
input_type = 'input_type_example' # str | 
uid = 'uid_example' # str | 

try:
    api_response = api_instance.delete_template_inputs(cluster_id, input_type, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_template_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **input_type** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoStackTemplateInput**](ComCapillaryOpsCpBoStackTemplateInput.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tools_config**
> delete_tools_config(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_instance.delete_tools_config(cluster_id)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->delete_tools_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_image**
> detach_image(body, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsImageOverrideRequest() # ComCapillaryOpsCpBoRequestsImageOverrideRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_instance.detach_image(body, cluster_id)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->detach_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsImageOverrideRequest**](ComCapillaryOpsCpBoRequestsImageOverrideRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_tools_config**
> ComCapillaryOpsCpBoToolsConfig edit_tools_config(body, cluster_id, tools_config_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoToolsConfig() # ComCapillaryOpsCpBoToolsConfig | 
cluster_id = 'cluster_id_example' # str | 
tools_config_id = 'tools_config_id_example' # str | 

try:
    api_response = api_instance.edit_tools_config(body, cluster_id, tools_config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->edit_tools_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoToolsConfig**](ComCapillaryOpsCpBoToolsConfig.md)|  | 
 **cluster_id** | **str**|  | 
 **tools_config_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoToolsConfig**](ComCapillaryOpsCpBoToolsConfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts**
> dict(str, object) get_alerts(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_alerts(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

**dict(str, object)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_inputs**
> dict(str, list[ComCapillaryOpsCpBoStackTemplateInput]) get_all_template_inputs(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_all_template_inputs(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_all_template_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

**dict(str, list[ComCapillaryOpsCpBoStackTemplateInput])**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_availability_schedules**
> ComCapillaryOpsCpBoAvailabilityscheduleAvailabilitySchedule get_availability_schedules(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_availability_schedules(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_availability_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAvailabilityscheduleAvailabilitySchedule**](ComCapillaryOpsCpBoAvailabilityscheduleAvailabilitySchedule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_common**
> ComCapillaryOpsCpBoAbstractCluster get_cluster_common(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_cluster_common(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_cluster_common: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAbstractCluster**](ComCapillaryOpsCpBoAbstractCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_info**
> ComCapillaryOpsCpBoResponseClusterClusterResponse get_cluster_info(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_cluster_info(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_cluster_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoResponseClusterClusterResponse**](ComCapillaryOpsCpBoResponseClusterClusterResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_metadata**
> ComCapillaryOpsCpV2ClustermetadataBoClusterMetadata get_cluster_metadata(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_cluster_metadata(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_cluster_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpV2ClustermetadataBoClusterMetadata**](ComCapillaryOpsCpV2ClustermetadataBoClusterMetadata.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_schedules**
> list[ComCapillaryOpsCpBoClusterSchedule] get_cluster_schedules(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_cluster_schedules(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_cluster_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoClusterSchedule]**](ComCapillaryOpsCpBoClusterSchedule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_tf_details**
> ComCapillaryOpsCpBoTFRunConfigurations get_cluster_tf_details(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_cluster_tf_details(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_cluster_tf_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoTFRunConfigurations**](ComCapillaryOpsCpBoTFRunConfigurations.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_k8s_credentials**
> ComCapillaryOpsCpBoKubernetesCredential get_k8s_credentials(cluster_id, refresh_permissions=refresh_permissions)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
refresh_permissions = true # bool |  (optional) (default to true)

try:
    api_response = api_instance.get_k8s_credentials(cluster_id, refresh_permissions=refresh_permissions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_k8s_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **refresh_permissions** | **bool**|  | [optional] [default to true]

### Return type

[**ComCapillaryOpsCpBoKubernetesCredential**](ComCapillaryOpsCpBoKubernetesCredential.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kube_config**
> str get_kube_config(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_kube_config(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_kube_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_matched_modules**
> ComCapillaryOpsCpV2RegistryMatchedModuleDTO get_matched_modules(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_matched_modules(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_matched_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpV2RegistryMatchedModuleDTO**](ComCapillaryOpsCpV2RegistryMatchedModuleDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaces_in_use_by_dependent_clusters**
> dict(str, str) get_namespaces_in_use_by_dependent_clusters(base_cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
base_cluster_id = 'base_cluster_id_example' # str | 

try:
    api_response = api_instance.get_namespaces_in_use_by_dependent_clusters(base_cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_namespaces_in_use_by_dependent_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_cluster_id** | **str**|  | 

### Return type

**dict(str, str)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_alerts**
> dict(str, object) get_open_alerts(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_open_alerts(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_open_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

**dict(str, object)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overrides2**
> list[ComCapillaryOpsCpBoOverrideObject] get_overrides2(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_overrides2(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_overrides2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoOverrideObject]**](ComCapillaryOpsCpBoOverrideObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pinned_snapshot1**
> ComCapillaryOpsCpBoSnapshotInfo get_pinned_snapshot1(cluster_id, resource_type, instance_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
instance_name = 'instance_name_example' # str | 

try:
    api_response = api_instance.get_pinned_snapshot1(cluster_id, resource_type, instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_pinned_snapshot1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **instance_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoSnapshotInfo**](ComCapillaryOpsCpBoSnapshotInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provided_resources**
> ComCapillaryOpsCpBoProvidedresourcesProvidedResources get_provided_resources(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_provided_resources(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_provided_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoProvidedresourcesProvidedResources**](ComCapillaryOpsCpBoProvidedresourcesProvidedResources.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_impacts**
> OrgSpringframeworkDataDomainPageComCapillaryOpsCpBoReleaseResourceReleaseImpact get_release_impacts(cluster_id, resource_type, resource_name, triggered_by=triggered_by, start=start, end=end, release_type=release_type, attribute=attribute, change_type=change_type, page_number=page_number, page_size=page_size)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 
triggered_by = 'triggered_by_example' # str |  (optional)
start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
release_type = 'release_type_example' # str |  (optional)
attribute = 'attribute_example' # str |  (optional)
change_type = 'change_type_example' # str |  (optional)
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)

try:
    api_response = api_instance.get_release_impacts(cluster_id, resource_type, resource_name, triggered_by=triggered_by, start=start, end=end, release_type=release_type, attribute=attribute, change_type=change_type, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_release_impacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 
 **triggered_by** | **str**|  | [optional] 
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **release_type** | **str**|  | [optional] 
 **attribute** | **str**|  | [optional] 
 **change_type** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**OrgSpringframeworkDataDomainPageComCapillaryOpsCpBoReleaseResourceReleaseImpact**](OrgSpringframeworkDataDomainPageComCapillaryOpsCpBoReleaseResourceReleaseImpact.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_stats**
> ComCapillaryOpsCpBoResoucesBlueprintFileSummaryDto get_resource_stats(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_resource_stats(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_resource_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoResoucesBlueprintFileSummaryDto**](ComCapillaryOpsCpBoResoucesBlueprintFileSummaryDto.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_input_by_uid**
> ComCapillaryOpsCpBoStackTemplateInput get_template_input_by_uid(cluster_id, input_type, uid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
input_type = 'input_type_example' # str | 
uid = 'uid_example' # str | 

try:
    api_response = api_instance.get_template_input_by_uid(cluster_id, input_type, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_template_input_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **input_type** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoStackTemplateInput**](ComCapillaryOpsCpBoStackTemplateInput.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_inputs**
> list[ComCapillaryOpsCpBoStackTemplateInput] get_template_inputs(cluster_id, input_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
input_type = 'input_type_example' # str | 

try:
    api_response = api_instance.get_template_inputs(cluster_id, input_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_template_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **input_type** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoStackTemplateInput]**](ComCapillaryOpsCpBoStackTemplateInput.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tools_config**
> ComCapillaryOpsCpBoToolsConfig get_tools_config(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_tools_config(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_tools_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoToolsConfig**](ComCapillaryOpsCpBoToolsConfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variable_counts**
> ComCapillaryOpsCpBoVariableCountDto get_variable_counts(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_variable_counts(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_variable_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoVariableCountDto**](ComCapillaryOpsCpBoVariableCountDto.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vars**
> ComCapillaryOpsCpBoAbstractCluster get_vars(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_vars(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_vars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAbstractCluster**](ComCapillaryOpsCpBoAbstractCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vars_with_secrets**
> ComCapillaryOpsCpBoAbstractCluster get_vars_with_secrets(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_vars_with_secrets(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_vars_with_secrets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAbstractCluster**](ComCapillaryOpsCpBoAbstractCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vars_with_status**
> dict(str, ComCapillaryOpsCpBoVariables) get_vars_with_status(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_vars_with_status(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_vars_with_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**dict(str, ComCapillaryOpsCpBoVariables)**](ComCapillaryOpsCpBoVariables.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpn_profile**
> str get_vpn_profile(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_vpn_profile(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->get_vpn_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshots1**
> list[ComCapillaryOpsCpBoSnapshotInfo] list_snapshots1(cluster_id, resource_type, instance_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
instance_name = 'instance_name_example' # str | 

try:
    api_response = api_instance.list_snapshots1(cluster_id, resource_type, instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->list_snapshots1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **instance_name** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoSnapshotInfo]**](ComCapillaryOpsCpBoSnapshotInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **override_sizing1**
> list[ComCapillaryOpsCpBoOverrideObject] override_sizing1(body, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ComCapillaryOpsCpBoRequestsOverrideRequest()] # list[ComCapillaryOpsCpBoRequestsOverrideRequest] | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.override_sizing1(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->override_sizing1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ComCapillaryOpsCpBoRequestsOverrideRequest]**](ComCapillaryOpsCpBoRequestsOverrideRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoOverrideObject]**](ComCapillaryOpsCpBoOverrideObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_release**
> str pause_release(body, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsPauseReleaseRequest() # ComCapillaryOpsCpBoRequestsPauseReleaseRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.pause_release(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->pause_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsPauseReleaseRequest**](ComCapillaryOpsCpBoRequestsPauseReleaseRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pin_snapshot1**
> ComCapillaryOpsCpBoSnapshotInfo pin_snapshot1(body, cluster_id, resource_type, instance_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoSnapshotInfo() # ComCapillaryOpsCpBoSnapshotInfo | 
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
instance_name = 'instance_name_example' # str | 

try:
    api_response = api_instance.pin_snapshot1(body, cluster_id, resource_type, instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->pin_snapshot1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoSnapshotInfo**](ComCapillaryOpsCpBoSnapshotInfo.md)|  | 
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **instance_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoSnapshotInfo**](ComCapillaryOpsCpBoSnapshotInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_kube_config**
> bool refresh_kube_config(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.refresh_kube_config(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->refresh_kube_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_silence**
> dict(str, object) remove_silence(cluster_id, silence_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
silence_id = 'silence_id_example' # str | 

try:
    api_response = api_instance.remove_silence(cluster_id, silence_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->remove_silence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **silence_id** | **str**|  | 

### Return type

**dict(str, object)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_details**
> list[ComCapillaryOpsCpBoResourceDetails] resource_details(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.resource_details(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->resource_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoResourceDetails]**](ComCapillaryOpsCpBoResourceDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cluster_code**
> bool set_cluster_code(cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.set_cluster_code(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->set_cluster_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **silence_alerts**
> dict(str, object) silence_alerts(body, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsSilenceAlarmRequest() # ComCapillaryOpsCpBoRequestsSilenceAlarmRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.silence_alerts(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->silence_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsSilenceAlarmRequest**](ComCapillaryOpsCpBoRequestsSilenceAlarmRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

**dict(str, object)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_availability_schedules**
> update_availability_schedules(body, schedule_id, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ComCapillaryOpsCpBoRequestsScheduleRequest()] # list[ComCapillaryOpsCpBoRequestsScheduleRequest] | 
schedule_id = 'schedule_id_example' # str | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_instance.update_availability_schedules(body, schedule_id, cluster_id)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->update_availability_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ComCapillaryOpsCpBoRequestsScheduleRequest]**](ComCapillaryOpsCpBoRequestsScheduleRequest.md)|  | 
 **schedule_id** | **str**|  | 
 **cluster_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_branch**
> ComCapillaryOpsCpBoAbstractCluster update_cluster_branch(body, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsBranchUpdateRequest() # ComCapillaryOpsCpBoRequestsBranchUpdateRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.update_cluster_branch(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->update_cluster_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsBranchUpdateRequest**](ComCapillaryOpsCpBoRequestsBranchUpdateRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAbstractCluster**](ComCapillaryOpsCpBoAbstractCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_schedules**
> list[ComCapillaryOpsCpBoClusterSchedule] update_cluster_schedules(body, cluster_id, cluster_schedule_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsScheduleRequest() # ComCapillaryOpsCpBoRequestsScheduleRequest | 
cluster_id = 'cluster_id_example' # str | 
cluster_schedule_id = 'cluster_schedule_id_example' # str | 

try:
    api_response = api_instance.update_cluster_schedules(body, cluster_id, cluster_schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->update_cluster_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsScheduleRequest**](ComCapillaryOpsCpBoRequestsScheduleRequest.md)|  | 
 **cluster_id** | **str**|  | 
 **cluster_schedule_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoClusterSchedule]**](ComCapillaryOpsCpBoClusterSchedule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_tf_details**
> ComCapillaryOpsCpBoTFRunConfigurations update_cluster_tf_details(body, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoTFRunConfigurations() # ComCapillaryOpsCpBoTFRunConfigurations | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.update_cluster_tf_details(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->update_cluster_tf_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoTFRunConfigurations**](ComCapillaryOpsCpBoTFRunConfigurations.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoTFRunConfigurations**](ComCapillaryOpsCpBoTFRunConfigurations.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_draft_cluster**
> ComCapillaryOpsCpBoAbstractCluster update_draft_cluster(body, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsDraftClusterRequest() # ComCapillaryOpsCpBoRequestsDraftClusterRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.update_draft_cluster(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->update_draft_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsDraftClusterRequest**](ComCapillaryOpsCpBoRequestsDraftClusterRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAbstractCluster**](ComCapillaryOpsCpBoAbstractCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_input**
> ComCapillaryOpsCpBoStackTemplateInput update_template_input(body, cluster_id, input_type, uid)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoStackTemplateInput() # ComCapillaryOpsCpBoStackTemplateInput | 
cluster_id = 'cluster_id_example' # str | 
input_type = 'input_type_example' # str | 
uid = 'uid_example' # str | 

try:
    api_response = api_instance.update_template_input(body, cluster_id, input_type, uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->update_template_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoStackTemplateInput**](ComCapillaryOpsCpBoStackTemplateInput.md)|  | 
 **cluster_id** | **str**|  | 
 **input_type** | **str**|  | 
 **uid** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoStackTemplateInput**](ComCapillaryOpsCpBoStackTemplateInput.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_provided_resources**
> ComCapillaryOpsCpBoProvidedresourcesProvidedResources upsert_provided_resources(body, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoProvidedresourcesProvidedResources() # ComCapillaryOpsCpBoProvidedresourcesProvidedResources | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.upsert_provided_resources(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->upsert_provided_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoProvidedresourcesProvidedResources**](ComCapillaryOpsCpBoProvidedresourcesProvidedResources.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoProvidedresourcesProvidedResources**](ComCapillaryOpsCpBoProvidedresourcesProvidedResources.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_vars1**
> ComCapillaryOpsCpBoAbstractCluster upsert_vars1(body, cluster_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiCommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, str) | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.upsert_vars1(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCommonClusterControllerApi->upsert_vars1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, str)**](dict.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAbstractCluster**](ComCapillaryOpsCpBoAbstractCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

