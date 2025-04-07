# swagger_client.UiCloudCostExplorerControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_daily_cloud_cost_using_get**](UiCloudCostExplorerControllerApi.md#get_daily_cloud_cost_using_get) | **GET** /cc-ui/v1/cost-explorer/stack/{stackName}/daily-cost | getDailyCloudCost
[**get_service_wise_cost_using_get**](UiCloudCostExplorerControllerApi.md#get_service_wise_cost_using_get) | **GET** /cc-ui/v1/cost-explorer/service-wise-cost/{clusterId} | getServiceWiseCost
[**is_aws_cost_explorer_enabled_using_get**](UiCloudCostExplorerControllerApi.md#is_aws_cost_explorer_enabled_using_get) | **GET** /cc-ui/v1/cost-explorer/aws/enabled | isAwsCostExplorerEnabled
[**sync_cloud_cost_using_get**](UiCloudCostExplorerControllerApi.md#sync_cloud_cost_using_get) | **GET** /cc-ui/v1/cost-explorer/sync-cost | syncCloudCost


# **get_daily_cloud_cost_using_get**
> DailyCloudCostDTO get_daily_cloud_cost_using_get(end, stack_name, start, cluster_ids=cluster_ids)

getDailyCloudCost

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
api_instance = swagger_client.UiCloudCostExplorerControllerApi(swagger_client.ApiClient(configuration))
end = '2013-10-20' # date | end
stack_name = 'stack_name_example' # str | stackName
start = '2013-10-20' # date | start
cluster_ids = ['cluster_ids_example'] # list[str] | clusterIds (optional)

try:
    # getDailyCloudCost
    api_response = api_instance.get_daily_cloud_cost_using_get(end, stack_name, start, cluster_ids=cluster_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCloudCostExplorerControllerApi->get_daily_cloud_cost_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end** | **date**| end | 
 **stack_name** | **str**| stackName | 
 **start** | **date**| start | 
 **cluster_ids** | [**list[str]**](str.md)| clusterIds | [optional] 

### Return type

[**DailyCloudCostDTO**](DailyCloudCostDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_wise_cost_using_get**
> list[DailyCost] get_service_wise_cost_using_get(cluster_id, end, start)

getServiceWiseCost

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
api_instance = swagger_client.UiCloudCostExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
end = '2013-10-20' # date | end
start = '2013-10-20' # date | start

try:
    # getServiceWiseCost
    api_response = api_instance.get_service_wise_cost_using_get(cluster_id, end, start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCloudCostExplorerControllerApi->get_service_wise_cost_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **end** | **date**| end | 
 **start** | **date**| start | 

### Return type

[**list[DailyCost]**](DailyCost.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_aws_cost_explorer_enabled_using_get**
> bool is_aws_cost_explorer_enabled_using_get()

isAwsCostExplorerEnabled

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
api_instance = swagger_client.UiCloudCostExplorerControllerApi(swagger_client.ApiClient(configuration))

try:
    # isAwsCostExplorerEnabled
    api_response = api_instance.is_aws_cost_explorer_enabled_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCloudCostExplorerControllerApi->is_aws_cost_explorer_enabled_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_cloud_cost_using_get**
> sync_cloud_cost_using_get()

syncCloudCost

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
api_instance = swagger_client.UiCloudCostExplorerControllerApi(swagger_client.ApiClient(configuration))

try:
    # syncCloudCost
    api_instance.sync_cloud_cost_using_get()
except ApiException as e:
    print("Exception when calling UiCloudCostExplorerControllerApi->sync_cloud_cost_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

