# swagger_client.UiCoderControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workspace_with_existing_branch**](UiCoderControllerApi.md#create_workspace_with_existing_branch) | **POST** /cc-ui/v1/coder/stack/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/existing-branch | 
[**create_workspace_with_existing_branch1**](UiCoderControllerApi.md#create_workspace_with_existing_branch1) | **POST** /cc-ui/v1/coder/stack/{stackName}/existing-branch | 
[**create_workspace_with_new_branch**](UiCoderControllerApi.md#create_workspace_with_new_branch) | **POST** /cc-ui/v1/coder/stack/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/new-branch | 
[**create_workspace_with_new_branch1**](UiCoderControllerApi.md#create_workspace_with_new_branch1) | **POST** /cc-ui/v1/coder/stack/{stackName}/new-branch | 
[**get_all3**](UiCoderControllerApi.md#get_all3) | **GET** /cc-ui/v1/coder/stack/{stackName}/workspaces | 
[**get_all4**](UiCoderControllerApi.md#get_all4) | **GET** /cc-ui/v1/coder/stack/{stackName}/resourceType/{resourceType}/resourceName/{resourceName}/workspaces | 
[**identify_coder_launch_eligible**](UiCoderControllerApi.md#identify_coder_launch_eligible) | **GET** /cc-ui/v1/coder/stack/{stackName}/coder-eligibility | 

# **create_workspace_with_existing_branch**
> ComCapillaryOpsCpBoCoderCoderWorkspaceResponse create_workspace_with_existing_branch(body, stack_name, resource_type, resource_name)



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
api_instance = swagger_client.UiCoderControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoCoderCreateWorkspaceExistingBranchRequest() # ComCapillaryOpsCpBoCoderCreateWorkspaceExistingBranchRequest | 
stack_name = 'stack_name_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.create_workspace_with_existing_branch(body, stack_name, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCoderControllerApi->create_workspace_with_existing_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoCoderCreateWorkspaceExistingBranchRequest**](ComCapillaryOpsCpBoCoderCreateWorkspaceExistingBranchRequest.md)|  | 
 **stack_name** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoCoderCoderWorkspaceResponse**](ComCapillaryOpsCpBoCoderCoderWorkspaceResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace_with_existing_branch1**
> ComCapillaryOpsCpBoCoderCoderWorkspaceResponse create_workspace_with_existing_branch1(body, stack_name)



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
api_instance = swagger_client.UiCoderControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoCoderCreateWorkspaceExistingBranchRequest() # ComCapillaryOpsCpBoCoderCreateWorkspaceExistingBranchRequest | 
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.create_workspace_with_existing_branch1(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCoderControllerApi->create_workspace_with_existing_branch1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoCoderCreateWorkspaceExistingBranchRequest**](ComCapillaryOpsCpBoCoderCreateWorkspaceExistingBranchRequest.md)|  | 
 **stack_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoCoderCoderWorkspaceResponse**](ComCapillaryOpsCpBoCoderCoderWorkspaceResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace_with_new_branch**
> ComCapillaryOpsCpBoCoderCoderWorkspaceResponse create_workspace_with_new_branch(body, stack_name, resource_type, resource_name)



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
api_instance = swagger_client.UiCoderControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoCoderCreateWorkspaceNewBranchRequest() # ComCapillaryOpsCpBoCoderCreateWorkspaceNewBranchRequest | 
stack_name = 'stack_name_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.create_workspace_with_new_branch(body, stack_name, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCoderControllerApi->create_workspace_with_new_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoCoderCreateWorkspaceNewBranchRequest**](ComCapillaryOpsCpBoCoderCreateWorkspaceNewBranchRequest.md)|  | 
 **stack_name** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoCoderCoderWorkspaceResponse**](ComCapillaryOpsCpBoCoderCoderWorkspaceResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workspace_with_new_branch1**
> ComCapillaryOpsCpBoCoderCoderWorkspaceResponse create_workspace_with_new_branch1(body, stack_name)



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
api_instance = swagger_client.UiCoderControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoCoderCreateWorkspaceNewBranchRequest() # ComCapillaryOpsCpBoCoderCreateWorkspaceNewBranchRequest | 
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.create_workspace_with_new_branch1(body, stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCoderControllerApi->create_workspace_with_new_branch1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoCoderCreateWorkspaceNewBranchRequest**](ComCapillaryOpsCpBoCoderCreateWorkspaceNewBranchRequest.md)|  | 
 **stack_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoCoderCoderWorkspaceResponse**](ComCapillaryOpsCpBoCoderCoderWorkspaceResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all3**
> list[ComCapillaryOpsCpBoCoderCoderWorkspaceResponse] get_all3(stack_name)



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
api_instance = swagger_client.UiCoderControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.get_all3(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCoderControllerApi->get_all3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoCoderCoderWorkspaceResponse]**](ComCapillaryOpsCpBoCoderCoderWorkspaceResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all4**
> list[ComCapillaryOpsCpBoCoderCoderWorkspaceResponse] get_all4(stack_name, resource_type, resource_name)



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
api_instance = swagger_client.UiCoderControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.get_all4(stack_name, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCoderControllerApi->get_all4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoCoderCoderWorkspaceResponse]**](ComCapillaryOpsCpBoCoderCoderWorkspaceResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identify_coder_launch_eligible**
> ComCapillaryOpsCpBoCoderCoderLaunchEligibilityResponse identify_coder_launch_eligible(stack_name)



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
api_instance = swagger_client.UiCoderControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 

try:
    api_response = api_instance.identify_coder_launch_eligible(stack_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCoderControllerApi->identify_coder_launch_eligible: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoCoderCoderLaunchEligibilityResponse**](ComCapillaryOpsCpBoCoderCoderLaunchEligibilityResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

