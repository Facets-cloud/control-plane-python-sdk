# swagger_client.UiApplicationControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_using_put**](UiApplicationControllerApi.md#abort_using_put) | **PUT** /cc-ui/v1/clusters/{clusterId}/abort | abort
[**cluster_sync_with_git_using_post**](UiApplicationControllerApi.md#cluster_sync_with_git_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/sync-with-git | clusterSyncWithGit
[**get_application_overrides_using_get**](UiApplicationControllerApi.md#get_application_overrides_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/{resourceType}/{appName}/overrides | getApplicationOverrides
[**get_argo_rollout_info_using_get**](UiApplicationControllerApi.md#get_argo_rollout_info_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/argo-info | getArgoRolloutInfo
[**get_deployed_commit_id_for_resource_using_get**](UiApplicationControllerApi.md#get_deployed_commit_id_for_resource_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName}/deployed-commit-id | getDeployedCommitIdForResource
[**get_events_using_get**](UiApplicationControllerApi.md#get_events_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/pods/{podName}/events | getEvents
[**get_hpa_using_get**](UiApplicationControllerApi.md#get_hpa_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceName/{applicationName}/hpa | getHPA
[**get_ingresses_using_get**](UiApplicationControllerApi.md#get_ingresses_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceName/{applicationName}/ingresses | getIngresses
[**get_resource_by_name_using_get**](UiApplicationControllerApi.md#get_resource_by_name_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/{resourceType}/{appName} | getResourceByName
[**get_resource_by_name_v2_using_get**](UiApplicationControllerApi.md#get_resource_by_name_v2_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName} | getResourceByNameV2
[**get_resource_history_using_get**](UiApplicationControllerApi.md#get_resource_history_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName}/resource-history | getResourceHistory
[**get_resource_out_properties_using_get**](UiApplicationControllerApi.md#get_resource_out_properties_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName}/resource-out-properties | getResourceOutProperties
[**get_resource_override_object_using_get**](UiApplicationControllerApi.md#get_resource_override_object_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName}/overrides | getResourceOverrideObject
[**get_validations_using_get**](UiApplicationControllerApi.md#get_validations_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/validation-errors | getValidations
[**list_pods_using_get**](UiApplicationControllerApi.md#list_pods_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceName/{applicationName}/pods | listPods
[**logs_using_get**](UiApplicationControllerApi.md#logs_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/pods/{podName}/logs | logs
[**post_resource_override_object_using_post**](UiApplicationControllerApi.md#post_resource_override_object_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName}/overrides | postResourceOverrideObject
[**promote_using_put**](UiApplicationControllerApi.md#promote_using_put) | **PUT** /cc-ui/v1/clusters/{clusterId}/promote | promote
[**rolling_restart_using_post**](UiApplicationControllerApi.md#rolling_restart_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/restart/{applicationName} | rollingRestart
[**run_validation_using_post**](UiApplicationControllerApi.md#run_validation_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/validate | runValidation


# **abort_using_put**
> abort_using_put(cluster_id, labels)

abort

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # abort
    api_instance.abort_using_put(cluster_id, labels)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->abort_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_sync_with_git_using_post**
> cluster_sync_with_git_using_post(cluster_id, force=force)

clusterSyncWithGit

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
force = false # bool | force (optional) (default to false)

try:
    # clusterSyncWithGit
    api_instance.cluster_sync_with_git_using_post(cluster_id, force=force)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->cluster_sync_with_git_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **force** | **bool**| force | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_overrides_using_get**
> object get_application_overrides_using_get(app_name, cluster_id, resource_type)

getApplicationOverrides

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
app_name = 'app_name_example' # str | appName
cluster_id = 'cluster_id_example' # str | clusterId
resource_type = 'resource_type_example' # str | resourceType

try:
    # getApplicationOverrides
    api_response = api_instance.get_application_overrides_using_get(app_name, cluster_id, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_application_overrides_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| appName | 
 **cluster_id** | **str**| clusterId | 
 **resource_type** | **str**| resourceType | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_argo_rollout_info_using_get**
> object get_argo_rollout_info_using_get(cluster_id, labels)

getArgoRolloutInfo

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # getArgoRolloutInfo
    api_response = api_instance.get_argo_rollout_info_using_get(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_argo_rollout_info_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_commit_id_for_resource_using_get**
> str get_deployed_commit_id_for_resource_using_get(cluster_id, resource_name, resource_type)

getDeployedCommitIdForResource

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # getDeployedCommitIdForResource
    api_response = api_instance.get_deployed_commit_id_for_resource_using_get(cluster_id, resource_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_deployed_commit_id_for_resource_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_using_get**
> list[Event] get_events_using_get(cluster_id, pod_name)

getEvents

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
pod_name = 'pod_name_example' # str | podName

try:
    # getEvents
    api_response = api_instance.get_events_using_get(cluster_id, pod_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_events_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **pod_name** | **str**| podName | 

### Return type

[**list[Event]**](Event.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hpa_using_get**
> HorizontalPodAutoscaler get_hpa_using_get(application_name, cluster_id)

getHPA

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
application_name = 'application_name_example' # str | applicationName
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getHPA
    api_response = api_instance.get_hpa_using_get(application_name, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_hpa_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| applicationName | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**HorizontalPodAutoscaler**](HorizontalPodAutoscaler.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ingresses_using_get**
> list[Ingress] get_ingresses_using_get(application_name, cluster_id)

getIngresses

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
application_name = 'application_name_example' # str | applicationName
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getIngresses
    api_response = api_instance.get_ingresses_using_get(application_name, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_ingresses_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| applicationName | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**list[Ingress]**](Ingress.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_by_name_using_get**
> object get_resource_by_name_using_get(app_name, cluster_id, resource_type)

getResourceByName

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
app_name = 'app_name_example' # str | appName
cluster_id = 'cluster_id_example' # str | clusterId
resource_type = 'resource_type_example' # str | resourceType

try:
    # getResourceByName
    api_response = api_instance.get_resource_by_name_using_get(app_name, cluster_id, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_resource_by_name_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| appName | 
 **cluster_id** | **str**| clusterId | 
 **resource_type** | **str**| resourceType | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_by_name_v2_using_get**
> object get_resource_by_name_v2_using_get(cluster_id, resource_name, resource_type)

getResourceByNameV2

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # getResourceByNameV2
    api_response = api_instance.get_resource_by_name_v2_using_get(cluster_id, resource_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_resource_by_name_v2_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_history_using_get**
> ResourceHistory get_resource_history_using_get(cluster_id, resource_name, resource_type)

getResourceHistory

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # getResourceHistory
    api_response = api_instance.get_resource_history_using_get(cluster_id, resource_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_resource_history_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 

### Return type

[**ResourceHistory**](ResourceHistory.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_out_properties_using_get**
> ResourceOutProperties get_resource_out_properties_using_get(cluster_id, resource_name, resource_type)

getResourceOutProperties

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # getResourceOutProperties
    api_response = api_instance.get_resource_out_properties_using_get(cluster_id, resource_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_resource_out_properties_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 

### Return type

[**ResourceOutProperties**](ResourceOutProperties.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_override_object_using_get**
> OverrideObject get_resource_override_object_using_get(cluster_id, resource_name, resource_type)

getResourceOverrideObject

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # getResourceOverrideObject
    api_response = api_instance.get_resource_override_object_using_get(cluster_id, resource_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_resource_override_object_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 

### Return type

[**OverrideObject**](OverrideObject.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validations_using_get**
> list[ValidationResponse] get_validations_using_get(cluster_id)

getValidations

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getValidations
    api_response = api_instance.get_validations_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_validations_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**list[ValidationResponse]**](ValidationResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pods_using_get**
> list[Pod] list_pods_using_get(application_name, cluster_id)

listPods

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
application_name = 'application_name_example' # str | applicationName
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # listPods
    api_response = api_instance.list_pods_using_get(application_name, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->list_pods_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| applicationName | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**list[Pod]**](Pod.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logs_using_get**
> StreamingResponseBody logs_using_get(cluster_id, labels, pod_name)

logs

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels
pod_name = 'pod_name_example' # str | podName

try:
    # logs
    api_response = api_instance.logs_using_get(cluster_id, labels, pod_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->logs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 
 **pod_name** | **str**| podName | 

### Return type

[**StreamingResponseBody**](StreamingResponseBody.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_resource_override_object_using_post**
> OverrideObject post_resource_override_object_using_post(cluster_id, override_request, resource_name, resource_type, do_sync=do_sync)

postResourceOverrideObject

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
override_request = swagger_client.OverrideRequest() # OverrideRequest | overrideRequest
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
do_sync = true # bool | doSync (optional) (default to true)

try:
    # postResourceOverrideObject
    api_response = api_instance.post_resource_override_object_using_post(cluster_id, override_request, resource_name, resource_type, do_sync=do_sync)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->post_resource_override_object_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **override_request** | [**OverrideRequest**](OverrideRequest.md)| overrideRequest | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **do_sync** | **bool**| doSync | [optional] [default to true]

### Return type

[**OverrideObject**](OverrideObject.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promote_using_put**
> promote_using_put(cluster_id, labels)

promote

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # promote
    api_instance.promote_using_put(cluster_id, labels)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->promote_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rolling_restart_using_post**
> rolling_restart_using_post(application_name, cluster_id, labels)

rollingRestart

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
application_name = 'application_name_example' # str | applicationName
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # rollingRestart
    api_instance.rolling_restart_using_post(application_name, cluster_id, labels)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->rolling_restart_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| applicationName | 
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_validation_using_post**
> run_validation_using_post(cluster_id)

runValidation

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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # runValidation
    api_instance.run_validation_using_post(cluster_id)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->run_validation_using_post: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

