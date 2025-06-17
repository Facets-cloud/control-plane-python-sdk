# swagger_client.UiAwsClusterControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_draft_cluster2**](UiAwsClusterControllerApi.md#configure_draft_cluster2) | **POST** /cc-ui/v1/aws/clusters/configure/{clusterId} | 
[**create_cluster_using_post2**](UiAwsClusterControllerApi.md#create_cluster_using_post2) | **POST** /cc-ui/v1/aws/clusters | Create a new Environment for a blueprint
[**get_cluster_using_get2**](UiAwsClusterControllerApi.md#get_cluster_using_get2) | **GET** /cc-ui/v1/aws/clusters/{clusterId} | 
[**onboard_customer**](UiAwsClusterControllerApi.md#onboard_customer) | **POST** /cc-ui/v1/aws/clusters/onboard-customer | 
[**update_cluster_using_put2**](UiAwsClusterControllerApi.md#update_cluster_using_put2) | **PUT** /cc-ui/v1/aws/clusters/{clusterId} | 
[**validate_vpc_id1**](UiAwsClusterControllerApi.md#validate_vpc_id1) | **GET** /cc-ui/v1/aws/clusters/validate-vpcId | 

# **configure_draft_cluster2**
> AwsCluster configure_draft_cluster2(body, cluster_id)



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
api_instance = swagger_client.UiAwsClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AwsClusterRequest() # AwsClusterRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.configure_draft_cluster2(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAwsClusterControllerApi->configure_draft_cluster2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AwsClusterRequest**](AwsClusterRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**AwsCluster**](AwsCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_using_post2**
> AwsCluster create_cluster_using_post2(body)

Create a new Environment for a blueprint

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
api_instance = swagger_client.UiAwsClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AwsClusterRequest() # AwsClusterRequest | 

try:
    # Create a new Environment for a blueprint
    api_response = api_instance.create_cluster_using_post2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAwsClusterControllerApi->create_cluster_using_post2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AwsClusterRequest**](AwsClusterRequest.md)|  | 

### Return type

[**AwsCluster**](AwsCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_using_get2**
> AwsCluster get_cluster_using_get2(cluster_id)



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
api_instance = swagger_client.UiAwsClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.get_cluster_using_get2(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAwsClusterControllerApi->get_cluster_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**|  | 

### Return type

[**AwsCluster**](AwsCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onboard_customer**
> onboard_customer(body)



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
api_instance = swagger_client.UiAwsClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomerOnboardRequest() # CustomerOnboardRequest | 

try:
    api_instance.onboard_customer(body)
except ApiException as e:
    print("Exception when calling UiAwsClusterControllerApi->onboard_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerOnboardRequest**](CustomerOnboardRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_using_put2**
> AwsCluster update_cluster_using_put2(body, cluster_id)



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
api_instance = swagger_client.UiAwsClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AwsClusterRequest() # AwsClusterRequest | 
cluster_id = 'cluster_id_example' # str | 

try:
    api_response = api_instance.update_cluster_using_put2(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAwsClusterControllerApi->update_cluster_using_put2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AwsClusterRequest**](AwsClusterRequest.md)|  | 
 **cluster_id** | **str**|  | 

### Return type

[**AwsCluster**](AwsCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_vpc_id1**
> bool validate_vpc_id1(vpc_id, region, account_id)



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
api_instance = swagger_client.UiAwsClusterControllerApi(swagger_client.ApiClient(configuration))
vpc_id = 'vpc_id_example' # str | 
region = 'region_example' # str | 
account_id = 'account_id_example' # str | 

try:
    api_response = api_instance.validate_vpc_id1(vpc_id, region, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAwsClusterControllerApi->validate_vpc_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpc_id** | **str**|  | 
 **region** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

