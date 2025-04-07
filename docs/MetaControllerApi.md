# swagger_client.MetaControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_supported_component_version_using_get**](MetaControllerApi.md#get_supported_component_version_using_get) | **GET** /cc/v1/meta/components/{componentType}/supportedVersion | getSupportedComponentVersion
[**get_supported_component_versions_using_get**](MetaControllerApi.md#get_supported_component_versions_using_get) | **GET** /cc/v1/meta/components/supportedVersion | getSupportedComponentVersions


# **get_supported_component_version_using_get**
> SupportedVersions get_supported_component_version_using_get(component_type)

getSupportedComponentVersion

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
api_instance = swagger_client.MetaControllerApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | componentType

try:
    # getSupportedComponentVersion
    api_response = api_instance.get_supported_component_version_using_get(component_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetaControllerApi->get_supported_component_version_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**| componentType | 

### Return type

[**SupportedVersions**](SupportedVersions.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_component_versions_using_get**
> list[SupportedVersions] get_supported_component_versions_using_get()

getSupportedComponentVersions

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
api_instance = swagger_client.MetaControllerApi(swagger_client.ApiClient(configuration))

try:
    # getSupportedComponentVersions
    api_response = api_instance.get_supported_component_versions_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetaControllerApi->get_supported_component_versions_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SupportedVersions]**](SupportedVersions.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

