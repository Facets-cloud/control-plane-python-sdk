# swagger_client.UiThemeFileControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**save_theme_file**](UiThemeFileControllerApi.md#save_theme_file) | **POST** /cc-ui/v1/themeFile | 

# **save_theme_file**
> bool save_theme_file(body)



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
api_instance = swagger_client.UiThemeFileControllerApi(swagger_client.ApiClient(configuration))
body = 'body_example' # str | 

try:
    api_response = api_instance.save_theme_file(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiThemeFileControllerApi->save_theme_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

