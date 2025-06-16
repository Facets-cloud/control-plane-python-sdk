# swagger_client.UiAlertsControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all**](UiAlertsControllerApi.md#delete_all) | **DELETE** /cc-ui/v1/alerts | 
[**get_alerts_count**](UiAlertsControllerApi.md#get_alerts_count) | **GET** /cc-ui/v1/alerts/firing/count | 
[**get_alerts_overview**](UiAlertsControllerApi.md#get_alerts_overview) | **GET** /cc-ui/v1/alerts/firing/overview | 
[**get_cluster_alerts**](UiAlertsControllerApi.md#get_cluster_alerts) | **GET** /cc-ui/v1/alerts/{clusterId}/all | 
[**get_firing_alerts**](UiAlertsControllerApi.md#get_firing_alerts) | **GET** /cc-ui/v1/alerts/firing | 

# **delete_all**
> delete_all()



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
api_instance = swagger_client.UiAlertsControllerApi(swagger_client.ApiClient(configuration))

try:
    api_instance.delete_all()
except ApiException as e:
    print("Exception when calling UiAlertsControllerApi->delete_all: %s\n" % e)
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

# **get_alerts_count**
> dict(str, int) get_alerts_count()



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
api_instance = swagger_client.UiAlertsControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_alerts_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAlertsControllerApi->get_alerts_count: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, int)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts_overview**
> list[ComCapillaryOpsCpBoAlertsAlertOverview] get_alerts_overview()



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
api_instance = swagger_client.UiAlertsControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_alerts_overview()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAlertsControllerApi->get_alerts_overview: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoAlertsAlertOverview]**](ComCapillaryOpsCpBoAlertsAlertOverview.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_alerts**
> ComCapillaryOpsCpBoAlertsClusterFiringAlertsDTO get_cluster_alerts(cluster_id)



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
api_instance = swagger_client.UiAlertsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_cluster_alerts(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAlertsControllerApi->get_cluster_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAlertsClusterFiringAlertsDTO**](ComCapillaryOpsCpBoAlertsClusterFiringAlertsDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firing_alerts**
> list[ComCapillaryOpsCpBoAlertsAlertGroup] get_firing_alerts()



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
api_instance = swagger_client.UiAlertsControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_firing_alerts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAlertsControllerApi->get_firing_alerts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoAlertsAlertGroup]**](ComCapillaryOpsCpBoAlertsAlertGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

