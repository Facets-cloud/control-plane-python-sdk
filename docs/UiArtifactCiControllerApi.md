# swagger_client.UiArtifactCiControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_edit_workflow**](UiArtifactCiControllerApi.md#bulk_edit_workflow) | **POST** /cc-ui/v1/artifacts-ci/bulk-edit-workflow | 
[**create_artifact_ci**](UiArtifactCiControllerApi.md#create_artifact_ci) | **POST** /cc-ui/v1/artifacts-ci | 
[**delete_artifact_ci**](UiArtifactCiControllerApi.md#delete_artifact_ci) | **DELETE** /cc-ui/v1/artifacts-ci/{ciId} | 
[**get_all_artifacts_ci**](UiArtifactCiControllerApi.md#get_all_artifacts_ci) | **GET** /cc-ui/v1/artifacts-ci | 
[**get_artifact_ci**](UiArtifactCiControllerApi.md#get_artifact_ci) | **GET** /cc-ui/v1/artifacts-ci/{ciId} | 
[**get_artifact_ci_by_name**](UiArtifactCiControllerApi.md#get_artifact_ci_by_name) | **GET** /cc-ui/v1/artifacts-ci/name/{ciName} | 
[**get_artifact_cis_by_stack**](UiArtifactCiControllerApi.md#get_artifact_cis_by_stack) | **GET** /cc-ui/v1/artifacts-ci/blueprint/{stackName} | 
[**get_artifacts_for_ci**](UiArtifactCiControllerApi.md#get_artifacts_for_ci) | **GET** /cc-ui/v1/artifacts-ci/{ciName}/artifacts | 
[**update_artifact_ci**](UiArtifactCiControllerApi.md#update_artifact_ci) | **PUT** /cc-ui/v1/artifacts-ci/{ciId} | 

# **bulk_edit_workflow**
> bulk_edit_workflow(body)



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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.BulkWorkflowAttachRequest() # BulkWorkflowAttachRequest | 

try:
    api_instance.bulk_edit_workflow(body)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->bulk_edit_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkWorkflowAttachRequest**](BulkWorkflowAttachRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_artifact_ci**
> ArtifactCI create_artifact_ci(body)



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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactCI() # ArtifactCI | 

try:
    api_response = api_instance.create_artifact_ci(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->create_artifact_ci: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactCI**](ArtifactCI.md)|  | 

### Return type

[**ArtifactCI**](ArtifactCI.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact_ci**
> ArtifactCI delete_artifact_ci(ci_id)



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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
ci_id = 'ci_id_example' # str | 

try:
    api_response = api_instance.delete_artifact_ci(ci_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->delete_artifact_ci: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ci_id** | **str**|  | 

### Return type

[**ArtifactCI**](ArtifactCI.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_artifacts_ci**
> list[ArtifactCI] get_all_artifacts_ci()



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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_artifacts_ci()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->get_all_artifacts_ci: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ArtifactCI]**](ArtifactCI.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_ci**
> ArtifactCI get_artifact_ci(ci_id)



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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
ci_id = 'ci_id_example' # str | 

try:
    api_response = api_instance.get_artifact_ci(ci_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->get_artifact_ci: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ci_id** | **str**|  | 

### Return type

[**ArtifactCI**](ArtifactCI.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_ci_by_name**
> ArtifactCI get_artifact_ci_by_name(ci_name)



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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
ci_name = 'ci_name_example' # str | 

try:
    api_response = api_instance.get_artifact_ci_by_name(ci_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->get_artifact_ci_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ci_name** | **str**|  | 

### Return type

[**ArtifactCI**](ArtifactCI.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_cis_by_stack**
> list[ArtifactCI] get_artifact_cis_by_stack(stack_name)



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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_artifact_cis_by_stack(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->get_artifact_cis_by_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**list[ArtifactCI]**](ArtifactCI.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifacts_for_ci**
> list[CiArtifactResponse] get_artifacts_for_ci(ci_name)



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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
ci_name = 'ci_name_example' # str | 

try:
    api_response = api_instance.get_artifacts_for_ci(ci_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->get_artifacts_for_ci: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ci_name** | **str**|  | 

### Return type

[**list[CiArtifactResponse]**](CiArtifactResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_artifact_ci**
> ArtifactCI update_artifact_ci(body, ci_id)



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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactCI() # ArtifactCI | 
ci_id = 'ci_id_example' # str | 

try:
    api_response = api_instance.update_artifact_ci(body, ci_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->update_artifact_ci: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactCI**](ArtifactCI.md)|  | 
 **ci_id** | **str**|  | 

### Return type

[**ArtifactCI**](ArtifactCI.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

