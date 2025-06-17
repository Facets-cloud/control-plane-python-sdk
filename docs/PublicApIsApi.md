# swagger_client.PublicApIsApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_feature_properties**](PublicApIsApi.md#get_all_feature_properties) | **GET** /public/v1/features | 
[**get_cp_cloud**](PublicApIsApi.md#get_cp_cloud) | **GET** /public/v1/cp-cloud | 
[**get_feature_property**](PublicApIsApi.md#get_feature_property) | **GET** /public/v1/features/{name} | 
[**get_login_options**](PublicApIsApi.md#get_login_options) | **GET** /public/v1/loginOptions | 
[**get_logo**](PublicApIsApi.md#get_logo) | **GET** /public/v1/logo | 
[**health_check**](PublicApIsApi.md#health_check) | **GET** /public/v1/health | 
[**link_aws_account**](PublicApIsApi.md#link_aws_account) | **POST** /public/v1/link-aws | 
[**link_azure_account**](PublicApIsApi.md#link_azure_account) | **POST** /public/v1/link-azure | 
[**link_bitbucket_account**](PublicApIsApi.md#link_bitbucket_account) | **POST** /public/v1/link-bitbucket | 
[**link_docker_registries**](PublicApIsApi.md#link_docker_registries) | **POST** /public/v1/link-docker-registries | 
[**link_ecr**](PublicApIsApi.md#link_ecr) | **POST** /public/v1/link-ecr | 
[**link_gcp_account**](PublicApIsApi.md#link_gcp_account) | **POST** /public/v1/link-gcp | 
[**link_github_account**](PublicApIsApi.md#link_github_account) | **POST** /public/v1/link-github | 
[**link_gitlab_account**](PublicApIsApi.md#link_gitlab_account) | **POST** /public/v1/link-gitlab | 
[**link_k8s_account**](PublicApIsApi.md#link_k8s_account) | **POST** /public/v1/link-kubernetes | 
[**process_github_installation_request**](PublicApIsApi.md#process_github_installation_request) | **POST** /public/v1/github-installation-request | 
[**retrieve_theme_file**](PublicApIsApi.md#retrieve_theme_file) | **GET** /public/v1/themeFile | 

# **get_all_feature_properties**
> dict(str, str) get_all_feature_properties()



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_feature_properties()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->get_all_feature_properties: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, str)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cp_cloud**
> str get_cp_cloud()



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_cp_cloud()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->get_cp_cloud: %s\n" % e)
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

# **get_feature_property**
> dict(str, str) get_feature_property(name)



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.get_feature_property(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->get_feature_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

**dict(str, str)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_options**
> list[CustomOAuth2ClientRegistration] get_login_options()



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_login_options()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->get_login_options: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustomOAuth2ClientRegistration]**](CustomOAuth2ClientRegistration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logo**
> str get_logo()



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_logo()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->get_logo: %s\n" % e)
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

# **health_check**
> dict(str, object) health_check()



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.health_check()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->health_check: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, object)**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_aws_account**
> link_aws_account(body)



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OneTimePayloadAwsAccount() # OneTimePayloadAwsAccount | 

try:
    api_instance.link_aws_account(body)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_aws_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OneTimePayloadAwsAccount**](OneTimePayloadAwsAccount.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_azure_account**
> link_azure_account(body)



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OneTimePayloadAzureAccount() # OneTimePayloadAzureAccount | 

try:
    api_instance.link_azure_account(body)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_azure_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OneTimePayloadAzureAccount**](OneTimePayloadAzureAccount.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_bitbucket_account**
> link_bitbucket_account(body)



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OneTimePayloadBitbucketOauthAppPayload() # OneTimePayloadBitbucketOauthAppPayload | 

try:
    api_instance.link_bitbucket_account(body)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_bitbucket_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OneTimePayloadBitbucketOauthAppPayload**](OneTimePayloadBitbucketOauthAppPayload.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_docker_registries**
> link_docker_registries(body)



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OneTimePayloadBasicDockerDTO() # OneTimePayloadBasicDockerDTO | 

try:
    api_instance.link_docker_registries(body)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_docker_registries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OneTimePayloadBasicDockerDTO**](OneTimePayloadBasicDockerDTO.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_ecr**
> link_ecr(body)



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OneTimePayloadECRArtifactory() # OneTimePayloadECRArtifactory | 

try:
    api_instance.link_ecr(body)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_ecr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OneTimePayloadECRArtifactory**](OneTimePayloadECRArtifactory.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_gcp_account**
> link_gcp_account(body)



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OneTimePayloadGcpAccount() # OneTimePayloadGcpAccount | 

try:
    api_instance.link_gcp_account(body)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_gcp_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OneTimePayloadGcpAccount**](OneTimePayloadGcpAccount.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_github_account**
> link_github_account(body)



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OneTimePayloadGithubAppInstallationPayload() # OneTimePayloadGithubAppInstallationPayload | 

try:
    api_instance.link_github_account(body)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_github_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OneTimePayloadGithubAppInstallationPayload**](OneTimePayloadGithubAppInstallationPayload.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_gitlab_account**
> link_gitlab_account(body)



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OneTimePayloadGitlabOauthAppPayload() # OneTimePayloadGitlabOauthAppPayload | 

try:
    api_instance.link_gitlab_account(body)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_gitlab_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OneTimePayloadGitlabOauthAppPayload**](OneTimePayloadGitlabOauthAppPayload.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_k8s_account**
> link_k8s_account(body)



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
body = swagger_client.OneTimePayloadKubernetesAccount() # OneTimePayloadKubernetesAccount | 

try:
    api_instance.link_k8s_account(body)
except ApiException as e:
    print("Exception when calling PublicApIsApi->link_k8s_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OneTimePayloadKubernetesAccount**](OneTimePayloadKubernetesAccount.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_github_installation_request**
> GithubAppInstallationRequestResponse process_github_installation_request(body)



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GithubAppInstallationRequest() # GithubAppInstallationRequest | 

try:
    api_response = api_instance.process_github_installation_request(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->process_github_installation_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GithubAppInstallationRequest**](GithubAppInstallationRequest.md)|  | 

### Return type

[**GithubAppInstallationRequestResponse**](GithubAppInstallationRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_theme_file**
> ThemeFileResponse retrieve_theme_file()



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
api_instance = swagger_client.PublicApIsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.retrieve_theme_file()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApIsApi->retrieve_theme_file: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ThemeFileResponse**](ThemeFileResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

