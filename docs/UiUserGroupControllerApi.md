# swagger_client.UiUserGroupControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_group_using_post**](UiUserGroupControllerApi.md#create_user_group_using_post) | **POST** /cc-ui/v1/user-groups/ | createUserGroup
[**delete_user_group_using_delete**](UiUserGroupControllerApi.md#delete_user_group_using_delete) | **DELETE** /cc-ui/v1/user-groups/{groupId} | deleteUserGroup
[**get_all_group_using_get**](UiUserGroupControllerApi.md#get_all_group_using_get) | **GET** /cc-ui/v1/user-groups/ | getAllGroup
[**get_all_user_groups_expanded_using_get**](UiUserGroupControllerApi.md#get_all_user_groups_expanded_using_get) | **GET** /cc-ui/v1/user-groups/list/groups-expanded | getAllUserGroupsExpanded
[**get_user_group_expanded_using_get**](UiUserGroupControllerApi.md#get_user_group_expanded_using_get) | **GET** /cc-ui/v1/user-groups/{groupId}/group-expanded | getUserGroupExpanded
[**get_user_group_using_get**](UiUserGroupControllerApi.md#get_user_group_using_get) | **GET** /cc-ui/v1/user-groups/{groupId} | getUserGroup
[**update_user_group_using_put**](UiUserGroupControllerApi.md#update_user_group_using_put) | **PUT** /cc-ui/v1/user-groups/ | updateUserGroup

# **create_user_group_using_post**
> UserGroup create_user_group_using_post(body)

createUserGroup

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
api_instance = swagger_client.UiUserGroupControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserGroup() # UserGroup | userGroup

try:
    # createUserGroup
    api_response = api_instance.create_user_group_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserGroupControllerApi->create_user_group_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGroup**](UserGroup.md)| userGroup | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_group_using_delete**
> delete_user_group_using_delete(group_id)

deleteUserGroup

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
api_instance = swagger_client.UiUserGroupControllerApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | groupId

try:
    # deleteUserGroup
    api_instance.delete_user_group_using_delete(group_id)
except ApiException as e:
    print("Exception when calling UiUserGroupControllerApi->delete_user_group_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| groupId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_group_using_get**
> list[UserGroup] get_all_group_using_get()

getAllGroup

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
api_instance = swagger_client.UiUserGroupControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllGroup
    api_response = api_instance.get_all_group_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserGroupControllerApi->get_all_group_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserGroup]**](UserGroup.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user_groups_expanded_using_get**
> list[ExpandedUserGroup] get_all_user_groups_expanded_using_get()

getAllUserGroupsExpanded

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
api_instance = swagger_client.UiUserGroupControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllUserGroupsExpanded
    api_response = api_instance.get_all_user_groups_expanded_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserGroupControllerApi->get_all_user_groups_expanded_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ExpandedUserGroup]**](ExpandedUserGroup.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group_expanded_using_get**
> ExpandedUserGroup get_user_group_expanded_using_get(group_id)

getUserGroupExpanded

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
api_instance = swagger_client.UiUserGroupControllerApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | groupId

try:
    # getUserGroupExpanded
    api_response = api_instance.get_user_group_expanded_using_get(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserGroupControllerApi->get_user_group_expanded_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| groupId | 

### Return type

[**ExpandedUserGroup**](ExpandedUserGroup.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group_using_get**
> UserGroup get_user_group_using_get(group_id)

getUserGroup

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
api_instance = swagger_client.UiUserGroupControllerApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | groupId

try:
    # getUserGroup
    api_response = api_instance.get_user_group_using_get(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserGroupControllerApi->get_user_group_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| groupId | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_group_using_put**
> UserGroup update_user_group_using_put(body)

updateUserGroup

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
api_instance = swagger_client.UiUserGroupControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserGroup() # UserGroup | userGroup

try:
    # updateUserGroup
    api_response = api_instance.update_user_group_using_put(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserGroupControllerApi->update_user_group_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGroup**](UserGroup.md)| userGroup | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

