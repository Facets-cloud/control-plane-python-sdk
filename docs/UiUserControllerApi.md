# swagger_client.UiUserControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze_access**](UiUserControllerApi.md#analyze_access) | **GET** /cc-ui/v1/users/analyze-access | 
[**create_token**](UiUserControllerApi.md#create_token) | **POST** /cc-ui/v1/users/createAccessToken | 
[**delete_all_logged_in_users**](UiUserControllerApi.md#delete_all_logged_in_users) | **DELETE** /cc-ui/v1/users/loggedIn/session | 
[**delete_token**](UiUserControllerApi.md#delete_token) | **DELETE** /cc-ui/v1/users/tokens/{tokenId} | 
[**delete_user**](UiUserControllerApi.md#delete_user) | **DELETE** /cc-ui/v1/users/{userId} | 
[**get_all_logged_in_users**](UiUserControllerApi.md#get_all_logged_in_users) | **GET** /cc-ui/v1/users/loggedIn | 
[**get_all_system_roles**](UiUserControllerApi.md#get_all_system_roles) | **GET** /cc-ui/v1/users/roles | 
[**get_all_users**](UiUserControllerApi.md#get_all_users) | **GET** /cc-ui/v1/users/ | 
[**get_all_users_expanded**](UiUserControllerApi.md#get_all_users_expanded) | **GET** /cc-ui/v1/users/list/users-expanded | 
[**get_current_user**](UiUserControllerApi.md#get_current_user) | **GET** /cc-ui/v1/users/current-user | 
[**get_token**](UiUserControllerApi.md#get_token) | **GET** /cc-ui/v1/users/tokens | 
[**get_user**](UiUserControllerApi.md#get_user) | **GET** /cc-ui/v1/users/{userId} | 
[**get_user_expanded**](UiUserControllerApi.md#get_user_expanded) | **GET** /cc-ui/v1/users/{userId}/user-expanded | 
[**invite_users**](UiUserControllerApi.md#invite_users) | **POST** /cc-ui/v1/users/invite-users | 
[**update_password**](UiUserControllerApi.md#update_password) | **POST** /cc-ui/v1/users/updatePassword | 

# **analyze_access**
> list[ComCapillaryOpsCpV2RbacAccessAnalyzerResponse] analyze_access(permissions)



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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
permissions = ['permissions_example'] # list[str] | 

try:
    api_response = api_instance.analyze_access(permissions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->analyze_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permissions** | [**list[str]**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpV2RbacAccessAnalyzerResponse]**](ComCapillaryOpsCpV2RbacAccessAnalyzerResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token**
> list[ComCapillaryOpsCpBoAuthUserAccessToken] create_token(token)



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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
token = swagger_client.ComCapillaryOpsCpBoAuthUserAccessToken() # ComCapillaryOpsCpBoAuthUserAccessToken | 

try:
    api_response = api_instance.create_token(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | [**ComCapillaryOpsCpBoAuthUserAccessToken**](.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoAuthUserAccessToken]**](ComCapillaryOpsCpBoAuthUserAccessToken.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_logged_in_users**
> bool delete_all_logged_in_users()



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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.delete_all_logged_in_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->delete_all_logged_in_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token**
> list[ComCapillaryOpsCpBoAuthUserAccessToken] delete_token(token_id)



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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
token_id = 'token_id_example' # str | 

try:
    api_response = api_instance.delete_token(token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->delete_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoAuthUserAccessToken]**](ComCapillaryOpsCpBoAuthUserAccessToken.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> bool delete_user(user_id)



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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.delete_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_logged_in_users**
> list[object] get_all_logged_in_users()



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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_logged_in_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_all_logged_in_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_system_roles**
> list[str] get_all_system_roles()



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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_system_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_all_system_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users**
> list[ComCapillaryOpsDeployerBoUser] get_all_users()



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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_all_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsDeployerBoUser]**](ComCapillaryOpsDeployerBoUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users_expanded**
> list[ComCapillaryOpsCpV2RbacExpandedUser] get_all_users_expanded()



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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_users_expanded()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_all_users_expanded: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpV2RbacExpandedUser]**](ComCapillaryOpsCpV2RbacExpandedUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> ComCapillaryOpsDeployerBoUser get_current_user()



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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ComCapillaryOpsDeployerBoUser**](ComCapillaryOpsDeployerBoUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> list[ComCapillaryOpsCpBoAuthUserAccessToken] get_token()



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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoAuthUserAccessToken]**](ComCapillaryOpsCpBoAuthUserAccessToken.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> ComCapillaryOpsDeployerBoUser get_user(user_id)



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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.get_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoUser**](ComCapillaryOpsDeployerBoUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_expanded**
> ComCapillaryOpsCpV2RbacExpandedUser get_user_expanded(user_id)



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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.get_user_expanded(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->get_user_expanded: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpV2RbacExpandedUser**](ComCapillaryOpsCpV2RbacExpandedUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_users**
> invite_users(body)



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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoUserInviteUserRequest() # ComCapillaryOpsCpBoUserInviteUserRequest | 

try:
    api_instance.invite_users(body)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->invite_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoUserInviteUserRequest**](ComCapillaryOpsCpBoUserInviteUserRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password**
> ComCapillaryOpsCpBoResponse update_password(body)



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
api_instance = swagger_client.UiUserControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoPasswordChange() # ComCapillaryOpsDeployerBoPasswordChange | 

try:
    api_response = api_instance.update_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserControllerApi->update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoPasswordChange**](ComCapillaryOpsDeployerBoPasswordChange.md)|  | 

### Return type

[**ComCapillaryOpsCpBoResponse**](ComCapillaryOpsCpBoResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

