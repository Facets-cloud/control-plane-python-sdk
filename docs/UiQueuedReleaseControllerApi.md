# swagger_client.UiQueuedReleaseControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_by_id**](UiQueuedReleaseControllerApi.md#delete_by_id) | **DELETE** /cc-ui/v1/clusters/{clusterId}/queued-releases/{queuedReleaseId} | 
[**get_all_queued_releases**](UiQueuedReleaseControllerApi.md#get_all_queued_releases) | **GET** /cc-ui/v1/clusters/{clusterId}/queued-releases/ | 

# **delete_by_id**
> delete_by_id(cluster_id, queued_release_id)



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
api_instance = swagger_client.UiQueuedReleaseControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
queued_release_id = 'queued_release_id_example' # str | 

try:
    api_instance.delete_by_id(cluster_id, queued_release_id)
except ApiException as e:
    print("Exception when calling UiQueuedReleaseControllerApi->delete_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **queued_release_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_queued_releases**
> list[ComCapillaryOpsCpBoReleaseQueuedRelease] get_all_queued_releases(cluster_id)



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
api_instance = swagger_client.UiQueuedReleaseControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_all_queued_releases(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiQueuedReleaseControllerApi->get_all_queued_releases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoReleaseQueuedRelease]**](ComCapillaryOpsCpBoReleaseQueuedRelease.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

