# swagger_client.UiOneTimeWebhookControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poll_webhook**](UiOneTimeWebhookControllerApi.md#poll_webhook) | **GET** /cc-ui/v1/onetime-webhook/poll/{webhookId} | 
[**register_webhook**](UiOneTimeWebhookControllerApi.md#register_webhook) | **POST** /cc-ui/v1/onetime-webhook/register | 

# **poll_webhook**
> OneTimeWebhook poll_webhook(webhook_id)



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
api_instance = swagger_client.UiOneTimeWebhookControllerApi(swagger_client.ApiClient(configuration))
webhook_id = 'webhook_id_example' # str | 

try:
    api_response = api_instance.poll_webhook(webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOneTimeWebhookControllerApi->poll_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 

### Return type

[**OneTimeWebhook**](OneTimeWebhook.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_webhook**
> OneTimeWebhook register_webhook(body)



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
api_instance = swagger_client.UiOneTimeWebhookControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.OneTimeWebhook() # OneTimeWebhook | 

try:
    api_response = api_instance.register_webhook(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOneTimeWebhookControllerApi->register_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OneTimeWebhook**](OneTimeWebhook.md)|  | 

### Return type

[**OneTimeWebhook**](OneTimeWebhook.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

