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
from swagger_client.api.ui_notification_controller_api import UiNotificationControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUiNotificationControllerApi(unittest.TestCase):
    """UiNotificationControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.ui_notification_controller_api.UiNotificationControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_notification_channel_using_post(self):
        """Test case for create_notification_channel_using_post

        createNotificationChannel  # noqa: E501
        """
        pass

    def test_create_subscription_using_post(self):
        """Test case for create_subscription_using_post

        createSubscription  # noqa: E501
        """
        pass

    def test_delete_notification_channel_using_delete(self):
        """Test case for delete_notification_channel_using_delete

        deleteNotificationChannel  # noqa: E501
        """
        pass

    def test_delete_subscription_using_delete(self):
        """Test case for delete_subscription_using_delete

        deleteSubscription  # noqa: E501
        """
        pass

    def test_edit_notification_channel_using_put(self):
        """Test case for edit_notification_channel_using_put

        editNotificationChannel  # noqa: E501
        """
        pass

    def test_edit_subscription_using_put(self):
        """Test case for edit_subscription_using_put

        editSubscription  # noqa: E501
        """
        pass

    def test_get_all_channel_types_using_get(self):
        """Test case for get_all_channel_types_using_get

        getAllChannelTypes  # noqa: E501
        """
        pass

    def test_get_all_channels_using_get(self):
        """Test case for get_all_channels_using_get

        getAllChannels  # noqa: E501
        """
        pass

    def test_get_all_notification_tags_using_get(self):
        """Test case for get_all_notification_tags_using_get

        getAllNotificationTags  # noqa: E501
        """
        pass

    def test_get_all_notification_types_using_get(self):
        """Test case for get_all_notification_types_using_get

        getAllNotificationTypes  # noqa: E501
        """
        pass

    def test_get_all_subscriptions_using_get(self):
        """Test case for get_all_subscriptions_using_get

        getAllSubscriptions  # noqa: E501
        """
        pass

    def test_get_channel_using_get(self):
        """Test case for get_channel_using_get

        getChannel  # noqa: E501
        """
        pass

    def test_get_filters_for_subscriptions_using_post(self):
        """Test case for get_filters_for_subscriptions_using_post

        getFiltersForSubscriptions  # noqa: E501
        """
        pass

    def test_get_notification_tags_for_notification_type_using_get(self):
        """Test case for get_notification_tags_for_notification_type_using_get

        getNotificationTagsForNotificationType  # noqa: E501
        """
        pass

    def test_get_subscription_attributes_using_get(self):
        """Test case for get_subscription_attributes_using_get

        getSubscriptionAttributes  # noqa: E501
        """
        pass

    def test_get_subscription_using_get(self):
        """Test case for get_subscription_using_get

        getSubscription  # noqa: E501
        """
        pass

    def test_test_notification_channel_using_post(self):
        """Test case for test_notification_channel_using_post

        testNotificationChannel  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
