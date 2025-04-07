# swagger_client.UiBillingControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buy_support_plan_using_post**](UiBillingControllerApi.md#buy_support_plan_using_post) | **POST** /cc-ui/v1/billing/buy-support-plan | buySupportPlan
[**get_billing_metadata_using_get**](UiBillingControllerApi.md#get_billing_metadata_using_get) | **GET** /cc-ui/v1/billing/metadata | getBillingMetadata
[**report_usage_using_get**](UiBillingControllerApi.md#report_usage_using_get) | **GET** /cc-ui/v1/billing/report-usage | reportUsage
[**start_stripe_customer_portal_session_using_get**](UiBillingControllerApi.md#start_stripe_customer_portal_session_using_get) | **GET** /cc-ui/v1/billing/manage-billing | startStripeCustomerPortalSession


# **buy_support_plan_using_post**
> str buy_support_plan_using_post(cancel_url, success_url)

buySupportPlan

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
api_instance = swagger_client.UiBillingControllerApi(swagger_client.ApiClient(configuration))
cancel_url = 'cancel_url_example' # str | cancelUrl
success_url = 'success_url_example' # str | successUrl

try:
    # buySupportPlan
    api_response = api_instance.buy_support_plan_using_post(cancel_url, success_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBillingControllerApi->buy_support_plan_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_url** | **str**| cancelUrl | 
 **success_url** | **str**| successUrl | 

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_metadata_using_get**
> list[BillingMetadata] get_billing_metadata_using_get()

getBillingMetadata

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
api_instance = swagger_client.UiBillingControllerApi(swagger_client.ApiClient(configuration))

try:
    # getBillingMetadata
    api_response = api_instance.get_billing_metadata_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBillingControllerApi->get_billing_metadata_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BillingMetadata]**](BillingMetadata.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_usage_using_get**
> report_usage_using_get()

reportUsage

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
api_instance = swagger_client.UiBillingControllerApi(swagger_client.ApiClient(configuration))

try:
    # reportUsage
    api_instance.report_usage_using_get()
except ApiException as e:
    print("Exception when calling UiBillingControllerApi->report_usage_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_stripe_customer_portal_session_using_get**
> str start_stripe_customer_portal_session_using_get(return_url)

startStripeCustomerPortalSession

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
api_instance = swagger_client.UiBillingControllerApi(swagger_client.ApiClient(configuration))
return_url = 'return_url_example' # str | returnUrl

try:
    # startStripeCustomerPortalSession
    api_response = api_instance.start_stripe_customer_portal_session_using_get(return_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiBillingControllerApi->start_stripe_customer_portal_session_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_url** | **str**| returnUrl | 

### Return type

**str**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

