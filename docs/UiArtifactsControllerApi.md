# swagger_client.UiArtifactsControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_image_via_register_using_post**](UiArtifactsControllerApi.md#attach_image_via_register_using_post) | **POST** /cc-ui/v1/artifacts/attach-image-via-register | attachImageViaRegister
[**delete_artifact_using_delete**](UiArtifactsControllerApi.md#delete_artifact_using_delete) | **DELETE** /cc-ui/v1/artifacts/{artifactId} | deleteArtifact
[**generate_artifact_push_credentials_using_post**](UiArtifactsControllerApi.md#generate_artifact_push_credentials_using_post) | **POST** /cc-ui/v1/artifacts/pushCredentials/{stackName}/{appName} | generateArtifactPushCredentials
[**generate_artifact_push_credentials_v2_using_post**](UiArtifactsControllerApi.md#generate_artifact_push_credentials_v2_using_post) | **POST** /cc-ui/v1/artifacts/pushCredentialsV2/artifactName/{artifactName}/registrationType/{registrationType}/value/{registrationValue} | generateArtifactPushCredentialsV2
[**generate_artifact_push_credentials_v3_using_post**](UiArtifactsControllerApi.md#generate_artifact_push_credentials_v3_using_post) | **POST** /cc-ui/v1/artifacts/pushCredentialsV3/artifactName/{artifactName} | generateArtifactPushCredentialsV3
[**get_all_using_get**](UiArtifactsControllerApi.md#get_all_using_get) | **GET** /cc-ui/v1/artifacts | getAll
[**get_artifact_by_application_name_using_get**](UiArtifactsControllerApi.md#get_artifact_by_application_name_using_get) | **GET** /cc-ui/v1/artifacts/cluster/{clusterId}/application/{applicationName} | getArtifactByApplicationName
[**get_artifact_by_cluster_id_using_get**](UiArtifactsControllerApi.md#get_artifact_by_cluster_id_using_get) | **GET** /cc-ui/v1/artifacts/{clusterId} | getArtifactByClusterId
[**get_artifacts_by_resource_name_and_resource_type_using_get**](UiArtifactsControllerApi.md#get_artifacts_by_resource_name_and_resource_type_using_get) | **GET** /cc-ui/v1/artifacts/cluster/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName} | getArtifactsByResourceNameAndResourceType
[**get_metadata_keys_using_get**](UiArtifactsControllerApi.md#get_metadata_keys_using_get) | **GET** /cc-ui/v1/artifacts/metadata/keys | getMetadataKeys
[**promote_artifact_by_artifact_ci_name_using_post**](UiArtifactsControllerApi.md#promote_artifact_by_artifact_ci_name_using_post) | **POST** /cc-ui/v1/artifacts/promote | promoteArtifactByArtifactCiName
[**promote_artifact_using_post**](UiArtifactsControllerApi.md#promote_artifact_using_post) | **POST** /cc-ui/v1/artifacts/{ciId}/promote/{artifactId} | promoteArtifact
[**push_artifact_using_post**](UiArtifactsControllerApi.md#push_artifact_using_post) | **POST** /cc-ui/v1/artifacts/push | pushArtifact
[**reclassify_artifacts_using_put**](UiArtifactsControllerApi.md#reclassify_artifacts_using_put) | **PUT** /cc-ui/v1/artifacts/reclassify | reclassifyArtifacts
[**register_artifact_by_env_using_post**](UiArtifactsControllerApi.md#register_artifact_by_env_using_post) | **POST** /cc-ui/v1/artifacts/register-by-env | registerArtifactByEnv
[**register_artifact_by_release_stream_using_post**](UiArtifactsControllerApi.md#register_artifact_by_release_stream_using_post) | **POST** /cc-ui/v1/artifacts/register-by-release-stream | registerArtifactByReleaseStream
[**register_artifact_saas_using_post**](UiArtifactsControllerApi.md#register_artifact_saas_using_post) | **POST** /cc-ui/v1/artifacts/register-saas | registerArtifactSaas
[**register_artifact_using_post1**](UiArtifactsControllerApi.md#register_artifact_using_post1) | **POST** /cc-ui/v1/artifacts/register | registerArtifact
[**register_artifact_v2_using_post**](UiArtifactsControllerApi.md#register_artifact_v2_using_post) | **POST** /cc-ui/v1/artifacts/registerV2 | registerArtifactV2
[**update_release_stream_using_post**](UiArtifactsControllerApi.md#update_release_stream_using_post) | **POST** /cc-ui/v1/artifacts/clusterId/{clusterId}/currentReleaseStream/{currentReleaseStream}/updatedReleaseStream/{updatedReleaseStream}/updateStream | updateReleaseStream
[**upload_artifacts_zip_using_post**](UiArtifactsControllerApi.md#upload_artifacts_zip_using_post) | **POST** /cc-ui/v1/artifacts/upload | uploadArtifactsZip

# **attach_image_via_register_using_post**
> attach_image_via_register_using_post(body)

attachImageViaRegister

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ImageOverrideRequest() # ImageOverrideRequest | request

try:
    # attachImageViaRegister
    api_instance.attach_image_via_register_using_post(body)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->attach_image_via_register_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageOverrideRequest**](ImageOverrideRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact_using_delete**
> delete_artifact_using_delete(artifact_id)

deleteArtifact

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
artifact_id = 'artifact_id_example' # str | artifactId

try:
    # deleteArtifact
    api_instance.delete_artifact_using_delete(artifact_id)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->delete_artifact_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **str**| artifactId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_artifact_push_credentials_using_post**
> ECRAuthorizationData generate_artifact_push_credentials_using_post(app_name, stack_name)

generateArtifactPushCredentials

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
app_name = 'app_name_example' # str | appName
stack_name = 'stack_name_example' # str | stackName

try:
    # generateArtifactPushCredentials
    api_response = api_instance.generate_artifact_push_credentials_using_post(app_name, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->generate_artifact_push_credentials_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| appName | 
 **stack_name** | **str**| stackName | 

### Return type

[**ECRAuthorizationData**](ECRAuthorizationData.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_artifact_push_credentials_v2_using_post**
> ECRAuthorizationData generate_artifact_push_credentials_v2_using_post(artifact_name, registration_type, registration_value)

generateArtifactPushCredentialsV2

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
artifact_name = 'artifact_name_example' # str | artifactName
registration_type = 'registration_type_example' # str | registrationType
registration_value = 'registration_value_example' # str | registrationValue

try:
    # generateArtifactPushCredentialsV2
    api_response = api_instance.generate_artifact_push_credentials_v2_using_post(artifact_name, registration_type, registration_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->generate_artifact_push_credentials_v2_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_name** | **str**| artifactName | 
 **registration_type** | **str**| registrationType | 
 **registration_value** | **str**| registrationValue | 

### Return type

[**ECRAuthorizationData**](ECRAuthorizationData.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_artifact_push_credentials_v3_using_post**
> ECRAuthorizationData generate_artifact_push_credentials_v3_using_post(artifact_name, metadata)

generateArtifactPushCredentialsV3

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
artifact_name = 'artifact_name_example' # str | artifactName
metadata = NULL # object | metadata

try:
    # generateArtifactPushCredentialsV3
    api_response = api_instance.generate_artifact_push_credentials_v3_using_post(artifact_name, metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->generate_artifact_push_credentials_v3_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_name** | **str**| artifactName | 
 **metadata** | [**object**](.md)| metadata | 

### Return type

[**ECRAuthorizationData**](ECRAuthorizationData.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_using_get**
> list[Artifact] get_all_using_get(artifactory=artifactory, classified=classified)

getAll

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
artifactory = 'artifactory_example' # str | artifactory (optional)
classified = true # bool | classified (optional)

try:
    # getAll
    api_response = api_instance.get_all_using_get(artifactory=artifactory, classified=classified)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->get_all_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactory** | **str**| artifactory | [optional] 
 **classified** | **bool**| classified | [optional] 

### Return type

[**list[Artifact]**](Artifact.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_by_application_name_using_get**
> Artifact get_artifact_by_application_name_using_get(application_name, cluster_id)

getArtifactByApplicationName

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
application_name = 'application_name_example' # str | applicationName
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getArtifactByApplicationName
    api_response = api_instance.get_artifact_by_application_name_using_get(application_name, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->get_artifact_by_application_name_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| applicationName | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_by_cluster_id_using_get**
> dict(str, dict(str, Artifact)) get_artifact_by_cluster_id_using_get(cluster_id)

getArtifactByClusterId

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getArtifactByClusterId
    api_response = api_instance.get_artifact_by_cluster_id_using_get(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->get_artifact_by_cluster_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

**dict(str, dict(str, Artifact))**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifacts_by_resource_name_and_resource_type_using_get**
> Artifact get_artifacts_by_resource_name_and_resource_type_using_get(cluster_id, resource_name, resource_type)

getArtifactsByResourceNameAndResourceType

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # getArtifactsByResourceNameAndResourceType
    api_response = api_instance.get_artifacts_by_resource_name_and_resource_type_using_get(cluster_id, resource_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->get_artifacts_by_resource_name_and_resource_type_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_keys_using_get**
> list[str] get_metadata_keys_using_get()

getMetadataKeys

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))

try:
    # getMetadataKeys
    api_response = api_instance.get_metadata_keys_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->get_metadata_keys_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promote_artifact_by_artifact_ci_name_using_post**
> Artifact promote_artifact_by_artifact_ci_name_using_post(artifact_id, ci_name)

promoteArtifactByArtifactCiName

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
artifact_id = 'artifact_id_example' # str | artifactId
ci_name = 'ci_name_example' # str | ciName

try:
    # promoteArtifactByArtifactCiName
    api_response = api_instance.promote_artifact_by_artifact_ci_name_using_post(artifact_id, ci_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->promote_artifact_by_artifact_ci_name_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **str**| artifactId | 
 **ci_name** | **str**| ciName | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promote_artifact_using_post**
> Artifact promote_artifact_using_post(artifact_id, ci_id)

promoteArtifact

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
artifact_id = 'artifact_id_example' # str | artifactId
ci_id = 'ci_id_example' # str | ciId

try:
    # promoteArtifact
    api_response = api_instance.promote_artifact_using_post(artifact_id, ci_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->promote_artifact_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **str**| artifactId | 
 **ci_id** | **str**| ciId | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **push_artifact_using_post**
> push_artifact_using_post(body)

pushArtifact

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactRequest() # ArtifactRequest | artifactRequest

try:
    # pushArtifact
    api_instance.push_artifact_using_post(body)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->push_artifact_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactRequest**](ArtifactRequest.md)| artifactRequest | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reclassify_artifacts_using_put**
> reclassify_artifacts_using_put(artifact_ci_id)

reclassifyArtifacts

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
artifact_ci_id = 'artifact_ci_id_example' # str | artifactCiId

try:
    # reclassifyArtifacts
    api_instance.reclassify_artifacts_using_put(artifact_ci_id)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->reclassify_artifacts_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_ci_id** | **str**| artifactCiId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_artifact_by_env_using_post**
> register_artifact_by_env_using_post(body)

registerArtifactByEnv

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactByEnvironmentRequest() # ArtifactByEnvironmentRequest | artifactRequest

try:
    # registerArtifactByEnv
    api_instance.register_artifact_by_env_using_post(body)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->register_artifact_by_env_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactByEnvironmentRequest**](ArtifactByEnvironmentRequest.md)| artifactRequest | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_artifact_by_release_stream_using_post**
> register_artifact_by_release_stream_using_post(body)

registerArtifactByReleaseStream

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactByReleaseStreamRequest() # ArtifactByReleaseStreamRequest | artifactRequest

try:
    # registerArtifactByReleaseStream
    api_instance.register_artifact_by_release_stream_using_post(body)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->register_artifact_by_release_stream_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactByReleaseStreamRequest**](ArtifactByReleaseStreamRequest.md)| artifactRequest | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_artifact_saas_using_post**
> register_artifact_saas_using_post(body)

registerArtifactSaas

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.SaasArtifactRequest() # SaasArtifactRequest | artifactRequest

try:
    # registerArtifactSaas
    api_instance.register_artifact_saas_using_post(body)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->register_artifact_saas_using_post: %s\n" % e)
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

# **register_artifact_using_post1**
> list[Artifact] register_artifact_using_post1(body)

registerArtifact

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Artifact() # Artifact | artifact

try:
    # registerArtifact
    api_response = api_instance.register_artifact_using_post1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->register_artifact_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Artifact**](Artifact.md)| artifact | 

### Return type

[**list[Artifact]**](Artifact.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_artifact_v2_using_post**
> register_artifact_v2_using_post(body)

registerArtifactV2

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactRequest() # ArtifactRequest | artifactRequest

try:
    # registerArtifactV2
    api_instance.register_artifact_v2_using_post(body)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->register_artifact_v2_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactRequest**](ArtifactRequest.md)| artifactRequest | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_release_stream_using_post**
> object update_release_stream_using_post(cluster_id, current_release_stream, exclude_apps, include_apps, updated_release_stream)

updateReleaseStream

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
current_release_stream = 'current_release_stream_example' # str | currentReleaseStream
exclude_apps = ['exclude_apps_example'] # list[str] | excludeApps
include_apps = ['include_apps_example'] # list[str] | includeApps
updated_release_stream = 'updated_release_stream_example' # str | updatedReleaseStream

try:
    # updateReleaseStream
    api_response = api_instance.update_release_stream_using_post(cluster_id, current_release_stream, exclude_apps, include_apps, updated_release_stream)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->update_release_stream_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **current_release_stream** | **str**| currentReleaseStream | 
 **exclude_apps** | [**list[str]**](str.md)| excludeApps | 
 **include_apps** | [**list[str]**](str.md)| includeApps | 
 **updated_release_stream** | **str**| updatedReleaseStream | 

### Return type

**object**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_artifacts_zip_using_post**
> upload_artifacts_zip_using_post(artifact_request, file)

uploadArtifactsZip

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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
artifact_request = NULL # object | 
file = 'file_example' # str | 

try:
    # uploadArtifactsZip
    api_instance.upload_artifacts_zip_using_post(artifact_request, file)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->upload_artifacts_zip_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_request** | [**object**](.md)|  | 
 **file** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

