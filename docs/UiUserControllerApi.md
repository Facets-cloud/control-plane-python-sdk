# swagger_client.UiUserControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_access_using_get**](UiUserControllerApi.md#analyze_access_using_get) | **GET** /cc-ui/v1/users/analyze-access | analyzeAccess
[**create_token_using_post**](UiUserControllerApi.md#create_token_using_post) | **POST** /cc-ui/v1/users/createAccessToken | createToken
[**delete_all_logged_in_users_using_delete**](UiUserControllerApi.md#delete_all_logged_in_users_using_delete) | **DELETE** /cc-ui/v1/users/loggedIn/session | deleteALlLoggedInUsers
[**delete_token_using_delete**](UiUserControllerApi.md#delete_token_using_delete) | **DELETE** /cc-ui/v1/users/tokens/{tokenId} | deleteToken
[**delete_user_using_delete**](UiUserControllerApi.md#delete_user_using_delete) | **DELETE** /cc-ui/v1/users/{userId} | deleteUser
[**get_all_logged_in_users_using_get**](UiUserControllerApi.md#get_all_logged_in_users_using_get) | **GET** /cc-ui/v1/users/loggedIn | getALlLoggedInUsers
[**get_all_system_roles_using_get**](UiUserControllerApi.md#get_all_system_roles_using_get) | **GET** /cc-ui/v1/users/roles | getAllSystemRoles
[**get_all_users_expanded_using_get**](UiUserControllerApi.md#get_all_users_expanded_using_get) | **GET** /cc-ui/v1/users/list/users-expanded | getAllUsersExpanded
[**get_all_users_using_get**](UiUserControllerApi.md#get_all_users_using_get) | **GET** /cc-ui/v1/users/ | getAllUsers
[**get_current_user_using_get**](UiUserControllerApi.md#get_current_user_using_get) | **GET** /cc-ui/v1/users/current-user | getCurrentUser
[**get_token_using_get**](UiUserControllerApi.md#get_token_using_get) | **GET** /cc-ui/v1/users/tokens | getToken
[**get_user_expanded_using_get**](UiUserControllerApi.md#get_user_expanded_using_get) | **GET** /cc-ui/v1/users/{userId}/user-expanded | getUserExpanded
[**get_user_using_get**](UiUserControllerApi.md#get_user_using_get) | **GET** /cc-ui/v1/users/{userId} | getUser
[**invite_users_using_post**](UiUserControllerApi.md#invite_users_using_post) | **POST** /cc-ui/v1/users/invite-users | inviteUsers
[**update_password_using_post**](UiUserControllerApi.md#update_password_using_post) | **POST** /cc-ui/v1/users/updatePassword | updatePassword

# **analyze_access_using_get**
> list[AccessAnalyzerResponse] analyze_access_using_get(permissions)

analyzeAccess

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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
permissions = ['permissions_example'] # list[str] | permissions

try:
    # analyzeAccess
    api_response = api_instance.analyze_access_using_get(permissions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->analyze_access_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permissions** | [**list[str]**](str.md)| permissions | 

### Return type

[**list[AccessAnalyzerResponse]**](AccessAnalyzerResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token_using_post**
> list[UserAccessToken] create_token_using_post(created_on=created_on, description=description, name=name, token=token, token_id=token_id, user_name=user_name)

createToken

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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
created_on = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
description = 'description_example' # str |  (optional)
name = 'name_example' # str |  (optional)
token = 'token_example' # str |  (optional)
token_id = 'token_id_example' # str |  (optional)
user_name = 'user_name_example' # str |  (optional)

try:
    # createToken
    api_response = api_instance.create_token_using_post(created_on=created_on, description=description, name=name, token=token, token_id=token_id, user_name=user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->create_token_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_on** | **datetime**|  | [optional] 
 **description** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **token** | **str**|  | [optional] 
 **token_id** | **str**|  | [optional] 
 **user_name** | **str**|  | [optional] 

### Return type

[**list[UserAccessToken]**](UserAccessToken.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_logged_in_users_using_delete**
> bool delete_all_logged_in_users_using_delete()

deleteALlLoggedInUsers

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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))

try:
    # deleteALlLoggedInUsers
    api_response = api_instance.delete_all_logged_in_users_using_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->delete_all_logged_in_users_using_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token_using_delete**
> list[UserAccessToken] delete_token_using_delete(token_id=token_id)

deleteToken

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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
token_id = 'token_id_example' # str | tokenId (optional)

try:
    # deleteToken
    api_response = api_instance.delete_token_using_delete(token_id=token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->delete_token_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| tokenId | [optional] 

### Return type

[**list[UserAccessToken]**](UserAccessToken.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_using_delete**
> bool delete_user_using_delete(user_id)

deleteUser

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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | userId

try:
    # deleteUser
    api_response = api_instance.delete_user_using_delete(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->delete_user_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_logged_in_users_using_get**
> list[object] get_all_logged_in_users_using_get()

getALlLoggedInUsers

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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))

try:
    # getALlLoggedInUsers
    api_response = api_instance.get_all_logged_in_users_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_all_logged_in_users_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_system_roles_using_get**
> list[Role] get_all_system_roles_using_get()

getAllSystemRoles

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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllSystemRoles
    api_response = api_instance.get_all_system_roles_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_all_system_roles_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Role]**](Role.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users_expanded_using_get**
> list[ExpandedUser] get_all_users_expanded_using_get()

getAllUsersExpanded

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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllUsersExpanded
    api_response = api_instance.get_all_users_expanded_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_all_users_expanded_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ExpandedUser]**](ExpandedUser.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users_using_get**
> list[User] get_all_users_using_get()

getAllUsers

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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllUsers
    api_response = api_instance.get_all_users_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_all_users_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[User]**](User.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_using_get**
> User get_current_user_using_get()

getCurrentUser

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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))

try:
    # getCurrentUser
    api_response = api_instance.get_current_user_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_current_user_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_using_get**
> list[UserAccessToken] get_token_using_get()

getToken

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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))

try:
    # getToken
    api_response = api_instance.get_token_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_token_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserAccessToken]**](UserAccessToken.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_expanded_using_get**
> ExpandedUser get_user_expanded_using_get(user_id)

getUserExpanded

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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | userId

try:
    # getUserExpanded
    api_response = api_instance.get_user_expanded_using_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_user_expanded_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId | 

### Return type

[**ExpandedUser**](ExpandedUser.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_using_get**
> User get_user_using_get(user_id)

getUser

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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | userId

try:
    # getUser
    api_response = api_instance.get_user_using_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId | 

### Return type

[**User**](User.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_users_using_post**
> invite_users_using_post(body)

inviteUsers

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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.InviteUserRequest() # InviteUserRequest | inviteUserRequest

try:
    # inviteUsers
    api_instance.invite_users_using_post(body)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->invite_users_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InviteUserRequest**](InviteUserRequest.md)| inviteUserRequest | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password_using_post**
> Response update_password_using_post(body)

updatePassword

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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.PasswordChange() # PasswordChange | updatePasswordRequest

try:
    # updatePassword
    api_response = api_instance.update_password_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->update_password_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordChange**](PasswordChange.md)| updatePasswordRequest | 

### Return type

[**Response**](Response.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

