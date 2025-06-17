# swagger_client.UiArtifactHubControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_helm_values**](UiArtifactHubControllerApi.md#get_helm_values) | **GET** /cc-ui/v1/artifactHub/packages/{packageId}/values | 
[**search_packages**](UiArtifactHubControllerApi.md#search_packages) | **GET** /cc-ui/v1/artifactHub/search-packages | 

# **get_helm_values**
> dict(str, object) get_helm_values(package_id, version)



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
api_instance = swagger_client.UiArtifactHubControllerApi(swagger_client.ApiClient(configuration))
package_id = 'package_id_example' # str | 
version = 'version_example' # str | 

try:
    api_response = api_instance.get_helm_values(package_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactHubControllerApi->get_helm_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**|  | 
 **version** | **str**|  | 

### Return type

**dict(str, object)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_packages**
> PackageResponse search_packages(offset=offset, limit=limit, facets=facets, ts_query_web=ts_query_web, category=category, verified=verified, sort=sort)



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
api_instance = swagger_client.UiArtifactHubControllerApi(swagger_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 20 # int |  (optional) (default to 20)
facets = false # bool |  (optional) (default to false)
ts_query_web = 'ts_query_web_example' # str |  (optional)
category = 56 # int |  (optional)
verified = true # bool |  (optional)
sort = 'sort_example' # str |  (optional)

try:
    api_response = api_instance.search_packages(offset=offset, limit=limit, facets=facets, ts_query_web=ts_query_web, category=category, verified=verified, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactHubControllerApi->search_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 20]
 **facets** | **bool**|  | [optional] [default to false]
 **ts_query_web** | **str**|  | [optional] 
 **category** | **int**|  | [optional] 
 **verified** | **bool**|  | [optional] 
 **sort** | **str**|  | [optional] 

### Return type

[**PackageResponse**](PackageResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

