# swagger_client.ArtifactControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_artifact_using_post**](ArtifactControllerApi.md#register_artifact_using_post) | **POST** /cc/v1/artifacts/register | registerArtifact

# **register_artifact_using_post**
> register_artifact_using_post(body)

registerArtifact

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
api_instance = swagger_client.ArtifactControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Artifact() # Artifact | artifact

try:
    # registerArtifact
    api_instance.register_artifact_using_post(body)
except ApiException as e:
    print("Exception when calling ArtifactControllerApi->register_artifact_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Artifact**](Artifact.md)| artifact | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

