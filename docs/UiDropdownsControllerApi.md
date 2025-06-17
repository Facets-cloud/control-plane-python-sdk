# swagger_client.UiDropdownsControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_affected_resources_by_cluster**](UiDropdownsControllerApi.md#get_affected_resources_by_cluster) | **POST** /cc-ui/v1/dropdown/cluster/{clusterId}/affected-resources | 
[**get_affected_resources_by_stack**](UiDropdownsControllerApi.md#get_affected_resources_by_stack) | **POST** /cc-ui/v1/dropdown/stack/{stackName}/affected-resources | 
[**get_all_cluster_resources_by_stack**](UiDropdownsControllerApi.md#get_all_cluster_resources_by_stack) | **GET** /cc-ui/v1/dropdown/stack/{stackName}/{resourceType}/{resourceName}/cluster-resources-info | 
[**get_all_permissions**](UiDropdownsControllerApi.md#get_all_permissions) | **GET** /cc-ui/v1/dropdown/getAllPermissions | 
[**get_all_resources**](UiDropdownsControllerApi.md#get_all_resources) | **GET** /cc-ui/v1/dropdown/cluster/{clusterId}/resources | 
[**get_all_resources_by_cluster**](UiDropdownsControllerApi.md#get_all_resources_by_cluster) | **GET** /cc-ui/v1/dropdown/cluster/{clusterId}/resources-info | 
[**get_all_resources_by_stack**](UiDropdownsControllerApi.md#get_all_resources_by_stack) | **GET** /cc-ui/v1/dropdown/stack/{stackName}/resources-info | 
[**get_all_resources_for_all_cluster_of_stack**](UiDropdownsControllerApi.md#get_all_resources_for_all_cluster_of_stack) | **GET** /cc-ui/v1/dropdown/stack/{stackName}/all-cluster-resources | 
[**get_all_vcs**](UiDropdownsControllerApi.md#get_all_vcs) | **GET** /cc-ui/v1/dropdown/vcs | 
[**get_application_list_by_cluster_id_and_resource_name**](UiDropdownsControllerApi.md#get_application_list_by_cluster_id_and_resource_name) | **GET** /cc-ui/v1/dropdown/{clusterId}/{resourceType} | 
[**get_az_for_region_by_cloud**](UiDropdownsControllerApi.md#get_az_for_region_by_cloud) | **GET** /cc-ui/v1/dropdown/{cloud}/region/{region}/availability-zones | 
[**get_file_from_facets_modules**](UiDropdownsControllerApi.md#get_file_from_facets_modules) | **GET** /cc-ui/v1/dropdown/file | 
[**get_git_history_for_resource**](UiDropdownsControllerApi.md#get_git_history_for_resource) | **GET** /cc-ui/v1/dropdown/logs/cluster/{clusterId}/resourceName/{resourceName}/resourceType/{resourceType} | 
[**get_launch_dag**](UiDropdownsControllerApi.md#get_launch_dag) | **GET** /cc-ui/v1/dropdown/{clusterId}/cloud/{cloud}/launch-dag | 
[**get_output_references**](UiDropdownsControllerApi.md#get_output_references) | **GET** /cc-ui/v1/dropdown/{stackName}/output/{outputType}/references | 
[**get_output_references_by_type**](UiDropdownsControllerApi.md#get_output_references_by_type) | **GET** /cc-ui/v1/dropdown/{stackName}/output-references | 
[**get_regions**](UiDropdownsControllerApi.md#get_regions) | **GET** /cc-ui/v1/dropdown/{cloud}/regions | 
[**get_regions_v2**](UiDropdownsControllerApi.md#get_regions_v2) | **GET** /cc-ui/v1/dropdown/{cloud}/regions-v2 | 
[**get_release_streams**](UiDropdownsControllerApi.md#get_release_streams) | **GET** /cc-ui/v1/dropdown/releaseStreams | 
[**get_resource_by_cluster_id**](UiDropdownsControllerApi.md#get_resource_by_cluster_id) | **GET** /cc-ui/v1/dropdown/cluster/{clusterId}/{resourceType}/{resourceName}/resource-info | 
[**get_resource_by_stack**](UiDropdownsControllerApi.md#get_resource_by_stack) | **GET** /cc-ui/v1/dropdown/stack/{stackName}/{resourceType}/{resourceName}/resource-info | 
[**get_resource_histories_by_stack**](UiDropdownsControllerApi.md#get_resource_histories_by_stack) | **GET** /cc-ui/v1/dropdown/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/resource-history | 
[**get_resource_history_overview_by_stack**](UiDropdownsControllerApi.md#get_resource_history_overview_by_stack) | **GET** /cc-ui/v1/dropdown/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/resource-history-overview | 
[**get_role_permissions**](UiDropdownsControllerApi.md#get_role_permissions) | **GET** /cc-ui/v1/dropdown/rolePermissions/{role} | 
[**get_service_overview**](UiDropdownsControllerApi.md#get_service_overview) | **GET** /cc-ui/v1/dropdown/stack/{stackName}/service/{serviceName}/overview | 
[**sync_cluster_history**](UiDropdownsControllerApi.md#sync_cluster_history) | **POST** /cc-ui/v1/dropdown/logs/cluster/{clusterId} | 
[**sync_substack_git_history**](UiDropdownsControllerApi.md#sync_substack_git_history) | **POST** /cc-ui/v1/dropdown/logs/substack | 

# **get_affected_resources_by_cluster**
> ResourceAffectedResponse get_affected_resources_by_cluster(body, cluster_id)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AffectedResourcesRequest() # AffectedResourcesRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_affected_resources_by_cluster(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_affected_resources_by_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AffectedResourcesRequest**](AffectedResourcesRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ResourceAffectedResponse**](ResourceAffectedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_affected_resources_by_stack**
> ResourceAffectedResponse get_affected_resources_by_stack(body, stack_name)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AffectedResourcesRequest() # AffectedResourcesRequest | 
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_affected_resources_by_stack(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_affected_resources_by_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AffectedResourcesRequest**](AffectedResourcesRequest.md)|  | 
 **stack_name** | **str**|  | 

### Return type

[**ResourceAffectedResponse**](ResourceAffectedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_cluster_resources_by_stack**
> list[BlueprintFile] get_all_cluster_resources_by_stack(stack_name, resource_type, resource_name)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.get_all_cluster_resources_by_stack(stack_name, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_all_cluster_resources_by_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

[**list[BlueprintFile]**](BlueprintFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_permissions**
> list[str] get_all_permissions()



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_permissions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_all_permissions: %s\n" % e)
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

# **get_all_resources**
> dict(str, list[str]) get_all_resources(cluster_id, exclude_substack_resources=exclude_substack_resources)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
exclude_substack_resources = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_resources(cluster_id, exclude_substack_resources=exclude_substack_resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_all_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **exclude_substack_resources** | **bool**|  | [optional] [default to false]

### Return type

**dict(str, list[str])**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_resources_by_cluster**
> list[BlueprintFile] get_all_resources_by_cluster(cluster_id, include_content=include_content, include_substack=include_substack, exclude_add_ons=exclude_add_ons)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
include_content = false # bool |  (optional) (default to false)
include_substack = true # bool |  (optional) (default to true)
exclude_add_ons = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_resources_by_cluster(cluster_id, include_content=include_content, include_substack=include_substack, exclude_add_ons=exclude_add_ons)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_all_resources_by_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **include_content** | **bool**|  | [optional] [default to false]
 **include_substack** | **bool**|  | [optional] [default to true]
 **exclude_add_ons** | **bool**|  | [optional] [default to false]

### Return type

[**list[BlueprintFile]**](BlueprintFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_resources_by_stack**
> list[BlueprintFile] get_all_resources_by_stack(stack_name, include_content=include_content, branch=branch, exclude_add_ons=exclude_add_ons)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
include_content = false # bool |  (optional) (default to false)
branch = '' # str |  (optional)
exclude_add_ons = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_resources_by_stack(stack_name, include_content=include_content, branch=branch, exclude_add_ons=exclude_add_ons)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_all_resources_by_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **include_content** | **bool**|  | [optional] [default to false]
 **branch** | **str**|  | [optional] 
 **exclude_add_ons** | **bool**|  | [optional] [default to false]

### Return type

[**list[BlueprintFile]**](BlueprintFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_resources_for_all_cluster_of_stack**
> list[ClusterResourcesResponse] get_all_resources_for_all_cluster_of_stack(stack_name, exclude_add_ons=exclude_add_ons)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
exclude_add_ons = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_resources_for_all_cluster_of_stack(stack_name, exclude_add_ons=exclude_add_ons)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_all_resources_for_all_cluster_of_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **exclude_add_ons** | **bool**|  | [optional] [default to false]

### Return type

[**list[ClusterResourcesResponse]**](ClusterResourcesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vcs**
> list[str] get_all_vcs()



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_vcs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_all_vcs: %s\n" % e)
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

# **get_application_list_by_cluster_id_and_resource_name**
> list[str] get_application_list_by_cluster_id_and_resource_name(cluster_id, resource_type)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 

try:
    api_response = api_instance.get_application_list_by_cluster_id_and_resource_name(cluster_id, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_application_list_by_cluster_id_and_resource_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_az_for_region_by_cloud**
> list[str] get_az_for_region_by_cloud(cloud, region)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cloud = 'cloud_example' # str | 
region = 'region_example' # str | 

try:
    api_response = api_instance.get_az_for_region_by_cloud(cloud, region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_az_for_region_by_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud** | **str**|  | 
 **region** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_from_facets_modules**
> JsonNode get_file_from_facets_modules(path, file_name)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
path = 'path_example' # str | 
file_name = 'file_name_example' # str | 

try:
    api_response = api_instance.get_file_from_facets_modules(path, file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_file_from_facets_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **file_name** | **str**|  | 

### Return type

[**JsonNode**](JsonNode.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_git_history_for_resource**
> StackGitLog get_git_history_for_resource(cluster_id, resource_name, resource_type)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_name = 'resource_name_example' # str | 
resource_type = 'resource_type_example' # str | 

try:
    api_response = api_instance.get_git_history_for_resource(cluster_id, resource_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_git_history_for_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_name** | **str**|  | 
 **resource_type** | **str**|  | 

### Return type

[**StackGitLog**](StackGitLog.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_launch_dag**
> list[BlueprintFile] get_launch_dag(cluster_id, cloud, is_provided_k8s=is_provided_k8s, is_dependent=is_dependent)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
cloud = 'cloud_example' # str | 
is_provided_k8s = false # bool |  (optional) (default to false)
is_dependent = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_launch_dag(cluster_id, cloud, is_provided_k8s=is_provided_k8s, is_dependent=is_dependent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_launch_dag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **cloud** | **str**|  | 
 **is_provided_k8s** | **bool**|  | [optional] [default to false]
 **is_dependent** | **bool**|  | [optional] [default to false]

### Return type

[**list[BlueprintFile]**](BlueprintFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_output_references**
> list[OutputReference] get_output_references(stack_name, output_type, resource_type=resource_type, resource_name=resource_name)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
output_type = 'output_type_example' # str | 
resource_type = 'resource_type_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)

try:
    api_response = api_instance.get_output_references(stack_name, output_type, resource_type=resource_type, resource_name=resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_output_references: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **output_type** | **str**|  | 
 **resource_type** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 

### Return type

[**list[OutputReference]**](OutputReference.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_output_references_by_type**
> list[OutputReference] get_output_references_by_type(stack_name, output_type, resource_type=resource_type, resource_name=resource_name)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
output_type = 'output_type_example' # str | 
resource_type = 'resource_type_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)

try:
    api_response = api_instance.get_output_references_by_type(stack_name, output_type, resource_type=resource_type, resource_name=resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_output_references_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **output_type** | **str**|  | 
 **resource_type** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 

### Return type

[**list[OutputReference]**](OutputReference.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_regions**
> list[AllRegionsAndAZ] get_regions(cloud)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cloud = 'cloud_example' # str | 

try:
    api_response = api_instance.get_regions(cloud)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud** | **str**|  | 

### Return type

[**list[AllRegionsAndAZ]**](AllRegionsAndAZ.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_regions_v2**
> AllRegionsAndAZ get_regions_v2(cloud)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cloud = 'cloud_example' # str | 

try:
    api_response = api_instance.get_regions_v2(cloud)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_regions_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud** | **str**|  | 

### Return type

[**AllRegionsAndAZ**](AllRegionsAndAZ.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_streams**
> list[str] get_release_streams()



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_release_streams()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_release_streams: %s\n" % e)
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

# **get_resource_by_cluster_id**
> BlueprintFile get_resource_by_cluster_id(cluster_id, resource_type, resource_name, include_content=include_content)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 
include_content = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_resource_by_cluster_id(cluster_id, resource_type, resource_name, include_content=include_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_resource_by_cluster_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 
 **include_content** | **bool**|  | [optional] [default to false]

### Return type

[**BlueprintFile**](BlueprintFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_by_stack**
> BlueprintFile get_resource_by_stack(stack_name, resource_type, resource_name, branch=branch)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 
branch = '' # str |  (optional)

try:
    api_response = api_instance.get_resource_by_stack(stack_name, resource_type, resource_name, branch=branch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_resource_by_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 
 **branch** | **str**|  | [optional] 

### Return type

[**BlueprintFile**](BlueprintFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_histories_by_stack**
> list[ResourceHistory] get_resource_histories_by_stack(stack_name, resource_type, resource_name)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.get_resource_histories_by_stack(stack_name, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_resource_histories_by_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

[**list[ResourceHistory]**](ResourceHistory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_history_overview_by_stack**
> list[ResourceHistoryOverview] get_resource_history_overview_by_stack(stack_name, resource_type, resource_name)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.get_resource_history_overview_by_stack(stack_name, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_resource_history_overview_by_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

[**list[ResourceHistoryOverview]**](ResourceHistoryOverview.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_permissions**
> list[str] get_role_permissions(role)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
role = 'role_example' # str | 

try:
    api_response = api_instance.get_role_permissions(role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_role_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_overview**
> ServiceOverview get_service_overview(stack_name, service_name)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
service_name = 'service_name_example' # str | 

try:
    api_response = api_instance.get_service_overview(stack_name, service_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_service_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **service_name** | **str**|  | 

### Return type

[**ServiceOverview**](ServiceOverview.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_cluster_history**
> sync_cluster_history(cluster_id, force=force)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
force = false # bool |  (optional) (default to false)

try:
    api_instance.sync_cluster_history(cluster_id, force=force)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->sync_cluster_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **force** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_substack_git_history**
> sync_substack_git_history(substack_name, force_sync)



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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
substack_name = 'substack_name_example' # str | 
force_sync = true # bool | 

try:
    api_instance.sync_substack_git_history(substack_name, force_sync)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->sync_substack_git_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **substack_name** | **str**|  | 
 **force_sync** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

