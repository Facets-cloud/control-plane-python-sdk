# swagger_client.UiOneTimeWebhookControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poll_webhook_using_get**](UiOneTimeWebhookControllerApi.md#poll_webhook_using_get) | **GET** /cc-ui/v1/onetime-webhook/poll/{webhookId} | pollWebhook
[**register_webhook_using_post**](UiOneTimeWebhookControllerApi.md#register_webhook_using_post) | **POST** /cc-ui/v1/onetime-webhook/register | registerWebhook

# **poll_webhook_using_get**
> OneTimeWebhook poll_webhook_using_get(webhook_id)

pollWebhook

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
api_instance = swagger_client.UiOneTimeWebhookControllerApi(swagger_client.ApiClient(configuration))
webhook_id = 'webhook_id_example' # str | webhookId

try:
    # pollWebhook
    api_response = api_instance.poll_webhook_using_get(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOneTimeWebhookControllerApi->poll_webhook_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| webhookId | 

### Return type

[**OneTimeWebhook**](OneTimeWebhook.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_webhook_using_post**
> OneTimeWebhook register_webhook_using_post(body)

registerWebhook

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
api_instance = swagger_client.UiOneTimeWebhookControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.OneTimeWebhook() # OneTimeWebhook | webhook

try:
    # registerWebhook
    api_response = api_instance.register_webhook_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOneTimeWebhookControllerApi->register_webhook_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OneTimeWebhook**](OneTimeWebhook.md)| webhook | 

### Return type

[**OneTimeWebhook**](OneTimeWebhook.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

