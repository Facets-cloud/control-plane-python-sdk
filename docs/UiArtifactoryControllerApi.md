# swagger_client.UiArtifactoryControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associate_stacks_using_post**](UiArtifactoryControllerApi.md#associate_stacks_using_post) | **POST** /cc-ui/v1/artifactories/{artifactoryId}/associate-projects | associateStacks
[**create_artifactory_mirror_using_post**](UiArtifactoryControllerApi.md#create_artifactory_mirror_using_post) | **POST** /cc-ui/v1/artifactories/mirrors | createArtifactoryMirror
[**create_basic_docker_artifactory_using_post**](UiArtifactoryControllerApi.md#create_basic_docker_artifactory_using_post) | **POST** /cc-ui/v1/artifactories/others | createBasicDockerArtifactory
[**create_ecr_artifactory_using_post1**](UiArtifactoryControllerApi.md#create_ecr_artifactory_using_post1) | **POST** /cc-ui/v1/artifactories | createECRArtifactory
[**delete_artifactory_using_delete**](UiArtifactoryControllerApi.md#delete_artifactory_using_delete) | **DELETE** /cc-ui/v1/artifactories/v2/{artifactoryId} | deleteArtifactory
[**delete_ecr_artifactory_using_delete**](UiArtifactoryControllerApi.md#delete_ecr_artifactory_using_delete) | **DELETE** /cc-ui/v1/artifactories/{artifactoryId} | deleteECRArtifactory
[**get_all_artifactories_for_stack_using_get**](UiArtifactoryControllerApi.md#get_all_artifactories_for_stack_using_get) | **GET** /cc-ui/v1/artifactories/stack/{stackName} | getAllArtifactoriesForStack
[**get_all_artifactories_using_get1**](UiArtifactoryControllerApi.md#get_all_artifactories_using_get1) | **GET** /cc-ui/v1/artifactories | getAllArtifactories
[**get_artifactory_by_id_using_get**](UiArtifactoryControllerApi.md#get_artifactory_by_id_using_get) | **GET** /cc-ui/v1/artifactories/{artifactoryId} | getArtifactoryById
[**get_artifactory_by_name_using_get**](UiArtifactoryControllerApi.md#get_artifactory_by_name_using_get) | **GET** /cc-ui/v1/artifactories/name/{name} | getArtifactoryByName
[**get_repositories_by_artifactory_name_using_get**](UiArtifactoryControllerApi.md#get_repositories_by_artifactory_name_using_get) | **GET** /cc-ui/v1/artifactories/name/{name}/repos | getRepositoriesByArtifactoryName
[**get_repositories_using_get**](UiArtifactoryControllerApi.md#get_repositories_using_get) | **GET** /cc-ui/v1/artifactories/{artifactoryId}/repos | getRepositories
[**get_tags_by_artifactory_name_using_get**](UiArtifactoryControllerApi.md#get_tags_by_artifactory_name_using_get) | **GET** /cc-ui/v1/artifactories/name/{name}/tags | getTagsByArtifactoryName
[**get_tags_using_get**](UiArtifactoryControllerApi.md#get_tags_using_get) | **GET** /cc-ui/v1/artifactories/{artifactoryId}/tags | getTags
[**request_artifactory_linking_using_post**](UiArtifactoryControllerApi.md#request_artifactory_linking_using_post) | **POST** /cc-ui/v1/artifactories/link-container-registry | requestArtifactoryLinking
[**update_basic_docker_artifactory_using_post**](UiArtifactoryControllerApi.md#update_basic_docker_artifactory_using_post) | **POST** /cc-ui/v1/artifactories/others/{artifactoryId} | updateBasicDockerArtifactory
[**update_ecr_artifactory_using_post**](UiArtifactoryControllerApi.md#update_ecr_artifactory_using_post) | **POST** /cc-ui/v1/artifactories/{artifactoryId} | updateECRArtifactory

# **associate_stacks_using_post**
> associate_stacks_using_post(body, artifactory_id)

associateStacks

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | stacks
artifactory_id = 'artifactory_id_example' # str | artifactoryId

try:
    # associateStacks
    api_instance.associate_stacks_using_post(body, artifactory_id)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->associate_stacks_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| stacks | 
 **artifactory_id** | **str**| artifactoryId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_artifactory_mirror_using_post**
> ArtifactoryMirror create_artifactory_mirror_using_post(body)

createArtifactoryMirror

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactoryMirror() # ArtifactoryMirror | artifactoryMirror

try:
    # createArtifactoryMirror
    api_response = api_instance.create_artifactory_mirror_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->create_artifactory_mirror_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactoryMirror**](ArtifactoryMirror.md)| artifactoryMirror | 

### Return type

[**ArtifactoryMirror**](ArtifactoryMirror.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_basic_docker_artifactory_using_post**
> BasicDockerArtifactory create_basic_docker_artifactory_using_post(body)

createBasicDockerArtifactory

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.BasicDockerDTO() # BasicDockerDTO | basicDockerDTO

try:
    # createBasicDockerArtifactory
    api_response = api_instance.create_basic_docker_artifactory_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->create_basic_docker_artifactory_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BasicDockerDTO**](BasicDockerDTO.md)| basicDockerDTO | 

### Return type

[**BasicDockerArtifactory**](BasicDockerArtifactory.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ecr_artifactory_using_post1**
> ECRArtifactory create_ecr_artifactory_using_post1(body)

createECRArtifactory

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ECRArtifactory() # ECRArtifactory | ecrArtifactory

try:
    # createECRArtifactory
    api_response = api_instance.create_ecr_artifactory_using_post1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->create_ecr_artifactory_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ECRArtifactory**](ECRArtifactory.md)| ecrArtifactory | 

### Return type

[**ECRArtifactory**](ECRArtifactory.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifactory_using_delete**
> delete_artifactory_using_delete(artifactory_id)

deleteArtifactory

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
artifactory_id = 'artifactory_id_example' # str | artifactoryId

try:
    # deleteArtifactory
    api_instance.delete_artifactory_using_delete(artifactory_id)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->delete_artifactory_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactory_id** | **str**| artifactoryId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ecr_artifactory_using_delete**
> bool delete_ecr_artifactory_using_delete(artifactory_id)

deleteECRArtifactory

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
artifactory_id = 'artifactory_id_example' # str | artifactoryId

try:
    # deleteECRArtifactory
    api_response = api_instance.delete_ecr_artifactory_using_delete(artifactory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->delete_ecr_artifactory_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactory_id** | **str**| artifactoryId | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_artifactories_for_stack_using_get**
> list[Artifactory] get_all_artifactories_for_stack_using_get(stack_name)

getAllArtifactoriesForStack

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getAllArtifactoriesForStack
    api_response = api_instance.get_all_artifactories_for_stack_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_all_artifactories_for_stack_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**list[Artifactory]**](Artifactory.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_artifactories_using_get1**
> list[Artifactory] get_all_artifactories_using_get1()

getAllArtifactories

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllArtifactories
    api_response = api_instance.get_all_artifactories_using_get1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_all_artifactories_using_get1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Artifactory]**](Artifactory.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifactory_by_id_using_get**
> Artifactory get_artifactory_by_id_using_get(artifactory_id)

getArtifactoryById

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
artifactory_id = 'artifactory_id_example' # str | artifactoryId

try:
    # getArtifactoryById
    api_response = api_instance.get_artifactory_by_id_using_get(artifactory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_artifactory_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactory_id** | **str**| artifactoryId | 

### Return type

[**Artifactory**](Artifactory.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifactory_by_name_using_get**
> Artifactory get_artifactory_by_name_using_get(name)

getArtifactoryByName

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | name

try:
    # getArtifactoryByName
    api_response = api_instance.get_artifactory_by_name_using_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_artifactory_by_name_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 

### Return type

[**Artifactory**](Artifactory.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_artifactory_name_using_get**
> list[str] get_repositories_by_artifactory_name_using_get(name, artifact_type=artifact_type)

getRepositoriesByArtifactoryName

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | name
artifact_type = 'docker_image' # str | artifactType (optional) (default to docker_image)

try:
    # getRepositoriesByArtifactoryName
    api_response = api_instance.get_repositories_by_artifactory_name_using_get(name, artifact_type=artifact_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_repositories_by_artifactory_name_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 
 **artifact_type** | **str**| artifactType | [optional] [default to docker_image]

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_using_get**
> list[str] get_repositories_using_get(artifactory_id)

getRepositories

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
artifactory_id = 'artifactory_id_example' # str | artifactoryId

try:
    # getRepositories
    api_response = api_instance.get_repositories_using_get(artifactory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_repositories_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactory_id** | **str**| artifactoryId | 

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_by_artifactory_name_using_get**
> list[str] get_tags_by_artifactory_name_using_get(name, repo, artifact_type=artifact_type)

getTagsByArtifactoryName

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | name
repo = 'repo_example' # str | repo
artifact_type = 'docker_image' # str | artifactType (optional) (default to docker_image)

try:
    # getTagsByArtifactoryName
    api_response = api_instance.get_tags_by_artifactory_name_using_get(name, repo, artifact_type=artifact_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_tags_by_artifactory_name_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 
 **repo** | **str**| repo | 
 **artifact_type** | **str**| artifactType | [optional] [default to docker_image]

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_using_get**
> list[str] get_tags_using_get(artifactory_id, repo)

getTags

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
artifactory_id = 'artifactory_id_example' # str | artifactoryId
repo = 'repo_example' # str | repo

try:
    # getTags
    api_response = api_instance.get_tags_using_get(artifactory_id, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_tags_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactory_id** | **str**| artifactoryId | 
 **repo** | **str**| repo | 

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_artifactory_linking_using_post**
> OneTimeWebhook request_artifactory_linking_using_post(body)

requestArtifactoryLinking

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactoryLinkingRequest() # ArtifactoryLinkingRequest | artifactoryLinkingRequest

try:
    # requestArtifactoryLinking
    api_response = api_instance.request_artifactory_linking_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->request_artifactory_linking_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactoryLinkingRequest**](ArtifactoryLinkingRequest.md)| artifactoryLinkingRequest | 

### Return type

[**OneTimeWebhook**](OneTimeWebhook.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_basic_docker_artifactory_using_post**
> BasicDockerArtifactory update_basic_docker_artifactory_using_post(body, artifactory_id)

updateBasicDockerArtifactory

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.BasicDockerDTO() # BasicDockerDTO | basicDockerDTO
artifactory_id = 'artifactory_id_example' # str | artifactoryId

try:
    # updateBasicDockerArtifactory
    api_response = api_instance.update_basic_docker_artifactory_using_post(body, artifactory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->update_basic_docker_artifactory_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BasicDockerDTO**](BasicDockerDTO.md)| basicDockerDTO | 
 **artifactory_id** | **str**| artifactoryId | 

### Return type

[**BasicDockerArtifactory**](BasicDockerArtifactory.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ecr_artifactory_using_post**
> ECRArtifactory update_ecr_artifactory_using_post(body, artifactory_id)

updateECRArtifactory

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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ECRArtifactory() # ECRArtifactory | ecrArtifactory
artifactory_id = 'artifactory_id_example' # str | artifactoryId

try:
    # updateECRArtifactory
    api_response = api_instance.update_ecr_artifactory_using_post(body, artifactory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->update_ecr_artifactory_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ECRArtifactory**](ECRArtifactory.md)| ecrArtifactory | 
 **artifactory_id** | **str**| artifactoryId | 

### Return type

[**ECRArtifactory**](ECRArtifactory.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

