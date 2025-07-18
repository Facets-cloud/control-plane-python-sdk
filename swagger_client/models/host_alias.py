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

class HostAlias(object):
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
        'hostnames': 'list[str]',
        'ip': 'str'
    }

    attribute_map = {
        'hostnames': 'hostnames',
        'ip': 'ip'
    }

    def __init__(self, hostnames=None, ip=None):  # noqa: E501
        """HostAlias - a model defined in Swagger"""  # noqa: E501
        self._hostnames = None
        self._ip = None
        self.discriminator = None
        if hostnames is not None:
            self.hostnames = hostnames
        if ip is not None:
            self.ip = ip

    @property
    def hostnames(self):
        """Gets the hostnames of this HostAlias.  # noqa: E501


        :return: The hostnames of this HostAlias.  # noqa: E501
        :rtype: list[str]
        """
        return self._hostnames

    @hostnames.setter
    def hostnames(self, hostnames):
        """Sets the hostnames of this HostAlias.


        :param hostnames: The hostnames of this HostAlias.  # noqa: E501
        :type: list[str]
        """

        self._hostnames = hostnames

    @property
    def ip(self):
        """Gets the ip of this HostAlias.  # noqa: E501


        :return: The ip of this HostAlias.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this HostAlias.


        :param ip: The ip of this HostAlias.  # noqa: E501
        :type: str
        """

        self._ip = ip

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
        if issubclass(HostAlias, dict):
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
        if not isinstance(other, HostAlias):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
