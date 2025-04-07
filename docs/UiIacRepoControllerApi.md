# swagger_client.UiIacRepoControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_iac_repo_using_post**](UiIacRepoControllerApi.md#create_iac_repo_using_post) | **POST** /cc-ui/v1/iac/repo | createIacRepo
[**delete_iac_repo_using_delete**](UiIacRepoControllerApi.md#delete_iac_repo_using_delete) | **DELETE** /cc-ui/v1/iac/repo/{id} | deleteIacRepo
[**get_all_iac_repos_using_get**](UiIacRepoControllerApi.md#get_all_iac_repos_using_get) | **GET** /cc-ui/v1/iac/repo | getAllIacRepos
[**get_iac_repo_by_id_using_get**](UiIacRepoControllerApi.md#get_iac_repo_by_id_using_get) | **GET** /cc-ui/v1/iac/repo/{id} | getIacRepoById
[**update_iac_repo_using_put**](UiIacRepoControllerApi.md#update_iac_repo_using_put) | **PUT** /cc-ui/v1/iac/repo/{id} | updateIacRepo


# **create_iac_repo_using_post**
> IacRepo create_iac_repo_using_post(iac_repo)

createIacRepo

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
api_instance = swagger_client.UiIacRepoControllerApi(swagger_client.ApiClient(configuration))
iac_repo = swagger_client.IacRepo() # IacRepo | iacRepo

try:
    # createIacRepo
    api_response = api_instance.create_iac_repo_using_post(iac_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiIacRepoControllerApi->create_iac_repo_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iac_repo** | [**IacRepo**](IacRepo.md)| iacRepo | 

### Return type

[**IacRepo**](IacRepo.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_iac_repo_using_delete**
> delete_iac_repo_using_delete(id)

deleteIacRepo

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
api_instance = swagger_client.UiIacRepoControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # deleteIacRepo
    api_instance.delete_iac_repo_using_delete(id)
except ApiException as e:
    print("Exception when calling UiIacRepoControllerApi->delete_iac_repo_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_iac_repos_using_get**
> list[IacRepo] get_all_iac_repos_using_get()

getAllIacRepos

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
api_instance = swagger_client.UiIacRepoControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllIacRepos
    api_response = api_instance.get_all_iac_repos_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiIacRepoControllerApi->get_all_iac_repos_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[IacRepo]**](IacRepo.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_iac_repo_by_id_using_get**
> IacRepo get_iac_repo_by_id_using_get(id)

getIacRepoById

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
api_instance = swagger_client.UiIacRepoControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id

try:
    # getIacRepoById
    api_response = api_instance.get_iac_repo_by_id_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiIacRepoControllerApi->get_iac_repo_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**IacRepo**](IacRepo.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_iac_repo_using_put**
> IacRepo update_iac_repo_using_put(id, updated_iac_repo)

updateIacRepo

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
api_instance = swagger_client.UiIacRepoControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | id
updated_iac_repo = swagger_client.IacRepo() # IacRepo | updatedIacRepo

try:
    # updateIacRepo
    api_response = api_instance.update_iac_repo_using_put(id, updated_iac_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiIacRepoControllerApi->update_iac_repo_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **updated_iac_repo** | [**IacRepo**](IacRepo.md)| updatedIacRepo | 

### Return type

[**IacRepo**](IacRepo.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

