# swagger_client.UiVersioningControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all_soft_delete_entities**](UiVersioningControllerApi.md#delete_all_soft_delete_entities) | **DELETE** /cc-ui/v1/versions/softDeletedEntities/all | 
[**delete_soft_delete_entity**](UiVersioningControllerApi.md#delete_soft_delete_entity) | **DELETE** /cc-ui/v1/versions/softDeletedEntities | 
[**get_version_by_id**](UiVersioningControllerApi.md#get_version_by_id) | **GET** /cc-ui/v1/versions/id/{id} | 
[**get_versions**](UiVersioningControllerApi.md#get_versions) | **GET** /cc-ui/v1/versions/{versioningKey} | 
[**get_versions_paginated**](UiVersioningControllerApi.md#get_versions_paginated) | **GET** /cc-ui/v1/versions/{versioningKey}/paginated | 
[**restore**](UiVersioningControllerApi.md#restore) | **POST** /cc-ui/v1/versions/{versionId}/restore | 
[**restore_soft_delete**](UiVersioningControllerApi.md#restore_soft_delete) | **POST** /cc-ui/v1/versions/softDeletedEntities/{entityId} | 
[**soft_deleted_entities**](UiVersioningControllerApi.md#soft_deleted_entities) | **GET** /cc-ui/v1/versions/softDeletedEntities | 
[**soft_deleted_entities_by_type**](UiVersioningControllerApi.md#soft_deleted_entities_by_type) | **GET** /cc-ui/v1/versions/softDeletedEntities/{entityType} | 

# **delete_all_soft_delete_entities**
> delete_all_soft_delete_entities()



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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))

try:
    api_instance.delete_all_soft_delete_entities()
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->delete_all_soft_delete_entities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_soft_delete_entity**
> delete_soft_delete_entity(id)



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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))
id = ['id_example'] # list[str] | 

try:
    api_instance.delete_soft_delete_entity(id)
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->delete_soft_delete_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_by_id**
> Version get_version_by_id(id)



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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_version_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->get_version_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Version**](Version.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions**
> list[VersionVersioned] get_versions(versioning_key, page=page, per_page=per_page)



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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))
versioning_key = 'versioning_key_example' # str | 
page = 0 # int |  (optional) (default to 0)
per_page = 10 # int |  (optional) (default to 10)

try:
    api_response = api_instance.get_versions(versioning_key, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->get_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versioning_key** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **per_page** | **int**|  | [optional] [default to 10]

### Return type

[**list[VersionVersioned]**](VersionVersioned.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions_paginated**
> PageVersionVersioned get_versions_paginated(versioning_key, page=page, per_page=per_page)



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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))
versioning_key = 'versioning_key_example' # str | 
page = 0 # int |  (optional) (default to 0)
per_page = 10 # int |  (optional) (default to 10)

try:
    api_response = api_instance.get_versions_paginated(versioning_key, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->get_versions_paginated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versioning_key** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **per_page** | **int**|  | [optional] [default to 10]

### Return type

[**PageVersionVersioned**](PageVersionVersioned.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore**
> object restore(version_id)



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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))
version_id = 'version_id_example' # str | 

try:
    api_response = api_instance.restore(version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_soft_delete**
> str restore_soft_delete(entity_id)



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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | 

try:
    api_response = api_instance.restore_soft_delete(entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->restore_soft_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **soft_deleted_entities**
> list[DeletedEntitySoftDelete] soft_deleted_entities(page=page, per_page=per_page, sort_by=sort_by)



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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))
page = 0 # int |  (optional) (default to 0)
per_page = 10 # int |  (optional) (default to 10)
sort_by = 'lastModifiedDate' # str |  (optional) (default to lastModifiedDate)

try:
    api_response = api_instance.soft_deleted_entities(page=page, per_page=per_page, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->soft_deleted_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 0]
 **per_page** | **int**|  | [optional] [default to 10]
 **sort_by** | **str**|  | [optional] [default to lastModifiedDate]

### Return type

[**list[DeletedEntitySoftDelete]**](DeletedEntitySoftDelete.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **soft_deleted_entities_by_type**
> list[DeletedEntitySoftDelete] soft_deleted_entities_by_type(entity_type, page=page, per_page=per_page, sort_by=sort_by)



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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | 
page = 0 # int |  (optional) (default to 0)
per_page = 10 # int |  (optional) (default to 10)
sort_by = 'lastModifiedDate' # str |  (optional) (default to lastModifiedDate)

try:
    api_response = api_instance.soft_deleted_entities_by_type(entity_type, page=page, per_page=per_page, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->soft_deleted_entities_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **per_page** | **int**|  | [optional] [default to 10]
 **sort_by** | **str**|  | [optional] [default to lastModifiedDate]

### Return type

[**list[DeletedEntitySoftDelete]**](DeletedEntitySoftDelete.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

