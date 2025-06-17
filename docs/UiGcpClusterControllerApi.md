# swagger_client.UiGcpClusterControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_draft_cluster**](UiGcpClusterControllerApi.md#configure_draft_cluster) | **POST** /cc-ui/v1/gcp/clusters/configure/{clusterId} | 
[**create_gcp_cluster**](UiGcpClusterControllerApi.md#create_gcp_cluster) | **POST** /cc-ui/v1/gcp/clusters | 
[**get_gcp_cluster**](UiGcpClusterControllerApi.md#get_gcp_cluster) | **GET** /cc-ui/v1/gcp/clusters/{clusterId} | 
[**update_gcp_cluster**](UiGcpClusterControllerApi.md#update_gcp_cluster) | **PUT** /cc-ui/v1/gcp/clusters/{clusterId} | 
[**validate_vpc_id**](UiGcpClusterControllerApi.md#validate_vpc_id) | **GET** /cc-ui/v1/gcp/clusters/validate-vpcId | 

# **configure_draft_cluster**
> GCPCluster configure_draft_cluster(body, cluster_id)



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
api_instance = swagger_client.UiGcpClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.GCPClusterRequest() # GCPClusterRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.configure_draft_cluster(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiGcpClusterControllerApi->configure_draft_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GCPClusterRequest**](GCPClusterRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**GCPCluster**](GCPCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_gcp_cluster**
> GCPCluster create_gcp_cluster(body)



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
api_instance = swagger_client.UiGcpClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.GCPClusterRequest() # GCPClusterRequest | 

try:
    api_response = api_instance.create_gcp_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiGcpClusterControllerApi->create_gcp_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GCPClusterRequest**](GCPClusterRequest.md)|  | 

### Return type

[**GCPCluster**](GCPCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gcp_cluster**
> GCPCluster get_gcp_cluster(cluster_id)



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
api_instance = swagger_client.UiGcpClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_gcp_cluster(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiGcpClusterControllerApi->get_gcp_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**GCPCluster**](GCPCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gcp_cluster**
> GCPCluster update_gcp_cluster(body, cluster_id)



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
api_instance = swagger_client.UiGcpClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.GCPClusterRequest() # GCPClusterRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.update_gcp_cluster(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiGcpClusterControllerApi->update_gcp_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GCPClusterRequest**](GCPClusterRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**GCPCluster**](GCPCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_vpc_id**
> bool validate_vpc_id(vpc_id, account_id)



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
api_instance = swagger_client.UiGcpClusterControllerApi(swagger_client.ApiClient(configuration))
vpc_id = 'vpc_id_example' # str | 
account_id = 'account_id_example' # str | 

try:
    api_response = api_instance.validate_vpc_id(vpc_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiGcpClusterControllerApi->validate_vpc_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpc_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

