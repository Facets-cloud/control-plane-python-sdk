# swagger_client.UiBlueprintDesignerControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_variables**](UiBlueprintDesignerControllerApi.md#add_variables) | **POST** /cc-ui/v1/designer/{stackName}/variables | 
[**apply_template**](UiBlueprintDesignerControllerApi.md#apply_template) | **POST** /cc-ui/v1/designer/{stackName}/{templateName}/apply | 
[**bulk_edit_disabled_for_resources**](UiBlueprintDesignerControllerApi.md#bulk_edit_disabled_for_resources) | **PUT** /cc-ui/v1/designer/{stackName}/resource-enable-disable | 
[**bulk_edit_disabled_for_resources1**](UiBlueprintDesignerControllerApi.md#bulk_edit_disabled_for_resources1) | **PUT** /cc-ui/v1/designer/{stackName}/branch/{branch}/resource-enable-disable | 
[**create_branch**](UiBlueprintDesignerControllerApi.md#create_branch) | **POST** /cc-ui/v1/designer/{stackName}/{branch}/create-branch | 
[**create_resources**](UiBlueprintDesignerControllerApi.md#create_resources) | **POST** /cc-ui/v1/designer/{stackName}/branch/{branch} | 
[**delete_resources**](UiBlueprintDesignerControllerApi.md#delete_resources) | **DELETE** /cc-ui/v1/designer/{stackName}/branch/{branch} | 
[**delete_variables**](UiBlueprintDesignerControllerApi.md#delete_variables) | **DELETE** /cc-ui/v1/designer/{stackName}/variables | 
[**get_add_on_modules**](UiBlueprintDesignerControllerApi.md#get_add_on_modules) | **GET** /cc-ui/v1/designer/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/add-ons | Get add ons for this resource
[**get_autocomplete_data**](UiBlueprintDesignerControllerApi.md#get_autocomplete_data) | **GET** /cc-ui/v1/designer/{stackName}/ref-autocomplete-data | 
[**get_autocomplete_data_v2**](UiBlueprintDesignerControllerApi.md#get_autocomplete_data_v2) | **GET** /cc-ui/v1/designer/{stackName}/ref-autocomplete-data-v2 | Get autocomplete data with module-specific output trees
[**get_designer_resources**](UiBlueprintDesignerControllerApi.md#get_designer_resources) | **GET** /cc-ui/v1/designer/{stackName}/{branchName}/files | 
[**get_module_inputs**](UiBlueprintDesignerControllerApi.md#get_module_inputs) | **GET** /cc-ui/v1/designer/{stackName}/intent/{intent}/flavor/{flavor}/input | 
[**get_pull_requests**](UiBlueprintDesignerControllerApi.md#get_pull_requests) | **GET** /cc-ui/v1/designer/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/pulls | 
[**get_pull_requests1**](UiBlueprintDesignerControllerApi.md#get_pull_requests1) | **GET** /cc-ui/v1/designer/{stackName}/pulls | 
[**get_schema_metadata**](UiBlueprintDesignerControllerApi.md#get_schema_metadata) | **GET** /cc-ui/v1/designer/facets-components | 
[**get_workflow_runs**](UiBlueprintDesignerControllerApi.md#get_workflow_runs) | **GET** /cc-ui/v1/designer/{stackName}/workflow-runs | 
[**get_workflow_runs1**](UiBlueprintDesignerControllerApi.md#get_workflow_runs1) | **GET** /cc-ui/v1/designer/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/workflow-runs | 
[**get_workflows**](UiBlueprintDesignerControllerApi.md#get_workflows) | **GET** /cc-ui/v1/designer/{stackName}/workflows | 
[**get_workflows1**](UiBlueprintDesignerControllerApi.md#get_workflows1) | **GET** /cc-ui/v1/designer/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/workflows | 
[**list_branches**](UiBlueprintDesignerControllerApi.md#list_branches) | **GET** /cc-ui/v1/designer/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/branch-list | 
[**list_branches1**](UiBlueprintDesignerControllerApi.md#list_branches1) | **GET** /cc-ui/v1/designer/{stackName}/branch-list | 
[**list_providers_exposed_by_module**](UiBlueprintDesignerControllerApi.md#list_providers_exposed_by_module) | **GET** /cc-ui/v1/designer/{stackName}/intent/{intent}/flavor/{flavor}/output-providers | 
[**rename_resource**](UiBlueprintDesignerControllerApi.md#rename_resource) | **PUT** /cc-ui/v1/designer/{stackName}/branch/{branch}/rename | 
[**sync_specified_blueprints_with_templates**](UiBlueprintDesignerControllerApi.md#sync_specified_blueprints_with_templates) | **POST** /cc-ui/v1/designer/{templateName}/sync | 
[**update_resources**](UiBlueprintDesignerControllerApi.md#update_resources) | **PUT** /cc-ui/v1/designer/{stackName}/branch/{branch} | 
[**update_variables**](UiBlueprintDesignerControllerApi.md#update_variables) | **PUT** /cc-ui/v1/designer/{stackName}/variables | 

# **add_variables**
> add_variables(body, stack_name)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, ComCapillaryOpsCpBoStackFileVariableDetails) | 
stack_name = 'stack_name_example' # str | 

try:
    api_instance.add_variables(body, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->add_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, ComCapillaryOpsCpBoStackFileVariableDetails)**](dict.md)|  | 
 **stack_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_template**
> apply_template(stack_name, template_name, prefix=prefix, suffix=suffix)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
template_name = 'template_name_example' # str | 
prefix = 'prefix_example' # str |  (optional)
suffix = 'suffix_example' # str |  (optional)

try:
    api_instance.apply_template(stack_name, template_name, prefix=prefix, suffix=suffix)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->apply_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **template_name** | **str**|  | 
 **prefix** | **str**|  | [optional] 
 **suffix** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_edit_disabled_for_resources**
> bulk_edit_disabled_for_resources(body, stack_name)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ComCapillaryOpsCpBoResoucesResourceEnableDisableRequest()] # list[ComCapillaryOpsCpBoResoucesResourceEnableDisableRequest] | 
stack_name = 'stack_name_example' # str | 

try:
    api_instance.bulk_edit_disabled_for_resources(body, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->bulk_edit_disabled_for_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ComCapillaryOpsCpBoResoucesResourceEnableDisableRequest]**](ComCapillaryOpsCpBoResoucesResourceEnableDisableRequest.md)|  | 
 **stack_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_edit_disabled_for_resources1**
> bulk_edit_disabled_for_resources1(body, stack_name, branch)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ComCapillaryOpsCpBoResoucesResourceEnableDisableRequest()] # list[ComCapillaryOpsCpBoResoucesResourceEnableDisableRequest] | 
stack_name = 'stack_name_example' # str | 
branch = 'branch_example' # str | 

try:
    api_instance.bulk_edit_disabled_for_resources1(body, stack_name, branch)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->bulk_edit_disabled_for_resources1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ComCapillaryOpsCpBoResoucesResourceEnableDisableRequest]**](ComCapillaryOpsCpBoResoucesResourceEnableDisableRequest.md)|  | 
 **stack_name** | **str**|  | 
 **branch** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_branch**
> create_branch(stack_name, branch)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
branch = 'branch_example' # str | 

try:
    api_instance.create_branch(stack_name, branch)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->create_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **branch** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_resources**
> create_resources(body, stack_name, branch)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ComCapillaryOpsCpBoRequestsDesignerResourceFileRequest()] # list[ComCapillaryOpsCpBoRequestsDesignerResourceFileRequest] | 
stack_name = 'stack_name_example' # str | 
branch = 'branch_example' # str | 

try:
    api_instance.create_resources(body, stack_name, branch)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->create_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ComCapillaryOpsCpBoRequestsDesignerResourceFileRequest]**](ComCapillaryOpsCpBoRequestsDesignerResourceFileRequest.md)|  | 
 **stack_name** | **str**|  | 
 **branch** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resources**
> delete_resources(body, stack_name, branch)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ComCapillaryOpsCpBoRequestsDesignerResourceFileRequest()] # list[ComCapillaryOpsCpBoRequestsDesignerResourceFileRequest] | 
stack_name = 'stack_name_example' # str | 
branch = 'branch_example' # str | 

try:
    api_instance.delete_resources(body, stack_name, branch)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->delete_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ComCapillaryOpsCpBoRequestsDesignerResourceFileRequest]**](ComCapillaryOpsCpBoRequestsDesignerResourceFileRequest.md)|  | 
 **stack_name** | **str**|  | 
 **branch** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_variables**
> delete_variables(body, stack_name)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | 
stack_name = 'stack_name_example' # str | 

try:
    api_instance.delete_variables(body, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->delete_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **stack_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_add_on_modules**
> list[ComCapillaryOpsCpV2RegistryAddOnDTO] get_add_on_modules(stack_name, resource_type, resource_name, cloud=cloud)

Get add ons for this resource

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 
cloud = 'cloud_example' # str |  (optional)

try:
    # Get add ons for this resource
    api_response = api_instance.get_add_on_modules(stack_name, resource_type, resource_name, cloud=cloud)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_add_on_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 
 **cloud** | **str**|  | [optional] 

### Return type

[**list[ComCapillaryOpsCpV2RegistryAddOnDTO]**](ComCapillaryOpsCpV2RegistryAddOnDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_autocomplete_data**
> ComCapillaryOpsCpBoAutocompleteResponse get_autocomplete_data(stack_name)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_autocomplete_data(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_autocomplete_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAutocompleteResponse**](ComCapillaryOpsCpBoAutocompleteResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_autocomplete_data_v2**
> ComCapillaryOpsCpBoAutocompleteResponseV2 get_autocomplete_data_v2(stack_name)

Get autocomplete data with module-specific output trees

Returns module-specific output trees for each resource with automatic fallback to intent-level outputs

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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    # Get autocomplete data with module-specific output trees
    api_response = api_instance.get_autocomplete_data_v2(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_autocomplete_data_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAutocompleteResponseV2**](ComCapillaryOpsCpBoAutocompleteResponseV2.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_designer_resources**
> list[ComCapillaryOpsCpBoResoucesBlueprintFile] get_designer_resources(stack_name, branch_name)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
branch_name = 'branch_name_example' # str | 

try:
    api_response = api_instance.get_designer_resources(stack_name, branch_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_designer_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **branch_name** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoResoucesBlueprintFile]**](ComCapillaryOpsCpBoResoucesBlueprintFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_module_inputs**
> dict(str, ComCapillaryOpsCpV2RegistryModuleInputDTO) get_module_inputs(stack_name, intent, flavor)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
intent = 'intent_example' # str | 
flavor = 'flavor_example' # str | 

try:
    api_response = api_instance.get_module_inputs(stack_name, intent, flavor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_module_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **intent** | **str**|  | 
 **flavor** | **str**|  | 

### Return type

[**dict(str, ComCapillaryOpsCpV2RegistryModuleInputDTO)**](ComCapillaryOpsCpV2RegistryModuleInputDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pull_requests**
> ComCapillaryOpsCpBoGithubListPullRequestResponse get_pull_requests(stack_name, resource_type, resource_name, state=state, page_size=page_size, page_number=page_number, created_date=created_date, query=query)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 
state = 'OPEN' # str |  (optional) (default to OPEN)
page_size = 10 # int |  (optional) (default to 10)
page_number = 1 # int |  (optional) (default to 1)
created_date = 'created_date_example' # str |  (optional)
query = 'query_example' # str |  (optional)

try:
    api_response = api_instance.get_pull_requests(stack_name, resource_type, resource_name, state=state, page_size=page_size, page_number=page_number, created_date=created_date, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_pull_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 
 **state** | **str**|  | [optional] [default to OPEN]
 **page_size** | **int**|  | [optional] [default to 10]
 **page_number** | **int**|  | [optional] [default to 1]
 **created_date** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 

### Return type

[**ComCapillaryOpsCpBoGithubListPullRequestResponse**](ComCapillaryOpsCpBoGithubListPullRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pull_requests1**
> ComCapillaryOpsCpBoGithubListPullRequestResponse get_pull_requests1(stack_name, state=state, page_size=page_size, page_number=page_number, created_date=created_date, query=query)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
state = 'OPEN' # str |  (optional) (default to OPEN)
page_size = 10 # int |  (optional) (default to 10)
page_number = 1 # int |  (optional) (default to 1)
created_date = 'created_date_example' # str |  (optional)
query = 'query_example' # str |  (optional)

try:
    api_response = api_instance.get_pull_requests1(stack_name, state=state, page_size=page_size, page_number=page_number, created_date=created_date, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_pull_requests1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **state** | **str**|  | [optional] [default to OPEN]
 **page_size** | **int**|  | [optional] [default to 10]
 **page_number** | **int**|  | [optional] [default to 1]
 **created_date** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 

### Return type

[**ComCapillaryOpsCpBoGithubListPullRequestResponse**](ComCapillaryOpsCpBoGithubListPullRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_metadata**
> ComFasterxmlJacksonDatabindJsonNode get_schema_metadata()



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_schema_metadata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_schema_metadata: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ComFasterxmlJacksonDatabindJsonNode**](ComFasterxmlJacksonDatabindJsonNode.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_runs**
> ComCapillaryOpsCpBoGithubListWorkflowRunsResponse get_workflow_runs(stack_name, page_size=page_size, page_number=page_number, workflow_id=workflow_id, event=event, status=status, branch=branch, actor=actor)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
page_size = 10 # int |  (optional) (default to 10)
page_number = 1 # int |  (optional) (default to 1)
workflow_id = 'workflow_id_example' # str |  (optional)
event = 'event_example' # str |  (optional)
status = 'status_example' # str |  (optional)
branch = 'branch_example' # str |  (optional)
actor = 'actor_example' # str |  (optional)

try:
    api_response = api_instance.get_workflow_runs(stack_name, page_size=page_size, page_number=page_number, workflow_id=workflow_id, event=event, status=status, branch=branch, actor=actor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_workflow_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **page_size** | **int**|  | [optional] [default to 10]
 **page_number** | **int**|  | [optional] [default to 1]
 **workflow_id** | **str**|  | [optional] 
 **event** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **branch** | **str**|  | [optional] 
 **actor** | **str**|  | [optional] 

### Return type

[**ComCapillaryOpsCpBoGithubListWorkflowRunsResponse**](ComCapillaryOpsCpBoGithubListWorkflowRunsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_runs1**
> ComCapillaryOpsCpBoGithubListWorkflowRunsResponse get_workflow_runs1(stack_name, resource_type, resource_name, page_size=page_size, page_number=page_number, workflow_id=workflow_id, event=event, status=status, branch=branch, actor=actor)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 
page_size = 10 # int |  (optional) (default to 10)
page_number = 1 # int |  (optional) (default to 1)
workflow_id = 'workflow_id_example' # str |  (optional)
event = 'event_example' # str |  (optional)
status = 'status_example' # str |  (optional)
branch = 'branch_example' # str |  (optional)
actor = 'actor_example' # str |  (optional)

try:
    api_response = api_instance.get_workflow_runs1(stack_name, resource_type, resource_name, page_size=page_size, page_number=page_number, workflow_id=workflow_id, event=event, status=status, branch=branch, actor=actor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_workflow_runs1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 
 **page_size** | **int**|  | [optional] [default to 10]
 **page_number** | **int**|  | [optional] [default to 1]
 **workflow_id** | **str**|  | [optional] 
 **event** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **branch** | **str**|  | [optional] 
 **actor** | **str**|  | [optional] 

### Return type

[**ComCapillaryOpsCpBoGithubListWorkflowRunsResponse**](ComCapillaryOpsCpBoGithubListWorkflowRunsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflows**
> list[ComCapillaryOpsCpBoGithubWorkflow] get_workflows(stack_name)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_workflows(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_workflows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoGithubWorkflow]**](ComCapillaryOpsCpBoGithubWorkflow.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflows1**
> list[ComCapillaryOpsCpBoGithubWorkflow] get_workflows1(stack_name, resource_type, resource_name)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.get_workflows1(stack_name, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->get_workflows1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoGithubWorkflow]**](ComCapillaryOpsCpBoGithubWorkflow.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_branches**
> list[str] list_branches(stack_name, resource_type, resource_name)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.list_branches(stack_name, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->list_branches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_branches1**
> ComCapillaryOpsCpBoBranchDTO list_branches1(stack_name)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.list_branches1(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->list_branches1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoBranchDTO**](ComCapillaryOpsCpBoBranchDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers_exposed_by_module**
> list[ComCapillaryOpsCpV2RegistryOutputTFProvider] list_providers_exposed_by_module(stack_name, intent, flavor)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
intent = 'intent_example' # str | 
flavor = 'flavor_example' # str | 

try:
    api_response = api_instance.list_providers_exposed_by_module(stack_name, intent, flavor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->list_providers_exposed_by_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **intent** | **str**|  | 
 **flavor** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpV2RegistryOutputTFProvider]**](ComCapillaryOpsCpV2RegistryOutputTFProvider.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_resource**
> rename_resource(body, stack_name, branch)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoRequestsDesignerResourceRenameRequest() # ComCapillaryOpsCpBoRequestsDesignerResourceRenameRequest | 
stack_name = 'stack_name_example' # str | 
branch = 'branch_example' # str | 

try:
    api_instance.rename_resource(body, stack_name, branch)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->rename_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsDesignerResourceRenameRequest**](ComCapillaryOpsCpBoRequestsDesignerResourceRenameRequest.md)|  | 
 **stack_name** | **str**|  | 
 **branch** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_specified_blueprints_with_templates**
> sync_specified_blueprints_with_templates(body, template_name)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | 
template_name = 'template_name_example' # str | 

try:
    api_instance.sync_specified_blueprints_with_templates(body, template_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->sync_specified_blueprints_with_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **template_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resources**
> update_resources(body, stack_name, branch)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ComCapillaryOpsCpBoRequestsDesignerResourceFileRequest()] # list[ComCapillaryOpsCpBoRequestsDesignerResourceFileRequest] | 
stack_name = 'stack_name_example' # str | 
branch = 'branch_example' # str | 

try:
    api_instance.update_resources(body, stack_name, branch)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->update_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ComCapillaryOpsCpBoRequestsDesignerResourceFileRequest]**](ComCapillaryOpsCpBoRequestsDesignerResourceFileRequest.md)|  | 
 **stack_name** | **str**|  | 
 **branch** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_variables**
> update_variables(body, stack_name)



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
api_instance = swagger_client.UiBlueprintDesignerControllerApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, ComCapillaryOpsCpBoStackFileVariableDetails) | 
stack_name = 'stack_name_example' # str | 

try:
    api_instance.update_variables(body, stack_name)
except ApiException as e:
    print("Exception when calling UiBlueprintDesignerControllerApi->update_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, ComCapillaryOpsCpBoStackFileVariableDetails)**](dict.md)|  | 
 **stack_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

