# swagger_client.UiAccountsControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aws_account**](UiAccountsControllerApi.md#create_aws_account) | **POST** /cc-ui/v1/accounts/aws/ | 
[**create_azure_account**](UiAccountsControllerApi.md#create_azure_account) | **POST** /cc-ui/v1/accounts/azure/ | 
[**create_bit_bucket_account**](UiAccountsControllerApi.md#create_bit_bucket_account) | **POST** /cc-ui/v1/accounts/bitbucket/ | 
[**create_coder_account**](UiAccountsControllerApi.md#create_coder_account) | **POST** /cc-ui/v1/accounts/coder/ | 
[**create_gcp_account**](UiAccountsControllerApi.md#create_gcp_account) | **POST** /cc-ui/v1/accounts/gcp/ | 
[**create_git_hub_account**](UiAccountsControllerApi.md#create_git_hub_account) | **POST** /cc-ui/v1/accounts/github/ | 
[**create_git_lab_account**](UiAccountsControllerApi.md#create_git_lab_account) | **POST** /cc-ui/v1/accounts/gitlab/ | 
[**create_kubernetes_account**](UiAccountsControllerApi.md#create_kubernetes_account) | **POST** /cc-ui/v1/accounts/kubernetes/ | 
[**delete_account**](UiAccountsControllerApi.md#delete_account) | **DELETE** /cc-ui/v1/accounts/{id} | 
[**get_account**](UiAccountsControllerApi.md#get_account) | **GET** /cc-ui/v1/accounts/{id} | 
[**get_account_by_name**](UiAccountsControllerApi.md#get_account_by_name) | **GET** /cc-ui/v1/accounts/name/{name} | 
[**get_accounts_by_type**](UiAccountsControllerApi.md#get_accounts_by_type) | **GET** /cc-ui/v1/accounts/type/{type} | 
[**get_all_accounts**](UiAccountsControllerApi.md#get_all_accounts) | **GET** /cc-ui/v1/accounts/ | 
[**get_all_vcs_token_details**](UiAccountsControllerApi.md#get_all_vcs_token_details) | **GET** /cc-ui/v1/accounts/token-details | 
[**get_bitbucket_projects_for_workspace**](UiAccountsControllerApi.md#get_bitbucket_projects_for_workspace) | **GET** /cc-ui/v1/accounts/{accountId}/workspaces/{workspace}/projects | 
[**get_vcs_organisations**](UiAccountsControllerApi.md#get_vcs_organisations) | **POST** /cc-ui/v1/accounts/get-organisations | 
[**get_vcs_organizations_by_account_id**](UiAccountsControllerApi.md#get_vcs_organizations_by_account_id) | **GET** /cc-ui/v1/accounts/vcs-orgs/{accountId} | 
[**get_vcs_token_details_by_stack_name**](UiAccountsControllerApi.md#get_vcs_token_details_by_stack_name) | **GET** /cc-ui/v1/accounts/stack/{stackName}/token-details | 
[**refresh_all_vcs_token_details**](UiAccountsControllerApi.md#refresh_all_vcs_token_details) | **POST** /cc-ui/v1/accounts/token-details/refresh | 
[**request_cloud_account_linking**](UiAccountsControllerApi.md#request_cloud_account_linking) | **POST** /cc-ui/v1/accounts/link-cloud | 
[**request_vcs_linking**](UiAccountsControllerApi.md#request_vcs_linking) | **POST** /cc-ui/v1/accounts/link-vcs | 
[**update_aws_account**](UiAccountsControllerApi.md#update_aws_account) | **PUT** /cc-ui/v1/accounts/aws/{id} | 
[**update_azure_account**](UiAccountsControllerApi.md#update_azure_account) | **PUT** /cc-ui/v1/accounts/azure/{id} | 
[**update_bit_bucket_account**](UiAccountsControllerApi.md#update_bit_bucket_account) | **PUT** /cc-ui/v1/accounts/bitbucket/{id} | 
[**update_coder_account**](UiAccountsControllerApi.md#update_coder_account) | **PUT** /cc-ui/v1/accounts/coder/{id} | 
[**update_gcp_account**](UiAccountsControllerApi.md#update_gcp_account) | **PUT** /cc-ui/v1/accounts/gcp/{id} | 
[**update_git_hub_account**](UiAccountsControllerApi.md#update_git_hub_account) | **PUT** /cc-ui/v1/accounts/github/{id} | 
[**update_git_lab_account**](UiAccountsControllerApi.md#update_git_lab_account) | **PUT** /cc-ui/v1/accounts/gitlab/{id} | 
[**update_kubernetes_account**](UiAccountsControllerApi.md#update_kubernetes_account) | **PUT** /cc-ui/v1/accounts/kubernetes/{id} | 
[**update_vcs_account**](UiAccountsControllerApi.md#update_vcs_account) | **PATCH** /cc-ui/v1/accounts/vcs/{id} | 
[**validate_aws_account**](UiAccountsControllerApi.md#validate_aws_account) | **POST** /cc-ui/v1/accounts/aws/validate | 
[**validate_azure_account**](UiAccountsControllerApi.md#validate_azure_account) | **POST** /cc-ui/v1/accounts/azure/validate | 
[**validate_bitbucket_account**](UiAccountsControllerApi.md#validate_bitbucket_account) | **POST** /cc-ui/v1/accounts/bitbucket/validate | 
[**validate_gcp_account**](UiAccountsControllerApi.md#validate_gcp_account) | **POST** /cc-ui/v1/accounts/gcp/validate | 
[**validate_github_account**](UiAccountsControllerApi.md#validate_github_account) | **POST** /cc-ui/v1/accounts/github/validate | 
[**validate_gitlab_account**](UiAccountsControllerApi.md#validate_gitlab_account) | **POST** /cc-ui/v1/accounts/gitlab/validate | 
[**validate_kubernetes_account**](UiAccountsControllerApi.md#validate_kubernetes_account) | **POST** /cc-ui/v1/accounts/kubernetes/validate | 

# **create_aws_account**
> ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount create_aws_account(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount() # ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount | 

try:
    api_response = api_instance.create_aws_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_aws_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount**](ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount.md)|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount**](ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_azure_account**
> ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount create_azure_account(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount() # ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount | 

try:
    api_response = api_instance.create_azure_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_azure_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount**](ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount.md)|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount**](ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bit_bucket_account**
> ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount create_bit_bucket_account(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount() # ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount | 

try:
    api_response = api_instance.create_bit_bucket_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_bit_bucket_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount**](ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount.md)|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount**](ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coder_account**
> ComCapillaryOpsCpBoAccountsCoderCoderAccount create_coder_account(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsCoderCoderAccount() # ComCapillaryOpsCpBoAccountsCoderCoderAccount | 

try:
    api_response = api_instance.create_coder_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_coder_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsCoderCoderAccount**](ComCapillaryOpsCpBoAccountsCoderCoderAccount.md)|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsCoderCoderAccount**](ComCapillaryOpsCpBoAccountsCoderCoderAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_gcp_account**
> ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount create_gcp_account(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount() # ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount | 

try:
    api_response = api_instance.create_gcp_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_gcp_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount**](ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount.md)|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount**](ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_git_hub_account**
> ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount create_git_hub_account(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount() # ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount | 

try:
    api_response = api_instance.create_git_hub_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_git_hub_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount**](ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount.md)|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount**](ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_git_lab_account**
> ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount create_git_lab_account(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount() # ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount | 

try:
    api_response = api_instance.create_git_lab_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_git_lab_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount**](ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount.md)|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount**](ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_kubernetes_account**
> ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount create_kubernetes_account(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount() # ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount | 

try:
    api_response = api_instance.create_kubernetes_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_kubernetes_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount**](ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount.md)|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount**](ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> bool delete_account(id)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.delete_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> ComCapillaryOpsCpBoAccountsAccount get_account(id)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsAccount**](ComCapillaryOpsCpBoAccountsAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_by_name**
> ComCapillaryOpsCpBoAccountsAccount get_account_by_name(name)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.get_account_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_account_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsAccount**](ComCapillaryOpsCpBoAccountsAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_by_type**
> list[ComCapillaryOpsCpBoAccountsAccount] get_accounts_by_type(type)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 

try:
    api_response = api_instance.get_accounts_by_type(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_accounts_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoAccountsAccount]**](ComCapillaryOpsCpBoAccountsAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_accounts**
> list[ComCapillaryOpsCpBoAccountsAccount] get_all_accounts()



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_all_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoAccountsAccount]**](ComCapillaryOpsCpBoAccountsAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vcs_token_details**
> list[ComCapillaryOpsCpBoAccountsVersioncontrolVCSTokenDetailsResponse] get_all_vcs_token_details()



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_vcs_token_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_all_vcs_token_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoAccountsVersioncontrolVCSTokenDetailsResponse]**](ComCapillaryOpsCpBoAccountsVersioncontrolVCSTokenDetailsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bitbucket_projects_for_workspace**
> list[str] get_bitbucket_projects_for_workspace(account_id, workspace)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | 
workspace = 'workspace_example' # str | 

try:
    api_response = api_instance.get_bitbucket_projects_for_workspace(account_id, workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_bitbucket_projects_for_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **workspace** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vcs_organisations**
> list[str] get_vcs_organisations(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsVersioncontrolVCSOrganizationsRequest() # ComCapillaryOpsCpBoAccountsVersioncontrolVCSOrganizationsRequest | 

try:
    api_response = api_instance.get_vcs_organisations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_vcs_organisations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsVersioncontrolVCSOrganizationsRequest**](ComCapillaryOpsCpBoAccountsVersioncontrolVCSOrganizationsRequest.md)|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vcs_organizations_by_account_id**
> list[str] get_vcs_organizations_by_account_id(account_id)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | 

try:
    api_response = api_instance.get_vcs_organizations_by_account_id(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_vcs_organizations_by_account_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vcs_token_details_by_stack_name**
> ComCapillaryOpsCpBoAccountsVersioncontrolVCSTokenDetailsResponse get_vcs_token_details_by_stack_name(stack_name)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_vcs_token_details_by_stack_name(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_vcs_token_details_by_stack_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsVersioncontrolVCSTokenDetailsResponse**](ComCapillaryOpsCpBoAccountsVersioncontrolVCSTokenDetailsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_all_vcs_token_details**
> refresh_all_vcs_token_details()



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))

try:
    api_instance.refresh_all_vcs_token_details()
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->refresh_all_vcs_token_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_cloud_account_linking**
> ComCapillaryOpsCpBoWebhookOneTimeWebhook request_cloud_account_linking(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsCloudCloudLinkingRequest() # ComCapillaryOpsCpBoAccountsCloudCloudLinkingRequest | 

try:
    api_response = api_instance.request_cloud_account_linking(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->request_cloud_account_linking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsCloudCloudLinkingRequest**](ComCapillaryOpsCpBoAccountsCloudCloudLinkingRequest.md)|  | 

### Return type

[**ComCapillaryOpsCpBoWebhookOneTimeWebhook**](ComCapillaryOpsCpBoWebhookOneTimeWebhook.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_vcs_linking**
> ComCapillaryOpsCpBoAccountsVersioncontrolVCSLinkingResponse request_vcs_linking(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsVersioncontrolVCSLinkingRequest() # ComCapillaryOpsCpBoAccountsVersioncontrolVCSLinkingRequest | 

try:
    api_response = api_instance.request_vcs_linking(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->request_vcs_linking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsVersioncontrolVCSLinkingRequest**](ComCapillaryOpsCpBoAccountsVersioncontrolVCSLinkingRequest.md)|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsVersioncontrolVCSLinkingResponse**](ComCapillaryOpsCpBoAccountsVersioncontrolVCSLinkingResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_aws_account**
> ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount update_aws_account(body, id)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount() # ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount | 
id = 'id_example' # str | 

try:
    api_response = api_instance.update_aws_account(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_aws_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount**](ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount.md)|  | 
 **id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount**](ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_azure_account**
> ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount update_azure_account(body, id)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount() # ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount | 
id = 'id_example' # str | 

try:
    api_response = api_instance.update_azure_account(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_azure_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount**](ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount.md)|  | 
 **id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount**](ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bit_bucket_account**
> ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount update_bit_bucket_account(body, id)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount() # ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount | 
id = 'id_example' # str | 

try:
    api_response = api_instance.update_bit_bucket_account(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_bit_bucket_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount**](ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount.md)|  | 
 **id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount**](ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coder_account**
> ComCapillaryOpsCpBoAccountsCoderCoderAccount update_coder_account(body, id)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsCoderCoderAccount() # ComCapillaryOpsCpBoAccountsCoderCoderAccount | 
id = 'id_example' # str | 

try:
    api_response = api_instance.update_coder_account(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_coder_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsCoderCoderAccount**](ComCapillaryOpsCpBoAccountsCoderCoderAccount.md)|  | 
 **id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsCoderCoderAccount**](ComCapillaryOpsCpBoAccountsCoderCoderAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gcp_account**
> ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount update_gcp_account(body, id)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount() # ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount | 
id = 'id_example' # str | 

try:
    api_response = api_instance.update_gcp_account(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_gcp_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount**](ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount.md)|  | 
 **id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount**](ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_git_hub_account**
> ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount update_git_hub_account(body, id)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount() # ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount | 
id = 'id_example' # str | 

try:
    api_response = api_instance.update_git_hub_account(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_git_hub_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount**](ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount.md)|  | 
 **id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount**](ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_git_lab_account**
> ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount update_git_lab_account(body, id)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount() # ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount | 
id = 'id_example' # str | 

try:
    api_response = api_instance.update_git_lab_account(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_git_lab_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount**](ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount.md)|  | 
 **id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount**](ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kubernetes_account**
> ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount update_kubernetes_account(body, id)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount() # ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount | 
id = 'id_example' # str | 

try:
    api_response = api_instance.update_kubernetes_account(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_kubernetes_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount**](ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount.md)|  | 
 **id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount**](ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vcs_account**
> update_vcs_account(body, id)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsVersioncontrolVCSAccountUpdateRequest() # ComCapillaryOpsCpBoAccountsVersioncontrolVCSAccountUpdateRequest | 
id = 'id_example' # str | 

try:
    api_instance.update_vcs_account(body, id)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_vcs_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsVersioncontrolVCSAccountUpdateRequest**](ComCapillaryOpsCpBoAccountsVersioncontrolVCSAccountUpdateRequest.md)|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_aws_account**
> ComCapillaryOpsCpBoResponse validate_aws_account(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount() # ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount | 

try:
    api_response = api_instance.validate_aws_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->validate_aws_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount**](ComCapillaryOpsCpBoAccountsCloudAwsAwsAccount.md)|  | 

### Return type

[**ComCapillaryOpsCpBoResponse**](ComCapillaryOpsCpBoResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_azure_account**
> ComCapillaryOpsCpBoResponse validate_azure_account(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount() # ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount | 

try:
    api_response = api_instance.validate_azure_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->validate_azure_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount**](ComCapillaryOpsCpBoAccountsCloudAzureAzureAccount.md)|  | 

### Return type

[**ComCapillaryOpsCpBoResponse**](ComCapillaryOpsCpBoResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_bitbucket_account**
> ComCapillaryOpsCpBoResponse validate_bitbucket_account(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount() # ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount | 

try:
    api_response = api_instance.validate_bitbucket_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->validate_bitbucket_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount**](ComCapillaryOpsCpBoAccountsVersioncontrolBitbucketBitBucketAccount.md)|  | 

### Return type

[**ComCapillaryOpsCpBoResponse**](ComCapillaryOpsCpBoResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_gcp_account**
> ComCapillaryOpsCpBoResponse validate_gcp_account(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount() # ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount | 

try:
    api_response = api_instance.validate_gcp_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->validate_gcp_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount**](ComCapillaryOpsCpBoAccountsCloudGcpGcpAccount.md)|  | 

### Return type

[**ComCapillaryOpsCpBoResponse**](ComCapillaryOpsCpBoResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_github_account**
> ComCapillaryOpsCpBoResponse validate_github_account(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount() # ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount | 

try:
    api_response = api_instance.validate_github_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->validate_github_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount**](ComCapillaryOpsCpBoAccountsVersioncontrolGithubGitHubAccount.md)|  | 

### Return type

[**ComCapillaryOpsCpBoResponse**](ComCapillaryOpsCpBoResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_gitlab_account**
> ComCapillaryOpsCpBoResponse validate_gitlab_account(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount() # ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount | 

try:
    api_response = api_instance.validate_gitlab_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->validate_gitlab_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount**](ComCapillaryOpsCpBoAccountsVersioncontrolGitlabGitLabAccount.md)|  | 

### Return type

[**ComCapillaryOpsCpBoResponse**](ComCapillaryOpsCpBoResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_kubernetes_account**
> ComCapillaryOpsCpBoResponse validate_kubernetes_account(body)



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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount() # ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount | 

try:
    api_response = api_instance.validate_kubernetes_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->validate_kubernetes_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount**](ComCapillaryOpsCpBoAccountsCloudKubernetesKubernetesAccount.md)|  | 

### Return type

[**ComCapillaryOpsCpBoResponse**](ComCapillaryOpsCpBoResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

