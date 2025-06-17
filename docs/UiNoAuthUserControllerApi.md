# swagger_client.UiNoAuthUserControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_password_request**](UiNoAuthUserControllerApi.md#reset_password_request) | **POST** /public-ui/v1/user/resetPassword | 
[**save_password**](UiNoAuthUserControllerApi.md#save_password) | **POST** /public-ui/v1/user/savePassword | 
[**validate_token**](UiNoAuthUserControllerApi.md#validate_token) | **POST** /public-ui/v1/user/token/validate | 

# **reset_password_request**
> Response reset_password_request(body)



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
api_instance = swagger_client.UiNoAuthUserControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResetPasswordRequest() # ResetPasswordRequest | 

try:
    api_response = api_instance.reset_password_request(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNoAuthUserControllerApi->reset_password_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetPasswordRequest**](ResetPasswordRequest.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_password**
> Response save_password(body)



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
api_instance = swagger_client.UiNoAuthUserControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.SavePasswordResetPasswordRequest() # SavePasswordResetPasswordRequest | 

try:
    api_response = api_instance.save_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNoAuthUserControllerApi->save_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SavePasswordResetPasswordRequest**](SavePasswordResetPasswordRequest.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_token**
> TokenValidity validate_token(body)



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
api_instance = swagger_client.UiNoAuthUserControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.TokenValidationRequest() # TokenValidationRequest | 

try:
    api_response = api_instance.validate_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNoAuthUserControllerApi->validate_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenValidationRequest**](TokenValidationRequest.md)|  | 

### Return type

[**TokenValidity**](TokenValidity.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

