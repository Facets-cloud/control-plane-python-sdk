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

class ECRAuthorizationData(object):
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
        'authorization_token': 'str',
        'proxy_endpoint': 'str'
    }

    attribute_map = {
        'authorization_token': 'authorizationToken',
        'proxy_endpoint': 'proxyEndpoint'
    }

    def __init__(self, authorization_token=None, proxy_endpoint=None):  # noqa: E501
        """ECRAuthorizationData - a model defined in Swagger"""  # noqa: E501
        self._authorization_token = None
        self._proxy_endpoint = None
        self.discriminator = None
        if authorization_token is not None:
            self.authorization_token = authorization_token
        if proxy_endpoint is not None:
            self.proxy_endpoint = proxy_endpoint

    @property
    def authorization_token(self):
        """Gets the authorization_token of this ECRAuthorizationData.  # noqa: E501


        :return: The authorization_token of this ECRAuthorizationData.  # noqa: E501
        :rtype: str
        """
        return self._authorization_token

    @authorization_token.setter
    def authorization_token(self, authorization_token):
        """Sets the authorization_token of this ECRAuthorizationData.


        :param authorization_token: The authorization_token of this ECRAuthorizationData.  # noqa: E501
        :type: str
        """

        self._authorization_token = authorization_token

    @property
    def proxy_endpoint(self):
        """Gets the proxy_endpoint of this ECRAuthorizationData.  # noqa: E501


        :return: The proxy_endpoint of this ECRAuthorizationData.  # noqa: E501
        :rtype: str
        """
        return self._proxy_endpoint

    @proxy_endpoint.setter
    def proxy_endpoint(self, proxy_endpoint):
        """Sets the proxy_endpoint of this ECRAuthorizationData.


        :param proxy_endpoint: The proxy_endpoint of this ECRAuthorizationData.  # noqa: E501
        :type: str
        """

        self._proxy_endpoint = proxy_endpoint

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
        if issubclass(ECRAuthorizationData, dict):
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
        if not isinstance(other, ECRAuthorizationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
