# swagger_client.CapillaryCloudCallbackControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**code_build_callback_using_post**](CapillaryCloudCallbackControllerApi.md#code_build_callback_using_post) | **POST** /cc/v1/callbacks/codebuild | codeBuildCallback
[**dr_result_callback_using_post**](CapillaryCloudCallbackControllerApi.md#dr_result_callback_using_post) | **POST** /cc/v1/callbacks/{cluster}/dr/{moduleType}/{instanceName} | drResultCallback

# **code_build_callback_using_post**
> bool code_build_callback_using_post(body)

codeBuildCallback

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
api_instance = swagger_client.CapillaryCloudCallbackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CodeBuildStatusCallback() # CodeBuildStatusCallback | callback

try:
    # codeBuildCallback
    api_response = api_instance.code_build_callback_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CapillaryCloudCallbackControllerApi->code_build_callback_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CodeBuildStatusCallback**](CodeBuildStatusCallback.md)| callback | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dr_result_callback_using_post**
> bool dr_result_callback_using_post(body, cluster, instance_name, module_type)

drResultCallback

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
api_instance = swagger_client.CapillaryCloudCallbackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.DRResult() # DRResult | callback
cluster = 'cluster_example' # str | cluster
instance_name = 'instance_name_example' # str | instanceName
module_type = 'module_type_example' # str | moduleType

try:
    # drResultCallback
    api_response = api_instance.dr_result_callback_using_post(body, cluster, instance_name, module_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CapillaryCloudCallbackControllerApi->dr_result_callback_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DRResult**](DRResult.md)| callback | 
 **cluster** | **str**| cluster | 
 **instance_name** | **str**| instanceName | 
 **module_type** | **str**| moduleType | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

