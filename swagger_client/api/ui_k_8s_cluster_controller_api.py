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


class UiK8sClusterControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_draft_cluster(self, body, cluster_id, **kwargs):  # noqa: E501
        """create_draft_cluster  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_draft_cluster(body, cluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KubernetesClusterRequest body: (required)
        :param str cluster_id: (required)
        :return: KubernetesCluster
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_draft_cluster_with_http_info(body, cluster_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_draft_cluster_with_http_info(body, cluster_id, **kwargs)  # noqa: E501
            return data

    def create_draft_cluster_with_http_info(self, body, cluster_id, **kwargs):  # noqa: E501
        """create_draft_cluster  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_draft_cluster_with_http_info(body, cluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KubernetesClusterRequest body: (required)
        :param str cluster_id: (required)
        :return: KubernetesCluster
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'cluster_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_draft_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_draft_cluster`")  # noqa: E501
        # verify the required parameter 'cluster_id' is set
        if ('cluster_id' not in params or
                params['cluster_id'] is None):
            raise ValueError("Missing the required parameter `cluster_id` when calling `create_draft_cluster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in params:
            path_params['clusterId'] = params['cluster_id']  # noqa: E501

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
            '/cc-ui/v1/kubernetes/clusters/configure/{clusterId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='KubernetesCluster',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_k8s_cluster(self, body, **kwargs):  # noqa: E501
        """create_k8s_cluster  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_k8s_cluster(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KubernetesClusterRequest body: (required)
        :return: KubernetesCluster
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_k8s_cluster_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_k8s_cluster_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_k8s_cluster_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_k8s_cluster  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_k8s_cluster_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KubernetesClusterRequest body: (required)
        :return: KubernetesCluster
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
                    " to method create_k8s_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_k8s_cluster`")  # noqa: E501

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
            '/cc-ui/v1/kubernetes/clusters', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='KubernetesCluster',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_k8s_cluster(self, cluster_id, **kwargs):  # noqa: E501
        """get_k8s_cluster  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_k8s_cluster(cluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_id: (required)
        :return: KubernetesCluster
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_k8s_cluster_with_http_info(cluster_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_k8s_cluster_with_http_info(cluster_id, **kwargs)  # noqa: E501
            return data

    def get_k8s_cluster_with_http_info(self, cluster_id, **kwargs):  # noqa: E501
        """get_k8s_cluster  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_k8s_cluster_with_http_info(cluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cluster_id: (required)
        :return: KubernetesCluster
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cluster_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_k8s_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cluster_id' is set
        if ('cluster_id' not in params or
                params['cluster_id'] is None):
            raise ValueError("Missing the required parameter `cluster_id` when calling `get_k8s_cluster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in params:
            path_params['clusterId'] = params['cluster_id']  # noqa: E501

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
            '/cc-ui/v1/kubernetes/clusters/{clusterId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='KubernetesCluster',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_k8s_cluster(self, body, cluster_id, **kwargs):  # noqa: E501
        """update_k8s_cluster  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_k8s_cluster(body, cluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KubernetesClusterRequest body: (required)
        :param str cluster_id: (required)
        :return: KubernetesCluster
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_k8s_cluster_with_http_info(body, cluster_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_k8s_cluster_with_http_info(body, cluster_id, **kwargs)  # noqa: E501
            return data

    def update_k8s_cluster_with_http_info(self, body, cluster_id, **kwargs):  # noqa: E501
        """update_k8s_cluster  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_k8s_cluster_with_http_info(body, cluster_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KubernetesClusterRequest body: (required)
        :param str cluster_id: (required)
        :return: KubernetesCluster
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'cluster_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_k8s_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_k8s_cluster`")  # noqa: E501
        # verify the required parameter 'cluster_id' is set
        if ('cluster_id' not in params or
                params['cluster_id'] is None):
            raise ValueError("Missing the required parameter `cluster_id` when calling `update_k8s_cluster`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cluster_id' in params:
            path_params['clusterId'] = params['cluster_id']  # noqa: E501

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
            '/cc-ui/v1/kubernetes/clusters/{clusterId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='KubernetesCluster',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
