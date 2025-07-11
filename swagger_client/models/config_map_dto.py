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

class ConfigMapDTO(object):
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
        'name': 'str',
        'keys': 'list[str]',
        'age': 'int'
    }

    attribute_map = {
        'name': 'name',
        'keys': 'keys',
        'age': 'age'
    }

    def __init__(self, name=None, keys=None, age=None):  # noqa: E501
        """ConfigMapDTO - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._keys = None
        self._age = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if keys is not None:
            self.keys = keys
        if age is not None:
            self.age = age

    @property
    def name(self):
        """Gets the name of this ConfigMapDTO.  # noqa: E501


        :return: The name of this ConfigMapDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigMapDTO.


        :param name: The name of this ConfigMapDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def keys(self):
        """Gets the keys of this ConfigMapDTO.  # noqa: E501


        :return: The keys of this ConfigMapDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this ConfigMapDTO.


        :param keys: The keys of this ConfigMapDTO.  # noqa: E501
        :type: list[str]
        """

        self._keys = keys

    @property
    def age(self):
        """Gets the age of this ConfigMapDTO.  # noqa: E501


        :return: The age of this ConfigMapDTO.  # noqa: E501
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this ConfigMapDTO.


        :param age: The age of this ConfigMapDTO.  # noqa: E501
        :type: int
        """

        self._age = age

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
        if issubclass(ConfigMapDTO, dict):
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
        if not isinstance(other, ConfigMapDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
