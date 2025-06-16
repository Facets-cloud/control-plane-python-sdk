# swagger_client.UiResourceGroupControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](UiResourceGroupControllerApi.md#create) | **POST** /cc-ui/v1/resource-groups | 
[**delete1**](UiResourceGroupControllerApi.md#delete1) | **DELETE** /cc-ui/v1/resource-groups/{resourceGroupId} | 
[**find_all**](UiResourceGroupControllerApi.md#find_all) | **GET** /cc-ui/v1/resource-groups | 
[**get_resource_group**](UiResourceGroupControllerApi.md#get_resource_group) | **GET** /cc-ui/v1/resource-groups/{resourceGroupId} | 
[**get_resource_groups_for_session_user**](UiResourceGroupControllerApi.md#get_resource_groups_for_session_user) | **GET** /cc-ui/v1/resource-groups/me | 
[**update1**](UiResourceGroupControllerApi.md#update1) | **PUT** /cc-ui/v1/resource-groups/{resourceGroupId} | 
[**update_all_resources**](UiResourceGroupControllerApi.md#update_all_resources) | **PUT** /cc-ui/v1/resource-groups/{resourceGroupId}/resources | 
[**update_resource**](UiResourceGroupControllerApi.md#update_resource) | **PATCH** /cc-ui/v1/resource-groups/{resourceGroupId}/resources | 

# **create**
> ComCapillaryOpsCpBoResourceGroup create(body)



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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsResourceGroupRequest() # ComCapillaryOpsCpBoRequestsResourceGroupRequest | 

try:
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsResourceGroupRequest**](ComCapillaryOpsCpBoRequestsResourceGroupRequest.md)|  | 

### Return type

[**ComCapillaryOpsCpBoResourceGroup**](ComCapillaryOpsCpBoResourceGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete1**
> ComCapillaryOpsCpBoResponse delete1(resource_group_id)



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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))
resource_group_id = 'resource_group_id_example' # str | 

try:
    api_response = api_instance.delete1(resource_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_group_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoResponse**](ComCapillaryOpsCpBoResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all**
> list[ComCapillaryOpsCpBoResourceGroup] find_all()



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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.find_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->find_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoResourceGroup]**](ComCapillaryOpsCpBoResourceGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_group**
> ComCapillaryOpsCpBoResourceGroup get_resource_group(resource_group_id)



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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))
resource_group_id = 'resource_group_id_example' # str | 

try:
    api_response = api_instance.get_resource_group(resource_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->get_resource_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_group_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoResourceGroup**](ComCapillaryOpsCpBoResourceGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_groups_for_session_user**
> list[ComCapillaryOpsCpBoResourceGroup] get_resource_groups_for_session_user()



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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_resource_groups_for_session_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->get_resource_groups_for_session_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoResourceGroup]**](ComCapillaryOpsCpBoResourceGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update1**
> ComCapillaryOpsCpBoResourceGroup update1(body, resource_group_id)



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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsResourceGroupRequest() # ComCapillaryOpsCpBoRequestsResourceGroupRequest | 
resource_group_id = 'resource_group_id_example' # str | 

try:
    api_response = api_instance.update1(body, resource_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->update1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsResourceGroupRequest**](ComCapillaryOpsCpBoRequestsResourceGroupRequest.md)|  | 
 **resource_group_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoResourceGroup**](ComCapillaryOpsCpBoResourceGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_all_resources**
> ComCapillaryOpsCpBoResourceGroup update_all_resources(body, resource_group_id)



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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ComCapillaryOpsCpBoResourceGroupResourceInfo()] # list[ComCapillaryOpsCpBoResourceGroupResourceInfo] | 
resource_group_id = 'resource_group_id_example' # str | 

try:
    api_response = api_instance.update_all_resources(body, resource_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->update_all_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ComCapillaryOpsCpBoResourceGroupResourceInfo]**](ComCapillaryOpsCpBoResourceGroupResourceInfo.md)|  | 
 **resource_group_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoResourceGroup**](ComCapillaryOpsCpBoResourceGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource**
> ComCapillaryOpsCpBoResourceGroup update_resource(body, resource_group_id)



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
api_instance = swagger_client.UiResourceGroupControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoResourceGroupResourceInfo() # ComCapillaryOpsCpBoResourceGroupResourceInfo | 
resource_group_id = 'resource_group_id_example' # str | 

try:
    api_response = api_instance.update_resource(body, resource_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiResourceGroupControllerApi->update_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoResourceGroupResourceInfo**](ComCapillaryOpsCpBoResourceGroupResourceInfo.md)|  | 
 **resource_group_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoResourceGroup**](ComCapillaryOpsCpBoResourceGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

