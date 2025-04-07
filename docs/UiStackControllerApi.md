# swagger_client.UiStackControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_tasks_using_post1**](UiStackControllerApi.md#create_cluster_tasks_using_post1) | **POST** /cc-ui/v1/stacks/clusterTask | createClusterTasks
[**create_project_using_post**](UiStackControllerApi.md#create_project_using_post) | **POST** /cc-ui/v1/stacks/project | createProject
[**create_stack_using_post1**](UiStackControllerApi.md#create_stack_using_post1) | **POST** /cc-ui/v1/stacks/ | createStack
[**create_stack_v2_using_post**](UiStackControllerApi.md#create_stack_v2_using_post) | **POST** /cc-ui/v1/stacks/v2 | createStackV2
[**create_starter_project_using_post**](UiStackControllerApi.md#create_starter_project_using_post) | **POST** /cc-ui/v1/stacks/starter-project | createStarterProject
[**create_sub_stack_using_post**](UiStackControllerApi.md#create_sub_stack_using_post) | **POST** /cc-ui/v1/stacks/substack/{substackName} | createSubStack
[**create_subscription_using_post1**](UiStackControllerApi.md#create_subscription_using_post1) | **POST** /cc-ui/v1/stacks/{stackName}/notification/subscriptions | createSubscription
[**delete_stack_using_delete**](UiStackControllerApi.md#delete_stack_using_delete) | **DELETE** /cc-ui/v1/stacks/{stackName} | deleteStack
[**enable_git_ops_using_put**](UiStackControllerApi.md#enable_git_ops_using_put) | **PUT** /cc-ui/v1/stacks/{stackName}/enable-git-ops | enableGitOps
[**get_all_cluster_tasks_using_get**](UiStackControllerApi.md#get_all_cluster_tasks_using_get) | **GET** /cc-ui/v1/stacks/clusterTask/{stackName} | getAllClusterTasks
[**get_all_clusters_using_get**](UiStackControllerApi.md#get_all_clusters_using_get) | **GET** /cc-ui/v1/stacks/clusters | getAllClusters
[**get_all_subscriptions_using_get1**](UiStackControllerApi.md#get_all_subscriptions_using_get1) | **GET** /cc-ui/v1/stacks/{stackName}/notification/subscriptions | getAllSubscriptions
[**get_all_template_inputs_meta_using_get**](UiStackControllerApi.md#get_all_template_inputs_meta_using_get) | **GET** /cc-ui/v1/stacks/{stackName}/templateInputs/meta | getAllTemplateInputsMeta
[**get_application_list_using_get**](UiStackControllerApi.md#get_application_list_using_get) | **GET** /cc-ui/v1/stacks/{stackName}/{resourceType}/ | getApplicationList
[**get_application_using_get1**](UiStackControllerApi.md#get_application_using_get1) | **GET** /cc-ui/v1/stacks/{stackName}/{resourceType}/{appName} | getApplication
[**get_cluster_metadata_by_stack_using_get**](UiStackControllerApi.md#get_cluster_metadata_by_stack_using_get) | **GET** /cc-ui/v1/stacks/{stackName}/clusters-metadata | getClusterMetadataByStack
[**get_clusters_overview_using_get**](UiStackControllerApi.md#get_clusters_overview_using_get) | **GET** /cc-ui/v1/stacks/{stackName}/clusters-overview | getClustersOverview
[**get_clusters_using_get1**](UiStackControllerApi.md#get_clusters_using_get1) | **GET** /cc-ui/v1/stacks/{stackName}/clusters | getClusters
[**get_clusters_with_status_using_get**](UiStackControllerApi.md#get_clusters_with_status_using_get) | **GET** /cc-ui/v1/stacks/{stackName}/clustersWithStatus | getClustersWithStatus
[**get_local_deployment_context_using_get**](UiStackControllerApi.md#get_local_deployment_context_using_get) | **GET** /cc-ui/v1/stacks/{stackName}/localDeploymentContext | getLocalDeploymentContext
[**get_overrides_using_get2**](UiStackControllerApi.md#get_overrides_using_get2) | **GET** /cc-ui/v1/stacks/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/overrides | getOverrides
[**get_resource_types_using_get**](UiStackControllerApi.md#get_resource_types_using_get) | **GET** /cc-ui/v1/stacks/{stackName}/suggestions/resourceType | getResourceTypes
[**get_resources_by_types_using_get**](UiStackControllerApi.md#get_resources_by_types_using_get) | **GET** /cc-ui/v1/stacks/{stackName}/suggestions/resourceType/{resourceType} | getResourcesByTypes
[**get_running_base_clusters_using_get**](UiStackControllerApi.md#get_running_base_clusters_using_get) | **GET** /cc-ui/v1/stacks/running-base-clusters | getRunningBaseClusters
[**get_stack_templates_using_get**](UiStackControllerApi.md#get_stack_templates_using_get) | **GET** /cc-ui/v1/stacks/templates | getStackTemplates
[**get_stack_using_get**](UiStackControllerApi.md#get_stack_using_get) | **GET** /cc-ui/v1/stacks/{stackName} | getStack
[**get_stack_with_account_using_get**](UiStackControllerApi.md#get_stack_with_account_using_get) | **GET** /cc-ui/v1/stacks/{stackName}/withAccount | getStackWithAccount
[**get_stacks_using_get1**](UiStackControllerApi.md#get_stacks_using_get1) | **GET** /cc-ui/v1/stacks/ | getStacks
[**migrate_overrides_to_git_using_get**](UiStackControllerApi.md#migrate_overrides_to_git_using_get) | **GET** /cc-ui/v1/stacks/migrate-overrides | migrateOverridesToGit
[**migrate_overrides_to_git_v2_using_post**](UiStackControllerApi.md#migrate_overrides_to_git_v2_using_post) | **POST** /cc-ui/v1/stacks/migrate-overrides-v2 | migrateOverridesToGitV2
[**reload_stack_using_get1**](UiStackControllerApi.md#reload_stack_using_get1) | **GET** /cc-ui/v1/stacks/{stackName}/reload | reloadStack
[**save_as_template_using_post**](UiStackControllerApi.md#save_as_template_using_post) | **POST** /cc-ui/v1/stacks/{stackName}/template | saveAsTemplate
[**save_as_template_v2_using_post**](UiStackControllerApi.md#save_as_template_v2_using_post) | **POST** /cc-ui/v1/stacks/{stackName}/template-v2 | saveAsTemplateV2
[**stack_sync_with_git_using_get**](UiStackControllerApi.md#stack_sync_with_git_using_get) | **GET** /cc-ui/v1/stacks/{stackName}/sync-with-git/v2 | Sync stack with git
[**sync_resources_using_get**](UiStackControllerApi.md#sync_resources_using_get) | **GET** /cc-ui/v1/stacks/{stackName}/sync-resources | syncResources
[**sync_stack_with_git_using_get**](UiStackControllerApi.md#sync_stack_with_git_using_get) | **GET** /cc-ui/v1/stacks/{stackName}/sync-with-git | syncStackWithGit
[**toggle_release_using_post1**](UiStackControllerApi.md#toggle_release_using_post1) | **POST** /cc-ui/v1/stacks/{stackName}/toggleRelease | toggleRelease
[**update_stack_using_put1**](UiStackControllerApi.md#update_stack_using_put1) | **PUT** /cc-ui/v1/stacks/{stackName} | updateStack


# **create_cluster_tasks_using_post1**
> list[ClusterTask] create_cluster_tasks_using_post1(task_request)

createClusterTasks

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
task_request = swagger_client.ClusterTaskRequest() # ClusterTaskRequest | taskRequest

try:
    # createClusterTasks
    api_response = api_instance.create_cluster_tasks_using_post1(task_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->create_cluster_tasks_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_request** | [**ClusterTaskRequest**](ClusterTaskRequest.md)| taskRequest | 

### Return type

[**list[ClusterTask]**](ClusterTask.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_using_post**
> Stack create_project_using_post(request)

createProject

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
request = swagger_client.CreateProjectRequest() # CreateProjectRequest | request

try:
    # createProject
    api_response = api_instance.create_project_using_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->create_project_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateProjectRequest**](CreateProjectRequest.md)| request | 

### Return type

[**Stack**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stack_using_post1**
> Stack create_stack_using_post1(stack)

createStack

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack = swagger_client.Stack() # Stack | stack

try:
    # createStack
    api_response = api_instance.create_stack_using_post1(stack)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->create_stack_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | [**Stack**](Stack.md)| stack | 

### Return type

[**Stack**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stack_v2_using_post**
> Stack create_stack_v2_using_post(create_blueprint_request)

createStackV2

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
create_blueprint_request = swagger_client.CreateBlueprintRequest() # CreateBlueprintRequest | createBlueprintRequest

try:
    # createStackV2
    api_response = api_instance.create_stack_v2_using_post(create_blueprint_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->create_stack_v2_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_blueprint_request** | [**CreateBlueprintRequest**](CreateBlueprintRequest.md)| createBlueprintRequest | 

### Return type

[**Stack**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_starter_project_using_post**
> Stack create_starter_project_using_post()

createStarterProject

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))

try:
    # createStarterProject
    api_response = api_instance.create_starter_project_using_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->create_starter_project_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Stack**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sub_stack_using_post**
> Substack create_sub_stack_using_post(sub_stack, substack_name)

createSubStack

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
sub_stack = swagger_client.SubstackRequest() # SubstackRequest | subStack
substack_name = 'substack_name_example' # str | substackName

try:
    # createSubStack
    api_response = api_instance.create_sub_stack_using_post(sub_stack, substack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->create_sub_stack_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_stack** | [**SubstackRequest**](SubstackRequest.md)| subStack | 
 **substack_name** | **str**| substackName | 

### Return type

[**Substack**](Substack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription_using_post1**
> Subscription create_subscription_using_post1(stack_name, subscription)

createSubscription

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName
subscription = swagger_client.Subscription() # Subscription | subscription

try:
    # createSubscription
    api_response = api_instance.create_subscription_using_post1(stack_name, subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->create_subscription_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 
 **subscription** | [**Subscription**](Subscription.md)| subscription | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stack_using_delete**
> Stack delete_stack_using_delete(stack_name)

deleteStack

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # deleteStack
    api_response = api_instance.delete_stack_using_delete(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->delete_stack_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**Stack**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_git_ops_using_put**
> Stack enable_git_ops_using_put(request, stack_name)

enableGitOps

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
request = swagger_client.EnableGitOpsRequest() # EnableGitOpsRequest | request
stack_name = 'stack_name_example' # str | stackName

try:
    # enableGitOps
    api_response = api_instance.enable_git_ops_using_put(request, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->enable_git_ops_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**EnableGitOpsRequest**](EnableGitOpsRequest.md)| request | 
 **stack_name** | **str**| stackName | 

### Return type

[**Stack**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_cluster_tasks_using_get**
> list[ClusterTask] get_all_cluster_tasks_using_get(stack_name)

getAllClusterTasks

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getAllClusterTasks
    api_response = api_instance.get_all_cluster_tasks_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_all_cluster_tasks_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**list[ClusterTask]**](ClusterTask.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_clusters_using_get**
> PageAbstractCluster get_all_clusters_using_get(page=page, per_page=per_page, sort_by=sort_by)

getAllClusters

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
page = 0 # int | page (optional) (default to 0)
per_page = 50 # int | perPage (optional) (default to 50)
sort_by = 'lastModifiedDate' # str | sortBy (optional) (default to lastModifiedDate)

try:
    # getAllClusters
    api_response = api_instance.get_all_clusters_using_get(page=page, per_page=per_page, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_all_clusters_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page | [optional] [default to 0]
 **per_page** | **int**| perPage | [optional] [default to 50]
 **sort_by** | **str**| sortBy | [optional] [default to lastModifiedDate]

### Return type

[**PageAbstractCluster**](PageAbstractCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_subscriptions_using_get1**
> list[Subscription] get_all_subscriptions_using_get1(stack_name)

getAllSubscriptions

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getAllSubscriptions
    api_response = api_instance.get_all_subscriptions_using_get1(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_all_subscriptions_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_inputs_meta_using_get**
> object get_all_template_inputs_meta_using_get(stack_name)

getAllTemplateInputsMeta

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getAllTemplateInputsMeta
    api_response = api_instance.get_all_template_inputs_meta_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_all_template_inputs_meta_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_list_using_get**
> list[str] get_application_list_using_get(resource_type, stack_name)

getApplicationList

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName

try:
    # getApplicationList
    api_response = api_instance.get_application_list_using_get(resource_type, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_application_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| resourceType | 
 **stack_name** | **str**| stackName | 

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_using_get1**
> object get_application_using_get1(app_name, resource_type, stack_name)

getApplication

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
app_name = 'app_name_example' # str | appName
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName

try:
    # getApplication
    api_response = api_instance.get_application_using_get1(app_name, resource_type, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_application_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| appName | 
 **resource_type** | **str**| resourceType | 
 **stack_name** | **str**| stackName | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_metadata_by_stack_using_get**
> list[ClusterMetadata] get_cluster_metadata_by_stack_using_get(stack_name)

getClusterMetadataByStack

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getClusterMetadataByStack
    api_response = api_instance.get_cluster_metadata_by_stack_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_cluster_metadata_by_stack_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**list[ClusterMetadata]**](ClusterMetadata.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters_overview_using_get**
> list[ClusterOverview] get_clusters_overview_using_get(stack_name)

getClustersOverview

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getClustersOverview
    api_response = api_instance.get_clusters_overview_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_clusters_overview_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**list[ClusterOverview]**](ClusterOverview.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters_using_get1**
> list[AbstractCluster] get_clusters_using_get1(stack_name)

getClusters

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getClusters
    api_response = api_instance.get_clusters_using_get1(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_clusters_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**list[AbstractCluster]**](AbstractCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters_with_status_using_get**
> list[AbstractCluster] get_clusters_with_status_using_get(stack_name)

getClustersWithStatus

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getClustersWithStatus
    api_response = api_instance.get_clusters_with_status_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_clusters_with_status_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**list[AbstractCluster]**](AbstractCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_local_deployment_context_using_get**
> DeploymentContext get_local_deployment_context_using_get(stack_name)

getLocalDeploymentContext

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getLocalDeploymentContext
    api_response = api_instance.get_local_deployment_context_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_local_deployment_context_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**DeploymentContext**](DeploymentContext.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overrides_using_get2**
> list[ClusterOverrideResponse] get_overrides_using_get2(resource_name, resource_type, stack_name)

getOverrides

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName

try:
    # getOverrides
    api_response = api_instance.get_overrides_using_get2(resource_name, resource_type, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_overrides_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **stack_name** | **str**| stackName | 

### Return type

[**list[ClusterOverrideResponse]**](ClusterOverrideResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_types_using_get**
> list[str] get_resource_types_using_get(stack_name)

getResourceTypes

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getResourceTypes
    api_response = api_instance.get_resource_types_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_resource_types_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources_by_types_using_get**
> list[str] get_resources_by_types_using_get(resource_type, stack_name)

getResourcesByTypes

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName

try:
    # getResourcesByTypes
    api_response = api_instance.get_resources_by_types_using_get(resource_type, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_resources_by_types_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| resourceType | 
 **stack_name** | **str**| stackName | 

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_running_base_clusters_using_get**
> list[AbstractCluster] get_running_base_clusters_using_get()

getRunningBaseClusters

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))

try:
    # getRunningBaseClusters
    api_response = api_instance.get_running_base_clusters_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_running_base_clusters_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AbstractCluster]**](AbstractCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stack_templates_using_get**
> list[StackTemplate] get_stack_templates_using_get()

getStackTemplates

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))

try:
    # getStackTemplates
    api_response = api_instance.get_stack_templates_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_stack_templates_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[StackTemplate]**](StackTemplate.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stack_using_get**
> Stack get_stack_using_get(stack_name)

getStack

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getStack
    api_response = api_instance.get_stack_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_stack_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**Stack**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stack_with_account_using_get**
> Stack get_stack_with_account_using_get(stack_name)

getStackWithAccount

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getStackWithAccount
    api_response = api_instance.get_stack_with_account_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_stack_with_account_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**Stack**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stacks_using_get1**
> list[Stack] get_stacks_using_get1()

getStacks

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))

try:
    # getStacks
    api_response = api_instance.get_stacks_using_get1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_stacks_using_get1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Stack]**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_overrides_to_git_using_get**
> migrate_overrides_to_git_using_get(stack_name)

migrateOverridesToGit

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # migrateOverridesToGit
    api_instance.migrate_overrides_to_git_using_get(stack_name)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->migrate_overrides_to_git_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_overrides_to_git_v2_using_post**
> migrate_overrides_to_git_v2_using_post(migrate_overrides_request)

migrateOverridesToGitV2

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
migrate_overrides_request = swagger_client.MigrateOverridesRequest() # MigrateOverridesRequest | migrateOverridesRequest

try:
    # migrateOverridesToGitV2
    api_instance.migrate_overrides_to_git_v2_using_post(migrate_overrides_request)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->migrate_overrides_to_git_v2_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migrate_overrides_request** | [**MigrateOverridesRequest**](MigrateOverridesRequest.md)| migrateOverridesRequest | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_stack_using_get1**
> Stack reload_stack_using_get1(stack_name)

reloadStack

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # reloadStack
    api_response = api_instance.reload_stack_using_get1(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->reload_stack_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**Stack**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as_template_using_post**
> Stack save_as_template_using_post(create_template_request, stack_name)

saveAsTemplate

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
create_template_request = swagger_client.CreateTemplateRequest() # CreateTemplateRequest | createTemplateRequest
stack_name = 'stack_name_example' # str | stackName

try:
    # saveAsTemplate
    api_response = api_instance.save_as_template_using_post(create_template_request, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->save_as_template_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_template_request** | [**CreateTemplateRequest**](CreateTemplateRequest.md)| createTemplateRequest | 
 **stack_name** | **str**| stackName | 

### Return type

[**Stack**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as_template_v2_using_post**
> Stack save_as_template_v2_using_post(save_as_template_request, stack_name)

saveAsTemplateV2

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
save_as_template_request = swagger_client.SaveAsTemplateRequest() # SaveAsTemplateRequest | saveAsTemplateRequest
stack_name = 'stack_name_example' # str | stackName

try:
    # saveAsTemplateV2
    api_response = api_instance.save_as_template_v2_using_post(save_as_template_request, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->save_as_template_v2_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_as_template_request** | [**SaveAsTemplateRequest**](SaveAsTemplateRequest.md)| saveAsTemplateRequest | 
 **stack_name** | **str**| stackName | 

### Return type

[**Stack**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_sync_with_git_using_get**
> stack_sync_with_git_using_get(stack_name)

Sync stack with git

Use this to sync stack with git. Runs synchronously for the stack, and then does a non-force sync of all clusters in async

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # Sync stack with git
    api_instance.stack_sync_with_git_using_get(stack_name)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->stack_sync_with_git_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_resources_using_get**
> sync_resources_using_get(stack_name)

syncResources

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # syncResources
    api_instance.sync_resources_using_get(stack_name)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->sync_resources_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_stack_with_git_using_get**
> sync_stack_with_git_using_get(stack_name)

syncStackWithGit

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # syncStackWithGit
    api_instance.sync_stack_with_git_using_get(stack_name)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->sync_stack_with_git_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_release_using_post1**
> ToggleRelease toggle_release_using_post1(stack_name, toggle_release)

toggleRelease

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName
toggle_release = swagger_client.ToggleRelease() # ToggleRelease | toggleRelease

try:
    # toggleRelease
    api_response = api_instance.toggle_release_using_post1(stack_name, toggle_release)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->toggle_release_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 
 **toggle_release** | [**ToggleRelease**](ToggleRelease.md)| toggleRelease | 

### Return type

[**ToggleRelease**](ToggleRelease.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack_using_put1**
> Stack update_stack_using_put1(stack, stack_name)

updateStack

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack = swagger_client.Stack() # Stack | stack
stack_name = 'stack_name_example' # str | stackName

try:
    # updateStack
    api_response = api_instance.update_stack_using_put1(stack, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->update_stack_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack** | [**Stack**](Stack.md)| stack | 
 **stack_name** | **str**| stackName | 

### Return type

[**Stack**](Stack.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

