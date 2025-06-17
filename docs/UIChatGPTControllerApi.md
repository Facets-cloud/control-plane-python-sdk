# swagger_client.UIChatGPTControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_kubernetes_cluster**](UIChatGPTControllerApi.md#analyze_kubernetes_cluster) | **GET** /cc-ui/v1/clusters/{clusterId}/kubernetes/analyze | 
[**chat**](UIChatGPTControllerApi.md#chat) | **POST** /cc-ui/v1/clusters/chat/{chatId} | Send a message to a chat
[**create_chat**](UIChatGPTControllerApi.md#create_chat) | **POST** /cc-ui/v1/clusters/{clusterId}/chat | Create a new chat
[**get_all_chats**](UIChatGPTControllerApi.md#get_all_chats) | **GET** /cc-ui/v1/clusters/{clusterId}/chat | Get chats by cluster ID
[**get_all_starters**](UIChatGPTControllerApi.md#get_all_starters) | **GET** /cc-ui/v1/clusters/chat/metadata | Get chat starters metadata
[**get_chat_by_id**](UIChatGPTControllerApi.md#get_chat_by_id) | **GET** /cc-ui/v1/clusters/chat/{chatId} | Get chat by ID
[**get_k8s_chats**](UIChatGPTControllerApi.md#get_k8s_chats) | **POST** /cc-ui/v1/clusters/{clusterId}/k8s-chat | Ask Questions about k8s operations

# **analyze_kubernetes_cluster**
> K8sAnalyzeResponse analyze_kubernetes_cluster(cluster_id, filters)



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
api_instance = swagger_client.UIChatGPTControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
filters = ['filters_example'] # list[str] | 

try:
    api_response = api_instance.analyze_kubernetes_cluster(cluster_id, filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UIChatGPTControllerApi->analyze_kubernetes_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **filters** | [**list[str]**](str.md)|  | 

### Return type

[**K8sAnalyzeResponse**](K8sAnalyzeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat**
> ChatMessage chat(body, chat_id)

Send a message to a chat

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
api_instance = swagger_client.UIChatGPTControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChatRequest() # ChatRequest | 
chat_id = 'chat_id_example' # str | Chat ID

try:
    # Send a message to a chat
    api_response = api_instance.chat(body, chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UIChatGPTControllerApi->chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChatRequest**](ChatRequest.md)|  | 
 **chat_id** | **str**| Chat ID | 

### Return type

[**ChatMessage**](ChatMessage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_chat**
> Chat create_chat(body, cluster_id)

Create a new chat

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
api_instance = swagger_client.UIChatGPTControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateChatRequest() # CreateChatRequest | 
cluster_id = 'cluster_id_example' # str | Cluster ID

try:
    # Create a new chat
    api_response = api_instance.create_chat(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UIChatGPTControllerApi->create_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateChatRequest**](CreateChatRequest.md)|  | 
 **cluster_id** | **str**| Cluster ID | 

### Return type

[**Chat**](Chat.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_chats**
> PageChat get_all_chats(cluster_id)

Get chats by cluster ID

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
api_instance = swagger_client.UIChatGPTControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | Cluster ID

try:
    # Get chats by cluster ID
    api_response = api_instance.get_all_chats(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UIChatGPTControllerApi->get_all_chats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster ID | 

### Return type

[**PageChat**](PageChat.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_starters**
> list[ChatStarterMetadata] get_all_starters()

Get chat starters metadata

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
api_instance = swagger_client.UIChatGPTControllerApi(swagger_client.ApiClient(configuration))

try:
    # Get chat starters metadata
    api_response = api_instance.get_all_starters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UIChatGPTControllerApi->get_all_starters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ChatStarterMetadata]**](ChatStarterMetadata.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_by_id**
> Chat get_chat_by_id(chat_id)

Get chat by ID

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
api_instance = swagger_client.UIChatGPTControllerApi(swagger_client.ApiClient(configuration))
chat_id = 'chat_id_example' # str | Chat ID

try:
    # Get chat by ID
    api_response = api_instance.get_chat_by_id(chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UIChatGPTControllerApi->get_chat_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **str**| Chat ID | 

### Return type

[**Chat**](Chat.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_k8s_chats**
> ChatMessage get_k8s_chats(body, cluster_id)

Ask Questions about k8s operations

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
api_instance = swagger_client.UIChatGPTControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ChatContext()] # list[ChatContext] | 
cluster_id = 'cluster_id_example' # str | Cluster ID

try:
    # Ask Questions about k8s operations
    api_response = api_instance.get_k8s_chats(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UIChatGPTControllerApi->get_k8s_chats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ChatContext]**](ChatContext.md)|  | 
 **cluster_id** | **str**| Cluster ID | 

### Return type

[**ChatMessage**](ChatMessage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

