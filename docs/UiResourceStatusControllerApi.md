# swagger_client.UiResourceStatusControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_release_preview_using_get**](UiResourceStatusControllerApi.md#get_release_preview_using_get) | **GET** /cc-ui/v1/resources/{clusterId}/release-preview | getReleasePreview
[**get_resource_status_using_get**](UiResourceStatusControllerApi.md#get_resource_status_using_get) | **GET** /cc-ui/v1/resources/{projectName}/{environmentName}/status | getResourceStatus
[**sync_resource_using_post**](UiResourceStatusControllerApi.md#sync_resource_using_post) | **POST** /cc-ui/v1/resources/sync | syncResource

# **get_release_preview_using_get**
> ReleasePreviewResponse get_release_preview_using_get(cluster_id)

getReleasePreview

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
api_instance = swagger_client.UiResourceStatusControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getReleasePreview
    api_response = api_instance.get_release_preview_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceStatusControllerApi->get_release_preview_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**ReleasePreviewResponse**](ReleasePreviewResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_status_using_get**
> ResourceStatusResponse get_resource_status_using_get(environment_name, project_name, resources)

getResourceStatus

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
api_instance = swagger_client.UiResourceStatusControllerApi(swagger_client.ApiClient(configuration))
environment_name = 'environment_name_example' # str | environmentName
project_name = 'project_name_example' # str | projectName
resources = NULL # object | resources

try:
    # getResourceStatus
    api_response = api_instance.get_resource_status_using_get(environment_name, project_name, resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceStatusControllerApi->get_resource_status_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_name** | **str**| environmentName | 
 **project_name** | **str**| projectName | 
 **resources** | [**object**](.md)| resources | 

### Return type

[**ResourceStatusResponse**](ResourceStatusResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_resource_using_post**
> ResourceStatusResponse sync_resource_using_post(body)

syncResource

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
api_instance = swagger_client.UiResourceStatusControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResourceSyncRequest() # ResourceSyncRequest | request

try:
    # syncResource
    api_response = api_instance.sync_resource_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceStatusControllerApi->sync_resource_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceSyncRequest**](ResourceSyncRequest.md)| request | 

### Return type

[**ResourceStatusResponse**](ResourceStatusResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

