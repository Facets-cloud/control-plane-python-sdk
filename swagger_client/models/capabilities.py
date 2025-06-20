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

class Capabilities(object):
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
        'add': 'list[str]',
        'drop': 'list[str]'
    }

    attribute_map = {
        'add': 'add',
        'drop': 'drop'
    }

    def __init__(self, add=None, drop=None):  # noqa: E501
        """Capabilities - a model defined in Swagger"""  # noqa: E501
        self._add = None
        self._drop = None
        self.discriminator = None
        if add is not None:
            self.add = add
        if drop is not None:
            self.drop = drop

    @property
    def add(self):
        """Gets the add of this Capabilities.  # noqa: E501


        :return: The add of this Capabilities.  # noqa: E501
        :rtype: list[str]
        """
        return self._add

    @add.setter
    def add(self, add):
        """Sets the add of this Capabilities.


        :param add: The add of this Capabilities.  # noqa: E501
        :type: list[str]
        """

        self._add = add

    @property
    def drop(self):
        """Gets the drop of this Capabilities.  # noqa: E501


        :return: The drop of this Capabilities.  # noqa: E501
        :rtype: list[str]
        """
        return self._drop

    @drop.setter
    def drop(self, drop):
        """Sets the drop of this Capabilities.


        :param drop: The drop of this Capabilities.  # noqa: E501
        :type: list[str]
        """

        self._drop = drop

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
        if issubclass(Capabilities, dict):
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
        if not isinstance(other, Capabilities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
