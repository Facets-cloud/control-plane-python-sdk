# swagger_client.UiCloudCostExplorerControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_daily_cloud_cost**](UiCloudCostExplorerControllerApi.md#get_daily_cloud_cost) | **GET** /cc-ui/v1/cost-explorer/stack/{stackName}/daily-cost | 
[**get_service_wise_cost**](UiCloudCostExplorerControllerApi.md#get_service_wise_cost) | **GET** /cc-ui/v1/cost-explorer/service-wise-cost/{clusterId} | 
[**is_aws_cost_explorer_enabled**](UiCloudCostExplorerControllerApi.md#is_aws_cost_explorer_enabled) | **GET** /cc-ui/v1/cost-explorer/aws/enabled | 
[**sync_cloud_cost**](UiCloudCostExplorerControllerApi.md#sync_cloud_cost) | **GET** /cc-ui/v1/cost-explorer/sync-cost | 

# **get_daily_cloud_cost**
> DailyCloudCostDTO get_daily_cloud_cost(stack_name, start, end, cluster_ids=cluster_ids)



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
api_instance = swagger_client.UiCloudCostExplorerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
start = '2013-10-20' # date | 
end = '2013-10-20' # date | 
cluster_ids = ['cluster_ids_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_daily_cloud_cost(stack_name, start, end, cluster_ids=cluster_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCloudCostExplorerControllerApi->get_daily_cloud_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **start** | **date**|  | 
 **end** | **date**|  | 
 **cluster_ids** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**DailyCloudCostDTO**](DailyCloudCostDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_wise_cost**
> list[DailyCost] get_service_wise_cost(cluster_id, start, end)



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
api_instance = swagger_client.UiCloudCostExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
start = '2013-10-20' # date | 
end = '2013-10-20' # date | 

try:
    api_response = api_instance.get_service_wise_cost(cluster_id, start, end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCloudCostExplorerControllerApi->get_service_wise_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **start** | **date**|  | 
 **end** | **date**|  | 

### Return type

[**list[DailyCost]**](DailyCost.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_aws_cost_explorer_enabled**
> bool is_aws_cost_explorer_enabled()



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
api_instance = swagger_client.UiCloudCostExplorerControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.is_aws_cost_explorer_enabled()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCloudCostExplorerControllerApi->is_aws_cost_explorer_enabled: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_cloud_cost**
> sync_cloud_cost()



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
api_instance = swagger_client.UiCloudCostExplorerControllerApi(swagger_client.ApiClient(configuration))

try:
    api_instance.sync_cloud_cost()
except ApiException as e:
    print("Exception when calling UiCloudCostExplorerControllerApi->sync_cloud_cost: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

