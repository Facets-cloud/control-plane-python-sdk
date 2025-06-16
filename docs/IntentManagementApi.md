# swagger_client.IntentManagementApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_intent**](IntentManagementApi.md#create_or_update_intent) | **POST** /cc-ui/v1/intents | 
[**delete_intent**](IntentManagementApi.md#delete_intent) | **DELETE** /cc-ui/v1/intents/{name} | 
[**get_all_intents**](IntentManagementApi.md#get_all_intents) | **GET** /cc-ui/v1/intents | 

# **create_or_update_intent**
> ComCapillaryOpsCpV2RegistryIntentIntentResponseDTO create_or_update_intent(body)



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
api_instance = swagger_client.IntentManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpV2RegistryIntentIntentRequestDTO() # ComCapillaryOpsCpV2RegistryIntentIntentRequestDTO | 

try:
    api_response = api_instance.create_or_update_intent(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentManagementApi->create_or_update_intent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpV2RegistryIntentIntentRequestDTO**](ComCapillaryOpsCpV2RegistryIntentIntentRequestDTO.md)|  | 

### Return type

[**ComCapillaryOpsCpV2RegistryIntentIntentResponseDTO**](ComCapillaryOpsCpV2RegistryIntentIntentResponseDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_intent**
> delete_intent(name)



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
api_instance = swagger_client.IntentManagementApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_instance.delete_intent(name)
except ApiException as e:
    print("Exception when calling IntentManagementApi->delete_intent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_intents**
> list[ComCapillaryOpsCpV2RegistryIntentIntentResponseDTO] get_all_intents()



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
api_instance = swagger_client.IntentManagementApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_intents()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntentManagementApi->get_all_intents: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpV2RegistryIntentIntentResponseDTO]**](ComCapillaryOpsCpV2RegistryIntentIntentResponseDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

