# coding: utf-8

"""
    Control-plane

    API Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UiTeamControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_team_members(self, body, team_id, **kwargs):  # noqa: E501
        """add_team_members  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_team_members(body, team_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: (required)
        :param str team_id: (required)
        :return: list[TeamMembership]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_team_members_with_http_info(body, team_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_team_members_with_http_info(body, team_id, **kwargs)  # noqa: E501
            return data

    def add_team_members_with_http_info(self, body, team_id, **kwargs):  # noqa: E501
        """add_team_members  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_team_members_with_http_info(body, team_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body: (required)
        :param str team_id: (required)
        :return: list[TeamMembership]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'team_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_team_members" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_team_members`")  # noqa: E501
        # verify the required parameter 'team_id' is set
        if ('team_id' not in params or
                params['team_id'] is None):
            raise ValueError("Missing the required parameter `team_id` when calling `add_team_members`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'team_id' in params:
            path_params['teamId'] = params['team_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/cc-ui/v1/teams/{teamId}/members', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TeamMembership]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_team(self, team_id, **kwargs):  # noqa: E501
        """get_team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team(team_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: (required)
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_team_with_http_info(team_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_team_with_http_info(team_id, **kwargs)  # noqa: E501
            return data

    def get_team_with_http_info(self, team_id, **kwargs):  # noqa: E501
        """get_team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_with_http_info(team_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: (required)
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'team_id' is set
        if ('team_id' not in params or
                params['team_id'] is None):
            raise ValueError("Missing the required parameter `team_id` when calling `get_team`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'team_id' in params:
            path_params['teamId'] = params['team_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/cc-ui/v1/teams/{teamId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Team',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_team_members(self, team_id, **kwargs):  # noqa: E501
        """get_team_members  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_members(team_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: (required)
        :return: list[TeamMembership]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_team_members_with_http_info(team_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_team_members_with_http_info(team_id, **kwargs)  # noqa: E501
            return data

    def get_team_members_with_http_info(self, team_id, **kwargs):  # noqa: E501
        """get_team_members  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_members_with_http_info(team_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str team_id: (required)
        :return: list[TeamMembership]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['team_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_members" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'team_id' is set
        if ('team_id' not in params or
                params['team_id'] is None):
            raise ValueError("Missing the required parameter `team_id` when calling `get_team_members`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'team_id' in params:
            path_params['teamId'] = params['team_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/cc-ui/v1/teams/{teamId}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TeamMembership]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_teams(self, **kwargs):  # noqa: E501
        """get_teams  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_teams(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Team]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_teams_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_teams_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_teams_with_http_info(self, **kwargs):  # noqa: E501
        """get_teams  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_teams_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Team]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_teams" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/cc-ui/v1/teams/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Team]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upsert_team(self, body, **kwargs):  # noqa: E501
        """upsert_team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_team(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Team body: (required)
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upsert_team_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.upsert_team_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def upsert_team_with_http_info(self, body, **kwargs):  # noqa: E501
        """upsert_team  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_team_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Team body: (required)
        :return: Team
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upsert_team" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `upsert_team`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/cc-ui/v1/teams/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Team',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
