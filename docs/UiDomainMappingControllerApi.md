# swagger_client.UiDomainMappingControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain_mapping_using_post**](UiDomainMappingControllerApi.md#add_domain_mapping_using_post) | **POST** /cc-ui/v1/domain-mapping/clusterId/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName} | addDomainMapping
[**delete_domain_mapping_using_delete**](UiDomainMappingControllerApi.md#delete_domain_mapping_using_delete) | **DELETE** /cc-ui/v1/domain-mapping/clusterId/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName} | deleteDomainMapping
[**get_all_domains_using_get**](UiDomainMappingControllerApi.md#get_all_domains_using_get) | **GET** /cc-ui/v1/domain-mapping/clusterId/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName} | getAllDomains
[**update_domain_mapping_using_put**](UiDomainMappingControllerApi.md#update_domain_mapping_using_put) | **PUT** /cc-ui/v1/domain-mapping/clusterId/{clusterId}/resourceType/{resourceType}/resourceName/{resourceName} | updateDomainMapping

# **add_domain_mapping_using_post**
> add_domain_mapping_using_post(body, cluster_id, resource_name, resource_type)

addDomainMapping

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
api_instance = swagger_client.UiDomainMappingControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.DomainDTO() # DomainDTO | domain
cluster_id = 'cluster_id_example' # str | clusterId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # addDomainMapping
    api_instance.add_domain_mapping_using_post(body, cluster_id, resource_name, resource_type)
except ApiException as e:
    print("Exception when calling UiDomainMappingControllerApi->add_domain_mapping_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainDTO**](DomainDTO.md)| domain | 
 **cluster_id** | **str**| clusterId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain_mapping_using_delete**
> delete_domain_mapping_using_delete(alias, cluster_id, resource_name, resource_type)

deleteDomainMapping

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
api_instance = swagger_client.UiDomainMappingControllerApi(swagger_client.ApiClient(configuration))
alias = 'alias_example' # str | alias
cluster_id = 'cluster_id_example' # str | clusterId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # deleteDomainMapping
    api_instance.delete_domain_mapping_using_delete(alias, cluster_id, resource_name, resource_type)
except ApiException as e:
    print("Exception when calling UiDomainMappingControllerApi->delete_domain_mapping_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias | 
 **cluster_id** | **str**| clusterId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_domains_using_get**
> list[DomainDTO] get_all_domains_using_get(cluster_id, resource_name, resource_type)

getAllDomains

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
api_instance = swagger_client.UiDomainMappingControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # getAllDomains
    api_response = api_instance.get_all_domains_using_get(cluster_id, resource_name, resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiDomainMappingControllerApi->get_all_domains_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 

### Return type

[**list[DomainDTO]**](DomainDTO.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_mapping_using_put**
> update_domain_mapping_using_put(body, cluster_id, resource_name, resource_type)

updateDomainMapping

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
api_instance = swagger_client.UiDomainMappingControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.DomainDTO() # DomainDTO | domain
cluster_id = 'cluster_id_example' # str | clusterId
resource_name = 'resource_name_example' # str | resourceName
resource_type = 'resource_type_example' # str | resourceType

try:
    # updateDomainMapping
    api_instance.update_domain_mapping_using_put(body, cluster_id, resource_name, resource_type)
except ApiException as e:
    print("Exception when calling UiDomainMappingControllerApi->update_domain_mapping_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainDTO**](DomainDTO.md)| domain | 
 **cluster_id** | **str**| clusterId | 
 **resource_name** | **str**| resourceName | 
 **resource_type** | **str**| resourceType | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

