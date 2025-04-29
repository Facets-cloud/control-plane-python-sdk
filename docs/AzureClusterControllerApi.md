# swagger_client.AzureClusterControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_using_post1**](AzureClusterControllerApi.md#create_cluster_using_post1) | **POST** /cc/v1/azure/clusters | createCluster
[**get_cluster_using_get1**](AzureClusterControllerApi.md#get_cluster_using_get1) | **GET** /cc/v1/azure/clusters/{clusterId} | getCluster
[**update_cluster_using_put1**](AzureClusterControllerApi.md#update_cluster_using_put1) | **PUT** /cc/v1/azure/clusters/{clusterId} | updateCluster

# **create_cluster_using_post1**
> AzureCluster create_cluster_using_post1(body)

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
api_instance = swagger_client.AzureClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AzureClusterRequest() # AzureClusterRequest | request

try:
    # createCluster
    api_response = api_instance.create_cluster_using_post1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureClusterControllerApi->create_cluster_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AzureClusterRequest**](AzureClusterRequest.md)| request | 

### Return type

[**AzureCluster**](AzureCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_using_get1**
> AzureCluster get_cluster_using_get1(cluster_id)

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
api_instance = swagger_client.AzureClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getCluster
    api_response = api_instance.get_cluster_using_get1(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureClusterControllerApi->get_cluster_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**AzureCluster**](AzureCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_using_put1**
> AzureCluster update_cluster_using_put1(body, cluster_id)

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
api_instance = swagger_client.AzureClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AzureClusterRequest() # AzureClusterRequest | request
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # updateCluster
    api_response = api_instance.update_cluster_using_put1(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureClusterControllerApi->update_cluster_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AzureClusterRequest**](AzureClusterRequest.md)| request | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**AzureCluster**](AzureCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

