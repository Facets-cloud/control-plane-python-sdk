# swagger_client.UiBlueprintDesignerControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_variables_using_post**](UiBlueprintDesignerControllerApi.md#add_variables_using_post) | **POST** /cc-ui/v1/designer/{stackName}/variables | addVariables
[**apply_template_using_post**](UiBlueprintDesignerControllerApi.md#apply_template_using_post) | **POST** /cc-ui/v1/designer/{stackName}/{templateName}/apply | applyTemplate
[**bulk_edit_disabled_for_resources_using_put**](UiBlueprintDesignerControllerApi.md#bulk_edit_disabled_for_resources_using_put) | **PUT** /cc-ui/v1/designer/{stackName}/branch/{branch}/resource-enable-disable | bulkEditDisabledForResources
[**bulk_edit_disabled_for_resources_using_put1**](UiBlueprintDesignerControllerApi.md#bulk_edit_disabled_for_resources_using_put1) | **PUT** /cc-ui/v1/designer/{stackName}/resource-enable-disable | bulkEditDisabledForResources
[**create_branch_using_post**](UiBlueprintDesignerControllerApi.md#create_branch_using_post) | **POST** /cc-ui/v1/designer/{stackName}/{branch}/create-branch | createBranch
[**create_resources_using_post**](UiBlueprintDesignerControllerApi.md#create_resources_using_post) | **POST** /cc-ui/v1/designer/{stackName}/branch/{branch} | createResources
[**create_resources_using_post1**](UiBlueprintDesignerControllerApi.md#create_resources_using_post1) | **POST** /cc-ui/v1/designer/{stackName} | createResources
[**delete_resources_using_delete**](UiBlueprintDesignerControllerApi.md#delete_resources_using_delete) | **DELETE** /cc-ui/v1/designer/{stackName}/branch/{branch} | deleteResources
[**delete_resources_using_delete1**](UiBlueprintDesignerControllerApi.md#delete_resources_using_delete1) | **DELETE** /cc-ui/v1/designer/{stackName} | deleteResources
[**delete_variables_using_delete**](UiBlueprintDesignerControllerApi.md#delete_variables_using_delete) | **DELETE** /cc-ui/v1/designer/{stackName}/variables | deleteVariables
[**get_add_on_modules_using_get**](UiBlueprintDesignerControllerApi.md#get_add_on_modules_using_get) | **GET** /cc-ui/v1/designer/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/add-ons | Get add ons for this resource
[**get_autocomplete_data_using_get**](UiBlueprintDesignerControllerApi.md#get_autocomplete_data_using_get) | **GET** /cc-ui/v1/designer/{stackName}/ref-autocomplete-data | getAutocompleteData
[**get_designer_resources_using_get**](UiBlueprintDesignerControllerApi.md#get_designer_resources_using_get) | **GET** /cc-ui/v1/designer/{stackName}/{branchName}/files | getDesignerResources
[**get_module_inputs_using_get**](UiBlueprintDesignerControllerApi.md#get_module_inputs_using_get) | **GET** /cc-ui/v1/designer/{stackName}/intent/{intent}/flavor/{flavor}/input | getModuleInputs
[**get_pull_requests_using_get**](UiBlueprintDesignerControllerApi.md#get_pull_requests_using_get) | **GET** /cc-ui/v1/designer/{stackName}/pulls | getPullRequests
[**get_pull_requests_using_get1**](UiBlueprintDesignerControllerApi.md#get_pull_requests_using_get1) | **GET** /cc-ui/v1/designer/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/pulls | getPullRequests
[**get_schema_metadata_using_get**](UiBlueprintDesignerControllerApi.md#get_schema_metadata_using_get) | **GET** /cc-ui/v1/designer/facets-components | getSchemaMetadata
[**get_workflow_runs_using_get**](UiBlueprintDesignerControllerApi.md#get_workflow_runs_using_get) | **GET** /cc-ui/v1/designer/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/workflow-runs | getWorkflowRuns
[**get_workflow_runs_using_get1**](UiBlueprintDesignerControllerApi.md#get_workflow_runs_using_get1) | **GET** /cc-ui/v1/designer/{stackName}/workflow-runs | getWorkflowRuns
[**get_workflows_using_get**](UiBlueprintDesignerControllerApi.md#get_workflows_using_get) | **GET** /cc-ui/v1/designer/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/workflows | getWorkflows
[**get_workflows_using_get1**](UiBlueprintDesignerControllerApi.md#get_workflows_using_get1) | **GET** /cc-ui/v1/designer/{stackName}/workflows | getWorkflows
[**list_branches_using_get**](UiBlueprintDesignerControllerApi.md#list_branches_using_get) | **GET** /cc-ui/v1/designer/{stackName}/branch-list | listBranches
[**list_branches_using_get1**](UiBlueprintDesignerControllerApi.md#list_branches_using_get1) | **GET** /cc-ui/v1/designer/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/branch-list | listBranches
[**rename_resource_using_put**](UiBlueprintDesignerControllerApi.md#rename_resource_using_put) | **PUT** /cc-ui/v1/designer/{stackName}/branch/{branch}/rename | renameResource
[**rename_resource_using_put1**](UiBlueprintDesignerControllerApi.md#rename_resource_using_put1) | **PUT** /cc-ui/v1/designer/{stackName}/rename | renameResource
[**sync_specified_blueprints_with_templates_using_post**](UiBlueprintDesignerControllerApi.md#sync_specified_blueprints_with_templates_using_post) | **POST** /cc-ui/v1/designer/{templateName}/sync | syncSpecifiedBlueprintsWithTemplates
[**update_resources_using_put**](UiBlueprintDesignerControllerApi.md#update_resources_using_put) | **PUT** /cc-ui/v1/designer/{stackName}/branch/{branch} | updateResources
[**update_resources_using_put1**](UiBlueprintDesignerControllerApi.md#update_resources_using_put1) | **PUT** /cc-ui/v1/designer/{stackName} | updateResources
[**update_variables_using_put**](UiBlueprintDesignerControllerApi.md#update_variables_using_put) | **PUT** /cc-ui/v1/designer/{stackName}/variables | updateVariables

# **add_variables_using_post**
> add_variables_using_post(body, stack_name)

addVariables

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, VariableDetails) | variables
stack_name = 'stack_name_example' # str | stackName

try:
    # addVariables
    api_instance.add_variables_using_post(body, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->add_variables_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, VariableDetails)**](dict.md)| variables | 
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_template_using_post**
> apply_template_using_post(stack_name, template_name, prefix=prefix, suffix=suffix)

applyTemplate

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName
template_name = 'template_name_example' # str | templateName
prefix = 'prefix_example' # str | prefix (optional)
suffix = 'suffix_example' # str | suffix (optional)

try:
    # applyTemplate
    api_instance.apply_template_using_post(stack_name, template_name, prefix=prefix, suffix=suffix)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->apply_template_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 
 **template_name** | **str**| templateName | 
 **prefix** | **str**| prefix | [optional] 
 **suffix** | **str**| suffix | [optional] 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_edit_disabled_for_resources_using_put**
> bulk_edit_disabled_for_resources_using_put(body, branch, stack_name)

bulkEditDisabledForResources

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ResourceEnableDisableRequest()] # list[ResourceEnableDisableRequest] | resourceEnableDisableRequestList
branch = 'branch_example' # str | branch
stack_name = 'stack_name_example' # str | stackName

try:
    # bulkEditDisabledForResources
    api_instance.bulk_edit_disabled_for_resources_using_put(body, branch, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->bulk_edit_disabled_for_resources_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ResourceEnableDisableRequest]**](ResourceEnableDisableRequest.md)| resourceEnableDisableRequestList | 
 **branch** | **str**| branch | 
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_edit_disabled_for_resources_using_put1**
> bulk_edit_disabled_for_resources_using_put1(body, stack_name)

bulkEditDisabledForResources

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ResourceEnableDisableRequest()] # list[ResourceEnableDisableRequest] | resourceEnableDisableRequestList
stack_name = 'stack_name_example' # str | stackName

try:
    # bulkEditDisabledForResources
    api_instance.bulk_edit_disabled_for_resources_using_put1(body, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->bulk_edit_disabled_for_resources_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ResourceEnableDisableRequest]**](ResourceEnableDisableRequest.md)| resourceEnableDisableRequestList | 
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_branch_using_post**
> create_branch_using_post(branch, stack_name)

createBranch

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
branch = 'branch_example' # str | branch
stack_name = 'stack_name_example' # str | stackName

try:
    # createBranch
    api_instance.create_branch_using_post(branch, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->create_branch_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**| branch | 
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_resources_using_post**
> create_resources_using_post(body, branch, stack_name)

createResources

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ResourceFileRequest()] # list[ResourceFileRequest] | resourceFileRequests
branch = 'branch_example' # str | branch
stack_name = 'stack_name_example' # str | stackName

try:
    # createResources
    api_instance.create_resources_using_post(body, branch, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->create_resources_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ResourceFileRequest]**](ResourceFileRequest.md)| resourceFileRequests | 
 **branch** | **str**| branch | 
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_resources_using_post1**
> create_resources_using_post1(body, stack_name)

createResources

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ResourceFileRequest()] # list[ResourceFileRequest] | resourceFileRequests
stack_name = 'stack_name_example' # str | stackName

try:
    # createResources
    api_instance.create_resources_using_post1(body, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->create_resources_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ResourceFileRequest]**](ResourceFileRequest.md)| resourceFileRequests | 
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resources_using_delete**
> delete_resources_using_delete(body, branch, stack_name)

deleteResources

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ResourceFileRequest()] # list[ResourceFileRequest] | resourceFileRequests
branch = 'branch_example' # str | branch
stack_name = 'stack_name_example' # str | stackName

try:
    # deleteResources
    api_instance.delete_resources_using_delete(body, branch, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->delete_resources_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ResourceFileRequest]**](ResourceFileRequest.md)| resourceFileRequests | 
 **branch** | **str**| branch | 
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resources_using_delete1**
> delete_resources_using_delete1(body, stack_name)

deleteResources

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ResourceFileRequest()] # list[ResourceFileRequest] | resourceFileRequests
stack_name = 'stack_name_example' # str | stackName

try:
    # deleteResources
    api_instance.delete_resources_using_delete1(body, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->delete_resources_using_delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ResourceFileRequest]**](ResourceFileRequest.md)| resourceFileRequests | 
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_variables_using_delete**
> delete_variables_using_delete(body, stack_name)

deleteVariables

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | variables
stack_name = 'stack_name_example' # str | stackName

try:
    # deleteVariables
    api_instance.delete_variables_using_delete(body, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->delete_variables_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| variables | 
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_add_on_modules_using_get**
> list[AddOnDTO] get_add_on_modules_using_get(resource_name, resource_type, stack_name, cloud=cloud)

Get add ons for this resource

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName
cloud = 'cloud_example' # str | cloud (optional)

try:
    # Get add ons for this resource
    api_response = api_instance.get_add_on_modules_using_get(resource_name, resource_type, stack_name, cloud=cloud)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_add_on_modules_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **stack_name** | **str**| stackName | 
 **cloud** | **str**| cloud | [optional] 

### Return type

[**list[AddOnDTO]**](AddOnDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_autocomplete_data_using_get**
> AutocompleteResponse get_autocomplete_data_using_get(stack_name)

getAutocompleteData

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getAutocompleteData
    api_response = api_instance.get_autocomplete_data_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_autocomplete_data_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**AutocompleteResponse**](AutocompleteResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_designer_resources_using_get**
> list[BlueprintFile] get_designer_resources_using_get(branch_name, stack_name)

getDesignerResources

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
branch_name = 'branch_name_example' # str | branchName
stack_name = 'stack_name_example' # str | stackName

try:
    # getDesignerResources
    api_response = api_instance.get_designer_resources_using_get(branch_name, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_designer_resources_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_name** | **str**| branchName | 
 **stack_name** | **str**| stackName | 

### Return type

[**list[BlueprintFile]**](BlueprintFile.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_module_inputs_using_get**
> dict(str, ModuleInputDTO) get_module_inputs_using_get(flavor, intent, stack_name)

getModuleInputs

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
flavor = 'flavor_example' # str | flavor
intent = 'intent_example' # str | intent
stack_name = 'stack_name_example' # str | stackName

try:
    # getModuleInputs
    api_response = api_instance.get_module_inputs_using_get(flavor, intent, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_module_inputs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavor** | **str**| flavor | 
 **intent** | **str**| intent | 
 **stack_name** | **str**| stackName | 

### Return type

[**dict(str, ModuleInputDTO)**](ModuleInputDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pull_requests_using_get**
> ListPullRequestResponse get_pull_requests_using_get(stack_name, created_date=created_date, page_number=page_number, page_size=page_size, query=query, state=state)

getPullRequests

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName
created_date = 'created_date_example' # str | createdDate (optional)
page_number = 1 # int | pageNumber (optional) (default to 1)
page_size = 10 # int | pageSize (optional) (default to 10)
query = 'query_example' # str | query (optional)
state = 'OPEN' # str | state (optional) (default to OPEN)

try:
    # getPullRequests
    api_response = api_instance.get_pull_requests_using_get(stack_name, created_date=created_date, page_number=page_number, page_size=page_size, query=query, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_pull_requests_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 
 **created_date** | **str**| createdDate | [optional] 
 **page_number** | **int**| pageNumber | [optional] [default to 1]
 **page_size** | **int**| pageSize | [optional] [default to 10]
 **query** | **str**| query | [optional] 
 **state** | **str**| state | [optional] [default to OPEN]

### Return type

[**ListPullRequestResponse**](ListPullRequestResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pull_requests_using_get1**
> ListPullRequestResponse get_pull_requests_using_get1(resource_name, resource_type, stack_name, created_date=created_date, page_number=page_number, page_size=page_size, query=query, state=state)

getPullRequests

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName
created_date = 'created_date_example' # str | createdDate (optional)
page_number = 1 # int | pageNumber (optional) (default to 1)
page_size = 10 # int | pageSize (optional) (default to 10)
query = 'query_example' # str | query (optional)
state = 'OPEN' # str | state (optional) (default to OPEN)

try:
    # getPullRequests
    api_response = api_instance.get_pull_requests_using_get1(resource_name, resource_type, stack_name, created_date=created_date, page_number=page_number, page_size=page_size, query=query, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_pull_requests_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **stack_name** | **str**| stackName | 
 **created_date** | **str**| createdDate | [optional] 
 **page_number** | **int**| pageNumber | [optional] [default to 1]
 **page_size** | **int**| pageSize | [optional] [default to 10]
 **query** | **str**| query | [optional] 
 **state** | **str**| state | [optional] [default to OPEN]

### Return type

[**ListPullRequestResponse**](ListPullRequestResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_metadata_using_get**
> JsonNode get_schema_metadata_using_get()

getSchemaMetadata

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))

try:
    # getSchemaMetadata
    api_response = api_instance.get_schema_metadata_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_schema_metadata_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonNode**](JsonNode.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_runs_using_get**
> ListWorkflowRunsResponse get_workflow_runs_using_get(resource_name, resource_type, stack_name, actor=actor, branch=branch, event=event, page_number=page_number, page_size=page_size, status=status, workflow_id=workflow_id)

getWorkflowRuns

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName
actor = 'actor_example' # str | actor (optional)
branch = 'branch_example' # str | branch (optional)
event = 'event_example' # str | event (optional)
page_number = 1 # int | pageNumber (optional) (default to 1)
page_size = 10 # int | pageSize (optional) (default to 10)
status = 'status_example' # str | status (optional)
workflow_id = 'workflow_id_example' # str | workflowId (optional)

try:
    # getWorkflowRuns
    api_response = api_instance.get_workflow_runs_using_get(resource_name, resource_type, stack_name, actor=actor, branch=branch, event=event, page_number=page_number, page_size=page_size, status=status, workflow_id=workflow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_workflow_runs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **stack_name** | **str**| stackName | 
 **actor** | **str**| actor | [optional] 
 **branch** | **str**| branch | [optional] 
 **event** | **str**| event | [optional] 
 **page_number** | **int**| pageNumber | [optional] [default to 1]
 **page_size** | **int**| pageSize | [optional] [default to 10]
 **status** | **str**| status | [optional] 
 **workflow_id** | **str**| workflowId | [optional] 

### Return type

[**ListWorkflowRunsResponse**](ListWorkflowRunsResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_runs_using_get1**
> ListWorkflowRunsResponse get_workflow_runs_using_get1(stack_name, actor=actor, branch=branch, event=event, page_number=page_number, page_size=page_size, status=status, workflow_id=workflow_id)

getWorkflowRuns

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName
actor = 'actor_example' # str | actor (optional)
branch = 'branch_example' # str | branch (optional)
event = 'event_example' # str | event (optional)
page_number = 1 # int | pageNumber (optional) (default to 1)
page_size = 10 # int | pageSize (optional) (default to 10)
status = 'status_example' # str | status (optional)
workflow_id = 'workflow_id_example' # str | workflowId (optional)

try:
    # getWorkflowRuns
    api_response = api_instance.get_workflow_runs_using_get1(stack_name, actor=actor, branch=branch, event=event, page_number=page_number, page_size=page_size, status=status, workflow_id=workflow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_workflow_runs_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 
 **actor** | **str**| actor | [optional] 
 **branch** | **str**| branch | [optional] 
 **event** | **str**| event | [optional] 
 **page_number** | **int**| pageNumber | [optional] [default to 1]
 **page_size** | **int**| pageSize | [optional] [default to 10]
 **status** | **str**| status | [optional] 
 **workflow_id** | **str**| workflowId | [optional] 

### Return type

[**ListWorkflowRunsResponse**](ListWorkflowRunsResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflows_using_get**
> list[Workflow] get_workflows_using_get(resource_name, resource_type, stack_name)

getWorkflows

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName

try:
    # getWorkflows
    api_response = api_instance.get_workflows_using_get(resource_name, resource_type, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_workflows_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **stack_name** | **str**| stackName | 

### Return type

[**list[Workflow]**](Workflow.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflows_using_get1**
> list[Workflow] get_workflows_using_get1(stack_name)

getWorkflows

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getWorkflows
    api_response = api_instance.get_workflows_using_get1(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_workflows_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**list[Workflow]**](Workflow.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_branches_using_get**
> BranchDTO list_branches_using_get(stack_name)

listBranches

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # listBranches
    api_response = api_instance.list_branches_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->list_branches_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**BranchDTO**](BranchDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_branches_using_get1**
> list[str] list_branches_using_get1(resource_name, resource_type, stack_name)

listBranches

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName

try:
    # listBranches
    api_response = api_instance.list_branches_using_get1(resource_name, resource_type, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->list_branches_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_name** | **str**| resourceName | 
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

# **rename_resource_using_put**
> rename_resource_using_put(body, branch, stack_name)

renameResource

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResourceRenameRequest() # ResourceRenameRequest | resourceRenameRequest
branch = 'branch_example' # str | branch
stack_name = 'stack_name_example' # str | stackName

try:
    # renameResource
    api_instance.rename_resource_using_put(body, branch, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->rename_resource_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceRenameRequest**](ResourceRenameRequest.md)| resourceRenameRequest | 
 **branch** | **str**| branch | 
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_resource_using_put1**
> rename_resource_using_put1(body, stack_name)

renameResource

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ResourceRenameRequest() # ResourceRenameRequest | resourceRenameRequest
stack_name = 'stack_name_example' # str | stackName

try:
    # renameResource
    api_instance.rename_resource_using_put1(body, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->rename_resource_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceRenameRequest**](ResourceRenameRequest.md)| resourceRenameRequest | 
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_specified_blueprints_with_templates_using_post**
> sync_specified_blueprints_with_templates_using_post(body, template_name)

syncSpecifiedBlueprintsWithTemplates

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | blueprintNames
template_name = 'template_name_example' # str | templateName

try:
    # syncSpecifiedBlueprintsWithTemplates
    api_instance.sync_specified_blueprints_with_templates_using_post(body, template_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->sync_specified_blueprints_with_templates_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| blueprintNames | 
 **template_name** | **str**| templateName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resources_using_put**
> update_resources_using_put(body, branch, stack_name)

updateResources

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ResourceFileRequest()] # list[ResourceFileRequest] | resourceFileRequests
branch = 'branch_example' # str | branch
stack_name = 'stack_name_example' # str | stackName

try:
    # updateResources
    api_instance.update_resources_using_put(body, branch, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->update_resources_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ResourceFileRequest]**](ResourceFileRequest.md)| resourceFileRequests | 
 **branch** | **str**| branch | 
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resources_using_put1**
> update_resources_using_put1(body, stack_name)

updateResources

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ResourceFileRequest()] # list[ResourceFileRequest] | resourceFileRequests
stack_name = 'stack_name_example' # str | stackName

try:
    # updateResources
    api_instance.update_resources_using_put1(body, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->update_resources_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ResourceFileRequest]**](ResourceFileRequest.md)| resourceFileRequests | 
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_variables_using_put**
> update_variables_using_put(body, stack_name)

updateVariables

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, VariableDetails) | variables
stack_name = 'stack_name_example' # str | stackName

try:
    # updateVariables
    api_instance.update_variables_using_put(body, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->update_variables_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, VariableDetails)**](dict.md)| variables | 
 **stack_name** | **str**| stackName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

