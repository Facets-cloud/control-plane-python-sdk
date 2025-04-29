# swagger_client.UiCoderControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace_with_existing_branch_using_post**](UiCoderControllerApi.md#create_workspace_with_existing_branch_using_post) | **POST** /cc-ui/v1/coder/stack/{stackName}/existing-branch | createWorkspaceWithExistingBranch
[**create_workspace_with_existing_branch_using_post1**](UiCoderControllerApi.md#create_workspace_with_existing_branch_using_post1) | **POST** /cc-ui/v1/coder/stack/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/existing-branch | createWorkspaceWithExistingBranch
[**create_workspace_with_new_branch_using_post**](UiCoderControllerApi.md#create_workspace_with_new_branch_using_post) | **POST** /cc-ui/v1/coder/stack/{stackName}/new-branch | createWorkspaceWithNewBranch
[**create_workspace_with_new_branch_using_post1**](UiCoderControllerApi.md#create_workspace_with_new_branch_using_post1) | **POST** /cc-ui/v1/coder/stack/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/new-branch | createWorkspaceWithNewBranch
[**get_all_using_get1**](UiCoderControllerApi.md#get_all_using_get1) | **GET** /cc-ui/v1/coder/stack/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/workspaces | getAll
[**get_all_using_get2**](UiCoderControllerApi.md#get_all_using_get2) | **GET** /cc-ui/v1/coder/stack/{stackName}/workspaces | getAll
[**identify_coder_launch_eligible_using_get**](UiCoderControllerApi.md#identify_coder_launch_eligible_using_get) | **GET** /cc-ui/v1/coder/stack/{stackName}/coder-eligibility | identifyCoderLaunchEligible

# **create_workspace_with_existing_branch_using_post**
> CoderWorkspaceResponse create_workspace_with_existing_branch_using_post(body, stack_name)

createWorkspaceWithExistingBranch

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
api_instance = swagger_client.UiCoderControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateWorkspaceExistingBranchRequest() # CreateWorkspaceExistingBranchRequest | createWorkspaceExistingBranchRequest
stack_name = 'stack_name_example' # str | stackName

try:
    # createWorkspaceWithExistingBranch
    api_response = api_instance.create_workspace_with_existing_branch_using_post(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCoderControllerApi->create_workspace_with_existing_branch_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWorkspaceExistingBranchRequest**](CreateWorkspaceExistingBranchRequest.md)| createWorkspaceExistingBranchRequest | 
 **stack_name** | **str**| stackName | 

### Return type

[**CoderWorkspaceResponse**](CoderWorkspaceResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace_with_existing_branch_using_post1**
> CoderWorkspaceResponse create_workspace_with_existing_branch_using_post1(body, resource_name, resource_type, stack_name)

createWorkspaceWithExistingBranch

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
api_instance = swagger_client.UiCoderControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateWorkspaceExistingBranchRequest() # CreateWorkspaceExistingBranchRequest | createWorkspaceExistingBranchRequest
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName

try:
    # createWorkspaceWithExistingBranch
    api_response = api_instance.create_workspace_with_existing_branch_using_post1(body, resource_name, resource_type, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCoderControllerApi->create_workspace_with_existing_branch_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWorkspaceExistingBranchRequest**](CreateWorkspaceExistingBranchRequest.md)| createWorkspaceExistingBranchRequest | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **stack_name** | **str**| stackName | 

### Return type

[**CoderWorkspaceResponse**](CoderWorkspaceResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace_with_new_branch_using_post**
> CoderWorkspaceResponse create_workspace_with_new_branch_using_post(body, stack_name)

createWorkspaceWithNewBranch

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
api_instance = swagger_client.UiCoderControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateWorkspaceNewBranchRequest() # CreateWorkspaceNewBranchRequest | createWorkspaceNewBranchRequest
stack_name = 'stack_name_example' # str | stackName

try:
    # createWorkspaceWithNewBranch
    api_response = api_instance.create_workspace_with_new_branch_using_post(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCoderControllerApi->create_workspace_with_new_branch_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWorkspaceNewBranchRequest**](CreateWorkspaceNewBranchRequest.md)| createWorkspaceNewBranchRequest | 
 **stack_name** | **str**| stackName | 

### Return type

[**CoderWorkspaceResponse**](CoderWorkspaceResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace_with_new_branch_using_post1**
> CoderWorkspaceResponse create_workspace_with_new_branch_using_post1(body, resource_name, resource_type, stack_name)

createWorkspaceWithNewBranch

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
api_instance = swagger_client.UiCoderControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateWorkspaceNewBranchRequest() # CreateWorkspaceNewBranchRequest | createWorkspaceNewBranchRequest
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName

try:
    # createWorkspaceWithNewBranch
    api_response = api_instance.create_workspace_with_new_branch_using_post1(body, resource_name, resource_type, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCoderControllerApi->create_workspace_with_new_branch_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWorkspaceNewBranchRequest**](CreateWorkspaceNewBranchRequest.md)| createWorkspaceNewBranchRequest | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **stack_name** | **str**| stackName | 

### Return type

[**CoderWorkspaceResponse**](CoderWorkspaceResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_using_get1**
> list[CoderWorkspaceResponse] get_all_using_get1(resource_name, resource_type, stack_name)

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
api_instance = swagger_client.UiCoderControllerApi(swagger_client.ApiClient(configuration))
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType
stack_name = 'stack_name_example' # str | stackName

try:
    # getAll
    api_response = api_instance.get_all_using_get1(resource_name, resource_type, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCoderControllerApi->get_all_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 
 **stack_name** | **str**| stackName | 

### Return type

[**list[CoderWorkspaceResponse]**](CoderWorkspaceResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_using_get2**
> list[CoderWorkspaceResponse] get_all_using_get2(stack_name)

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
api_instance = swagger_client.UiCoderControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # getAll
    api_response = api_instance.get_all_using_get2(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCoderControllerApi->get_all_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**list[CoderWorkspaceResponse]**](CoderWorkspaceResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identify_coder_launch_eligible_using_get**
> CoderLaunchEligibilityResponse identify_coder_launch_eligible_using_get(stack_name)

identifyCoderLaunchEligible

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
api_instance = swagger_client.UiCoderControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName

try:
    # identifyCoderLaunchEligible
    api_response = api_instance.identify_coder_launch_eligible_using_get(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCoderControllerApi->identify_coder_launch_eligible_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 

### Return type

[**CoderLaunchEligibilityResponse**](CoderLaunchEligibilityResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

