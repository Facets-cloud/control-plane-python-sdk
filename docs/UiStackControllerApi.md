# swagger_client.UiStackControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](UiStackControllerApi.md#create_project) | **POST** /cc-ui/v1/stacks/project | 
[**create_stack**](UiStackControllerApi.md#create_stack) | **POST** /cc-ui/v1/stacks/ | 
[**create_stack_v2**](UiStackControllerApi.md#create_stack_v2) | **POST** /cc-ui/v1/stacks/v2 | 
[**create_starter_project**](UiStackControllerApi.md#create_starter_project) | **POST** /cc-ui/v1/stacks/starter-project | 
[**create_sub_stack**](UiStackControllerApi.md#create_sub_stack) | **POST** /cc-ui/v1/stacks/substack/{substackName} | 
[**create_subscription**](UiStackControllerApi.md#create_subscription) | **POST** /cc-ui/v1/stacks/{stackName}/notification/subscriptions | 
[**delete_overrides_fields**](UiStackControllerApi.md#delete_overrides_fields) | **DELETE** /cc-ui/v1/stacks/{stackName}/overrides-fields | 
[**delete_stack**](UiStackControllerApi.md#delete_stack) | **DELETE** /cc-ui/v1/stacks/{stackName} | 
[**enable_git_ops**](UiStackControllerApi.md#enable_git_ops) | **PUT** /cc-ui/v1/stacks/{stackName}/enable-git-ops | 
[**get_all_clusters**](UiStackControllerApi.md#get_all_clusters) | **GET** /cc-ui/v1/stacks/clusters | 
[**get_all_subscriptions**](UiStackControllerApi.md#get_all_subscriptions) | **GET** /cc-ui/v1/stacks/{stackName}/notification/subscriptions | 
[**get_all_template_inputs_meta**](UiStackControllerApi.md#get_all_template_inputs_meta) | **GET** /cc-ui/v1/stacks/{stackName}/templateInputs/meta | 
[**get_application**](UiStackControllerApi.md#get_application) | **GET** /cc-ui/v1/stacks/{stackName}/{resourceType}/{appName} | 
[**get_application_list**](UiStackControllerApi.md#get_application_list) | **GET** /cc-ui/v1/stacks/{stackName}/{resourceType}/ | 
[**get_cluster_metadata_by_stack**](UiStackControllerApi.md#get_cluster_metadata_by_stack) | **GET** /cc-ui/v1/stacks/{stackName}/clusters-metadata | 
[**get_clusters**](UiStackControllerApi.md#get_clusters) | **GET** /cc-ui/v1/stacks/{stackName}/clusters | 
[**get_clusters_overview**](UiStackControllerApi.md#get_clusters_overview) | **GET** /cc-ui/v1/stacks/{stackName}/clusters-overview | 
[**get_clusters_with_status**](UiStackControllerApi.md#get_clusters_with_status) | **GET** /cc-ui/v1/stacks/{stackName}/clustersWithStatus | 
[**get_local_deployment_context**](UiStackControllerApi.md#get_local_deployment_context) | **GET** /cc-ui/v1/stacks/{stackName}/localDeploymentContext | 
[**get_overrides**](UiStackControllerApi.md#get_overrides) | **GET** /cc-ui/v1/stacks/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/overrides | 
[**get_resource_types**](UiStackControllerApi.md#get_resource_types) | **GET** /cc-ui/v1/stacks/{stackName}/suggestions/resourceType | 
[**get_resources_by_types**](UiStackControllerApi.md#get_resources_by_types) | **GET** /cc-ui/v1/stacks/{stackName}/suggestions/resourceType/{resourceType} | 
[**get_running_base_clusters**](UiStackControllerApi.md#get_running_base_clusters) | **GET** /cc-ui/v1/stacks/running-base-clusters | 
[**get_stack**](UiStackControllerApi.md#get_stack) | **GET** /cc-ui/v1/stacks/{stackName} | 
[**get_stack_templates**](UiStackControllerApi.md#get_stack_templates) | **GET** /cc-ui/v1/stacks/templates | 
[**get_stack_with_account**](UiStackControllerApi.md#get_stack_with_account) | **GET** /cc-ui/v1/stacks/{stackName}/withAccount | 
[**get_stacks**](UiStackControllerApi.md#get_stacks) | **GET** /cc-ui/v1/stacks/ | 
[**migrate_overrides_to_git**](UiStackControllerApi.md#migrate_overrides_to_git) | **GET** /cc-ui/v1/stacks/migrate-overrides | 
[**migrate_overrides_to_git_v2**](UiStackControllerApi.md#migrate_overrides_to_git_v2) | **POST** /cc-ui/v1/stacks/migrate-overrides-v2 | 
[**reload_stack**](UiStackControllerApi.md#reload_stack) | **GET** /cc-ui/v1/stacks/{stackName}/reload | 
[**save_as_template**](UiStackControllerApi.md#save_as_template) | **POST** /cc-ui/v1/stacks/{stackName}/template | 
[**save_as_template_v2**](UiStackControllerApi.md#save_as_template_v2) | **POST** /cc-ui/v1/stacks/{stackName}/template-v2 | 
[**stack_sync_with_git**](UiStackControllerApi.md#stack_sync_with_git) | **GET** /cc-ui/v1/stacks/{stackName}/sync-with-git/v2 | Sync stack with git
[**sync_resources**](UiStackControllerApi.md#sync_resources) | **GET** /cc-ui/v1/stacks/{stackName}/sync-resources | 
[**sync_stack_with_git**](UiStackControllerApi.md#sync_stack_with_git) | **GET** /cc-ui/v1/stacks/{stackName}/sync-with-git | 
[**toggle_release**](UiStackControllerApi.md#toggle_release) | **POST** /cc-ui/v1/stacks/{stackName}/toggleRelease | 
[**update_stack**](UiStackControllerApi.md#update_stack) | **PUT** /cc-ui/v1/stacks/{stackName} | 

# **create_project**
> Stack create_project(body)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateProjectRequest() # CreateProjectRequest | 

try:
    api_response = api_instance.create_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProjectRequest**](CreateProjectRequest.md)|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stack**
> Stack create_stack(body)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Stack() # Stack | 

try:
    api_response = api_instance.create_stack(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->create_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Stack**](Stack.md)|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stack_v2**
> Stack create_stack_v2(body)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateBlueprintRequest() # CreateBlueprintRequest | 

try:
    api_response = api_instance.create_stack_v2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->create_stack_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBlueprintRequest**](CreateBlueprintRequest.md)|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_starter_project**
> Stack create_starter_project()



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.create_starter_project()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->create_starter_project: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Stack**](Stack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sub_stack**
> Substack create_sub_stack(body, substack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.SubstackRequest() # SubstackRequest | 
substack_name = 'substack_name_example' # str | 

try:
    api_response = api_instance.create_sub_stack(body, substack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->create_sub_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubstackRequest**](SubstackRequest.md)|  | 
 **substack_name** | **str**|  | 

### Return type

[**Substack**](Substack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription**
> Subscription create_subscription(body, stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Subscription() # Subscription | 
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.create_subscription(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Subscription**](Subscription.md)|  | 
 **stack_name** | **str**|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_overrides_fields**
> list[OverrideObject] delete_overrides_fields(body, stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.OverrideDeleteRequest() # OverrideDeleteRequest | 
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.delete_overrides_fields(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->delete_overrides_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OverrideDeleteRequest**](OverrideDeleteRequest.md)|  | 
 **stack_name** | **str**|  | 

### Return type

[**list[OverrideObject]**](OverrideObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stack**
> Stack delete_stack(stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.delete_stack(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->delete_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_git_ops**
> Stack enable_git_ops(body, stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.EnableGitOpsRequest() # EnableGitOpsRequest | 
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.enable_git_ops(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->enable_git_ops: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnableGitOpsRequest**](EnableGitOpsRequest.md)|  | 
 **stack_name** | **str**|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_clusters**
> PageAbstractCluster get_all_clusters(page=page, per_page=per_page, sort_by=sort_by)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
page = 0 # int |  (optional) (default to 0)
per_page = 50 # int |  (optional) (default to 50)
sort_by = 'LAST_MODIFIED_DATE' # str |  (optional) (default to LAST_MODIFIED_DATE)

try:
    api_response = api_instance.get_all_clusters(page=page, per_page=per_page, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_all_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **per_page** | **int**|  | [optional] [default to 50]
 **sort_by** | **str**|  | [optional] [default to LAST_MODIFIED_DATE]

### Return type

[**PageAbstractCluster**](PageAbstractCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_subscriptions**
> list[Subscription] get_all_subscriptions(stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_all_subscriptions(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_all_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_template_inputs_meta**
> dict(str, object) get_all_template_inputs_meta(stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_all_template_inputs_meta(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_all_template_inputs_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

**dict(str, object)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> dict(str, object) get_application(stack_name, app_name, resource_type)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
app_name = 'app_name_example' # str | 
resource_type = 'resource_type_example' # str | 

try:
    api_response = api_instance.get_application(stack_name, app_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **app_name** | **str**|  | 
 **resource_type** | **str**|  | 

### Return type

**dict(str, object)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_list**
> list[str] get_application_list(stack_name, resource_type)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
resource_type = 'resource_type_example' # str | 

try:
    api_response = api_instance.get_application_list(stack_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_application_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **resource_type** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_metadata_by_stack**
> list[ClusterMetadata] get_cluster_metadata_by_stack(stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_cluster_metadata_by_stack(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_cluster_metadata_by_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**list[ClusterMetadata]**](ClusterMetadata.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters**
> list[AbstractCluster] get_clusters(stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_clusters(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**list[AbstractCluster]**](AbstractCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters_overview**
> list[ClusterOverview] get_clusters_overview(stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_clusters_overview(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_clusters_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**list[ClusterOverview]**](ClusterOverview.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters_with_status**
> list[AbstractCluster] get_clusters_with_status(stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_clusters_with_status(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_clusters_with_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**list[AbstractCluster]**](AbstractCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_local_deployment_context**
> DeploymentContext get_local_deployment_context(stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_local_deployment_context(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_local_deployment_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**DeploymentContext**](DeploymentContext.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overrides**
> list[ClusterOverrideResponse] get_overrides(stack_name, resource_type, resource_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.get_overrides(stack_name, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_overrides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

[**list[ClusterOverrideResponse]**](ClusterOverrideResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_types**
> list[str] get_resource_types(stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_resource_types(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_resource_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources_by_types**
> list[str] get_resources_by_types(stack_name, resource_type)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
resource_type = 'resource_type_example' # str | 

try:
    api_response = api_instance.get_resources_by_types(stack_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_resources_by_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **resource_type** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_running_base_clusters**
> list[AbstractCluster] get_running_base_clusters()



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_running_base_clusters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_running_base_clusters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AbstractCluster]**](AbstractCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stack**
> Stack get_stack(stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_stack(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stack_templates**
> list[StackTemplate] get_stack_templates()



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_stack_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_stack_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[StackTemplate]**](StackTemplate.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stack_with_account**
> Stack get_stack_with_account(stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_stack_with_account(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_stack_with_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stacks**
> list[Stack] get_stacks()



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_stacks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->get_stacks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Stack]**](Stack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_overrides_to_git**
> migrate_overrides_to_git(stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_instance.migrate_overrides_to_git(stack_name)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->migrate_overrides_to_git: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_overrides_to_git_v2**
> migrate_overrides_to_git_v2(body)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.MigrateOverridesRequest() # MigrateOverridesRequest | 

try:
    api_instance.migrate_overrides_to_git_v2(body)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->migrate_overrides_to_git_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrateOverridesRequest**](MigrateOverridesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_stack**
> Stack reload_stack(stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.reload_stack(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->reload_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as_template**
> Stack save_as_template(body, stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateTemplateRequest() # CreateTemplateRequest | 
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.save_as_template(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->save_as_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTemplateRequest**](CreateTemplateRequest.md)|  | 
 **stack_name** | **str**|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_as_template_v2**
> Stack save_as_template_v2(body, stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.SaveAsTemplateRequest() # SaveAsTemplateRequest | 
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.save_as_template_v2(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->save_as_template_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SaveAsTemplateRequest**](SaveAsTemplateRequest.md)|  | 
 **stack_name** | **str**|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_sync_with_git**
> stack_sync_with_git(stack_name)

Sync stack with git

Use this to sync stack with git. Runs synchronously for the stack, and then does a non-force sync of all clusters in async

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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    # Sync stack with git
    api_instance.stack_sync_with_git(stack_name)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->stack_sync_with_git: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_resources**
> sync_resources(stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_instance.sync_resources(stack_name)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->sync_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_stack_with_git**
> sync_stack_with_git(stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_instance.sync_stack_with_git(stack_name)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->sync_stack_with_git: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_release**
> ToggleRelease toggle_release(body, stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ToggleRelease() # ToggleRelease | 
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.toggle_release(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->toggle_release: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ToggleRelease**](ToggleRelease.md)|  | 
 **stack_name** | **str**|  | 

### Return type

[**ToggleRelease**](ToggleRelease.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack**
> Stack update_stack(body, stack_name)



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
api_instance = swagger_client.UiStackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Stack() # Stack | 
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.update_stack(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiStackControllerApi->update_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Stack**](Stack.md)|  | 
 **stack_name** | **str**|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

