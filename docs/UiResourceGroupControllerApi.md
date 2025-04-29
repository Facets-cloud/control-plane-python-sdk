# swagger_client.UiResourceGroupControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_using_post**](UiResourceGroupControllerApi.md#create_using_post) | **POST** /cc-ui/v1/resource-groups | create
[**delete_using_delete1**](UiResourceGroupControllerApi.md#delete_using_delete1) | **DELETE** /cc-ui/v1/resource-groups/{resourceGroupId} | delete
[**find_all_using_get**](UiResourceGroupControllerApi.md#find_all_using_get) | **GET** /cc-ui/v1/resource-groups | findAll
[**get_resource_group_using_get**](UiResourceGroupControllerApi.md#get_resource_group_using_get) | **GET** /cc-ui/v1/resource-groups/{resourceGroupId} | getResourceGroup
[**get_resource_groups_for_session_user_using_get**](UiResourceGroupControllerApi.md#get_resource_groups_for_session_user_using_get) | **GET** /cc-ui/v1/resource-groups/me | getResourceGroupsForSessionUser
[**update_all_resources_using_put**](UiResourceGroupControllerApi.md#update_all_resources_using_put) | **PUT** /cc-ui/v1/resource-groups/{resourceGroupId}/resources | updateAllResources
[**update_resource_using_patch**](UiResourceGroupControllerApi.md#update_resource_using_patch) | **PATCH** /cc-ui/v1/resource-groups/{resourceGroupId}/resources | updateResource
[**update_using_put1**](UiResourceGroupControllerApi.md#update_using_put1) | **PUT** /cc-ui/v1/resource-groups/{resourceGroupId} | update

# **create_using_post**
> ResourceGroup create_using_post(body)

create

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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResourceGroupRequest() # ResourceGroupRequest | resourceGroupRequest

try:
    # create
    api_response = api_instance.create_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->create_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceGroupRequest**](ResourceGroupRequest.md)| resourceGroupRequest | 

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete1**
> Response delete_using_delete1(resource_group_id)

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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))
resource_group_id = 'resource_group_id_example' # str | resourceGroupId

try:
    # delete
    api_response = api_instance.delete_using_delete1(resource_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->delete_using_delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_group_id** | **str**| resourceGroupId | 

### Return type

[**Response**](Response.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_using_get**
> list[ResourceGroup] find_all_using_get()

findAll

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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))

try:
    # findAll
    api_response = api_instance.find_all_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->find_all_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ResourceGroup]**](ResourceGroup.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_group_using_get**
> ResourceGroup get_resource_group_using_get(resource_group_id)

getResourceGroup

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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))
resource_group_id = 'resource_group_id_example' # str | resourceGroupId

try:
    # getResourceGroup
    api_response = api_instance.get_resource_group_using_get(resource_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->get_resource_group_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_group_id** | **str**| resourceGroupId | 

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_groups_for_session_user_using_get**
> list[ResourceGroup] get_resource_groups_for_session_user_using_get()

getResourceGroupsForSessionUser

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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))

try:
    # getResourceGroupsForSessionUser
    api_response = api_instance.get_resource_groups_for_session_user_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->get_resource_groups_for_session_user_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ResourceGroup]**](ResourceGroup.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_all_resources_using_put**
> ResourceGroup update_all_resources_using_put(body, resource_group_id)

updateAllResources

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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ResourceInfo()] # list[ResourceInfo] | allResourcesUpdateRequest
resource_group_id = 'resource_group_id_example' # str | resourceGroupId

try:
    # updateAllResources
    api_response = api_instance.update_all_resources_using_put(body, resource_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->update_all_resources_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ResourceInfo]**](ResourceInfo.md)| allResourcesUpdateRequest | 
 **resource_group_id** | **str**| resourceGroupId | 

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource_using_patch**
> ResourceGroup update_resource_using_patch(body, resource_group_id)

updateResource

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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResourceInfo() # ResourceInfo | resourceUpdateRequest
resource_group_id = 'resource_group_id_example' # str | resourceGroupId

try:
    # updateResource
    api_response = api_instance.update_resource_using_patch(body, resource_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->update_resource_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceInfo**](ResourceInfo.md)| resourceUpdateRequest | 
 **resource_group_id** | **str**| resourceGroupId | 

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put1**
> ResourceGroup update_using_put1(body, resource_group_id)

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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResourceGroupRequest() # ResourceGroupRequest | resourceGroupRequest
resource_group_id = 'resource_group_id_example' # str | resourceGroupId

try:
    # update
    api_response = api_instance.update_using_put1(body, resource_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->update_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceGroupRequest**](ResourceGroupRequest.md)| resourceGroupRequest | 
 **resource_group_id** | **str**| resourceGroupId | 

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

