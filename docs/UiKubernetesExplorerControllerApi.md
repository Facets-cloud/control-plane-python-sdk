# swagger_client.UiKubernetesExplorerControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**container_logs**](UiKubernetesExplorerControllerApi.md#container_logs) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/pods/{podName}/{containerName}/logs | 
[**get_all_ingress_rules_for_cluster**](UiKubernetesExplorerControllerApi.md#get_all_ingress_rules_for_cluster) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/ingress-rules | 
[**get_config_map_data**](UiKubernetesExplorerControllerApi.md#get_config_map_data) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/configMaps/{configMapName} | 
[**get_manifest**](UiKubernetesExplorerControllerApi.md#get_manifest) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/{k8sResourceType}/{k8sResourceName}/manifest | 
[**get_pods_for_deployment**](UiKubernetesExplorerControllerApi.md#get_pods_for_deployment) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/deployments/{deploymentName} | 
[**get_secrets_data**](UiKubernetesExplorerControllerApi.md#get_secrets_data) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/secrets/{secretName} | 
[**list_config_map_by_labels**](UiKubernetesExplorerControllerApi.md#list_config_map_by_labels) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/configMaps | 
[**list_containers_in_pod**](UiKubernetesExplorerControllerApi.md#list_containers_in_pod) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/{podName}/containers | 
[**list_containers_in_pod_v2**](UiKubernetesExplorerControllerApi.md#list_containers_in_pod_v2) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/{podName}/v2/containers | 
[**list_cron_job_by_labels**](UiKubernetesExplorerControllerApi.md#list_cron_job_by_labels) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/cronJobs | 
[**list_daemon_sets_by_labels**](UiKubernetesExplorerControllerApi.md#list_daemon_sets_by_labels) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/daemonSets | 
[**list_deployments_by_labels**](UiKubernetesExplorerControllerApi.md#list_deployments_by_labels) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/deployments | 
[**list_events_by_k8s_resource**](UiKubernetesExplorerControllerApi.md#list_events_by_k8s_resource) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/{k8sResourceType}/{k8sResourceName}/events | 
[**list_hpa_by_labels**](UiKubernetesExplorerControllerApi.md#list_hpa_by_labels) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/hpa | 
[**list_ingresses_by_labels**](UiKubernetesExplorerControllerApi.md#list_ingresses_by_labels) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/ingresses | 
[**list_jobs_by_labels**](UiKubernetesExplorerControllerApi.md#list_jobs_by_labels) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/jobs | 
[**list_pods_by_labels**](UiKubernetesExplorerControllerApi.md#list_pods_by_labels) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/pods | 
[**list_pvby_labels**](UiKubernetesExplorerControllerApi.md#list_pvby_labels) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/pv | 
[**list_pvcby_labels**](UiKubernetesExplorerControllerApi.md#list_pvcby_labels) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/pvc | 
[**list_replicasets_by_labels**](UiKubernetesExplorerControllerApi.md#list_replicasets_by_labels) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/replicasets | 
[**list_secrets_by_labels**](UiKubernetesExplorerControllerApi.md#list_secrets_by_labels) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/secrets | 
[**list_services_by_labels**](UiKubernetesExplorerControllerApi.md#list_services_by_labels) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/services | 
[**list_statefulsets_labels_by_labels**](UiKubernetesExplorerControllerApi.md#list_statefulsets_labels_by_labels) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/statefulsets | 

# **container_logs**
> OrgSpringframeworkWebServletMvcMethodAnnotationStreamingResponseBody container_logs(cluster_id, pod_name, container_name, tail, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
pod_name = 'pod_name_example' # str | 
container_name = 'container_name_example' # str | 
tail = 56 # int | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.container_logs(cluster_id, pod_name, container_name, tail, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->container_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **pod_name** | **str**|  | 
 **container_name** | **str**|  | 
 **tail** | **int**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**OrgSpringframeworkWebServletMvcMethodAnnotationStreamingResponseBody**](OrgSpringframeworkWebServletMvcMethodAnnotationStreamingResponseBody.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ingress_rules_for_cluster**
> list[ComCapillaryOpsCpBoK8sDtoIngressRulesDTO] get_all_ingress_rules_for_cluster(cluster_id)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_all_ingress_rules_for_cluster(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->get_all_ingress_rules_for_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoIngressRulesDTO]**](ComCapillaryOpsCpBoK8sDtoIngressRulesDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_map_data**
> object get_config_map_data(cluster_id, config_map_name, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
config_map_name = 'config_map_name_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.get_config_map_data(cluster_id, config_map_name, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->get_config_map_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **config_map_name** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manifest**
> str get_manifest(cluster_id, k8s_resource_type, k8s_resource_name, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
k8s_resource_type = 'k8s_resource_type_example' # str | 
k8s_resource_name = 'k8s_resource_name_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.get_manifest(cluster_id, k8s_resource_type, k8s_resource_name, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->get_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **k8s_resource_type** | **str**|  | 
 **k8s_resource_name** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pods_for_deployment**
> list[str] get_pods_for_deployment(cluster_id, deployment_name, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
deployment_name = 'deployment_name_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.get_pods_for_deployment(cluster_id, deployment_name, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->get_pods_for_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **deployment_name** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secrets_data**
> object get_secrets_data(cluster_id, secret_name, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
secret_name = 'secret_name_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.get_secrets_data(cluster_id, secret_name, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->get_secrets_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **secret_name** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_config_map_by_labels**
> list[ComCapillaryOpsCpBoK8sDtoConfigMapDTO] list_config_map_by_labels(cluster_id, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_config_map_by_labels(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_config_map_by_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoConfigMapDTO]**](ComCapillaryOpsCpBoK8sDtoConfigMapDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_containers_in_pod**
> list[IoFabric8KubernetesApiModelContainer] list_containers_in_pod(cluster_id, pod_name, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
pod_name = 'pod_name_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_containers_in_pod(cluster_id, pod_name, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_containers_in_pod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **pod_name** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[IoFabric8KubernetesApiModelContainer]**](IoFabric8KubernetesApiModelContainer.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_containers_in_pod_v2**
> list[ComCapillaryOpsCpBoK8sDtoContainerDTO] list_containers_in_pod_v2(cluster_id, pod_name, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
pod_name = 'pod_name_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_containers_in_pod_v2(cluster_id, pod_name, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_containers_in_pod_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **pod_name** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoContainerDTO]**](ComCapillaryOpsCpBoK8sDtoContainerDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cron_job_by_labels**
> list[ComCapillaryOpsCpBoK8sDtoCronJobDTO] list_cron_job_by_labels(cluster_id, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_cron_job_by_labels(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_cron_job_by_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoCronJobDTO]**](ComCapillaryOpsCpBoK8sDtoCronJobDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_daemon_sets_by_labels**
> list[ComCapillaryOpsCpBoK8sDtoDaemonSetDTO] list_daemon_sets_by_labels(cluster_id, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_daemon_sets_by_labels(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_daemon_sets_by_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoDaemonSetDTO]**](ComCapillaryOpsCpBoK8sDtoDaemonSetDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployments_by_labels**
> list[ComCapillaryOpsCpBoK8sDtoDeploymentDTO] list_deployments_by_labels(cluster_id, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_deployments_by_labels(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_deployments_by_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoDeploymentDTO]**](ComCapillaryOpsCpBoK8sDtoDeploymentDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_events_by_k8s_resource**
> list[ComCapillaryOpsCpBoK8sDtoEventDTO] list_events_by_k8s_resource(cluster_id, k8s_resource_type, k8s_resource_name, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
k8s_resource_type = 'k8s_resource_type_example' # str | 
k8s_resource_name = 'k8s_resource_name_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_events_by_k8s_resource(cluster_id, k8s_resource_type, k8s_resource_name, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_events_by_k8s_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **k8s_resource_type** | **str**|  | 
 **k8s_resource_name** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoEventDTO]**](ComCapillaryOpsCpBoK8sDtoEventDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hpa_by_labels**
> list[ComCapillaryOpsCpBoK8sDtoHorizontalPodAutoscalerDTO] list_hpa_by_labels(cluster_id, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_hpa_by_labels(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_hpa_by_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoHorizontalPodAutoscalerDTO]**](ComCapillaryOpsCpBoK8sDtoHorizontalPodAutoscalerDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ingresses_by_labels**
> list[ComCapillaryOpsCpBoK8sDtoIngressDTO] list_ingresses_by_labels(cluster_id, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_ingresses_by_labels(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_ingresses_by_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoIngressDTO]**](ComCapillaryOpsCpBoK8sDtoIngressDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs_by_labels**
> list[ComCapillaryOpsCpBoK8sDtoJobDTO] list_jobs_by_labels(cluster_id, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_jobs_by_labels(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_jobs_by_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoJobDTO]**](ComCapillaryOpsCpBoK8sDtoJobDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pods_by_labels**
> list[ComCapillaryOpsCpBoK8sDtoPodDTO] list_pods_by_labels(cluster_id, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_pods_by_labels(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_pods_by_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoPodDTO]**](ComCapillaryOpsCpBoK8sDtoPodDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pvby_labels**
> list[ComCapillaryOpsCpBoK8sDtoPersistentVolumeDTO] list_pvby_labels(cluster_id, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_pvby_labels(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_pvby_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoPersistentVolumeDTO]**](ComCapillaryOpsCpBoK8sDtoPersistentVolumeDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pvcby_labels**
> list[ComCapillaryOpsCpBoK8sDtoPersistentVolumeClaimDTO] list_pvcby_labels(cluster_id, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_pvcby_labels(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_pvcby_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoPersistentVolumeClaimDTO]**](ComCapillaryOpsCpBoK8sDtoPersistentVolumeClaimDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replicasets_by_labels**
> list[ComCapillaryOpsCpBoK8sDtoReplicasetDTO] list_replicasets_by_labels(cluster_id, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_replicasets_by_labels(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_replicasets_by_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoReplicasetDTO]**](ComCapillaryOpsCpBoK8sDtoReplicasetDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_secrets_by_labels**
> list[ComCapillaryOpsCpBoK8sDtoSecretDTO] list_secrets_by_labels(cluster_id, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_secrets_by_labels(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_secrets_by_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoSecretDTO]**](ComCapillaryOpsCpBoK8sDtoSecretDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_services_by_labels**
> list[ComCapillaryOpsCpBoK8sDtoServiceDTO] list_services_by_labels(cluster_id)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.list_services_by_labels(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_services_by_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoServiceDTO]**](ComCapillaryOpsCpBoK8sDtoServiceDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_statefulsets_labels_by_labels**
> list[ComCapillaryOpsCpBoK8sDtoStatefulSetDTO] list_statefulsets_labels_by_labels(cluster_id, labels)



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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
labels = {'key': 'labels_example'} # dict(str, str) | 

try:
    api_response = api_instance.list_statefulsets_labels_by_labels(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_statefulsets_labels_by_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **labels** | [**dict(str, str)**](str.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoK8sDtoStatefulSetDTO]**](ComCapillaryOpsCpBoK8sDtoStatefulSetDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

