# swagger_client.ArtifactoryControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ecr_artifactory**](ArtifactoryControllerApi.md#create_ecr_artifactory) | **POST** /cc/v1/artifactories | 
[**get_all_artifactories**](ArtifactoryControllerApi.md#get_all_artifactories) | **GET** /cc/v1/artifactories | 
[**update_ecr_artifactory**](ArtifactoryControllerApi.md#update_ecr_artifactory) | **PUT** /cc/v1/artifactories/{artifactoryId} | 

# **create_ecr_artifactory**
> ComCapillaryOpsCpBoECRArtifactory create_ecr_artifactory(body)



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
api_instance = swagger_client.ArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoECRArtifactory() # ComCapillaryOpsCpBoECRArtifactory | 

try:
    api_response = api_instance.create_ecr_artifactory(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactoryControllerApi->create_ecr_artifactory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoECRArtifactory**](ComCapillaryOpsCpBoECRArtifactory.md)|  | 

### Return type

[**ComCapillaryOpsCpBoECRArtifactory**](ComCapillaryOpsCpBoECRArtifactory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_artifactories**
> list[ComCapillaryOpsCpBoArtifactory] get_all_artifactories()



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
api_instance = swagger_client.ArtifactoryControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_artifactories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactoryControllerApi->get_all_artifactories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoArtifactory]**](ComCapillaryOpsCpBoArtifactory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ecr_artifactory**
> ComCapillaryOpsCpBoECRArtifactory update_ecr_artifactory(body, artifactory_id)



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
api_instance = swagger_client.ArtifactoryControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoECRArtifactory() # ComCapillaryOpsCpBoECRArtifactory | 
artifactory_id = 'artifactory_id_example' # str | 

try:
    api_response = api_instance.update_ecr_artifactory(body, artifactory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactoryControllerApi->update_ecr_artifactory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoECRArtifactory**](ComCapillaryOpsCpBoECRArtifactory.md)|  | 
 **artifactory_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoECRArtifactory**](ComCapillaryOpsCpBoECRArtifactory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

