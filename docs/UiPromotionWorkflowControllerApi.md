# swagger_client.UiPromotionWorkflowControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow_using_post**](UiPromotionWorkflowControllerApi.md#create_workflow_using_post) | **POST** /cc-ui/v1/workflow | createWorkflow
[**delete_workflow_using_delete**](UiPromotionWorkflowControllerApi.md#delete_workflow_using_delete) | **DELETE** /cc-ui/v1/workflow/{workflowId} | deleteWorkflow
[**get_all_workflows_using_get**](UiPromotionWorkflowControllerApi.md#get_all_workflows_using_get) | **GET** /cc-ui/v1/workflow | getAllWorkflows
[**get_default_workflow_using_get**](UiPromotionWorkflowControllerApi.md#get_default_workflow_using_get) | **GET** /cc-ui/v1/workflow/default-workflow/registration-type/{registrationType} | getDefaultWorkflow
[**get_registration_specific_workflows_using_get**](UiPromotionWorkflowControllerApi.md#get_registration_specific_workflows_using_get) | **GET** /cc-ui/v1/workflow/registration-specific | getRegistrationSpecificWorkflows
[**get_workflow_using_get**](UiPromotionWorkflowControllerApi.md#get_workflow_using_get) | **GET** /cc-ui/v1/workflow/{workflowId} | getWorkflow
[**get_workflows_by_stack_using_get**](UiPromotionWorkflowControllerApi.md#get_workflows_by_stack_using_get) | **GET** /cc-ui/v1/workflow/blueprint/{stackName} | getWorkflowsByStack
[**update_workflow_using_put**](UiPromotionWorkflowControllerApi.md#update_workflow_using_put) | **PUT** /cc-ui/v1/workflow/{workflowId} | updateWorkflow

# **create_workflow_using_post**
> PromotionWorkflow create_workflow_using_post(body)

createWorkflow

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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.PromotionWorkflow() # PromotionWorkflow | promotionWorkflow

try:
    # createWorkflow
    api_response = api_instance.create_workflow_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->create_workflow_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PromotionWorkflow**](PromotionWorkflow.md)| promotionWorkflow | 

### Return type

[**PromotionWorkflow**](PromotionWorkflow.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workflow_using_delete**
> PromotionWorkflow delete_workflow_using_delete(workflow_id)

deleteWorkflow

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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))
workflow_id = 'workflow_id_example' # str | workflowId

try:
    # deleteWorkflow
    api_response = api_instance.delete_workflow_using_delete(workflow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->delete_workflow_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| workflowId | 

### Return type

[**PromotionWorkflow**](PromotionWorkflow.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_workflows_using_get**
> list[PromotionWorkflow] get_all_workflows_using_get()

getAllWorkflows

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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllWorkflows
    api_response = api_instance.get_all_workflows_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->get_all_workflows_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PromotionWorkflow]**](PromotionWorkflow.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_workflow_using_get**
> PromotionWorkflow get_default_workflow_using_get(registration_type, stack_name=stack_name)

getDefaultWorkflow

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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))
registration_type = 'registration_type_example' # str | registrationType
stack_name = 'stack_name_example' # str | stackName (optional)

try:
    # getDefaultWorkflow
    api_response = api_instance.get_default_workflow_using_get(registration_type, stack_name=stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->get_default_workflow_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_type** | **str**| registrationType | 
 **stack_name** | **str**| stackName | [optional] 

### Return type

[**PromotionWorkflow**](PromotionWorkflow.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_specific_workflows_using_get**
> list[PromotionWorkflow] get_registration_specific_workflows_using_get(registration_type, stack_name=stack_name)

getRegistrationSpecificWorkflows

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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))
registration_type = 'registration_type_example' # str | registrationType
stack_name = 'stack_name_example' # str | stackName (optional)

try:
    # getRegistrationSpecificWorkflows
    api_response = api_instance.get_registration_specific_workflows_using_get(registration_type, stack_name=stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->get_registration_specific_workflows_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_type** | **str**| registrationType | 
 **stack_name** | **str**| stackName | [optional] 

### Return type

[**list[PromotionWorkflow]**](PromotionWorkflow.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_using_get**
> PromotionWorkflow get_workflow_using_get(workflow_id)

getWorkflow

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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))
workflow_id = 'workflow_id_example' # str | workflowId

try:
    # getWorkflow
    api_response = api_instance.get_workflow_using_get(workflow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->get_workflow_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| workflowId | 

### Return type

[**PromotionWorkflow**](PromotionWorkflow.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflows_by_stack_using_get**
> list[PromotionWorkflow] get_workflows_by_stack_using_get(stack_name)

getWorkflowsByStack

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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getWorkflowsByStack
    api_response = api_instance.get_workflows_by_stack_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->get_workflows_by_stack_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**list[PromotionWorkflow]**](PromotionWorkflow.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workflow_using_put**
> PromotionWorkflow update_workflow_using_put(body, workflow_id)

updateWorkflow

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
api_instance = swagger_client.UiPromotionWorkflowControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.PromotionWorkflow() # PromotionWorkflow | promotionWorkflow
workflow_id = 'workflow_id_example' # str | workflowId

try:
    # updateWorkflow
    api_response = api_instance.update_workflow_using_put(body, workflow_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiPromotionWorkflowControllerApi->update_workflow_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PromotionWorkflow**](PromotionWorkflow.md)| promotionWorkflow | 
 **workflow_id** | **str**| workflowId | 

### Return type

[**PromotionWorkflow**](PromotionWorkflow.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

