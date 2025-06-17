# swagger_client.UiMetaControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cp_account**](UiMetaControllerApi.md#get_cp_account) | **GET** /cc-ui/v1/meta/cpAccount | 
[**get_supported_component_version**](UiMetaControllerApi.md#get_supported_component_version) | **GET** /cc-ui/v1/meta/components/{componentType}/supportedVersion | 
[**get_supported_component_versions**](UiMetaControllerApi.md#get_supported_component_versions) | **GET** /cc-ui/v1/meta/components/supportedVersion | 

# **get_cp_account**
> dict(str, str) get_cp_account()



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
api_instance = swagger_client.UiMetaControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_cp_account()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiMetaControllerApi->get_cp_account: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, str)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_component_version**
> SupportedVersions get_supported_component_version(component_type)



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
api_instance = swagger_client.UiMetaControllerApi(swagger_client.ApiClient(configuration))
component_type = 'component_type_example' # str | 

try:
    api_response = api_instance.get_supported_component_version(component_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiMetaControllerApi->get_supported_component_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_type** | **str**|  | 

### Return type

[**SupportedVersions**](SupportedVersions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_component_versions**
> list[SupportedVersions] get_supported_component_versions()



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
api_instance = swagger_client.UiMetaControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_supported_component_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiMetaControllerApi->get_supported_component_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SupportedVersions]**](SupportedVersions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

