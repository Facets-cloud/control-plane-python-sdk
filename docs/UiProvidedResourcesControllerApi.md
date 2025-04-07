# swagger_client.UiProvidedResourcesControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_provided_resources_info_using_get**](UiProvidedResourcesControllerApi.md#get_provided_resources_info_using_get) | **GET** /cc-ui/v1/provided-resources/cluster/{clusterId}/resource-type/{resourceType}/resource-name/{resourceName} | getProvidedResourcesInfo
[**save_provided_resources_details_using_post**](UiProvidedResourcesControllerApi.md#save_provided_resources_details_using_post) | **POST** /cc-ui/v1/provided-resources/{clusterId} | saveProvidedResourcesDetails


# **get_provided_resources_info_using_get**
> GetProvidedResourcesResponse get_provided_resources_info_using_get(cluster_id, resource_name, resource_type)

getProvidedResourcesInfo

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
api_instance = swagger_client.UiProvidedResourcesControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # getProvidedResourcesInfo
    api_response = api_instance.get_provided_resources_info_using_get(cluster_id, resource_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiProvidedResourcesControllerApi->get_provided_resources_info_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 

### Return type

[**GetProvidedResourcesResponse**](GetProvidedResourcesResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_provided_resources_details_using_post**
> save_provided_resources_details_using_post(cluster_id, save_provided_resources_request)

saveProvidedResourcesDetails

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
api_instance = swagger_client.UiProvidedResourcesControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
save_provided_resources_request = swagger_client.SaveProvidedResourcesRequest() # SaveProvidedResourcesRequest | saveProvidedResourcesRequest

try:
    # saveProvidedResourcesDetails
    api_instance.save_provided_resources_details_using_post(cluster_id, save_provided_resources_request)
except ApiException as e:
    print("Exception when calling UiProvidedResourcesControllerApi->save_provided_resources_details_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **save_provided_resources_request** | [**SaveProvidedResourcesRequest**](SaveProvidedResourcesRequest.md)| saveProvidedResourcesRequest | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

