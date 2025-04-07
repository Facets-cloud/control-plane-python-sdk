# swagger_client.UiOAuthControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_generic_o_auth_integration_using_post**](UiOAuthControllerApi.md#add_generic_o_auth_integration_using_post) | **POST** /cc-ui/v1/oauth/generic-oauth-integration | addGenericOAuthIntegration
[**add_integrations_using_post**](UiOAuthControllerApi.md#add_integrations_using_post) | **POST** /cc-ui/v1/oauth | addIntegrations
[**delete_integrations_using_delete**](UiOAuthControllerApi.md#delete_integrations_using_delete) | **DELETE** /cc-ui/v1/oauth/{registrationId} | deleteIntegrations
[**edit_generic_o_auth_integration_using_put**](UiOAuthControllerApi.md#edit_generic_o_auth_integration_using_put) | **PUT** /cc-ui/v1/oauth/generic-oauth-integration | editGenericOAuthIntegration
[**get_all_integrations_using_get**](UiOAuthControllerApi.md#get_all_integrations_using_get) | **GET** /cc-ui/v1/oauth | getAllIntegrations
[**update_integrations_using_put**](UiOAuthControllerApi.md#update_integrations_using_put) | **PUT** /cc-ui/v1/oauth/{registrationId} | updateIntegrations


# **add_generic_o_auth_integration_using_post**
> list[CustomOAuth2ClientRegistration] add_generic_o_auth_integration_using_post(client)

addGenericOAuthIntegration

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
api_instance = swagger_client.UiOAuthControllerApi(swagger_client.ApiClient(configuration))
client = swagger_client.GenericOAuth2ClientRegistration() # GenericOAuth2ClientRegistration | client

try:
    # addGenericOAuthIntegration
    api_response = api_instance.add_generic_o_auth_integration_using_post(client)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOAuthControllerApi->add_generic_o_auth_integration_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | [**GenericOAuth2ClientRegistration**](GenericOAuth2ClientRegistration.md)| client | 

### Return type

[**list[CustomOAuth2ClientRegistration]**](CustomOAuth2ClientRegistration.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_integrations_using_post**
> list[CustomOAuth2ClientRegistration] add_integrations_using_post(client)

addIntegrations

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
api_instance = swagger_client.UiOAuthControllerApi(swagger_client.ApiClient(configuration))
client = swagger_client.CustomOAuth2ClientRegistration() # CustomOAuth2ClientRegistration | client

try:
    # addIntegrations
    api_response = api_instance.add_integrations_using_post(client)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOAuthControllerApi->add_integrations_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | [**CustomOAuth2ClientRegistration**](CustomOAuth2ClientRegistration.md)| client | 

### Return type

[**list[CustomOAuth2ClientRegistration]**](CustomOAuth2ClientRegistration.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_integrations_using_delete**
> list[CustomOAuth2ClientRegistration] delete_integrations_using_delete(registration_id)

deleteIntegrations

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
api_instance = swagger_client.UiOAuthControllerApi(swagger_client.ApiClient(configuration))
registration_id = 'registration_id_example' # str | registrationId

try:
    # deleteIntegrations
    api_response = api_instance.delete_integrations_using_delete(registration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOAuthControllerApi->delete_integrations_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| registrationId | 

### Return type

[**list[CustomOAuth2ClientRegistration]**](CustomOAuth2ClientRegistration.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_generic_o_auth_integration_using_put**
> list[CustomOAuth2ClientRegistration] edit_generic_o_auth_integration_using_put(client, registration_id=registration_id)

editGenericOAuthIntegration

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
api_instance = swagger_client.UiOAuthControllerApi(swagger_client.ApiClient(configuration))
client = swagger_client.GenericOAuth2ClientRegistration() # GenericOAuth2ClientRegistration | client
registration_id = 'registration_id_example' # str | registrationId (optional)

try:
    # editGenericOAuthIntegration
    api_response = api_instance.edit_generic_o_auth_integration_using_put(client, registration_id=registration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOAuthControllerApi->edit_generic_o_auth_integration_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | [**GenericOAuth2ClientRegistration**](GenericOAuth2ClientRegistration.md)| client | 
 **registration_id** | **str**| registrationId | [optional] 

### Return type

[**list[CustomOAuth2ClientRegistration]**](CustomOAuth2ClientRegistration.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_integrations_using_get**
> list[CustomOAuth2ClientRegistration] get_all_integrations_using_get()

getAllIntegrations

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
api_instance = swagger_client.UiOAuthControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllIntegrations
    api_response = api_instance.get_all_integrations_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOAuthControllerApi->get_all_integrations_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustomOAuth2ClientRegistration]**](CustomOAuth2ClientRegistration.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_integrations_using_put**
> list[CustomOAuth2ClientRegistration] update_integrations_using_put(client, registration_id)

updateIntegrations

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
api_instance = swagger_client.UiOAuthControllerApi(swagger_client.ApiClient(configuration))
client = swagger_client.CustomOAuth2ClientRegistration() # CustomOAuth2ClientRegistration | client
registration_id = 'registration_id_example' # str | registrationId

try:
    # updateIntegrations
    api_response = api_instance.update_integrations_using_put(client, registration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOAuthControllerApi->update_integrations_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | [**CustomOAuth2ClientRegistration**](CustomOAuth2ClientRegistration.md)| client | 
 **registration_id** | **str**| registrationId | 

### Return type

[**list[CustomOAuth2ClientRegistration]**](CustomOAuth2ClientRegistration.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

