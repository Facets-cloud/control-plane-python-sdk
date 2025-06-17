# swagger_client.UiArtifactRoutingRuleControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_artifact_routing_rule**](UiArtifactRoutingRuleControllerApi.md#add_artifact_routing_rule) | **POST** /cc-ui/v1/artifact-routing-rule | 
[**delete_artifact_routing_rule**](UiArtifactRoutingRuleControllerApi.md#delete_artifact_routing_rule) | **DELETE** /cc-ui/v1/artifact-routing-rule/{ruleId} | 
[**get_all_artifact_routing_rules**](UiArtifactRoutingRuleControllerApi.md#get_all_artifact_routing_rules) | **GET** /cc-ui/v1/artifact-routing-rule | 
[**get_all_operators**](UiArtifactRoutingRuleControllerApi.md#get_all_operators) | **GET** /cc-ui/v1/artifact-routing-rule/operators | 
[**get_artifact_routing_rule**](UiArtifactRoutingRuleControllerApi.md#get_artifact_routing_rule) | **GET** /cc-ui/v1/artifact-routing-rule/{ruleId} | 
[**test_rule_for_branch_name**](UiArtifactRoutingRuleControllerApi.md#test_rule_for_branch_name) | **POST** /cc-ui/v1/artifact-routing-rule/test | 
[**update_artifact_routing_rule**](UiArtifactRoutingRuleControllerApi.md#update_artifact_routing_rule) | **PUT** /cc-ui/v1/artifact-routing-rule | 

# **add_artifact_routing_rule**
> ArtifactRoutingRuleResponse add_artifact_routing_rule(body)



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
api_instance = swagger_client.UiArtifactRoutingRuleControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactRoutingRuleRequest() # ArtifactRoutingRuleRequest | 

try:
    api_response = api_instance.add_artifact_routing_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactRoutingRuleControllerApi->add_artifact_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactRoutingRuleRequest**](ArtifactRoutingRuleRequest.md)|  | 

### Return type

[**ArtifactRoutingRuleResponse**](ArtifactRoutingRuleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact_routing_rule**
> delete_artifact_routing_rule(rule_id)



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
api_instance = swagger_client.UiArtifactRoutingRuleControllerApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | 

try:
    api_instance.delete_artifact_routing_rule(rule_id)
except ApiException as e:
    print("Exception when calling UiArtifactRoutingRuleControllerApi->delete_artifact_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_artifact_routing_rules**
> list[ArtifactRoutingRuleResponse] get_all_artifact_routing_rules(stack_name, registration_type=registration_type)



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
api_instance = swagger_client.UiArtifactRoutingRuleControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | 
registration_type = 'registration_type_example' # str |  (optional)

try:
    api_response = api_instance.get_all_artifact_routing_rules(stack_name, registration_type=registration_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactRoutingRuleControllerApi->get_all_artifact_routing_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**|  | 
 **registration_type** | **str**|  | [optional] 

### Return type

[**list[ArtifactRoutingRuleResponse]**](ArtifactRoutingRuleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_operators**
> list[str] get_all_operators()



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
api_instance = swagger_client.UiArtifactRoutingRuleControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_operators()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactRoutingRuleControllerApi->get_all_operators: %s\n" % e)
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

# **get_artifact_routing_rule**
> ArtifactRoutingRuleResponse get_artifact_routing_rule(rule_id)



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
api_instance = swagger_client.UiArtifactRoutingRuleControllerApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | 

try:
    api_response = api_instance.get_artifact_routing_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactRoutingRuleControllerApi->get_artifact_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

[**ArtifactRoutingRuleResponse**](ArtifactRoutingRuleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_rule_for_branch_name**
> TestRuleResponse test_rule_for_branch_name(body, metadata)



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
api_instance = swagger_client.UiArtifactRoutingRuleControllerApi(swagger_client.ApiClient(configuration))
body = [swagger_client.Criterion()] # list[Criterion] | 
metadata = {'key': 'metadata_example'} # dict(str, str) | 

try:
    api_response = api_instance.test_rule_for_branch_name(body, metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactRoutingRuleControllerApi->test_rule_for_branch_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Criterion]**](Criterion.md)|  | 
 **metadata** | [**dict(str, str)**](str.md)|  | 

### Return type

[**TestRuleResponse**](TestRuleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_artifact_routing_rule**
> ArtifactRoutingRuleResponse update_artifact_routing_rule(body)



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
api_instance = swagger_client.UiArtifactRoutingRuleControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArtifactRoutingRuleRequest() # ArtifactRoutingRuleRequest | 

try:
    api_response = api_instance.update_artifact_routing_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactRoutingRuleControllerApi->update_artifact_routing_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtifactRoutingRuleRequest**](ArtifactRoutingRuleRequest.md)|  | 

### Return type

[**ArtifactRoutingRuleResponse**](ArtifactRoutingRuleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

