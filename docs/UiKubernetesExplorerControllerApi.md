# swagger_client.UiKubernetesExplorerControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**container_logs_using_get**](UiKubernetesExplorerControllerApi.md#container_logs_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/pods/{podName}/{containerName}/logs | containerLogs
[**get_all_ingress_rules_for_cluster_using_get**](UiKubernetesExplorerControllerApi.md#get_all_ingress_rules_for_cluster_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/ingress-rules | getAllIngressRulesForCluster
[**get_config_map_data_using_get**](UiKubernetesExplorerControllerApi.md#get_config_map_data_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/configMaps/{configMapName} | getConfigMapData
[**get_manifest_using_get**](UiKubernetesExplorerControllerApi.md#get_manifest_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/{k8sResourceType}/{k8sResourceName}/manifest | getManifest
[**get_pods_for_deployment_using_get**](UiKubernetesExplorerControllerApi.md#get_pods_for_deployment_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/deployments/{deploymentName} | getPodsForDeployment
[**get_secrets_data_using_get**](UiKubernetesExplorerControllerApi.md#get_secrets_data_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/secrets/{secretName} | getSecretsData
[**list_config_map_by_labels_using_get**](UiKubernetesExplorerControllerApi.md#list_config_map_by_labels_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/configMaps | listConfigMapByLabels
[**list_containers_in_pod_using_get**](UiKubernetesExplorerControllerApi.md#list_containers_in_pod_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/{podName}/containers | listContainersInPod
[**list_containers_in_pod_v2_using_get**](UiKubernetesExplorerControllerApi.md#list_containers_in_pod_v2_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/{podName}/v2/containers | listContainersInPodV2
[**list_cron_job_by_labels_using_get**](UiKubernetesExplorerControllerApi.md#list_cron_job_by_labels_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/cronJobs | listCronJobByLabels
[**list_daemon_sets_by_labels_using_get**](UiKubernetesExplorerControllerApi.md#list_daemon_sets_by_labels_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/daemonSets | listDaemonSetsByLabels
[**list_deployments_by_labels_using_get**](UiKubernetesExplorerControllerApi.md#list_deployments_by_labels_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/deployments | listDeploymentsByLabels
[**list_events_by_k8s_resource_using_get**](UiKubernetesExplorerControllerApi.md#list_events_by_k8s_resource_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/{k8sResourceType}/{k8sResourceName}/events | listEventsByK8sResource
[**list_hpa_by_labels_using_get**](UiKubernetesExplorerControllerApi.md#list_hpa_by_labels_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/hpa | listHpaByLabels
[**list_ingresses_by_labels_using_get**](UiKubernetesExplorerControllerApi.md#list_ingresses_by_labels_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/ingresses | listIngressesByLabels
[**list_jobs_by_labels_using_get**](UiKubernetesExplorerControllerApi.md#list_jobs_by_labels_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/jobs | listJobsByLabels
[**list_pods_by_labels_using_get**](UiKubernetesExplorerControllerApi.md#list_pods_by_labels_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/pods | listPodsByLabels
[**list_pvby_labels_using_get**](UiKubernetesExplorerControllerApi.md#list_pvby_labels_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/pv | listPVByLabels
[**list_pvcby_labels_using_get**](UiKubernetesExplorerControllerApi.md#list_pvcby_labels_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/pvc | listPVCByLabels
[**list_replicasets_by_labels_using_get**](UiKubernetesExplorerControllerApi.md#list_replicasets_by_labels_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/replicasets | listReplicasetsByLabels
[**list_secrets_by_labels_using_get**](UiKubernetesExplorerControllerApi.md#list_secrets_by_labels_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/secrets | listSecretsByLabels
[**list_services_by_labels_using_get**](UiKubernetesExplorerControllerApi.md#list_services_by_labels_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/services | listServicesByLabels
[**list_statefulsets_labels_by_labels_using_get**](UiKubernetesExplorerControllerApi.md#list_statefulsets_labels_by_labels_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/k8s-explorer/statefulsets | listStatefulsetsLabelsByLabels


# **container_logs_using_get**
> StreamingResponseBody container_logs_using_get(cluster_id, container_name, labels, pod_name, tail)

containerLogs

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
container_name = 'container_name_example' # str | containerName
labels = NULL # object | labels
pod_name = 'pod_name_example' # str | podName
tail = 56 # int | tail

try:
    # containerLogs
    api_response = api_instance.container_logs_using_get(cluster_id, container_name, labels, pod_name, tail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->container_logs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **container_name** | **str**| containerName | 
 **labels** | [**object**](.md)| labels | 
 **pod_name** | **str**| podName | 
 **tail** | **int**| tail | 

### Return type

[**StreamingResponseBody**](StreamingResponseBody.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ingress_rules_for_cluster_using_get**
> list[IngressRulesDTO] get_all_ingress_rules_for_cluster_using_get(cluster_id)

getAllIngressRulesForCluster

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getAllIngressRulesForCluster
    api_response = api_instance.get_all_ingress_rules_for_cluster_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->get_all_ingress_rules_for_cluster_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**list[IngressRulesDTO]**](IngressRulesDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_map_data_using_get**
> object get_config_map_data_using_get(cluster_id, config_map_name, labels)

getConfigMapData

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
config_map_name = 'config_map_name_example' # str | configMapName
labels = NULL # object | labels

try:
    # getConfigMapData
    api_response = api_instance.get_config_map_data_using_get(cluster_id, config_map_name, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->get_config_map_data_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **config_map_name** | **str**| configMapName | 
 **labels** | [**object**](.md)| labels | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manifest_using_get**
> str get_manifest_using_get(cluster_id, k8s_resource_name, k8s_resource_type, labels)

getManifest

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
k8s_resource_name = 'k8s_resource_name_example' # str | k8sResourceName
k8s_resource_type = 'k8s_resource_type_example' # str | k8sResourceType
labels = NULL # object | labels

try:
    # getManifest
    api_response = api_instance.get_manifest_using_get(cluster_id, k8s_resource_name, k8s_resource_type, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->get_manifest_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **k8s_resource_name** | **str**| k8sResourceName | 
 **k8s_resource_type** | **str**| k8sResourceType | 
 **labels** | [**object**](.md)| labels | 

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pods_for_deployment_using_get**
> list[str] get_pods_for_deployment_using_get(cluster_id, deployment_name, labels)

getPodsForDeployment

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
deployment_name = 'deployment_name_example' # str | deploymentName
labels = NULL # object | labels

try:
    # getPodsForDeployment
    api_response = api_instance.get_pods_for_deployment_using_get(cluster_id, deployment_name, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->get_pods_for_deployment_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **deployment_name** | **str**| deploymentName | 
 **labels** | [**object**](.md)| labels | 

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secrets_data_using_get**
> object get_secrets_data_using_get(cluster_id, labels, secret_name)

getSecretsData

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels
secret_name = 'secret_name_example' # str | secretName

try:
    # getSecretsData
    api_response = api_instance.get_secrets_data_using_get(cluster_id, labels, secret_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->get_secrets_data_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 
 **secret_name** | **str**| secretName | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_config_map_by_labels_using_get**
> list[ConfigMapDTO] list_config_map_by_labels_using_get(cluster_id, labels)

listConfigMapByLabels

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # listConfigMapByLabels
    api_response = api_instance.list_config_map_by_labels_using_get(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_config_map_by_labels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

[**list[ConfigMapDTO]**](ConfigMapDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_containers_in_pod_using_get**
> list[Container] list_containers_in_pod_using_get(cluster_id, labels, pod_name)

listContainersInPod

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels
pod_name = 'pod_name_example' # str | podName

try:
    # listContainersInPod
    api_response = api_instance.list_containers_in_pod_using_get(cluster_id, labels, pod_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_containers_in_pod_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 
 **pod_name** | **str**| podName | 

### Return type

[**list[Container]**](Container.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_containers_in_pod_v2_using_get**
> list[ContainerDTO] list_containers_in_pod_v2_using_get(cluster_id, labels, pod_name)

listContainersInPodV2

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels
pod_name = 'pod_name_example' # str | podName

try:
    # listContainersInPodV2
    api_response = api_instance.list_containers_in_pod_v2_using_get(cluster_id, labels, pod_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_containers_in_pod_v2_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 
 **pod_name** | **str**| podName | 

### Return type

[**list[ContainerDTO]**](ContainerDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cron_job_by_labels_using_get**
> list[CronJobDTO] list_cron_job_by_labels_using_get(cluster_id, labels)

listCronJobByLabels

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # listCronJobByLabels
    api_response = api_instance.list_cron_job_by_labels_using_get(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_cron_job_by_labels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

[**list[CronJobDTO]**](CronJobDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_daemon_sets_by_labels_using_get**
> list[DaemonSetDTO] list_daemon_sets_by_labels_using_get(cluster_id, labels)

listDaemonSetsByLabels

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # listDaemonSetsByLabels
    api_response = api_instance.list_daemon_sets_by_labels_using_get(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_daemon_sets_by_labels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

[**list[DaemonSetDTO]**](DaemonSetDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployments_by_labels_using_get**
> list[DeploymentDTO] list_deployments_by_labels_using_get(cluster_id, labels)

listDeploymentsByLabels

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # listDeploymentsByLabels
    api_response = api_instance.list_deployments_by_labels_using_get(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_deployments_by_labels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

[**list[DeploymentDTO]**](DeploymentDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_events_by_k8s_resource_using_get**
> list[EventDTO] list_events_by_k8s_resource_using_get(cluster_id, k8s_resource_name, k8s_resource_type, labels)

listEventsByK8sResource

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
k8s_resource_name = 'k8s_resource_name_example' # str | k8sResourceName
k8s_resource_type = 'k8s_resource_type_example' # str | k8sResourceType
labels = NULL # object | labels

try:
    # listEventsByK8sResource
    api_response = api_instance.list_events_by_k8s_resource_using_get(cluster_id, k8s_resource_name, k8s_resource_type, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_events_by_k8s_resource_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **k8s_resource_name** | **str**| k8sResourceName | 
 **k8s_resource_type** | **str**| k8sResourceType | 
 **labels** | [**object**](.md)| labels | 

### Return type

[**list[EventDTO]**](EventDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hpa_by_labels_using_get**
> list[HorizontalPodAutoscalerDTO] list_hpa_by_labels_using_get(cluster_id, labels)

listHpaByLabels

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # listHpaByLabels
    api_response = api_instance.list_hpa_by_labels_using_get(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_hpa_by_labels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

[**list[HorizontalPodAutoscalerDTO]**](HorizontalPodAutoscalerDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ingresses_by_labels_using_get**
> list[IngressDTO] list_ingresses_by_labels_using_get(cluster_id, labels)

listIngressesByLabels

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # listIngressesByLabels
    api_response = api_instance.list_ingresses_by_labels_using_get(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_ingresses_by_labels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

[**list[IngressDTO]**](IngressDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs_by_labels_using_get**
> list[JobDTO] list_jobs_by_labels_using_get(cluster_id, labels)

listJobsByLabels

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # listJobsByLabels
    api_response = api_instance.list_jobs_by_labels_using_get(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_jobs_by_labels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

[**list[JobDTO]**](JobDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pods_by_labels_using_get**
> list[PodDTO] list_pods_by_labels_using_get(cluster_id, labels)

listPodsByLabels

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # listPodsByLabels
    api_response = api_instance.list_pods_by_labels_using_get(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_pods_by_labels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

[**list[PodDTO]**](PodDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pvby_labels_using_get**
> list[PersistentVolumeDTO] list_pvby_labels_using_get(cluster_id, labels)

listPVByLabels

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # listPVByLabels
    api_response = api_instance.list_pvby_labels_using_get(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_pvby_labels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

[**list[PersistentVolumeDTO]**](PersistentVolumeDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pvcby_labels_using_get**
> list[PersistentVolumeClaimDTO] list_pvcby_labels_using_get(cluster_id, labels)

listPVCByLabels

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # listPVCByLabels
    api_response = api_instance.list_pvcby_labels_using_get(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_pvcby_labels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

[**list[PersistentVolumeClaimDTO]**](PersistentVolumeClaimDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replicasets_by_labels_using_get**
> list[ReplicasetDTO] list_replicasets_by_labels_using_get(cluster_id, labels)

listReplicasetsByLabels

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # listReplicasetsByLabels
    api_response = api_instance.list_replicasets_by_labels_using_get(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_replicasets_by_labels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

[**list[ReplicasetDTO]**](ReplicasetDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_secrets_by_labels_using_get**
> list[SecretDTO] list_secrets_by_labels_using_get(cluster_id, labels)

listSecretsByLabels

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # listSecretsByLabels
    api_response = api_instance.list_secrets_by_labels_using_get(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_secrets_by_labels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

[**list[SecretDTO]**](SecretDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_services_by_labels_using_get**
> list[ServiceDTO] list_services_by_labels_using_get(cluster_id, labels=labels)

listServicesByLabels

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels (optional)

try:
    # listServicesByLabels
    api_response = api_instance.list_services_by_labels_using_get(cluster_id, labels=labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_services_by_labels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | [optional] 

### Return type

[**list[ServiceDTO]**](ServiceDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_statefulsets_labels_by_labels_using_get**
> list[StatefulSetDTO] list_statefulsets_labels_by_labels_using_get(cluster_id, labels)

listStatefulsetsLabelsByLabels

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
api_instance = swagger_client.UiKubernetesExplorerControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
labels = NULL # object | labels

try:
    # listStatefulsetsLabelsByLabels
    api_response = api_instance.list_statefulsets_labels_by_labels_using_get(cluster_id, labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiKubernetesExplorerControllerApi->list_statefulsets_labels_by_labels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **labels** | [**object**](.md)| labels | 

### Return type

[**list[StatefulSetDTO]**](StatefulSetDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

