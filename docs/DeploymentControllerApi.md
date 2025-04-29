# swagger_client.DeploymentControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_automation_suite_using_delete**](DeploymentControllerApi.md#abort_automation_suite_using_delete) | **DELETE** /cc/v1/clusters/{clusterId}/deployments/qa/{executionId}/abortSuite | abortAutomationSuite
[**get_automation_suite_status_using_get**](DeploymentControllerApi.md#get_automation_suite_status_using_get) | **GET** /cc/v1/clusters/{clusterId}/deployments/qa/{executionId}/status | getAutomationSuiteStatus
[**get_deployments_using_get**](DeploymentControllerApi.md#get_deployments_using_get) | **GET** /cc/v1/clusters/{clusterId}/deployments | getDeployments
[**get_logs_using_get**](DeploymentControllerApi.md#get_logs_using_get) | **GET** /cc/v1/clusters/{clusterId}/deployments/{id} | getLogs
[**trigger_automation_suite_using_post**](DeploymentControllerApi.md#trigger_automation_suite_using_post) | **POST** /cc/v1/clusters/{clusterId}/deployments/qa/triggerSuite | triggerAutomationSuite
[**validate_sanity_result_using_post**](DeploymentControllerApi.md#validate_sanity_result_using_post) | **POST** /cc/v1/clusters/{clusterId}/deployments/qa/validateSanityResult | validateSanityResult

# **abort_automation_suite_using_delete**
> abort_automation_suite_using_delete(cluster_id, execution_id)

abortAutomationSuite

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
api_instance = swagger_client.DeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
execution_id = 'execution_id_example' # str | executionId

try:
    # abortAutomationSuite
    api_instance.abort_automation_suite_using_delete(cluster_id, execution_id)
except ApiException as e:
    print("Exception when calling DeploymentControllerApi->abort_automation_suite_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **execution_id** | **str**| executionId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_automation_suite_status_using_get**
> str get_automation_suite_status_using_get(cluster_id, execution_id)

getAutomationSuiteStatus

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
api_instance = swagger_client.DeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
execution_id = 'execution_id_example' # str | executionId

try:
    # getAutomationSuiteStatus
    api_response = api_instance.get_automation_suite_status_using_get(cluster_id, execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentControllerApi->get_automation_suite_status_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **execution_id** | **str**| executionId | 

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments_using_get**
> ListDeploymentsWrapper get_deployments_using_get(cluster_id)

getDeployments

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
api_instance = swagger_client.DeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getDeployments
    api_response = api_instance.get_deployments_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentControllerApi->get_deployments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**ListDeploymentsWrapper**](ListDeploymentsWrapper.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs_using_get**
> list[str] get_logs_using_get(cluster_id, id)

getLogs

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
api_instance = swagger_client.DeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
id = 'id_example' # str | id

try:
    # getLogs
    api_response = api_instance.get_logs_using_get(cluster_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentControllerApi->get_logs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **id** | **str**| id | 

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_automation_suite_using_post**
> str trigger_automation_suite_using_post(body, cluster_id)

triggerAutomationSuite

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
api_instance = swagger_client.DeploymentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.QASuite() # QASuite | automationSuite
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # triggerAutomationSuite
    api_response = api_instance.trigger_automation_suite_using_post(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentControllerApi->trigger_automation_suite_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QASuite**](QASuite.md)| automationSuite | 
 **cluster_id** | **str**| clusterId | 

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_sanity_result_using_post**
> validate_sanity_result_using_post(body, cluster_id)

validateSanityResult

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
api_instance = swagger_client.DeploymentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.QASuiteResult() # QASuiteResult | qaSuiteResult
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # validateSanityResult
    api_instance.validate_sanity_result_using_post(body, cluster_id)
except ApiException as e:
    print("Exception when calling DeploymentControllerApi->validate_sanity_result_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QASuiteResult**](QASuiteResult.md)| qaSuiteResult | 
 **cluster_id** | **str**| clusterId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

