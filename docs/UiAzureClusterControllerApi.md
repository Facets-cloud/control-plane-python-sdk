# swagger_client.UiAzureClusterControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_draft_cluster_using_post1**](UiAzureClusterControllerApi.md#configure_draft_cluster_using_post1) | **POST** /cc-ui/v1/azure/clusters/configure/{clusterId} | configureDraftCluster
[**create_azure_cluster_using_post**](UiAzureClusterControllerApi.md#create_azure_cluster_using_post) | **POST** /cc-ui/v1/azure/clusters | createAzureCluster
[**get_azure_cluster_using_get**](UiAzureClusterControllerApi.md#get_azure_cluster_using_get) | **GET** /cc-ui/v1/azure/clusters/{clusterId} | getAzureCluster
[**update_azure_cluster_using_put**](UiAzureClusterControllerApi.md#update_azure_cluster_using_put) | **PUT** /cc-ui/v1/azure/clusters/{clusterId} | updateAzureCluster
[**validate_vnet_using_get**](UiAzureClusterControllerApi.md#validate_vnet_using_get) | **GET** /cc-ui/v1/azure/clusters/validate-vnet | validateVnet

# **configure_draft_cluster_using_post1**
> AzureCluster configure_draft_cluster_using_post1(body, cluster_id)

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
api_instance = swagger_client.UiAzureClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AzureClusterRequest() # AzureClusterRequest | request
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # configureDraftCluster
    api_response = api_instance.configure_draft_cluster_using_post1(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAzureClusterControllerApi->configure_draft_cluster_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AzureClusterRequest**](AzureClusterRequest.md)| request | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**AzureCluster**](AzureCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_azure_cluster_using_post**
> AzureCluster create_azure_cluster_using_post(body)

createAzureCluster

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
api_instance = swagger_client.UiAzureClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AzureClusterRequest() # AzureClusterRequest | request

try:
    # createAzureCluster
    api_response = api_instance.create_azure_cluster_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAzureClusterControllerApi->create_azure_cluster_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AzureClusterRequest**](AzureClusterRequest.md)| request | 

### Return type

[**AzureCluster**](AzureCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_cluster_using_get**
> AzureCluster get_azure_cluster_using_get(cluster_id)

getAzureCluster

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
api_instance = swagger_client.UiAzureClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getAzureCluster
    api_response = api_instance.get_azure_cluster_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAzureClusterControllerApi->get_azure_cluster_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**AzureCluster**](AzureCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_azure_cluster_using_put**
> AzureCluster update_azure_cluster_using_put(body, cluster_id)

updateAzureCluster

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
api_instance = swagger_client.UiAzureClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AzureClusterRequest() # AzureClusterRequest | request
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # updateAzureCluster
    api_response = api_instance.update_azure_cluster_using_put(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAzureClusterControllerApi->update_azure_cluster_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AzureClusterRequest**](AzureClusterRequest.md)| request | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**AzureCluster**](AzureCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_vnet_using_get**
> bool validate_vnet_using_get(account_id, resource_group, vnet)

validateVnet

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
api_instance = swagger_client.UiAzureClusterControllerApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | accountId
resource_group = 'resource_group_example' # str | resourceGroup
vnet = 'vnet_example' # str | vnet

try:
    # validateVnet
    api_response = api_instance.validate_vnet_using_get(account_id, resource_group, vnet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAzureClusterControllerApi->validate_vnet_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | 
 **resource_group** | **str**| resourceGroup | 
 **vnet** | **str**| vnet | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

