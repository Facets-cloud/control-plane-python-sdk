# swagger_client.PublicApIsApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_feature_properties_using_get**](PublicApIsApi.md#get_all_feature_properties_using_get) | **GET** /public/v1/features | getAllFeatureProperties
[**get_cp_cloud_using_get**](PublicApIsApi.md#get_cp_cloud_using_get) | **GET** /public/v1/cp-cloud | getCPCloud
[**get_feature_property_using_get**](PublicApIsApi.md#get_feature_property_using_get) | **GET** /public/v1/features/{name} | getFeatureProperty
[**get_login_options_using_get**](PublicApIsApi.md#get_login_options_using_get) | **GET** /public/v1/loginOptions | getLoginOptions
[**get_logo_using_get**](PublicApIsApi.md#get_logo_using_get) | **GET** /public/v1/logo | getLogo
[**health_check_using_get**](PublicApIsApi.md#health_check_using_get) | **GET** /public/v1/health | healthCheck
[**link_aws_account_using_post**](PublicApIsApi.md#link_aws_account_using_post) | **POST** /public/v1/link-aws | linkAwsAccount
[**link_azure_account_using_post**](PublicApIsApi.md#link_azure_account_using_post) | **POST** /public/v1/link-azure | linkAzureAccount
[**link_bitbucket_account_using_post**](PublicApIsApi.md#link_bitbucket_account_using_post) | **POST** /public/v1/link-bitbucket | linkBitbucketAccount
[**link_docker_registries_using_post**](PublicApIsApi.md#link_docker_registries_using_post) | **POST** /public/v1/link-docker-registries | linkDockerRegistries
[**link_ecr_using_post**](PublicApIsApi.md#link_ecr_using_post) | **POST** /public/v1/link-ecr | linkECR
[**link_gcp_account_using_post**](PublicApIsApi.md#link_gcp_account_using_post) | **POST** /public/v1/link-gcp | linkGcpAccount
[**link_github_account_using_post**](PublicApIsApi.md#link_github_account_using_post) | **POST** /public/v1/link-github | linkGithubAccount
[**link_gitlab_account_using_post**](PublicApIsApi.md#link_gitlab_account_using_post) | **POST** /public/v1/link-gitlab | linkGitlabAccount
[**link_k8s_account_using_post**](PublicApIsApi.md#link_k8s_account_using_post) | **POST** /public/v1/link-kubernetes | linkK8sAccount
[**process_github_installation_request_using_post**](PublicApIsApi.md#process_github_installation_request_using_post) | **POST** /public/v1/github-installation-request | processGithubInstallationRequest
[**retrieve_theme_file_using_get**](PublicApIsApi.md#retrieve_theme_file_using_get) | **GET** /public/v1/themeFile | retrieveThemeFile


# **get_all_feature_properties_using_get**
> dict(str, str) get_all_feature_properties_using_get()

getAllFeatureProperties

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))

try:
    # getAllFeatureProperties
    api_response = api_instance.get_all_feature_properties_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->get_all_feature_properties_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, str)**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cp_cloud_using_get**
> str get_cp_cloud_using_get()

getCPCloud

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))

try:
    # getCPCloud
    api_response = api_instance.get_cp_cloud_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->get_cp_cloud_using_get: %s\n" % e)
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

# **get_feature_property_using_get**
> dict(str, str) get_feature_property_using_get(name)

getFeatureProperty

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | name

try:
    # getFeatureProperty
    api_response = api_instance.get_feature_property_using_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->get_feature_property_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 

### Return type

**dict(str, str)**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_options_using_get**
> list[CustomOAuth2ClientRegistration] get_login_options_using_get()

getLoginOptions

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))

try:
    # getLoginOptions
    api_response = api_instance.get_login_options_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->get_login_options_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustomOAuth2ClientRegistration]**](CustomOAuth2ClientRegistration.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logo_using_get**
> str get_logo_using_get()

getLogo

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))

try:
    # getLogo
    api_response = api_instance.get_logo_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->get_logo_using_get: %s\n" % e)
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

# **health_check_using_get**
> dict(str, object) health_check_using_get()

healthCheck

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))

try:
    # healthCheck
    api_response = api_instance.health_check_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->health_check_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, object)**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_aws_account_using_post**
> link_aws_account_using_post(payload)

linkAwsAccount

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
payload = swagger_client.OneTimePayloadAwsAccount() # OneTimePayloadAwsAccount | payload

try:
    # linkAwsAccount
    api_instance.link_aws_account_using_post(payload)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_aws_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**OneTimePayloadAwsAccount**](OneTimePayloadAwsAccount.md)| payload | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_azure_account_using_post**
> link_azure_account_using_post(payload)

linkAzureAccount

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
payload = swagger_client.OneTimePayloadAzureAccount() # OneTimePayloadAzureAccount | payload

try:
    # linkAzureAccount
    api_instance.link_azure_account_using_post(payload)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_azure_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**OneTimePayloadAzureAccount**](OneTimePayloadAzureAccount.md)| payload | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_bitbucket_account_using_post**
> link_bitbucket_account_using_post(payload)

linkBitbucketAccount

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
payload = swagger_client.OneTimePayloadBitbucketOauthAppPayload() # OneTimePayloadBitbucketOauthAppPayload | payload

try:
    # linkBitbucketAccount
    api_instance.link_bitbucket_account_using_post(payload)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_bitbucket_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**OneTimePayloadBitbucketOauthAppPayload**](OneTimePayloadBitbucketOauthAppPayload.md)| payload | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_docker_registries_using_post**
> link_docker_registries_using_post(payload)

linkDockerRegistries

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
payload = swagger_client.OneTimePayloadBasicDockerDTO() # OneTimePayloadBasicDockerDTO | payload

try:
    # linkDockerRegistries
    api_instance.link_docker_registries_using_post(payload)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_docker_registries_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**OneTimePayloadBasicDockerDTO**](OneTimePayloadBasicDockerDTO.md)| payload | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_ecr_using_post**
> link_ecr_using_post(payload)

linkECR

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
payload = swagger_client.OneTimePayloadECRArtifactory() # OneTimePayloadECRArtifactory | payload

try:
    # linkECR
    api_instance.link_ecr_using_post(payload)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_ecr_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**OneTimePayloadECRArtifactory**](OneTimePayloadECRArtifactory.md)| payload | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_gcp_account_using_post**
> link_gcp_account_using_post(payload)

linkGcpAccount

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
payload = swagger_client.OneTimePayloadGcpAccount() # OneTimePayloadGcpAccount | payload

try:
    # linkGcpAccount
    api_instance.link_gcp_account_using_post(payload)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_gcp_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**OneTimePayloadGcpAccount**](OneTimePayloadGcpAccount.md)| payload | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_github_account_using_post**
> link_github_account_using_post(payload)

linkGithubAccount

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
payload = swagger_client.OneTimePayloadGithubAppInstallationPayload() # OneTimePayloadGithubAppInstallationPayload | payload

try:
    # linkGithubAccount
    api_instance.link_github_account_using_post(payload)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_github_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**OneTimePayloadGithubAppInstallationPayload**](OneTimePayloadGithubAppInstallationPayload.md)| payload | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_gitlab_account_using_post**
> link_gitlab_account_using_post(payload)

linkGitlabAccount

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
payload = swagger_client.OneTimePayloadGitlabOauthAppPayload() # OneTimePayloadGitlabOauthAppPayload | payload

try:
    # linkGitlabAccount
    api_instance.link_gitlab_account_using_post(payload)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_gitlab_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**OneTimePayloadGitlabOauthAppPayload**](OneTimePayloadGitlabOauthAppPayload.md)| payload | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_k8s_account_using_post**
> link_k8s_account_using_post(payload)

linkK8sAccount

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
payload = swagger_client.OneTimePayloadKubernetesAccount() # OneTimePayloadKubernetesAccount | payload

try:
    # linkK8sAccount
    api_instance.link_k8s_account_using_post(payload)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_k8s_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**OneTimePayloadKubernetesAccount**](OneTimePayloadKubernetesAccount.md)| payload | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_github_installation_request_using_post**
> GithubAppInstallationRequestResponse process_github_installation_request_using_post(github_app_installation_request)

processGithubInstallationRequest

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
github_app_installation_request = swagger_client.GithubAppInstallationRequest() # GithubAppInstallationRequest | githubAppInstallationRequest

try:
    # processGithubInstallationRequest
    api_response = api_instance.process_github_installation_request_using_post(github_app_installation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->process_github_installation_request_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **github_app_installation_request** | [**GithubAppInstallationRequest**](GithubAppInstallationRequest.md)| githubAppInstallationRequest | 

### Return type

[**GithubAppInstallationRequestResponse**](GithubAppInstallationRequestResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_theme_file_using_get**
> ThemeFileResponse retrieve_theme_file_using_get()

retrieveThemeFile

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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))

try:
    # retrieveThemeFile
    api_response = api_instance.retrieve_theme_file_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->retrieve_theme_file_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ThemeFileResponse**](ThemeFileResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

