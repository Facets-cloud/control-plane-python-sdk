# swagger_client.UiUserVcsTokenControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_using_post1**](UiUserVcsTokenControllerApi.md#add_using_post1) | **POST** /cc-ui/v1/user-token | add
[**delete_using_delete2**](UiUserVcsTokenControllerApi.md#delete_using_delete2) | **DELETE** /cc-ui/v1/user-token/{id} | delete
[**get_all_using_get5**](UiUserVcsTokenControllerApi.md#get_all_using_get5) | **GET** /cc-ui/v1/user-token | getAll
[**update_using_put2**](UiUserVcsTokenControllerApi.md#update_using_put2) | **PUT** /cc-ui/v1/user-token | update


# **add_using_post1**
> UserVCSTokenResponse add_using_post1(user_vcs_token_request)

add

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
api_instance = swagger_client.UiUserVcsTokenControllerApi(swagger_client.ApiClient(configuration))
user_vcs_token_request = swagger_client.UserVCSTokenRequest() # UserVCSTokenRequest | userVCSTokenRequest

try:
    # add
    api_response = api_instance.add_using_post1(user_vcs_token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserVcsTokenControllerApi->add_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_vcs_token_request** | [**UserVCSTokenRequest**](UserVCSTokenRequest.md)| userVCSTokenRequest | 

### Return type

[**UserVCSTokenResponse**](UserVCSTokenResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete2**
> delete_using_delete2(id)

delete

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
api_instance = swagger_client.UiUserVcsTokenControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # delete
    api_instance.delete_using_delete2(id)
except ApiException as e:
    print("Exception when calling UiUserVcsTokenControllerApi->delete_using_delete2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_using_get5**
> list[UserVCSTokenResponse] get_all_using_get5()

getAll

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
api_instance = swagger_client.UiUserVcsTokenControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAll
    api_response = api_instance.get_all_using_get5()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserVcsTokenControllerApi->get_all_using_get5: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserVCSTokenResponse]**](UserVCSTokenResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put2**
> UserVCSTokenResponse update_using_put2(user_vcs_token_request)

update

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
api_instance = swagger_client.UiUserVcsTokenControllerApi(swagger_client.ApiClient(configuration))
user_vcs_token_request = swagger_client.UserVCSTokenRequest() # UserVCSTokenRequest | userVCSTokenRequest

try:
    # update
    api_response = api_instance.update_using_put2(user_vcs_token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserVcsTokenControllerApi->update_using_put2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_vcs_token_request** | [**UserVCSTokenRequest**](UserVCSTokenRequest.md)| userVCSTokenRequest | 

### Return type

[**UserVCSTokenResponse**](UserVCSTokenResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

