# swagger_client.UiApplicationControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort**](UiApplicationControllerApi.md#abort) | **PUT** /cc-ui/v1/clusters/{clusterId}/abort | 
[**cluster_sync_with_git**](UiApplicationControllerApi.md#cluster_sync_with_git) | **POST** /cc-ui/v1/clusters/{clusterId}/sync-with-git | 
[**get_application_overrides**](UiApplicationControllerApi.md#get_application_overrides) | **GET** /cc-ui/v1/clusters/{clusterId}/{resourceType}/{appName}/overrides | 
[**get_argo_rollout_info**](UiApplicationControllerApi.md#get_argo_rollout_info) | **GET** /cc-ui/v1/clusters/{clusterId}/argo-info | 
[**get_deployed_commit_id_for_resource**](UiApplicationControllerApi.md#get_deployed_commit_id_for_resource) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName}/deployed-commit-id | 
[**get_events**](UiApplicationControllerApi.md#get_events) | **GET** /cc-ui/v1/clusters/{clusterId}/pods/{podName}/events | 
[**get_hpa**](UiApplicationControllerApi.md#get_hpa) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceName/{applicationName}/hpa | 
[**get_ingresses**](UiApplicationControllerApi.md#get_ingresses) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceName/{applicationName}/ingresses | 
[**get_resource_by_name**](UiApplicationControllerApi.md#get_resource_by_name) | **GET** /cc-ui/v1/clusters/{clusterId}/{resourceType}/{appName} | 
[**get_resource_by_name_v2**](UiApplicationControllerApi.md#get_resource_by_name_v2) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName} | 
[**get_resource_history**](UiApplicationControllerApi.md#get_resource_history) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName}/resource-history | 
[**get_resource_out_properties**](UiApplicationControllerApi.md#get_resource_out_properties) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName}/resource-out-properties | 
[**get_resource_override_object**](UiApplicationControllerApi.md#get_resource_override_object) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName}/overrides | 
[**get_validations**](UiApplicationControllerApi.md#get_validations) | **GET** /cc-ui/v1/clusters/{clusterId}/validation-errors | 
[**list_pods**](UiApplicationControllerApi.md#list_pods) | **GET** /cc-ui/v1/clusters/{clusterId}/resourceName/{applicationName}/pods | 
[**logs**](UiApplicationControllerApi.md#logs) | **GET** /cc-ui/v1/clusters/{clusterId}/pods/{podName}/logs | 
[**post_resource_override_object**](UiApplicationControllerApi.md#post_resource_override_object) | **POST** /cc-ui/v1/clusters/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName}/overrides | 
[**promote**](UiApplicationControllerApi.md#promote) | **PUT** /cc-ui/v1/clusters/{clusterId}/promote | 
[**rolling_restart**](UiApplicationControllerApi.md#rolling_restart) | **POST** /cc-ui/v1/clusters/{clusterId}/restart/{applicationName} | 
[**run_validation**](UiApplicationControllerApi.md#run_validation) | **POST** /cc-ui/v1/clusters/{clusterId}/validate | 

# **abort**
> abort(cluster_id, labels)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_instance.abort(cluster_id, labels)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->abort: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_sync_with_git**
> cluster_sync_with_git(cluster_id, force=force)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
force = false # bool |  (optional) (default to false)

try:
    api_instance.cluster_sync_with_git(cluster_id, force=force)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->cluster_sync_with_git: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **force** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_overrides**
> dict(str, object) get_application_overrides(cluster_id, app_name, resource_type)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
app_name = 'app_name_example' # str | 
resource_type = 'resource_type_example' # str | 

try:
    api_response = api_instance.get_application_overrides(cluster_id, app_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_application_overrides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **app_name** | **str**|  | 
 **resource_type** | **str**|  | 

### Return type

**dict(str, object)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_argo_rollout_info**
> object get_argo_rollout_info(cluster_id, labels)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.get_argo_rollout_info(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_argo_rollout_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_commit_id_for_resource**
> str get_deployed_commit_id_for_resource(cluster_id, resource_type, resource_name)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.get_deployed_commit_id_for_resource(cluster_id, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_deployed_commit_id_for_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events**
> list[Event] get_events(cluster_id, pod_name)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
pod_name = 'pod_name_example' # str | 

try:
    api_response = api_instance.get_events(cluster_id, pod_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **pod_name** | **str**|  | 

### Return type

[**list[Event]**](Event.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hpa**
> HorizontalPodAutoscaler get_hpa(cluster_id, application_name)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
application_name = 'application_name_example' # str | 

try:
    api_response = api_instance.get_hpa(cluster_id, application_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_hpa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **application_name** | **str**|  | 

### Return type

[**HorizontalPodAutoscaler**](HorizontalPodAutoscaler.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ingresses**
> list[Ingress] get_ingresses(cluster_id, application_name)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
application_name = 'application_name_example' # str | 

try:
    api_response = api_instance.get_ingresses(cluster_id, application_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_ingresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **application_name** | **str**|  | 

### Return type

[**list[Ingress]**](Ingress.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_by_name**
> dict(str, object) get_resource_by_name(cluster_id, app_name, resource_type)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
app_name = 'app_name_example' # str | 
resource_type = 'resource_type_example' # str | 

try:
    api_response = api_instance.get_resource_by_name(cluster_id, app_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_resource_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **app_name** | **str**|  | 
 **resource_type** | **str**|  | 

### Return type

**dict(str, object)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_by_name_v2**
> dict(str, object) get_resource_by_name_v2(cluster_id, resource_name, resource_type)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_name = 'resource_name_example' # str | 
resource_type = 'resource_type_example' # str | 

try:
    api_response = api_instance.get_resource_by_name_v2(cluster_id, resource_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_resource_by_name_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_name** | **str**|  | 
 **resource_type** | **str**|  | 

### Return type

**dict(str, object)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_history**
> ResourceHistory get_resource_history(cluster_id, resource_type, resource_name)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.get_resource_history(cluster_id, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_resource_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

[**ResourceHistory**](ResourceHistory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_out_properties**
> ResourceOutProperties get_resource_out_properties(cluster_id, resource_type, resource_name)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.get_resource_out_properties(cluster_id, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_resource_out_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

[**ResourceOutProperties**](ResourceOutProperties.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_override_object**
> OverrideObject get_resource_override_object(cluster_id, resource_name, resource_type)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_name = 'resource_name_example' # str | 
resource_type = 'resource_type_example' # str | 

try:
    api_response = api_instance.get_resource_override_object(cluster_id, resource_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_resource_override_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_name** | **str**|  | 
 **resource_type** | **str**|  | 

### Return type

[**OverrideObject**](OverrideObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validations**
> list[ValidationResponse] get_validations(cluster_id)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_validations(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->get_validations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**list[ValidationResponse]**](ValidationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pods**
> list[Pod] list_pods(cluster_id, application_name)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
application_name = 'application_name_example' # str | 

try:
    api_response = api_instance.list_pods(cluster_id, application_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->list_pods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **application_name** | **str**|  | 

### Return type

[**list[Pod]**](Pod.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logs**
> StreamingResponseBody logs(cluster_id, pod_name, labels)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
pod_name = 'pod_name_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.logs(cluster_id, pod_name, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **pod_name** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**StreamingResponseBody**](StreamingResponseBody.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_resource_override_object**
> OverrideObject post_resource_override_object(body, cluster_id, resource_name, resource_type, do_sync=do_sync, change_affected_resources=change_affected_resources)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.OverrideRequest() # OverrideRequest | 
cluster_id = 'cluster_id_example' # str | 
resource_name = 'resource_name_example' # str | 
resource_type = 'resource_type_example' # str | 
do_sync = true # bool |  (optional) (default to true)
change_affected_resources = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.post_resource_override_object(body, cluster_id, resource_name, resource_type, do_sync=do_sync, change_affected_resources=change_affected_resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->post_resource_override_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OverrideRequest**](OverrideRequest.md)|  | 
 **cluster_id** | **str**|  | 
 **resource_name** | **str**|  | 
 **resource_type** | **str**|  | 
 **do_sync** | **bool**|  | [optional] [default to true]
 **change_affected_resources** | **bool**|  | [optional] [default to false]

### Return type

[**OverrideObject**](OverrideObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promote**
> promote(cluster_id, labels)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_instance.promote(cluster_id, labels)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->promote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rolling_restart**
> rolling_restart(cluster_id, application_name, labels)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
application_name = 'application_name_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_instance.rolling_restart(cluster_id, application_name, labels)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->rolling_restart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **application_name** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_validation**
> run_validation(cluster_id)



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
api_instance = swagger_client.UiApplicationControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_instance.run_validation(cluster_id)
except ApiException as e:
    print("Exception when calling UiApplicationControllerApi->run_validation: %s\n" % e)
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

