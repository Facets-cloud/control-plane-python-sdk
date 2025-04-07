# swagger_client.UiAssistantControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**continue_chat_using_post**](UiAssistantControllerApi.md#continue_chat_using_post) | **POST** /cc-ui/v2/assistant/chat | Continue Chat
[**create_thread_using_get**](UiAssistantControllerApi.md#create_thread_using_get) | **GET** /cc-ui/v2/assistant/thread | createThread
[**get_chat_using_post**](UiAssistantControllerApi.md#get_chat_using_post) | **POST** /cc-ui/v2/assistant/{threadId}/getChat | getChat


# **continue_chat_using_post**
> AssistantResponse continue_chat_using_post(request)

Continue Chat

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
api_instance = swagger_client.UiAssistantControllerApi(swagger_client.ApiClient(configuration))
request = swagger_client.AssistantRequest() # AssistantRequest | request

try:
    # Continue Chat
    api_response = api_instance.continue_chat_using_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAssistantControllerApi->continue_chat_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AssistantRequest**](AssistantRequest.md)| request | 

### Return type

[**AssistantResponse**](AssistantResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thread_using_get**
> AssistantResponse create_thread_using_get()

createThread

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
api_instance = swagger_client.UiAssistantControllerApi(swagger_client.ApiClient(configuration))

try:
    # createThread
    api_response = api_instance.create_thread_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAssistantControllerApi->create_thread_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AssistantResponse**](AssistantResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_using_post**
> AssistantResponse get_chat_using_post(thread_id)

getChat

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
api_instance = swagger_client.UiAssistantControllerApi(swagger_client.ApiClient(configuration))
thread_id = 'thread_id_example' # str | threadId

try:
    # getChat
    api_response = api_instance.get_chat_using_post(thread_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAssistantControllerApi->get_chat_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| threadId | 

### Return type

[**AssistantResponse**](AssistantResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

