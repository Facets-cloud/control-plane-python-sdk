# swagger_client.UiReleaseStreamControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_using_post**](UiReleaseStreamControllerApi.md#add_using_post) | **POST** /cc-ui/v1/release-stream | add
[**delete_using_delete**](UiReleaseStreamControllerApi.md#delete_using_delete) | **DELETE** /cc-ui/v1/release-stream/{name} | delete
[**get_all_using_get3**](UiReleaseStreamControllerApi.md#get_all_using_get3) | **GET** /cc-ui/v1/release-stream | getAll


# **add_using_post**
> ReleaseStream add_using_post(release_stream_request)

add

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
api_instance = swagger_client.UiReleaseStreamControllerApi(swagger_client.ApiClient(configuration))
release_stream_request = swagger_client.ReleaseStreamRequest() # ReleaseStreamRequest | releaseStreamRequest

try:
    # add
    api_response = api_instance.add_using_post(release_stream_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiReleaseStreamControllerApi->add_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_stream_request** | [**ReleaseStreamRequest**](ReleaseStreamRequest.md)| releaseStreamRequest | 

### Return type

[**ReleaseStream**](ReleaseStream.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete**
> delete_using_delete(name)

delete

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
api_instance = swagger_client.UiReleaseStreamControllerApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | name

try:
    # delete
    api_instance.delete_using_delete(name)
except ApiException as e:
    print("Exception when calling UiReleaseStreamControllerApi->delete_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_using_get3**
> list[ReleaseStreamResponse] get_all_using_get3(stack_name=stack_name)

getAll

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
api_instance = swagger_client.UiReleaseStreamControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName (optional)

try:
    # getAll
    api_response = api_instance.get_all_using_get3(stack_name=stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiReleaseStreamControllerApi->get_all_using_get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | [optional] 

### Return type

[**list[ReleaseStreamResponse]**](ReleaseStreamResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

