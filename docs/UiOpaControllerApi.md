# swagger_client.UiOpaControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_edit_opa_policy_state**](UiOpaControllerApi.md#bulk_edit_opa_policy_state) | **POST** /cc-ui/v1/opa/enable-disable-policies | 
[**create_policy**](UiOpaControllerApi.md#create_policy) | **POST** /cc-ui/v1/opa/{policyName} | 
[**delete_policy**](UiOpaControllerApi.md#delete_policy) | **DELETE** /cc-ui/v1/opa/{policyName} | 
[**edit_policy**](UiOpaControllerApi.md#edit_policy) | **PUT** /cc-ui/v1/opa/{policyName} | 
[**execute_policy**](UiOpaControllerApi.md#execute_policy) | **POST** /cc-ui/v1/opa/{policyName}/execute | 
[**get_all_policies**](UiOpaControllerApi.md#get_all_policies) | **GET** /cc-ui/v1/opa | 
[**get_all_policy_templates**](UiOpaControllerApi.md#get_all_policy_templates) | **GET** /cc-ui/v1/opa/policy-templates | 
[**get_policy**](UiOpaControllerApi.md#get_policy) | **GET** /cc-ui/v1/opa/{policyName} | 

# **bulk_edit_opa_policy_state**
> bulk_edit_opa_policy_state(body)



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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.EnableDisableOPAPolicy()] # list[EnableDisableOPAPolicy] | 

try:
    api_instance.bulk_edit_opa_policy_state(body)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->bulk_edit_opa_policy_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[EnableDisableOPAPolicy]**](EnableDisableOPAPolicy.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_policy**
> OpaPolicy create_policy(body, policy_name)



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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.OpaPolicyRequest() # OpaPolicyRequest | 
policy_name = 'policy_name_example' # str | 

try:
    api_response = api_instance.create_policy(body, policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpaPolicyRequest**](OpaPolicyRequest.md)|  | 
 **policy_name** | **str**|  | 

### Return type

[**OpaPolicy**](OpaPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(policy_name)



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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))
policy_name = 'policy_name_example' # str | 

try:
    api_instance.delete_policy(policy_name)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_policy**
> OpaPolicy edit_policy(body, policy_name)



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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.OpaPolicyRequest() # OpaPolicyRequest | 
policy_name = 'policy_name_example' # str | 

try:
    api_response = api_instance.edit_policy(body, policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->edit_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpaPolicyRequest**](OpaPolicyRequest.md)|  | 
 **policy_name** | **str**|  | 

### Return type

[**OpaPolicy**](OpaPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_policy**
> OpaPolicyExecutionResult execute_policy(body, policy_name)



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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str | 
policy_name = 'policy_name_example' # str | 

try:
    api_response = api_instance.execute_policy(body, policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->execute_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **policy_name** | **str**|  | 

### Return type

[**OpaPolicyExecutionResult**](OpaPolicyExecutionResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_policies**
> list[OpaPolicy] get_all_policies()



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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->get_all_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OpaPolicy]**](OpaPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_policy_templates**
> list[PolicyTemplateDTO] get_all_policy_templates()



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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_policy_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->get_all_policy_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PolicyTemplateDTO]**](PolicyTemplateDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> OpaPolicy get_policy(policy_name)



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
api_instance = swagger_client.UiOpaControllerApi(swagger_client.ApiClient(configuration))
policy_name = 'policy_name_example' # str | 

try:
    api_response = api_instance.get_policy(policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiOpaControllerApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**|  | 

### Return type

[**OpaPolicy**](OpaPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

