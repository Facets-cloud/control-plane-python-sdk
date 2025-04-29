# swagger_client.UiCustomRoleControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_role_using_post**](UiCustomRoleControllerApi.md#create_custom_role_using_post) | **POST** /cc-ui/v1/custom-role | createCustomRole
[**delete_custom_role_using_delete**](UiCustomRoleControllerApi.md#delete_custom_role_using_delete) | **DELETE** /cc-ui/v1/custom-role/{roleName} | deleteCustomRole
[**get_all_custom_roles_using_get**](UiCustomRoleControllerApi.md#get_all_custom_roles_using_get) | **GET** /cc-ui/v1/custom-role | getAllCustomRoles
[**get_all_roles_using_get**](UiCustomRoleControllerApi.md#get_all_roles_using_get) | **GET** /cc-ui/v1/custom-role/roles | getAllRoles
[**get_custom_role_using_get**](UiCustomRoleControllerApi.md#get_custom_role_using_get) | **GET** /cc-ui/v1/custom-role/{roleName} | getCustomRole
[**update_custom_role_using_put**](UiCustomRoleControllerApi.md#update_custom_role_using_put) | **PUT** /cc-ui/v1/custom-role/{roleName} | updateCustomRole

# **create_custom_role_using_post**
> RoleMapping create_custom_role_using_post(body)

createCustomRole

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
api_instance = swagger_client.UiCustomRoleControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomRoleRequest() # CustomRoleRequest | request

try:
    # createCustomRole
    api_response = api_instance.create_custom_role_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomRoleControllerApi->create_custom_role_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomRoleRequest**](CustomRoleRequest.md)| request | 

### Return type

[**RoleMapping**](RoleMapping.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_role_using_delete**
> delete_custom_role_using_delete(role_name)

deleteCustomRole

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
api_instance = swagger_client.UiCustomRoleControllerApi(swagger_client.ApiClient(configuration))
role_name = 'role_name_example' # str | roleName

try:
    # deleteCustomRole
    api_instance.delete_custom_role_using_delete(role_name)
except ApiException as e:
    print("Exception when calling UiCustomRoleControllerApi->delete_custom_role_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| roleName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_custom_roles_using_get**
> list[RoleMapping] get_all_custom_roles_using_get()

getAllCustomRoles

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
api_instance = swagger_client.UiCustomRoleControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllCustomRoles
    api_response = api_instance.get_all_custom_roles_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomRoleControllerApi->get_all_custom_roles_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RoleMapping]**](RoleMapping.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles_using_get**
> list[RoleMapping] get_all_roles_using_get()

getAllRoles

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
api_instance = swagger_client.UiCustomRoleControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllRoles
    api_response = api_instance.get_all_roles_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomRoleControllerApi->get_all_roles_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RoleMapping]**](RoleMapping.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_role_using_get**
> RoleMapping get_custom_role_using_get(role_name)

getCustomRole

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
api_instance = swagger_client.UiCustomRoleControllerApi(swagger_client.ApiClient(configuration))
role_name = 'role_name_example' # str | roleName

try:
    # getCustomRole
    api_response = api_instance.get_custom_role_using_get(role_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomRoleControllerApi->get_custom_role_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| roleName | 

### Return type

[**RoleMapping**](RoleMapping.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_role_using_put**
> RoleMapping update_custom_role_using_put(body, role_name)

updateCustomRole

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
api_instance = swagger_client.UiCustomRoleControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomRoleRequest() # CustomRoleRequest | request
role_name = 'role_name_example' # str | roleName

try:
    # updateCustomRole
    api_response = api_instance.update_custom_role_using_put(body, role_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomRoleControllerApi->update_custom_role_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomRoleRequest**](CustomRoleRequest.md)| request | 
 **role_name** | **str**| roleName | 

### Return type

[**RoleMapping**](RoleMapping.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

