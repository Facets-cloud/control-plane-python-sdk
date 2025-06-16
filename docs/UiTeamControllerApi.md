# swagger_client.UiTeamControllerApi

All URIs are relative to *https://facetsdemo.console.facets.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_team_members**](UiTeamControllerApi.md#add_team_members) | **POST** /cc-ui/v1/teams/{teamId}/members | 
[**get_team**](UiTeamControllerApi.md#get_team) | **GET** /cc-ui/v1/teams/{teamId} | 
[**get_team_members**](UiTeamControllerApi.md#get_team_members) | **GET** /cc-ui/v1/teams/{teamId}/members | 
[**get_teams**](UiTeamControllerApi.md#get_teams) | **GET** /cc-ui/v1/teams/ | 
[**upsert_team**](UiTeamControllerApi.md#upsert_team) | **POST** /cc-ui/v1/teams/ | 

# **add_team_members**
> list[ComCapillaryOpsCpBoTeamMembership] add_team_members(body, team_id)



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
api_instance = swagger_client.UiTeamControllerApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | 
team_id = 'team_id_example' # str | 

try:
    api_response = api_instance.add_team_members(body, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTeamControllerApi->add_team_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **team_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoTeamMembership]**](ComCapillaryOpsCpBoTeamMembership.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team**
> ComCapillaryOpsCpBoTeam get_team(team_id)



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
api_instance = swagger_client.UiTeamControllerApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | 

try:
    api_response = api_instance.get_team(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTeamControllerApi->get_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

[**ComCapillaryOpsCpBoTeam**](ComCapillaryOpsCpBoTeam.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_members**
> list[ComCapillaryOpsCpBoTeamMembership] get_team_members(team_id)



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
api_instance = swagger_client.UiTeamControllerApi(swagger_client.ApiClient(configuration))
team_id = 'team_id_example' # str | 

try:
    api_response = api_instance.get_team_members(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTeamControllerApi->get_team_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**|  | 

### Return type

[**list[ComCapillaryOpsCpBoTeamMembership]**](ComCapillaryOpsCpBoTeamMembership.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams**
> list[ComCapillaryOpsCpBoTeam] get_teams()



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
api_instance = swagger_client.UiTeamControllerApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.get_teams()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTeamControllerApi->get_teams: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ComCapillaryOpsCpBoTeam]**](ComCapillaryOpsCpBoTeam.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_team**
> ComCapillaryOpsCpBoTeam upsert_team(body)



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
api_instance = swagger_client.UiTeamControllerApi(swagger_client.ApiClient(configuration))
body = swagger_client.ComCapillaryOpsCpBoTeam() # ComCapillaryOpsCpBoTeam | 

try:
    api_response = api_instance.upsert_team(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UiTeamControllerApi->upsert_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComCapillaryOpsCpBoTeam**](ComCapillaryOpsCpBoTeam.md)|  | 

### Return type

[**ComCapillaryOpsCpBoTeam**](ComCapillaryOpsCpBoTeam.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

