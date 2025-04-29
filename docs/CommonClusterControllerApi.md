# swagger_client.CommonClusterControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cluster_k8s_credentials_using_post**](CommonClusterControllerApi.md#add_cluster_k8s_credentials_using_post) | **POST** /cc/v1/clusters/{clusterId}/credentials | addClusterK8sCredentials
[**delete_cluster_using_delete**](CommonClusterControllerApi.md#delete_cluster_using_delete) | **DELETE** /cc/v1/clusters/{clusterId} | deleteCluster
[**get_overrides_using_get**](CommonClusterControllerApi.md#get_overrides_using_get) | **GET** /cc/v1/clusters/{clusterId}/overrides | getOverrides
[**get_pinned_snapshot_using_get**](CommonClusterControllerApi.md#get_pinned_snapshot_using_get) | **GET** /cc/v1/clusters/{clusterId}/dr/{resourceType}/snapshots/{instanceName}/pinnedSnapshot | getPinnedSnapshot
[**list_snapshots_using_get**](CommonClusterControllerApi.md#list_snapshots_using_get) | **GET** /cc/v1/clusters/{clusterId}/dr/{resourceType}/snapshots/{instanceName} | listSnapshots
[**notify_alerts_using_post**](CommonClusterControllerApi.md#notify_alerts_using_post) | **POST** /cc/v1/clusters/{clusterId}/alerts | notifyAlerts
[**notify_application_deployment_complete_using_post**](CommonClusterControllerApi.md#notify_application_deployment_complete_using_post) | **POST** /cc/v1/clusters/{clusterId}/app-name/{appName}/application-deployment-completed | notifyApplicationDeploymentComplete
[**notify_resource_deployment_complete_using_post**](CommonClusterControllerApi.md#notify_resource_deployment_complete_using_post) | **POST** /cc/v1/clusters/{clusterId}/resource-type/{resourceType}/resource-name/{resourceName}/resource-deployment-completed | notifyResourceDeploymentComplete
[**override_sizing_using_post**](CommonClusterControllerApi.md#override_sizing_using_post) | **POST** /cc/v1/clusters/{clusterId}/overrides | overrideSizing
[**pin_snapshot_using_post**](CommonClusterControllerApi.md#pin_snapshot_using_post) | **POST** /cc/v1/clusters/{clusterId}/dr/{resourceType}/snapshots/{instanceName}/pinnedSnapshot | pinSnapshot
[**upsert_vars_using_post**](CommonClusterControllerApi.md#upsert_vars_using_post) | **POST** /cc/v1/clusters/{clusterId}/vars/upsert | upsertVars

# **add_cluster_k8s_credentials_using_post**
> bool add_cluster_k8s_credentials_using_post(body, cluster_id)

addClusterK8sCredentials

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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.K8sCredentials() # K8sCredentials | request
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # addClusterK8sCredentials
    api_response = api_instance.add_cluster_k8s_credentials_using_post(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->add_cluster_k8s_credentials_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**K8sCredentials**](K8sCredentials.md)| request | 
 **cluster_id** | **str**| clusterId | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_using_delete**
> bool delete_cluster_using_delete(cluster_id)

deleteCluster

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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # deleteCluster
    api_response = api_instance.delete_cluster_using_delete(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->delete_cluster_using_delete: %s\n" % e)
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

# **get_overrides_using_get**
> list[OverrideObject] get_overrides_using_get(cluster_id)

getOverrides

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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getOverrides
    api_response = api_instance.get_overrides_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->get_overrides_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**list[OverrideObject]**](OverrideObject.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pinned_snapshot_using_get**
> SnapshotInfo get_pinned_snapshot_using_get(cluster_id, instance_name, resource_type)

getPinnedSnapshot

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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
instance_name = 'instance_name_example' # str | instanceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # getPinnedSnapshot
    api_response = api_instance.get_pinned_snapshot_using_get(cluster_id, instance_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->get_pinned_snapshot_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **instance_name** | **str**| instanceName | 
 **resource_type** | **str**| resourceType | 

### Return type

[**SnapshotInfo**](SnapshotInfo.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshots_using_get**
> list[SnapshotInfo] list_snapshots_using_get(cluster_id, instance_name, resource_type)

listSnapshots

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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
instance_name = 'instance_name_example' # str | instanceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # listSnapshots
    api_response = api_instance.list_snapshots_using_get(cluster_id, instance_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->list_snapshots_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **instance_name** | **str**| instanceName | 
 **resource_type** | **str**| resourceType | 

### Return type

[**list[SnapshotInfo]**](SnapshotInfo.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_alerts_using_post**
> bool notify_alerts_using_post(body, cluster_id)

notifyAlerts

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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Response() # Response | alerts
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # notifyAlerts
    api_response = api_instance.notify_alerts_using_post(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->notify_alerts_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Response**](Response.md)| alerts | 
 **cluster_id** | **str**| clusterId | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_application_deployment_complete_using_post**
> bool notify_application_deployment_complete_using_post(app_name, cluster_id, build_id=build_id, deployment_status=deployment_status)

notifyApplicationDeploymentComplete

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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
app_name = 'app_name_example' # str | appName
cluster_id = 'cluster_id_example' # str | clusterId
build_id = 'build_id_example' # str | buildId (optional)
deployment_status = 'deployment_status_example' # str | deploymentStatus (optional)

try:
    # notifyApplicationDeploymentComplete
    api_response = api_instance.notify_application_deployment_complete_using_post(app_name, cluster_id, build_id=build_id, deployment_status=deployment_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->notify_application_deployment_complete_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| appName | 
 **cluster_id** | **str**| clusterId | 
 **build_id** | **str**| buildId | [optional] 
 **deployment_status** | **str**| deploymentStatus | [optional] 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notify_resource_deployment_complete_using_post**
> notify_resource_deployment_complete_using_post(cluster_id, deployment_status, resource_name, resource_type, build_id=build_id)

notifyResourceDeploymentComplete

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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
deployment_status = 'deployment_status_example' # str | deploymentStatus
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
build_id = 'build_id_example' # str | buildId (optional)

try:
    # notifyResourceDeploymentComplete
    api_instance.notify_resource_deployment_complete_using_post(cluster_id, deployment_status, resource_name, resource_type, build_id=build_id)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->notify_resource_deployment_complete_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **deployment_status** | **str**| deploymentStatus | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **build_id** | **str**| buildId | [optional] 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **override_sizing_using_post**
> list[OverrideObject] override_sizing_using_post(body, cluster_id)

overrideSizing

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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.OverrideRequest()] # list[OverrideRequest] | request
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # overrideSizing
    api_response = api_instance.override_sizing_using_post(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->override_sizing_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[OverrideRequest]**](OverrideRequest.md)| request | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**list[OverrideObject]**](OverrideObject.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pin_snapshot_using_post**
> SnapshotInfo pin_snapshot_using_post(body, cluster_id, instance_name, resource_type)

pinSnapshot

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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.SnapshotInfo() # SnapshotInfo | snapshotInfo
cluster_id = 'cluster_id_example' # str | clusterId
instance_name = 'instance_name_example' # str | instanceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # pinSnapshot
    api_response = api_instance.pin_snapshot_using_post(body, cluster_id, instance_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->pin_snapshot_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SnapshotInfo**](SnapshotInfo.md)| snapshotInfo | 
 **cluster_id** | **str**| clusterId | 
 **instance_name** | **str**| instanceName | 
 **resource_type** | **str**| resourceType | 

### Return type

[**SnapshotInfo**](SnapshotInfo.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_vars_using_post**
> dict(str, str) upsert_vars_using_post(body, cluster_id)

upsertVars

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
api_instance = swagger_client.CommonClusterControllerApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, str) | clusterVars
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # upsertVars
    api_response = api_instance.upsert_vars_using_post(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonClusterControllerApi->upsert_vars_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, str)**](dict.md)| clusterVars | 
 **cluster_id** | **str**| clusterId | 

### Return type

**dict(str, str)**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

