# swagger_client.UiOpaControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_edit_opa_policy_state_using_post**](UiOpaControllerApi.md#bulk_edit_opa_policy_state_using_post) | **POST** /cc-ui/v1/opa/enable-disable-policies | bulkEditOpaPolicyState
[**create_policy_using_post**](UiOpaControllerApi.md#create_policy_using_post) | **POST** /cc-ui/v1/opa/{policyName} | createPolicy
[**delete_policy_using_delete**](UiOpaControllerApi.md#delete_policy_using_delete) | **DELETE** /cc-ui/v1/opa/{policyName} | deletePolicy
[**edit_policy_using_put**](UiOpaControllerApi.md#edit_policy_using_put) | **PUT** /cc-ui/v1/opa/{policyName} | editPolicy
[**execute_policy_using_post**](UiOpaControllerApi.md#execute_policy_using_post) | **POST** /cc-ui/v1/opa/{policyName}/execute | executePolicy
[**get_all_policies_using_get**](UiOpaControllerApi.md#get_all_policies_using_get) | **GET** /cc-ui/v1/opa | getAllPolicies
[**get_all_policy_templates_using_get**](UiOpaControllerApi.md#get_all_policy_templates_using_get) | **GET** /cc-ui/v1/opa/policy-templates | getAllPolicyTemplates
[**get_policy_using_get**](UiOpaControllerApi.md#get_policy_using_get) | **GET** /cc-ui/v1/opa/{policyName} | getPolicy

# **bulk_edit_opa_policy_state_using_post**
> bulk_edit_opa_policy_state_using_post(body)

bulkEditOpaPolicyState

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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.EnableDisableOPAPolicy()] # list[EnableDisableOPAPolicy] | enableDisableOPAPoliciesList

try:
    # bulkEditOpaPolicyState
    api_instance.bulk_edit_opa_policy_state_using_post(body)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->bulk_edit_opa_policy_state_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[EnableDisableOPAPolicy]**](EnableDisableOPAPolicy.md)| enableDisableOPAPoliciesList | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy_using_post**
> OpaPolicy create_policy_using_post(body, policy_name)

createPolicy

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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.OpaPolicyRequest() # OpaPolicyRequest | opaRequest
policy_name = 'policy_name_example' # str | policyName

try:
    # createPolicy
    api_response = api_instance.create_policy_using_post(body, policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->create_policy_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpaPolicyRequest**](OpaPolicyRequest.md)| opaRequest | 
 **policy_name** | **str**| policyName | 

### Return type

[**OpaPolicy**](OpaPolicy.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_using_delete**
> delete_policy_using_delete(policy_name)

deletePolicy

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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))
policy_name = 'policy_name_example' # str | policyName

try:
    # deletePolicy
    api_instance.delete_policy_using_delete(policy_name)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->delete_policy_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| policyName | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_policy_using_put**
> OpaPolicy edit_policy_using_put(body, policy_name)

editPolicy

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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.OpaPolicyRequest() # OpaPolicyRequest | opaRequest
policy_name = 'policy_name_example' # str | policyName

try:
    # editPolicy
    api_response = api_instance.edit_policy_using_put(body, policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->edit_policy_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpaPolicyRequest**](OpaPolicyRequest.md)| opaRequest | 
 **policy_name** | **str**| policyName | 

### Return type

[**OpaPolicy**](OpaPolicy.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_policy_using_post**
> OpaPolicyExecutionResult execute_policy_using_post(body, policy_name)

executePolicy

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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str | inputJson
policy_name = 'policy_name_example' # str | policyName

try:
    # executePolicy
    api_response = api_instance.execute_policy_using_post(body, policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->execute_policy_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| inputJson | 
 **policy_name** | **str**| policyName | 

### Return type

[**OpaPolicyExecutionResult**](OpaPolicyExecutionResult.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_policies_using_get**
> list[OpaPolicy] get_all_policies_using_get()

getAllPolicies

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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllPolicies
    api_response = api_instance.get_all_policies_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->get_all_policies_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OpaPolicy]**](OpaPolicy.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_policy_templates_using_get**
> list[PolicyTemplateDTO] get_all_policy_templates_using_get()

getAllPolicyTemplates

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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllPolicyTemplates
    api_response = api_instance.get_all_policy_templates_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->get_all_policy_templates_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PolicyTemplateDTO]**](PolicyTemplateDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_using_get**
> OpaPolicy get_policy_using_get(policy_name)

getPolicy

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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))
policy_name = 'policy_name_example' # str | policyName

try:
    # getPolicy
    api_response = api_instance.get_policy_using_get(policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->get_policy_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| policyName | 

### Return type

[**OpaPolicy**](OpaPolicy.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

