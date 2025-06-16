# swagger_client.UiSettingsControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_setting_value**](UiSettingsControllerApi.md#add_setting_value) | **PUT** /cc-ui/v1/settings/value/{entityType}/{entityId} | 
[**get_all_settings_for_entity**](UiSettingsControllerApi.md#get_all_settings_for_entity) | **GET** /cc-ui/v1/settings/entity/{entity} | 
[**get_all_settings_yaml**](UiSettingsControllerApi.md#get_all_settings_yaml) | **GET** /cc-ui/v1/settings/ui-yaml | 
[**get_setting_value**](UiSettingsControllerApi.md#get_setting_value) | **GET** /cc-ui/v1/settings/value/{entityType}/{entityId} | 
[**set_onboarding_display**](UiSettingsControllerApi.md#set_onboarding_display) | **PUT** /cc-ui/v1/settings/onboarding-display/{value} | 

# **add_setting_value**
> dict(str, object) add_setting_value(body, entity_id, entity_type)



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
api_instance = swagger_client.UiSettingsControllerApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, object) | 
entity_id = 'entity_id_example' # str | 
entity_type = 'entity_type_example' # str | 

try:
    api_response = api_instance.add_setting_value(body, entity_id, entity_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiSettingsControllerApi->add_setting_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)|  | 
 **entity_id** | **str**|  | 
 **entity_type** | **str**|  | 

### Return type

**dict(str, object)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_settings_for_entity**
> list[ComCapillaryOpsCpBoSetting] get_all_settings_for_entity(entity)



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
api_instance = swagger_client.UiSettingsControllerApi(swagger_client.ApiClient(configuration))
entity = 'entity_example' # str | 

try:
    api_response = api_instance.get_all_settings_for_entity(entity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiSettingsControllerApi->get_all_settings_for_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoSetting]**](ComCapillaryOpsCpBoSetting.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_settings_yaml**
> ComFasterxmlJacksonDatabindJsonNode get_all_settings_yaml()



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
api_instance = swagger_client.UiSettingsControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_settings_yaml()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiSettingsControllerApi->get_all_settings_yaml: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ComFasterxmlJacksonDatabindJsonNode**](ComFasterxmlJacksonDatabindJsonNode.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_setting_value**
> dict(str, object) get_setting_value(entity_type, entity_id)



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
api_instance = swagger_client.UiSettingsControllerApi(swagger_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | 
entity_id = 'entity_id_example' # str | 

try:
    api_response = api_instance.get_setting_value(entity_type, entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiSettingsControllerApi->get_setting_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  | 
 **entity_id** | **str**|  | 

### Return type

**dict(str, object)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_onboarding_display**
> set_onboarding_display(value)



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
api_instance = swagger_client.UiSettingsControllerApi(swagger_client.ApiClient(configuration))
value = true # bool | 

try:
    api_instance.set_onboarding_display(value)
except ApiException as e:
    print("Exception when calling UiSettingsControllerApi->set_onboarding_display: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

