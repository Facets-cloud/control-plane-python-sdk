# swagger_client.ArtifactoryControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ecr_artifactory_using_post**](ArtifactoryControllerApi.md#create_ecr_artifactory_using_post) | **POST** /cc/v1/artifactories | createECRArtifactory
[**get_all_artifactories_using_get**](ArtifactoryControllerApi.md#get_all_artifactories_using_get) | **GET** /cc/v1/artifactories | getAllArtifactories
[**update_ecr_artifactory_using_put**](ArtifactoryControllerApi.md#update_ecr_artifactory_using_put) | **PUT** /cc/v1/artifactories/{artifactoryId} | updateECRArtifactory


# **create_ecr_artifactory_using_post**
> ECRArtifactory create_ecr_artifactory_using_post(ecr_artifactory)

createECRArtifactory

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
api_instance = swagger_client.ArtifactoryControllerApi(swagger_client.ApiClient(configuration))
ecr_artifactory = swagger_client.ECRArtifactory() # ECRArtifactory | ecrArtifactory

try:
    # createECRArtifactory
    api_response = api_instance.create_ecr_artifactory_using_post(ecr_artifactory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactoryControllerApi->create_ecr_artifactory_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ecr_artifactory** | [**ECRArtifactory**](ECRArtifactory.md)| ecrArtifactory | 

### Return type

[**ECRArtifactory**](ECRArtifactory.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_artifactories_using_get**
> list[Artifactory] get_all_artifactories_using_get()

getAllArtifactories

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
api_instance = swagger_client.ArtifactoryControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllArtifactories
    api_response = api_instance.get_all_artifactories_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactoryControllerApi->get_all_artifactories_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Artifactory]**](Artifactory.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ecr_artifactory_using_put**
> ECRArtifactory update_ecr_artifactory_using_put(artifactory_id, ecr_artifactory)

updateECRArtifactory

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
api_instance = swagger_client.ArtifactoryControllerApi(swagger_client.ApiClient(configuration))
artifactory_id = 'artifactory_id_example' # str | artifactoryId
ecr_artifactory = swagger_client.ECRArtifactory() # ECRArtifactory | ecrArtifactory

try:
    # updateECRArtifactory
    api_response = api_instance.update_ecr_artifactory_using_put(artifactory_id, ecr_artifactory)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactoryControllerApi->update_ecr_artifactory_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifactory_id** | **str**| artifactoryId | 
 **ecr_artifactory** | [**ECRArtifactory**](ECRArtifactory.md)| ecrArtifactory | 

### Return type

[**ECRArtifactory**](ECRArtifactory.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

