# swagger_client.UiTfModuleControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bootstrap_modules_using_post**](UiTfModuleControllerApi.md#bootstrap_modules_using_post) | **POST** /cc-ui/v1/modules/bootstrap | Bootstrap Modules
[**delete_tf_module_using_delete**](UiTfModuleControllerApi.md#delete_tf_module_using_delete) | **DELETE** /cc-ui/v1/modules/{id} | Delete a Module
[**download_module_by_id_using_get**](UiTfModuleControllerApi.md#download_module_by_id_using_get) | **GET** /cc-ui/v1/modules/{id}/download | downloadModuleById
[**download_module_by_version_id_using_get**](UiTfModuleControllerApi.md#download_module_by_version_id_using_get) | **GET** /cc-ui/v1/modules/version/{versionId}/download | downloadModuleByVersionId
[**get_all_modules_lite_using_get**](UiTfModuleControllerApi.md#get_all_modules_lite_using_get) | **GET** /cc-ui/v1/modules/modules-lite | getAllModulesLite
[**get_all_modules_using_get**](UiTfModuleControllerApi.md#get_all_modules_using_get) | **GET** /cc-ui/v1/modules | getAllModules
[**get_all_using_get4**](UiTfModuleControllerApi.md#get_all_using_get4) | **GET** /cc-ui/v1/modules/all | Get All Modules
[**get_by_id_using_get**](UiTfModuleControllerApi.md#get_by_id_using_get) | **GET** /cc-ui/v1/modules/{id} | Get Module by ID
[**get_facets_yaml_by_stack_using_get**](UiTfModuleControllerApi.md#get_facets_yaml_by_stack_using_get) | **GET** /cc-ui/v1/modules/stack/{stackName}/{intent}/{flavor}/{version}/fields | Get facets.yaml by Stack
[**get_grouped_modules_for_stack_using_get**](UiTfModuleControllerApi.md#get_grouped_modules_for_stack_using_get) | **GET** /cc-ui/v1/modules/stack/{stackName}/grouped | Get Grouped Modules for Stack
[**get_intent_add_on_modules_using_get**](UiTfModuleControllerApi.md#get_intent_add_on_modules_using_get) | **GET** /cc-ui/v1/modules/intent/{intent}/flavor/{flavor}/add-ons | Get Add-On Modules
[**get_module_for_ifv_and_stack_using_get**](UiTfModuleControllerApi.md#get_module_for_ifv_and_stack_using_get) | **GET** /cc-ui/v1/modules/stack/{stackName}/{intent}/{flavor}/{version}/module | getModuleForIFVAndStack
[**mark_as_published_by_id_using_post**](UiTfModuleControllerApi.md#mark_as_published_by_id_using_post) | **POST** /cc-ui/v1/modules/{id}/mark-published | Mark Module as Published
[**mark_as_published_using_post**](UiTfModuleControllerApi.md#mark_as_published_using_post) | **POST** /cc-ui/v1/modules/intent/{intent}/flavor/{flavor}/version/{version}/mark-published | Mark Module as Published
[**upload_module_using_post**](UiTfModuleControllerApi.md#upload_module_using_post) | **POST** /cc-ui/v1/modules/upload | Upload a module


# **bootstrap_modules_using_post**
> dict(str, list[str]) bootstrap_modules_using_post()

Bootstrap Modules

- **Description:** Bootstraps modules for initialization. - **Audit Logging:** No specific audit logging at the moment.

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
api_instance = swagger_client.UiTfModuleControllerApi(swagger_client.ApiClient(configuration))

try:
    # Bootstrap Modules
    api_response = api_instance.bootstrap_modules_using_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfModuleControllerApi->bootstrap_modules_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, list[str])**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tf_module_using_delete**
> TFModule delete_tf_module_using_delete(id)

Delete a Module

- **Description:** Deletes a module by ID. - **Permissions:** Requires MODULE_DELETE permission.  - **Audit Logging:** Yes

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
api_instance = swagger_client.UiTfModuleControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete a Module
    api_response = api_instance.delete_tf_module_using_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfModuleControllerApi->delete_tf_module_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**TFModule**](TFModule.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_module_by_id_using_get**
> Resource download_module_by_id_using_get(id)

downloadModuleById

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
api_instance = swagger_client.UiTfModuleControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # downloadModuleById
    api_response = api_instance.download_module_by_id_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfModuleControllerApi->download_module_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**Resource**](Resource.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_module_by_version_id_using_get**
> Resource download_module_by_version_id_using_get(version_id)

downloadModuleByVersionId

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
api_instance = swagger_client.UiTfModuleControllerApi(swagger_client.ApiClient(configuration))
version_id = 'version_id_example' # str | versionId

try:
    # downloadModuleByVersionId
    api_response = api_instance.download_module_by_version_id_using_get(version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfModuleControllerApi->download_module_by_version_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**| versionId | 

### Return type

[**Resource**](Resource.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_modules_lite_using_get**
> list[TFModuleLiteDTO] get_all_modules_lite_using_get(allow_preview_modules=allow_preview_modules, clouds=clouds)

getAllModulesLite

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
api_instance = swagger_client.UiTfModuleControllerApi(swagger_client.ApiClient(configuration))
allow_preview_modules = false # bool | allowPreviewModules (optional) (default to false)
clouds = ['clouds_example'] # list[str] | clouds (optional)

try:
    # getAllModulesLite
    api_response = api_instance.get_all_modules_lite_using_get(allow_preview_modules=allow_preview_modules, clouds=clouds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfModuleControllerApi->get_all_modules_lite_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_preview_modules** | **bool**| allowPreviewModules | [optional] [default to false]
 **clouds** | [**list[str]**](str.md)| clouds | [optional] 

### Return type

[**list[TFModuleLiteDTO]**](TFModuleLiteDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_modules_using_get**
> list[TFModuleListResponseDTO] get_all_modules_using_get()

getAllModules

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
api_instance = swagger_client.UiTfModuleControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllModules
    api_response = api_instance.get_all_modules_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfModuleControllerApi->get_all_modules_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TFModuleListResponseDTO]**](TFModuleListResponseDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_using_get4**
> list[TFModule] get_all_using_get4(allow_preview_modules=allow_preview_modules, include_facets_yaml=include_facets_yaml, with_path_only=with_path_only)

Get All Modules

- **Description:** Retrieves all modules with optional filtering. - **Audit Logging:** No specific audit logging at the moment.

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
api_instance = swagger_client.UiTfModuleControllerApi(swagger_client.ApiClient(configuration))
allow_preview_modules = false # bool | allowPreviewModules (optional) (default to false)
include_facets_yaml = false # bool | includeFacetsYaml (optional) (default to false)
with_path_only = false # bool | withPathOnly (optional) (default to false)

try:
    # Get All Modules
    api_response = api_instance.get_all_using_get4(allow_preview_modules=allow_preview_modules, include_facets_yaml=include_facets_yaml, with_path_only=with_path_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfModuleControllerApi->get_all_using_get4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_preview_modules** | **bool**| allowPreviewModules | [optional] [default to false]
 **include_facets_yaml** | **bool**| includeFacetsYaml | [optional] [default to false]
 **with_path_only** | **bool**| withPathOnly | [optional] [default to false]

### Return type

[**list[TFModule]**](TFModule.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_id_using_get**
> TFModuleResponseDTO get_by_id_using_get(id)

Get Module by ID

- **Description:** Retrieves a module by its ID. - **Audit Logging:** No specific audit logging at the moment.

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
api_instance = swagger_client.UiTfModuleControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Get Module by ID
    api_response = api_instance.get_by_id_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfModuleControllerApi->get_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**TFModuleResponseDTO**](TFModuleResponseDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_facets_yaml_by_stack_using_get**
> JsonNode get_facets_yaml_by_stack_using_get(flavor, intent, stack_name, version)

Get facets.yaml by Stack

- **Description:** Retrieves facets.yaml by stack information. - **Audit Logging:** No specific audit logging at the moment.

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
api_instance = swagger_client.UiTfModuleControllerApi(swagger_client.ApiClient(configuration))
flavor = 'flavor_example' # str | flavor
intent = 'intent_example' # str | intent
stack_name = 'stack_name_example' # str | stackName
version = 'version_example' # str | version

try:
    # Get facets.yaml by Stack
    api_response = api_instance.get_facets_yaml_by_stack_using_get(flavor, intent, stack_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfModuleControllerApi->get_facets_yaml_by_stack_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavor** | **str**| flavor | 
 **intent** | **str**| intent | 
 **stack_name** | **str**| stackName | 
 **version** | **str**| version | 

### Return type

[**JsonNode**](JsonNode.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grouped_modules_for_stack_using_get**
> ListResourcesResponse get_grouped_modules_for_stack_using_get(stack_name)

Get Grouped Modules for Stack

- **Description:** Retrieves grouped modules specifically for a stack name. - **Audit Logging:** No specific audit logging at the moment.

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
api_instance = swagger_client.UiTfModuleControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # Get Grouped Modules for Stack
    api_response = api_instance.get_grouped_modules_for_stack_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfModuleControllerApi->get_grouped_modules_for_stack_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**ListResourcesResponse**](ListResourcesResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_intent_add_on_modules_using_get**
> list[TFModuleLiteDTO] get_intent_add_on_modules_using_get(flavor, intent, cloud=cloud)

Get Add-On Modules

- **Description:** Retrieves all add-on modules based on intent and flavor, optionally by cloud. - **Audit Logging:** No specific audit logging at the moment.

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
api_instance = swagger_client.UiTfModuleControllerApi(swagger_client.ApiClient(configuration))
flavor = 'flavor_example' # str | flavor
intent = 'intent_example' # str | intent
cloud = 'cloud_example' # str | cloud (optional)

try:
    # Get Add-On Modules
    api_response = api_instance.get_intent_add_on_modules_using_get(flavor, intent, cloud=cloud)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfModuleControllerApi->get_intent_add_on_modules_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavor** | **str**| flavor | 
 **intent** | **str**| intent | 
 **cloud** | **str**| cloud | [optional] 

### Return type

[**list[TFModuleLiteDTO]**](TFModuleLiteDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_module_for_ifv_and_stack_using_get**
> TFModuleResponseDTO get_module_for_ifv_and_stack_using_get(flavor, intent, stack_name, version)

getModuleForIFVAndStack

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
api_instance = swagger_client.UiTfModuleControllerApi(swagger_client.ApiClient(configuration))
flavor = 'flavor_example' # str | flavor
intent = 'intent_example' # str | intent
stack_name = 'stack_name_example' # str | stackName
version = 'version_example' # str | version

try:
    # getModuleForIFVAndStack
    api_response = api_instance.get_module_for_ifv_and_stack_using_get(flavor, intent, stack_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfModuleControllerApi->get_module_for_ifv_and_stack_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavor** | **str**| flavor | 
 **intent** | **str**| intent | 
 **stack_name** | **str**| stackName | 
 **version** | **str**| version | 

### Return type

[**TFModuleResponseDTO**](TFModuleResponseDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_as_published_by_id_using_post**
> TFModule mark_as_published_by_id_using_post(id)

Mark Module as Published

- **Description:** Marks a specific module version as published. - **Permissions:** Requires MODULE_WRITE permission.  - **Audit Logging:** Yes

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
api_instance = swagger_client.UiTfModuleControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Mark Module as Published
    api_response = api_instance.mark_as_published_by_id_using_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfModuleControllerApi->mark_as_published_by_id_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**TFModule**](TFModule.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_as_published_using_post**
> TFModule mark_as_published_using_post(flavor, intent, version)

Mark Module as Published

- **Description:** Marks a specific module version as published. - **Permissions:** Requires MODULE_WRITE permission.  - **Audit Logging:** Yes

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
api_instance = swagger_client.UiTfModuleControllerApi(swagger_client.ApiClient(configuration))
flavor = 'flavor_example' # str | flavor
intent = 'intent_example' # str | intent
version = 'version_example' # str | version

try:
    # Mark Module as Published
    api_response = api_instance.mark_as_published_using_post(flavor, intent, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfModuleControllerApi->mark_as_published_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flavor** | **str**| flavor | 
 **intent** | **str**| intent | 
 **version** | **str**| version | 

### Return type

[**TFModule**](TFModule.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_module_using_post**
> TFModule upload_module_using_post(file, metadata=metadata)

Upload a module

- **Description:** Uploads a module using a file. - **Permissions:** Requires MODULE_WRITE permission. - **Parameters:**   - `file`: The module file to upload   - `metadata` (optional): Additional module metadata including:     - `gitUrl`: Web URL of the git repository (Expected to embed the commit id)     - `gitRef`: Git reference (branch, tag, or commit)     - `isFeatureBranch`: If this is true, this preview module cannot be directly marked as published until we register the module again with this as false. - **Audit Logging:** Yes

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
api_instance = swagger_client.UiTfModuleControllerApi(swagger_client.ApiClient(configuration))
file = '/path/to/file.txt' # file | file
metadata = NULL # object | metadata (optional)

try:
    # Upload a module
    api_response = api_instance.upload_module_using_post(file, metadata=metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfModuleControllerApi->upload_module_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| file | 
 **metadata** | [**object**](.md)| metadata | [optional] 

### Return type

[**TFModule**](TFModule.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

