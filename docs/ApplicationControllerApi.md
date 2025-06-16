# swagger_client.ApplicationControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build**](ApplicationControllerApi.md#build) | **POST** /api/{applicationFamily}/applications/{applicationId}/builds | 
[**change_password**](ApplicationControllerApi.md#change_password) | **PUT** /api/users/{userId}/changePassword | 
[**create_app_secret_request**](ApplicationControllerApi.md#create_app_secret_request) | **POST** /api/{applicationFamily}/applications/{applicationId}/secretRequests | 
[**create_application**](ApplicationControllerApi.md#create_application) | **POST** /api/{applicationFamily}/applications | 
[**create_ecr_registry**](ApplicationControllerApi.md#create_ecr_registry) | **POST** /api/ecrRegistry | 
[**create_generic_action**](ApplicationControllerApi.md#create_generic_action) | **POST** /api/buildType/{buildType}/actions | 
[**create_user**](ApplicationControllerApi.md#create_user) | **POST** /api/users | 
[**create_user_cc**](ApplicationControllerApi.md#create_user_cc) | **POST** /api/cc-users | 
[**delete_application**](ApplicationControllerApi.md#delete_application) | **DELETE** /api/{applicationFamily}/applications/{applicationId} | 
[**delete_application_secret**](ApplicationControllerApi.md#delete_application_secret) | **DELETE** /api/{applicationFamily}/{environment}/applications/{applicationId}/secrets/{secretName} | 
[**deploy**](ApplicationControllerApi.md#deploy) | **POST** /api/{applicationFamily}/{environment}/applications/{applicationId}/deployments | 
[**disable_alerting**](ApplicationControllerApi.md#disable_alerting) | **DELETE** /api/{applicationFamily}/{environment}/applications/{applicationId}/alerting | 
[**disable_monitoring**](ApplicationControllerApi.md#disable_monitoring) | **DELETE** /api/{applicationFamily}/{environment}/applications/{applicationId}/monitoring | 
[**download_dump_file**](ApplicationControllerApi.md#download_dump_file) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/dumps/download | 
[**download_test_report**](ApplicationControllerApi.md#download_test_report) | **GET** /api/{applicationFamily}/applications/{applicationId}/builds/{buildId}/downloadArtifacts | 
[**enable_alerting**](ApplicationControllerApi.md#enable_alerting) | **POST** /api/{applicationFamily}/{environment}/applications/{applicationId}/alerting | 
[**enable_monitoring**](ApplicationControllerApi.md#enable_monitoring) | **POST** /api/{applicationFamily}/{environment}/applications/{applicationId}/monitoring | 
[**execute_action_on_pod**](ApplicationControllerApi.md#execute_action_on_pod) | **POST** /api/{applicationFamily}/{environment}/applications/{applicationId}/pods/{podName}/actions/executeAction | 
[**get_actions_for_pod**](ApplicationControllerApi.md#get_actions_for_pod) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/pods/{podName}/actions | 
[**get_alerting_details**](ApplicationControllerApi.md#get_alerting_details) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/alerting | 
[**get_all_application_metrics**](ApplicationControllerApi.md#get_all_application_metrics) | **GET** /api/{applicationFamily}/appmetrics | 
[**get_all_registries**](ApplicationControllerApi.md#get_all_registries) | **GET** /api/getRegistries | 
[**get_application1**](ApplicationControllerApi.md#get_application1) | **GET** /api/{applicationFamily}/applications/{applicationId} | 
[**get_application_branches**](ApplicationControllerApi.md#get_application_branches) | **GET** /api/{applicationFamily}/applications/{applicationId}/branches | 
[**get_application_families**](ApplicationControllerApi.md#get_application_families) | **GET** /api/applicationFamilies | 
[**get_application_metric_summary**](ApplicationControllerApi.md#get_application_metric_summary) | **GET** /api/{applicationFamily}/applications/{applicationId}/metrics | 
[**get_application_pod_details**](ApplicationControllerApi.md#get_application_pod_details) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/podDetails | 
[**get_application_secret_requests**](ApplicationControllerApi.md#get_application_secret_requests) | **GET** /api/{applicationFamily}/applications/{applicationId}/secretRequests | 
[**get_application_secrets**](ApplicationControllerApi.md#get_application_secrets) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/secretRequests | 
[**get_application_tags**](ApplicationControllerApi.md#get_application_tags) | **GET** /api/{applicationFamily}/applications/{applicationId}/tags | 
[**get_application_types**](ApplicationControllerApi.md#get_application_types) | **GET** /api/applicationTypes | 
[**get_applications**](ApplicationControllerApi.md#get_applications) | **GET** /api/{applicationFamily}/applications | 
[**get_build**](ApplicationControllerApi.md#get_build) | **GET** /api/{applicationFamily}/applications/{applicationId}/builds/{buildId} | 
[**get_build_logs**](ApplicationControllerApi.md#get_build_logs) | **GET** /api/{applicationFamily}/applications/{applicationId}/builds/{buildId}/logs | 
[**get_builds**](ApplicationControllerApi.md#get_builds) | **GET** /api/{applicationFamily}/applications/{applicationId}/builds | 
[**get_cc_environment_meta_data**](ApplicationControllerApi.md#get_cc_environment_meta_data) | **GET** /api/cc/{applicationFamily}/environmentMetaData | 
[**get_current_deployment**](ApplicationControllerApi.md#get_current_deployment) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/deployment/current | 
[**get_deployment_status**](ApplicationControllerApi.md#get_deployment_status) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/deploymentStatus | 
[**get_dump_file_list**](ApplicationControllerApi.md#get_dump_file_list) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/dumps | 
[**get_ecr_token**](ApplicationControllerApi.md#get_ecr_token) | **GET** /api/getEcrLoginToken | 
[**get_environment**](ApplicationControllerApi.md#get_environment) | **GET** /api/{applicationFamily}/environments/{id} | 
[**get_environment_meta_data**](ApplicationControllerApi.md#get_environment_meta_data) | **GET** /api/{applicationFamily}/environmentMetaData | 
[**get_environments**](ApplicationControllerApi.md#get_environments) | **GET** /api/{applicationFamily}/environments | 
[**get_executed_actions_for_application**](ApplicationControllerApi.md#get_executed_actions_for_application) | **GET** /api/{applicationFamily}/applications/{applicationId}/executedActions | 
[**get_images**](ApplicationControllerApi.md#get_images) | **GET** /api/{applicationFamily}/applications/{applicationId}/images | 
[**get_monitoring_details**](ApplicationControllerApi.md#get_monitoring_details) | **GET** /api/{applicationFamily}/{environment}/applications/{applicationId}/monitoring | 
[**get_test_build_details**](ApplicationControllerApi.md#get_test_build_details) | **GET** /api/{applicationFamily}/applications/{applicationId}/builds/{buildId}/testDetails | 
[**get_users**](ApplicationControllerApi.md#get_users) | **GET** /api/users | 
[**global_stats**](ApplicationControllerApi.md#global_stats) | **GET** /api/stats | 
[**halt_application**](ApplicationControllerApi.md#halt_application) | **POST** /api/{applicationFamily}/{environment}/applications/{applicationId}/halt | 
[**login**](ApplicationControllerApi.md#login) | **GET** /api/login | 
[**login1**](ApplicationControllerApi.md#login1) | **HEAD** /api/login | 
[**login2**](ApplicationControllerApi.md#login2) | **POST** /api/login | 
[**login3**](ApplicationControllerApi.md#login3) | **PUT** /api/login | 
[**login4**](ApplicationControllerApi.md#login4) | **PATCH** /api/login | 
[**login5**](ApplicationControllerApi.md#login5) | **DELETE** /api/login | 
[**login6**](ApplicationControllerApi.md#login6) | **OPTIONS** /api/login | 
[**me**](ApplicationControllerApi.md#me) | **GET** /api/me | 
[**process_webhook_pr_bitbucket**](ApplicationControllerApi.md#process_webhook_pr_bitbucket) | **POST** /api/{applicationFamily}/applications/{applicationId}/webhooks/pr/bitbucket | 
[**process_webhook_pr_github**](ApplicationControllerApi.md#process_webhook_pr_github) | **POST** /api/{applicationFamily}/applications/{applicationId}/webhooks/pr/github | 
[**redeploy**](ApplicationControllerApi.md#redeploy) | **POST** /api/{applicationFamily}/{environment}/redeployment | 
[**refresh_build_details**](ApplicationControllerApi.md#refresh_build_details) | **PUT** /api/codebuild/builds/{codeBuildId}/refresh | 
[**resume_application**](ApplicationControllerApi.md#resume_application) | **POST** /api/{applicationFamily}/{environment}/applications/{applicationId}/resume | 
[**update_application**](ApplicationControllerApi.md#update_application) | **PUT** /api/{applicationFamily}/applications | 
[**update_application_secrets**](ApplicationControllerApi.md#update_application_secrets) | **PUT** /api/{applicationFamily}/{environment}/applications/{applicationId}/secrets | 
[**update_build**](ApplicationControllerApi.md#update_build) | **PUT** /api/{applicationFamily}/applications/{applicationId}/builds/{buildId} | 
[**update_user**](ApplicationControllerApi.md#update_user) | **PUT** /api/users/{userId} | 
[**upsert_application_family_metadata**](ApplicationControllerApi.md#upsert_application_family_metadata) | **POST** /api/applicationFamilies/{applicationFamily}/metadata | 
[**upsert_environment**](ApplicationControllerApi.md#upsert_environment) | **POST** /api/{applicationFamily}/environments | 

# **build**
> ComCapillaryOpsDeployerBoBuild build(body, application_family, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoBuild() # ComCapillaryOpsDeployerBoBuild | 
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.build(body, application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoBuild**](ComCapillaryOpsDeployerBoBuild.md)|  | 
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoBuild**](ComCapillaryOpsDeployerBoBuild.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password**
> ComCapillaryOpsDeployerBoUser change_password(body, user_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoPasswordChange() # ComCapillaryOpsDeployerBoPasswordChange | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.change_password(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoPasswordChange**](ComCapillaryOpsDeployerBoPasswordChange.md)|  | 
 **user_id** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoUser**](ComCapillaryOpsDeployerBoUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_secret_request**
> list[ComCapillaryOpsDeployerBoApplicationSecretRequestSecretName] create_app_secret_request(body, application_family, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ComCapillaryOpsDeployerBoApplicationSecretRequestSecretName()] # list[ComCapillaryOpsDeployerBoApplicationSecretRequestSecretName] | 
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.create_app_secret_request(body, application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->create_app_secret_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ComCapillaryOpsDeployerBoApplicationSecretRequestSecretName]**](ComCapillaryOpsDeployerBoApplicationSecretRequestSecretName.md)|  | 
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsDeployerBoApplicationSecretRequestSecretName]**](ComCapillaryOpsDeployerBoApplicationSecretRequestSecretName.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application**
> ComCapillaryOpsDeployerBoApplication create_application(body, application_family)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoApplication() # ComCapillaryOpsDeployerBoApplication | 
application_family = 'application_family_example' # str | 

try:
    api_response = api_instance.create_application(body, application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->create_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoApplication**](ComCapillaryOpsDeployerBoApplication.md)|  | 
 **application_family** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoApplication**](ComCapillaryOpsDeployerBoApplication.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ecr_registry**
> ComCapillaryOpsDeployerBoECRRegistry create_ecr_registry(body)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoECRRegistry() # ComCapillaryOpsDeployerBoECRRegistry | 

try:
    api_response = api_instance.create_ecr_registry(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->create_ecr_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoECRRegistry**](ComCapillaryOpsDeployerBoECRRegistry.md)|  | 

### Return type

[**ComCapillaryOpsDeployerBoECRRegistry**](ComCapillaryOpsDeployerBoECRRegistry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_generic_action**
> ComCapillaryOpsDeployerBoActionsApplicationAction create_generic_action(body, build_type)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoActionsApplicationAction() # ComCapillaryOpsDeployerBoActionsApplicationAction | 
build_type = 'build_type_example' # str | 

try:
    api_response = api_instance.create_generic_action(body, build_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->create_generic_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoActionsApplicationAction**](ComCapillaryOpsDeployerBoActionsApplicationAction.md)|  | 
 **build_type** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoActionsApplicationAction**](ComCapillaryOpsDeployerBoActionsApplicationAction.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> ComCapillaryOpsDeployerBoUser create_user(body)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoUser() # ComCapillaryOpsDeployerBoUser | 

try:
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoUser**](ComCapillaryOpsDeployerBoUser.md)|  | 

### Return type

[**ComCapillaryOpsDeployerBoUser**](ComCapillaryOpsDeployerBoUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_cc**
> ComCapillaryOpsDeployerBoUser create_user_cc(body)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoUser() # ComCapillaryOpsDeployerBoUser | 

try:
    api_response = api_instance.create_user_cc(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->create_user_cc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoUser**](ComCapillaryOpsDeployerBoUser.md)|  | 

### Return type

[**ComCapillaryOpsDeployerBoUser**](ComCapillaryOpsDeployerBoUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> bool delete_application(application_family, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.delete_application(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->delete_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_secret**
> bool delete_application_secret(application_family, environment, application_id, secret_name)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
environment = 'environment_example' # str | 
application_id = 'application_id_example' # str | 
secret_name = 'secret_name_example' # str | 

try:
    api_response = api_instance.delete_application_secret(application_family, environment, application_id, secret_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->delete_application_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **environment** | **str**|  | 
 **application_id** | **str**|  | 
 **secret_name** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy**
> ComCapillaryOpsDeployerBoDeployment deploy(body, application_family, environment, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoDeployment() # ComCapillaryOpsDeployerBoDeployment | 
application_family = 'application_family_example' # str | 
environment = 'environment_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.deploy(body, application_family, environment, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->deploy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoDeployment**](ComCapillaryOpsDeployerBoDeployment.md)|  | 
 **application_family** | **str**|  | 
 **environment** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoDeployment**](ComCapillaryOpsDeployerBoDeployment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_alerting**
> bool disable_alerting(application_family, application_id, environment)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 
environment = 'environment_example' # str | 

try:
    api_response = api_instance.disable_alerting(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->disable_alerting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 
 **environment** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_monitoring**
> bool disable_monitoring(application_family, application_id, environment)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 
environment = 'environment_example' # str | 

try:
    api_response = api_instance.disable_monitoring(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->disable_monitoring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 
 **environment** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_dump_file**
> str download_dump_file(application_family, environment, path, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
environment = 'environment_example' # str | 
path = 'path_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.download_dump_file(application_family, environment, path, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->download_dump_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **environment** | **str**|  | 
 **path** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_test_report**
> str download_test_report(application_family, application_id, build_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 
build_id = 'build_id_example' # str | 

try:
    api_response = api_instance.download_test_report(application_family, application_id, build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->download_test_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 
 **build_id** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_alerting**
> bool enable_alerting(application_family, application_id, environment)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 
environment = 'environment_example' # str | 

try:
    api_response = api_instance.enable_alerting(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->enable_alerting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 
 **environment** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_monitoring**
> bool enable_monitoring(application_family, application_id, environment)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 
environment = 'environment_example' # str | 

try:
    api_response = api_instance.enable_monitoring(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->enable_monitoring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 
 **environment** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_action_on_pod**
> ComCapillaryOpsDeployerBoActionsActionExecution execute_action_on_pod(body, application_family, environment, application_id, pod_name)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoActionsApplicationAction() # ComCapillaryOpsDeployerBoActionsApplicationAction | 
application_family = 'application_family_example' # str | 
environment = 'environment_example' # str | 
application_id = 'application_id_example' # str | 
pod_name = 'pod_name_example' # str | 

try:
    api_response = api_instance.execute_action_on_pod(body, application_family, environment, application_id, pod_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->execute_action_on_pod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoActionsApplicationAction**](ComCapillaryOpsDeployerBoActionsApplicationAction.md)|  | 
 **application_family** | **str**|  | 
 **environment** | **str**|  | 
 **application_id** | **str**|  | 
 **pod_name** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoActionsActionExecution**](ComCapillaryOpsDeployerBoActionsActionExecution.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_for_pod**
> list[ComCapillaryOpsDeployerBoActionsApplicationAction] get_actions_for_pod(application_family, environment, application_id, pod_name)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
environment = 'environment_example' # str | 
application_id = 'application_id_example' # str | 
pod_name = 'pod_name_example' # str | 

try:
    api_response = api_instance.get_actions_for_pod(application_family, environment, application_id, pod_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_actions_for_pod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **environment** | **str**|  | 
 **application_id** | **str**|  | 
 **pod_name** | **str**|  | 

### Return type

[**list[ComCapillaryOpsDeployerBoActionsApplicationAction]**](ComCapillaryOpsDeployerBoActionsApplicationAction.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerting_details**
> ComCapillaryOpsDeployerBoAlerting get_alerting_details(application_family, application_id, environment)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 
environment = 'environment_example' # str | 

try:
    api_response = api_instance.get_alerting_details(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_alerting_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 
 **environment** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoAlerting**](ComCapillaryOpsDeployerBoAlerting.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_application_metrics**
> list[ComCapillaryOpsDeployerBoApplicationMetricsWrapper] get_all_application_metrics(application_family)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 

try:
    api_response = api_instance.get_all_application_metrics(application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_all_application_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 

### Return type

[**list[ComCapillaryOpsDeployerBoApplicationMetricsWrapper]**](ComCapillaryOpsDeployerBoApplicationMetricsWrapper.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_registries**
> list[ComCapillaryOpsDeployerBoRegistry] get_all_registries()



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_registries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_all_registries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsDeployerBoRegistry]**](ComCapillaryOpsDeployerBoRegistry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application1**
> ComCapillaryOpsDeployerBoApplication get_application1(application_family, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.get_application1(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoApplication**](ComCapillaryOpsDeployerBoApplication.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_branches**
> list[str] get_application_branches(application_family, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.get_application_branches(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_branches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_families**
> list[str] get_application_families()



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_application_families()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_families: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_metric_summary**
> dict(str, ComCapillaryOpsDeployerBoApplicationMetrics) get_application_metric_summary(application_family, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.get_application_metric_summary(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_metric_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

[**dict(str, ComCapillaryOpsDeployerBoApplicationMetrics)**](ComCapillaryOpsDeployerBoApplicationMetrics.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_pod_details**
> list[ComCapillaryOpsDeployerBoApplicationPodDetails] get_application_pod_details(application_family, environment, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
environment = 'environment_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.get_application_pod_details(application_family, environment, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_pod_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **environment** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsDeployerBoApplicationPodDetails]**](ComCapillaryOpsDeployerBoApplicationPodDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_secret_requests**
> list[ComCapillaryOpsDeployerBoApplicationSecretRequest] get_application_secret_requests(application_family, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.get_application_secret_requests(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_secret_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsDeployerBoApplicationSecretRequest]**](ComCapillaryOpsDeployerBoApplicationSecretRequest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_secrets**
> list[ComCapillaryOpsDeployerBoApplicationSecretSecretName] get_application_secrets(application_family, environment, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
environment = 'environment_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.get_application_secrets(application_family, environment, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_secrets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **environment** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsDeployerBoApplicationSecretSecretName]**](ComCapillaryOpsDeployerBoApplicationSecretSecretName.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_tags**
> list[str] get_application_tags(application_family, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.get_application_tags(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_types**
> list[str] get_application_types()



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_application_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_application_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications**
> list[ComCapillaryOpsDeployerBoApplication] get_applications(application_family)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 

try:
    api_response = api_instance.get_applications(application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 

### Return type

[**list[ComCapillaryOpsDeployerBoApplication]**](ComCapillaryOpsDeployerBoApplication.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build**
> ComCapillaryOpsDeployerBoBuild get_build(application_family, application_id, build_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 
build_id = 'build_id_example' # str | 

try:
    api_response = api_instance.get_build(application_family, application_id, build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 
 **build_id** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoBuild**](ComCapillaryOpsDeployerBoBuild.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_logs**
> ComCapillaryOpsDeployerBoTokenPaginatedResponseComCapillaryOpsDeployerBoLogEvent get_build_logs(application_family, application_id, build_id, next_token=next_token)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 
build_id = 'build_id_example' # str | 
next_token = 'next_token_example' # str |  (optional)

try:
    api_response = api_instance.get_build_logs(application_family, application_id, build_id, next_token=next_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_build_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 
 **build_id** | **str**|  | 
 **next_token** | **str**|  | [optional] 

### Return type

[**ComCapillaryOpsDeployerBoTokenPaginatedResponseComCapillaryOpsDeployerBoLogEvent**](ComCapillaryOpsDeployerBoTokenPaginatedResponseComCapillaryOpsDeployerBoLogEvent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_builds**
> list[ComCapillaryOpsDeployerBoBuild] get_builds(application_family, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.get_builds(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsDeployerBoBuild]**](ComCapillaryOpsDeployerBoBuild.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cc_environment_meta_data**
> list[ComCapillaryOpsDeployerBoEnvironmentMetaData] get_cc_environment_meta_data(application_family)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 

try:
    api_response = api_instance.get_cc_environment_meta_data(application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_cc_environment_meta_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 

### Return type

[**list[ComCapillaryOpsDeployerBoEnvironmentMetaData]**](ComCapillaryOpsDeployerBoEnvironmentMetaData.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_deployment**
> ComCapillaryOpsDeployerBoDeployment get_current_deployment(application_family, application_id, environment)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 
environment = 'environment_example' # str | 

try:
    api_response = api_instance.get_current_deployment(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_current_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 
 **environment** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoDeployment**](ComCapillaryOpsDeployerBoDeployment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_status**
> ComCapillaryOpsDeployerBoDeploymentStatusDetails get_deployment_status(application_family, environment, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
environment = 'environment_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.get_deployment_status(application_family, environment, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_deployment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **environment** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoDeploymentStatusDetails**](ComCapillaryOpsDeployerBoDeploymentStatusDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dump_file_list**
> dict(str, str) get_dump_file_list(application_family, environment, application_id, _date=_date)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
environment = 'environment_example' # str | 
application_id = 'application_id_example' # str | 
_date = '_date_example' # str |  (optional)

try:
    api_response = api_instance.get_dump_file_list(application_family, environment, application_id, _date=_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_dump_file_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **environment** | **str**|  | 
 **application_id** | **str**|  | 
 **_date** | **str**|  | [optional] 

### Return type

**dict(str, str)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ecr_token**
> object get_ecr_token(host)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
host = 'host_example' # str | 

try:
    api_response = api_instance.get_ecr_token(host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_ecr_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment**
> ComCapillaryOpsDeployerBoEnvironment get_environment(application_family, id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
id = 'id_example' # str | 

try:
    api_response = api_instance.get_environment(application_family, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoEnvironment**](ComCapillaryOpsDeployerBoEnvironment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_meta_data**
> list[ComCapillaryOpsDeployerBoEnvironmentMetaData] get_environment_meta_data(application_family)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 

try:
    api_response = api_instance.get_environment_meta_data(application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_environment_meta_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 

### Return type

[**list[ComCapillaryOpsDeployerBoEnvironmentMetaData]**](ComCapillaryOpsDeployerBoEnvironmentMetaData.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environments**
> list[ComCapillaryOpsDeployerBoEnvironment] get_environments(application_family)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 

try:
    api_response = api_instance.get_environments(application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 

### Return type

[**list[ComCapillaryOpsDeployerBoEnvironment]**](ComCapillaryOpsDeployerBoEnvironment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_executed_actions_for_application**
> list[ComCapillaryOpsDeployerBoActionsActionExecution] get_executed_actions_for_application(application_family, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.get_executed_actions_for_application(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_executed_actions_for_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsDeployerBoActionsActionExecution]**](ComCapillaryOpsDeployerBoActionsActionExecution.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> list[str] get_images(application_family, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.get_images(application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitoring_details**
> ComCapillaryOpsDeployerBoMonitoring get_monitoring_details(application_family, application_id, environment)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 
environment = 'environment_example' # str | 

try:
    api_response = api_instance.get_monitoring_details(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_monitoring_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 
 **environment** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoMonitoring**](ComCapillaryOpsDeployerBoMonitoring.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_build_details**
> ComCapillaryOpsDeployerBoTestBuildDetails get_test_build_details(application_family, application_id, build_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 
build_id = 'build_id_example' # str | 

try:
    api_response = api_instance.get_test_build_details(application_family, application_id, build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_test_build_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 
 **build_id** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoTestBuildDetails**](ComCapillaryOpsDeployerBoTestBuildDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[ComCapillaryOpsDeployerBoUser] get_users()



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->get_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsDeployerBoUser]**](ComCapillaryOpsDeployerBoUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **global_stats**
> ComCapillaryOpsDeployerBoGlobalStats global_stats()



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.global_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->global_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ComCapillaryOpsDeployerBoGlobalStats**](ComCapillaryOpsDeployerBoGlobalStats.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **halt_application**
> bool halt_application(application_family, application_id, environment)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 
environment = 'environment_example' # str | 

try:
    api_response = api_instance.halt_application(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->halt_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 
 **environment** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> str login()



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.login()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->login: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login1**
> str login1()



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.login1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->login1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login2**
> str login2()



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.login2()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->login2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login3**
> str login3()



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.login3()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->login3: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login4**
> str login4()



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.login4()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->login4: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login5**
> str login5()



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.login5()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->login5: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login6**
> str login6()



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.login6()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->login6: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me**
> ComCapillaryOpsDeployerServiceOAuth2UserServiceImplSimpleOauth2User me()



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ComCapillaryOpsDeployerServiceOAuth2UserServiceImplSimpleOauth2User**](ComCapillaryOpsDeployerServiceOAuth2UserServiceImplSimpleOauth2User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_webhook_pr_bitbucket**
> object process_webhook_pr_bitbucket(body, x_event_key, host, application_family, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoWebhookBitbucketBitbucketPREvent() # ComCapillaryOpsDeployerBoWebhookBitbucketBitbucketPREvent | 
x_event_key = 'x_event_key_example' # str | 
host = 'host_example' # str | 
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.process_webhook_pr_bitbucket(body, x_event_key, host, application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->process_webhook_pr_bitbucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoWebhookBitbucketBitbucketPREvent**](ComCapillaryOpsDeployerBoWebhookBitbucketBitbucketPREvent.md)|  | 
 **x_event_key** | **str**|  | 
 **host** | **str**|  | 
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_webhook_pr_github**
> object process_webhook_pr_github(body, host, application_family, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoWebhookGithubGithubPREvent() # ComCapillaryOpsDeployerBoWebhookGithubGithubPREvent | 
host = 'host_example' # str | 
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.process_webhook_pr_github(body, host, application_family, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->process_webhook_pr_github: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoWebhookGithubGithubPREvent**](ComCapillaryOpsDeployerBoWebhookGithubGithubPREvent.md)|  | 
 **host** | **str**|  | 
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeploy**
> dict(str, bool) redeploy(application_family, environment)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
environment = 'environment_example' # str | 

try:
    api_response = api_instance.redeploy(application_family, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->redeploy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **environment** | **str**|  | 

### Return type

**dict(str, bool)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_build_details**
> bool refresh_build_details(code_build_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
code_build_id = 'code_build_id_example' # str | 

try:
    api_response = api_instance.refresh_build_details(code_build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->refresh_build_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_build_id** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_application**
> bool resume_application(application_family, application_id, environment)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 
environment = 'environment_example' # str | 

try:
    api_response = api_instance.resume_application(application_family, application_id, environment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->resume_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 
 **environment** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application**
> ComCapillaryOpsDeployerBoApplication update_application(body, application_family)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoApplication() # ComCapillaryOpsDeployerBoApplication | 
application_family = 'application_family_example' # str | 

try:
    api_response = api_instance.update_application(body, application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->update_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoApplication**](ComCapillaryOpsDeployerBoApplication.md)|  | 
 **application_family** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoApplication**](ComCapillaryOpsDeployerBoApplication.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_secrets**
> list[ComCapillaryOpsDeployerBoApplicationSecretSecretName] update_application_secrets(body, application_family, environment, application_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ComCapillaryOpsDeployerBoApplicationSecretSecretName()] # list[ComCapillaryOpsDeployerBoApplicationSecretSecretName] | 
application_family = 'application_family_example' # str | 
environment = 'environment_example' # str | 
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.update_application_secrets(body, application_family, environment, application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->update_application_secrets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ComCapillaryOpsDeployerBoApplicationSecretSecretName]**](ComCapillaryOpsDeployerBoApplicationSecretSecretName.md)|  | 
 **application_family** | **str**|  | 
 **environment** | **str**|  | 
 **application_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsDeployerBoApplicationSecretSecretName]**](ComCapillaryOpsDeployerBoApplicationSecretSecretName.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_build**
> ComCapillaryOpsDeployerBoBuild update_build(body, application_family, application_id, build_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoBuild() # ComCapillaryOpsDeployerBoBuild | 
application_family = 'application_family_example' # str | 
application_id = 'application_id_example' # str | 
build_id = 'build_id_example' # str | 

try:
    api_response = api_instance.update_build(body, application_family, application_id, build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->update_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoBuild**](ComCapillaryOpsDeployerBoBuild.md)|  | 
 **application_family** | **str**|  | 
 **application_id** | **str**|  | 
 **build_id** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoBuild**](ComCapillaryOpsDeployerBoBuild.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> ComCapillaryOpsDeployerBoUser update_user(body, user_id)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoUser() # ComCapillaryOpsDeployerBoUser | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.update_user(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoUser**](ComCapillaryOpsDeployerBoUser.md)|  | 
 **user_id** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoUser**](ComCapillaryOpsDeployerBoUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_application_family_metadata**
> ComCapillaryOpsDeployerBoApplicationFamilyMetadata upsert_application_family_metadata(body, application_family)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoApplicationFamilyMetadata() # ComCapillaryOpsDeployerBoApplicationFamilyMetadata | 
application_family = 'application_family_example' # str | 

try:
    api_response = api_instance.upsert_application_family_metadata(body, application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->upsert_application_family_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoApplicationFamilyMetadata**](ComCapillaryOpsDeployerBoApplicationFamilyMetadata.md)|  | 
 **application_family** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoApplicationFamilyMetadata**](ComCapillaryOpsDeployerBoApplicationFamilyMetadata.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_environment**
> ComCapillaryOpsDeployerBoEnvironment upsert_environment(body, application_family)



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
api_instance = swagger_client.ApplicationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsDeployerBoEnvironment() # ComCapillaryOpsDeployerBoEnvironment | 
application_family = 'application_family_example' # str | 

try:
    api_response = api_instance.upsert_environment(body, application_family)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationControllerApi->upsert_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsDeployerBoEnvironment**](ComCapillaryOpsDeployerBoEnvironment.md)|  | 
 **application_family** | **str**|  | 

### Return type

[**ComCapillaryOpsDeployerBoEnvironment**](ComCapillaryOpsDeployerBoEnvironment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

