# swagger_client.UiArtifactRoutingRuleControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_artifact_routing_rule_using_post**](UiArtifactRoutingRuleControllerApi.md#add_artifact_routing_rule_using_post) | **POST** /cc-ui/v1/artifact-routing-rule | addArtifactRoutingRule
[**delete_artifact_routing_rule_using_delete**](UiArtifactRoutingRuleControllerApi.md#delete_artifact_routing_rule_using_delete) | **DELETE** /cc-ui/v1/artifact-routing-rule/{ruleId} | deleteArtifactRoutingRule
[**get_all_artifact_routing_rules_using_get**](UiArtifactRoutingRuleControllerApi.md#get_all_artifact_routing_rules_using_get) | **GET** /cc-ui/v1/artifact-routing-rule | getAllArtifactRoutingRules
[**get_all_operators_using_get**](UiArtifactRoutingRuleControllerApi.md#get_all_operators_using_get) | **GET** /cc-ui/v1/artifact-routing-rule/operators | getAllOperators
[**get_artifact_routing_rule_using_get**](UiArtifactRoutingRuleControllerApi.md#get_artifact_routing_rule_using_get) | **GET** /cc-ui/v1/artifact-routing-rule/{ruleId} | getArtifactRoutingRule
[**test_rule_for_branch_name_using_post**](UiArtifactRoutingRuleControllerApi.md#test_rule_for_branch_name_using_post) | **POST** /cc-ui/v1/artifact-routing-rule/test | testRuleForBranchName
[**update_artifact_routing_rule_using_put**](UiArtifactRoutingRuleControllerApi.md#update_artifact_routing_rule_using_put) | **PUT** /cc-ui/v1/artifact-routing-rule | updateArtifactRoutingRule


# **add_artifact_routing_rule_using_post**
> ArtifactRoutingRuleResponse add_artifact_routing_rule_using_post(artifact_routing_rule_request)

addArtifactRoutingRule

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
api_instance = swagger_client.UiArtifactRoutingRuleControllerApi(swagger_client.ApiClient(configuration))
artifact_routing_rule_request = swagger_client.ArtifactRoutingRuleRequest() # ArtifactRoutingRuleRequest | artifactRoutingRuleRequest

try:
    # addArtifactRoutingRule
    api_response = api_instance.add_artifact_routing_rule_using_post(artifact_routing_rule_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactRoutingRuleControllerApi->add_artifact_routing_rule_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_routing_rule_request** | [**ArtifactRoutingRuleRequest**](ArtifactRoutingRuleRequest.md)| artifactRoutingRuleRequest | 

### Return type

[**ArtifactRoutingRuleResponse**](ArtifactRoutingRuleResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact_routing_rule_using_delete**
> delete_artifact_routing_rule_using_delete(rule_id)

deleteArtifactRoutingRule

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
api_instance = swagger_client.UiArtifactRoutingRuleControllerApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | ruleId

try:
    # deleteArtifactRoutingRule
    api_instance.delete_artifact_routing_rule_using_delete(rule_id)
except ApiException as e:
    print("Exception when calling UiArtifactRoutingRuleControllerApi->delete_artifact_routing_rule_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| ruleId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_artifact_routing_rules_using_get**
> list[ArtifactRoutingRuleResponse] get_all_artifact_routing_rules_using_get(stack_name, registration_type=registration_type)

getAllArtifactRoutingRules

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
api_instance = swagger_client.UiArtifactRoutingRuleControllerApi(swagger_client.ApiClient(configuration))
stack_name = 'stack_name_example' # str | stackName
registration_type = 'registration_type_example' # str | registrationType (optional)

try:
    # getAllArtifactRoutingRules
    api_response = api_instance.get_all_artifact_routing_rules_using_get(stack_name, registration_type=registration_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactRoutingRuleControllerApi->get_all_artifact_routing_rules_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_name** | **str**| stackName | 
 **registration_type** | **str**| registrationType | [optional] 

### Return type

[**list[ArtifactRoutingRuleResponse]**](ArtifactRoutingRuleResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_operators_using_get**
> list[str] get_all_operators_using_get()

getAllOperators

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
api_instance = swagger_client.UiArtifactRoutingRuleControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllOperators
    api_response = api_instance.get_all_operators_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactRoutingRuleControllerApi->get_all_operators_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_routing_rule_using_get**
> ArtifactRoutingRuleResponse get_artifact_routing_rule_using_get(rule_id)

getArtifactRoutingRule

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
api_instance = swagger_client.UiArtifactRoutingRuleControllerApi(swagger_client.ApiClient(configuration))
rule_id = 'rule_id_example' # str | ruleId

try:
    # getArtifactRoutingRule
    api_response = api_instance.get_artifact_routing_rule_using_get(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactRoutingRuleControllerApi->get_artifact_routing_rule_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| ruleId | 

### Return type

[**ArtifactRoutingRuleResponse**](ArtifactRoutingRuleResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_rule_for_branch_name_using_post**
> TestRuleResponse test_rule_for_branch_name_using_post(criteria, metadata)

testRuleForBranchName

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
api_instance = swagger_client.UiArtifactRoutingRuleControllerApi(swagger_client.ApiClient(configuration))
criteria = [swagger_client.Criterion()] # list[Criterion] | criteria
metadata = NULL # object | metadata

try:
    # testRuleForBranchName
    api_response = api_instance.test_rule_for_branch_name_using_post(criteria, metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactRoutingRuleControllerApi->test_rule_for_branch_name_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **criteria** | [**list[Criterion]**](Criterion.md)| criteria | 
 **metadata** | [**object**](.md)| metadata | 

### Return type

[**TestRuleResponse**](TestRuleResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_artifact_routing_rule_using_put**
> ArtifactRoutingRuleResponse update_artifact_routing_rule_using_put(artifact_routing_rule_request)

updateArtifactRoutingRule

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
api_instance = swagger_client.UiArtifactRoutingRuleControllerApi(swagger_client.ApiClient(configuration))
artifact_routing_rule_request = swagger_client.ArtifactRoutingRuleRequest() # ArtifactRoutingRuleRequest | artifactRoutingRuleRequest

try:
    # updateArtifactRoutingRule
    api_response = api_instance.update_artifact_routing_rule_using_put(artifact_routing_rule_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiArtifactRoutingRuleControllerApi->update_artifact_routing_rule_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_routing_rule_request** | [**ArtifactRoutingRuleRequest**](ArtifactRoutingRuleRequest.md)| artifactRoutingRuleRequest | 

### Return type

[**ArtifactRoutingRuleResponse**](ArtifactRoutingRuleResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

