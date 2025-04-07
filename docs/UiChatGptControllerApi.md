# swagger_client.UiChatGptControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_kubernetes_cluster_using_get**](UiChatGptControllerApi.md#analyze_kubernetes_cluster_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/kubernetes/analyze | analyzeKubernetesCluster
[**chat_using_post**](UiChatGptControllerApi.md#chat_using_post) | **POST** /cc-ui/v1/clusters/chat/{chatId} | Send a message to a chat
[**create_chat_using_post**](UiChatGptControllerApi.md#create_chat_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/chat | Create a new chat
[**get_all_chats_using_get**](UiChatGptControllerApi.md#get_all_chats_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/chat | Get chats by cluster ID
[**get_all_starters_using_get**](UiChatGptControllerApi.md#get_all_starters_using_get) | **GET** /cc-ui/v1/clusters/chat/metadata | Get chat starters metadata
[**get_chat_by_id_using_get**](UiChatGptControllerApi.md#get_chat_by_id_using_get) | **GET** /cc-ui/v1/clusters/chat/{chatId} | Get chat by ID
[**get_k8s_chats_using_post**](UiChatGptControllerApi.md#get_k8s_chats_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/k8s-chat | Ask Questions about k8s operations


# **analyze_kubernetes_cluster_using_get**
> K8sAnalyzeResponse analyze_kubernetes_cluster_using_get(cluster_id, filters)

analyzeKubernetesCluster

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
api_instance = swagger_client.UiChatGptControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
filters = ['filters_example'] # list[str] | filters

try:
    # analyzeKubernetesCluster
    api_response = api_instance.analyze_kubernetes_cluster_using_get(cluster_id, filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiChatGptControllerApi->analyze_kubernetes_cluster_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **filters** | [**list[str]**](str.md)| filters | 

### Return type

[**K8sAnalyzeResponse**](K8sAnalyzeResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_using_post**
> ChatMessage chat_using_post(chat_id, request)

Send a message to a chat

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
api_instance = swagger_client.UiChatGptControllerApi(swagger_client.ApiClient(configuration))
chat_id = 'chat_id_example' # str | Chat ID
request = swagger_client.ChatRequest() # ChatRequest | request

try:
    # Send a message to a chat
    api_response = api_instance.chat_using_post(chat_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiChatGptControllerApi->chat_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **str**| Chat ID | 
 **request** | [**ChatRequest**](ChatRequest.md)| request | 

### Return type

[**ChatMessage**](ChatMessage.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_chat_using_post**
> Chat create_chat_using_post(cluster_id, request)

Create a new chat

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
api_instance = swagger_client.UiChatGptControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | Cluster ID
request = swagger_client.CreateChatRequest() # CreateChatRequest | request

try:
    # Create a new chat
    api_response = api_instance.create_chat_using_post(cluster_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiChatGptControllerApi->create_chat_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster ID | 
 **request** | [**CreateChatRequest**](CreateChatRequest.md)| request | 

### Return type

[**Chat**](Chat.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_chats_using_get**
> PageChat get_all_chats_using_get(cluster_id)

Get chats by cluster ID

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
api_instance = swagger_client.UiChatGptControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | Cluster ID

try:
    # Get chats by cluster ID
    api_response = api_instance.get_all_chats_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiChatGptControllerApi->get_all_chats_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster ID | 

### Return type

[**PageChat**](PageChat.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_starters_using_get**
> list[ChatStarterMetadata] get_all_starters_using_get()

Get chat starters metadata

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
api_instance = swagger_client.UiChatGptControllerApi(swagger_client.ApiClient(configuration))

try:
    # Get chat starters metadata
    api_response = api_instance.get_all_starters_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiChatGptControllerApi->get_all_starters_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ChatStarterMetadata]**](ChatStarterMetadata.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_by_id_using_get**
> Chat get_chat_by_id_using_get(chat_id)

Get chat by ID

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
api_instance = swagger_client.UiChatGptControllerApi(swagger_client.ApiClient(configuration))
chat_id = 'chat_id_example' # str | Chat ID

try:
    # Get chat by ID
    api_response = api_instance.get_chat_by_id_using_get(chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiChatGptControllerApi->get_chat_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_id** | **str**| Chat ID | 

### Return type

[**Chat**](Chat.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_k8s_chats_using_post**
> ChatMessage get_k8s_chats_using_post(cluster_id, questions)

Ask Questions about k8s operations

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
api_instance = swagger_client.UiChatGptControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | Cluster ID
questions = [swagger_client.ChatContext()] # list[ChatContext] | questions

try:
    # Ask Questions about k8s operations
    api_response = api_instance.get_k8s_chats_using_post(cluster_id, questions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiChatGptControllerApi->get_k8s_chats_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster ID | 
 **questions** | [**list[ChatContext]**](ChatContext.md)| questions | 

### Return type

[**ChatMessage**](ChatMessage.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

