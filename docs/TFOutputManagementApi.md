# swagger_client.TFOutputManagementApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_output**](TFOutputManagementApi.md#create_or_update_output) | **POST** /cc-ui/v1/tf-outputs | 
[**delete_output**](TFOutputManagementApi.md#delete_output) | **DELETE** /cc-ui/v1/tf-outputs/{name} | 
[**get_all_outputs**](TFOutputManagementApi.md#get_all_outputs) | **GET** /cc-ui/v1/tf-outputs | 
[**get_output_by_name**](TFOutputManagementApi.md#get_output_by_name) | **GET** /cc-ui/v1/tf-outputs/{name} | 
[**get_outputs_by_provider_source**](TFOutputManagementApi.md#get_outputs_by_provider_source) | **GET** /cc-ui/v1/tf-outputs/provider | Get all outputs that use a specific provider source

# **create_or_update_output**
> ComCapillaryOpsCpV2RegistryOutputTFOutputResponseDTO create_or_update_output(body)



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
api_instance = swagger_client.TFOutputManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpV2RegistryOutputTFOutputRequestDTO() # ComCapillaryOpsCpV2RegistryOutputTFOutputRequestDTO | 

try:
    api_response = api_instance.create_or_update_output(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TFOutputManagementApi->create_or_update_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpV2RegistryOutputTFOutputRequestDTO**](ComCapillaryOpsCpV2RegistryOutputTFOutputRequestDTO.md)|  | 

### Return type

[**ComCapillaryOpsCpV2RegistryOutputTFOutputResponseDTO**](ComCapillaryOpsCpV2RegistryOutputTFOutputResponseDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_output**
> delete_output(name, namespace)



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
api_instance = swagger_client.TFOutputManagementApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
namespace = 'namespace_example' # str | 

try:
    api_instance.delete_output(name, namespace)
except ApiException as e:
    print("Exception when calling TFOutputManagementApi->delete_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **namespace** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_outputs**
> list[ComCapillaryOpsCpV2RegistryOutputTFOutputResponseDTO] get_all_outputs()



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
api_instance = swagger_client.TFOutputManagementApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_outputs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TFOutputManagementApi->get_all_outputs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpV2RegistryOutputTFOutputResponseDTO]**](ComCapillaryOpsCpV2RegistryOutputTFOutputResponseDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_output_by_name**
> ComCapillaryOpsCpV2RegistryOutputTFOutputResponseDTO get_output_by_name(name, namespace)



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
api_instance = swagger_client.TFOutputManagementApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
namespace = 'namespace_example' # str | 

try:
    api_response = api_instance.get_output_by_name(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TFOutputManagementApi->get_output_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **namespace** | **str**|  | 

### Return type

[**ComCapillaryOpsCpV2RegistryOutputTFOutputResponseDTO**](ComCapillaryOpsCpV2RegistryOutputTFOutputResponseDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outputs_by_provider_source**
> list[ComCapillaryOpsCpV2RegistryOutputTFOutputResponseDTO] get_outputs_by_provider_source(source)

Get all outputs that use a specific provider source

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
api_instance = swagger_client.TFOutputManagementApi(swagger_client.ApiClient(configuration))
source = 'source_example' # str | Provider source name

try:
    # Get all outputs that use a specific provider source
    api_response = api_instance.get_outputs_by_provider_source(source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TFOutputManagementApi->get_outputs_by_provider_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Provider source name | 

### Return type

[**list[ComCapillaryOpsCpV2RegistryOutputTFOutputResponseDTO]**](ComCapillaryOpsCpV2RegistryOutputTFOutputResponseDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

