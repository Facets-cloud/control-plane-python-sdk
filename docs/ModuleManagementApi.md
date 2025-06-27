# swagger_client.ModuleManagementApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bootstrap_modules**](ModuleManagementApi.md#bootstrap_modules) | **POST** /cc-ui/v1/modules/bootstrap | Bootstrap Modules
[**delete_tf_module**](ModuleManagementApi.md#delete_tf_module) | **DELETE** /cc-ui/v1/modules/{id} | Delete a Module
[**download_module_by_id**](ModuleManagementApi.md#download_module_by_id) | **GET** /cc-ui/v1/modules/{id}/download | 
[**download_module_by_version_id**](ModuleManagementApi.md#download_module_by_version_id) | **GET** /cc-ui/v1/modules/version/{versionId}/download | 
[**get_all2**](ModuleManagementApi.md#get_all2) | **GET** /cc-ui/v1/modules/all | Get All Modules
[**get_all_modules**](ModuleManagementApi.md#get_all_modules) | **GET** /cc-ui/v1/modules | Get All Modules
[**get_all_modules_lite**](ModuleManagementApi.md#get_all_modules_lite) | **GET** /cc-ui/v1/modules/modules-lite | 
[**get_by_id**](ModuleManagementApi.md#get_by_id) | **GET** /cc-ui/v1/modules/{id} | Get Module by ID
[**get_grouped_modules_for_stack**](ModuleManagementApi.md#get_grouped_modules_for_stack) | **GET** /cc-ui/v1/modules/stack/{stackName}/grouped | Get Grouped Modules for Stack
[**get_intent_add_on_modules**](ModuleManagementApi.md#get_intent_add_on_modules) | **GET** /cc-ui/v1/modules/intent/{intent}/flavor/{flavor}/add-ons | Get Add-On Modules
[**get_module_for_ifv_and_stack**](ModuleManagementApi.md#get_module_for_ifv_and_stack) | **GET** /cc-ui/v1/modules/stack/{stackName}/{intent}/{flavor}/{version}/module | 
[**get_module_usages**](ModuleManagementApi.md#get_module_usages) | **GET** /cc-ui/v1/modules/{id}/usages | Get Module Usages
[**mark_as_published**](ModuleManagementApi.md#mark_as_published) | **POST** /cc-ui/v1/modules/intent/{intent}/flavor/{flavor}/version/{version}/mark-published | Mark Module as Published
[**mark_as_published_by_id**](ModuleManagementApi.md#mark_as_published_by_id) | **POST** /cc-ui/v1/modules/{id}/mark-published | Mark Module as Published
[**upload_module**](ModuleManagementApi.md#upload_module) | **POST** /cc-ui/v1/modules/upload | Upload a module

# **bootstrap_modules**
> dict(str, list[str]) bootstrap_modules()

Bootstrap Modules

- **Description:** Bootstraps modules for initialization. - **Audit Logging:** No specific audit logging at the moment.

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
api_instance = swagger_client.ModuleManagementApi(swagger_client.ApiClient(configuration))

try:
    # Bootstrap Modules
    api_response = api_instance.bootstrap_modules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleManagementApi->bootstrap_modules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, list[str])**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tf_module**
> TFModule delete_tf_module(id, force=force)

Delete a Module

- **Description:** Deletes a module by ID. - **Permissions:** Requires MODULE_DELETE permission.  - **Audit Logging:** Yes

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
api_instance = swagger_client.ModuleManagementApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 
force = false # bool |  (optional) (default to false)

try:
    # Delete a Module
    api_response = api_instance.delete_tf_module(id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleManagementApi->delete_tf_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **force** | **bool**|  | [optional] [default to false]

### Return type

[**TFModule**](TFModule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_module_by_id**
> str download_module_by_id(id)



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
api_instance = swagger_client.ModuleManagementApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.download_module_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleManagementApi->download_module_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_module_by_version_id**
> str download_module_by_version_id(version_id)



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
api_instance = swagger_client.ModuleManagementApi(swagger_client.ApiClient(configuration))
version_id = 'version_id_example' # str | 

try:
    api_response = api_instance.download_module_by_version_id(version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleManagementApi->download_module_by_version_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all2**
> list[TFModule] get_all2(include_facets_yaml=include_facets_yaml, allow_preview_modules=allow_preview_modules, with_path_only=with_path_only)

Get All Modules

- **Description:** Retrieves all modules with optional filtering. - **Audit Logging:** No specific audit logging at the moment.

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
api_instance = swagger_client.ModuleManagementApi(swagger_client.ApiClient(configuration))
include_facets_yaml = false # bool |  (optional) (default to false)
allow_preview_modules = false # bool |  (optional) (default to false)
with_path_only = false # bool |  (optional) (default to false)

try:
    # Get All Modules
    api_response = api_instance.get_all2(include_facets_yaml=include_facets_yaml, allow_preview_modules=allow_preview_modules, with_path_only=with_path_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleManagementApi->get_all2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_facets_yaml** | **bool**|  | [optional] [default to false]
 **allow_preview_modules** | **bool**|  | [optional] [default to false]
 **with_path_only** | **bool**|  | [optional] [default to false]

### Return type

[**list[TFModule]**](TFModule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_modules**
> list[TFModuleListResponseDTO] get_all_modules(can_download=can_download)

Get All Modules

- **Description:** Retrieves all modules with optional filtering. - **Parameters:**   - `canDownload` (optional): When true, returns only modules that have downloadable content (modules with path). Defaults to false. - **Permissions:** Requires MODULE_READ permission. - **Audit Logging:** No specific audit logging at the moment.

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
api_instance = swagger_client.ModuleManagementApi(swagger_client.ApiClient(configuration))
can_download = false # bool |  (optional) (default to false)

try:
    # Get All Modules
    api_response = api_instance.get_all_modules(can_download=can_download)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleManagementApi->get_all_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **can_download** | **bool**|  | [optional] [default to false]

### Return type

[**list[TFModuleListResponseDTO]**](TFModuleListResponseDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_modules_lite**
> list[TFModuleLiteDTO] get_all_modules_lite(clouds=clouds, allow_preview_modules=allow_preview_modules)



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
api_instance = swagger_client.ModuleManagementApi(swagger_client.ApiClient(configuration))
clouds = ['clouds_example'] # list[str] |  (optional)
allow_preview_modules = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_all_modules_lite(clouds=clouds, allow_preview_modules=allow_preview_modules)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleManagementApi->get_all_modules_lite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clouds** | [**list[str]**](str.md)|  | [optional] 
 **allow_preview_modules** | **bool**|  | [optional] [default to false]

### Return type

[**list[TFModuleLiteDTO]**](TFModuleLiteDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_id**
> TFModuleResponseDTO get_by_id(id)

Get Module by ID

- **Description:** Retrieves a module by its ID. - **Audit Logging:** No specific audit logging at the moment.

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
api_instance = swagger_client.ModuleManagementApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Module by ID
    api_response = api_instance.get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleManagementApi->get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TFModuleResponseDTO**](TFModuleResponseDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grouped_modules_for_stack**
> ListResourcesResponse get_grouped_modules_for_stack(stack_name)

Get Grouped Modules for Stack

- **Description:** Retrieves grouped modules specifically for a stack name. - **Audit Logging:** No specific audit logging at the moment.

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
api_instance = swagger_client.ModuleManagementApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    # Get Grouped Modules for Stack
    api_response = api_instance.get_grouped_modules_for_stack(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleManagementApi->get_grouped_modules_for_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**ListResourcesResponse**](ListResourcesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_intent_add_on_modules**
> list[TFModuleLiteDTO] get_intent_add_on_modules(intent, flavor, cloud=cloud)

Get Add-On Modules

- **Description:** Retrieves all add-on modules based on intent and flavor, optionally by cloud. - **Audit Logging:** No specific audit logging at the moment.

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
api_instance = swagger_client.ModuleManagementApi(swagger_client.ApiClient(configuration))
intent = 'intent_example' # str | 
flavor = 'flavor_example' # str | 
cloud = 'cloud_example' # str |  (optional)

try:
    # Get Add-On Modules
    api_response = api_instance.get_intent_add_on_modules(intent, flavor, cloud=cloud)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleManagementApi->get_intent_add_on_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intent** | **str**|  | 
 **flavor** | **str**|  | 
 **cloud** | **str**|  | [optional] 

### Return type

[**list[TFModuleLiteDTO]**](TFModuleLiteDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_module_for_ifv_and_stack**
> TFModuleResponseDTO get_module_for_ifv_and_stack(stack_name, intent, flavor, version)



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
api_instance = swagger_client.ModuleManagementApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
intent = 'intent_example' # str | 
flavor = 'flavor_example' # str | 
version = 'version_example' # str | 

try:
    api_response = api_instance.get_module_for_ifv_and_stack(stack_name, intent, flavor, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleManagementApi->get_module_for_ifv_and_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **intent** | **str**|  | 
 **flavor** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**TFModuleResponseDTO**](TFModuleResponseDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_module_usages**
> list[ModuleUsageDTO] get_module_usages(id)

Get Module Usages

- **Description:** Retrieves all usages of a module across stacks and clusters. - **Audit Logging:** No specific audit logging at the moment.

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
api_instance = swagger_client.ModuleManagementApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Module Usages
    api_response = api_instance.get_module_usages(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleManagementApi->get_module_usages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[ModuleUsageDTO]**](ModuleUsageDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_as_published**
> TFModule mark_as_published(intent, flavor, version)

Mark Module as Published

- **Description:** Marks a specific module version as published. - **Permissions:** Requires MODULE_WRITE permission.  - **Audit Logging:** Yes

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
api_instance = swagger_client.ModuleManagementApi(swagger_client.ApiClient(configuration))
intent = 'intent_example' # str | 
flavor = 'flavor_example' # str | 
version = 'version_example' # str | 

try:
    # Mark Module as Published
    api_response = api_instance.mark_as_published(intent, flavor, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleManagementApi->mark_as_published: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intent** | **str**|  | 
 **flavor** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**TFModule**](TFModule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_as_published_by_id**
> TFModule mark_as_published_by_id(id)

Mark Module as Published

- **Description:** Marks a specific module version as published. - **Permissions:** Requires MODULE_WRITE permission.  - **Audit Logging:** Yes

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
api_instance = swagger_client.ModuleManagementApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Mark Module as Published
    api_response = api_instance.mark_as_published_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleManagementApi->mark_as_published_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TFModule**](TFModule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_module**
> TFModule upload_module(body=body)

Upload a module

- **Description:** Uploads a module using a file. - **Permissions:** Requires MODULE_WRITE permission. - **Parameters:**   - `file`: The module file to upload   - `metadata` (optional): Additional module metadata including:     - `gitUrl`: Web URL of the git repository (Expected to embed the commit id)     - `gitRef`: Git reference (branch, tag, or commit)     - `isFeatureBranch`: If this is true, this preview module cannot be directly marked as published until we register the module again with this as false. - **Audit Logging:** Yes

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
api_instance = swagger_client.ModuleManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.ModulesUploadBody() # ModulesUploadBody |  (optional)

try:
    # Upload a module
    api_response = api_instance.upload_module(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleManagementApi->upload_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModulesUploadBody**](ModulesUploadBody.md)|  | [optional] 

### Return type

[**TFModule**](TFModule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

