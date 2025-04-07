# swagger_client.UiDeliveryPipelineControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_delivery_pipeline_using_get**](UiDeliveryPipelineControllerApi.md#get_delivery_pipeline_using_get) | **GET** /cc-ui/v1/delivery-pipeline/{stackName} | getDeliveryPipeline
[**update_delivery_pipeline_using_put**](UiDeliveryPipelineControllerApi.md#update_delivery_pipeline_using_put) | **PUT** /cc-ui/v1/delivery-pipeline/{stackName} | updateDeliveryPipeline


# **get_delivery_pipeline_using_get**
> list[PipelineNode] get_delivery_pipeline_using_get(stack_name)

getDeliveryPipeline

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
api_instance = swagger_client.UiDeliveryPipelineControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getDeliveryPipeline
    api_response = api_instance.get_delivery_pipeline_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeliveryPipelineControllerApi->get_delivery_pipeline_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**list[PipelineNode]**](PipelineNode.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_delivery_pipeline_using_put**
> list[PipelineNode] update_delivery_pipeline_using_put(pipeline_nodes, stack_name)

updateDeliveryPipeline

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
api_instance = swagger_client.UiDeliveryPipelineControllerApi(swagger_client.ApiClient(configuration))
pipeline_nodes = [swagger_client.PipelineNode()] # list[PipelineNode] | pipelineNodes
stack_name = 'stack_name_example' # str | stackName

try:
    # updateDeliveryPipeline
    api_response = api_instance.update_delivery_pipeline_using_put(pipeline_nodes, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeliveryPipelineControllerApi->update_delivery_pipeline_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_nodes** | [**list[PipelineNode]**](PipelineNode.md)| pipelineNodes | 
 **stack_name** | **str**| stackName | 

### Return type

[**list[PipelineNode]**](PipelineNode.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

