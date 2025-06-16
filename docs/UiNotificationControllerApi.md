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
> list[ComCapillaryOpsCpBoNotificationsNotificationChannel] create_notification_channel(body)



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
body = swagger_client.ComCapillaryOpsCpBoNotificationsNotificationChannel() # ComCapillaryOpsCpBoNotificationsNotificationChannel | 

try:
    api_response = api_instance.create_notification_channel(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->create_notification_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoNotificationsNotificationChannel**](ComCapillaryOpsCpBoNotificationsNotificationChannel.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoNotificationsNotificationChannel]**](ComCapillaryOpsCpBoNotificationsNotificationChannel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription1**
> list[ComCapillaryOpsCpBoNotificationsSubscription] create_subscription1(body)



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
body = swagger_client.ComCapillaryOpsCpBoNotificationsSubscription() # ComCapillaryOpsCpBoNotificationsSubscription | 

try:
    api_response = api_instance.create_subscription1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->create_subscription1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoNotificationsSubscription**](ComCapillaryOpsCpBoNotificationsSubscription.md)|  | 

### Return type

[**list[ComCapillaryOpsCpBoNotificationsSubscription]**](ComCapillaryOpsCpBoNotificationsSubscription.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_channel**
> list[ComCapillaryOpsCpBoNotificationsNotificationChannel] delete_notification_channel(channel_id)



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

[**list[ComCapillaryOpsCpBoNotificationsNotificationChannel]**](ComCapillaryOpsCpBoNotificationsNotificationChannel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> list[ComCapillaryOpsCpBoNotificationsSubscription] delete_subscription(subscription_id)



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

[**list[ComCapillaryOpsCpBoNotificationsSubscription]**](ComCapillaryOpsCpBoNotificationsSubscription.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_notification_channel**
> list[ComCapillaryOpsCpBoNotificationsNotificationChannel] edit_notification_channel(body, channel_id)



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
body = swagger_client.ComCapillaryOpsCpBoNotificationsNotificationChannel() # ComCapillaryOpsCpBoNotificationsNotificationChannel | 
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
 **body** | [**ComCapillaryOpsCpBoNotificationsNotificationChannel**](ComCapillaryOpsCpBoNotificationsNotificationChannel.md)|  | 
 **channel_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoNotificationsNotificationChannel]**](ComCapillaryOpsCpBoNotificationsNotificationChannel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_subscription**
> list[ComCapillaryOpsCpBoNotificationsSubscription] edit_subscription(body, subscription_id)



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
body = swagger_client.ComCapillaryOpsCpBoNotificationsSubscription() # ComCapillaryOpsCpBoNotificationsSubscription | 
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
 **body** | [**ComCapillaryOpsCpBoNotificationsSubscription**](ComCapillaryOpsCpBoNotificationsSubscription.md)|  | 
 **subscription_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoNotificationsSubscription]**](ComCapillaryOpsCpBoNotificationsSubscription.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_channel_types**
> list[ComCapillaryOpsCpBoNotificationsChannelTypeChannelTypePayload] get_all_channel_types()



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

[**list[ComCapillaryOpsCpBoNotificationsChannelTypeChannelTypePayload]**](ComCapillaryOpsCpBoNotificationsChannelTypeChannelTypePayload.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_channels**
> list[ComCapillaryOpsCpBoNotificationsNotificationChannel] get_all_channels()



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

[**list[ComCapillaryOpsCpBoNotificationsNotificationChannel]**](ComCapillaryOpsCpBoNotificationsNotificationChannel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_notification_tags**
> list[ComCapillaryOpsCpBoNotificationsNotificationTagNotificationTagPayload] get_all_notification_tags()



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

[**list[ComCapillaryOpsCpBoNotificationsNotificationTagNotificationTagPayload]**](ComCapillaryOpsCpBoNotificationsNotificationTagNotificationTagPayload.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_notification_types**
> list[ComCapillaryOpsCpBoNotificationsNotificationTypeNotificationTypeResponse] get_all_notification_types()



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

[**list[ComCapillaryOpsCpBoNotificationsNotificationTypeNotificationTypeResponse]**](ComCapillaryOpsCpBoNotificationsNotificationTypeNotificationTypeResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_subscriptions1**
> list[ComCapillaryOpsCpBoNotificationsSubscription] get_all_subscriptions1()



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

[**list[ComCapillaryOpsCpBoNotificationsSubscription]**](ComCapillaryOpsCpBoNotificationsSubscription.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel**
> ComCapillaryOpsCpBoNotificationsNotificationChannel get_channel(channel_id)



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

[**ComCapillaryOpsCpBoNotificationsNotificationChannel**](ComCapillaryOpsCpBoNotificationsNotificationChannel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filters_for_subscriptions**
> ComCapillaryOpsCpBoNotificationsTagsModelTagDataModel get_filters_for_subscriptions(body, notification_type, tag_name)



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

[**ComCapillaryOpsCpBoNotificationsTagsModelTagDataModel**](ComCapillaryOpsCpBoNotificationsTagsModelTagDataModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_tags_for_notification_type**
> list[ComCapillaryOpsCpBoNotificationsNotificationTagsForTypeResult] get_notification_tags_for_notification_type(notification_type)



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

[**list[ComCapillaryOpsCpBoNotificationsNotificationTagsForTypeResult]**](ComCapillaryOpsCpBoNotificationsNotificationTagsForTypeResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> ComCapillaryOpsCpBoNotificationsSubscription get_subscription(subscription_id)



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

[**ComCapillaryOpsCpBoNotificationsSubscription**](ComCapillaryOpsCpBoNotificationsSubscription.md)

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
body = swagger_client.ComCapillaryOpsCpBoRequestsTestNotificationRequest() # ComCapillaryOpsCpBoRequestsTestNotificationRequest | 

try:
    api_response = api_instance.test_notification_channel(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiNotificationControllerApi->test_notification_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoRequestsTestNotificationRequest**](ComCapillaryOpsCpBoRequestsTestNotificationRequest.md)|  | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

