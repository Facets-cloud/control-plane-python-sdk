# swagger_client.UiTeamControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_team_members_using_post**](UiTeamControllerApi.md#add_team_members_using_post) | **POST** /cc-ui/v1/teams/{teamId}/members | addTeamMembers
[**get_team_members_using_get**](UiTeamControllerApi.md#get_team_members_using_get) | **GET** /cc-ui/v1/teams/{teamId}/members | getTeamMembers
[**get_team_using_get**](UiTeamControllerApi.md#get_team_using_get) | **GET** /cc-ui/v1/teams/{teamId} | getTeam
[**get_teams_using_get**](UiTeamControllerApi.md#get_teams_using_get) | **GET** /cc-ui/v1/teams/ | getTeams
[**upsert_team_using_post**](UiTeamControllerApi.md#upsert_team_using_post) | **POST** /cc-ui/v1/teams/ | upsertTeam


# **add_team_members_using_post**
> list[TeamMembership] add_team_members_using_post(team_id, user_names)

addTeamMembers

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
api_instance = swagger_client.UiTeamControllerApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | teamId
user_names = [swagger_client.list[str]()] # list[str] | userNames

try:
    # addTeamMembers
    api_response = api_instance.add_team_members_using_post(team_id, user_names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTeamControllerApi->add_team_members_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| teamId | 
 **user_names** | **list[str]**| userNames | 

### Return type

[**list[TeamMembership]**](TeamMembership.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_members_using_get**
> list[TeamMembership] get_team_members_using_get(team_id)

getTeamMembers

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
api_instance = swagger_client.UiTeamControllerApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | teamId

try:
    # getTeamMembers
    api_response = api_instance.get_team_members_using_get(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTeamControllerApi->get_team_members_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| teamId | 

### Return type

[**list[TeamMembership]**](TeamMembership.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_using_get**
> Team get_team_using_get(team_id)

getTeam

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
api_instance = swagger_client.UiTeamControllerApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | teamId

try:
    # getTeam
    api_response = api_instance.get_team_using_get(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTeamControllerApi->get_team_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| teamId | 

### Return type

[**Team**](Team.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams_using_get**
> list[Team] get_teams_using_get()

getTeams

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
api_instance = swagger_client.UiTeamControllerApi(swagger_client.ApiClient(configuration))

try:
    # getTeams
    api_response = api_instance.get_teams_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTeamControllerApi->get_teams_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Team]**](Team.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_team_using_post**
> Team upsert_team_using_post(team)

upsertTeam

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
api_instance = swagger_client.UiTeamControllerApi(swagger_client.ApiClient(configuration))
team = swagger_client.Team() # Team | team

try:
    # upsertTeam
    api_response = api_instance.upsert_team_using_post(team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTeamControllerApi->upsert_team_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | [**Team**](Team.md)| team | 

### Return type

[**Team**](Team.md)

### Authorization

[main](../README.md#main)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

