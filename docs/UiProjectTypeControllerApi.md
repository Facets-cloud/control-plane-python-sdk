# swagger_client.UiProjectTypeControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_project_type**](UiProjectTypeControllerApi.md#add_project_type) | **POST** /cc-ui/v1/project-types | Add a new project type
[**delete_project_type**](UiProjectTypeControllerApi.md#delete_project_type) | **DELETE** /cc-ui/v1/project-types/{id} | Delete a project type
[**get_all_project_types**](UiProjectTypeControllerApi.md#get_all_project_types) | **GET** /cc-ui/v1/project-types | Get all project types
[**get_project_type_by_id**](UiProjectTypeControllerApi.md#get_project_type_by_id) | **GET** /cc-ui/v1/project-types/{id} | Get project type by ID
[**update_project_type**](UiProjectTypeControllerApi.md#update_project_type) | **PUT** /cc-ui/v1/project-types/{id} | Update an existing project type

# **add_project_type**
> ComCapillaryOpsCpV2ProjecttypeBoProjectTypeResponse add_project_type(body)

Add a new project type

- **Description:** Creates a new project type from the provided request details.  - **Restrictions:** Only users with the appropriate permissions can add project types.  - **Permissions:** Requires `PROJECT_TYPE_WRITE` permission.  - **Audit Logging:** This operation is logged for audit purposes.

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
api_instance = swagger_client.UiProjectTypeControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpV2ProjecttypeBoProjectTypeRequest() # ComCapillaryOpsCpV2ProjecttypeBoProjectTypeRequest | 

try:
    # Add a new project type
    api_response = api_instance.add_project_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiProjectTypeControllerApi->add_project_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpV2ProjecttypeBoProjectTypeRequest**](ComCapillaryOpsCpV2ProjecttypeBoProjectTypeRequest.md)|  | 

### Return type

[**ComCapillaryOpsCpV2ProjecttypeBoProjectTypeResponse**](ComCapillaryOpsCpV2ProjecttypeBoProjectTypeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_type**
> delete_project_type(id)

Delete a project type

- **Description:** Deletes an existing project type based on its ID.  - **Restrictions:** Only users with the correct RBAC permission can delete a project type.  - **Permissions:** Requires `PROJECT_TYPE_DELETE` permission.  - **Audit Logging:** This operation is logged for audit purposes.

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
api_instance = swagger_client.UiProjectTypeControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a project type
    api_instance.delete_project_type(id)
except ApiException as e:
    print("Exception when calling UiProjectTypeControllerApi->delete_project_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_project_types**
> list[ComCapillaryOpsCpV2ProjecttypeBoProjectTypeResponse] get_all_project_types()

Get all project types

- **Description:** Retrieve a list of all existing project types.  - **Restrictions:** None.  - **Permissions:** No specific permissions required.  - **Audit Logging:** Not applicable.

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
api_instance = swagger_client.UiProjectTypeControllerApi(swagger_client.ApiClient(configuration))

try:
    # Get all project types
    api_response = api_instance.get_all_project_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiProjectTypeControllerApi->get_all_project_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpV2ProjecttypeBoProjectTypeResponse]**](ComCapillaryOpsCpV2ProjecttypeBoProjectTypeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_type_by_id**
> ComCapillaryOpsCpV2ProjecttypeBoProjectTypeResponse get_project_type_by_id(id)

Get project type by ID

- **Description:** Retrieve a specific project type by its ID.  - **Restrictions:** None.  - **Permissions:** No specific permissions required.  - **Audit Logging:** Not applicable.

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
api_instance = swagger_client.UiProjectTypeControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get project type by ID
    api_response = api_instance.get_project_type_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiProjectTypeControllerApi->get_project_type_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpV2ProjecttypeBoProjectTypeResponse**](ComCapillaryOpsCpV2ProjecttypeBoProjectTypeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_type**
> ComCapillaryOpsCpV2ProjecttypeBoProjectTypeResponse update_project_type(body, id)

Update an existing project type

- **Description:** Updates details of a specified project type by its ID.  - **Restrictions:** Only users with the correct permissions can update project types.  - **Permissions:** Requires `PROJECT_TYPE_WRITE` permission.  - **Audit Logging:** This operation is logged for audit purposes.

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
api_instance = swagger_client.UiProjectTypeControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpV2ProjecttypeBoProjectTypeRequest() # ComCapillaryOpsCpV2ProjecttypeBoProjectTypeRequest | 
id = 'id_example' # str | 

try:
    # Update an existing project type
    api_response = api_instance.update_project_type(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiProjectTypeControllerApi->update_project_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpV2ProjecttypeBoProjectTypeRequest**](ComCapillaryOpsCpV2ProjecttypeBoProjectTypeRequest.md)|  | 
 **id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpV2ProjecttypeBoProjectTypeResponse**](ComCapillaryOpsCpV2ProjecttypeBoProjectTypeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

