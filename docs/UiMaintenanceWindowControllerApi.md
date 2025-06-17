# swagger_client.UiMaintenanceWindowControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enable_disable**](UiMaintenanceWindowControllerApi.md#enable_disable) | **PUT** /cc-ui/v1/maintenance-window/{clusterId}/enable-disable | 
[**get_by_cluster_id**](UiMaintenanceWindowControllerApi.md#get_by_cluster_id) | **GET** /cc-ui/v1/maintenance-window/{clusterId} | 
[**update2**](UiMaintenanceWindowControllerApi.md#update2) | **PUT** /cc-ui/v1/maintenance-window | 

# **enable_disable**
> MaintenanceWindowDTO enable_disable(cluster_id, disabled)



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
api_instance = swagger_client.UiMaintenanceWindowControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
disabled = true # bool | 

try:
    api_response = api_instance.enable_disable(cluster_id, disabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiMaintenanceWindowControllerApi->enable_disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **disabled** | **bool**|  | 

### Return type

[**MaintenanceWindowDTO**](MaintenanceWindowDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_cluster_id**
> MaintenanceWindowDTO get_by_cluster_id(cluster_id)



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
api_instance = swagger_client.UiMaintenanceWindowControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_by_cluster_id(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiMaintenanceWindowControllerApi->get_by_cluster_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**MaintenanceWindowDTO**](MaintenanceWindowDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update2**
> MaintenanceWindowDTO update2(body)



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
api_instance = swagger_client.UiMaintenanceWindowControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.MaintenanceWindowDTO() # MaintenanceWindowDTO | 

try:
    api_response = api_instance.update2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiMaintenanceWindowControllerApi->update2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaintenanceWindowDTO**](MaintenanceWindowDTO.md)|  | 

### Return type

[**MaintenanceWindowDTO**](MaintenanceWindowDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

