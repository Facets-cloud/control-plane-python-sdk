# swagger_client.UiAuditLogsControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_logs_using_get**](UiAuditLogsControllerApi.md#get_audit_logs_using_get) | **GET** /cc-ui/v1/audit-logs | getAuditLogs

# **get_audit_logs_using_get**
> PageFacetsAuditLogResponse get_audit_logs_using_get(cluster_name=cluster_name, end=end, entity=entity, entity_action=entity_action, number=number, performed_by=performed_by, size=size, stack_name=stack_name, start=start, target=target)

getAuditLogs

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
api_instance = swagger_client.UiAuditLogsControllerApi(swagger_client.ApiClient(configuration))
cluster_name = 'cluster_name_example' # str | Regex based string match (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | end (optional)
entity = ['entity_example'] # list[str] | entity (optional)
entity_action = ['entity_action_example'] # list[str] | entityAction (optional)
number = 0 # int | number (optional) (default to 0)
performed_by = 'performed_by_example' # str | Regex based string match (optional)
size = 50 # int | size (optional) (default to 50)
stack_name = 'stack_name_example' # str | Regex based string match (optional)
start = '2013-10-20T19:20:30+01:00' # datetime | start (optional)
target = 'target_example' # str | Regex based string match (optional)

try:
    # getAuditLogs
    api_response = api_instance.get_audit_logs_using_get(cluster_name=cluster_name, end=end, entity=entity, entity_action=entity_action, number=number, performed_by=performed_by, size=size, stack_name=stack_name, start=start, target=target)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAuditLogsControllerApi->get_audit_logs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Regex based string match | [optional] 
 **end** | **datetime**| end | [optional] 
 **entity** | [**list[str]**](str.md)| entity | [optional] 
 **entity_action** | [**list[str]**](str.md)| entityAction | [optional] 
 **number** | **int**| number | [optional] [default to 0]
 **performed_by** | **str**| Regex based string match | [optional] 
 **size** | **int**| size | [optional] [default to 50]
 **stack_name** | **str**| Regex based string match | [optional] 
 **start** | **datetime**| start | [optional] 
 **target** | **str**| Regex based string match | [optional] 

### Return type

[**PageFacetsAuditLogResponse**](PageFacetsAuditLogResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

