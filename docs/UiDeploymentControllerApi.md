# swagger_client.UiDeploymentControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_automation_suite_using_delete1**](UiDeploymentControllerApi.md#abort_automation_suite_using_delete1) | **DELETE** /cc-ui/v1/clusters/{clusterId}/deployments/qa/{executionId}/abortSuite | abortAutomationSuite
[**approve_release_using_post**](UiDeploymentControllerApi.md#approve_release_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/approveRelease | approveRelease
[**clean_s3_sources_using_delete**](UiDeploymentControllerApi.md#clean_s3_sources_using_delete) | **DELETE** /cc-ui/v1/clusters/{clusterId}/deployments/clean-s3-sources | cleanS3Sources
[**create_deployment_using_post**](UiDeploymentControllerApi.md#create_deployment_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/deployments | createDeployment
[**destroy_cluster_using_delete**](UiDeploymentControllerApi.md#destroy_cluster_using_delete) | **DELETE** /cc-ui/v1/clusters/{clusterId}/deployments/destroy | destroyCluster
[**download_terraform_export_using_get**](UiDeploymentControllerApi.md#download_terraform_export_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/download-terraform-export | downloadTerraformExport
[**get_cluster_state_using_get**](UiDeploymentControllerApi.md#get_cluster_state_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/state | getClusterState
[**get_deployment_logs_using_get**](UiDeploymentControllerApi.md#get_deployment_logs_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/logs | getDeploymentLogs
[**get_deployment_stats_using_get**](UiDeploymentControllerApi.md#get_deployment_stats_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/stats | getDeploymentStats
[**get_deployment_using_get**](UiDeploymentControllerApi.md#get_deployment_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId} | getDeployment
[**get_deployments_overview_using_get**](UiDeploymentControllerApi.md#get_deployments_overview_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/overview | getDeploymentsOverview
[**get_deployments_using_get1**](UiDeploymentControllerApi.md#get_deployments_using_get1) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments | getDeployments
[**get_latest_release_by_application_using_get**](UiDeploymentControllerApi.md#get_latest_release_by_application_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/latest-successful-release/{application} | getLatestReleaseByApplication
[**get_latest_release_using_get**](UiDeploymentControllerApi.md#get_latest_release_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/latest-successful-release | getLatestRelease
[**get_release_changes_using_get**](UiDeploymentControllerApi.md#get_release_changes_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/release-changes | getReleaseChanges
[**launch_cluster_using_put**](UiDeploymentControllerApi.md#launch_cluster_using_put) | **PUT** /cc-ui/v1/clusters/{clusterId}/deployments/launch | launchCluster
[**reject_release_using_post**](UiDeploymentControllerApi.md#reject_release_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/rejectRelease | rejectRelease
[**release_using_put**](UiDeploymentControllerApi.md#release_using_put) | **PUT** /cc-ui/v1/clusters/{clusterId}/deployments/release | release
[**release_v2_using_put**](UiDeploymentControllerApi.md#release_v2_using_put) | **PUT** /cc-ui/v1/clusters/{clusterId}/deployments/releaseV2/{releaseType} | releaseV2
[**run_hotfix_deployment_recipe_using_post**](UiDeploymentControllerApi.md#run_hotfix_deployment_recipe_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/deployments/recipes/deployment/hotfix | runHotfixDeploymentRecipe
[**search_deployments_using_get**](UiDeploymentControllerApi.md#search_deployments_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/search | searchDeployments
[**sign_off_deployment_using_put**](UiDeploymentControllerApi.md#sign_off_deployment_using_put) | **PUT** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/signoff | signOffDeployment
[**simulate_using_get**](UiDeploymentControllerApi.md#simulate_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/simulate | simulate
[**state_unlock_using_put**](UiDeploymentControllerApi.md#state_unlock_using_put) | **PUT** /cc-ui/v1/clusters/{clusterId}/deployments/unlock | stateUnlock
[**stream_deployment_logs_using_get**](UiDeploymentControllerApi.md#stream_deployment_logs_using_get) | **GET** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/logs/stream | streamDeploymentLogs
[**trigger_maintenance_release_using_post**](UiDeploymentControllerApi.md#trigger_maintenance_release_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/deployments/maintenance | triggerMaintenanceRelease
[**trigger_rollback_plan_release_using_post**](UiDeploymentControllerApi.md#trigger_rollback_plan_release_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/deployments/{deploymentId}/{resourceType}/{resourceName}/rollback-plan | triggerRollbackPlanRelease
[**trigger_terraform_export_using_post**](UiDeploymentControllerApi.md#trigger_terraform_export_using_post) | **POST** /cc-ui/v1/clusters/{clusterId}/deployments/terraform-export | triggerTerraformExport

# **abort_automation_suite_using_delete1**
> abort_automation_suite_using_delete1(cluster_id, execution_id)

abortAutomationSuite

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
execution_id = 'execution_id_example' # str | executionId

try:
    # abortAutomationSuite
    api_instance.abort_automation_suite_using_delete1(cluster_id, execution_id)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->abort_automation_suite_using_delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **execution_id** | **str**| executionId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_release_using_post**
> DeploymentLog approve_release_using_post(cluster_id, deployment_id)

approveRelease

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
deployment_id = 'deployment_id_example' # str | deploymentId

try:
    # approveRelease
    api_response = api_instance.approve_release_using_post(cluster_id, deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->approve_release_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **deployment_id** | **str**| deploymentId | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clean_s3_sources_using_delete**
> clean_s3_sources_using_delete(cluster_id)

cleanS3Sources

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # cleanS3Sources
    api_instance.clean_s3_sources_using_delete(cluster_id)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->clean_s3_sources_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_deployment_using_post**
> DeploymentLog create_deployment_using_post(body, cluster_id)

createDeployment

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeploymentRequest() # DeploymentRequest | deploymentRequest
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # createDeployment
    api_response = api_instance.create_deployment_using_post(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->create_deployment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeploymentRequest**](DeploymentRequest.md)| deploymentRequest | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_cluster_using_delete**
> DeploymentLog destroy_cluster_using_delete(cluster_id)

destroyCluster

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # destroyCluster
    api_response = api_instance.destroy_cluster_using_delete(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->destroy_cluster_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_terraform_export_using_get**
> download_terraform_export_using_get(cluster_id, deployment_id)

downloadTerraformExport

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
deployment_id = 'deployment_id_example' # str | deploymentId

try:
    # downloadTerraformExport
    api_instance.download_terraform_export_using_get(cluster_id, deployment_id)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->download_terraform_export_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **deployment_id** | **str**| deploymentId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_state_using_get**
> str get_cluster_state_using_get(cluster_id)

getClusterState

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getClusterState
    api_response = api_instance.get_cluster_state_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_cluster_state_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_logs_using_get**
> TokenPaginatedResponse get_deployment_logs_using_get(cluster_id, deployment_id, next_token=next_token)

getDeploymentLogs

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
deployment_id = 'deployment_id_example' # str | deploymentId
next_token = 'next_token_example' # str | nextToken (optional)

try:
    # getDeploymentLogs
    api_response = api_instance.get_deployment_logs_using_get(cluster_id, deployment_id, next_token=next_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_deployment_logs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **deployment_id** | **str**| deploymentId | 
 **next_token** | **str**| nextToken | [optional] 

### Return type

[**TokenPaginatedResponse**](TokenPaginatedResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_stats_using_get**
> DeploymentStatsDto get_deployment_stats_using_get(cluster_id, days=days)

getDeploymentStats

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
days = 30 # int | days (optional) (default to 30)

try:
    # getDeploymentStats
    api_response = api_instance.get_deployment_stats_using_get(cluster_id, days=days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_deployment_stats_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **days** | **int**| days | [optional] [default to 30]

### Return type

[**DeploymentStatsDto**](DeploymentStatsDto.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_using_get**
> DeploymentLog get_deployment_using_get(cluster_id, deployment_id)

getDeployment

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
deployment_id = 'deployment_id_example' # str | deploymentId

try:
    # getDeployment
    api_response = api_instance.get_deployment_using_get(cluster_id, deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_deployment_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **deployment_id** | **str**| deploymentId | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments_overview_using_get**
> DeploymentOverview get_deployments_overview_using_get(cluster_id)

getDeploymentsOverview

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getDeploymentsOverview
    api_response = api_instance.get_deployments_overview_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_deployments_overview_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**DeploymentOverview**](DeploymentOverview.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments_using_get1**
> ListDeploymentsWrapper get_deployments_using_get1(cluster_id)

getDeployments

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getDeployments
    api_response = api_instance.get_deployments_using_get1(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_deployments_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**ListDeploymentsWrapper**](ListDeploymentsWrapper.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_release_by_application_using_get**
> DeploymentLog get_latest_release_by_application_using_get(application, cluster_id)

getLatestReleaseByApplication

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
application = 'application_example' # str | application
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getLatestReleaseByApplication
    api_response = api_instance.get_latest_release_by_application_using_get(application, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_latest_release_by_application_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| application | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_release_using_get**
> DeploymentLog get_latest_release_using_get(cluster_id)

getLatestRelease

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getLatestRelease
    api_response = api_instance.get_latest_release_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_latest_release_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_changes_using_get**
> ReleaseChanges get_release_changes_using_get(cluster_id, deployment_id)

getReleaseChanges

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
deployment_id = 'deployment_id_example' # str | deploymentId

try:
    # getReleaseChanges
    api_response = api_instance.get_release_changes_using_get(cluster_id, deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->get_release_changes_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **deployment_id** | **str**| deploymentId | 

### Return type

[**ReleaseChanges**](ReleaseChanges.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_cluster_using_put**
> DeploymentLog launch_cluster_using_put(cluster_id)

launchCluster

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # launchCluster
    api_response = api_instance.launch_cluster_using_put(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->launch_cluster_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_release_using_post**
> DeploymentLog reject_release_using_post(cluster_id, deployment_id)

rejectRelease

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
deployment_id = 'deployment_id_example' # str | deploymentId

try:
    # rejectRelease
    api_response = api_instance.reject_release_using_post(cluster_id, deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->reject_release_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **deployment_id** | **str**| deploymentId | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_using_put**
> DeploymentLog release_using_put(cluster_id, allow_destroy=allow_destroy, can_queue=can_queue, comment=comment, force_release=force_release, with_refresh=with_refresh)

release

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
allow_destroy = false # bool | allowDestroy (optional) (default to false)
can_queue = false # bool | canQueue (optional) (default to false)
comment = 'comment_example' # str | comment (optional)
force_release = false # bool | forceRelease (optional) (default to false)
with_refresh = true # bool | withRefresh (optional) (default to true)

try:
    # release
    api_response = api_instance.release_using_put(cluster_id, allow_destroy=allow_destroy, can_queue=can_queue, comment=comment, force_release=force_release, with_refresh=with_refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->release_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **allow_destroy** | **bool**| allowDestroy | [optional] [default to false]
 **can_queue** | **bool**| canQueue | [optional] [default to false]
 **comment** | **str**| comment | [optional] 
 **force_release** | **bool**| forceRelease | [optional] [default to false]
 **with_refresh** | **bool**| withRefresh | [optional] [default to true]

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_v2_using_put**
> DeploymentLog release_v2_using_put(cluster_id, release_type, allow_destroy=allow_destroy, can_queue=can_queue, comment=comment, force_release=force_release, with_refresh=with_refresh)

releaseV2

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
release_type = 'release_type_example' # str | releaseType
allow_destroy = false # bool | allowDestroy (optional) (default to false)
can_queue = false # bool | canQueue (optional) (default to false)
comment = 'comment_example' # str | comment (optional)
force_release = false # bool | forceRelease (optional) (default to false)
with_refresh = true # bool | withRefresh (optional) (default to true)

try:
    # releaseV2
    api_response = api_instance.release_v2_using_put(cluster_id, release_type, allow_destroy=allow_destroy, can_queue=can_queue, comment=comment, force_release=force_release, with_refresh=with_refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->release_v2_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **release_type** | **str**| releaseType | 
 **allow_destroy** | **bool**| allowDestroy | [optional] [default to false]
 **can_queue** | **bool**| canQueue | [optional] [default to false]
 **comment** | **str**| comment | [optional] 
 **force_release** | **bool**| forceRelease | [optional] [default to false]
 **with_refresh** | **bool**| withRefresh | [optional] [default to true]

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_hotfix_deployment_recipe_using_post**
> DeploymentLog run_hotfix_deployment_recipe_using_post(body, cluster_id, allow_destroy=allow_destroy, can_queue=can_queue, comment=comment, force_release=force_release, is_plan=is_plan, with_refresh=with_refresh)

runHotfixDeploymentRecipe

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.HotfixDeploymentRecipe() # HotfixDeploymentRecipe | deploymentRecipe
cluster_id = 'cluster_id_example' # str | clusterId
allow_destroy = false # bool | allowDestroy (optional) (default to false)
can_queue = false # bool | canQueue (optional) (default to false)
comment = 'comment_example' # str | comment (optional)
force_release = false # bool | forceRelease (optional) (default to false)
is_plan = false # bool | isPlan (optional) (default to false)
with_refresh = false # bool | withRefresh (optional) (default to false)

try:
    # runHotfixDeploymentRecipe
    api_response = api_instance.run_hotfix_deployment_recipe_using_post(body, cluster_id, allow_destroy=allow_destroy, can_queue=can_queue, comment=comment, force_release=force_release, is_plan=is_plan, with_refresh=with_refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->run_hotfix_deployment_recipe_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HotfixDeploymentRecipe**](HotfixDeploymentRecipe.md)| deploymentRecipe | 
 **cluster_id** | **str**| clusterId | 
 **allow_destroy** | **bool**| allowDestroy | [optional] [default to false]
 **can_queue** | **bool**| canQueue | [optional] [default to false]
 **comment** | **str**| comment | [optional] 
 **force_release** | **bool**| forceRelease | [optional] [default to false]
 **is_plan** | **bool**| isPlan | [optional] [default to false]
 **with_refresh** | **bool**| withRefresh | [optional] [default to false]

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_deployments_using_get**
> PageDeploymentLog search_deployments_using_get(cluster_id, end=end, exclude_status=exclude_status, page_number=page_number, page_size=page_size, release_type=release_type, signed_off=signed_off, start=start, status=status, tf_version=tf_version, triggered_by=triggered_by)

searchDeployments

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
end = '2013-10-20T19:20:30+01:00' # datetime | end (optional)
exclude_status = ['exclude_status_example'] # list[str] | excludeStatus (optional)
page_number = 0 # int | pageNumber (optional) (default to 0)
page_size = 50 # int | pageSize (optional) (default to 50)
release_type = 'release_type_example' # str | releaseType (optional)
signed_off = true # bool | signedOff (optional)
start = '2013-10-20T19:20:30+01:00' # datetime | start (optional)
status = 'status_example' # str | status (optional)
tf_version = 'tf_version_example' # str | tfVersion (optional)
triggered_by = 'triggered_by_example' # str | triggeredBy (optional)

try:
    # searchDeployments
    api_response = api_instance.search_deployments_using_get(cluster_id, end=end, exclude_status=exclude_status, page_number=page_number, page_size=page_size, release_type=release_type, signed_off=signed_off, start=start, status=status, tf_version=tf_version, triggered_by=triggered_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->search_deployments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **end** | **datetime**| end | [optional] 
 **exclude_status** | [**list[str]**](str.md)| excludeStatus | [optional] 
 **page_number** | **int**| pageNumber | [optional] [default to 0]
 **page_size** | **int**| pageSize | [optional] [default to 50]
 **release_type** | **str**| releaseType | [optional] 
 **signed_off** | **bool**| signedOff | [optional] 
 **start** | **datetime**| start | [optional] 
 **status** | **str**| status | [optional] 
 **tf_version** | **str**| tfVersion | [optional] 
 **triggered_by** | **str**| triggeredBy | [optional] 

### Return type

[**PageDeploymentLog**](PageDeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_off_deployment_using_put**
> DeploymentLog sign_off_deployment_using_put(cluster_id, deployment_id)

signOffDeployment

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
deployment_id = 'deployment_id_example' # str | deploymentId

try:
    # signOffDeployment
    api_response = api_instance.sign_off_deployment_using_put(cluster_id, deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->sign_off_deployment_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **deployment_id** | **str**| deploymentId | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simulate_using_get**
> list[ChangeRepresentation] simulate_using_get(cluster_id)

simulate

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # simulate
    api_response = api_instance.simulate_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->simulate_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**list[ChangeRepresentation]**](ChangeRepresentation.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_unlock_using_put**
> DeploymentLog state_unlock_using_put(cluster_id, lock_id)

stateUnlock

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
lock_id = 'lock_id_example' # str | lockId

try:
    # stateUnlock
    api_response = api_instance.state_unlock_using_put(cluster_id, lock_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->state_unlock_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **lock_id** | **str**| lockId | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_deployment_logs_using_get**
> StreamingResponseBody stream_deployment_logs_using_get(cluster_id, deployment_id)

streamDeploymentLogs

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
deployment_id = 'deployment_id_example' # str | deploymentId

try:
    # streamDeploymentLogs
    api_response = api_instance.stream_deployment_logs_using_get(cluster_id, deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->stream_deployment_logs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **deployment_id** | **str**| deploymentId | 

### Return type

[**StreamingResponseBody**](StreamingResponseBody.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_maintenance_release_using_post**
> DeploymentLog trigger_maintenance_release_using_post(cluster_id)

triggerMaintenanceRelease

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # triggerMaintenanceRelease
    api_response = api_instance.trigger_maintenance_release_using_post(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->trigger_maintenance_release_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_rollback_plan_release_using_post**
> DeploymentLog trigger_rollback_plan_release_using_post(cluster_id, deployment_id, resource_name, resource_type)

triggerRollbackPlanRelease

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
deployment_id = 'deployment_id_example' # str | deploymentId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # triggerRollbackPlanRelease
    api_response = api_instance.trigger_rollback_plan_release_using_post(cluster_id, deployment_id, resource_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->trigger_rollback_plan_release_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **deployment_id** | **str**| deploymentId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_terraform_export_using_post**
> DeploymentLog trigger_terraform_export_using_post(cluster_id)

triggerTerraformExport

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
api_instance = swagger_client.UiDeploymentControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # triggerTerraformExport
    api_response = api_instance.trigger_terraform_export_using_post(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDeploymentControllerApi->trigger_terraform_export_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**DeploymentLog**](DeploymentLog.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

