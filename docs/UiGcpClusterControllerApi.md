# swagger_client.UiGcpClusterControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_draft_cluster_using_post2**](UiGcpClusterControllerApi.md#configure_draft_cluster_using_post2) | **POST** /cc-ui/v1/gcp/clusters/configure/{clusterId} | configureDraftCluster
[**create_gcp_cluster_using_post**](UiGcpClusterControllerApi.md#create_gcp_cluster_using_post) | **POST** /cc-ui/v1/gcp/clusters | createGCPCluster
[**get_gcp_cluster_using_get**](UiGcpClusterControllerApi.md#get_gcp_cluster_using_get) | **GET** /cc-ui/v1/gcp/clusters/{clusterId} | getGCPCluster
[**update_gcp_cluster_using_put**](UiGcpClusterControllerApi.md#update_gcp_cluster_using_put) | **PUT** /cc-ui/v1/gcp/clusters/{clusterId} | updateGCPCluster
[**validate_vpc_id_using_get1**](UiGcpClusterControllerApi.md#validate_vpc_id_using_get1) | **GET** /cc-ui/v1/gcp/clusters/validate-vpcId | validateVpcId


# **configure_draft_cluster_using_post2**
> GCPCluster configure_draft_cluster_using_post2(cluster_id, request)

configureDraftCluster

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
api_instance = swagger_client.UiGcpClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
request = swagger_client.GCPClusterRequest() # GCPClusterRequest | request

try:
    # configureDraftCluster
    api_response = api_instance.configure_draft_cluster_using_post2(cluster_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiGcpClusterControllerApi->configure_draft_cluster_using_post2: %s\n" % e)
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

# **create_gcp_cluster_using_post**
> GCPCluster create_gcp_cluster_using_post(request)

createGCPCluster

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
api_instance = swagger_client.UiGcpClusterControllerApi(swagger_client.ApiClient(configuration))
request = swagger_client.GCPClusterRequest() # GCPClusterRequest | request

try:
    # createGCPCluster
    api_response = api_instance.create_gcp_cluster_using_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiGcpClusterControllerApi->create_gcp_cluster_using_post: %s\n" % e)
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

# **get_gcp_cluster_using_get**
> GCPCluster get_gcp_cluster_using_get(cluster_id)

getGCPCluster

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
api_instance = swagger_client.UiGcpClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getGCPCluster
    api_response = api_instance.get_gcp_cluster_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiGcpClusterControllerApi->get_gcp_cluster_using_get: %s\n" % e)
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

# **update_gcp_cluster_using_put**
> GCPCluster update_gcp_cluster_using_put(cluster_id, request)

updateGCPCluster

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
api_instance = swagger_client.UiGcpClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
request = swagger_client.GCPClusterRequest() # GCPClusterRequest | request

try:
    # updateGCPCluster
    api_response = api_instance.update_gcp_cluster_using_put(cluster_id, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiGcpClusterControllerApi->update_gcp_cluster_using_put: %s\n" % e)
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

# **validate_vpc_id_using_get1**
> bool validate_vpc_id_using_get1(account_id, vpc_id)

validateVpcId

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
api_instance = swagger_client.UiGcpClusterControllerApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | accountId
vpc_id = 'vpc_id_example' # str | vpcId

try:
    # validateVpcId
    api_response = api_instance.validate_vpc_id_using_get1(account_id, vpc_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiGcpClusterControllerApi->validate_vpc_id_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | 
 **vpc_id** | **str**| vpcId | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

