# swagger_client.UiCiCdControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_rule_and_workflow_using_put**](UiCiCdControllerApi.md#attach_rule_and_workflow_using_put) | **PUT** /cc-ui/v1/ci-cd/attach | Attach Rule and Workflow
[**detach_rule_and_workflow_using_put**](UiCiCdControllerApi.md#detach_rule_and_workflow_using_put) | **PUT** /cc-ui/v1/ci-cd/detach | Detach Rule and Workflow
[**generate_artifact_push_credentials_using_post1**](UiCiCdControllerApi.md#generate_artifact_push_credentials_using_post1) | **POST** /cc-ui/v1/ci-cd/pushCredentials | Generate Artifact Push Credentials
[**get_ci_cd_details_using_get**](UiCiCdControllerApi.md#get_ci_cd_details_using_get) | **GET** /cc-ui/v1/ci-cd/{stackName} | Get CI/CD Details
[**register_artifact_saas_using_post1**](UiCiCdControllerApi.md#register_artifact_saas_using_post1) | **POST** /cc-ui/v1/ci-cd/register | Register Artifact SaaS
[**save_ci_cd_details_using_post**](UiCiCdControllerApi.md#save_ci_cd_details_using_post) | **POST** /cc-ui/v1/ci-cd | Save CI/CD Details

# **attach_rule_and_workflow_using_put**
> attach_rule_and_workflow_using_put(body)

Attach Rule and Workflow

- **Description:** Attaches a rule and workflow to an artifact CI.  - **Restrictions:** CI must exist or will be created for the project.  - **Permissions:** Requires `ARTIFACT_CI_WRITE` permission.  - **Audit Logging:** Not applicable.

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
api_instance = swagger_client.UiCiCdControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AttachDetachCiRequest() # AttachDetachCiRequest | attachDetachCiRequest

try:
    # Attach Rule and Workflow
    api_instance.attach_rule_and_workflow_using_put(body)
except ApiException as e:
    print("Exception when calling UiCiCdControllerApi->attach_rule_and_workflow_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttachDetachCiRequest**](AttachDetachCiRequest.md)| attachDetachCiRequest | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_rule_and_workflow_using_put**
> detach_rule_and_workflow_using_put(body)

Detach Rule and Workflow

- **Description:** Detaches a rule and workflow from an artifact CI.  - **Restrictions:** Existing CI registration required.  - **Permissions:** Requires `ARTIFACT_CI_WRITE` permission.  - **Audit Logging:** Not applicable.

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
api_instance = swagger_client.UiCiCdControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AttachDetachCiRequest() # AttachDetachCiRequest | attachDetachCiRequest

try:
    # Detach Rule and Workflow
    api_instance.detach_rule_and_workflow_using_put(body)
except ApiException as e:
    print("Exception when calling UiCiCdControllerApi->detach_rule_and_workflow_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttachDetachCiRequest**](AttachDetachCiRequest.md)| attachDetachCiRequest | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_artifact_push_credentials_using_post1**
> PushCredentialsResponse generate_artifact_push_credentials_using_post1(body)

Generate Artifact Push Credentials

- **Description:** Generates push credentials for an artifact.  - **Restrictions:** Only for supported artifactory types.  - **Permissions:** Requires `ARTIFACTS_WRITE` permission.  - **Audit Logging:** Not applicable.

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
api_instance = swagger_client.UiCiCdControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.PushCredentialsRequest() # PushCredentialsRequest | pushCredentialsRequest

try:
    # Generate Artifact Push Credentials
    api_response = api_instance.generate_artifact_push_credentials_using_post1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCiCdControllerApi->generate_artifact_push_credentials_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PushCredentialsRequest**](PushCredentialsRequest.md)| pushCredentialsRequest | 

### Return type

[**PushCredentialsResponse**](PushCredentialsResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ci_cd_details_using_get**
> CiCdDto get_ci_cd_details_using_get(stack_name)

Get CI/CD Details

- **Description:** Retrieves CI/CD details for a specified project name.  - **Restrictions:** Requires existing default artifact routing rule or promotion workflow.  - **Permissions:** None required.  - **Audit Logging:** Not applicable.

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
api_instance = swagger_client.UiCiCdControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # Get CI/CD Details
    api_response = api_instance.get_ci_cd_details_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCiCdControllerApi->get_ci_cd_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**CiCdDto**](CiCdDto.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_artifact_saas_using_post1**
> register_artifact_saas_using_post1(body)

Register Artifact SaaS

- **Description:** Registers a new artifact within the system for SaaS.  - **Restrictions:** Valid artifactory name and consistent registration type required. Blueprint must be CI/CD configured.  - **Permissions:** Requires `ARTIFACTS_WRITE` permission.  - **Audit Logging:** Not applicable.

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
api_instance = swagger_client.UiCiCdControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.SaasArtifactRequest() # SaasArtifactRequest | artifactRequest

try:
    # Register Artifact SaaS
    api_instance.register_artifact_saas_using_post1(body)
except ApiException as e:
    print("Exception when calling UiCiCdControllerApi->register_artifact_saas_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SaasArtifactRequest**](SaasArtifactRequest.md)| artifactRequest | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_ci_cd_details_using_post**
> save_ci_cd_details_using_post(body)

Save CI/CD Details

- **Description:** Saves CI/CD configuration details.  - **Restrictions:** Cannot change registration type after initial configuration.  - **Permissions:** Requires `CI_CD_CONFIGURE` permission.  - **Audit Logging:** This operation is logged for audit purposes.

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
api_instance = swagger_client.UiCiCdControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CiCdDto() # CiCdDto | ciCdDto

try:
    # Save CI/CD Details
    api_instance.save_ci_cd_details_using_post(body)
except ApiException as e:
    print("Exception when calling UiCiCdControllerApi->save_ci_cd_details_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CiCdDto**](CiCdDto.md)| ciCdDto | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

