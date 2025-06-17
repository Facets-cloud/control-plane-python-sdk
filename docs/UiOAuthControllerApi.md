# swagger_client.UiOAuthControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_generic_o_auth_integration**](UiOAuthControllerApi.md#add_generic_o_auth_integration) | **POST** /cc-ui/v1/oauth/generic-oauth-integration | 
[**add_integrations**](UiOAuthControllerApi.md#add_integrations) | **POST** /cc-ui/v1/oauth | 
[**delete_integrations**](UiOAuthControllerApi.md#delete_integrations) | **DELETE** /cc-ui/v1/oauth/{registrationId} | 
[**edit_generic_o_auth_integration**](UiOAuthControllerApi.md#edit_generic_o_auth_integration) | **PUT** /cc-ui/v1/oauth/generic-oauth-integration | 
[**get_all_integrations**](UiOAuthControllerApi.md#get_all_integrations) | **GET** /cc-ui/v1/oauth | 
[**update_integrations**](UiOAuthControllerApi.md#update_integrations) | **PUT** /cc-ui/v1/oauth/{registrationId} | 

# **add_generic_o_auth_integration**
> list[CustomOAuth2ClientRegistration] add_generic_o_auth_integration(body)



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
api_instance = swagger_client.UiOAuthControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.GenericOAuth2ClientRegistration() # GenericOAuth2ClientRegistration | 

try:
    api_response = api_instance.add_generic_o_auth_integration(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOAuthControllerApi->add_generic_o_auth_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenericOAuth2ClientRegistration**](GenericOAuth2ClientRegistration.md)|  | 

### Return type

[**list[CustomOAuth2ClientRegistration]**](CustomOAuth2ClientRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_integrations**
> list[CustomOAuth2ClientRegistration] add_integrations(body)



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
api_instance = swagger_client.UiOAuthControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomOAuth2ClientRegistration() # CustomOAuth2ClientRegistration | 

try:
    api_response = api_instance.add_integrations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOAuthControllerApi->add_integrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomOAuth2ClientRegistration**](CustomOAuth2ClientRegistration.md)|  | 

### Return type

[**list[CustomOAuth2ClientRegistration]**](CustomOAuth2ClientRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_integrations**
> list[CustomOAuth2ClientRegistration] delete_integrations(registration_id)



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
api_instance = swagger_client.UiOAuthControllerApi(swagger_client.ApiClient(configuration))
registration_id = 'registration_id_example' # str | 

try:
    api_response = api_instance.delete_integrations(registration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOAuthControllerApi->delete_integrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**|  | 

### Return type

[**list[CustomOAuth2ClientRegistration]**](CustomOAuth2ClientRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_generic_o_auth_integration**
> list[CustomOAuth2ClientRegistration] edit_generic_o_auth_integration(body, registration_id)



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
api_instance = swagger_client.UiOAuthControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.GenericOAuth2ClientRegistration() # GenericOAuth2ClientRegistration | 
registration_id = 'registration_id_example' # str | 

try:
    api_response = api_instance.edit_generic_o_auth_integration(body, registration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOAuthControllerApi->edit_generic_o_auth_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenericOAuth2ClientRegistration**](GenericOAuth2ClientRegistration.md)|  | 
 **registration_id** | **str**|  | 

### Return type

[**list[CustomOAuth2ClientRegistration]**](CustomOAuth2ClientRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_integrations**
> list[CustomOAuth2ClientRegistration] get_all_integrations()



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
api_instance = swagger_client.UiOAuthControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_integrations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOAuthControllerApi->get_all_integrations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustomOAuth2ClientRegistration]**](CustomOAuth2ClientRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integrations**
> list[CustomOAuth2ClientRegistration] update_integrations(body, registration_id)



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
api_instance = swagger_client.UiOAuthControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomOAuth2ClientRegistration() # CustomOAuth2ClientRegistration | 
registration_id = 'registration_id_example' # str | 

try:
    api_response = api_instance.update_integrations(body, registration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOAuthControllerApi->update_integrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomOAuth2ClientRegistration**](CustomOAuth2ClientRegistration.md)|  | 
 **registration_id** | **str**|  | 

### Return type

[**list[CustomOAuth2ClientRegistration]**](CustomOAuth2ClientRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

