# swagger_client.BuildControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_image_from_deployer**](BuildControllerApi.md#get_image_from_deployer) | **GET** /cc/v1/build/deployer/{applicationId} | 

# **get_image_from_deployer**
> ComCapillaryOpsDeployerBoBuild get_image_from_deployer(application_id, strategy, release_type=release_type)



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
api_instance = swagger_client.BuildControllerApi(swagger_client.ApiClient(configuration))
application_id = 'application_id_example' # str | 
strategy = 'strategy_example' # str | 
release_type = 'RELEASE' # str |  (optional) (default to RELEASE)

try:
    api_response = api_instance.get_image_from_deployer(application_id, strategy, release_type=release_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildControllerApi->get_image_from_deployer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **strategy** | **str**|  | 
 **release_type** | **str**|  | [optional] [default to RELEASE]

### Return type

[**ComCapillaryOpsDeployerBoBuild**](ComCapillaryOpsDeployerBoBuild.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

