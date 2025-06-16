# swagger_client.UiAzureClusterControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_draft_cluster1**](UiAzureClusterControllerApi.md#configure_draft_cluster1) | **POST** /cc-ui/v1/azure/clusters/configure/{clusterId} | 
[**create_azure_cluster**](UiAzureClusterControllerApi.md#create_azure_cluster) | **POST** /cc-ui/v1/azure/clusters | 
[**get_azure_cluster**](UiAzureClusterControllerApi.md#get_azure_cluster) | **GET** /cc-ui/v1/azure/clusters/{clusterId} | 
[**update_azure_cluster**](UiAzureClusterControllerApi.md#update_azure_cluster) | **PUT** /cc-ui/v1/azure/clusters/{clusterId} | 
[**validate_vnet**](UiAzureClusterControllerApi.md#validate_vnet) | **GET** /cc-ui/v1/azure/clusters/validate-vnet | 

# **configure_draft_cluster1**
> ComCapillaryOpsCpBoAzureCluster configure_draft_cluster1(body, cluster_id)



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
api_instance = swagger_client.UiAzureClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsAzureClusterRequest() # ComCapillaryOpsCpBoRequestsAzureClusterRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.configure_draft_cluster1(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAzureClusterControllerApi->configure_draft_cluster1: %s\n" % e)
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

# **create_azure_cluster**
> ComCapillaryOpsCpBoAzureCluster create_azure_cluster(body)



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
api_instance = swagger_client.UiAzureClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsAzureClusterRequest() # ComCapillaryOpsCpBoRequestsAzureClusterRequest | 

try:
    api_response = api_instance.create_azure_cluster(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAzureClusterControllerApi->create_azure_cluster: %s\n" % e)
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

# **get_azure_cluster**
> ComCapillaryOpsCpBoAzureCluster get_azure_cluster(cluster_id)



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
api_instance = swagger_client.UiAzureClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_azure_cluster(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAzureClusterControllerApi->get_azure_cluster: %s\n" % e)
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

# **update_azure_cluster**
> ComCapillaryOpsCpBoAzureCluster update_azure_cluster(body, cluster_id)



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
api_instance = swagger_client.UiAzureClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsAzureClusterRequest() # ComCapillaryOpsCpBoRequestsAzureClusterRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.update_azure_cluster(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAzureClusterControllerApi->update_azure_cluster: %s\n" % e)
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

# **validate_vnet**
> bool validate_vnet(vnet, resource_group, account_id)



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
api_instance = swagger_client.UiAzureClusterControllerApi(swagger_client.ApiClient(configuration))
vnet = 'vnet_example' # str | 
resource_group = 'resource_group_example' # str | 
account_id = 'account_id_example' # str | 

try:
    api_response = api_instance.validate_vnet(vnet, resource_group, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAzureClusterControllerApi->validate_vnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnet** | **str**|  | 
 **resource_group** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

