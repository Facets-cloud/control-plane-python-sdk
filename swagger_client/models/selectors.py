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

class Selectors(object):
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
        'resource_type': 'str',
        'resource_name': 'str',
        'display_type': 'str',
        'sub_type': 'str'
    }

    attribute_map = {
        'resource_type': 'resourceType',
        'resource_name': 'resourceName',
        'display_type': 'displayType',
        'sub_type': 'subType'
    }

    def __init__(self, resource_type=None, resource_name=None, display_type=None, sub_type=None):  # noqa: E501
        """Selectors - a model defined in Swagger"""  # noqa: E501
        self._resource_type = None
        self._resource_name = None
        self._display_type = None
        self._sub_type = None
        self.discriminator = None
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_name is not None:
            self.resource_name = resource_name
        if display_type is not None:
            self.display_type = display_type
        if sub_type is not None:
            self.sub_type = sub_type

    @property
    def resource_type(self):
        """Gets the resource_type of this Selectors.  # noqa: E501


        :return: The resource_type of this Selectors.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Selectors.


        :param resource_type: The resource_type of this Selectors.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def resource_name(self):
        """Gets the resource_name of this Selectors.  # noqa: E501


        :return: The resource_name of this Selectors.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this Selectors.


        :param resource_name: The resource_name of this Selectors.  # noqa: E501
        :type: str
        """

        self._resource_name = resource_name

    @property
    def display_type(self):
        """Gets the display_type of this Selectors.  # noqa: E501


        :return: The display_type of this Selectors.  # noqa: E501
        :rtype: str
        """
        return self._display_type

    @display_type.setter
    def display_type(self, display_type):
        """Sets the display_type of this Selectors.


        :param display_type: The display_type of this Selectors.  # noqa: E501
        :type: str
        """
        allowed_values = ["INLINE", "TAB", "PAGE"]  # noqa: E501
        if display_type not in allowed_values:
            raise ValueError(
                "Invalid value for `display_type` ({0}), must be one of {1}"  # noqa: E501
                .format(display_type, allowed_values)
            )

        self._display_type = display_type

    @property
    def sub_type(self):
        """Gets the sub_type of this Selectors.  # noqa: E501


        :return: The sub_type of this Selectors.  # noqa: E501
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this Selectors.


        :param sub_type: The sub_type of this Selectors.  # noqa: E501
        :type: str
        """

        self._sub_type = sub_type

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
        if issubclass(Selectors, dict):
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
        if not isinstance(other, Selectors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
