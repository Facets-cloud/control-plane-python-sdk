# swagger_client.UiLocalClusterControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_using_post3**](UiLocalClusterControllerApi.md#create_cluster_using_post3) | **POST** /cc-ui/v1/local/clusters | Create a new Environment for a blueprint
[**get_cluster_using_get3**](UiLocalClusterControllerApi.md#get_cluster_using_get3) | **GET** /cc-ui/v1/local/clusters/{clusterId} | 
[**get_vagrant**](UiLocalClusterControllerApi.md#get_vagrant) | **GET** /cc-ui/v1/local/clusters/{clusterId}/vagrant | 
[**update_cluster_using_put3**](UiLocalClusterControllerApi.md#update_cluster_using_put3) | **PUT** /cc-ui/v1/local/clusters/{clusterId} | 

# **create_cluster_using_post3**
> ComCapillaryOpsCpBoLocalCluster create_cluster_using_post3(body)

Create a new Environment for a blueprint

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
api_instance = swagger_client.UiLocalClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsLocalClusterRequest() # ComCapillaryOpsCpBoRequestsLocalClusterRequest | 

try:
    # Create a new Environment for a blueprint
    api_response = api_instance.create_cluster_using_post3(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiLocalClusterControllerApi->create_cluster_using_post3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsLocalClusterRequest**](ComCapillaryOpsCpBoRequestsLocalClusterRequest.md)|  | 

### Return type

[**ComCapillaryOpsCpBoLocalCluster**](ComCapillaryOpsCpBoLocalCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_using_get3**
> ComCapillaryOpsCpBoLocalCluster get_cluster_using_get3(cluster_id)



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
api_instance = swagger_client.UiLocalClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_cluster_using_get3(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiLocalClusterControllerApi->get_cluster_using_get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoLocalCluster**](ComCapillaryOpsCpBoLocalCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vagrant**
> str get_vagrant(cluster_id)



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
api_instance = swagger_client.UiLocalClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_vagrant(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiLocalClusterControllerApi->get_vagrant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_using_put3**
> ComCapillaryOpsCpBoLocalCluster update_cluster_using_put3(body, cluster_id)



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
api_instance = swagger_client.UiLocalClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsLocalClusterRequest() # ComCapillaryOpsCpBoRequestsLocalClusterRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.update_cluster_using_put3(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiLocalClusterControllerApi->update_cluster_using_put3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsLocalClusterRequest**](ComCapillaryOpsCpBoRequestsLocalClusterRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoLocalCluster**](ComCapillaryOpsCpBoLocalCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

