# swagger_client.UiUserGroupControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_group**](UiUserGroupControllerApi.md#create_user_group) | **POST** /cc-ui/v1/user-groups/ | 
[**delete_user_group**](UiUserGroupControllerApi.md#delete_user_group) | **DELETE** /cc-ui/v1/user-groups/{groupId} | 
[**get_all_group**](UiUserGroupControllerApi.md#get_all_group) | **GET** /cc-ui/v1/user-groups/ | 
[**get_all_user_groups_expanded**](UiUserGroupControllerApi.md#get_all_user_groups_expanded) | **GET** /cc-ui/v1/user-groups/list/groups-expanded | 
[**get_user_group**](UiUserGroupControllerApi.md#get_user_group) | **GET** /cc-ui/v1/user-groups/{groupId} | 
[**get_user_group_expanded**](UiUserGroupControllerApi.md#get_user_group_expanded) | **GET** /cc-ui/v1/user-groups/{groupId}/group-expanded | 
[**update_user_group**](UiUserGroupControllerApi.md#update_user_group) | **PUT** /cc-ui/v1/user-groups/ | 

# **create_user_group**
> ComCapillaryOpsCpBoGroupUserGroup create_user_group(body)



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
api_instance = swagger_client.UiUserGroupControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoGroupUserGroup() # ComCapillaryOpsCpBoGroupUserGroup | 

try:
    api_response = api_instance.create_user_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserGroupControllerApi->create_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoGroupUserGroup**](ComCapillaryOpsCpBoGroupUserGroup.md)|  | 

### Return type

[**ComCapillaryOpsCpBoGroupUserGroup**](ComCapillaryOpsCpBoGroupUserGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_group**
> delete_user_group(group_id)



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
api_instance = swagger_client.UiUserGroupControllerApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 

try:
    api_instance.delete_user_group(group_id)
except ApiException as e:
    print("Exception when calling UiUserGroupControllerApi->delete_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_group**
> list[ComCapillaryOpsCpBoGroupUserGroup] get_all_group()



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
api_instance = swagger_client.UiUserGroupControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_group()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserGroupControllerApi->get_all_group: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoGroupUserGroup]**](ComCapillaryOpsCpBoGroupUserGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user_groups_expanded**
> list[ComCapillaryOpsCpV2RbacExpandedUserGroup] get_all_user_groups_expanded()



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
api_instance = swagger_client.UiUserGroupControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_user_groups_expanded()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserGroupControllerApi->get_all_user_groups_expanded: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpV2RbacExpandedUserGroup]**](ComCapillaryOpsCpV2RbacExpandedUserGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group**
> ComCapillaryOpsCpBoGroupUserGroup get_user_group(group_id)



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
api_instance = swagger_client.UiUserGroupControllerApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 

try:
    api_response = api_instance.get_user_group(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserGroupControllerApi->get_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoGroupUserGroup**](ComCapillaryOpsCpBoGroupUserGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group_expanded**
> ComCapillaryOpsCpV2RbacExpandedUserGroup get_user_group_expanded(group_id)



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
api_instance = swagger_client.UiUserGroupControllerApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 

try:
    api_response = api_instance.get_user_group_expanded(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserGroupControllerApi->get_user_group_expanded: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpV2RbacExpandedUserGroup**](ComCapillaryOpsCpV2RbacExpandedUserGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_group**
> ComCapillaryOpsCpBoGroupUserGroup update_user_group(body)



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
api_instance = swagger_client.UiUserGroupControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoGroupUserGroup() # ComCapillaryOpsCpBoGroupUserGroup | 

try:
    api_response = api_instance.update_user_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserGroupControllerApi->update_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoGroupUserGroup**](ComCapillaryOpsCpBoGroupUserGroup.md)|  | 

### Return type

[**ComCapillaryOpsCpBoGroupUserGroup**](ComCapillaryOpsCpBoGroupUserGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

