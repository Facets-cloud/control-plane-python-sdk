# swagger_client.StackControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stack**](StackControllerApi.md#create_stack) | **POST** /cc/v1/stacks/ | 
[**create_substack**](StackControllerApi.md#create_substack) | **POST** /cc/v1/stacks/substack/{substackName} | 
[**get_clusters**](StackControllerApi.md#get_clusters) | **GET** /cc/v1/stacks/{stackName}/clusters | 
[**get_stacks**](StackControllerApi.md#get_stacks) | **GET** /cc/v1/stacks/ | 
[**reload_stack**](StackControllerApi.md#reload_stack) | **GET** /cc/v1/stacks/{stackName}/reload | 
[**toggle_release**](StackControllerApi.md#toggle_release) | **POST** /cc/v1/stacks/{stackName}/toggleRelease | 
[**update_stack**](StackControllerApi.md#update_stack) | **PUT** /cc/v1/stacks/{stackName} | 

# **create_stack**
> ComCapillaryOpsCpBoStack create_stack(body)



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
api_instance = swagger_client.StackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoStack() # ComCapillaryOpsCpBoStack | 

try:
    api_response = api_instance.create_stack(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackControllerApi->create_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoStack**](ComCapillaryOpsCpBoStack.md)|  | 

### Return type

[**ComCapillaryOpsCpBoStack**](ComCapillaryOpsCpBoStack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_substack**
> ComCapillaryOpsCpBoSubstack create_substack(body, substack_name)



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
api_instance = swagger_client.StackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoSubstack() # ComCapillaryOpsCpBoSubstack | 
substack_name = 'substack_name_example' # str | 

try:
    api_response = api_instance.create_substack(body, substack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackControllerApi->create_substack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoSubstack**](ComCapillaryOpsCpBoSubstack.md)|  | 
 **substack_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoSubstack**](ComCapillaryOpsCpBoSubstack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters**
> list[ComCapillaryOpsCpBoAbstractCluster] get_clusters(stack_name)



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
api_instance = swagger_client.StackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_clusters(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackControllerApi->get_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoAbstractCluster]**](ComCapillaryOpsCpBoAbstractCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stacks**
> list[ComCapillaryOpsCpBoStack] get_stacks()



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
api_instance = swagger_client.StackControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_stacks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackControllerApi->get_stacks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoStack]**](ComCapillaryOpsCpBoStack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_stack**
> ComCapillaryOpsCpBoStack reload_stack(stack_name)



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
api_instance = swagger_client.StackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.reload_stack(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackControllerApi->reload_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoStack**](ComCapillaryOpsCpBoStack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_release**
> ComCapillaryOpsCpBoToggleRelease toggle_release(body, stack_name)



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
api_instance = swagger_client.StackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoToggleRelease() # ComCapillaryOpsCpBoToggleRelease | 
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.toggle_release(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackControllerApi->toggle_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoToggleRelease**](ComCapillaryOpsCpBoToggleRelease.md)|  | 
 **stack_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoToggleRelease**](ComCapillaryOpsCpBoToggleRelease.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack**
> ComCapillaryOpsCpBoStack update_stack(body, stack_name)



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
api_instance = swagger_client.StackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoStack() # ComCapillaryOpsCpBoStack | 
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.update_stack(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackControllerApi->update_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoStack**](ComCapillaryOpsCpBoStack.md)|  | 
 **stack_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoStack**](ComCapillaryOpsCpBoStack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

