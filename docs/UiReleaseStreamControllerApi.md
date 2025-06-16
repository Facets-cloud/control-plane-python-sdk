# swagger_client.UiReleaseStreamControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add1**](UiReleaseStreamControllerApi.md#add1) | **POST** /cc-ui/v1/release-stream | 
[**delete2**](UiReleaseStreamControllerApi.md#delete2) | **DELETE** /cc-ui/v1/release-stream/{name} | 
[**get_all1**](UiReleaseStreamControllerApi.md#get_all1) | **GET** /cc-ui/v1/release-stream | 

# **add1**
> ComCapillaryOpsCpBoReleasestreamReleaseStream add1(body)



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
api_instance = swagger_client.UiReleaseStreamControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoReleasestreamReleaseStreamRequest() # ComCapillaryOpsCpBoReleasestreamReleaseStreamRequest | 

try:
    api_response = api_instance.add1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiReleaseStreamControllerApi->add1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoReleasestreamReleaseStreamRequest**](ComCapillaryOpsCpBoReleasestreamReleaseStreamRequest.md)|  | 

### Return type

[**ComCapillaryOpsCpBoReleasestreamReleaseStream**](ComCapillaryOpsCpBoReleasestreamReleaseStream.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete2**
> delete2(name)



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
api_instance = swagger_client.UiReleaseStreamControllerApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_instance.delete2(name)
except ApiException as e:
    print("Exception when calling UiReleaseStreamControllerApi->delete2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all1**
> list[ComCapillaryOpsCpBoReleasestreamReleaseStreamResponse] get_all1(stack_name=stack_name)



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
api_instance = swagger_client.UiReleaseStreamControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str |  (optional)

try:
    api_response = api_instance.get_all1(stack_name=stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiReleaseStreamControllerApi->get_all1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | [optional] 

### Return type

[**list[ComCapillaryOpsCpBoReleasestreamReleaseStreamResponse]**](ComCapillaryOpsCpBoReleasestreamReleaseStreamResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

