# swagger_client.MetaControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_supported_component_version**](MetaControllerApi.md#get_supported_component_version) | **GET** /cc/v1/meta/components/{componentType}/supportedVersion | 
[**get_supported_component_versions**](MetaControllerApi.md#get_supported_component_versions) | **GET** /cc/v1/meta/components/supportedVersion | 

# **get_supported_component_version**
> ComCapillaryOpsCpBoComponentsSupportedVersions get_supported_component_version(component_type)



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
api_instance = swagger_client.MetaControllerApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | 

try:
    api_response = api_instance.get_supported_component_version(component_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetaControllerApi->get_supported_component_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoComponentsSupportedVersions**](ComCapillaryOpsCpBoComponentsSupportedVersions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_component_versions**
> list[ComCapillaryOpsCpBoComponentsSupportedVersions] get_supported_component_versions()



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
api_instance = swagger_client.MetaControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_supported_component_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetaControllerApi->get_supported_component_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoComponentsSupportedVersions]**](ComCapillaryOpsCpBoComponentsSupportedVersions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

