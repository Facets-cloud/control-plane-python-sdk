# swagger_client.UiTfOutputControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_output_using_post**](UiTfOutputControllerApi.md#create_or_update_output_using_post) | **POST** /cc-ui/v1/tf-outputs | createOrUpdateOutput
[**delete_output_using_delete**](UiTfOutputControllerApi.md#delete_output_using_delete) | **DELETE** /cc-ui/v1/tf-outputs/{name} | deleteOutput
[**get_all_outputs_using_get**](UiTfOutputControllerApi.md#get_all_outputs_using_get) | **GET** /cc-ui/v1/tf-outputs | getAllOutputs


# **create_or_update_output_using_post**
> TFOutput create_or_update_output_using_post(request_dto)

createOrUpdateOutput

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
api_instance = swagger_client.UiTfOutputControllerApi(swagger_client.ApiClient(configuration))
request_dto = swagger_client.TFOutputRequestDTO() # TFOutputRequestDTO | requestDTO

try:
    # createOrUpdateOutput
    api_response = api_instance.create_or_update_output_using_post(request_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfOutputControllerApi->create_or_update_output_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_dto** | [**TFOutputRequestDTO**](TFOutputRequestDTO.md)| requestDTO | 

### Return type

[**TFOutput**](TFOutput.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_output_using_delete**
> delete_output_using_delete(name)

deleteOutput

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
api_instance = swagger_client.UiTfOutputControllerApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | name

try:
    # deleteOutput
    api_instance.delete_output_using_delete(name)
except ApiException as e:
    print("Exception when calling UiTfOutputControllerApi->delete_output_using_delete: %s\n" % e)
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

# **get_all_outputs_using_get**
> list[TFOutput] get_all_outputs_using_get()

getAllOutputs

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
api_instance = swagger_client.UiTfOutputControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllOutputs
    api_response = api_instance.get_all_outputs_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfOutputControllerApi->get_all_outputs_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TFOutput]**](TFOutput.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

