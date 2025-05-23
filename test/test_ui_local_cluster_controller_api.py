# coding: utf-8

"""
    Api Documentation

    Api Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.ui_local_cluster_controller_api import UiLocalClusterControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUiLocalClusterControllerApi(unittest.TestCase):
    """UiLocalClusterControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.ui_local_cluster_controller_api.UiLocalClusterControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_cluster_using_post3(self):
        """Test case for create_cluster_using_post3

        Create a new Environment for a blueprint  # noqa: E501
        """
        pass

    def test_get_cluster_using_get3(self):
        """Test case for get_cluster_using_get3

        getCluster  # noqa: E501
        """
        pass

    def test_get_vagrant_using_get(self):
        """Test case for get_vagrant_using_get

        getVagrant  # noqa: E501
        """
        pass

    def test_update_cluster_using_put3(self):
        """Test case for update_cluster_using_put3

        updateCluster  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
