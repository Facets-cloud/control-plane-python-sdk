# swagger_client.CallbackControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sonar_call_back_using_post**](CallbackControllerApi.md#sonar_call_back_using_post) | **POST** /callback/sonar | sonarCallBack


# **sonar_call_back_using_post**
> bool sonar_call_back_using_post(body)

sonarCallBack

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
api_instance = swagger_client.CallbackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CallbackBody() # CallbackBody | body

try:
    # sonarCallBack
    api_response = api_instance.sonar_call_back_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallbackControllerApi->sonar_call_back_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CallbackBody**](CallbackBody.md)| body | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

