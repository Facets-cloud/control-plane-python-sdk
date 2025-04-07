# swagger_client.UiNotificationControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_channel_using_post**](UiNotificationControllerApi.md#create_notification_channel_using_post) | **POST** /cc-ui/v1/notification/channels | createNotificationChannel
[**create_subscription_using_post**](UiNotificationControllerApi.md#create_subscription_using_post) | **POST** /cc-ui/v1/notification/subscriptions | createSubscription
[**delete_notification_channel_using_delete**](UiNotificationControllerApi.md#delete_notification_channel_using_delete) | **DELETE** /cc-ui/v1/notification/channels/{channelId} | deleteNotificationChannel
[**delete_subscription_using_delete**](UiNotificationControllerApi.md#delete_subscription_using_delete) | **DELETE** /cc-ui/v1/notification/subscriptions/{subscriptionId} | deleteSubscription
[**edit_notification_channel_using_put**](UiNotificationControllerApi.md#edit_notification_channel_using_put) | **PUT** /cc-ui/v1/notification/channels/{channelId} | editNotificationChannel
[**edit_subscription_using_put**](UiNotificationControllerApi.md#edit_subscription_using_put) | **PUT** /cc-ui/v1/notification/subscriptions/{subscriptionId} | editSubscription
[**get_all_channel_types_using_get**](UiNotificationControllerApi.md#get_all_channel_types_using_get) | **GET** /cc-ui/v1/notification/channelTypes | getAllChannelTypes
[**get_all_channels_using_get**](UiNotificationControllerApi.md#get_all_channels_using_get) | **GET** /cc-ui/v1/notification/channels | getAllChannels
[**get_all_notification_tags_using_get**](UiNotificationControllerApi.md#get_all_notification_tags_using_get) | **GET** /cc-ui/v1/notification/notificationTags | getAllNotificationTags
[**get_all_notification_types_using_get**](UiNotificationControllerApi.md#get_all_notification_types_using_get) | **GET** /cc-ui/v1/notification/notificationTypes | getAllNotificationTypes
[**get_all_subscriptions_using_get**](UiNotificationControllerApi.md#get_all_subscriptions_using_get) | **GET** /cc-ui/v1/notification/subscriptions | getAllSubscriptions
[**get_channel_using_get**](UiNotificationControllerApi.md#get_channel_using_get) | **GET** /cc-ui/v1/notification/channels/{channelId} | getChannel
[**get_filters_for_subscriptions_using_post**](UiNotificationControllerApi.md#get_filters_for_subscriptions_using_post) | **POST** /cc-ui/v1/notification/{notificationType}/tag/{tagName}/values/ | getFiltersForSubscriptions
[**get_notification_tags_for_notification_type_using_get**](UiNotificationControllerApi.md#get_notification_tags_for_notification_type_using_get) | **GET** /cc-ui/v1/notification/{notificationType}/tags | getNotificationTagsForNotificationType
[**get_subscription_attributes_using_get**](UiNotificationControllerApi.md#get_subscription_attributes_using_get) | **GET** /cc-ui/v1/notification/notificationType/{notificationType}/attributes | getSubscriptionAttributes
[**get_subscription_using_get**](UiNotificationControllerApi.md#get_subscription_using_get) | **GET** /cc-ui/v1/notification/subscriptions/{subscriptionId} | getSubscription
[**test_notification_channel_using_post**](UiNotificationControllerApi.md#test_notification_channel_using_post) | **POST** /cc-ui/v1/notification/channels/test | testNotificationChannel


# **create_notification_channel_using_post**
> list[NotificationChannel] create_notification_channel_using_post(nc)

createNotificationChannel

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
nc = swagger_client.NotificationChannel() # NotificationChannel | nc

try:
    # createNotificationChannel
    api_response = api_instance.create_notification_channel_using_post(nc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->create_notification_channel_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nc** | [**NotificationChannel**](NotificationChannel.md)| nc | 

### Return type

[**list[NotificationChannel]**](NotificationChannel.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription_using_post**
> list[Subscription] create_subscription_using_post(subscription)

createSubscription

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
subscription = swagger_client.Subscription() # Subscription | subscription

try:
    # createSubscription
    api_response = api_instance.create_subscription_using_post(subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->create_subscription_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | [**Subscription**](Subscription.md)| subscription | 

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_channel_using_delete**
> list[NotificationChannel] delete_notification_channel_using_delete(channel_id)

deleteNotificationChannel

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
channel_id = 'channel_id_example' # str | channelId

try:
    # deleteNotificationChannel
    api_response = api_instance.delete_notification_channel_using_delete(channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->delete_notification_channel_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| channelId | 

### Return type

[**list[NotificationChannel]**](NotificationChannel.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription_using_delete**
> list[Subscription] delete_subscription_using_delete(subscription_id)

deleteSubscription

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | subscriptionId

try:
    # deleteSubscription
    api_response = api_instance.delete_subscription_using_delete(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->delete_subscription_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscriptionId | 

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_notification_channel_using_put**
> list[NotificationChannel] edit_notification_channel_using_put(channel_id, nc)

editNotificationChannel

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
channel_id = 'channel_id_example' # str | channelId
nc = swagger_client.NotificationChannel() # NotificationChannel | nc

try:
    # editNotificationChannel
    api_response = api_instance.edit_notification_channel_using_put(channel_id, nc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->edit_notification_channel_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| channelId | 
 **nc** | [**NotificationChannel**](NotificationChannel.md)| nc | 

### Return type

[**list[NotificationChannel]**](NotificationChannel.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_subscription_using_put**
> list[Subscription] edit_subscription_using_put(subscription, subscription_id)

editSubscription

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
subscription = swagger_client.Subscription() # Subscription | subscription
subscription_id = 'subscription_id_example' # str | subscriptionId

try:
    # editSubscription
    api_response = api_instance.edit_subscription_using_put(subscription, subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->edit_subscription_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | [**Subscription**](Subscription.md)| subscription | 
 **subscription_id** | **str**| subscriptionId | 

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_channel_types_using_get**
> list[ChannelTypePayload] get_all_channel_types_using_get()

getAllChannelTypes

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllChannelTypes
    api_response = api_instance.get_all_channel_types_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_all_channel_types_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ChannelTypePayload]**](ChannelTypePayload.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_channels_using_get**
> list[NotificationChannel] get_all_channels_using_get()

getAllChannels

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllChannels
    api_response = api_instance.get_all_channels_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_all_channels_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NotificationChannel]**](NotificationChannel.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_notification_tags_using_get**
> list[NotificationTagPayload] get_all_notification_tags_using_get()

getAllNotificationTags

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllNotificationTags
    api_response = api_instance.get_all_notification_tags_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_all_notification_tags_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NotificationTagPayload]**](NotificationTagPayload.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_notification_types_using_get**
> list[NotificationTypeResponse] get_all_notification_types_using_get()

getAllNotificationTypes

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllNotificationTypes
    api_response = api_instance.get_all_notification_types_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_all_notification_types_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NotificationTypeResponse]**](NotificationTypeResponse.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_subscriptions_using_get**
> list[Subscription] get_all_subscriptions_using_get()

getAllSubscriptions

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))

try:
    # getAllSubscriptions
    api_response = api_instance.get_all_subscriptions_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_all_subscriptions_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_using_get**
> NotificationChannel get_channel_using_get(channel_id)

getChannel

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
channel_id = 'channel_id_example' # str | channelId

try:
    # getChannel
    api_response = api_instance.get_channel_using_get(channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_channel_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| channelId | 

### Return type

[**NotificationChannel**](NotificationChannel.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filters_for_subscriptions_using_post**
> TagDataModel get_filters_for_subscriptions_using_post(filter_params, notification_type, tag_name)

getFiltersForSubscriptions

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
filter_params = NULL # object | filterParams
notification_type = 'notification_type_example' # str | notificationType
tag_name = 'tag_name_example' # str | tagName

try:
    # getFiltersForSubscriptions
    api_response = api_instance.get_filters_for_subscriptions_using_post(filter_params, notification_type, tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_filters_for_subscriptions_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_params** | **object**| filterParams | 
 **notification_type** | **str**| notificationType | 
 **tag_name** | **str**| tagName | 

### Return type

[**TagDataModel**](TagDataModel.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_tags_for_notification_type_using_get**
> list[NotificationTagsForTypeResult] get_notification_tags_for_notification_type_using_get(notification_type)

getNotificationTagsForNotificationType

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
notification_type = 'notification_type_example' # str | notificationType

try:
    # getNotificationTagsForNotificationType
    api_response = api_instance.get_notification_tags_for_notification_type_using_get(notification_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_notification_tags_for_notification_type_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_type** | **str**| notificationType | 

### Return type

[**list[NotificationTagsForTypeResult]**](NotificationTagsForTypeResult.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_attributes_using_get**
> list[str] get_subscription_attributes_using_get(notification_type)

getSubscriptionAttributes

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
notification_type = 'notification_type_example' # str | notificationType

try:
    # getSubscriptionAttributes
    api_response = api_instance.get_subscription_attributes_using_get(notification_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_subscription_attributes_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_type** | **str**| notificationType | 

### Return type

**list[str]**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_using_get**
> Subscription get_subscription_using_get(subscription_id)

getSubscription

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | subscriptionId

try:
    # getSubscription
    api_response = api_instance.get_subscription_using_get(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->get_subscription_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscriptionId | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_notification_channel_using_post**
> bool test_notification_channel_using_post(test_notification_request)

testNotificationChannel

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
api_instance = swagger_client.UiNotificationControllerApi(swagger_client.ApiClient(configuration))
test_notification_request = swagger_client.TestNotificationRequest() # TestNotificationRequest | testNotificationRequest

try:
    # testNotificationChannel
    api_response = api_instance.test_notification_channel_using_post(test_notification_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->test_notification_channel_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_notification_request** | [**TestNotificationRequest**](TestNotificationRequest.md)| testNotificationRequest | 

### Return type

**bool**

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

