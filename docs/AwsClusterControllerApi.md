# swagger_client.AwsClusterControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster2**](AwsClusterControllerApi.md#create_cluster2) | **POST** /cc/v1/aws/clusters | 
[**get_cluster2**](AwsClusterControllerApi.md#get_cluster2) | **GET** /cc/v1/aws/clusters/{clusterId} | 
[**update_cluster2**](AwsClusterControllerApi.md#update_cluster2) | **PUT** /cc/v1/aws/clusters/{clusterId} | 

# **create_cluster2**
> ComCapillaryOpsCpBoAwsCluster create_cluster2(body)



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
api_instance = swagger_client.AwsClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsAwsClusterRequest() # ComCapillaryOpsCpBoRequestsAwsClusterRequest | 

try:
    api_response = api_instance.create_cluster2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsClusterControllerApi->create_cluster2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsAwsClusterRequest**](ComCapillaryOpsCpBoRequestsAwsClusterRequest.md)|  | 

### Return type

[**ComCapillaryOpsCpBoAwsCluster**](ComCapillaryOpsCpBoAwsCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster2**
> ComCapillaryOpsCpBoAwsCluster get_cluster2(cluster_id)



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
api_instance = swagger_client.AwsClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_cluster2(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsClusterControllerApi->get_cluster2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAwsCluster**](ComCapillaryOpsCpBoAwsCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster2**
> ComCapillaryOpsCpBoAwsCluster update_cluster2(body, cluster_id)



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
api_instance = swagger_client.AwsClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsAwsClusterRequest() # ComCapillaryOpsCpBoRequestsAwsClusterRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.update_cluster2(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsClusterControllerApi->update_cluster2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsAwsClusterRequest**](ComCapillaryOpsCpBoRequestsAwsClusterRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAwsCluster**](ComCapillaryOpsCpBoAwsCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

