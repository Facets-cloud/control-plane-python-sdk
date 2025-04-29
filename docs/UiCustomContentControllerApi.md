# swagger_client.UiCustomContentControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_content_file_using_post**](UiCustomContentControllerApi.md#create_content_file_using_post) | **POST** /cc-ui/v1/content/files | createContentFile
[**delete_content_file_using_delete**](UiCustomContentControllerApi.md#delete_content_file_using_delete) | **DELETE** /cc-ui/v1/content/files/{contentId} | deleteContentFile
[**get_content_files_by_selectors_using_get**](UiCustomContentControllerApi.md#get_content_files_by_selectors_using_get) | **GET** /cc-ui/v1/content/files/selectors/{contentType} | getContentFilesBySelectors
[**render_content_using_post**](UiCustomContentControllerApi.md#render_content_using_post) | **POST** /cc-ui/v1/content/files/{contentId}/render | renderContent
[**update_content_file_using_put**](UiCustomContentControllerApi.md#update_content_file_using_put) | **PUT** /cc-ui/v1/content/files/{contentId} | updateContentFile

# **create_content_file_using_post**
> ContentFile create_content_file_using_post(body)

createContentFile

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
api_instance = swagger_client.UiCustomContentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ContentFile() # ContentFile | contentFile

try:
    # createContentFile
    api_response = api_instance.create_content_file_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomContentControllerApi->create_content_file_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContentFile**](ContentFile.md)| contentFile | 

### Return type

[**ContentFile**](ContentFile.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_content_file_using_delete**
> delete_content_file_using_delete(content_id)

deleteContentFile

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
api_instance = swagger_client.UiCustomContentControllerApi(swagger_client.ApiClient(configuration))
content_id = 'content_id_example' # str | contentId

try:
    # deleteContentFile
    api_instance.delete_content_file_using_delete(content_id)
except ApiException as e:
    print("Exception when calling UiCustomContentControllerApi->delete_content_file_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | **str**| contentId | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_files_by_selectors_using_get**
> list[ContentFile] get_content_files_by_selectors_using_get(content_type, display_type=display_type, resource_name=resource_name, resource_type=resource_type, sub_type=sub_type)

getContentFilesBySelectors

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
api_instance = swagger_client.UiCustomContentControllerApi(swagger_client.ApiClient(configuration))
content_type = 'content_type_example' # str | contentType
display_type = 'display_type_example' # str | displayType (optional)
resource_name = 'resource_name_example' # str | resourceName (optional)
resource_type = 'resource_type_example' # str | resourceType (optional)
sub_type = 'sub_type_example' # str | subType (optional)

try:
    # getContentFilesBySelectors
    api_response = api_instance.get_content_files_by_selectors_using_get(content_type, display_type=display_type, resource_name=resource_name, resource_type=resource_type, sub_type=sub_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomContentControllerApi->get_content_files_by_selectors_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| contentType | 
 **display_type** | **str**| displayType | [optional] 
 **resource_name** | **str**| resourceName | [optional] 
 **resource_type** | **str**| resourceType | [optional] 
 **sub_type** | **str**| subType | [optional] 

### Return type

[**list[ContentFile]**](ContentFile.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_content_using_post**
> str render_content_using_post(body, content_id)

renderContent

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
api_instance = swagger_client.UiCustomContentControllerApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, str) | payload
content_id = 'content_id_example' # str | contentId

try:
    # renderContent
    api_response = api_instance.render_content_using_post(body, content_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomContentControllerApi->render_content_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, str)**](dict.md)| payload | 
 **content_id** | **str**| contentId | 

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_content_file_using_put**
> ContentFile update_content_file_using_put(body, content_id)

updateContentFile

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
api_instance = swagger_client.UiCustomContentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ContentFile() # ContentFile | updatedContent
content_id = 'content_id_example' # str | contentId

try:
    # updateContentFile
    api_response = api_instance.update_content_file_using_put(body, content_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomContentControllerApi->update_content_file_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContentFile**](ContentFile.md)| updatedContent | 
 **content_id** | **str**| contentId | 

### Return type

[**ContentFile**](ContentFile.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

