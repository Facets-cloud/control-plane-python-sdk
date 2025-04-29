# swagger_client.UiSettingsControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_setting_value_using_put**](UiSettingsControllerApi.md#add_setting_value_using_put) | **PUT** /cc-ui/v1/settings/value/{entityType}/{entityId} | addSettingValue
[**get_all_settings_for_entity_using_get**](UiSettingsControllerApi.md#get_all_settings_for_entity_using_get) | **GET** /cc-ui/v1/settings/entity/{entity} | getAllSettingsForEntity
[**get_all_settings_yaml_using_get**](UiSettingsControllerApi.md#get_all_settings_yaml_using_get) | **GET** /cc-ui/v1/settings/ui-yaml | getAllSettingsYaml
[**get_setting_value_using_get**](UiSettingsControllerApi.md#get_setting_value_using_get) | **GET** /cc-ui/v1/settings/value/{entityType}/{entityId} | getSettingValue
[**set_onboarding_display_using_put**](UiSettingsControllerApi.md#set_onboarding_display_using_put) | **PUT** /cc-ui/v1/settings/onboarding-display/{value} | setOnboardingDisplay

# **add_setting_value_using_put**
> object add_setting_value_using_put(body, entity_id, entity_type)

addSettingValue

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
api_instance = swagger_client.UiSettingsControllerApi(swagger_client.ApiClient(configuration))
body = NULL # object | settingValueRequest
entity_id = 'entity_id_example' # str | entityId
entity_type = 'entity_type_example' # str | entityType

try:
    # addSettingValue
    api_response = api_instance.add_setting_value_using_put(body, entity_id, entity_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiSettingsControllerApi->add_setting_value_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| settingValueRequest | 
 **entity_id** | **str**| entityId | 
 **entity_type** | **str**| entityType | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_settings_for_entity_using_get**
> list[Setting] get_all_settings_for_entity_using_get(entity)

getAllSettingsForEntity

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
api_instance = swagger_client.UiSettingsControllerApi(swagger_client.ApiClient(configuration))
entity = 'entity_example' # str | entity

try:
    # getAllSettingsForEntity
    api_response = api_instance.get_all_settings_for_entity_using_get(entity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiSettingsControllerApi->get_all_settings_for_entity_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**| entity | 

### Return type

[**list[Setting]**](Setting.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_settings_yaml_using_get**
> JsonNode get_all_settings_yaml_using_get()

getAllSettingsYaml

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
api_instance = swagger_client.UiSettingsControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllSettingsYaml
    api_response = api_instance.get_all_settings_yaml_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiSettingsControllerApi->get_all_settings_yaml_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonNode**](JsonNode.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_setting_value_using_get**
> object get_setting_value_using_get(entity_id, entity_type)

getSettingValue

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
api_instance = swagger_client.UiSettingsControllerApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | entityId
entity_type = 'entity_type_example' # str | entityType

try:
    # getSettingValue
    api_response = api_instance.get_setting_value_using_get(entity_id, entity_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiSettingsControllerApi->get_setting_value_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| entityId | 
 **entity_type** | **str**| entityType | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_onboarding_display_using_put**
> set_onboarding_display_using_put(value)

setOnboardingDisplay

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
api_instance = swagger_client.UiSettingsControllerApi(swagger_client.ApiClient(configuration))
value = true # bool | value

try:
    # setOnboardingDisplay
    api_instance.set_onboarding_display_using_put(value)
except ApiException as e:
    print("Exception when calling UiSettingsControllerApi->set_onboarding_display_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **bool**| value | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

