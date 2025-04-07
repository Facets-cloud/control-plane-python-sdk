# swagger_client.GcpClusterControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_using_post2**](GcpClusterControllerApi.md#create_cluster_using_post2) | **POST** /cc/v1/gcp/clusters | createCluster
[**get_cluster_using_get2**](GcpClusterControllerApi.md#get_cluster_using_get2) | **GET** /cc/v1/gcp/clusters/{clusterId} | getCluster
[**update_cluster_using_put2**](GcpClusterControllerApi.md#update_cluster_using_put2) | **PUT** /cc/v1/gcp/clusters/{clusterId} | updateCluster


# **create_cluster_using_post2**
> GCPCluster create_cluster_using_post2(request)

createCluster

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
api_instance = swagger_client.GcpClusterControllerApi(swagger_client.ApiClient(configuration))
request = swagger_client.GCPClusterRequest() # GCPClusterRequest | request

try:
    # createCluster
    api_response = api_instance.create_cluster_using_post2(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GcpClusterControllerApi->create_cluster_using_post2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GCPClusterRequest**](GCPClusterRequest.md)| request | 

### Return type

[**GCPCluster**](GCPCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_using_get2**
> GCPCluster get_cluster_using_get2(cluster_id)

getCluster

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
api_instance = swagger_client.GcpClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getCluster
    api_response = api_instance.get_cluster_using_get2(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GcpClusterControllerApi->get_cluster_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**GCPCluster**](GCPCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_using_put2**
> GCPCluster update_cluster_using_put2(cluster_id, request)

updateCluster

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
api_instance = swagger_client.GcpClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
request = swagger_client.GCPClusterRequest() # GCPClusterRequest | request

try:
    # updateCluster
    api_response = api_instance.update_cluster_using_put2(cluster_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GcpClusterControllerApi->update_cluster_using_put2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **request** | [**GCPClusterRequest**](GCPClusterRequest.md)| request | 

### Return type

[**GCPCluster**](GCPCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

