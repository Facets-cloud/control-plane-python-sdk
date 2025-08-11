# swagger_client.UiArtifactsControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_image_via_register**](UiArtifactsControllerApi.md#attach_image_via_register) | **POST** /cc-ui/v1/artifacts/attach-image-via-register | 
[**delete_artifact**](UiArtifactsControllerApi.md#delete_artifact) | **DELETE** /cc-ui/v1/artifacts/{artifactId} | 
[**generate_artifact_push_credentials1**](UiArtifactsControllerApi.md#generate_artifact_push_credentials1) | **POST** /cc-ui/v1/artifacts/pushCredentials/{stackName}/{appName} | 
[**generate_artifact_push_credentials_v2**](UiArtifactsControllerApi.md#generate_artifact_push_credentials_v2) | **POST** /cc-ui/v1/artifacts/pushCredentialsV2/artifactName/{artifactName}/registrationType/{registrationType}/value/{registrationValue} | 
[**generate_artifact_push_credentials_v3**](UiArtifactsControllerApi.md#generate_artifact_push_credentials_v3) | **POST** /cc-ui/v1/artifacts/pushCredentialsV3/artifactName/{artifactName} | 
[**get_artifact_by_application_name**](UiArtifactsControllerApi.md#get_artifact_by_application_name) | **GET** /cc-ui/v1/artifacts/cluster/{clusterId}/application/{applicationName} | 
[**get_artifact_by_cluster_id**](UiArtifactsControllerApi.md#get_artifact_by_cluster_id) | **GET** /cc-ui/v1/artifacts/{clusterId} | 
[**get_artifacts_by_resource_name_and_resource_type**](UiArtifactsControllerApi.md#get_artifacts_by_resource_name_and_resource_type) | **GET** /cc-ui/v1/artifacts/cluster/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName} | 
[**get_metadata_keys**](UiArtifactsControllerApi.md#get_metadata_keys) | **GET** /cc-ui/v1/artifacts/metadata/keys | 
[**promote_artifact**](UiArtifactsControllerApi.md#promote_artifact) | **POST** /cc-ui/v1/artifacts/{ciId}/promote/{artifactId} | 
[**promote_artifact_by_artifact_ci_name**](UiArtifactsControllerApi.md#promote_artifact_by_artifact_ci_name) | **POST** /cc-ui/v1/artifacts/promote | 
[**push_artifact**](UiArtifactsControllerApi.md#push_artifact) | **POST** /cc-ui/v1/artifacts/push | 
[**reclassify_artifacts**](UiArtifactsControllerApi.md#reclassify_artifacts) | **PUT** /cc-ui/v1/artifacts/reclassify | 
[**register_artifact**](UiArtifactsControllerApi.md#register_artifact) | **POST** /cc-ui/v1/artifacts/register | 
[**register_artifact_by_env**](UiArtifactsControllerApi.md#register_artifact_by_env) | **POST** /cc-ui/v1/artifacts/register-by-env | 
[**register_artifact_by_release_stream**](UiArtifactsControllerApi.md#register_artifact_by_release_stream) | **POST** /cc-ui/v1/artifacts/register-by-release-stream | 
[**register_artifact_saas1**](UiArtifactsControllerApi.md#register_artifact_saas1) | **POST** /cc-ui/v1/artifacts/register-saas | 
[**register_artifact_v2**](UiArtifactsControllerApi.md#register_artifact_v2) | **POST** /cc-ui/v1/artifacts/registerV2 | 
[**update_release_stream**](UiArtifactsControllerApi.md#update_release_stream) | **POST** /cc-ui/v1/artifacts/clusterId/{clusterId}/currentReleaseStream/{currentReleaseStream}/updatedReleaseStream/{updatedReleaseStream}/updateStream | 
[**upload_artifacts_zip**](UiArtifactsControllerApi.md#upload_artifacts_zip) | **POST** /cc-ui/v1/artifacts/upload | 

# **attach_image_via_register**
> attach_image_via_register(body)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ImageOverrideRequest() # ImageOverrideRequest | 

try:
    api_instance.attach_image_via_register(body)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->attach_image_via_register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageOverrideRequest**](ImageOverrideRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact**
> delete_artifact(artifact_id)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
artifact_id = 'artifact_id_example' # str | 

try:
    api_instance.delete_artifact(artifact_id)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->delete_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_artifact_push_credentials1**
> ECRAuthorizationData generate_artifact_push_credentials1(stack_name, app_name)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
app_name = 'app_name_example' # str | 

try:
    api_response = api_instance.generate_artifact_push_credentials1(stack_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->generate_artifact_push_credentials1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **app_name** | **str**|  | 

### Return type

[**ECRAuthorizationData**](ECRAuthorizationData.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_artifact_push_credentials_v2**
> ECRAuthorizationData generate_artifact_push_credentials_v2(artifact_name, registration_type, registration_value)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
artifact_name = 'artifact_name_example' # str | 
registration_type = 'registration_type_example' # str | 
registration_value = 'registration_value_example' # str | 

try:
    api_response = api_instance.generate_artifact_push_credentials_v2(artifact_name, registration_type, registration_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->generate_artifact_push_credentials_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_name** | **str**|  | 
 **registration_type** | **str**|  | 
 **registration_value** | **str**|  | 

### Return type

[**ECRAuthorizationData**](ECRAuthorizationData.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_artifact_push_credentials_v3**
> ECRAuthorizationData generate_artifact_push_credentials_v3(artifact_name, metadata)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
artifact_name = 'artifact_name_example' # str | 
metadata = {'key': 'metadata_example'} # dict(str, str) | 

try:
    api_response = api_instance.generate_artifact_push_credentials_v3(artifact_name, metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->generate_artifact_push_credentials_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_name** | **str**|  | 
 **metadata** | [**dict(str, str)**](str.md)|  | 

### Return type

[**ECRAuthorizationData**](ECRAuthorizationData.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_by_application_name**
> Artifact get_artifact_by_application_name(application_name, cluster_id)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
application_name = 'application_name_example' # str | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_artifact_by_application_name(application_name, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->get_artifact_by_application_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  | 
 **cluster_id** | **str**|  | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_by_cluster_id**
> dict(str, dict(str, Artifact)) get_artifact_by_cluster_id(cluster_id)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_artifact_by_cluster_id(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->get_artifact_by_cluster_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

**dict(str, dict(str, Artifact))**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifacts_by_resource_name_and_resource_type**
> Artifact get_artifacts_by_resource_name_and_resource_type(cluster_id, resource_type, resource_name)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.get_artifacts_by_resource_name_and_resource_type(cluster_id, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->get_artifacts_by_resource_name_and_resource_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_keys**
> list[str] get_metadata_keys()



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_metadata_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->get_metadata_keys: %s\n" % e)
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

# **promote_artifact**
> Artifact promote_artifact(ci_id, artifact_id)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
ci_id = 'ci_id_example' # str | 
artifact_id = 'artifact_id_example' # str | 

try:
    api_response = api_instance.promote_artifact(ci_id, artifact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->promote_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ci_id** | **str**|  | 
 **artifact_id** | **str**|  | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promote_artifact_by_artifact_ci_name**
> Artifact promote_artifact_by_artifact_ci_name(ci_name, artifact_id)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
ci_name = 'ci_name_example' # str | 
artifact_id = 'artifact_id_example' # str | 

try:
    api_response = api_instance.promote_artifact_by_artifact_ci_name(ci_name, artifact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->promote_artifact_by_artifact_ci_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ci_name** | **str**|  | 
 **artifact_id** | **str**|  | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **push_artifact**
> push_artifact(body)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactRequest() # ArtifactRequest | 

try:
    api_instance.push_artifact(body)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->push_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactRequest**](ArtifactRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reclassify_artifacts**
> reclassify_artifacts(artifact_ci_id)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
artifact_ci_id = 'artifact_ci_id_example' # str | 

try:
    api_instance.reclassify_artifacts(artifact_ci_id)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->reclassify_artifacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_ci_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_artifact**
> list[Artifact] register_artifact(body)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Artifact() # Artifact | 

try:
    api_response = api_instance.register_artifact(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->register_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Artifact**](Artifact.md)|  | 

### Return type

[**list[Artifact]**](Artifact.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_artifact_by_env**
> register_artifact_by_env(body)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactByEnvironmentRequest() # ArtifactByEnvironmentRequest | 

try:
    api_instance.register_artifact_by_env(body)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->register_artifact_by_env: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactByEnvironmentRequest**](ArtifactByEnvironmentRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_artifact_by_release_stream**
> register_artifact_by_release_stream(body)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactByReleaseStreamRequest() # ArtifactByReleaseStreamRequest | 

try:
    api_instance.register_artifact_by_release_stream(body)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->register_artifact_by_release_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactByReleaseStreamRequest**](ArtifactByReleaseStreamRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_artifact_saas1**
> register_artifact_saas1(body)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.SaasArtifactRequest() # SaasArtifactRequest | 

try:
    api_instance.register_artifact_saas1(body)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->register_artifact_saas1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SaasArtifactRequest**](SaasArtifactRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_artifact_v2**
> register_artifact_v2(body)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactRequest() # ArtifactRequest | 

try:
    api_instance.register_artifact_v2(body)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->register_artifact_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactRequest**](ArtifactRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_release_stream**
> object update_release_stream(cluster_id, current_release_stream, updated_release_stream, include_apps, exclude_apps)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
current_release_stream = 'current_release_stream_example' # str | 
updated_release_stream = 'updated_release_stream_example' # str | 
include_apps = ['include_apps_example'] # list[str] | 
exclude_apps = ['exclude_apps_example'] # list[str] | 

try:
    api_response = api_instance.update_release_stream(cluster_id, current_release_stream, updated_release_stream, include_apps, exclude_apps)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->update_release_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **current_release_stream** | **str**|  | 
 **updated_release_stream** | **str**|  | 
 **include_apps** | [**list[str]**](str.md)|  | 
 **exclude_apps** | [**list[str]**](str.md)|  | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_artifacts_zip**
> upload_artifacts_zip(body=body)



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
api_instance = swagger_client.UiArtifactsControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactsUploadBody() # ArtifactsUploadBody |  (optional)

try:
    api_instance.upload_artifacts_zip(body=body)
except ApiException as e:
    print("Exception when calling UiArtifactsControllerApi->upload_artifacts_zip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactsUploadBody**](ArtifactsUploadBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

