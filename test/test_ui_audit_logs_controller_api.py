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
from swagger_client.api.ui_audit_logs_controller_api import UiAuditLogsControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUiAuditLogsControllerApi(unittest.TestCase):
    """UiAuditLogsControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.ui_audit_logs_controller_api.UiAuditLogsControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_audit_logs_using_get(self):
        """Test case for get_audit_logs_using_get

        getAuditLogs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
