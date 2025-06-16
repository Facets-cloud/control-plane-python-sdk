# swagger_client.DeploymentControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_automation_suite**](DeploymentControllerApi.md#abort_automation_suite) | **DELETE** /cc/v1/clusters/{clusterId}/deployments/qa/{executionId}/abortSuite | 
[**get_automation_suite_status**](DeploymentControllerApi.md#get_automation_suite_status) | **GET** /cc/v1/clusters/{clusterId}/deployments/qa/{executionId}/status | 
[**get_deployments**](DeploymentControllerApi.md#get_deployments) | **GET** /cc/v1/clusters/{clusterId}/deployments | 
[**get_logs**](DeploymentControllerApi.md#get_logs) | **GET** /cc/v1/clusters/{clusterId}/deployments/{id} | 
[**trigger_automation_suite**](DeploymentControllerApi.md#trigger_automation_suite) | **POST** /cc/v1/clusters/{clusterId}/deployments/qa/triggerSuite | 
[**validate_sanity_result**](DeploymentControllerApi.md#validate_sanity_result) | **POST** /cc/v1/clusters/{clusterId}/deployments/qa/validateSanityResult | 

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
api_instance = swagger_client.DeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
execution_id = 'execution_id_example' # str | 

try:
    api_instance.abort_automation_suite(cluster_id, execution_id)
except ApiException as e:
    print("Exception when calling DeploymentControllerApi->abort_automation_suite: %s\n" % e)
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

# **get_automation_suite_status**
> str get_automation_suite_status(cluster_id, execution_id)



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
api_instance = swagger_client.DeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
execution_id = 'execution_id_example' # str | 

try:
    api_response = api_instance.get_automation_suite_status(cluster_id, execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentControllerApi->get_automation_suite_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **execution_id** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments**
> ComCapillaryOpsCpBoWrappersListDeploymentsWrapper get_deployments(cluster_id)



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
api_instance = swagger_client.DeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_deployments(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentControllerApi->get_deployments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoWrappersListDeploymentsWrapper**](ComCapillaryOpsCpBoWrappersListDeploymentsWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs**
> list[str] get_logs(cluster_id, id)



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
api_instance = swagger_client.DeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_logs(cluster_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentControllerApi->get_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_automation_suite**
> str trigger_automation_suite(body, cluster_id)



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
api_instance = swagger_client.DeploymentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoQASuite() # ComCapillaryOpsCpBoQASuite | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.trigger_automation_suite(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentControllerApi->trigger_automation_suite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoQASuite**](ComCapillaryOpsCpBoQASuite.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_sanity_result**
> validate_sanity_result(body, cluster_id)



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
api_instance = swagger_client.DeploymentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoQASuiteResult() # ComCapillaryOpsCpBoQASuiteResult | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_instance.validate_sanity_result(body, cluster_id)
except ApiException as e:
    print("Exception when calling DeploymentControllerApi->validate_sanity_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoQASuiteResult**](ComCapillaryOpsCpBoQASuiteResult.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

