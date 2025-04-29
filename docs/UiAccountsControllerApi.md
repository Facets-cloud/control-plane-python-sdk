# swagger_client.UiAccountsControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aws_account_using_post**](UiAccountsControllerApi.md#create_aws_account_using_post) | **POST** /cc-ui/v1/accounts/aws/ | createAwsAccount
[**create_azure_account_using_post**](UiAccountsControllerApi.md#create_azure_account_using_post) | **POST** /cc-ui/v1/accounts/azure/ | createAzureAccount
[**create_bit_bucket_account_using_post**](UiAccountsControllerApi.md#create_bit_bucket_account_using_post) | **POST** /cc-ui/v1/accounts/bitbucket/ | createBitBucketAccount
[**create_coder_account_using_post**](UiAccountsControllerApi.md#create_coder_account_using_post) | **POST** /cc-ui/v1/accounts/coder/ | createCoderAccount
[**create_gcp_account_using_post**](UiAccountsControllerApi.md#create_gcp_account_using_post) | **POST** /cc-ui/v1/accounts/gcp/ | createGcpAccount
[**create_git_hub_account_using_post**](UiAccountsControllerApi.md#create_git_hub_account_using_post) | **POST** /cc-ui/v1/accounts/github/ | createGitHubAccount
[**create_git_lab_account_using_post**](UiAccountsControllerApi.md#create_git_lab_account_using_post) | **POST** /cc-ui/v1/accounts/gitlab/ | createGitLabAccount
[**create_kubernetes_account_using_post**](UiAccountsControllerApi.md#create_kubernetes_account_using_post) | **POST** /cc-ui/v1/accounts/kubernetes/ | createKubernetesAccount
[**delete_account_using_delete**](UiAccountsControllerApi.md#delete_account_using_delete) | **DELETE** /cc-ui/v1/accounts/{id} | deleteAccount
[**get_account_by_name_using_get**](UiAccountsControllerApi.md#get_account_by_name_using_get) | **GET** /cc-ui/v1/accounts/name/{name} | getAccountByName
[**get_account_using_get**](UiAccountsControllerApi.md#get_account_using_get) | **GET** /cc-ui/v1/accounts/{id} | getAccount
[**get_accounts_by_type_using_get**](UiAccountsControllerApi.md#get_accounts_by_type_using_get) | **GET** /cc-ui/v1/accounts/type/{type} | getAccountsByType
[**get_all_accounts_using_get**](UiAccountsControllerApi.md#get_all_accounts_using_get) | **GET** /cc-ui/v1/accounts/ | getAllAccounts
[**get_all_vcs_token_details_using_get**](UiAccountsControllerApi.md#get_all_vcs_token_details_using_get) | **GET** /cc-ui/v1/accounts/token-details | getAllVCSTokenDetails
[**get_bitbucket_projects_for_workspace_using_get**](UiAccountsControllerApi.md#get_bitbucket_projects_for_workspace_using_get) | **GET** /cc-ui/v1/accounts/{accountId}/workspaces/{workspace}/projects | getBitbucketProjectsForWorkspace
[**get_vcs_organisations_using_post**](UiAccountsControllerApi.md#get_vcs_organisations_using_post) | **POST** /cc-ui/v1/accounts/get-organisations | getVCSOrganisations
[**get_vcs_organizations_by_account_id_using_get**](UiAccountsControllerApi.md#get_vcs_organizations_by_account_id_using_get) | **GET** /cc-ui/v1/accounts/vcs-orgs/{accountId} | getVcsOrganizationsByAccountId
[**get_vcs_token_details_by_stack_name_using_get**](UiAccountsControllerApi.md#get_vcs_token_details_by_stack_name_using_get) | **GET** /cc-ui/v1/accounts/stack/{stackName}/token-details | getVCSTokenDetailsByStackName
[**refresh_all_vcs_token_details_using_post**](UiAccountsControllerApi.md#refresh_all_vcs_token_details_using_post) | **POST** /cc-ui/v1/accounts/token-details/refresh | refreshAllVCSTokenDetails
[**request_cloud_account_linking_using_post**](UiAccountsControllerApi.md#request_cloud_account_linking_using_post) | **POST** /cc-ui/v1/accounts/link-cloud | requestCloudAccountLinking
[**request_vcs_linking_using_post**](UiAccountsControllerApi.md#request_vcs_linking_using_post) | **POST** /cc-ui/v1/accounts/link-vcs | requestVCSLinking
[**update_aws_account_using_put**](UiAccountsControllerApi.md#update_aws_account_using_put) | **PUT** /cc-ui/v1/accounts/aws/{id} | updateAwsAccount
[**update_azure_account_using_put**](UiAccountsControllerApi.md#update_azure_account_using_put) | **PUT** /cc-ui/v1/accounts/azure/{id} | updateAzureAccount
[**update_bit_bucket_account_using_put**](UiAccountsControllerApi.md#update_bit_bucket_account_using_put) | **PUT** /cc-ui/v1/accounts/bitbucket/{id} | updateBitBucketAccount
[**update_coder_account_using_put**](UiAccountsControllerApi.md#update_coder_account_using_put) | **PUT** /cc-ui/v1/accounts/coder/{id} | updateCoderAccount
[**update_gcp_account_using_put**](UiAccountsControllerApi.md#update_gcp_account_using_put) | **PUT** /cc-ui/v1/accounts/gcp/{id} | updateGcpAccount
[**update_git_hub_account_using_put**](UiAccountsControllerApi.md#update_git_hub_account_using_put) | **PUT** /cc-ui/v1/accounts/github/{id} | updateGitHubAccount
[**update_git_lab_account_using_put**](UiAccountsControllerApi.md#update_git_lab_account_using_put) | **PUT** /cc-ui/v1/accounts/gitlab/{id} | updateGitLabAccount
[**update_kubernetes_account_using_put**](UiAccountsControllerApi.md#update_kubernetes_account_using_put) | **PUT** /cc-ui/v1/accounts/kubernetes/{id} | updateKubernetesAccount
[**update_vcs_account_using_patch**](UiAccountsControllerApi.md#update_vcs_account_using_patch) | **PATCH** /cc-ui/v1/accounts/vcs/{id} | updateVCSAccount
[**validate_aws_account_using_post**](UiAccountsControllerApi.md#validate_aws_account_using_post) | **POST** /cc-ui/v1/accounts/aws/validate | validateAwsAccount
[**validate_azure_account_using_post**](UiAccountsControllerApi.md#validate_azure_account_using_post) | **POST** /cc-ui/v1/accounts/azure/validate | validateAzureAccount
[**validate_bitbucket_account_using_post**](UiAccountsControllerApi.md#validate_bitbucket_account_using_post) | **POST** /cc-ui/v1/accounts/bitbucket/validate | validateBitbucketAccount
[**validate_gcp_account_using_post**](UiAccountsControllerApi.md#validate_gcp_account_using_post) | **POST** /cc-ui/v1/accounts/gcp/validate | validateGcpAccount
[**validate_github_account_using_post**](UiAccountsControllerApi.md#validate_github_account_using_post) | **POST** /cc-ui/v1/accounts/github/validate | validateGithubAccount
[**validate_gitlab_account_using_post**](UiAccountsControllerApi.md#validate_gitlab_account_using_post) | **POST** /cc-ui/v1/accounts/gitlab/validate | validateGitlabAccount
[**validate_kubernetes_account_using_post**](UiAccountsControllerApi.md#validate_kubernetes_account_using_post) | **POST** /cc-ui/v1/accounts/kubernetes/validate | validateKubernetesAccount

# **create_aws_account_using_post**
> AwsAccount create_aws_account_using_post(body)

createAwsAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AwsAccount() # AwsAccount | awsAccountRequest

try:
    # createAwsAccount
    api_response = api_instance.create_aws_account_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_aws_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AwsAccount**](AwsAccount.md)| awsAccountRequest | 

### Return type

[**AwsAccount**](AwsAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_azure_account_using_post**
> AzureAccount create_azure_account_using_post(body)

createAzureAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AzureAccount() # AzureAccount | azureAccountRequest

try:
    # createAzureAccount
    api_response = api_instance.create_azure_account_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_azure_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AzureAccount**](AzureAccount.md)| azureAccountRequest | 

### Return type

[**AzureAccount**](AzureAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bit_bucket_account_using_post**
> BitBucketAccount create_bit_bucket_account_using_post(body)

createBitBucketAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.BitBucketAccount() # BitBucketAccount | bitbucketAccountRequest

try:
    # createBitBucketAccount
    api_response = api_instance.create_bit_bucket_account_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_bit_bucket_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BitBucketAccount**](BitBucketAccount.md)| bitbucketAccountRequest | 

### Return type

[**BitBucketAccount**](BitBucketAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coder_account_using_post**
> CoderAccount create_coder_account_using_post(body)

createCoderAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CoderAccount() # CoderAccount | coderAccountRequest

try:
    # createCoderAccount
    api_response = api_instance.create_coder_account_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_coder_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CoderAccount**](CoderAccount.md)| coderAccountRequest | 

### Return type

[**CoderAccount**](CoderAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_gcp_account_using_post**
> GcpAccount create_gcp_account_using_post(body)

createGcpAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.GcpAccount() # GcpAccount | gcpAccountRequest

try:
    # createGcpAccount
    api_response = api_instance.create_gcp_account_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_gcp_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GcpAccount**](GcpAccount.md)| gcpAccountRequest | 

### Return type

[**GcpAccount**](GcpAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_git_hub_account_using_post**
> GitHubAccount create_git_hub_account_using_post(body)

createGitHubAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.GitHubAccount() # GitHubAccount | githubAccountRequest

try:
    # createGitHubAccount
    api_response = api_instance.create_git_hub_account_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_git_hub_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GitHubAccount**](GitHubAccount.md)| githubAccountRequest | 

### Return type

[**GitHubAccount**](GitHubAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_git_lab_account_using_post**
> GitLabAccount create_git_lab_account_using_post(body)

createGitLabAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.GitLabAccount() # GitLabAccount | gitlabAccountRequest

try:
    # createGitLabAccount
    api_response = api_instance.create_git_lab_account_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_git_lab_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GitLabAccount**](GitLabAccount.md)| gitlabAccountRequest | 

### Return type

[**GitLabAccount**](GitLabAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_kubernetes_account_using_post**
> KubernetesAccount create_kubernetes_account_using_post(body)

createKubernetesAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.KubernetesAccount() # KubernetesAccount | k8sAccountRequest

try:
    # createKubernetesAccount
    api_response = api_instance.create_kubernetes_account_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->create_kubernetes_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KubernetesAccount**](KubernetesAccount.md)| k8sAccountRequest | 

### Return type

[**KubernetesAccount**](KubernetesAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account_using_delete**
> bool delete_account_using_delete(id)

deleteAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # deleteAccount
    api_response = api_instance.delete_account_using_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->delete_account_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_by_name_using_get**
> Account get_account_by_name_using_get(name)

getAccountByName

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | name

try:
    # getAccountByName
    api_response = api_instance.get_account_by_name_using_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_account_by_name_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 

### Return type

[**Account**](Account.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_using_get**
> Account get_account_using_get(id)

getAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # getAccount
    api_response = api_instance.get_account_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_account_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**Account**](Account.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_by_type_using_get**
> list[Account] get_accounts_by_type_using_get(type)

getAccountsByType

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | type

try:
    # getAccountsByType
    api_response = api_instance.get_accounts_by_type_using_get(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_accounts_by_type_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 

### Return type

[**list[Account]**](Account.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_accounts_using_get**
> list[Account] get_all_accounts_using_get()

getAllAccounts

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllAccounts
    api_response = api_instance.get_all_accounts_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_all_accounts_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Account]**](Account.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_vcs_token_details_using_get**
> list[VCSTokenDetailsResponse] get_all_vcs_token_details_using_get()

getAllVCSTokenDetails

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllVCSTokenDetails
    api_response = api_instance.get_all_vcs_token_details_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_all_vcs_token_details_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VCSTokenDetailsResponse]**](VCSTokenDetailsResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bitbucket_projects_for_workspace_using_get**
> list[str] get_bitbucket_projects_for_workspace_using_get(account_id, workspace)

getBitbucketProjectsForWorkspace

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | accountId
workspace = 'workspace_example' # str | workspace

try:
    # getBitbucketProjectsForWorkspace
    api_response = api_instance.get_bitbucket_projects_for_workspace_using_get(account_id, workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_bitbucket_projects_for_workspace_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | 
 **workspace** | **str**| workspace | 

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vcs_organisations_using_post**
> list[str] get_vcs_organisations_using_post(body)

getVCSOrganisations

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.VCSOrganizationsRequest() # VCSOrganizationsRequest | VCSOrganizationsRequest

try:
    # getVCSOrganisations
    api_response = api_instance.get_vcs_organisations_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_vcs_organisations_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VCSOrganizationsRequest**](VCSOrganizationsRequest.md)| VCSOrganizationsRequest | 

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vcs_organizations_by_account_id_using_get**
> list[str] get_vcs_organizations_by_account_id_using_get(account_id)

getVcsOrganizationsByAccountId

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | accountId

try:
    # getVcsOrganizationsByAccountId
    api_response = api_instance.get_vcs_organizations_by_account_id_using_get(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_vcs_organizations_by_account_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | 

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vcs_token_details_by_stack_name_using_get**
> VCSTokenDetailsResponse get_vcs_token_details_by_stack_name_using_get(stack_name)

getVCSTokenDetailsByStackName

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getVCSTokenDetailsByStackName
    api_response = api_instance.get_vcs_token_details_by_stack_name_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->get_vcs_token_details_by_stack_name_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**VCSTokenDetailsResponse**](VCSTokenDetailsResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_all_vcs_token_details_using_post**
> refresh_all_vcs_token_details_using_post()

refreshAllVCSTokenDetails

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))

try:
    # refreshAllVCSTokenDetails
    api_instance.refresh_all_vcs_token_details_using_post()
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->refresh_all_vcs_token_details_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_cloud_account_linking_using_post**
> OneTimeWebhook request_cloud_account_linking_using_post(body)

requestCloudAccountLinking

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CloudLinkingRequest() # CloudLinkingRequest | cloudLinkingRequest

try:
    # requestCloudAccountLinking
    api_response = api_instance.request_cloud_account_linking_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->request_cloud_account_linking_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CloudLinkingRequest**](CloudLinkingRequest.md)| cloudLinkingRequest | 

### Return type

[**OneTimeWebhook**](OneTimeWebhook.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_vcs_linking_using_post**
> VCSLinkingResponse request_vcs_linking_using_post(body)

requestVCSLinking

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.VCSLinkingRequest() # VCSLinkingRequest | vcsLinkingRequest

try:
    # requestVCSLinking
    api_response = api_instance.request_vcs_linking_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->request_vcs_linking_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VCSLinkingRequest**](VCSLinkingRequest.md)| vcsLinkingRequest | 

### Return type

[**VCSLinkingResponse**](VCSLinkingResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_aws_account_using_put**
> AwsAccount update_aws_account_using_put(body, id)

updateAwsAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AwsAccount() # AwsAccount | awsAccountRequest
id = 'id_example' # str | id

try:
    # updateAwsAccount
    api_response = api_instance.update_aws_account_using_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_aws_account_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AwsAccount**](AwsAccount.md)| awsAccountRequest | 
 **id** | **str**| id | 

### Return type

[**AwsAccount**](AwsAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_azure_account_using_put**
> AzureAccount update_azure_account_using_put(body, id)

updateAzureAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AzureAccount() # AzureAccount | azureAccountRequest
id = 'id_example' # str | id

try:
    # updateAzureAccount
    api_response = api_instance.update_azure_account_using_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_azure_account_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AzureAccount**](AzureAccount.md)| azureAccountRequest | 
 **id** | **str**| id | 

### Return type

[**AzureAccount**](AzureAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bit_bucket_account_using_put**
> BitBucketAccount update_bit_bucket_account_using_put(body, id)

updateBitBucketAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.BitBucketAccount() # BitBucketAccount | bitbucketAccountRequest
id = 'id_example' # str | id

try:
    # updateBitBucketAccount
    api_response = api_instance.update_bit_bucket_account_using_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_bit_bucket_account_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BitBucketAccount**](BitBucketAccount.md)| bitbucketAccountRequest | 
 **id** | **str**| id | 

### Return type

[**BitBucketAccount**](BitBucketAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coder_account_using_put**
> CoderAccount update_coder_account_using_put(body, id)

updateCoderAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CoderAccount() # CoderAccount | coderAccount
id = 'id_example' # str | id

try:
    # updateCoderAccount
    api_response = api_instance.update_coder_account_using_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_coder_account_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CoderAccount**](CoderAccount.md)| coderAccount | 
 **id** | **str**| id | 

### Return type

[**CoderAccount**](CoderAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gcp_account_using_put**
> GcpAccount update_gcp_account_using_put(body, id)

updateGcpAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.GcpAccount() # GcpAccount | gcpAccountRequest
id = 'id_example' # str | id

try:
    # updateGcpAccount
    api_response = api_instance.update_gcp_account_using_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_gcp_account_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GcpAccount**](GcpAccount.md)| gcpAccountRequest | 
 **id** | **str**| id | 

### Return type

[**GcpAccount**](GcpAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_git_hub_account_using_put**
> GitHubAccount update_git_hub_account_using_put(body, id)

updateGitHubAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.GitHubAccount() # GitHubAccount | githubAccountRequest
id = 'id_example' # str | id

try:
    # updateGitHubAccount
    api_response = api_instance.update_git_hub_account_using_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_git_hub_account_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GitHubAccount**](GitHubAccount.md)| githubAccountRequest | 
 **id** | **str**| id | 

### Return type

[**GitHubAccount**](GitHubAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_git_lab_account_using_put**
> GitLabAccount update_git_lab_account_using_put(body, id)

updateGitLabAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.GitLabAccount() # GitLabAccount | gitlabAccountRequest
id = 'id_example' # str | id

try:
    # updateGitLabAccount
    api_response = api_instance.update_git_lab_account_using_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_git_lab_account_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GitLabAccount**](GitLabAccount.md)| gitlabAccountRequest | 
 **id** | **str**| id | 

### Return type

[**GitLabAccount**](GitLabAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kubernetes_account_using_put**
> KubernetesAccount update_kubernetes_account_using_put(body, id)

updateKubernetesAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.KubernetesAccount() # KubernetesAccount | k8sAccountRequest
id = 'id_example' # str | id

try:
    # updateKubernetesAccount
    api_response = api_instance.update_kubernetes_account_using_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_kubernetes_account_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KubernetesAccount**](KubernetesAccount.md)| k8sAccountRequest | 
 **id** | **str**| id | 

### Return type

[**KubernetesAccount**](KubernetesAccount.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vcs_account_using_patch**
> update_vcs_account_using_patch(body, id)

updateVCSAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.VCSAccountUpdateRequest() # VCSAccountUpdateRequest | vcsAccountUpdateRequest
id = 'id_example' # str | id

try:
    # updateVCSAccount
    api_instance.update_vcs_account_using_patch(body, id)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->update_vcs_account_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VCSAccountUpdateRequest**](VCSAccountUpdateRequest.md)| vcsAccountUpdateRequest | 
 **id** | **str**| id | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_aws_account_using_post**
> Response validate_aws_account_using_post(body)

validateAwsAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AwsAccount() # AwsAccount | awsAccount

try:
    # validateAwsAccount
    api_response = api_instance.validate_aws_account_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->validate_aws_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AwsAccount**](AwsAccount.md)| awsAccount | 

### Return type

[**Response**](Response.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_azure_account_using_post**
> Response validate_azure_account_using_post(body)

validateAzureAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AzureAccount() # AzureAccount | azureAccount

try:
    # validateAzureAccount
    api_response = api_instance.validate_azure_account_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->validate_azure_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AzureAccount**](AzureAccount.md)| azureAccount | 

### Return type

[**Response**](Response.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_bitbucket_account_using_post**
> Response validate_bitbucket_account_using_post(body)

validateBitbucketAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.BitBucketAccount() # BitBucketAccount | bitBucketAccount

try:
    # validateBitbucketAccount
    api_response = api_instance.validate_bitbucket_account_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->validate_bitbucket_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BitBucketAccount**](BitBucketAccount.md)| bitBucketAccount | 

### Return type

[**Response**](Response.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_gcp_account_using_post**
> Response validate_gcp_account_using_post(body)

validateGcpAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.GcpAccount() # GcpAccount | gcpAccount

try:
    # validateGcpAccount
    api_response = api_instance.validate_gcp_account_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->validate_gcp_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GcpAccount**](GcpAccount.md)| gcpAccount | 

### Return type

[**Response**](Response.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_github_account_using_post**
> Response validate_github_account_using_post(body)

validateGithubAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.GitHubAccount() # GitHubAccount | gitHubAccount

try:
    # validateGithubAccount
    api_response = api_instance.validate_github_account_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->validate_github_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GitHubAccount**](GitHubAccount.md)| gitHubAccount | 

### Return type

[**Response**](Response.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_gitlab_account_using_post**
> Response validate_gitlab_account_using_post(body)

validateGitlabAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.GitLabAccount() # GitLabAccount | gitLabAccount

try:
    # validateGitlabAccount
    api_response = api_instance.validate_gitlab_account_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->validate_gitlab_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GitLabAccount**](GitLabAccount.md)| gitLabAccount | 

### Return type

[**Response**](Response.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_kubernetes_account_using_post**
> Response validate_kubernetes_account_using_post(body)

validateKubernetesAccount

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
api_instance = swagger_client.UiAccountsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.KubernetesAccount() # KubernetesAccount | kubernetesAccount

try:
    # validateKubernetesAccount
    api_response = api_instance.validate_kubernetes_account_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAccountsControllerApi->validate_kubernetes_account_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KubernetesAccount**](KubernetesAccount.md)| kubernetesAccount | 

### Return type

[**Response**](Response.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

