# swagger_client.UiAlertsControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all_using_delete**](UiAlertsControllerApi.md#delete_all_using_delete) | **DELETE** /cc-ui/v1/alerts | deleteAll
[**get_alerts_count_using_get**](UiAlertsControllerApi.md#get_alerts_count_using_get) | **GET** /cc-ui/v1/alerts/firing/count | getAlertsCount
[**get_alerts_overview_using_get**](UiAlertsControllerApi.md#get_alerts_overview_using_get) | **GET** /cc-ui/v1/alerts/firing/overview | getAlertsOverview
[**get_cluster_alerts_using_get**](UiAlertsControllerApi.md#get_cluster_alerts_using_get) | **GET** /cc-ui/v1/alerts/{clusterId}/all | getClusterAlerts
[**get_firing_alerts_using_get**](UiAlertsControllerApi.md#get_firing_alerts_using_get) | **GET** /cc-ui/v1/alerts/firing | getFiringAlerts


# **delete_all_using_delete**
> delete_all_using_delete()

deleteAll

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
api_instance = swagger_client.UiAlertsControllerApi(swagger_client.ApiClient(configuration))

try:
    # deleteAll
    api_instance.delete_all_using_delete()
except ApiException as e:
    print("Exception when calling UiAlertsControllerApi->delete_all_using_delete: %s\n" % e)
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

# **get_alerts_count_using_get**
> dict(str, int) get_alerts_count_using_get()

getAlertsCount

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
api_instance = swagger_client.UiAlertsControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAlertsCount
    api_response = api_instance.get_alerts_count_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAlertsControllerApi->get_alerts_count_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, int)**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts_overview_using_get**
> list[AlertOverview] get_alerts_overview_using_get()

getAlertsOverview

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
api_instance = swagger_client.UiAlertsControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAlertsOverview
    api_response = api_instance.get_alerts_overview_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAlertsControllerApi->get_alerts_overview_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AlertOverview]**](AlertOverview.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_alerts_using_get**
> ClusterFiringAlertsDTO get_cluster_alerts_using_get(cluster_id)

getClusterAlerts

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
api_instance = swagger_client.UiAlertsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getClusterAlerts
    api_response = api_instance.get_cluster_alerts_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAlertsControllerApi->get_cluster_alerts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**ClusterFiringAlertsDTO**](ClusterFiringAlertsDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firing_alerts_using_get**
> list[AlertGroup] get_firing_alerts_using_get()

getFiringAlerts

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
api_instance = swagger_client.UiAlertsControllerApi(swagger_client.ApiClient(configuration))

try:
    # getFiringAlerts
    api_response = api_instance.get_firing_alerts_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAlertsControllerApi->get_firing_alerts_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AlertGroup]**](AlertGroup.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

