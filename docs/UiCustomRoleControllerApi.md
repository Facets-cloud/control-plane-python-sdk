# swagger_client.UiCustomRoleControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_role**](UiCustomRoleControllerApi.md#create_custom_role) | **POST** /cc-ui/v1/custom-role | 
[**delete_custom_role**](UiCustomRoleControllerApi.md#delete_custom_role) | **DELETE** /cc-ui/v1/custom-role/{roleName} | 
[**get_all_custom_roles**](UiCustomRoleControllerApi.md#get_all_custom_roles) | **GET** /cc-ui/v1/custom-role | 
[**get_all_roles**](UiCustomRoleControllerApi.md#get_all_roles) | **GET** /cc-ui/v1/custom-role/roles | 
[**get_custom_role**](UiCustomRoleControllerApi.md#get_custom_role) | **GET** /cc-ui/v1/custom-role/{roleName} | 
[**update_custom_role**](UiCustomRoleControllerApi.md#update_custom_role) | **PUT** /cc-ui/v1/custom-role/{roleName} | 

# **create_custom_role**
> RoleMapping create_custom_role(body)



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
api_instance = swagger_client.UiCustomRoleControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomRoleRequest() # CustomRoleRequest | 

try:
    api_response = api_instance.create_custom_role(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomRoleControllerApi->create_custom_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomRoleRequest**](CustomRoleRequest.md)|  | 

### Return type

[**RoleMapping**](RoleMapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_role**
> delete_custom_role(role_name)



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
api_instance = swagger_client.UiCustomRoleControllerApi(swagger_client.ApiClient(configuration))
role_name = 'role_name_example' # str | 

try:
    api_instance.delete_custom_role(role_name)
except ApiException as e:
    print("Exception when calling UiCustomRoleControllerApi->delete_custom_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_custom_roles**
> list[RoleMapping] get_all_custom_roles()



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
api_instance = swagger_client.UiCustomRoleControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_custom_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomRoleControllerApi->get_all_custom_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RoleMapping]**](RoleMapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles**
> list[RoleMapping] get_all_roles()



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
api_instance = swagger_client.UiCustomRoleControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomRoleControllerApi->get_all_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RoleMapping]**](RoleMapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_role**
> RoleMapping get_custom_role(role_name)



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
api_instance = swagger_client.UiCustomRoleControllerApi(swagger_client.ApiClient(configuration))
role_name = 'role_name_example' # str | 

try:
    api_response = api_instance.get_custom_role(role_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomRoleControllerApi->get_custom_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**|  | 

### Return type

[**RoleMapping**](RoleMapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_role**
> RoleMapping update_custom_role(body, role_name)



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
api_instance = swagger_client.UiCustomRoleControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomRoleRequest() # CustomRoleRequest | 
role_name = 'role_name_example' # str | 

try:
    api_response = api_instance.update_custom_role(body, role_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomRoleControllerApi->update_custom_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomRoleRequest**](CustomRoleRequest.md)|  | 
 **role_name** | **str**|  | 

### Return type

[**RoleMapping**](RoleMapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

