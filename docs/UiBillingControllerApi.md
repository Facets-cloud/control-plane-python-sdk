# swagger_client.UiBillingControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buy_support_plan**](UiBillingControllerApi.md#buy_support_plan) | **POST** /cc-ui/v1/billing/buy-support-plan | 
[**get_billing_metadata**](UiBillingControllerApi.md#get_billing_metadata) | **GET** /cc-ui/v1/billing/metadata | 
[**report_usage**](UiBillingControllerApi.md#report_usage) | **GET** /cc-ui/v1/billing/report-usage | 
[**start_stripe_customer_portal_session**](UiBillingControllerApi.md#start_stripe_customer_portal_session) | **GET** /cc-ui/v1/billing/manage-billing | 

# **buy_support_plan**
> str buy_support_plan(success_url, cancel_url)



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
api_instance = swagger_client.UiBillingControllerApi(swagger_client.ApiClient(configuration))
success_url = 'success_url_example' # str | 
cancel_url = 'cancel_url_example' # str | 

try:
    api_response = api_instance.buy_support_plan(success_url, cancel_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBillingControllerApi->buy_support_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **success_url** | **str**|  | 
 **cancel_url** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_metadata**
> list[BillingMetadata] get_billing_metadata()



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
api_instance = swagger_client.UiBillingControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_billing_metadata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBillingControllerApi->get_billing_metadata: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BillingMetadata]**](BillingMetadata.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_usage**
> report_usage()



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
api_instance = swagger_client.UiBillingControllerApi(swagger_client.ApiClient(configuration))

try:
    api_instance.report_usage()
except ApiException as e:
    print("Exception when calling UiBillingControllerApi->report_usage: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_stripe_customer_portal_session**
> str start_stripe_customer_portal_session(return_url)



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
api_instance = swagger_client.UiBillingControllerApi(swagger_client.ApiClient(configuration))
return_url = 'return_url_example' # str | 

try:
    api_response = api_instance.start_stripe_customer_portal_session(return_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBillingControllerApi->start_stripe_customer_portal_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_url** | **str**|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

