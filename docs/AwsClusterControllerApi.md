# swagger_client.AwsClusterControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_using_post**](AwsClusterControllerApi.md#create_cluster_using_post) | **POST** /cc/v1/aws/clusters | createCluster
[**get_cluster_using_get**](AwsClusterControllerApi.md#get_cluster_using_get) | **GET** /cc/v1/aws/clusters/{clusterId} | getCluster
[**update_cluster_using_put**](AwsClusterControllerApi.md#update_cluster_using_put) | **PUT** /cc/v1/aws/clusters/{clusterId} | updateCluster

# **create_cluster_using_post**
> AwsCluster create_cluster_using_post(body)

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
api_instance = swagger_client.AwsClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AwsClusterRequest() # AwsClusterRequest | request

try:
    # createCluster
    api_response = api_instance.create_cluster_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsClusterControllerApi->create_cluster_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AwsClusterRequest**](AwsClusterRequest.md)| request | 

### Return type

[**AwsCluster**](AwsCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_using_get**
> AwsCluster get_cluster_using_get(cluster_id)

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
api_instance = swagger_client.AwsClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getCluster
    api_response = api_instance.get_cluster_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsClusterControllerApi->get_cluster_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**AwsCluster**](AwsCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_using_put**
> AwsCluster update_cluster_using_put(body, cluster_id)

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
api_instance = swagger_client.AwsClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AwsClusterRequest() # AwsClusterRequest | request
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # updateCluster
    api_response = api_instance.update_cluster_using_put(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsClusterControllerApi->update_cluster_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AwsClusterRequest**](AwsClusterRequest.md)| request | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**AwsCluster**](AwsCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

