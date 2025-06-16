# swagger_client.UiUserVcsTokenControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add**](UiUserVcsTokenControllerApi.md#add) | **POST** /cc-ui/v1/user-token | 
[**delete**](UiUserVcsTokenControllerApi.md#delete) | **DELETE** /cc-ui/v1/user-token/{id} | 
[**get_all**](UiUserVcsTokenControllerApi.md#get_all) | **GET** /cc-ui/v1/user-token | 
[**update**](UiUserVcsTokenControllerApi.md#update) | **PUT** /cc-ui/v1/user-token | 

# **add**
> ComCapillaryOpsCpBoUserUserVCSTokenResponse add(body)



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
api_instance = swagger_client.UiUserVcsTokenControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoUserUserVCSTokenRequest() # ComCapillaryOpsCpBoUserUserVCSTokenRequest | 

try:
    api_response = api_instance.add(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserVcsTokenControllerApi->add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoUserUserVCSTokenRequest**](ComCapillaryOpsCpBoUserUserVCSTokenRequest.md)|  | 

### Return type

[**ComCapillaryOpsCpBoUserUserVCSTokenResponse**](ComCapillaryOpsCpBoUserUserVCSTokenResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(id)



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
api_instance = swagger_client.UiUserVcsTokenControllerApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.delete(id)
except ApiException as e:
    print("Exception when calling UiUserVcsTokenControllerApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> list[ComCapillaryOpsCpBoUserUserVCSTokenResponse] get_all()



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
api_instance = swagger_client.UiUserVcsTokenControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserVcsTokenControllerApi->get_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoUserUserVCSTokenResponse]**](ComCapillaryOpsCpBoUserUserVCSTokenResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ComCapillaryOpsCpBoUserUserVCSTokenResponse update(body)



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
api_instance = swagger_client.UiUserVcsTokenControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoUserUserVCSTokenRequest() # ComCapillaryOpsCpBoUserUserVCSTokenRequest | 

try:
    api_response = api_instance.update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiUserVcsTokenControllerApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoUserUserVCSTokenRequest**](ComCapillaryOpsCpBoUserUserVCSTokenRequest.md)|  | 

### Return type

[**ComCapillaryOpsCpBoUserUserVCSTokenResponse**](ComCapillaryOpsCpBoUserUserVCSTokenResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

