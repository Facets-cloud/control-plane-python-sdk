# swagger_client.CallbackControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sonar_call_back**](CallbackControllerApi.md#sonar_call_back) | **POST** /callback/sonar | 

# **sonar_call_back**
> bool sonar_call_back(body)



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
api_instance = swagger_client.CallbackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoWebhookSonarCallbackBody() # ComCapillaryOpsDeployerBoWebhookSonarCallbackBody | 

try:
    api_response = api_instance.sonar_call_back(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallbackControllerApi->sonar_call_back: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoWebhookSonarCallbackBody**](ComCapillaryOpsDeployerBoWebhookSonarCallbackBody.md)|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

