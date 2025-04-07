# swagger_client.UiQueuedReleaseControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_by_id_using_delete**](UiQueuedReleaseControllerApi.md#delete_by_id_using_delete) | **DELETE** /cc-ui/v1/clusters/{clusterId}/queued-releases/{queuedReleaseId} | deleteById
[**get_all_queued_releases_using_get**](UiQueuedReleaseControllerApi.md#get_all_queued_releases_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/queued-releases/ | getAllQueuedReleases


# **delete_by_id_using_delete**
> delete_by_id_using_delete(cluster_id, queued_release_id)

deleteById

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
api_instance = swagger_client.UiQueuedReleaseControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
queued_release_id = 'queued_release_id_example' # str | queuedReleaseId

try:
    # deleteById
    api_instance.delete_by_id_using_delete(cluster_id, queued_release_id)
except ApiException as e:
    print("Exception when calling UiQueuedReleaseControllerApi->delete_by_id_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **queued_release_id** | **str**| queuedReleaseId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_queued_releases_using_get**
> list[QueuedRelease] get_all_queued_releases_using_get(cluster_id)

getAllQueuedReleases

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
api_instance = swagger_client.UiQueuedReleaseControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getAllQueuedReleases
    api_response = api_instance.get_all_queued_releases_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiQueuedReleaseControllerApi->get_all_queued_releases_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**list[QueuedRelease]**](QueuedRelease.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

