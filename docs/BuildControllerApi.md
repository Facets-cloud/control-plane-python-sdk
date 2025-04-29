# swagger_client.BuildControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_image_from_deployer_using_get**](BuildControllerApi.md#get_image_from_deployer_using_get) | **GET** /cc/v1/build/deployer/{applicationId} | getImageFromDeployer

# **get_image_from_deployer_using_get**
> Build get_image_from_deployer_using_get(application_id, strategy, release_type=release_type)

getImageFromDeployer

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
api_instance = swagger_client.BuildControllerApi(swagger_client.ApiClient(configuration))
application_id = 'application_id_example' # str | applicationId
strategy = 'strategy_example' # str | strategy
release_type = 'RELEASE' # str | releaseType (optional) (default to RELEASE)

try:
    # getImageFromDeployer
    api_response = api_instance.get_image_from_deployer_using_get(application_id, strategy, release_type=release_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildControllerApi->get_image_from_deployer_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| applicationId | 
 **strategy** | **str**| strategy | 
 **release_type** | **str**| releaseType | [optional] [default to RELEASE]

### Return type

[**Build**](Build.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

