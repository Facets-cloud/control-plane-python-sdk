# swagger_client.UiAuditLogsControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_logs**](UiAuditLogsControllerApi.md#get_audit_logs) | **GET** /cc-ui/v1/audit-logs | 

# **get_audit_logs**
> OrgSpringframeworkDataDomainPageComCapillaryOpsCpBoAuditFacetsAuditLogResponse get_audit_logs(start, end=end, number=number, size=size, stack_name=stack_name, cluster_name=cluster_name, target=target, performed_by=performed_by, entity=entity, entity_action=entity_action)



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
api_instance = swagger_client.UiAuditLogsControllerApi(swagger_client.ApiClient(configuration))
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
number = 0 # int |  (optional) (default to 0)
size = 50 # int |  (optional) (default to 50)
stack_name = 'stack_name_example' # str | Regex based string match (optional)
cluster_name = 'cluster_name_example' # str | Regex based string match (optional)
target = 'target_example' # str | Regex based string match (optional)
performed_by = 'performed_by_example' # str | Regex based string match (optional)
entity = ['entity_example'] # list[str] |  (optional)
entity_action = ['entity_action_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_audit_logs(start, end=end, number=number, size=size, stack_name=stack_name, cluster_name=cluster_name, target=target, performed_by=performed_by, entity=entity, entity_action=entity_action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAuditLogsControllerApi->get_audit_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**|  | 
 **end** | **datetime**|  | [optional] 
 **number** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 50]
 **stack_name** | **str**| Regex based string match | [optional] 
 **cluster_name** | **str**| Regex based string match | [optional] 
 **target** | **str**| Regex based string match | [optional] 
 **performed_by** | **str**| Regex based string match | [optional] 
 **entity** | [**list[str]**](str.md)|  | [optional] 
 **entity_action** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**OrgSpringframeworkDataDomainPageComCapillaryOpsCpBoAuditFacetsAuditLogResponse**](OrgSpringframeworkDataDomainPageComCapillaryOpsCpBoAuditFacetsAuditLogResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

