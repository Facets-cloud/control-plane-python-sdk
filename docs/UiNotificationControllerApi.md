# swagger_client.UiNotificationControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_channel**](UiNotificationControllerApi.md#create_notification_channel) | **POST** /cc-ui/v1/notification/channels | 
[**create_subscription1**](UiNotificationControllerApi.md#create_subscription1) | **POST** /cc-ui/v1/notification/subscriptions | 
[**delete_notification_channel**](UiNotificationControllerApi.md#delete_notification_channel) | **DELETE** /cc-ui/v1/notification/channels/{channelId} | 
[**delete_subscription**](UiNotificationControllerApi.md#delete_subscription) | **DELETE** /cc-ui/v1/notification/subscriptions/{subscriptionId} | 
[**edit_notification_channel**](UiNotificationControllerApi.md#edit_notification_channel) | **PUT** /cc-ui/v1/notification/channels/{channelId} | 
[**edit_subscription**](UiNotificationControllerApi.md#edit_subscription) | **PUT** /cc-ui/v1/notification/subscriptions/{subscriptionId} | 
[**get_all_channel_types**](UiNotificationControllerApi.md#get_all_channel_types) | **GET** /cc-ui/v1/notification/channelTypes | 
[**get_all_channels**](UiNotificationControllerApi.md#get_all_channels) | **GET** /cc-ui/v1/notification/channels | 
[**get_all_notification_tags**](UiNotificationControllerApi.md#get_all_notification_tags) | **GET** /cc-ui/v1/notification/notificationTags | 
[**get_all_notification_types**](UiNotificationControllerApi.md#get_all_notification_types) | **GET** /cc-ui/v1/notification/notificationTypes | 
[**get_all_subscriptions1**](UiNotificationControllerApi.md#get_all_subscriptions1) | **GET** /cc-ui/v1/notification/subscriptions | 
[**get_channel**](UiNotificationControllerApi.md#get_channel) | **GET** /cc-ui/v1/notification/channels/{channelId} | 
[**get_filters_for_subscriptions**](UiNotificationControllerApi.md#get_filters_for_subscriptions) | **POST** /cc-ui/v1/notification/{notificationType}/tag/{tagName}/values/ | 
[**get_notification_tags_for_notification_type**](UiNotificationControllerApi.md#get_notification_tags_for_notification_type) | **GET** /cc-ui/v1/notification/{notificationType}/tags | 
[**get_subscription**](UiNotificationControllerApi.md#get_subscription) | **GET** /cc-ui/v1/notification/subscriptions/{subscriptionId} | 
[**get_subscription_attributes**](UiNotificationControllerApi.md#get_subscription_attributes) | **GET** /cc-ui/v1/notification/notificationType/{notificationType}/attributes | 
[**test_notification_channel**](UiNotificationControllerApi.md#test_notification_channel) | **POST** /cc-ui/v1/notification/channels/test | 

# **create_notification_channel**
> list[NotificationChannel] create_notification_channel(body)



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.NotificationChannel() # NotificationChannel | 

try:
    api_response = api_instance.create_notification_channel(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->create_notification_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationChannel**](NotificationChannel.md)|  | 

### Return type

[**list[NotificationChannel]**](NotificationChannel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription1**
> list[Subscription] create_subscription1(body)



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Subscription() # Subscription | 

try:
    api_response = api_instance.create_subscription1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->create_subscription1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Subscription**](Subscription.md)|  | 

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_channel**
> list[NotificationChannel] delete_notification_channel(channel_id)



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
channel_id = 'channel_id_example' # str | 

try:
    api_response = api_instance.delete_notification_channel(channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->delete_notification_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

[**list[NotificationChannel]**](NotificationChannel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> list[Subscription] delete_subscription(subscription_id)



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 

try:
    api_response = api_instance.delete_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->delete_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_notification_channel**
> list[NotificationChannel] edit_notification_channel(body, channel_id)



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.NotificationChannel() # NotificationChannel | 
channel_id = 'channel_id_example' # str | 

try:
    api_response = api_instance.edit_notification_channel(body, channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->edit_notification_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationChannel**](NotificationChannel.md)|  | 
 **channel_id** | **str**|  | 

### Return type

[**list[NotificationChannel]**](NotificationChannel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_subscription**
> list[Subscription] edit_subscription(body, subscription_id)



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Subscription() # Subscription | 
subscription_id = 'subscription_id_example' # str | 

try:
    api_response = api_instance.edit_subscription(body, subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->edit_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Subscription**](Subscription.md)|  | 
 **subscription_id** | **str**|  | 

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_channel_types**
> list[ChannelTypePayload] get_all_channel_types()



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_channel_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_all_channel_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ChannelTypePayload]**](ChannelTypePayload.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_channels**
> list[NotificationChannel] get_all_channels()



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_channels()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_all_channels: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NotificationChannel]**](NotificationChannel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_notification_tags**
> list[NotificationTagPayload] get_all_notification_tags()



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_notification_tags()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_all_notification_tags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NotificationTagPayload]**](NotificationTagPayload.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_notification_types**
> list[NotificationTypeResponse] get_all_notification_types()



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_notification_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_all_notification_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NotificationTypeResponse]**](NotificationTypeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_subscriptions1**
> list[Subscription] get_all_subscriptions1()



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_all_subscriptions1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_all_subscriptions1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel**
> NotificationChannel get_channel(channel_id)



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
channel_id = 'channel_id_example' # str | 

try:
    api_response = api_instance.get_channel(channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

[**NotificationChannel**](NotificationChannel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filters_for_subscriptions**
> TagDataModel get_filters_for_subscriptions(body, notification_type, tag_name)



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, list[str]) | 
notification_type = 'notification_type_example' # str | 
tag_name = 'tag_name_example' # str | 

try:
    api_response = api_instance.get_filters_for_subscriptions(body, notification_type, tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_filters_for_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, list[str])**](dict.md)|  | 
 **notification_type** | **str**|  | 
 **tag_name** | **str**|  | 

### Return type

[**TagDataModel**](TagDataModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_tags_for_notification_type**
> list[NotificationTagsForTypeResult] get_notification_tags_for_notification_type(notification_type)



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
notification_type = 'notification_type_example' # str | 

try:
    api_response = api_instance.get_notification_tags_for_notification_type(notification_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_notification_tags_for_notification_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_type** | **str**|  | 

### Return type

[**list[NotificationTagsForTypeResult]**](NotificationTagsForTypeResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> Subscription get_subscription(subscription_id)



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 

try:
    api_response = api_instance.get_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_attributes**
> list[str] get_subscription_attributes(notification_type)



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
notification_type = 'notification_type_example' # str | 

try:
    api_response = api_instance.get_subscription_attributes(notification_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_subscription_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_type** | **str**|  | 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_notification_channel**
> bool test_notification_channel(body)



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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.TestNotificationRequest() # TestNotificationRequest | 

try:
    api_response = api_instance.test_notification_channel(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->test_notification_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TestNotificationRequest**](TestNotificationRequest.md)|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

