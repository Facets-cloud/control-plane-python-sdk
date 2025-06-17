# swagger_client.UiCustomContentControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_content_file**](UiCustomContentControllerApi.md#create_content_file) | **POST** /cc-ui/v1/content/files | 
[**delete_content_file**](UiCustomContentControllerApi.md#delete_content_file) | **DELETE** /cc-ui/v1/content/files/{contentId} | 
[**get_content_files_by_selectors**](UiCustomContentControllerApi.md#get_content_files_by_selectors) | **GET** /cc-ui/v1/content/files/selectors/{contentType} | 
[**render_content**](UiCustomContentControllerApi.md#render_content) | **POST** /cc-ui/v1/content/files/{contentId}/render | 
[**update_content_file**](UiCustomContentControllerApi.md#update_content_file) | **PUT** /cc-ui/v1/content/files/{contentId} | 

# **create_content_file**
> ContentFile create_content_file(body)



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
api_instance = swagger_client.UiCustomContentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ContentFile() # ContentFile | 

try:
    api_response = api_instance.create_content_file(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomContentControllerApi->create_content_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContentFile**](ContentFile.md)|  | 

### Return type

[**ContentFile**](ContentFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_content_file**
> delete_content_file(content_id)



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
api_instance = swagger_client.UiCustomContentControllerApi(swagger_client.ApiClient(configuration))
content_id = 'content_id_example' # str | 

try:
    api_instance.delete_content_file(content_id)
except ApiException as e:
    print("Exception when calling UiCustomContentControllerApi->delete_content_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_files_by_selectors**
> list[ContentFile] get_content_files_by_selectors(content_type, resource_type=resource_type, resource_name=resource_name, display_type=display_type, sub_type=sub_type)



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
api_instance = swagger_client.UiCustomContentControllerApi(swagger_client.ApiClient(configuration))
content_type = 'content_type_example' # str | 
resource_type = 'resource_type_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)
display_type = 'display_type_example' # str |  (optional)
sub_type = 'sub_type_example' # str |  (optional)

try:
    api_response = api_instance.get_content_files_by_selectors(content_type, resource_type=resource_type, resource_name=resource_name, display_type=display_type, sub_type=sub_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomContentControllerApi->get_content_files_by_selectors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | 
 **resource_type** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 
 **display_type** | **str**|  | [optional] 
 **sub_type** | **str**|  | [optional] 

### Return type

[**list[ContentFile]**](ContentFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **render_content**
> str render_content(body, content_id)



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
api_instance = swagger_client.UiCustomContentControllerApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, str) | 
content_id = 'content_id_example' # str | 

try:
    api_response = api_instance.render_content(body, content_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomContentControllerApi->render_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, str)**](dict.md)|  | 
 **content_id** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_content_file**
> ContentFile update_content_file(body, content_id)



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
api_instance = swagger_client.UiCustomContentControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ContentFile() # ContentFile | 
content_id = 'content_id_example' # str | 

try:
    api_response = api_instance.update_content_file(body, content_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiCustomContentControllerApi->update_content_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContentFile**](ContentFile.md)|  | 
 **content_id** | **str**|  | 

### Return type

[**ContentFile**](ContentFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

