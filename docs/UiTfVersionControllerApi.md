# swagger_client.UiTfVersionControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tf_stream_for_cluster_using_delete**](UiTfVersionControllerApi.md#delete_tf_stream_for_cluster_using_delete) | **DELETE** /cc-ui/v1/terraform/cluster/{clusterId} | deleteTfStreamForCluster
[**get_all_versions_using_get**](UiTfVersionControllerApi.md#get_all_versions_using_get) | **GET** /cc-ui/v1/terraform/versions | getAllVersions
[**get_pending_migration_scripts_by_cluster_id_using_get**](UiTfVersionControllerApi.md#get_pending_migration_scripts_by_cluster_id_using_get) | **GET** /cc-ui/v1/terraform/cluster/{clusterId}/pending-migration-scripts | getPendingMigrationScriptsByClusterId
[**get_tf_stream_for_cluster_using_get**](UiTfVersionControllerApi.md#get_tf_stream_for_cluster_using_get) | **GET** /cc-ui/v1/terraform/cluster/{clusterId} | getTfStreamForCluster
[**get_tf_versions_for_stream_using_get**](UiTfVersionControllerApi.md#get_tf_versions_for_stream_using_get) | **GET** /cc-ui/v1/terraform/stream/{tfStream}/versions | getTfVersionsForStream
[**populate_release_stream_tf_version_mapping_using_post**](UiTfVersionControllerApi.md#populate_release_stream_tf_version_mapping_using_post) | **POST** /cc-ui/v1/terraform/sync-release-stream-mapping | populateReleaseStreamTfVersionMapping
[**set_tf_version_for_cluster_using_put**](UiTfVersionControllerApi.md#set_tf_version_for_cluster_using_put) | **PUT** /cc-ui/v1/terraform/cluster/{clusterId} | setTfVersionForCluster


# **delete_tf_stream_for_cluster_using_delete**
> bool delete_tf_stream_for_cluster_using_delete(cluster_id)

deleteTfStreamForCluster

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
api_instance = swagger_client.UiTfVersionControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # deleteTfStreamForCluster
    api_response = api_instance.delete_tf_stream_for_cluster_using_delete(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfVersionControllerApi->delete_tf_stream_for_cluster_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_versions_using_get**
> list[TfVersion] get_all_versions_using_get()

getAllVersions

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
api_instance = swagger_client.UiTfVersionControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllVersions
    api_response = api_instance.get_all_versions_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfVersionControllerApi->get_all_versions_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TfVersion]**](TfVersion.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pending_migration_scripts_by_cluster_id_using_get**
> PendingMigrationDetails get_pending_migration_scripts_by_cluster_id_using_get(cluster_id)

getPendingMigrationScriptsByClusterId

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
api_instance = swagger_client.UiTfVersionControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getPendingMigrationScriptsByClusterId
    api_response = api_instance.get_pending_migration_scripts_by_cluster_id_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfVersionControllerApi->get_pending_migration_scripts_by_cluster_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**PendingMigrationDetails**](PendingMigrationDetails.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tf_stream_for_cluster_using_get**
> ClusterTfVersionMapping get_tf_stream_for_cluster_using_get(cluster_id)

getTfStreamForCluster

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
api_instance = swagger_client.UiTfVersionControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getTfStreamForCluster
    api_response = api_instance.get_tf_stream_for_cluster_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfVersionControllerApi->get_tf_stream_for_cluster_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**ClusterTfVersionMapping**](ClusterTfVersionMapping.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tf_versions_for_stream_using_get**
> list[TfVersion] get_tf_versions_for_stream_using_get(tf_stream)

getTfVersionsForStream

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
api_instance = swagger_client.UiTfVersionControllerApi(swagger_client.ApiClient(configuration))
tf_stream = 'tf_stream_example' # str | tfStream

try:
    # getTfVersionsForStream
    api_response = api_instance.get_tf_versions_for_stream_using_get(tf_stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfVersionControllerApi->get_tf_versions_for_stream_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tf_stream** | **str**| tfStream | 

### Return type

[**list[TfVersion]**](TfVersion.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **populate_release_stream_tf_version_mapping_using_post**
> populate_release_stream_tf_version_mapping_using_post()

populateReleaseStreamTfVersionMapping

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
api_instance = swagger_client.UiTfVersionControllerApi(swagger_client.ApiClient(configuration))

try:
    # populateReleaseStreamTfVersionMapping
    api_instance.populate_release_stream_tf_version_mapping_using_post()
except ApiException as e:
    print("Exception when calling UiTfVersionControllerApi->populate_release_stream_tf_version_mapping_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tf_version_for_cluster_using_put**
> ClusterTfVersionMapping set_tf_version_for_cluster_using_put(cluster_id, tf_version)

setTfVersionForCluster

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
api_instance = swagger_client.UiTfVersionControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
tf_version = swagger_client.TfVersion() # TfVersion | tfVersion

try:
    # setTfVersionForCluster
    api_response = api_instance.set_tf_version_for_cluster_using_put(cluster_id, tf_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfVersionControllerApi->set_tf_version_for_cluster_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **tf_version** | [**TfVersion**](TfVersion.md)| tfVersion | 

### Return type

[**ClusterTfVersionMapping**](ClusterTfVersionMapping.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

