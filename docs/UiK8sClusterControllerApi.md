# swagger_client.UiK8sClusterControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_draft_cluster**](UiK8sClusterControllerApi.md#create_draft_cluster) | **POST** /cc-ui/v1/kubernetes/clusters/configure/{clusterId} | 
[**create_k8s_cluster**](UiK8sClusterControllerApi.md#create_k8s_cluster) | **POST** /cc-ui/v1/kubernetes/clusters | 
[**get_k8s_cluster**](UiK8sClusterControllerApi.md#get_k8s_cluster) | **GET** /cc-ui/v1/kubernetes/clusters/{clusterId} | 
[**update_k8s_cluster**](UiK8sClusterControllerApi.md#update_k8s_cluster) | **PUT** /cc-ui/v1/kubernetes/clusters/{clusterId} | 

# **create_draft_cluster**
> ComCapillaryOpsCpBoKubernetesCluster create_draft_cluster(body, cluster_id)



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
api_instance = swagger_client.UiK8sClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsKubernetesClusterRequest() # ComCapillaryOpsCpBoRequestsKubernetesClusterRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.create_draft_cluster(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiK8sClusterControllerApi->create_draft_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsKubernetesClusterRequest**](ComCapillaryOpsCpBoRequestsKubernetesClusterRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoKubernetesCluster**](ComCapillaryOpsCpBoKubernetesCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_k8s_cluster**
> ComCapillaryOpsCpBoKubernetesCluster create_k8s_cluster(body)



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
api_instance = swagger_client.UiK8sClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsKubernetesClusterRequest() # ComCapillaryOpsCpBoRequestsKubernetesClusterRequest | 

try:
    api_response = api_instance.create_k8s_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiK8sClusterControllerApi->create_k8s_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsKubernetesClusterRequest**](ComCapillaryOpsCpBoRequestsKubernetesClusterRequest.md)|  | 

### Return type

[**ComCapillaryOpsCpBoKubernetesCluster**](ComCapillaryOpsCpBoKubernetesCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_k8s_cluster**
> ComCapillaryOpsCpBoKubernetesCluster get_k8s_cluster(cluster_id)



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
api_instance = swagger_client.UiK8sClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_k8s_cluster(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiK8sClusterControllerApi->get_k8s_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoKubernetesCluster**](ComCapillaryOpsCpBoKubernetesCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_k8s_cluster**
> ComCapillaryOpsCpBoKubernetesCluster update_k8s_cluster(body, cluster_id)



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
api_instance = swagger_client.UiK8sClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsKubernetesClusterRequest() # ComCapillaryOpsCpBoRequestsKubernetesClusterRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.update_k8s_cluster(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiK8sClusterControllerApi->update_k8s_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsKubernetesClusterRequest**](ComCapillaryOpsCpBoRequestsKubernetesClusterRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoKubernetesCluster**](ComCapillaryOpsCpBoKubernetesCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

