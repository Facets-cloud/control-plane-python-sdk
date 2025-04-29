# swagger_client.UiDropdownsControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_cluster_resources_by_stack_using_get**](UiDropdownsControllerApi.md#get_all_cluster_resources_by_stack_using_get) | **GET** /cc-ui/v1/dropdown/stack/{stackName}/{resourceType}/{resourceName}/cluster-resources-info | getAllClusterResourcesByStack
[**get_all_permissions_using_get**](UiDropdownsControllerApi.md#get_all_permissions_using_get) | **GET** /cc-ui/v1/dropdown/getAllPermissions | getAllPermissions
[**get_all_resources_by_cluster_using_get**](UiDropdownsControllerApi.md#get_all_resources_by_cluster_using_get) | **GET** /cc-ui/v1/dropdown/cluster/{clusterId}/resources-info | getAllResourcesByCluster
[**get_all_resources_by_stack_using_get**](UiDropdownsControllerApi.md#get_all_resources_by_stack_using_get) | **GET** /cc-ui/v1/dropdown/stack/{stackName}/resources-info | getAllResourcesByStack
[**get_all_resources_for_all_cluster_of_stack_using_get**](UiDropdownsControllerApi.md#get_all_resources_for_all_cluster_of_stack_using_get) | **GET** /cc-ui/v1/dropdown/stack/{stackName}/all-cluster-resources | getAllResourcesForAllClusterOfStack
[**get_all_resources_using_get**](UiDropdownsControllerApi.md#get_all_resources_using_get) | **GET** /cc-ui/v1/dropdown/cluster/{clusterId}/resources | getAllResources
[**get_all_vcs_using_get**](UiDropdownsControllerApi.md#get_all_vcs_using_get) | **GET** /cc-ui/v1/dropdown/vcs | getAllVCS
[**get_application_list_by_cluster_id_and_resource_name_using_get**](UiDropdownsControllerApi.md#get_application_list_by_cluster_id_and_resource_name_using_get) | **GET** /cc-ui/v1/dropdown/{clusterId}/{resourceType} | getApplicationListByClusterIdAndResourceName
[**get_file_from_facets_modules_using_get**](UiDropdownsControllerApi.md#get_file_from_facets_modules_using_get) | **GET** /cc-ui/v1/dropdown/file | getFileFromFacetsModules
[**get_git_history_for_resource_using_get**](UiDropdownsControllerApi.md#get_git_history_for_resource_using_get) | **GET** /cc-ui/v1/dropdown/logs/cluster/{clusterId}/resourceName/{resourceName}/resourceType/{resourceType} | getGitHistoryForResource
[**get_launch_dag_using_get**](UiDropdownsControllerApi.md#get_launch_dag_using_get) | **GET** /cc-ui/v1/dropdown/{clusterId}/cloud/{cloud}/launch-dag | getLaunchDAG
[**get_output_references_using_get**](UiDropdownsControllerApi.md#get_output_references_using_get) | **GET** /cc-ui/v1/dropdown/{stackName}/output/{outputType}/references | getOutputReferences
[**get_regions_using_get**](UiDropdownsControllerApi.md#get_regions_using_get) | **GET** /cc-ui/v1/dropdown/{cloud}/regions | getRegions
[**get_release_streams_using_get**](UiDropdownsControllerApi.md#get_release_streams_using_get) | **GET** /cc-ui/v1/dropdown/releaseStreams | getReleaseStreams
[**get_resource_by_cluster_id_using_get**](UiDropdownsControllerApi.md#get_resource_by_cluster_id_using_get) | **GET** /cc-ui/v1/dropdown/cluster/{clusterId}/{resourceType}/{resourceName}/resource-info | getResourceByClusterId
[**get_resource_by_stack_using_get**](UiDropdownsControllerApi.md#get_resource_by_stack_using_get) | **GET** /cc-ui/v1/dropdown/stack/{stackName}/{resourceType}/{resourceName}/resource-info | getResourceByStack
[**get_resource_histories_by_stack_using_get**](UiDropdownsControllerApi.md#get_resource_histories_by_stack_using_get) | **GET** /cc-ui/v1/dropdown/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/resource-history | getResourceHistoriesByStack
[**get_resource_history_overview_by_stack_using_get**](UiDropdownsControllerApi.md#get_resource_history_overview_by_stack_using_get) | **GET** /cc-ui/v1/dropdown/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/resource-history-overview | getResourceHistoryOverviewByStack
[**get_role_permissions_using_get**](UiDropdownsControllerApi.md#get_role_permissions_using_get) | **GET** /cc-ui/v1/dropdown/rolePermissions/{role} | getRolePermissions
[**get_service_overview_using_get**](UiDropdownsControllerApi.md#get_service_overview_using_get) | **GET** /cc-ui/v1/dropdown/stack/{stackName}/service/{serviceName}/overview | getServiceOverview
[**sync_cluster_history_using_post**](UiDropdownsControllerApi.md#sync_cluster_history_using_post) | **POST** /cc-ui/v1/dropdown/logs/cluster/{clusterId} | syncClusterHistory
[**sync_substack_git_history_using_post**](UiDropdownsControllerApi.md#sync_substack_git_history_using_post) | **POST** /cc-ui/v1/dropdown/logs/substack | syncSubstackGitHistory

# **get_all_cluster_resources_by_stack_using_get**
> list[BlueprintFile] get_all_cluster_resources_by_stack_using_get(resource_name, resource_type, stack_name)

getAllClusterResourcesByStack

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName

try:
    # getAllClusterResourcesByStack
    api_response = api_instance.get_all_cluster_resources_by_stack_using_get(resource_name, resource_type, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_all_cluster_resources_by_stack_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **stack_name** | **str**| stackName | 

### Return type

[**list[BlueprintFile]**](BlueprintFile.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_permissions_using_get**
> list[RBACEntity] get_all_permissions_using_get()

getAllPermissions

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllPermissions
    api_response = api_instance.get_all_permissions_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_all_permissions_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RBACEntity]**](RBACEntity.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_resources_by_cluster_using_get**
> list[BlueprintFile] get_all_resources_by_cluster_using_get(cluster_id, exclude_add_ons=exclude_add_ons, include_content=include_content, include_substack=include_substack)

getAllResourcesByCluster

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
exclude_add_ons = false # bool | excludeAddOns (optional) (default to false)
include_content = false # bool | includeContent (optional) (default to false)
include_substack = true # bool | includeSubstack (optional) (default to true)

try:
    # getAllResourcesByCluster
    api_response = api_instance.get_all_resources_by_cluster_using_get(cluster_id, exclude_add_ons=exclude_add_ons, include_content=include_content, include_substack=include_substack)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_all_resources_by_cluster_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **exclude_add_ons** | **bool**| excludeAddOns | [optional] [default to false]
 **include_content** | **bool**| includeContent | [optional] [default to false]
 **include_substack** | **bool**| includeSubstack | [optional] [default to true]

### Return type

[**list[BlueprintFile]**](BlueprintFile.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_resources_by_stack_using_get**
> list[BlueprintFile] get_all_resources_by_stack_using_get(stack_name, branch=branch, exclude_add_ons=exclude_add_ons, include_content=include_content)

getAllResourcesByStack

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName
branch = 'branch_example' # str | branch (optional)
exclude_add_ons = false # bool | excludeAddOns (optional) (default to false)
include_content = false # bool | includeContent (optional) (default to false)

try:
    # getAllResourcesByStack
    api_response = api_instance.get_all_resources_by_stack_using_get(stack_name, branch=branch, exclude_add_ons=exclude_add_ons, include_content=include_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_all_resources_by_stack_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 
 **branch** | **str**| branch | [optional] 
 **exclude_add_ons** | **bool**| excludeAddOns | [optional] [default to false]
 **include_content** | **bool**| includeContent | [optional] [default to false]

### Return type

[**list[BlueprintFile]**](BlueprintFile.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_resources_for_all_cluster_of_stack_using_get**
> list[ClusterResourcesResponse] get_all_resources_for_all_cluster_of_stack_using_get(stack_name, exclude_add_ons=exclude_add_ons)

getAllResourcesForAllClusterOfStack

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName
exclude_add_ons = false # bool | excludeAddOns (optional) (default to false)

try:
    # getAllResourcesForAllClusterOfStack
    api_response = api_instance.get_all_resources_for_all_cluster_of_stack_using_get(stack_name, exclude_add_ons=exclude_add_ons)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_all_resources_for_all_cluster_of_stack_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 
 **exclude_add_ons** | **bool**| excludeAddOns | [optional] [default to false]

### Return type

[**list[ClusterResourcesResponse]**](ClusterResourcesResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_resources_using_get**
> dict(str, list[str]) get_all_resources_using_get(cluster_id, exclude_substack_resources=exclude_substack_resources)

getAllResources

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
exclude_substack_resources = false # bool | excludeSubstackResources (optional) (default to false)

try:
    # getAllResources
    api_response = api_instance.get_all_resources_using_get(cluster_id, exclude_substack_resources=exclude_substack_resources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_all_resources_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **exclude_substack_resources** | **bool**| excludeSubstackResources | [optional] [default to false]

### Return type

**dict(str, list[str])**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vcs_using_get**
> list[str] get_all_vcs_using_get()

getAllVCS

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllVCS
    api_response = api_instance.get_all_vcs_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_all_vcs_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_list_by_cluster_id_and_resource_name_using_get**
> list[str] get_application_list_by_cluster_id_and_resource_name_using_get(cluster_id, resource_type)

getApplicationListByClusterIdAndResourceName

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
resource_type = 'resource_type_example' # str | resourceType

try:
    # getApplicationListByClusterIdAndResourceName
    api_response = api_instance.get_application_list_by_cluster_id_and_resource_name_using_get(cluster_id, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_application_list_by_cluster_id_and_resource_name_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **resource_type** | **str**| resourceType | 

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_from_facets_modules_using_get**
> JsonNode get_file_from_facets_modules_using_get(file_name, path)

getFileFromFacetsModules

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
file_name = 'file_name_example' # str | fileName
path = 'path_example' # str | path

try:
    # getFileFromFacetsModules
    api_response = api_instance.get_file_from_facets_modules_using_get(file_name, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_file_from_facets_modules_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| fileName | 
 **path** | **str**| path | 

### Return type

[**JsonNode**](JsonNode.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_git_history_for_resource_using_get**
> StackGitLog get_git_history_for_resource_using_get(cluster_id, resource_name, resource_type)

getGitHistoryForResource

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # getGitHistoryForResource
    api_response = api_instance.get_git_history_for_resource_using_get(cluster_id, resource_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_git_history_for_resource_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 

### Return type

[**StackGitLog**](StackGitLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_launch_dag_using_get**
> list[BlueprintFile] get_launch_dag_using_get(cloud, cluster_id, is_dependent=is_dependent, is_provided_k8s=is_provided_k8s)

getLaunchDAG

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cloud = 'cloud_example' # str | cloud
cluster_id = 'cluster_id_example' # str | clusterId
is_dependent = false # bool | isDependent (optional) (default to false)
is_provided_k8s = false # bool | isProvidedK8s (optional) (default to false)

try:
    # getLaunchDAG
    api_response = api_instance.get_launch_dag_using_get(cloud, cluster_id, is_dependent=is_dependent, is_provided_k8s=is_provided_k8s)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_launch_dag_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud** | **str**| cloud | 
 **cluster_id** | **str**| clusterId | 
 **is_dependent** | **bool**| isDependent | [optional] [default to false]
 **is_provided_k8s** | **bool**| isProvidedK8s | [optional] [default to false]

### Return type

[**list[BlueprintFile]**](BlueprintFile.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_output_references_using_get**
> list[OutputReference] get_output_references_using_get(output_type, stack_name)

getOutputReferences

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
output_type = 'output_type_example' # str | outputType
stack_name = 'stack_name_example' # str | stackName

try:
    # getOutputReferences
    api_response = api_instance.get_output_references_using_get(output_type, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_output_references_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **output_type** | **str**| outputType | 
 **stack_name** | **str**| stackName | 

### Return type

[**list[OutputReference]**](OutputReference.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_regions_using_get**
> list[AllRegionsAndAZ] get_regions_using_get(cloud)

getRegions

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cloud = 'cloud_example' # str | cloud

try:
    # getRegions
    api_response = api_instance.get_regions_using_get(cloud)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_regions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud** | **str**| cloud | 

### Return type

[**list[AllRegionsAndAZ]**](AllRegionsAndAZ.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_streams_using_get**
> list[str] get_release_streams_using_get()

getReleaseStreams

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))

try:
    # getReleaseStreams
    api_response = api_instance.get_release_streams_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_release_streams_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_by_cluster_id_using_get**
> BlueprintFile get_resource_by_cluster_id_using_get(cluster_id, resource_name, resource_type, include_content=include_content)

getResourceByClusterId

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
include_content = false # bool | includeContent (optional) (default to false)

try:
    # getResourceByClusterId
    api_response = api_instance.get_resource_by_cluster_id_using_get(cluster_id, resource_name, resource_type, include_content=include_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_resource_by_cluster_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **include_content** | **bool**| includeContent | [optional] [default to false]

### Return type

[**BlueprintFile**](BlueprintFile.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_by_stack_using_get**
> BlueprintFile get_resource_by_stack_using_get(resource_name, resource_type, stack_name, branch=branch)

getResourceByStack

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName
branch = 'branch_example' # str | branch (optional)

try:
    # getResourceByStack
    api_response = api_instance.get_resource_by_stack_using_get(resource_name, resource_type, stack_name, branch=branch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_resource_by_stack_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **stack_name** | **str**| stackName | 
 **branch** | **str**| branch | [optional] 

### Return type

[**BlueprintFile**](BlueprintFile.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_histories_by_stack_using_get**
> list[ResourceHistory] get_resource_histories_by_stack_using_get(resource_name, resource_type, stack_name)

getResourceHistoriesByStack

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName

try:
    # getResourceHistoriesByStack
    api_response = api_instance.get_resource_histories_by_stack_using_get(resource_name, resource_type, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_resource_histories_by_stack_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **stack_name** | **str**| stackName | 

### Return type

[**list[ResourceHistory]**](ResourceHistory.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_history_overview_by_stack_using_get**
> list[ResourceHistoryOverview] get_resource_history_overview_by_stack_using_get(resource_name, resource_type, stack_name)

getResourceHistoryOverviewByStack

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName

try:
    # getResourceHistoryOverviewByStack
    api_response = api_instance.get_resource_history_overview_by_stack_using_get(resource_name, resource_type, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_resource_history_overview_by_stack_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **stack_name** | **str**| stackName | 

### Return type

[**list[ResourceHistoryOverview]**](ResourceHistoryOverview.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_permissions_using_get**
> list[RBACEntity] get_role_permissions_using_get(role)

getRolePermissions

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
role = 'role_example' # str | role

try:
    # getRolePermissions
    api_response = api_instance.get_role_permissions_using_get(role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_role_permissions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| role | 

### Return type

[**list[RBACEntity]**](RBACEntity.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_overview_using_get**
> ServiceOverview get_service_overview_using_get(service_name, stack_name)

getServiceOverview

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
service_name = 'service_name_example' # str | serviceName
stack_name = 'stack_name_example' # str | stackName

try:
    # getServiceOverview
    api_response = api_instance.get_service_overview_using_get(service_name, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->get_service_overview_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| serviceName | 
 **stack_name** | **str**| stackName | 

### Return type

[**ServiceOverview**](ServiceOverview.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_cluster_history_using_post**
> sync_cluster_history_using_post(cluster_id, force=force)

syncClusterHistory

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
force = false # bool | force (optional) (default to false)

try:
    # syncClusterHistory
    api_instance.sync_cluster_history_using_post(cluster_id, force=force)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->sync_cluster_history_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **force** | **bool**| force | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_substack_git_history_using_post**
> sync_substack_git_history_using_post(force_sync, substack_name)

syncSubstackGitHistory

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
api_instance = swagger_client.UiDropdownsControllerApi(swagger_client.ApiClient(configuration))
force_sync = true # bool | forceSync
substack_name = 'substack_name_example' # str | substackName

try:
    # syncSubstackGitHistory
    api_instance.sync_substack_git_history_using_post(force_sync, substack_name)
except ApiException as e:
    print("Exception when calling UiDropdownsControllerApi->sync_substack_git_history_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **force_sync** | **bool**| forceSync | 
 **substack_name** | **str**| substackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

