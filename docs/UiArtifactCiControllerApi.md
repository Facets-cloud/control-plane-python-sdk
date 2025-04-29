# swagger_client.UiArtifactCiControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_edit_workflow_using_post**](UiArtifactCiControllerApi.md#bulk_edit_workflow_using_post) | **POST** /cc-ui/v1/artifacts-ci/bulk-edit-workflow | bulkEditWorkflow
[**create_artifact_ci_using_post**](UiArtifactCiControllerApi.md#create_artifact_ci_using_post) | **POST** /cc-ui/v1/artifacts-ci | createArtifactCI
[**delete_artifact_ci_using_delete**](UiArtifactCiControllerApi.md#delete_artifact_ci_using_delete) | **DELETE** /cc-ui/v1/artifacts-ci/{ciId} | deleteArtifactCI
[**get_all_artifacts_ci_using_get**](UiArtifactCiControllerApi.md#get_all_artifacts_ci_using_get) | **GET** /cc-ui/v1/artifacts-ci | getAllArtifactsCI
[**get_artifact_ci_by_name_using_get**](UiArtifactCiControllerApi.md#get_artifact_ci_by_name_using_get) | **GET** /cc-ui/v1/artifacts-ci/name/{ciName} | getArtifactCiByName
[**get_artifact_ci_using_get**](UiArtifactCiControllerApi.md#get_artifact_ci_using_get) | **GET** /cc-ui/v1/artifacts-ci/{ciId} | getArtifactCI
[**get_artifact_cis_by_stack_using_get**](UiArtifactCiControllerApi.md#get_artifact_cis_by_stack_using_get) | **GET** /cc-ui/v1/artifacts-ci/blueprint/{stackName} | getArtifactCisByStack
[**get_artifacts_for_ci_using_get**](UiArtifactCiControllerApi.md#get_artifacts_for_ci_using_get) | **GET** /cc-ui/v1/artifacts-ci/{ciName}/artifacts | getArtifactsForCI
[**update_artifact_ci_using_put**](UiArtifactCiControllerApi.md#update_artifact_ci_using_put) | **PUT** /cc-ui/v1/artifacts-ci/{ciId} | updateArtifactCI

# **bulk_edit_workflow_using_post**
> bulk_edit_workflow_using_post(body)

bulkEditWorkflow

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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.BulkWorkflowAttachRequest() # BulkWorkflowAttachRequest | bulkWorkflowAttachRequest

try:
    # bulkEditWorkflow
    api_instance.bulk_edit_workflow_using_post(body)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->bulk_edit_workflow_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkWorkflowAttachRequest**](BulkWorkflowAttachRequest.md)| bulkWorkflowAttachRequest | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_artifact_ci_using_post**
> ArtifactCI create_artifact_ci_using_post(body)

createArtifactCI

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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactCI() # ArtifactCI | artifactCI

try:
    # createArtifactCI
    api_response = api_instance.create_artifact_ci_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->create_artifact_ci_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactCI**](ArtifactCI.md)| artifactCI | 

### Return type

[**ArtifactCI**](ArtifactCI.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact_ci_using_delete**
> ArtifactCI delete_artifact_ci_using_delete(ci_id)

deleteArtifactCI

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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
ci_id = 'ci_id_example' # str | ciId

try:
    # deleteArtifactCI
    api_response = api_instance.delete_artifact_ci_using_delete(ci_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->delete_artifact_ci_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ci_id** | **str**| ciId | 

### Return type

[**ArtifactCI**](ArtifactCI.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_artifacts_ci_using_get**
> list[ArtifactCI] get_all_artifacts_ci_using_get()

getAllArtifactsCI

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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllArtifactsCI
    api_response = api_instance.get_all_artifacts_ci_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->get_all_artifacts_ci_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ArtifactCI]**](ArtifactCI.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_ci_by_name_using_get**
> ArtifactCI get_artifact_ci_by_name_using_get(ci_name)

getArtifactCiByName

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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
ci_name = 'ci_name_example' # str | ciName

try:
    # getArtifactCiByName
    api_response = api_instance.get_artifact_ci_by_name_using_get(ci_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->get_artifact_ci_by_name_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ci_name** | **str**| ciName | 

### Return type

[**ArtifactCI**](ArtifactCI.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_ci_using_get**
> ArtifactCI get_artifact_ci_using_get(ci_id)

getArtifactCI

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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
ci_id = 'ci_id_example' # str | ciId

try:
    # getArtifactCI
    api_response = api_instance.get_artifact_ci_using_get(ci_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->get_artifact_ci_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ci_id** | **str**| ciId | 

### Return type

[**ArtifactCI**](ArtifactCI.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_cis_by_stack_using_get**
> list[ArtifactCI] get_artifact_cis_by_stack_using_get(stack_name)

getArtifactCisByStack

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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getArtifactCisByStack
    api_response = api_instance.get_artifact_cis_by_stack_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->get_artifact_cis_by_stack_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**list[ArtifactCI]**](ArtifactCI.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifacts_for_ci_using_get**
> list[CiArtifactResponse] get_artifacts_for_ci_using_get(ci_name)

getArtifactsForCI

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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
ci_name = 'ci_name_example' # str | ciName

try:
    # getArtifactsForCI
    api_response = api_instance.get_artifacts_for_ci_using_get(ci_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->get_artifacts_for_ci_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ci_name** | **str**| ciName | 

### Return type

[**list[CiArtifactResponse]**](CiArtifactResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_artifact_ci_using_put**
> ArtifactCI update_artifact_ci_using_put(body, ci_id)

updateArtifactCI

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
api_instance = swagger_client.UiArtifactCiControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactCI() # ArtifactCI | artifactCI
ci_id = 'ci_id_example' # str | ciId

try:
    # updateArtifactCI
    api_response = api_instance.update_artifact_ci_using_put(body, ci_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactCiControllerApi->update_artifact_ci_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactCI**](ArtifactCI.md)| artifactCI | 
 **ci_id** | **str**| ciId | 

### Return type

[**ArtifactCI**](ArtifactCI.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

