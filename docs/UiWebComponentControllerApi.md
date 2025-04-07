# swagger_client.UiWebComponentControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_component_using_post**](UiWebComponentControllerApi.md#create_component_using_post) | **POST** /cc-ui/v1/web-components | createComponent
[**delete_component_using_delete**](UiWebComponentControllerApi.md#delete_component_using_delete) | **DELETE** /cc-ui/v1/web-components/{webComponentId} | deleteComponent
[**get_all_components_using_get**](UiWebComponentControllerApi.md#get_all_components_using_get) | **GET** /cc-ui/v1/web-components | getAllComponents
[**get_component_using_get**](UiWebComponentControllerApi.md#get_component_using_get) | **GET** /cc-ui/v1/web-components/{webComponentId} | getComponent
[**update_component_using_put**](UiWebComponentControllerApi.md#update_component_using_put) | **PUT** /cc-ui/v1/web-components/{webComponentId} | updateComponent


# **create_component_using_post**
> WebComponentDTO create_component_using_post(component)

createComponent

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
api_instance = swagger_client.UiWebComponentControllerApi(swagger_client.ApiClient(configuration))
component = swagger_client.WebComponentDTO() # WebComponentDTO | component

try:
    # createComponent
    api_response = api_instance.create_component_using_post(component)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiWebComponentControllerApi->create_component_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component** | [**WebComponentDTO**](WebComponentDTO.md)| component | 

### Return type

[**WebComponentDTO**](WebComponentDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_component_using_delete**
> delete_component_using_delete(web_component_id)

deleteComponent

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
api_instance = swagger_client.UiWebComponentControllerApi(swagger_client.ApiClient(configuration))
web_component_id = 'web_component_id_example' # str | webComponentId

try:
    # deleteComponent
    api_instance.delete_component_using_delete(web_component_id)
except ApiException as e:
    print("Exception when calling UiWebComponentControllerApi->delete_component_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_component_id** | **str**| webComponentId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_components_using_get**
> list[WebComponentDTO] get_all_components_using_get()

getAllComponents

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
api_instance = swagger_client.UiWebComponentControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllComponents
    api_response = api_instance.get_all_components_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiWebComponentControllerApi->get_all_components_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[WebComponentDTO]**](WebComponentDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component_using_get**
> WebComponentDTO get_component_using_get(web_component_id)

getComponent

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
api_instance = swagger_client.UiWebComponentControllerApi(swagger_client.ApiClient(configuration))
web_component_id = 'web_component_id_example' # str | webComponentId

try:
    # getComponent
    api_response = api_instance.get_component_using_get(web_component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiWebComponentControllerApi->get_component_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_component_id** | **str**| webComponentId | 

### Return type

[**WebComponentDTO**](WebComponentDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_component_using_put**
> WebComponentDTO update_component_using_put(component, web_component_id)

updateComponent

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
api_instance = swagger_client.UiWebComponentControllerApi(swagger_client.ApiClient(configuration))
component = swagger_client.WebComponentDTO() # WebComponentDTO | component
web_component_id = 'web_component_id_example' # str | webComponentId

try:
    # updateComponent
    api_response = api_instance.update_component_using_put(component, web_component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiWebComponentControllerApi->update_component_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component** | [**WebComponentDTO**](WebComponentDTO.md)| component | 
 **web_component_id** | **str**| webComponentId | 

### Return type

[**WebComponentDTO**](WebComponentDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

