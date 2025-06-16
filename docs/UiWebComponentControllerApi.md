# swagger_client.UiWebComponentControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_component**](UiWebComponentControllerApi.md#create_component) | **POST** /cc-ui/v1/web-components | 
[**delete_component**](UiWebComponentControllerApi.md#delete_component) | **DELETE** /cc-ui/v1/web-components/{webComponentId} | 
[**get_all_components**](UiWebComponentControllerApi.md#get_all_components) | **GET** /cc-ui/v1/web-components | 
[**get_component**](UiWebComponentControllerApi.md#get_component) | **GET** /cc-ui/v1/web-components/{webComponentId} | 
[**update_component**](UiWebComponentControllerApi.md#update_component) | **PUT** /cc-ui/v1/web-components/{webComponentId} | 

# **create_component**
> ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO create_component(body)



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
api_instance = swagger_client.UiWebComponentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO() # ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO | 

try:
    api_response = api_instance.create_component(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiWebComponentControllerApi->create_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO**](ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO.md)|  | 

### Return type

[**ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO**](ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_component**
> delete_component(web_component_id)



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
api_instance = swagger_client.UiWebComponentControllerApi(swagger_client.ApiClient(configuration))
web_component_id = 'web_component_id_example' # str | 

try:
    api_instance.delete_component(web_component_id)
except ApiException as e:
    print("Exception when calling UiWebComponentControllerApi->delete_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_component_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_components**
> list[ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO] get_all_components()



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
api_instance = swagger_client.UiWebComponentControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_components()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiWebComponentControllerApi->get_all_components: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO]**](ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component**
> ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO get_component(web_component_id)



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
api_instance = swagger_client.UiWebComponentControllerApi(swagger_client.ApiClient(configuration))
web_component_id = 'web_component_id_example' # str | 

try:
    api_response = api_instance.get_component(web_component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiWebComponentControllerApi->get_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_component_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO**](ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_component**
> ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO update_component(body, web_component_id)



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
api_instance = swagger_client.UiWebComponentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO() # ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO | 
web_component_id = 'web_component_id_example' # str | 

try:
    api_response = api_instance.update_component(body, web_component_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiWebComponentControllerApi->update_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO**](ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO.md)|  | 
 **web_component_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO**](ComCapillaryOpsCpV2WebcomponentBoWebComponentDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

