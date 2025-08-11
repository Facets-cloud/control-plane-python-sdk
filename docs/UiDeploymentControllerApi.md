# swagger_client.UiDeploymentControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_automation_suite**](UiDeploymentControllerApi.md#abort_automation_suite) | **DELETE** /cc-ui/v1/clusters/{clusterId}/deployments/qa/{executionId}/abortSuite | 
[**approve_release**](UiDeploymentControllerApi.md#approve_release) | **POST** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/approveRelease | 
[**create_deployment**](UiDeploymentControllerApi.md#create_deployment) | **POST** /cc-ui/v1/clusters/{clusterId}/deployments | 
[**destroy_cluster**](UiDeploymentControllerApi.md#destroy_cluster) | **DELETE** /cc-ui/v1/clusters/{clusterId}/deployments/destroy | 
[**download_terraform_export**](UiDeploymentControllerApi.md#download_terraform_export) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/download-terraform-export | 
[**get_cluster_state**](UiDeploymentControllerApi.md#get_cluster_state) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/state | 
[**get_deployment**](UiDeploymentControllerApi.md#get_deployment) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId} | 
[**get_deployment_by_release_trace_id**](UiDeploymentControllerApi.md#get_deployment_by_release_trace_id) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/trace-id/{releaseTraceId} | 
[**get_deployment_logs**](UiDeploymentControllerApi.md#get_deployment_logs) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/logs | 
[**get_deployment_stats**](UiDeploymentControllerApi.md#get_deployment_stats) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/stats | 
[**get_deployments**](UiDeploymentControllerApi.md#get_deployments) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments | 
[**get_deployments_overview**](UiDeploymentControllerApi.md#get_deployments_overview) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/overview | 
[**get_latest_release**](UiDeploymentControllerApi.md#get_latest_release) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/latest-successful-release | 
[**get_latest_release_by_application**](UiDeploymentControllerApi.md#get_latest_release_by_application) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/latest-successful-release/{application} | 
[**get_release_changes**](UiDeploymentControllerApi.md#get_release_changes) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/release-changes | 
[**launch_cluster**](UiDeploymentControllerApi.md#launch_cluster) | **PUT** /cc-ui/v1/clusters/{clusterId}/deployments/launch | 
[**reject_release**](UiDeploymentControllerApi.md#reject_release) | **POST** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/rejectRelease | 
[**release**](UiDeploymentControllerApi.md#release) | **PUT** /cc-ui/v1/clusters/{clusterId}/deployments/release | 
[**release_v2**](UiDeploymentControllerApi.md#release_v2) | **PUT** /cc-ui/v1/clusters/{clusterId}/deployments/releaseV2/{releaseType} | 
[**run_hotfix_deployment_recipe**](UiDeploymentControllerApi.md#run_hotfix_deployment_recipe) | **POST** /cc-ui/v1/clusters/{clusterId}/deployments/recipes/deployment/hotfix | 
[**search_deployments**](UiDeploymentControllerApi.md#search_deployments) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/search | 
[**sign_off_deployment**](UiDeploymentControllerApi.md#sign_off_deployment) | **PUT** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/signoff | 
[**simulate**](UiDeploymentControllerApi.md#simulate) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/simulate | 
[**state_unlock**](UiDeploymentControllerApi.md#state_unlock) | **PUT** /cc-ui/v1/clusters/{clusterId}/deployments/unlock | 
[**stream_deployment_logs**](UiDeploymentControllerApi.md#stream_deployment_logs) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/logs/stream | 
[**trigger_maintenance_release**](UiDeploymentControllerApi.md#trigger_maintenance_release) | **POST** /cc-ui/v1/clusters/{clusterId}/deployments/maintenance | 
[**trigger_rollback_plan_release**](UiDeploymentControllerApi.md#trigger_rollback_plan_release) | **POST** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/{resourceType}/{resourceName}/rollback-plan | 
[**trigger_terraform_export**](UiDeploymentControllerApi.md#trigger_terraform_export) | **POST** /cc-ui/v1/clusters/{clusterId}/deployments/terraform-export | 
[**upload_release_metadata**](UiDeploymentControllerApi.md#upload_release_metadata) | **POST** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/upload-release-metadata | 

# **abort_automation_suite**
> abort_automation_suite(cluster_id, execution_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
execution_id = 'execution_id_example' # str | 

try:
    api_instance.abort_automation_suite(cluster_id, execution_id)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->abort_automation_suite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **execution_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_release**
> DeploymentLog approve_release(cluster_id, deployment_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
deployment_id = 'deployment_id_example' # str | 

try:
    api_response = api_instance.approve_release(cluster_id, deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->approve_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **deployment_id** | **str**|  | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_deployment**
> DeploymentLog create_deployment(body, cluster_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeploymentRequest() # DeploymentRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.create_deployment(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->create_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeploymentRequest**](DeploymentRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_cluster**
> DeploymentLog destroy_cluster(cluster_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.destroy_cluster(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->destroy_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_terraform_export**
> download_terraform_export(cluster_id, deployment_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
deployment_id = 'deployment_id_example' # str | 

try:
    api_instance.download_terraform_export(cluster_id, deployment_id)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->download_terraform_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **deployment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_state**
> str get_cluster_state(cluster_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_cluster_state(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_cluster_state: %s\n" % e)
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

# **get_deployment**
> DeploymentLog get_deployment(cluster_id, deployment_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
deployment_id = 'deployment_id_example' # str | 

try:
    api_response = api_instance.get_deployment(cluster_id, deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **deployment_id** | **str**|  | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_by_release_trace_id**
> DeploymentLog get_deployment_by_release_trace_id(cluster_id, release_trace_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
release_trace_id = 'release_trace_id_example' # str | 

try:
    api_response = api_instance.get_deployment_by_release_trace_id(cluster_id, release_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_deployment_by_release_trace_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **release_trace_id** | **str**|  | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_logs**
> TokenPaginatedResponse get_deployment_logs(cluster_id, deployment_id, next_token=next_token)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
deployment_id = 'deployment_id_example' # str | 
next_token = 'next_token_example' # str |  (optional)

try:
    api_response = api_instance.get_deployment_logs(cluster_id, deployment_id, next_token=next_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_deployment_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **deployment_id** | **str**|  | 
 **next_token** | **str**|  | [optional] 

### Return type

[**TokenPaginatedResponse**](TokenPaginatedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_stats**
> DeploymentStatsDto get_deployment_stats(cluster_id, days=days)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
days = 30 # int |  (optional) (default to 30)

try:
    api_response = api_instance.get_deployment_stats(cluster_id, days=days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_deployment_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **days** | **int**|  | [optional] [default to 30]

### Return type

[**DeploymentStatsDto**](DeploymentStatsDto.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments**
> ListDeploymentsWrapper get_deployments(cluster_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_deployments(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_deployments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ListDeploymentsWrapper**](ListDeploymentsWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments_overview**
> DeploymentOverview get_deployments_overview(cluster_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_deployments_overview(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_deployments_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**DeploymentOverview**](DeploymentOverview.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_release**
> DeploymentLog get_latest_release(cluster_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_latest_release(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_latest_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_release_by_application**
> DeploymentLog get_latest_release_by_application(cluster_id, application)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
application = 'application_example' # str | 

try:
    api_response = api_instance.get_latest_release_by_application(cluster_id, application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_latest_release_by_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **application** | **str**|  | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_changes**
> ReleaseChanges get_release_changes(cluster_id, deployment_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
deployment_id = 'deployment_id_example' # str | 

try:
    api_response = api_instance.get_release_changes(cluster_id, deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_release_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **deployment_id** | **str**|  | 

### Return type

[**ReleaseChanges**](ReleaseChanges.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_cluster**
> DeploymentLog launch_cluster(cluster_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.launch_cluster(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->launch_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_release**
> DeploymentLog reject_release(cluster_id, deployment_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
deployment_id = 'deployment_id_example' # str | 

try:
    api_response = api_instance.reject_release(cluster_id, deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->reject_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **deployment_id** | **str**|  | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release**
> DeploymentLog release(cluster_id, with_refresh=with_refresh, force_release=force_release, allow_destroy=allow_destroy, comment=comment, can_queue=can_queue)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
with_refresh = true # bool |  (optional) (default to true)
force_release = false # bool |  (optional) (default to false)
allow_destroy = false # bool |  (optional) (default to false)
comment = 'comment_example' # str |  (optional)
can_queue = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.release(cluster_id, with_refresh=with_refresh, force_release=force_release, allow_destroy=allow_destroy, comment=comment, can_queue=can_queue)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **with_refresh** | **bool**|  | [optional] [default to true]
 **force_release** | **bool**|  | [optional] [default to false]
 **allow_destroy** | **bool**|  | [optional] [default to false]
 **comment** | **str**|  | [optional] 
 **can_queue** | **bool**|  | [optional] [default to false]

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_v2**
> DeploymentLog release_v2(cluster_id, release_type, with_refresh=with_refresh, force_release=force_release, allow_destroy=allow_destroy, comment=comment, can_queue=can_queue)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
release_type = 'release_type_example' # str | 
with_refresh = true # bool |  (optional) (default to true)
force_release = false # bool |  (optional) (default to false)
allow_destroy = false # bool |  (optional) (default to false)
comment = 'comment_example' # str |  (optional)
can_queue = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.release_v2(cluster_id, release_type, with_refresh=with_refresh, force_release=force_release, allow_destroy=allow_destroy, comment=comment, can_queue=can_queue)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->release_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **release_type** | **str**|  | 
 **with_refresh** | **bool**|  | [optional] [default to true]
 **force_release** | **bool**|  | [optional] [default to false]
 **allow_destroy** | **bool**|  | [optional] [default to false]
 **comment** | **str**|  | [optional] 
 **can_queue** | **bool**|  | [optional] [default to false]

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_hotfix_deployment_recipe**
> DeploymentLog run_hotfix_deployment_recipe(body, cluster_id, allow_destroy=allow_destroy, with_refresh=with_refresh, force_release=force_release, comment=comment, is_plan=is_plan, can_queue=can_queue, release_trace_id=release_trace_id, skip_state_check=skip_state_check)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.HotfixDeploymentRecipe() # HotfixDeploymentRecipe | 
cluster_id = 'cluster_id_example' # str | 
allow_destroy = false # bool |  (optional) (default to false)
with_refresh = false # bool |  (optional) (default to false)
force_release = false # bool |  (optional) (default to false)
comment = 'comment_example' # str |  (optional)
is_plan = false # bool |  (optional) (default to false)
can_queue = false # bool |  (optional) (default to false)
release_trace_id = 'release_trace_id_example' # str | Unique identifier of the release that you can search it with (optional)
skip_state_check = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.run_hotfix_deployment_recipe(body, cluster_id, allow_destroy=allow_destroy, with_refresh=with_refresh, force_release=force_release, comment=comment, is_plan=is_plan, can_queue=can_queue, release_trace_id=release_trace_id, skip_state_check=skip_state_check)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->run_hotfix_deployment_recipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HotfixDeploymentRecipe**](HotfixDeploymentRecipe.md)|  | 
 **cluster_id** | **str**|  | 
 **allow_destroy** | **bool**|  | [optional] [default to false]
 **with_refresh** | **bool**|  | [optional] [default to false]
 **force_release** | **bool**|  | [optional] [default to false]
 **comment** | **str**|  | [optional] 
 **is_plan** | **bool**|  | [optional] [default to false]
 **can_queue** | **bool**|  | [optional] [default to false]
 **release_trace_id** | **str**| Unique identifier of the release that you can search it with | [optional] 
 **skip_state_check** | **bool**|  | [optional] [default to false]

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_deployments**
> PageDeploymentLog search_deployments(cluster_id, page_number=page_number, page_size=page_size, release_type=release_type, signed_off=signed_off, status=status, exclude_status=exclude_status, triggered_by=triggered_by, start=start, end=end, tf_version=tf_version)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)
release_type = 'release_type_example' # str |  (optional)
signed_off = true # bool |  (optional)
status = 'status_example' # str |  (optional)
exclude_status = ['exclude_status_example'] # list[str] |  (optional)
triggered_by = 'triggered_by_example' # str |  (optional)
start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
tf_version = 'tf_version_example' # str |  (optional)

try:
    api_response = api_instance.search_deployments(cluster_id, page_number=page_number, page_size=page_size, release_type=release_type, signed_off=signed_off, status=status, exclude_status=exclude_status, triggered_by=triggered_by, start=start, end=end, tf_version=tf_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->search_deployments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]
 **release_type** | **str**|  | [optional] 
 **signed_off** | **bool**|  | [optional] 
 **status** | **str**|  | [optional] 
 **exclude_status** | [**list[str]**](str.md)|  | [optional] 
 **triggered_by** | **str**|  | [optional] 
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **tf_version** | **str**|  | [optional] 

### Return type

[**PageDeploymentLog**](PageDeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_off_deployment**
> DeploymentLog sign_off_deployment(cluster_id, deployment_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
deployment_id = 'deployment_id_example' # str | 

try:
    api_response = api_instance.sign_off_deployment(cluster_id, deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->sign_off_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **deployment_id** | **str**|  | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simulate**
> list[ChangeRepresentationObject] simulate(cluster_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.simulate(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->simulate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**list[ChangeRepresentationObject]**](ChangeRepresentationObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_unlock**
> DeploymentLog state_unlock(cluster_id, lock_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
lock_id = 'lock_id_example' # str | 

try:
    api_response = api_instance.state_unlock(cluster_id, lock_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->state_unlock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **lock_id** | **str**|  | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_deployment_logs**
> StreamingResponseBody stream_deployment_logs(cluster_id, deployment_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
deployment_id = 'deployment_id_example' # str | 

try:
    api_response = api_instance.stream_deployment_logs(cluster_id, deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->stream_deployment_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **deployment_id** | **str**|  | 

### Return type

[**StreamingResponseBody**](StreamingResponseBody.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_maintenance_release**
> DeploymentLog trigger_maintenance_release(cluster_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.trigger_maintenance_release(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->trigger_maintenance_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_rollback_plan_release**
> DeploymentLog trigger_rollback_plan_release(cluster_id, deployment_id, resource_type, resource_name)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
deployment_id = 'deployment_id_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.trigger_rollback_plan_release(cluster_id, deployment_id, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->trigger_rollback_plan_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **deployment_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_terraform_export**
> DeploymentLog trigger_terraform_export(cluster_id)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.trigger_terraform_export(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->trigger_terraform_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_release_metadata**
> upload_release_metadata(cluster_id, deployment_id, body=body)



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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
deployment_id = 'deployment_id_example' # str | 
body = swagger_client.DeploymentIdUploadreleasemetadataBody() # DeploymentIdUploadreleasemetadataBody |  (optional)

try:
    api_instance.upload_release_metadata(cluster_id, deployment_id, body=body)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->upload_release_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **deployment_id** | **str**|  | 
 **body** | [**DeploymentIdUploadreleasemetadataBody**](DeploymentIdUploadreleasemetadataBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

