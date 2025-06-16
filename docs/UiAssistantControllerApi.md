# swagger_client.UiAssistantControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**continue_chat**](UiAssistantControllerApi.md#continue_chat) | **POST** /cc-ui/v2/assistant/chat | Continue Chat
[**create_thread**](UiAssistantControllerApi.md#create_thread) | **GET** /cc-ui/v2/assistant/thread | 
[**get_chat**](UiAssistantControllerApi.md#get_chat) | **POST** /cc-ui/v2/assistant/{threadId}/getChat | 

# **continue_chat**
> ComCapillaryOpsCpV2AssistantsBoAssistantResponse continue_chat(body)

Continue Chat

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
api_instance = swagger_client.UiAssistantControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpV2AssistantsBoAssistantRequest() # ComCapillaryOpsCpV2AssistantsBoAssistantRequest | 

try:
    # Continue Chat
    api_response = api_instance.continue_chat(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAssistantControllerApi->continue_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpV2AssistantsBoAssistantRequest**](ComCapillaryOpsCpV2AssistantsBoAssistantRequest.md)|  | 

### Return type

[**ComCapillaryOpsCpV2AssistantsBoAssistantResponse**](ComCapillaryOpsCpV2AssistantsBoAssistantResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_thread**
> ComCapillaryOpsCpV2AssistantsBoAssistantResponse create_thread()



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
api_instance = swagger_client.UiAssistantControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.create_thread()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAssistantControllerApi->create_thread: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ComCapillaryOpsCpV2AssistantsBoAssistantResponse**](ComCapillaryOpsCpV2AssistantsBoAssistantResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat**
> ComCapillaryOpsCpV2AssistantsBoAssistantResponse get_chat(thread_id)



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
api_instance = swagger_client.UiAssistantControllerApi(swagger_client.ApiClient(configuration))
thread_id = 'thread_id_example' # str | 

try:
    api_response = api_instance.get_chat(thread_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAssistantControllerApi->get_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpV2AssistantsBoAssistantResponse**](ComCapillaryOpsCpV2AssistantsBoAssistantResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

