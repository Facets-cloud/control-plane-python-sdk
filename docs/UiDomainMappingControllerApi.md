# swagger_client.UiDomainMappingControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain_mapping**](UiDomainMappingControllerApi.md#add_domain_mapping) | **POST** /cc-ui/v1/domain-mapping/clusterId/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName} | 
[**delete_domain_mapping**](UiDomainMappingControllerApi.md#delete_domain_mapping) | **DELETE** /cc-ui/v1/domain-mapping/clusterId/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName} | 
[**get_all_domains**](UiDomainMappingControllerApi.md#get_all_domains) | **GET** /cc-ui/v1/domain-mapping/clusterId/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName} | 
[**update_domain_mapping**](UiDomainMappingControllerApi.md#update_domain_mapping) | **PUT** /cc-ui/v1/domain-mapping/clusterId/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName} | 

# **add_domain_mapping**
> add_domain_mapping(body, cluster_id, resource_type, resource_name)



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
api_instance = swagger_client.UiDomainMappingControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.DomainDTO() # DomainDTO | 
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_instance.add_domain_mapping(body, cluster_id, resource_type, resource_name)
except ApiException as e:
    print("Exception when calling UiDomainMappingControllerApi->add_domain_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainDTO**](DomainDTO.md)|  | 
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain_mapping**
> delete_domain_mapping(cluster_id, resource_type, resource_name, alias)



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
api_instance = swagger_client.UiDomainMappingControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 
alias = 'alias_example' # str | 

try:
    api_instance.delete_domain_mapping(cluster_id, resource_type, resource_name, alias)
except ApiException as e:
    print("Exception when calling UiDomainMappingControllerApi->delete_domain_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 
 **alias** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_domains**
> list[DomainDTO] get_all_domains(cluster_id, resource_type, resource_name)



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
api_instance = swagger_client.UiDomainMappingControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_response = api_instance.get_all_domains(cluster_id, resource_type, resource_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDomainMappingControllerApi->get_all_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

[**list[DomainDTO]**](DomainDTO.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_mapping**
> update_domain_mapping(body, cluster_id, resource_type, resource_name)



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
api_instance = swagger_client.UiDomainMappingControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.DomainDTO() # DomainDTO | 
cluster_id = 'cluster_id_example' # str | 
resource_type = 'resource_type_example' # str | 
resource_name = 'resource_name_example' # str | 

try:
    api_instance.update_domain_mapping(body, cluster_id, resource_type, resource_name)
except ApiException as e:
    print("Exception when calling UiDomainMappingControllerApi->update_domain_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainDTO**](DomainDTO.md)|  | 
 **cluster_id** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

