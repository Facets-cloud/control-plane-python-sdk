# swagger_client.StackControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stack_using_post**](StackControllerApi.md#create_stack_using_post) | **POST** /cc/v1/stacks/ | createStack
[**create_substack_using_post**](StackControllerApi.md#create_substack_using_post) | **POST** /cc/v1/stacks/substack/{substackName} | createSubstack
[**get_clusters_using_get**](StackControllerApi.md#get_clusters_using_get) | **GET** /cc/v1/stacks/{stackName}/clusters | getClusters
[**get_stacks_using_get**](StackControllerApi.md#get_stacks_using_get) | **GET** /cc/v1/stacks/ | getStacks
[**reload_stack_using_get**](StackControllerApi.md#reload_stack_using_get) | **GET** /cc/v1/stacks/{stackName}/reload | reloadStack
[**toggle_release_using_post**](StackControllerApi.md#toggle_release_using_post) | **POST** /cc/v1/stacks/{stackName}/toggleRelease | toggleRelease
[**update_stack_using_put**](StackControllerApi.md#update_stack_using_put) | **PUT** /cc/v1/stacks/{stackName} | updateStack

# **create_stack_using_post**
> Stack create_stack_using_post(body)

createStack

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
api_instance = swagger_client.StackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Stack() # Stack | stack

try:
    # createStack
    api_response = api_instance.create_stack_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackControllerApi->create_stack_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Stack**](Stack.md)| stack | 

### Return type

[**Stack**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_substack_using_post**
> Substack create_substack_using_post(body, substack_name)

createSubstack

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
api_instance = swagger_client.StackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Substack() # Substack | subStack
substack_name = 'substack_name_example' # str | substackName

try:
    # createSubstack
    api_response = api_instance.create_substack_using_post(body, substack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackControllerApi->create_substack_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Substack**](Substack.md)| subStack | 
 **substack_name** | **str**| substackName | 

### Return type

[**Substack**](Substack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters_using_get**
> list[AbstractCluster] get_clusters_using_get(stack_name)

getClusters

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
api_instance = swagger_client.StackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getClusters
    api_response = api_instance.get_clusters_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackControllerApi->get_clusters_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**list[AbstractCluster]**](AbstractCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stacks_using_get**
> list[Stack] get_stacks_using_get()

getStacks

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
api_instance = swagger_client.StackControllerApi(swagger_client.ApiClient(configuration))

try:
    # getStacks
    api_response = api_instance.get_stacks_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackControllerApi->get_stacks_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Stack]**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_stack_using_get**
> Stack reload_stack_using_get(stack_name)

reloadStack

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
api_instance = swagger_client.StackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # reloadStack
    api_response = api_instance.reload_stack_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackControllerApi->reload_stack_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**Stack**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_release_using_post**
> ToggleRelease toggle_release_using_post(body, stack_name)

toggleRelease

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
api_instance = swagger_client.StackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ToggleRelease() # ToggleRelease | toggleRelease
stack_name = 'stack_name_example' # str | stackName

try:
    # toggleRelease
    api_response = api_instance.toggle_release_using_post(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackControllerApi->toggle_release_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ToggleRelease**](ToggleRelease.md)| toggleRelease | 
 **stack_name** | **str**| stackName | 

### Return type

[**ToggleRelease**](ToggleRelease.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack_using_put**
> Stack update_stack_using_put(body, stack_name)

updateStack

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
api_instance = swagger_client.StackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Stack() # Stack | stack
stack_name = 'stack_name_example' # str | stackName

try:
    # updateStack
    api_response = api_instance.update_stack_using_put(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackControllerApi->update_stack_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Stack**](Stack.md)| stack | 
 **stack_name** | **str**| stackName | 

### Return type

[**Stack**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

