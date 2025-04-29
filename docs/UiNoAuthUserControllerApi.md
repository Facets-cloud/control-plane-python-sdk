# swagger_client.UiNoAuthUserControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_password_request_using_post**](UiNoAuthUserControllerApi.md#reset_password_request_using_post) | **POST** /public-ui/v1/user/resetPassword | resetPasswordRequest
[**save_password_using_post**](UiNoAuthUserControllerApi.md#save_password_using_post) | **POST** /public-ui/v1/user/savePassword | savePassword
[**validate_token_using_post**](UiNoAuthUserControllerApi.md#validate_token_using_post) | **POST** /public-ui/v1/user/token/validate | validateToken

# **reset_password_request_using_post**
> Response reset_password_request_using_post(body)

resetPasswordRequest

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
api_instance = swagger_client.UiNoAuthUserControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResetPasswordRequest() # ResetPasswordRequest | resetPasswordRequest

try:
    # resetPasswordRequest
    api_response = api_instance.reset_password_request_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNoAuthUserControllerApi->reset_password_request_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetPasswordRequest**](ResetPasswordRequest.md)| resetPasswordRequest | 

### Return type

[**Response**](Response.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_password_using_post**
> Response save_password_using_post(body)

savePassword

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
api_instance = swagger_client.UiNoAuthUserControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.SavePasswordResetPasswordRequest() # SavePasswordResetPasswordRequest | savePasswordResetPasswordRequest

try:
    # savePassword
    api_response = api_instance.save_password_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNoAuthUserControllerApi->save_password_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SavePasswordResetPasswordRequest**](SavePasswordResetPasswordRequest.md)| savePasswordResetPasswordRequest | 

### Return type

[**Response**](Response.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_token_using_post**
> TokenValidity validate_token_using_post(body)

validateToken

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
api_instance = swagger_client.UiNoAuthUserControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.TokenValidationRequest() # TokenValidationRequest | validationRequest

try:
    # validateToken
    api_response = api_instance.validate_token_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNoAuthUserControllerApi->validate_token_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenValidationRequest**](TokenValidationRequest.md)| validationRequest | 

### Return type

[**TokenValidity**](TokenValidity.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

