# coding: utf-8

"""
    Control-plane

    API Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ArtifactoryLinkingRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'webhook': 'OneTimeWebhook',
        'artifactory_name': 'str'
    }

    attribute_map = {
        'webhook': 'webhook',
        'artifactory_name': 'artifactoryName'
    }

    def __init__(self, webhook=None, artifactory_name=None):  # noqa: E501
        """ArtifactoryLinkingRequest - a model defined in Swagger"""  # noqa: E501
        self._webhook = None
        self._artifactory_name = None
        self.discriminator = None
        if webhook is not None:
            self.webhook = webhook
        if artifactory_name is not None:
            self.artifactory_name = artifactory_name

    @property
    def webhook(self):
        """Gets the webhook of this ArtifactoryLinkingRequest.  # noqa: E501


        :return: The webhook of this ArtifactoryLinkingRequest.  # noqa: E501
        :rtype: OneTimeWebhook
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this ArtifactoryLinkingRequest.


        :param webhook: The webhook of this ArtifactoryLinkingRequest.  # noqa: E501
        :type: OneTimeWebhook
        """

        self._webhook = webhook

    @property
    def artifactory_name(self):
        """Gets the artifactory_name of this ArtifactoryLinkingRequest.  # noqa: E501


        :return: The artifactory_name of this ArtifactoryLinkingRequest.  # noqa: E501
        :rtype: str
        """
        return self._artifactory_name

    @artifactory_name.setter
    def artifactory_name(self, artifactory_name):
        """Sets the artifactory_name of this ArtifactoryLinkingRequest.


        :param artifactory_name: The artifactory_name of this ArtifactoryLinkingRequest.  # noqa: E501
        :type: str
        """

        self._artifactory_name = artifactory_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ArtifactoryLinkingRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ArtifactoryLinkingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
