# swagger_client.ApplicationControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_using_post**](ApplicationControllerApi.md#build_using_post) | **POST** /api/{applicationFamily}/applications/{applicationId}/builds | build
[**change_password_using_put**](ApplicationControllerApi.md#change_password_using_put) | **PUT** /api/users/{userId}/changePassword | changePassword
[**create_app_secret_request_using_post**](ApplicationControllerApi.md#create_app_secret_request_using_post) | **POST** /api/{applicationFamily}/applications/{applicationId}/secretRequests | createAppSecretRequest
[**create_application_using_post**](ApplicationControllerApi.md#create_application_using_post) | **POST** /api/{applicationFamily}/applications | createApplication
[**create_ecr_registry_using_post**](ApplicationControllerApi.md#create_ecr_registry_using_post) | **POST** /api/ecrRegistry | createECRRegistry
[**create_generic_action_using_post**](ApplicationControllerApi.md#create_generic_action_using_post) | **POST** /api/buildType/{buildType}/actions | createGenericAction
[**create_user_cc_using_post**](ApplicationControllerApi.md#create_user_cc_using_post) | **POST** /api/cc-users | createUserCC
[**create_user_using_post**](ApplicationControllerApi.md#create_user_using_post) | **POST** /api/users | createUser
[**delete_application_secret_using_delete**](ApplicationControllerApi.md#delete_application_secret_using_delete) | **DELETE** /api/{applicationFamily}/{environment}/applications/{applicationId}/secrets/{secretName} | deleteApplicationSecret
[**delete_application_using_delete**](ApplicationControllerApi.md#delete_application_using_delete) | **DELETE** /api/{applicationFamily}/applications/{applicationId} | deleteApplication
[**deploy_using_post**](ApplicationControllerApi.md#deploy_using_post) | **POST** /api/{applicationFamily}/{environment}/applications/{applicationId}/deployments | deploy
[**disable_alerting_using_delete**](ApplicationControllerApi.md#disable_alerting_using_delete) | **DELETE** /api/{applicationFamily}/{environment}/applications/{applicationId}/alerting | disableAlerting
[**disable_monitoring_using_delete**](ApplicationControllerApi.md#disable_monitoring_using_delete) | **DELETE** /api/{applicationFamily}/{environment}/applications/{applicationId}/monitoring | disableMonitoring
[**download_dump_file_using_get**](ApplicationControllerApi.md#download_dump_file_using_get) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/dumps/download | downloadDumpFile
[**download_test_report_using_get**](ApplicationControllerApi.md#download_test_report_using_get) | **GET** /api/{applicationFamily}/applications/{applicationId}/builds/{buildId}/downloadArtifacts | downloadTestReport
[**enable_alerting_using_post**](ApplicationControllerApi.md#enable_alerting_using_post) | **POST** /api/{applicationFamily}/{environment}/applications/{applicationId}/alerting | enableAlerting
[**enable_monitoring_using_post**](ApplicationControllerApi.md#enable_monitoring_using_post) | **POST** /api/{applicationFamily}/{environment}/applications/{applicationId}/monitoring | enableMonitoring
[**execute_action_on_pod_using_post**](ApplicationControllerApi.md#execute_action_on_pod_using_post) | **POST** /api/{applicationFamily}/{environment}/applications/{applicationId}/pods/{podName}/actions/executeAction | executeActionOnPod
[**get_actions_for_pod_using_get**](ApplicationControllerApi.md#get_actions_for_pod_using_get) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/pods/{podName}/actions | getActionsForPod
[**get_alerting_details_using_get**](ApplicationControllerApi.md#get_alerting_details_using_get) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/alerting | getAlertingDetails
[**get_all_application_metrics_using_get**](ApplicationControllerApi.md#get_all_application_metrics_using_get) | **GET** /api/{applicationFamily}/appmetrics | getAllApplicationMetrics
[**get_all_registries_using_get**](ApplicationControllerApi.md#get_all_registries_using_get) | **GET** /api/getRegistries | getAllRegistries
[**get_application_branches_using_get**](ApplicationControllerApi.md#get_application_branches_using_get) | **GET** /api/{applicationFamily}/applications/{applicationId}/branches | getApplicationBranches
[**get_application_families_using_get**](ApplicationControllerApi.md#get_application_families_using_get) | **GET** /api/applicationFamilies | getApplicationFamilies
[**get_application_metric_summary_using_get**](ApplicationControllerApi.md#get_application_metric_summary_using_get) | **GET** /api/{applicationFamily}/applications/{applicationId}/metrics | getApplicationMetricSummary
[**get_application_pod_details_using_get**](ApplicationControllerApi.md#get_application_pod_details_using_get) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/podDetails | getApplicationPodDetails
[**get_application_secret_requests_using_get**](ApplicationControllerApi.md#get_application_secret_requests_using_get) | **GET** /api/{applicationFamily}/applications/{applicationId}/secretRequests | getApplicationSecretRequests
[**get_application_secrets_using_get**](ApplicationControllerApi.md#get_application_secrets_using_get) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/secretRequests | getApplicationSecrets
[**get_application_tags_using_get**](ApplicationControllerApi.md#get_application_tags_using_get) | **GET** /api/{applicationFamily}/applications/{applicationId}/tags | getApplicationTags
[**get_application_types_using_get**](ApplicationControllerApi.md#get_application_types_using_get) | **GET** /api/applicationTypes | getApplicationTypes
[**get_application_using_get**](ApplicationControllerApi.md#get_application_using_get) | **GET** /api/{applicationFamily}/applications/{applicationId} | getApplication
[**get_applications_using_get**](ApplicationControllerApi.md#get_applications_using_get) | **GET** /api/{applicationFamily}/applications | getApplications
[**get_build_logs_using_get**](ApplicationControllerApi.md#get_build_logs_using_get) | **GET** /api/{applicationFamily}/applications/{applicationId}/builds/{buildId}/logs | getBuildLogs
[**get_build_using_get**](ApplicationControllerApi.md#get_build_using_get) | **GET** /api/{applicationFamily}/applications/{applicationId}/builds/{buildId} | getBuild
[**get_builds_using_get**](ApplicationControllerApi.md#get_builds_using_get) | **GET** /api/{applicationFamily}/applications/{applicationId}/builds | getBuilds
[**get_cc_environment_meta_data_using_get**](ApplicationControllerApi.md#get_cc_environment_meta_data_using_get) | **GET** /api/cc/{applicationFamily}/environmentMetaData | getCCEnvironmentMetaData
[**get_current_deployment_using_get**](ApplicationControllerApi.md#get_current_deployment_using_get) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/deployment/current | getCurrentDeployment
[**get_deployment_status_using_get**](ApplicationControllerApi.md#get_deployment_status_using_get) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/deploymentStatus | getDeploymentStatus
[**get_dump_file_list_using_get**](ApplicationControllerApi.md#get_dump_file_list_using_get) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/dumps | getDumpFileList
[**get_ecr_token_using_get**](ApplicationControllerApi.md#get_ecr_token_using_get) | **GET** /api/getEcrLoginToken | getEcrToken
[**get_environment_meta_data_using_get**](ApplicationControllerApi.md#get_environment_meta_data_using_get) | **GET** /api/{applicationFamily}/environmentMetaData | getEnvironmentMetaData
[**get_environment_using_get**](ApplicationControllerApi.md#get_environment_using_get) | **GET** /api/{applicationFamily}/environments/{id} | getEnvironment
[**get_environments_using_get**](ApplicationControllerApi.md#get_environments_using_get) | **GET** /api/{applicationFamily}/environments | getEnvironments
[**get_executed_actions_for_application_using_get**](ApplicationControllerApi.md#get_executed_actions_for_application_using_get) | **GET** /api/{applicationFamily}/applications/{applicationId}/executedActions | getExecutedActionsForApplication
[**get_images_using_get**](ApplicationControllerApi.md#get_images_using_get) | **GET** /api/{applicationFamily}/applications/{applicationId}/images | getImages
[**get_monitoring_details_using_get**](ApplicationControllerApi.md#get_monitoring_details_using_get) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/monitoring | getMonitoringDetails
[**get_test_build_details_using_get**](ApplicationControllerApi.md#get_test_build_details_using_get) | **GET** /api/{applicationFamily}/applications/{applicationId}/builds/{buildId}/testDetails | getTestBuildDetails
[**get_users_using_get**](ApplicationControllerApi.md#get_users_using_get) | **GET** /api/users | getUsers
[**global_stats_using_get**](ApplicationControllerApi.md#global_stats_using_get) | **GET** /api/stats | globalStats
[**halt_application_using_post**](ApplicationControllerApi.md#halt_application_using_post) | **POST** /api/{applicationFamily}/{environment}/applications/{applicationId}/halt | haltApplication
[**login_using_delete**](ApplicationControllerApi.md#login_using_delete) | **DELETE** /api/login | login
[**login_using_get**](ApplicationControllerApi.md#login_using_get) | **GET** /api/login | login
[**login_using_head**](ApplicationControllerApi.md#login_using_head) | **HEAD** /api/login | login
[**login_using_options**](ApplicationControllerApi.md#login_using_options) | **OPTIONS** /api/login | login
[**login_using_patch**](ApplicationControllerApi.md#login_using_patch) | **PATCH** /api/login | login
[**login_using_post**](ApplicationControllerApi.md#login_using_post) | **POST** /api/login | login
[**login_using_put**](ApplicationControllerApi.md#login_using_put) | **PUT** /api/login | login
[**me_using_get**](ApplicationControllerApi.md#me_using_get) | **GET** /api/me | me
[**process_webhook_pr_bitbucket_using_post**](ApplicationControllerApi.md#process_webhook_pr_bitbucket_using_post) | **POST** /api/{applicationFamily}/applications/{applicationId}/webhooks/pr/bitbucket | processWebhookPRBitbucket
[**process_webhook_pr_github_using_post**](ApplicationControllerApi.md#process_webhook_pr_github_using_post) | **POST** /api/{applicationFamily}/applications/{applicationId}/webhooks/pr/github | processWebhookPRGithub
[**redeploy_using_post**](ApplicationControllerApi.md#redeploy_using_post) | **POST** /api/{applicationFamily}/{environment}/redeployment | redeploy
[**refresh_build_details_using_put**](ApplicationControllerApi.md#refresh_build_details_using_put) | **PUT** /api/codebuild/builds/{codeBuildId}/refresh | refreshBuildDetails
[**resume_application_using_post**](ApplicationControllerApi.md#resume_application_using_post) | **POST** /api/{applicationFamily}/{environment}/applications/{applicationId}/resume | resumeApplication
[**update_application_secrets_using_put**](ApplicationControllerApi.md#update_application_secrets_using_put) | **PUT** /api/{applicationFamily}/{environment}/applications/{applicationId}/secrets | updateApplicationSecrets
[**update_application_using_put**](ApplicationControllerApi.md#update_application_using_put) | **PUT** /api/{applicationFamily}/applications | updateApplication
[**update_build_using_put**](ApplicationControllerApi.md#update_build_using_put) | **PUT** /api/{applicationFamily}/applications/{applicationId}/builds/{buildId} | updateBuild
[**update_user_using_put**](ApplicationControllerApi.md#update_user_using_put) | **PUT** /api/users/{userId} | updateUser
[**upsert_application_family_metadata_using_post**](ApplicationControllerApi.md#upsert_application_family_metadata_using_post) | **POST** /api/applicationFamilies/{applicationFamily}/metadata | upsertApplicationFamilyMetadata
[**upsert_environment_using_post**](ApplicationControllerApi.md#upsert_environment_using_post) | **POST** /api/{applicationFamily}/environments | upsertEnvironment


# **build_using_post**
> Build build_using_post(application_family, application_id, build)

build

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
build = swagger_client.Build() # Build | build

try:
    # build
    api_response = api_instance.build_using_post(application_family, application_id, build)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->build_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **build** | [**Build**](Build.md)| build | 

### Return type

[**Build**](Build.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password_using_put**
> User change_password_using_put(pwd_change, user_id)

changePassword

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
pwd_change = swagger_client.PasswordChange() # PasswordChange | pwdChange
user_id = 'user_id_example' # str | userId

try:
    # changePassword
    api_response = api_instance.change_password_using_put(pwd_change, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->change_password_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pwd_change** | [**PasswordChange**](PasswordChange.md)| pwdChange | 
 **user_id** | **str**| userId | 

### Return type

[**User**](User.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_secret_request_using_post**
> list[ApplicationSecretRequest] create_app_secret_request_using_post(application_family, application_id, application_secret_requests)

createAppSecretRequest

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
application_secret_requests = [swagger_client.ApplicationSecretRequest()] # list[ApplicationSecretRequest] | applicationSecretRequests

try:
    # createAppSecretRequest
    api_response = api_instance.create_app_secret_request_using_post(application_family, application_id, application_secret_requests)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->create_app_secret_request_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **application_secret_requests** | [**list[ApplicationSecretRequest]**](ApplicationSecretRequest.md)| applicationSecretRequests | 

### Return type

[**list[ApplicationSecretRequest]**](ApplicationSecretRequest.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application_using_post**
> Application create_application_using_post(application, application_family)

createApplication

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application = swagger_client.Application() # Application | application
application_family = 'application_family_example' # str | applicationFamily

try:
    # createApplication
    api_response = api_instance.create_application_using_post(application, application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->create_application_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | [**Application**](Application.md)| application | 
 **application_family** | **str**| applicationFamily | 

### Return type

[**Application**](Application.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ecr_registry_using_post**
> ECRRegistry create_ecr_registry_using_post(ecr_registry)

createECRRegistry

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
ecr_registry = swagger_client.ECRRegistry() # ECRRegistry | ecrRegistry

try:
    # createECRRegistry
    api_response = api_instance.create_ecr_registry_using_post(ecr_registry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->create_ecr_registry_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ecr_registry** | [**ECRRegistry**](ECRRegistry.md)| ecrRegistry | 

### Return type

[**ECRRegistry**](ECRRegistry.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_generic_action_using_post**
> ApplicationAction create_generic_action_using_post(application_action, build_type)

createGenericAction

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_action = swagger_client.ApplicationAction() # ApplicationAction | applicationAction
build_type = 'build_type_example' # str | buildType

try:
    # createGenericAction
    api_response = api_instance.create_generic_action_using_post(application_action, build_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->create_generic_action_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_action** | [**ApplicationAction**](ApplicationAction.md)| applicationAction | 
 **build_type** | **str**| buildType | 

### Return type

[**ApplicationAction**](ApplicationAction.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_cc_using_post**
> User create_user_cc_using_post(user)

createUserCC

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
user = swagger_client.User() # User | user

try:
    # createUserCC
    api_response = api_instance.create_user_cc_using_post(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->create_user_cc_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| user | 

### Return type

[**User**](User.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_using_post**
> User create_user_using_post(user)

createUser

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
user = swagger_client.User() # User | user

try:
    # createUser
    api_response = api_instance.create_user_using_post(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->create_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| user | 

### Return type

[**User**](User.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_secret_using_delete**
> bool delete_application_secret_using_delete(application_family, application_id, environment, secret_name)

deleteApplicationSecret

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment
secret_name = 'secret_name_example' # str | secretName

try:
    # deleteApplicationSecret
    api_response = api_instance.delete_application_secret_using_delete(application_family, application_id, environment, secret_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->delete_application_secret_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 
 **secret_name** | **str**| secretName | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_using_delete**
> bool delete_application_using_delete(application_family, application_id)

deleteApplication

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId

try:
    # deleteApplication
    api_response = api_instance.delete_application_using_delete(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->delete_application_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_using_post**
> Deployment deploy_using_post(application_family, application_id, deployment, environment)

deploy

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
deployment = swagger_client.Deployment() # Deployment | deployment
environment = 'environment_example' # str | environment

try:
    # deploy
    api_response = api_instance.deploy_using_post(application_family, application_id, deployment, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->deploy_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **deployment** | [**Deployment**](Deployment.md)| deployment | 
 **environment** | **str**| environment | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_alerting_using_delete**
> bool disable_alerting_using_delete(application_family, application_id, environment)

disableAlerting

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment

try:
    # disableAlerting
    api_response = api_instance.disable_alerting_using_delete(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->disable_alerting_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_monitoring_using_delete**
> bool disable_monitoring_using_delete(application_family, application_id, environment)

disableMonitoring

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment

try:
    # disableMonitoring
    api_response = api_instance.disable_monitoring_using_delete(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->disable_monitoring_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_dump_file_using_get**
> InputStreamResource download_dump_file_using_get(application_family, application_id, environment, path)

downloadDumpFile

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment
path = 'path_example' # str | path

try:
    # downloadDumpFile
    api_response = api_instance.download_dump_file_using_get(application_family, application_id, environment, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->download_dump_file_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 
 **path** | **str**| path | 

### Return type

[**InputStreamResource**](InputStreamResource.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_test_report_using_get**
> InputStreamResource download_test_report_using_get(application_family, application_id, build_id)

downloadTestReport

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
build_id = 'build_id_example' # str | buildId

try:
    # downloadTestReport
    api_response = api_instance.download_test_report_using_get(application_family, application_id, build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->download_test_report_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **build_id** | **str**| buildId | 

### Return type

[**InputStreamResource**](InputStreamResource.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_alerting_using_post**
> bool enable_alerting_using_post(application_family, application_id, environment)

enableAlerting

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment

try:
    # enableAlerting
    api_response = api_instance.enable_alerting_using_post(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->enable_alerting_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_monitoring_using_post**
> bool enable_monitoring_using_post(application_family, application_id, environment)

enableMonitoring

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment

try:
    # enableMonitoring
    api_response = api_instance.enable_monitoring_using_post(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->enable_monitoring_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_action_on_pod_using_post**
> ActionExecution execute_action_on_pod_using_post(application_action, application_family, application_id, environment, pod_name)

executeActionOnPod

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_action = swagger_client.ApplicationAction() # ApplicationAction | applicationAction
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment
pod_name = 'pod_name_example' # str | podName

try:
    # executeActionOnPod
    api_response = api_instance.execute_action_on_pod_using_post(application_action, application_family, application_id, environment, pod_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->execute_action_on_pod_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_action** | [**ApplicationAction**](ApplicationAction.md)| applicationAction | 
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 
 **pod_name** | **str**| podName | 

### Return type

[**ActionExecution**](ActionExecution.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_for_pod_using_get**
> list[ApplicationAction] get_actions_for_pod_using_get(application_family, application_id, environment, pod_name)

getActionsForPod

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment
pod_name = 'pod_name_example' # str | podName

try:
    # getActionsForPod
    api_response = api_instance.get_actions_for_pod_using_get(application_family, application_id, environment, pod_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_actions_for_pod_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 
 **pod_name** | **str**| podName | 

### Return type

[**list[ApplicationAction]**](ApplicationAction.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerting_details_using_get**
> Alerting get_alerting_details_using_get(application_family, application_id, environment)

getAlertingDetails

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment

try:
    # getAlertingDetails
    api_response = api_instance.get_alerting_details_using_get(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_alerting_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 

### Return type

[**Alerting**](Alerting.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_application_metrics_using_get**
> list[ApplicationMetricsWrapper] get_all_application_metrics_using_get(application_family)

getAllApplicationMetrics

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily

try:
    # getAllApplicationMetrics
    api_response = api_instance.get_all_application_metrics_using_get(application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_all_application_metrics_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 

### Return type

[**list[ApplicationMetricsWrapper]**](ApplicationMetricsWrapper.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_registries_using_get**
> list[Registry] get_all_registries_using_get()

getAllRegistries

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllRegistries
    api_response = api_instance.get_all_registries_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_all_registries_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Registry]**](Registry.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_branches_using_get**
> list[str] get_application_branches_using_get(application_family, application_id)

getApplicationBranches

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId

try:
    # getApplicationBranches
    api_response = api_instance.get_application_branches_using_get(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_branches_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_families_using_get**
> list[str] get_application_families_using_get()

getApplicationFamilies

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    # getApplicationFamilies
    api_response = api_instance.get_application_families_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_families_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_metric_summary_using_get**
> dict(str, ApplicationMetrics) get_application_metric_summary_using_get(application_family, application_id)

getApplicationMetricSummary

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId

try:
    # getApplicationMetricSummary
    api_response = api_instance.get_application_metric_summary_using_get(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_metric_summary_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 

### Return type

[**dict(str, ApplicationMetrics)**](ApplicationMetrics.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_pod_details_using_get**
> list[ApplicationPodDetails] get_application_pod_details_using_get(application_family, application_id, environment)

getApplicationPodDetails

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment

try:
    # getApplicationPodDetails
    api_response = api_instance.get_application_pod_details_using_get(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_pod_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 

### Return type

[**list[ApplicationPodDetails]**](ApplicationPodDetails.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_secret_requests_using_get**
> list[ApplicationSecretRequest] get_application_secret_requests_using_get(application_family, application_id)

getApplicationSecretRequests

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId

try:
    # getApplicationSecretRequests
    api_response = api_instance.get_application_secret_requests_using_get(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_secret_requests_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 

### Return type

[**list[ApplicationSecretRequest]**](ApplicationSecretRequest.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_secrets_using_get**
> list[ApplicationSecret] get_application_secrets_using_get(application_family, application_id, environment)

getApplicationSecrets

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment

try:
    # getApplicationSecrets
    api_response = api_instance.get_application_secrets_using_get(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_secrets_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 

### Return type

[**list[ApplicationSecret]**](ApplicationSecret.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_tags_using_get**
> list[str] get_application_tags_using_get(application_family, application_id)

getApplicationTags

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId

try:
    # getApplicationTags
    api_response = api_instance.get_application_tags_using_get(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_tags_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_types_using_get**
> list[str] get_application_types_using_get()

getApplicationTypes

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    # getApplicationTypes
    api_response = api_instance.get_application_types_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_types_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_using_get**
> Application get_application_using_get(application_family, application_id)

getApplication

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId

try:
    # getApplication
    api_response = api_instance.get_application_using_get(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 

### Return type

[**Application**](Application.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications_using_get**
> list[Application] get_applications_using_get(application_family)

getApplications

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily

try:
    # getApplications
    api_response = api_instance.get_applications_using_get(application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_applications_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 

### Return type

[**list[Application]**](Application.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_logs_using_get**
> TokenPaginatedResponseLogEvent get_build_logs_using_get(application_family, application_id, build_id, next_token=next_token)

getBuildLogs

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
build_id = 'build_id_example' # str | buildId
next_token = 'next_token_example' # str | nextToken (optional)

try:
    # getBuildLogs
    api_response = api_instance.get_build_logs_using_get(application_family, application_id, build_id, next_token=next_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_build_logs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **build_id** | **str**| buildId | 
 **next_token** | **str**| nextToken | [optional] 

### Return type

[**TokenPaginatedResponseLogEvent**](TokenPaginatedResponseLogEvent.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_using_get**
> Build get_build_using_get(application_family, application_id, build_id)

getBuild

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
build_id = 'build_id_example' # str | buildId

try:
    # getBuild
    api_response = api_instance.get_build_using_get(application_family, application_id, build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_build_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **build_id** | **str**| buildId | 

### Return type

[**Build**](Build.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_builds_using_get**
> list[Build] get_builds_using_get(application_family, application_id)

getBuilds

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId

try:
    # getBuilds
    api_response = api_instance.get_builds_using_get(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_builds_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 

### Return type

[**list[Build]**](Build.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cc_environment_meta_data_using_get**
> list[EnvironmentMetaData] get_cc_environment_meta_data_using_get(application_family)

getCCEnvironmentMetaData

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily

try:
    # getCCEnvironmentMetaData
    api_response = api_instance.get_cc_environment_meta_data_using_get(application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_cc_environment_meta_data_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 

### Return type

[**list[EnvironmentMetaData]**](EnvironmentMetaData.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_deployment_using_get**
> Deployment get_current_deployment_using_get(application_family, application_id, environment)

getCurrentDeployment

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment

try:
    # getCurrentDeployment
    api_response = api_instance.get_current_deployment_using_get(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_current_deployment_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_status_using_get**
> DeploymentStatusDetails get_deployment_status_using_get(application_family, application_id, environment)

getDeploymentStatus

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment

try:
    # getDeploymentStatus
    api_response = api_instance.get_deployment_status_using_get(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_deployment_status_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 

### Return type

[**DeploymentStatusDetails**](DeploymentStatusDetails.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dump_file_list_using_get**
> dict(str, str) get_dump_file_list_using_get(application_family, application_id, environment, _date=_date)

getDumpFileList

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment
_date = '_date_example' # str | date (optional)

try:
    # getDumpFileList
    api_response = api_instance.get_dump_file_list_using_get(application_family, application_id, environment, _date=_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_dump_file_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 
 **_date** | **str**| date | [optional] 

### Return type

**dict(str, str)**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ecr_token_using_get**
> object get_ecr_token_using_get(host)

getEcrToken

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
host = 'host_example' # str | Host

try:
    # getEcrToken
    api_response = api_instance.get_ecr_token_using_get(host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_ecr_token_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| Host | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_meta_data_using_get**
> list[EnvironmentMetaData] get_environment_meta_data_using_get(application_family)

getEnvironmentMetaData

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily

try:
    # getEnvironmentMetaData
    api_response = api_instance.get_environment_meta_data_using_get(application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_environment_meta_data_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 

### Return type

[**list[EnvironmentMetaData]**](EnvironmentMetaData.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_using_get**
> Environment get_environment_using_get(application_family, id)

getEnvironment

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
id = 'id_example' # str | id

try:
    # getEnvironment
    api_response = api_instance.get_environment_using_get(application_family, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_environment_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **id** | **str**| id | 

### Return type

[**Environment**](Environment.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environments_using_get**
> list[Environment] get_environments_using_get(application_family)

getEnvironments

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily

try:
    # getEnvironments
    api_response = api_instance.get_environments_using_get(application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_environments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 

### Return type

[**list[Environment]**](Environment.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_executed_actions_for_application_using_get**
> list[ActionExecution] get_executed_actions_for_application_using_get(application_family, application_id)

getExecutedActionsForApplication

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId

try:
    # getExecutedActionsForApplication
    api_response = api_instance.get_executed_actions_for_application_using_get(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_executed_actions_for_application_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 

### Return type

[**list[ActionExecution]**](ActionExecution.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images_using_get**
> list[str] get_images_using_get(application_family, application_id)

getImages

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId

try:
    # getImages
    api_response = api_instance.get_images_using_get(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_images_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitoring_details_using_get**
> Monitoring get_monitoring_details_using_get(application_family, application_id, environment)

getMonitoringDetails

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment

try:
    # getMonitoringDetails
    api_response = api_instance.get_monitoring_details_using_get(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_monitoring_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 

### Return type

[**Monitoring**](Monitoring.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_build_details_using_get**
> TestBuildDetails get_test_build_details_using_get(application_family, application_id, build_id)

getTestBuildDetails

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
build_id = 'build_id_example' # str | buildId

try:
    # getTestBuildDetails
    api_response = api_instance.get_test_build_details_using_get(application_family, application_id, build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_test_build_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **build_id** | **str**| buildId | 

### Return type

[**TestBuildDetails**](TestBuildDetails.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_using_get**
> list[User] get_users_using_get()

getUsers

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    # getUsers
    api_response = api_instance.get_users_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_users_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[User]**](User.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **global_stats_using_get**
> GlobalStats global_stats_using_get()

globalStats

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    # globalStats
    api_response = api_instance.global_stats_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->global_stats_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GlobalStats**](GlobalStats.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **halt_application_using_post**
> bool halt_application_using_post(application_family, application_id, environment)

haltApplication

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment

try:
    # haltApplication
    api_response = api_instance.halt_application_using_post(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->halt_application_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_using_delete**
> str login_using_delete()

login

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    # login
    api_response = api_instance.login_using_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->login_using_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_using_get**
> str login_using_get()

login

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    # login
    api_response = api_instance.login_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->login_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_using_head**
> str login_using_head()

login

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    # login
    api_response = api_instance.login_using_head()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->login_using_head: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_using_options**
> str login_using_options()

login

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    # login
    api_response = api_instance.login_using_options()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->login_using_options: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_using_patch**
> str login_using_patch()

login

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    # login
    api_response = api_instance.login_using_patch()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->login_using_patch: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_using_post**
> str login_using_post()

login

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    # login
    api_response = api_instance.login_using_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->login_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_using_put**
> str login_using_put()

login

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    # login
    api_response = api_instance.login_using_put()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->login_using_put: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_using_get**
> SimpleOauth2User me_using_get()

me

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    # me
    api_response = api_instance.me_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->me_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SimpleOauth2User**](SimpleOauth2User.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_webhook_pr_bitbucket_using_post**
> object process_webhook_pr_bitbucket_using_post(host, x_event_key, application_family, application_id, webhook)

processWebhookPRBitbucket

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
host = 'host_example' # str | Host
x_event_key = 'x_event_key_example' # str | X-Event-Key
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
webhook = swagger_client.BitbucketPREvent() # BitbucketPREvent | webhook

try:
    # processWebhookPRBitbucket
    api_response = api_instance.process_webhook_pr_bitbucket_using_post(host, x_event_key, application_family, application_id, webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->process_webhook_pr_bitbucket_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| Host | 
 **x_event_key** | **str**| X-Event-Key | 
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **webhook** | [**BitbucketPREvent**](BitbucketPREvent.md)| webhook | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_webhook_pr_github_using_post**
> object process_webhook_pr_github_using_post(host, application_family, application_id, webhook)

processWebhookPRGithub

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
host = 'host_example' # str | Host
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
webhook = swagger_client.GithubPREvent() # GithubPREvent | webhook

try:
    # processWebhookPRGithub
    api_response = api_instance.process_webhook_pr_github_using_post(host, application_family, application_id, webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->process_webhook_pr_github_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| Host | 
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **webhook** | [**GithubPREvent**](GithubPREvent.md)| webhook | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeploy_using_post**
> dict(str, bool) redeploy_using_post(application_family, environment)

redeploy

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
environment = 'environment_example' # str | environment

try:
    # redeploy
    api_response = api_instance.redeploy_using_post(application_family, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->redeploy_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **environment** | **str**| environment | 

### Return type

**dict(str, bool)**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_build_details_using_put**
> bool refresh_build_details_using_put(code_build_id)

refreshBuildDetails

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
code_build_id = 'code_build_id_example' # str | codeBuildId

try:
    # refreshBuildDetails
    api_response = api_instance.refresh_build_details_using_put(code_build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->refresh_build_details_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_build_id** | **str**| codeBuildId | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_application_using_post**
> bool resume_application_using_post(application_family, application_id, environment)

resumeApplication

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
environment = 'environment_example' # str | environment

try:
    # resumeApplication
    api_response = api_instance.resume_application_using_post(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->resume_application_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **environment** | **str**| environment | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_secrets_using_put**
> list[ApplicationSecret] update_application_secrets_using_put(application_family, application_id, application_secrets, environment)

updateApplicationSecrets

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
application_secrets = [swagger_client.ApplicationSecret()] # list[ApplicationSecret] | applicationSecrets
environment = 'environment_example' # str | environment

try:
    # updateApplicationSecrets
    api_response = api_instance.update_application_secrets_using_put(application_family, application_id, application_secrets, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->update_application_secrets_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **application_secrets** | [**list[ApplicationSecret]**](ApplicationSecret.md)| applicationSecrets | 
 **environment** | **str**| environment | 

### Return type

[**list[ApplicationSecret]**](ApplicationSecret.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_using_put**
> Application update_application_using_put(application, application_family)

updateApplication

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application = swagger_client.Application() # Application | application
application_family = 'application_family_example' # str | applicationFamily

try:
    # updateApplication
    api_response = api_instance.update_application_using_put(application, application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->update_application_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | [**Application**](Application.md)| application | 
 **application_family** | **str**| applicationFamily | 

### Return type

[**Application**](Application.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_build_using_put**
> Build update_build_using_put(application_family, application_id, build, build_id)

updateBuild

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_id = 'application_id_example' # str | applicationId
build = swagger_client.Build() # Build | build
build_id = 'build_id_example' # str | buildId

try:
    # updateBuild
    api_response = api_instance.update_build_using_put(application_family, application_id, build, build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->update_build_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_id** | **str**| applicationId | 
 **build** | [**Build**](Build.md)| build | 
 **build_id** | **str**| buildId | 

### Return type

[**Build**](Build.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_using_put**
> User update_user_using_put(user, user_id)

updateUser

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
user = swagger_client.User() # User | user
user_id = 'user_id_example' # str | userId

try:
    # updateUser
    api_response = api_instance.update_user_using_put(user, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->update_user_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| user | 
 **user_id** | **str**| userId | 

### Return type

[**User**](User.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_application_family_metadata_using_post**
> ApplicationFamilyMetadata upsert_application_family_metadata_using_post(application_family, application_family_metadata)

upsertApplicationFamilyMetadata

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
application_family_metadata = swagger_client.ApplicationFamilyMetadata() # ApplicationFamilyMetadata | applicationFamilyMetadata

try:
    # upsertApplicationFamilyMetadata
    api_response = api_instance.upsert_application_family_metadata_using_post(application_family, application_family_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->upsert_application_family_metadata_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **application_family_metadata** | [**ApplicationFamilyMetadata**](ApplicationFamilyMetadata.md)| applicationFamilyMetadata | 

### Return type

[**ApplicationFamilyMetadata**](ApplicationFamilyMetadata.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_environment_using_post**
> Environment upsert_environment_using_post(application_family, environment)

upsertEnvironment

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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | applicationFamily
environment = swagger_client.Environment() # Environment | environment

try:
    # upsertEnvironment
    api_response = api_instance.upsert_environment_using_post(application_family, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->upsert_environment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**| applicationFamily | 
 **environment** | [**Environment**](Environment.md)| environment | 

### Return type

[**Environment**](Environment.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

