# swagger_client.UiDeliveryPipelineControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_delivery_pipeline**](UiDeliveryPipelineControllerApi.md#get_delivery_pipeline) | **GET** /cc-ui/v1/delivery-pipeline/{stackName} | 
[**update_delivery_pipeline**](UiDeliveryPipelineControllerApi.md#update_delivery_pipeline) | **PUT** /cc-ui/v1/delivery-pipeline/{stackName} | 

# **get_delivery_pipeline**
> list[PipelineNode] get_delivery_pipeline(stack_name)



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
api_instance = swagger_client.UiDeliveryPipelineControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_delivery_pipeline(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeliveryPipelineControllerApi->get_delivery_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**list[PipelineNode]**](PipelineNode.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_delivery_pipeline**
> list[PipelineNode] update_delivery_pipeline(body, stack_name)



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
api_instance = swagger_client.UiDeliveryPipelineControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.PipelineNode()] # list[PipelineNode] | 
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.update_delivery_pipeline(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeliveryPipelineControllerApi->update_delivery_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[PipelineNode]**](PipelineNode.md)|  | 
 **stack_name** | **str**|  | 

### Return type

[**list[PipelineNode]**](PipelineNode.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

