# swagger_client.UiProjectTypeControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_project_type_using_post**](UiProjectTypeControllerApi.md#add_project_type_using_post) | **POST** /cc-ui/v1/project-types | Add a new project type
[**delete_project_type_using_delete**](UiProjectTypeControllerApi.md#delete_project_type_using_delete) | **DELETE** /cc-ui/v1/project-types/{id} | Delete a project type
[**get_all_project_types_using_get**](UiProjectTypeControllerApi.md#get_all_project_types_using_get) | **GET** /cc-ui/v1/project-types | Get all project types
[**get_project_type_by_id_using_get**](UiProjectTypeControllerApi.md#get_project_type_by_id_using_get) | **GET** /cc-ui/v1/project-types/{id} | Get project type by ID
[**update_project_type_using_put**](UiProjectTypeControllerApi.md#update_project_type_using_put) | **PUT** /cc-ui/v1/project-types/{id} | Update an existing project type

# **add_project_type_using_post**
> ProjectTypeResponse add_project_type_using_post(body)

Add a new project type

- **Description:** Creates a new project type from the provided request details.  - **Restrictions:** Only users with the appropriate permissions can add project types.  - **Permissions:** Requires `PROJECT_TYPE_WRITE` permission.  - **Audit Logging:** This operation is logged for audit purposes.

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
api_instance = swagger_client.UiProjectTypeControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProjectTypeRequest() # ProjectTypeRequest | projectTypeRequest

try:
    # Add a new project type
    api_response = api_instance.add_project_type_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiProjectTypeControllerApi->add_project_type_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectTypeRequest**](ProjectTypeRequest.md)| projectTypeRequest | 

### Return type

[**ProjectTypeResponse**](ProjectTypeResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_type_using_delete**
> delete_project_type_using_delete(id)

Delete a project type

- **Description:** Deletes an existing project type based on its ID.  - **Restrictions:** Only users with the correct RBAC permission can delete a project type.  - **Permissions:** Requires `PROJECT_TYPE_DELETE` permission.  - **Audit Logging:** This operation is logged for audit purposes.

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
api_instance = swagger_client.UiProjectTypeControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Delete a project type
    api_instance.delete_project_type_using_delete(id)
except ApiException as e:
    print("Exception when calling UiProjectTypeControllerApi->delete_project_type_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_project_types_using_get**
> list[ProjectTypeResponse] get_all_project_types_using_get()

Get all project types

- **Description:** Retrieve a list of all existing project types.  - **Restrictions:** None.  - **Permissions:** No specific permissions required.  - **Audit Logging:** Not applicable.

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
api_instance = swagger_client.UiProjectTypeControllerApi(swagger_client.ApiClient(configuration))

try:
    # Get all project types
    api_response = api_instance.get_all_project_types_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiProjectTypeControllerApi->get_all_project_types_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProjectTypeResponse]**](ProjectTypeResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_type_by_id_using_get**
> ProjectTypeResponse get_project_type_by_id_using_get(id)

Get project type by ID

- **Description:** Retrieve a specific project type by its ID.  - **Restrictions:** None.  - **Permissions:** No specific permissions required.  - **Audit Logging:** Not applicable.

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
api_instance = swagger_client.UiProjectTypeControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # Get project type by ID
    api_response = api_instance.get_project_type_by_id_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiProjectTypeControllerApi->get_project_type_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**ProjectTypeResponse**](ProjectTypeResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_type_using_put**
> ProjectTypeResponse update_project_type_using_put(body, id)

Update an existing project type

- **Description:** Updates details of a specified project type by its ID.  - **Restrictions:** Only users with the correct permissions can update project types.  - **Permissions:** Requires `PROJECT_TYPE_WRITE` permission.  - **Audit Logging:** This operation is logged for audit purposes.

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
api_instance = swagger_client.UiProjectTypeControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProjectTypeRequest() # ProjectTypeRequest | projectTypeRequest
id = 'id_example' # str | id

try:
    # Update an existing project type
    api_response = api_instance.update_project_type_using_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiProjectTypeControllerApi->update_project_type_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectTypeRequest**](ProjectTypeRequest.md)| projectTypeRequest | 
 **id** | **str**| id | 

### Return type

[**ProjectTypeResponse**](ProjectTypeResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

