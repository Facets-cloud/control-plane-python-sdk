# swagger_client.CapillaryCloudCallbackControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**code_build_callback**](CapillaryCloudCallbackControllerApi.md#code_build_callback) | **POST** /cc/v1/callbacks/codebuild | 
[**dr_result_callback**](CapillaryCloudCallbackControllerApi.md#dr_result_callback) | **POST** /cc/v1/callbacks/{cluster}/dr/{moduleType}/{instanceName} | 

# **code_build_callback**
> bool code_build_callback(body)



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
api_instance = swagger_client.CapillaryCloudCallbackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoCodeBuildStatusCallback() # ComCapillaryOpsCpBoCodeBuildStatusCallback | 

try:
    api_response = api_instance.code_build_callback(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CapillaryCloudCallbackControllerApi->code_build_callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoCodeBuildStatusCallback**](ComCapillaryOpsCpBoCodeBuildStatusCallback.md)|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dr_result_callback**
> bool dr_result_callback(body, cluster, module_type, instance_name)



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
api_instance = swagger_client.CapillaryCloudCallbackControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoDRResult() # ComCapillaryOpsCpBoDRResult | 
cluster = 'cluster_example' # str | 
module_type = 'module_type_example' # str | 
instance_name = 'instance_name_example' # str | 

try:
    api_response = api_instance.dr_result_callback(body, cluster, module_type, instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CapillaryCloudCallbackControllerApi->dr_result_callback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoDRResult**](ComCapillaryOpsCpBoDRResult.md)|  | 
 **cluster** | **str**|  | 
 **module_type** | **str**|  | 
 **instance_name** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

