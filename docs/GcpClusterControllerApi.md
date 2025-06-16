# swagger_client.GcpClusterControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster**](GcpClusterControllerApi.md#create_cluster) | **POST** /cc/v1/gcp/clusters | 
[**get_cluster**](GcpClusterControllerApi.md#get_cluster) | **GET** /cc/v1/gcp/clusters/{clusterId} | 
[**update_cluster**](GcpClusterControllerApi.md#update_cluster) | **PUT** /cc/v1/gcp/clusters/{clusterId} | 

# **create_cluster**
> ComCapillaryOpsCpBoGCPCluster create_cluster(body)



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
api_instance = swagger_client.GcpClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsGCPClusterRequest() # ComCapillaryOpsCpBoRequestsGCPClusterRequest | 

try:
    api_response = api_instance.create_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GcpClusterControllerApi->create_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsGCPClusterRequest**](ComCapillaryOpsCpBoRequestsGCPClusterRequest.md)|  | 

### Return type

[**ComCapillaryOpsCpBoGCPCluster**](ComCapillaryOpsCpBoGCPCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster**
> ComCapillaryOpsCpBoGCPCluster get_cluster(cluster_id)



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
api_instance = swagger_client.GcpClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_cluster(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GcpClusterControllerApi->get_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoGCPCluster**](ComCapillaryOpsCpBoGCPCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster**
> ComCapillaryOpsCpBoGCPCluster update_cluster(body, cluster_id)



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
api_instance = swagger_client.GcpClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsGCPClusterRequest() # ComCapillaryOpsCpBoRequestsGCPClusterRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.update_cluster(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GcpClusterControllerApi->update_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsGCPClusterRequest**](ComCapillaryOpsCpBoRequestsGCPClusterRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoGCPCluster**](ComCapillaryOpsCpBoGCPCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

