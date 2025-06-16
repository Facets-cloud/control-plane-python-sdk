# swagger_client.CommonClusterControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cluster_k8s_credentials**](CommonClusterControllerApi.md#add_cluster_k8s_credentials) | **POST** /cc/v1/clusters/{clusterId}/credentials | 
[**delete_cluster**](CommonClusterControllerApi.md#delete_cluster) | **DELETE** /cc/v1/clusters/{clusterId} | 
[**get_overrides**](CommonClusterControllerApi.md#get_overrides) | **GET** /cc/v1/clusters/{clusterId}/overrides | 
[**get_pinned_snapshot**](CommonClusterControllerApi.md#get_pinned_snapshot) | **GET** /cc/v1/clusters/{clusterId}/dr/{resourceType}/snapshots/{instanceName}/pinnedSnapshot | 
[**list_snapshots**](CommonClusterControllerApi.md#list_snapshots) | **GET** /cc/v1/clusters/{clusterId}/dr/{resourceType}/snapshots/{instanceName} | 
[**notify_alerts**](CommonClusterControllerApi.md#notify_alerts) | **POST** /cc/v1/clusters/{clusterId}/alerts | 
[**notify_application_deployment_complete**](CommonClusterControllerApi.md#notify_application_deployment_complete) | **POST** /cc/v1/clusters/{clusterId}/app-name/{appName}/application-deployment-completed | 
[**notify_resource_deployment_complete**](CommonClusterControllerApi.md#notify_resource_deployment_complete) | **POST** /cc/v1/clusters/{clusterId}/resource-type/{resourceType}/resource-name/{resourceName}/resource-deployment-completed | 
[**override_sizing**](CommonClusterControllerApi.md#override_sizing) | **POST** /cc/v1/clusters/{clusterId}/overrides | 
[**pin_snapshot**](CommonClusterControllerApi.md#pin_snapshot) | **POST** /cc/v1/clusters/{clusterId}/dr/{resourceType}/snapshots/{instanceName}/pinnedSnapshot | 
[**upsert_vars**](CommonClusterControllerApi.md#upsert_vars) | **POST** /cc/v1/clusters/{clusterId}/vars/upsert | 

# **add_cluster_k8s_credentials**
> bool add_cluster_k8s_credentials(body, cluster_id)



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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoK8sCredentials() # ComCapillaryOpsCpBoK8sCredentials | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.add_cluster_k8s_credentials(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->add_cluster_k8s_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoK8sCredentials**](ComCapillaryOpsCpBoK8sCredentials.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster**
> bool delete_cluster(cluster_id)



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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.delete_cluster(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->delete_cluster: %s\n" % e)
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

# **get_overrides**
> list[ComCapillaryOpsCpBoOverrideObject] get_overrides(cluster_id)



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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_overrides(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->get_overrides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoOverrideObject]**](ComCapillaryOpsCpBoOverrideObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pinned_snapshot**
> ComCapillaryOpsCpBoSnapshotInfo get_pinned_snapshot(cluster_id, resource_type, instance_name)



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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
instance_name = 'instance_name_example' # str | 

try:
    api_response = api_instance.get_pinned_snapshot(cluster_id, resource_type, instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->get_pinned_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **instance_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoSnapshotInfo**](ComCapillaryOpsCpBoSnapshotInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshots**
> list[ComCapillaryOpsCpBoSnapshotInfo] list_snapshots(cluster_id, resource_type, instance_name)



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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
instance_name = 'instance_name_example' # str | 

try:
    api_response = api_instance.list_snapshots(cluster_id, resource_type, instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->list_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **instance_name** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoSnapshotInfo]**](ComCapillaryOpsCpBoSnapshotInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_alerts**
> bool notify_alerts(body, cluster_id)



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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAlertManagerPayloadResponse() # ComCapillaryOpsCpBoAlertManagerPayloadResponse | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.notify_alerts(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->notify_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAlertManagerPayloadResponse**](ComCapillaryOpsCpBoAlertManagerPayloadResponse.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_application_deployment_complete**
> bool notify_application_deployment_complete(cluster_id, app_name, deployment_status=deployment_status, build_id=build_id)



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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
app_name = 'app_name_example' # str | 
deployment_status = 'deployment_status_example' # str |  (optional)
build_id = 'build_id_example' # str |  (optional)

try:
    api_response = api_instance.notify_application_deployment_complete(cluster_id, app_name, deployment_status=deployment_status, build_id=build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->notify_application_deployment_complete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **app_name** | **str**|  | 
 **deployment_status** | **str**|  | [optional] 
 **build_id** | **str**|  | [optional] 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_resource_deployment_complete**
> notify_resource_deployment_complete(cluster_id, resource_type, resource_name, deployment_status, build_id=build_id)



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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 
deployment_status = 'deployment_status_example' # str | 
build_id = 'build_id_example' # str |  (optional)

try:
    api_instance.notify_resource_deployment_complete(cluster_id, resource_type, resource_name, deployment_status, build_id=build_id)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->notify_resource_deployment_complete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 
 **deployment_status** | **str**|  | 
 **build_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **override_sizing**
> list[ComCapillaryOpsCpBoOverrideObject] override_sizing(body, cluster_id)



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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ComCapillaryOpsCpBoRequestsOverrideRequest()] # list[ComCapillaryOpsCpBoRequestsOverrideRequest] | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.override_sizing(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->override_sizing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ComCapillaryOpsCpBoRequestsOverrideRequest]**](ComCapillaryOpsCpBoRequestsOverrideRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoOverrideObject]**](ComCapillaryOpsCpBoOverrideObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pin_snapshot**
> ComCapillaryOpsCpBoSnapshotInfo pin_snapshot(body, cluster_id, resource_type, instance_name)



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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoSnapshotInfo() # ComCapillaryOpsCpBoSnapshotInfo | 
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
instance_name = 'instance_name_example' # str | 

try:
    api_response = api_instance.pin_snapshot(body, cluster_id, resource_type, instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->pin_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoSnapshotInfo**](ComCapillaryOpsCpBoSnapshotInfo.md)|  | 
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **instance_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoSnapshotInfo**](ComCapillaryOpsCpBoSnapshotInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_vars**
> dict(str, str) upsert_vars(body, cluster_id)



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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, str) | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.upsert_vars(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->upsert_vars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, str)**](dict.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

**dict(str, str)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

