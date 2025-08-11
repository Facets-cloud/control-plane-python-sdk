# swagger_client.VariableManagementApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_variable**](VariableManagementApi.md#add_variable) | **POST** /cc-ui/v1/stacks/{stackName}/variables | Add new variable/secret
[**add_variables_bulk**](VariableManagementApi.md#add_variables_bulk) | **POST** /cc-ui/v1/stacks/{stackName}/variables/bulk | Add multiple new variables/secrets
[**get_variable_across_environments**](VariableManagementApi.md#get_variable_across_environments) | **GET** /cc-ui/v1/stacks/{stackName}/variables/{variableName}/environments | Get variable/secret across environments
[**update_variable**](VariableManagementApi.md#update_variable) | **PUT** /cc-ui/v1/stacks/{stackName}/variables | Update variable/secret

# **add_variable**
> add_variable(body, stack_name)

Add new variable/secret

Adds a new variable/secret with project-level default and optional environment-specific values

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
api_instance = swagger_client.VariableManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.VariableRequest() # VariableRequest | 
stack_name = 'stack_name_example' # str | Project name

try:
    # Add new variable/secret
    api_instance.add_variable(body, stack_name)
except ApiException as e:
    print("Exception when calling VariableManagementApi->add_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariableRequest**](VariableRequest.md)|  | 
 **stack_name** | **str**| Project name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_variables_bulk**
> add_variables_bulk(body, stack_name)

Add multiple new variables/secrets

Adds multiple new variables/secrets with project-level defaults and optional environment-specific values

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
api_instance = swagger_client.VariableManagementApi(swagger_client.ApiClient(configuration))
body = [swagger_client.VariableRequest()] # list[VariableRequest] | 
stack_name = 'stack_name_example' # str | Project name

try:
    # Add multiple new variables/secrets
    api_instance.add_variables_bulk(body, stack_name)
except ApiException as e:
    print("Exception when calling VariableManagementApi->add_variables_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[VariableRequest]**](VariableRequest.md)|  | 
 **stack_name** | **str**| Project name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variable_across_environments**
> VariableEnvironmentResponse get_variable_across_environments(stack_name, variable_name)

Get variable/secret across environments

Retrieves values of a specific variable/secret across all environments in a project

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
api_instance = swagger_client.VariableManagementApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | Project name
variable_name = 'variable_name_example' # str | Variable name

try:
    # Get variable/secret across environments
    api_response = api_instance.get_variable_across_environments(stack_name, variable_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariableManagementApi->get_variable_across_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| Project name | 
 **variable_name** | **str**| Variable name | 

### Return type

[**VariableEnvironmentResponse**](VariableEnvironmentResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_variable**
> update_variable(body, stack_name)

Update variable/secret

Updates an existing variable/secret with project-level default and optional environment-specific values

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
api_instance = swagger_client.VariableManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.VariableRequest() # VariableRequest | 
stack_name = 'stack_name_example' # str | Project name

try:
    # Update variable/secret
    api_instance.update_variable(body, stack_name)
except ApiException as e:
    print("Exception when calling VariableManagementApi->update_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariableRequest**](VariableRequest.md)|  | 
 **stack_name** | **str**| Project name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

