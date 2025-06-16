# swagger_client.UiTfVersionControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tf_stream_for_cluster**](UiTfVersionControllerApi.md#delete_tf_stream_for_cluster) | **DELETE** /cc-ui/v1/terraform/cluster/{clusterId} | 
[**get_all_versions**](UiTfVersionControllerApi.md#get_all_versions) | **GET** /cc-ui/v1/terraform/versions | 
[**get_pending_migration_scripts_by_cluster_id**](UiTfVersionControllerApi.md#get_pending_migration_scripts_by_cluster_id) | **GET** /cc-ui/v1/terraform/cluster/{clusterId}/pending-migration-scripts | 
[**get_tf_stream_for_cluster**](UiTfVersionControllerApi.md#get_tf_stream_for_cluster) | **GET** /cc-ui/v1/terraform/cluster/{clusterId} | 
[**get_tf_versions_for_stream**](UiTfVersionControllerApi.md#get_tf_versions_for_stream) | **GET** /cc-ui/v1/terraform/stream/{tfStream}/versions | 
[**populate_release_stream_tf_version_mapping**](UiTfVersionControllerApi.md#populate_release_stream_tf_version_mapping) | **POST** /cc-ui/v1/terraform/sync-release-stream-mapping | 
[**set_tf_version_for_cluster**](UiTfVersionControllerApi.md#set_tf_version_for_cluster) | **PUT** /cc-ui/v1/terraform/cluster/{clusterId} | 

# **delete_tf_stream_for_cluster**
> bool delete_tf_stream_for_cluster(cluster_id)



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
api_instance = swagger_client.UiTfVersionControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.delete_tf_stream_for_cluster(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfVersionControllerApi->delete_tf_stream_for_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_versions**
> list[ComCapillaryOpsCpBoTfVersion] get_all_versions()



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
api_instance = swagger_client.UiTfVersionControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfVersionControllerApi->get_all_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoTfVersion]**](ComCapillaryOpsCpBoTfVersion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pending_migration_scripts_by_cluster_id**
> ComCapillaryOpsCpBoPendingMigrationDetails get_pending_migration_scripts_by_cluster_id(cluster_id)



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
api_instance = swagger_client.UiTfVersionControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_pending_migration_scripts_by_cluster_id(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfVersionControllerApi->get_pending_migration_scripts_by_cluster_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoPendingMigrationDetails**](ComCapillaryOpsCpBoPendingMigrationDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tf_stream_for_cluster**
> ComCapillaryOpsCpBoClusterTfVersionMapping get_tf_stream_for_cluster(cluster_id)



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
api_instance = swagger_client.UiTfVersionControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_tf_stream_for_cluster(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfVersionControllerApi->get_tf_stream_for_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoClusterTfVersionMapping**](ComCapillaryOpsCpBoClusterTfVersionMapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tf_versions_for_stream**
> list[ComCapillaryOpsCpBoTfVersion] get_tf_versions_for_stream(tf_stream)



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
api_instance = swagger_client.UiTfVersionControllerApi(swagger_client.ApiClient(configuration))
tf_stream = 'tf_stream_example' # str | 

try:
    api_response = api_instance.get_tf_versions_for_stream(tf_stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfVersionControllerApi->get_tf_versions_for_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tf_stream** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoTfVersion]**](ComCapillaryOpsCpBoTfVersion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **populate_release_stream_tf_version_mapping**
> populate_release_stream_tf_version_mapping()



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
api_instance = swagger_client.UiTfVersionControllerApi(swagger_client.ApiClient(configuration))

try:
    api_instance.populate_release_stream_tf_version_mapping()
except ApiException as e:
    print("Exception when calling UiTfVersionControllerApi->populate_release_stream_tf_version_mapping: %s\n" % e)
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

# **set_tf_version_for_cluster**
> ComCapillaryOpsCpBoClusterTfVersionMapping set_tf_version_for_cluster(body, cluster_id)



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
api_instance = swagger_client.UiTfVersionControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoTfVersion() # ComCapillaryOpsCpBoTfVersion | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.set_tf_version_for_cluster(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTfVersionControllerApi->set_tf_version_for_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoTfVersion**](ComCapillaryOpsCpBoTfVersion.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoClusterTfVersionMapping**](ComCapillaryOpsCpBoClusterTfVersionMapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

