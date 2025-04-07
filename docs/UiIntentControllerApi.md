# swagger_client.UiIntentControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_intent_using_post**](UiIntentControllerApi.md#create_or_update_intent_using_post) | **POST** /cc-ui/v1/intents | createOrUpdateIntent
[**delete_intent_using_delete**](UiIntentControllerApi.md#delete_intent_using_delete) | **DELETE** /cc-ui/v1/intents/{name} | deleteIntent
[**get_all_intents_using_get**](UiIntentControllerApi.md#get_all_intents_using_get) | **GET** /cc-ui/v1/intents | getAllIntents


# **create_or_update_intent_using_post**
> IntentResponseDTO create_or_update_intent_using_post(request_dto)

createOrUpdateIntent

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
api_instance = swagger_client.UiIntentControllerApi(swagger_client.ApiClient(configuration))
request_dto = swagger_client.IntentRequestDTO() # IntentRequestDTO | requestDTO

try:
    # createOrUpdateIntent
    api_response = api_instance.create_or_update_intent_using_post(request_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiIntentControllerApi->create_or_update_intent_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_dto** | [**IntentRequestDTO**](IntentRequestDTO.md)| requestDTO | 

### Return type

[**IntentResponseDTO**](IntentResponseDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_intent_using_delete**
> delete_intent_using_delete(name)

deleteIntent

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
api_instance = swagger_client.UiIntentControllerApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | name

try:
    # deleteIntent
    api_instance.delete_intent_using_delete(name)
except ApiException as e:
    print("Exception when calling UiIntentControllerApi->delete_intent_using_delete: %s\n" % e)
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

# **get_all_intents_using_get**
> list[IntentResponseDTO] get_all_intents_using_get()

getAllIntents

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
api_instance = swagger_client.UiIntentControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllIntents
    api_response = api_instance.get_all_intents_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiIntentControllerApi->get_all_intents_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[IntentResponseDTO]**](IntentResponseDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

