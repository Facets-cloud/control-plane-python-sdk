# swagger_client.UiEnvironmentControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_draft_environment**](UiEnvironmentControllerApi.md#configure_draft_environment) | **POST** /cc-ui/v1/environments/configure/{clusterId} | 
[**create_environment**](UiEnvironmentControllerApi.md#create_environment) | **POST** /cc-ui/v1/environments | 
[**get_environment**](UiEnvironmentControllerApi.md#get_environment) | **GET** /cc-ui/v1/environments/{clusterId} | 
[**update_environment**](UiEnvironmentControllerApi.md#update_environment) | **PUT** /cc-ui/v1/environments/{clusterId} | 

# **configure_draft_environment**
> Environment configure_draft_environment(body, cluster_id)



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
api_instance = swagger_client.UiEnvironmentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.EnvironmentRequest() # EnvironmentRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.configure_draft_environment(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiEnvironmentControllerApi->configure_draft_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnvironmentRequest**](EnvironmentRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**Environment**](Environment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_environment**
> Environment create_environment(body)



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
api_instance = swagger_client.UiEnvironmentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.EnvironmentRequest() # EnvironmentRequest | 

try:
    api_response = api_instance.create_environment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiEnvironmentControllerApi->create_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnvironmentRequest**](EnvironmentRequest.md)|  | 

### Return type

[**Environment**](Environment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment**
> Environment get_environment(cluster_id)



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
api_instance = swagger_client.UiEnvironmentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_environment(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiEnvironmentControllerApi->get_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**Environment**](Environment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_environment**
> Environment update_environment(body, cluster_id)



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
api_instance = swagger_client.UiEnvironmentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.EnvironmentRequest() # EnvironmentRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.update_environment(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiEnvironmentControllerApi->update_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnvironmentRequest**](EnvironmentRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**Environment**](Environment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

