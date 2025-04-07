# swagger_client.UiArtifactHubControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_helm_values_using_get**](UiArtifactHubControllerApi.md#get_helm_values_using_get) | **GET** /cc-ui/v1/artifactHub/packages/{packageId}/values | getHelmValues
[**search_packages_using_get**](UiArtifactHubControllerApi.md#search_packages_using_get) | **GET** /cc-ui/v1/artifactHub/search-packages | searchPackages


# **get_helm_values_using_get**
> object get_helm_values_using_get(package_id, version)

getHelmValues

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
api_instance = swagger_client.UiArtifactHubControllerApi(swagger_client.ApiClient(configuration))
package_id = 'package_id_example' # str | packageId
version = 'version_example' # str | version

try:
    # getHelmValues
    api_response = api_instance.get_helm_values_using_get(package_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactHubControllerApi->get_helm_values_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**| packageId | 
 **version** | **str**| version | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_packages_using_get**
> PackageResponse search_packages_using_get(category=category, facets=facets, limit=limit, offset=offset, sort=sort, ts_query_web=ts_query_web, verified=verified)

searchPackages

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
api_instance = swagger_client.UiArtifactHubControllerApi(swagger_client.ApiClient(configuration))
category = 56 # int | category (optional)
facets = false # bool | facets (optional) (default to false)
limit = 20 # int | limit (optional) (default to 20)
offset = 0 # int | offset (optional) (default to 0)
sort = 'sort_example' # str | sort (optional)
ts_query_web = 'ts_query_web_example' # str | tsQueryWeb (optional)
verified = true # bool | verified (optional)

try:
    # searchPackages
    api_response = api_instance.search_packages_using_get(category=category, facets=facets, limit=limit, offset=offset, sort=sort, ts_query_web=ts_query_web, verified=verified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactHubControllerApi->search_packages_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **int**| category | [optional] 
 **facets** | **bool**| facets | [optional] [default to false]
 **limit** | **int**| limit | [optional] [default to 20]
 **offset** | **int**| offset | [optional] [default to 0]
 **sort** | **str**| sort | [optional] 
 **ts_query_web** | **str**| tsQueryWeb | [optional] 
 **verified** | **bool**| verified | [optional] 

### Return type

[**PackageResponse**](PackageResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

