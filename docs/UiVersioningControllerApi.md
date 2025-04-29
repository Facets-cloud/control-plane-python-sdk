# swagger_client.UiVersioningControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all_soft_delete_entities_using_delete**](UiVersioningControllerApi.md#delete_all_soft_delete_entities_using_delete) | **DELETE** /cc-ui/v1/versions/softDeletedEntities/all | deleteAllSoftDeleteEntities
[**delete_soft_delete_entity_using_delete**](UiVersioningControllerApi.md#delete_soft_delete_entity_using_delete) | **DELETE** /cc-ui/v1/versions/softDeletedEntities | deleteSoftDeleteEntity
[**get_version_by_id_using_get**](UiVersioningControllerApi.md#get_version_by_id_using_get) | **GET** /cc-ui/v1/versions/id/{id} | getVersionById
[**get_versions_using_get**](UiVersioningControllerApi.md#get_versions_using_get) | **GET** /cc-ui/v1/versions/{versioningKey} | getVersions
[**restore_soft_delete_using_post**](UiVersioningControllerApi.md#restore_soft_delete_using_post) | **POST** /cc-ui/v1/versions/softDeletedEntities/{entityId} | restoreSoftDelete
[**restore_using_post**](UiVersioningControllerApi.md#restore_using_post) | **POST** /cc-ui/v1/versions/{versionId}/restore | restore
[**soft_deleted_entities_by_type_using_get**](UiVersioningControllerApi.md#soft_deleted_entities_by_type_using_get) | **GET** /cc-ui/v1/versions/softDeletedEntities/{entityType} | softDeletedEntitiesByType
[**soft_deleted_entities_using_get**](UiVersioningControllerApi.md#soft_deleted_entities_using_get) | **GET** /cc-ui/v1/versions/softDeletedEntities | softDeletedEntities

# **delete_all_soft_delete_entities_using_delete**
> delete_all_soft_delete_entities_using_delete()

deleteAllSoftDeleteEntities

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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))

try:
    # deleteAllSoftDeleteEntities
    api_instance.delete_all_soft_delete_entities_using_delete()
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->delete_all_soft_delete_entities_using_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_soft_delete_entity_using_delete**
> delete_soft_delete_entity_using_delete(id)

deleteSoftDeleteEntity

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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))
id = ['id_example'] # list[str] | id

try:
    # deleteSoftDeleteEntity
    api_instance.delete_soft_delete_entity_using_delete(id)
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->delete_soft_delete_entity_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| id | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_by_id_using_get**
> Version get_version_by_id_using_get(id)

getVersionById

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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # getVersionById
    api_response = api_instance.get_version_by_id_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->get_version_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**Version**](Version.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions_using_get**
> list[Version] get_versions_using_get(versioning_key, page=page, per_page=per_page)

getVersions

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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))
versioning_key = 'versioning_key_example' # str | versioningKey
page = 0 # int | page (optional) (default to 0)
per_page = 10 # int | perPage (optional) (default to 10)

try:
    # getVersions
    api_response = api_instance.get_versions_using_get(versioning_key, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->get_versions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versioning_key** | **str**| versioningKey | 
 **page** | **int**| page | [optional] [default to 0]
 **per_page** | **int**| perPage | [optional] [default to 10]

### Return type

[**list[Version]**](Version.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_soft_delete_using_post**
> str restore_soft_delete_using_post(entity_id)

restoreSoftDelete

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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | entityId

try:
    # restoreSoftDelete
    api_response = api_instance.restore_soft_delete_using_post(entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->restore_soft_delete_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| entityId | 

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_using_post**
> object restore_using_post(version_id)

restore

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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))
version_id = 'version_id_example' # str | versionId

try:
    # restore
    api_response = api_instance.restore_using_post(version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->restore_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_id** | **str**| versionId | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **soft_deleted_entities_by_type_using_get**
> list[DeletedEntity] soft_deleted_entities_by_type_using_get(entity_type, page=page, per_page=per_page, sort_by=sort_by)

softDeletedEntitiesByType

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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))
entity_type = 'entity_type_example' # str | entityType
page = 0 # int | page (optional) (default to 0)
per_page = 10 # int | perPage (optional) (default to 10)
sort_by = 'lastModifiedDate' # str | sortBy (optional) (default to lastModifiedDate)

try:
    # softDeletedEntitiesByType
    api_response = api_instance.soft_deleted_entities_by_type_using_get(entity_type, page=page, per_page=per_page, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->soft_deleted_entities_by_type_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| entityType | 
 **page** | **int**| page | [optional] [default to 0]
 **per_page** | **int**| perPage | [optional] [default to 10]
 **sort_by** | **str**| sortBy | [optional] [default to lastModifiedDate]

### Return type

[**list[DeletedEntity]**](DeletedEntity.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **soft_deleted_entities_using_get**
> list[DeletedEntity] soft_deleted_entities_using_get(page=page, per_page=per_page, sort_by=sort_by)

softDeletedEntities

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
api_instance = swagger_client.UiVersioningControllerApi(swagger_client.ApiClient(configuration))
page = 0 # int | page (optional) (default to 0)
per_page = 10 # int | perPage (optional) (default to 10)
sort_by = 'lastModifiedDate' # str | sortBy (optional) (default to lastModifiedDate)

try:
    # softDeletedEntities
    api_response = api_instance.soft_deleted_entities_using_get(page=page, per_page=per_page, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiVersioningControllerApi->soft_deleted_entities_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page | [optional] [default to 0]
 **per_page** | **int**| perPage | [optional] [default to 10]
 **sort_by** | **str**| sortBy | [optional] [default to lastModifiedDate]

### Return type

[**list[DeletedEntity]**](DeletedEntity.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

