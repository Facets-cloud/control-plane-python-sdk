# coding: utf-8

"""
    Api Documentation

    Api Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UiOneTimeWebhookControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def poll_webhook_using_get(self, webhook_id, **kwargs):  # noqa: E501
        """pollWebhook  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poll_webhook_using_get(webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str webhook_id: webhookId (required)
        :return: OneTimeWebhook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.poll_webhook_using_get_with_http_info(webhook_id, **kwargs)  # noqa: E501
        else:
            (data) = self.poll_webhook_using_get_with_http_info(webhook_id, **kwargs)  # noqa: E501
            return data

    def poll_webhook_using_get_with_http_info(self, webhook_id, **kwargs):  # noqa: E501
        """pollWebhook  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.poll_webhook_using_get_with_http_info(webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str webhook_id: webhookId (required)
        :return: OneTimeWebhook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['webhook_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method poll_webhook_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'webhook_id' is set
        if ('webhook_id' not in params or
                params['webhook_id'] is None):
            raise ValueError("Missing the required parameter `webhook_id` when calling `poll_webhook_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'webhook_id' in params:
            path_params['webhookId'] = params['webhook_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['main']  # noqa: E501

        return self.api_client.call_api(
            '/cc-ui/v1/onetime-webhook/poll/{webhookId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OneTimeWebhook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def register_webhook_using_post(self, body, **kwargs):  # noqa: E501
        """registerWebhook  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_webhook_using_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OneTimeWebhook body: webhook (required)
        :return: OneTimeWebhook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.register_webhook_using_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.register_webhook_using_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def register_webhook_using_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """registerWebhook  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_webhook_using_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OneTimeWebhook body: webhook (required)
        :return: OneTimeWebhook
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
                    " to method register_webhook_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `register_webhook_using_post`")  # noqa: E501

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
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['main']  # noqa: E501

        return self.api_client.call_api(
            '/cc-ui/v1/onetime-webhook/register', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OneTimeWebhook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
