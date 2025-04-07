# swagger_client.UiK8sClusterControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_draft_cluster_using_post1**](UiK8sClusterControllerApi.md#create_draft_cluster_using_post1) | **POST** /cc-ui/v1/kubernetes/clusters/configure/{clusterId} | createDraftCluster
[**create_k8s_cluster_using_post**](UiK8sClusterControllerApi.md#create_k8s_cluster_using_post) | **POST** /cc-ui/v1/kubernetes/clusters | createK8sCluster
[**get_k8s_cluster_using_get**](UiK8sClusterControllerApi.md#get_k8s_cluster_using_get) | **GET** /cc-ui/v1/kubernetes/clusters/{clusterId} | getK8sCluster
[**update_k8s_cluster_using_put**](UiK8sClusterControllerApi.md#update_k8s_cluster_using_put) | **PUT** /cc-ui/v1/kubernetes/clusters/{clusterId} | updateK8sCluster


# **create_draft_cluster_using_post1**
> KubernetesCluster create_draft_cluster_using_post1(cluster_id, request)

createDraftCluster

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
api_instance = swagger_client.UiK8sClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
request = swagger_client.KubernetesClusterRequest() # KubernetesClusterRequest | request

try:
    # createDraftCluster
    api_response = api_instance.create_draft_cluster_using_post1(cluster_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiK8sClusterControllerApi->create_draft_cluster_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **request** | [**KubernetesClusterRequest**](KubernetesClusterRequest.md)| request | 

### Return type

[**KubernetesCluster**](KubernetesCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_k8s_cluster_using_post**
> KubernetesCluster create_k8s_cluster_using_post(request)

createK8sCluster

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
api_instance = swagger_client.UiK8sClusterControllerApi(swagger_client.ApiClient(configuration))
request = swagger_client.KubernetesClusterRequest() # KubernetesClusterRequest | request

try:
    # createK8sCluster
    api_response = api_instance.create_k8s_cluster_using_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiK8sClusterControllerApi->create_k8s_cluster_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**KubernetesClusterRequest**](KubernetesClusterRequest.md)| request | 

### Return type

[**KubernetesCluster**](KubernetesCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_k8s_cluster_using_get**
> KubernetesCluster get_k8s_cluster_using_get(cluster_id)

getK8sCluster

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
api_instance = swagger_client.UiK8sClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getK8sCluster
    api_response = api_instance.get_k8s_cluster_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiK8sClusterControllerApi->get_k8s_cluster_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**KubernetesCluster**](KubernetesCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_k8s_cluster_using_put**
> KubernetesCluster update_k8s_cluster_using_put(cluster_id, request)

updateK8sCluster

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
api_instance = swagger_client.UiK8sClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
request = swagger_client.KubernetesClusterRequest() # KubernetesClusterRequest | request

try:
    # updateK8sCluster
    api_response = api_instance.update_k8s_cluster_using_put(cluster_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiK8sClusterControllerApi->update_k8s_cluster_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **request** | [**KubernetesClusterRequest**](KubernetesClusterRequest.md)| request | 

### Return type

[**KubernetesCluster**](KubernetesCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

