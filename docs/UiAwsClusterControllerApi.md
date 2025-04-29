# swagger_client.UiAwsClusterControllerApi

All URIs are relative to *//facetsdemo.console.facets.cloud/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_draft_cluster_using_post**](UiAwsClusterControllerApi.md#configure_draft_cluster_using_post) | **POST** /cc-ui/v1/aws/clusters/configure/{clusterId} | configureDraftCluster
[**create_cluster_using_post2**](UiAwsClusterControllerApi.md#create_cluster_using_post2) | **POST** /cc-ui/v1/aws/clusters | Create a new Environment for a blueprint
[**get_cluster_using_get2**](UiAwsClusterControllerApi.md#get_cluster_using_get2) | **GET** /cc-ui/v1/aws/clusters/{clusterId} | getCluster
[**onboard_customer_using_post**](UiAwsClusterControllerApi.md#onboard_customer_using_post) | **POST** /cc-ui/v1/aws/clusters/onboard-customer | onboardCustomer
[**update_cluster_using_put2**](UiAwsClusterControllerApi.md#update_cluster_using_put2) | **PUT** /cc-ui/v1/aws/clusters/{clusterId} | updateCluster
[**validate_vpc_id_using_get**](UiAwsClusterControllerApi.md#validate_vpc_id_using_get) | **GET** /cc-ui/v1/aws/clusters/validate-vpcId | validateVpcId

# **configure_draft_cluster_using_post**
> AwsCluster configure_draft_cluster_using_post(body, cluster_id)

configureDraftCluster

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
api_instance = swagger_client.UiAwsClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AwsClusterRequest() # AwsClusterRequest | request
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # configureDraftCluster
    api_response = api_instance.configure_draft_cluster_using_post(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAwsClusterControllerApi->configure_draft_cluster_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AwsClusterRequest**](AwsClusterRequest.md)| request | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**AwsCluster**](AwsCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

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
# Configure HTTP basic authorization: main
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.UiAwsClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AwsClusterRequest() # AwsClusterRequest | request

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
 **body** | [**AwsClusterRequest**](AwsClusterRequest.md)| request | 

### Return type

[**AwsCluster**](AwsCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_using_get2**
> AwsCluster get_cluster_using_get2(cluster_id)

getCluster

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
api_instance = swagger_client.UiAwsClusterControllerApi(swagger_client.ApiClient(configuration))
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # getCluster
    api_response = api_instance.get_cluster_using_get2(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAwsClusterControllerApi->get_cluster_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| clusterId | 

### Return type

[**AwsCluster**](AwsCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onboard_customer_using_post**
> onboard_customer_using_post(body)

onboardCustomer

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
api_instance = swagger_client.UiAwsClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomerOnboardRequest() # CustomerOnboardRequest | request

try:
    # onboardCustomer
    api_instance.onboard_customer_using_post(body)
except ApiException as e:
    print("Exception when calling UiAwsClusterControllerApi->onboard_customer_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerOnboardRequest**](CustomerOnboardRequest.md)| request | 

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_using_put2**
> AwsCluster update_cluster_using_put2(body, cluster_id)

updateCluster

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
api_instance = swagger_client.UiAwsClusterControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.AwsClusterRequest() # AwsClusterRequest | request
cluster_id = 'cluster_id_example' # str | clusterId

try:
    # updateCluster
    api_response = api_instance.update_cluster_using_put2(body, cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAwsClusterControllerApi->update_cluster_using_put2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AwsClusterRequest**](AwsClusterRequest.md)| request | 
 **cluster_id** | **str**| clusterId | 

### Return type

[**AwsCluster**](AwsCluster.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_vpc_id_using_get**
> bool validate_vpc_id_using_get(account_id, region, vpc_id)

validateVpcId

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
api_instance = swagger_client.UiAwsClusterControllerApi(swagger_client.ApiClient(configuration))
account_id = 'account_id_example' # str | accountId
region = 'region_example' # str | region
vpc_id = 'vpc_id_example' # str | vpcId

try:
    # validateVpcId
    api_response = api_instance.validate_vpc_id_using_get(account_id, region, vpc_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiAwsClusterControllerApi->validate_vpc_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| accountId | 
 **region** | **str**| region | 
 **vpc_id** | **str**| vpcId | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

