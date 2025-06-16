# swagger_client.UiPromotionWorkflowControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow**](UiPromotionWorkflowControllerApi.md#create_workflow) | **POST** /cc-ui/v1/workflow | 
[**delete_workflow**](UiPromotionWorkflowControllerApi.md#delete_workflow) | **DELETE** /cc-ui/v1/workflow/{workflowId} | 
[**get_all_workflows**](UiPromotionWorkflowControllerApi.md#get_all_workflows) | **GET** /cc-ui/v1/workflow | 
[**get_default_workflow**](UiPromotionWorkflowControllerApi.md#get_default_workflow) | **GET** /cc-ui/v1/workflow/default-workflow/registration-type/{registrationType} | 
[**get_registration_specific_workflows**](UiPromotionWorkflowControllerApi.md#get_registration_specific_workflows) | **GET** /cc-ui/v1/workflow/registration-specific | 
[**get_workflow**](UiPromotionWorkflowControllerApi.md#get_workflow) | **GET** /cc-ui/v1/workflow/{workflowId} | 
[**get_workflows_by_stack**](UiPromotionWorkflowControllerApi.md#get_workflows_by_stack) | **GET** /cc-ui/v1/workflow/blueprint/{stackName} | 
[**update_workflow**](UiPromotionWorkflowControllerApi.md#update_workflow) | **PUT** /cc-ui/v1/workflow/{workflowId} | 

# **create_workflow**
> ComCapillaryOpsCpBoArtifactsPromotionWorkflow create_workflow(body)



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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoArtifactsPromotionWorkflow() # ComCapillaryOpsCpBoArtifactsPromotionWorkflow | 

try:
    api_response = api_instance.create_workflow(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->create_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoArtifactsPromotionWorkflow**](ComCapillaryOpsCpBoArtifactsPromotionWorkflow.md)|  | 

### Return type

[**ComCapillaryOpsCpBoArtifactsPromotionWorkflow**](ComCapillaryOpsCpBoArtifactsPromotionWorkflow.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workflow**
> ComCapillaryOpsCpBoArtifactsPromotionWorkflow delete_workflow(workflow_id)



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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))
workflow_id = 'workflow_id_example' # str | 

try:
    api_response = api_instance.delete_workflow(workflow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->delete_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoArtifactsPromotionWorkflow**](ComCapillaryOpsCpBoArtifactsPromotionWorkflow.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_workflows**
> list[ComCapillaryOpsCpBoArtifactsPromotionWorkflow] get_all_workflows()



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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_workflows()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->get_all_workflows: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoArtifactsPromotionWorkflow]**](ComCapillaryOpsCpBoArtifactsPromotionWorkflow.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_workflow**
> ComCapillaryOpsCpBoArtifactsPromotionWorkflow get_default_workflow(registration_type, stack_name=stack_name)



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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))
registration_type = 'registration_type_example' # str | 
stack_name = 'stack_name_example' # str |  (optional)

try:
    api_response = api_instance.get_default_workflow(registration_type, stack_name=stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->get_default_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_type** | **str**|  | 
 **stack_name** | **str**|  | [optional] 

### Return type

[**ComCapillaryOpsCpBoArtifactsPromotionWorkflow**](ComCapillaryOpsCpBoArtifactsPromotionWorkflow.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_specific_workflows**
> list[ComCapillaryOpsCpBoArtifactsPromotionWorkflow] get_registration_specific_workflows(registration_type, stack_name=stack_name)



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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))
registration_type = 'registration_type_example' # str | 
stack_name = 'stack_name_example' # str |  (optional)

try:
    api_response = api_instance.get_registration_specific_workflows(registration_type, stack_name=stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->get_registration_specific_workflows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_type** | **str**|  | 
 **stack_name** | **str**|  | [optional] 

### Return type

[**list[ComCapillaryOpsCpBoArtifactsPromotionWorkflow]**](ComCapillaryOpsCpBoArtifactsPromotionWorkflow.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow**
> ComCapillaryOpsCpBoArtifactsPromotionWorkflow get_workflow(workflow_id)



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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))
workflow_id = 'workflow_id_example' # str | 

try:
    api_response = api_instance.get_workflow(workflow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->get_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoArtifactsPromotionWorkflow**](ComCapillaryOpsCpBoArtifactsPromotionWorkflow.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflows_by_stack**
> list[ComCapillaryOpsCpBoArtifactsPromotionWorkflow] get_workflows_by_stack(stack_name)



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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_workflows_by_stack(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->get_workflows_by_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoArtifactsPromotionWorkflow]**](ComCapillaryOpsCpBoArtifactsPromotionWorkflow.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workflow**
> ComCapillaryOpsCpBoArtifactsPromotionWorkflow update_workflow(body, workflow_id)



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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoArtifactsPromotionWorkflow() # ComCapillaryOpsCpBoArtifactsPromotionWorkflow | 
workflow_id = 'workflow_id_example' # str | 

try:
    api_response = api_instance.update_workflow(body, workflow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->update_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoArtifactsPromotionWorkflow**](ComCapillaryOpsCpBoArtifactsPromotionWorkflow.md)|  | 
 **workflow_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoArtifactsPromotionWorkflow**](ComCapillaryOpsCpBoArtifactsPromotionWorkflow.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

