# swagger_client.UiMaintenanceWindowControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enable_disable_using_put**](UiMaintenanceWindowControllerApi.md#enable_disable_using_put) | **PUT** /cc-ui/v1/maintenance-window/{clusterId}/enable-disable | enableDisable
[**get_by_cluster_id_using_get**](UiMaintenanceWindowControllerApi.md#get_by_cluster_id_using_get) | **GET** /cc-ui/v1/maintenance-window/{clusterId} | getByClusterId
[**update_using_put**](UiMaintenanceWindowControllerApi.md#update_using_put) | **PUT** /cc-ui/v1/maintenance-window | update

# **enable_disable_using_put**
> MaintenanceWindowDTO enable_disable_using_put(cluster_id, disabled)

enableDisable

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
api_instance = swagger_client.UiMaintenanceWindowControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
disabled = true # bool | disabled

try:
    # enableDisable
    api_response = api_instance.enable_disable_using_put(cluster_id, disabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiMaintenanceWindowControllerApi->enable_disable_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **disabled** | **bool**| disabled | 

### Return type

[**MaintenanceWindowDTO**](MaintenanceWindowDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_cluster_id_using_get**
> MaintenanceWindowDTO get_by_cluster_id_using_get(cluster_id)

getByClusterId

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
api_instance = swagger_client.UiMaintenanceWindowControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getByClusterId
    api_response = api_instance.get_by_cluster_id_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiMaintenanceWindowControllerApi->get_by_cluster_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**MaintenanceWindowDTO**](MaintenanceWindowDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put**
> MaintenanceWindowDTO update_using_put(body)

update

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
api_instance = swagger_client.UiMaintenanceWindowControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.MaintenanceWindowDTO() # MaintenanceWindowDTO | maintenanceWindowDTO

try:
    # update
    api_response = api_instance.update_using_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiMaintenanceWindowControllerApi->update_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MaintenanceWindowDTO**](MaintenanceWindowDTO.md)| maintenanceWindowDTO | 

### Return type

[**MaintenanceWindowDTO**](MaintenanceWindowDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

