# swagger_client.UiThemeFileControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**save_theme_file_using_post**](UiThemeFileControllerApi.md#save_theme_file_using_post) | **POST** /cc-ui/v1/themeFile | saveThemeFile


# **save_theme_file_using_post**
> bool save_theme_file_using_post(theme_file_content)

saveThemeFile

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
api_instance = swagger_client.UiThemeFileControllerApi(swagger_client.ApiClient(configuration))
theme_file_content = 'theme_file_content_example' # str | themeFileContent

try:
    # saveThemeFile
    api_response = api_instance.save_theme_file_using_post(theme_file_content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiThemeFileControllerApi->save_theme_file_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **theme_file_content** | **str**| themeFileContent | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

