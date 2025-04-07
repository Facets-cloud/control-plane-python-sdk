# swagger_client.UiLocalClusterControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_using_post3**](UiLocalClusterControllerApi.md#create_cluster_using_post3) | **POST** /cc-ui/v1/local/clusters | Create a new Environment for a blueprint
[**get_cluster_using_get3**](UiLocalClusterControllerApi.md#get_cluster_using_get3) | **GET** /cc-ui/v1/local/clusters/{clusterId} | getCluster
[**get_vagrant_using_get**](UiLocalClusterControllerApi.md#get_vagrant_using_get) | **GET** /cc-ui/v1/local/clusters/{clusterId}/vagrant | getVagrant
[**update_cluster_using_put3**](UiLocalClusterControllerApi.md#update_cluster_using_put3) | **PUT** /cc-ui/v1/local/clusters/{clusterId} | updateCluster


# **create_cluster_using_post3**
> LocalCluster create_cluster_using_post3(request)

Create a new Environment for a blueprint

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
api_instance = swagger_client.UiLocalClusterControllerApi(swagger_client.ApiClient(configuration))
request = swagger_client.LocalClusterRequest() # LocalClusterRequest | request

try:
    # Create a new Environment for a blueprint
    api_response = api_instance.create_cluster_using_post3(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiLocalClusterControllerApi->create_cluster_using_post3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**LocalClusterRequest**](LocalClusterRequest.md)| request | 

### Return type

[**LocalCluster**](LocalCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_using_get3**
> LocalCluster get_cluster_using_get3(cluster_id)

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
api_instance = swagger_client.UiLocalClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getCluster
    api_response = api_instance.get_cluster_using_get3(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiLocalClusterControllerApi->get_cluster_using_get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**LocalCluster**](LocalCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vagrant_using_get**
> str get_vagrant_using_get(cluster_id)

getVagrant

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
api_instance = swagger_client.UiLocalClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getVagrant
    api_response = api_instance.get_vagrant_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiLocalClusterControllerApi->get_vagrant_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_using_put3**
> LocalCluster update_cluster_using_put3(cluster_id, request)

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
api_instance = swagger_client.UiLocalClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
request = swagger_client.LocalClusterRequest() # LocalClusterRequest | request

try:
    # updateCluster
    api_response = api_instance.update_cluster_using_put3(cluster_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiLocalClusterControllerApi->update_cluster_using_put3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **request** | [**LocalClusterRequest**](LocalClusterRequest.md)| request | 

### Return type

[**LocalCluster**](LocalCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

