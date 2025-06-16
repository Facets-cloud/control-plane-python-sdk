# swagger_client.AzureClusterControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster1**](AzureClusterControllerApi.md#create_cluster1) | **POST** /cc/v1/azure/clusters | 
[**get_cluster1**](AzureClusterControllerApi.md#get_cluster1) | **GET** /cc/v1/azure/clusters/{clusterId} | 
[**update_cluster1**](AzureClusterControllerApi.md#update_cluster1) | **PUT** /cc/v1/azure/clusters/{clusterId} | 

# **create_cluster1**
> ComCapillaryOpsCpBoAzureCluster create_cluster1(body)



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
api_instance = swagger_client.AzureClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsAzureClusterRequest() # ComCapillaryOpsCpBoRequestsAzureClusterRequest | 

try:
    api_response = api_instance.create_cluster1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureClusterControllerApi->create_cluster1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsAzureClusterRequest**](ComCapillaryOpsCpBoRequestsAzureClusterRequest.md)|  | 

### Return type

[**ComCapillaryOpsCpBoAzureCluster**](ComCapillaryOpsCpBoAzureCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster1**
> ComCapillaryOpsCpBoAzureCluster get_cluster1(cluster_id)



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
api_instance = swagger_client.AzureClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_cluster1(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureClusterControllerApi->get_cluster1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAzureCluster**](ComCapillaryOpsCpBoAzureCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster1**
> ComCapillaryOpsCpBoAzureCluster update_cluster1(body, cluster_id)



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
api_instance = swagger_client.AzureClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsAzureClusterRequest() # ComCapillaryOpsCpBoRequestsAzureClusterRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.update_cluster1(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureClusterControllerApi->update_cluster1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsAzureClusterRequest**](ComCapillaryOpsCpBoRequestsAzureClusterRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAzureCluster**](ComCapillaryOpsCpBoAzureCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

