# swagger_client.UiResourceStatusControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_namespaces_in_use_by_dependent_clusters**](UiResourceStatusControllerApi.md#get_namespaces_in_use_by_dependent_clusters) | **GET** /cc-ui/v1/resources/{baseClusterId}/base-env-in-use-namespaces | 
[**get_release_preview**](UiResourceStatusControllerApi.md#get_release_preview) | **GET** /cc-ui/v1/resources/{clusterId}/release-preview | 
[**get_resource_status**](UiResourceStatusControllerApi.md#get_resource_status) | **GET** /cc-ui/v1/resources/{projectName}/{environmentName}/status | 
[**sync_resource**](UiResourceStatusControllerApi.md#sync_resource) | **POST** /cc-ui/v1/resources/sync | 

# **get_namespaces_in_use_by_dependent_clusters**
> dict(str, str) get_namespaces_in_use_by_dependent_clusters(base_cluster_id)



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
api_instance = swagger_client.UiResourceStatusControllerApi(swagger_client.ApiClient(configuration))
base_cluster_id = 'base_cluster_id_example' # str | 

try:
    api_response = api_instance.get_namespaces_in_use_by_dependent_clusters(base_cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceStatusControllerApi->get_namespaces_in_use_by_dependent_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_cluster_id** | **str**|  | 

### Return type

**dict(str, str)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_preview**
> ReleasePreviewResponse get_release_preview(cluster_id)



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
api_instance = swagger_client.UiResourceStatusControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_release_preview(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceStatusControllerApi->get_release_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ReleasePreviewResponse**](ReleasePreviewResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_status**
> ResourceStatusResponse get_resource_status(project_name, environment_name, resources)



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
api_instance = swagger_client.UiResourceStatusControllerApi(swagger_client.ApiClient(configuration))
project_name = 'project_name_example' # str | 
environment_name = 'environment_name_example' # str | 
resources = {'key': 'resources_example'} # dict(str, str) | 

try:
    api_response = api_instance.get_resource_status(project_name, environment_name, resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceStatusControllerApi->get_resource_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **environment_name** | **str**|  | 
 **resources** | [**dict(str, str)**](str.md)|  | 

### Return type

[**ResourceStatusResponse**](ResourceStatusResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_resource**
> ResourceStatusResponse sync_resource(body)



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
api_instance = swagger_client.UiResourceStatusControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResourceSyncRequest() # ResourceSyncRequest | 

try:
    api_response = api_instance.sync_resource(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceStatusControllerApi->sync_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceSyncRequest**](ResourceSyncRequest.md)|  | 

### Return type

[**ResourceStatusResponse**](ResourceStatusResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

