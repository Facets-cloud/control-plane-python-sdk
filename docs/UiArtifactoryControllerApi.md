# swagger_client.UiArtifactoryControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associate_stacks**](UiArtifactoryControllerApi.md#associate_stacks) | **POST** /cc-ui/v1/artifactories/{artifactoryId}/associate-projects | 
[**create_artifactory_mirror**](UiArtifactoryControllerApi.md#create_artifactory_mirror) | **POST** /cc-ui/v1/artifactories/mirrors | 
[**create_basic_docker_artifactory**](UiArtifactoryControllerApi.md#create_basic_docker_artifactory) | **POST** /cc-ui/v1/artifactories/others | 
[**create_ecr_artifactory1**](UiArtifactoryControllerApi.md#create_ecr_artifactory1) | **POST** /cc-ui/v1/artifactories | 
[**delete_artifactory**](UiArtifactoryControllerApi.md#delete_artifactory) | **DELETE** /cc-ui/v1/artifactories/v2/{artifactoryId} | 
[**delete_ecr_artifactory**](UiArtifactoryControllerApi.md#delete_ecr_artifactory) | **DELETE** /cc-ui/v1/artifactories/{artifactoryId} | 
[**get_all_artifactories1**](UiArtifactoryControllerApi.md#get_all_artifactories1) | **GET** /cc-ui/v1/artifactories | 
[**get_all_artifactories_for_stack**](UiArtifactoryControllerApi.md#get_all_artifactories_for_stack) | **GET** /cc-ui/v1/artifactories/stack/{stackName} | 
[**get_artifactory_by_id**](UiArtifactoryControllerApi.md#get_artifactory_by_id) | **GET** /cc-ui/v1/artifactories/{artifactoryId} | 
[**get_artifactory_by_name**](UiArtifactoryControllerApi.md#get_artifactory_by_name) | **GET** /cc-ui/v1/artifactories/name/{name} | 
[**get_repositories**](UiArtifactoryControllerApi.md#get_repositories) | **GET** /cc-ui/v1/artifactories/{artifactoryId}/repos | 
[**get_repositories_by_artifactory_name**](UiArtifactoryControllerApi.md#get_repositories_by_artifactory_name) | **GET** /cc-ui/v1/artifactories/name/{name}/repos | 
[**get_tags**](UiArtifactoryControllerApi.md#get_tags) | **GET** /cc-ui/v1/artifactories/{artifactoryId}/tags | 
[**get_tags_by_artifactory_name**](UiArtifactoryControllerApi.md#get_tags_by_artifactory_name) | **GET** /cc-ui/v1/artifactories/name/{name}/tags | 
[**request_artifactory_linking**](UiArtifactoryControllerApi.md#request_artifactory_linking) | **POST** /cc-ui/v1/artifactories/link-container-registry | 
[**update_basic_docker_artifactory**](UiArtifactoryControllerApi.md#update_basic_docker_artifactory) | **POST** /cc-ui/v1/artifactories/others/{artifactoryId} | 
[**update_ecr_artifactory1**](UiArtifactoryControllerApi.md#update_ecr_artifactory1) | **POST** /cc-ui/v1/artifactories/{artifactoryId} | 

# **associate_stacks**
> associate_stacks(body, artifactory_id)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | 
artifactory_id = 'artifactory_id_example' # str | 

try:
    api_instance.associate_stacks(body, artifactory_id)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->associate_stacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **artifactory_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_artifactory_mirror**
> ComCapillaryOpsCpBoArtifactoryMirror create_artifactory_mirror(body)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoArtifactoryMirror() # ComCapillaryOpsCpBoArtifactoryMirror | 

try:
    api_response = api_instance.create_artifactory_mirror(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->create_artifactory_mirror: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoArtifactoryMirror**](ComCapillaryOpsCpBoArtifactoryMirror.md)|  | 

### Return type

[**ComCapillaryOpsCpBoArtifactoryMirror**](ComCapillaryOpsCpBoArtifactoryMirror.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_basic_docker_artifactory**
> ComCapillaryOpsCpBoArtifactoryBasicDockerArtifactory create_basic_docker_artifactory(body)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoArtifactoryDtoBasicDockerDTO() # ComCapillaryOpsCpBoArtifactoryDtoBasicDockerDTO | 

try:
    api_response = api_instance.create_basic_docker_artifactory(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->create_basic_docker_artifactory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoArtifactoryDtoBasicDockerDTO**](ComCapillaryOpsCpBoArtifactoryDtoBasicDockerDTO.md)|  | 

### Return type

[**ComCapillaryOpsCpBoArtifactoryBasicDockerArtifactory**](ComCapillaryOpsCpBoArtifactoryBasicDockerArtifactory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ecr_artifactory1**
> ComCapillaryOpsCpBoECRArtifactory create_ecr_artifactory1(body)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoECRArtifactory() # ComCapillaryOpsCpBoECRArtifactory | 

try:
    api_response = api_instance.create_ecr_artifactory1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->create_ecr_artifactory1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoECRArtifactory**](ComCapillaryOpsCpBoECRArtifactory.md)|  | 

### Return type

[**ComCapillaryOpsCpBoECRArtifactory**](ComCapillaryOpsCpBoECRArtifactory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifactory**
> delete_artifactory(artifactory_id)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
artifactory_id = 'artifactory_id_example' # str | 

try:
    api_instance.delete_artifactory(artifactory_id)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->delete_artifactory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactory_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ecr_artifactory**
> bool delete_ecr_artifactory(artifactory_id)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
artifactory_id = 'artifactory_id_example' # str | 

try:
    api_response = api_instance.delete_ecr_artifactory(artifactory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->delete_ecr_artifactory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactory_id** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_artifactories1**
> list[ComCapillaryOpsCpBoArtifactory] get_all_artifactories1()



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_artifactories1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_all_artifactories1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoArtifactory]**](ComCapillaryOpsCpBoArtifactory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_artifactories_for_stack**
> list[ComCapillaryOpsCpBoArtifactory] get_all_artifactories_for_stack(stack_name)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_all_artifactories_for_stack(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_all_artifactories_for_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoArtifactory]**](ComCapillaryOpsCpBoArtifactory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifactory_by_id**
> ComCapillaryOpsCpBoArtifactory get_artifactory_by_id(artifactory_id)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
artifactory_id = 'artifactory_id_example' # str | 

try:
    api_response = api_instance.get_artifactory_by_id(artifactory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_artifactory_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactory_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoArtifactory**](ComCapillaryOpsCpBoArtifactory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifactory_by_name**
> ComCapillaryOpsCpBoArtifactory get_artifactory_by_name(name)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    api_response = api_instance.get_artifactory_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_artifactory_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoArtifactory**](ComCapillaryOpsCpBoArtifactory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories**
> list[str] get_repositories(artifactory_id)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
artifactory_id = 'artifactory_id_example' # str | 

try:
    api_response = api_instance.get_repositories(artifactory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactory_id** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repositories_by_artifactory_name**
> list[str] get_repositories_by_artifactory_name(name, artifact_type=artifact_type)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
artifact_type = 'docker_image' # str |  (optional) (default to docker_image)

try:
    api_response = api_instance.get_repositories_by_artifactory_name(name, artifact_type=artifact_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_repositories_by_artifactory_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **artifact_type** | **str**|  | [optional] [default to docker_image]

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags**
> list[str] get_tags(artifactory_id, repo)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
artifactory_id = 'artifactory_id_example' # str | 
repo = 'repo_example' # str | 

try:
    api_response = api_instance.get_tags(artifactory_id, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactory_id** | **str**|  | 
 **repo** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_by_artifactory_name**
> list[str] get_tags_by_artifactory_name(name, repo, artifact_type=artifact_type)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
repo = 'repo_example' # str | 
artifact_type = 'docker_image' # str |  (optional) (default to docker_image)

try:
    api_response = api_instance.get_tags_by_artifactory_name(name, repo, artifact_type=artifact_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->get_tags_by_artifactory_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **repo** | **str**|  | 
 **artifact_type** | **str**|  | [optional] [default to docker_image]

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_artifactory_linking**
> ComCapillaryOpsCpBoWebhookOneTimeWebhook request_artifactory_linking(body)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoArtifactoryDtoArtifactoryLinkingRequest() # ComCapillaryOpsCpBoArtifactoryDtoArtifactoryLinkingRequest | 

try:
    api_response = api_instance.request_artifactory_linking(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->request_artifactory_linking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoArtifactoryDtoArtifactoryLinkingRequest**](ComCapillaryOpsCpBoArtifactoryDtoArtifactoryLinkingRequest.md)|  | 

### Return type

[**ComCapillaryOpsCpBoWebhookOneTimeWebhook**](ComCapillaryOpsCpBoWebhookOneTimeWebhook.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_basic_docker_artifactory**
> ComCapillaryOpsCpBoArtifactoryBasicDockerArtifactory update_basic_docker_artifactory(body, artifactory_id)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoArtifactoryDtoBasicDockerDTO() # ComCapillaryOpsCpBoArtifactoryDtoBasicDockerDTO | 
artifactory_id = 'artifactory_id_example' # str | 

try:
    api_response = api_instance.update_basic_docker_artifactory(body, artifactory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->update_basic_docker_artifactory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoArtifactoryDtoBasicDockerDTO**](ComCapillaryOpsCpBoArtifactoryDtoBasicDockerDTO.md)|  | 
 **artifactory_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoArtifactoryBasicDockerArtifactory**](ComCapillaryOpsCpBoArtifactoryBasicDockerArtifactory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ecr_artifactory1**
> ComCapillaryOpsCpBoECRArtifactory update_ecr_artifactory1(body, artifactory_id)



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
api_instance = swagger_client.UiArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoECRArtifactory() # ComCapillaryOpsCpBoECRArtifactory | 
artifactory_id = 'artifactory_id_example' # str | 

try:
    api_response = api_instance.update_ecr_artifactory1(body, artifactory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactoryControllerApi->update_ecr_artifactory1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoECRArtifactory**](ComCapillaryOpsCpBoECRArtifactory.md)|  | 
 **artifactory_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoECRArtifactory**](ComCapillaryOpsCpBoECRArtifactory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

