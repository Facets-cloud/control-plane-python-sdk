# coding: utf-8

"""
    Api Documentation

    Api Documentation  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProjectTypeMappedResource(object):
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
        'flavor': 'str',
        'intent': 'str',
        'intent_type': 'str'
    }

    attribute_map = {
        'flavor': 'flavor',
        'intent': 'intent',
        'intent_type': 'intentType'
    }

    def __init__(self, flavor=None, intent=None, intent_type=None):  # noqa: E501
        """ProjectTypeMappedResource - a model defined in Swagger"""  # noqa: E501
        self._flavor = None
        self._intent = None
        self._intent_type = None
        self.discriminator = None
        if flavor is not None:
            self.flavor = flavor
        if intent is not None:
            self.intent = intent
        if intent_type is not None:
            self.intent_type = intent_type

    @property
    def flavor(self):
        """Gets the flavor of this ProjectTypeMappedResource.  # noqa: E501


        :return: The flavor of this ProjectTypeMappedResource.  # noqa: E501
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this ProjectTypeMappedResource.


        :param flavor: The flavor of this ProjectTypeMappedResource.  # noqa: E501
        :type: str
        """

        self._flavor = flavor

    @property
    def intent(self):
        """Gets the intent of this ProjectTypeMappedResource.  # noqa: E501


        :return: The intent of this ProjectTypeMappedResource.  # noqa: E501
        :rtype: str
        """
        return self._intent

    @intent.setter
    def intent(self, intent):
        """Sets the intent of this ProjectTypeMappedResource.


        :param intent: The intent of this ProjectTypeMappedResource.  # noqa: E501
        :type: str
        """

        self._intent = intent

    @property
    def intent_type(self):
        """Gets the intent_type of this ProjectTypeMappedResource.  # noqa: E501


        :return: The intent_type of this ProjectTypeMappedResource.  # noqa: E501
        :rtype: str
        """
        return self._intent_type

    @intent_type.setter
    def intent_type(self, intent_type):
        """Sets the intent_type of this ProjectTypeMappedResource.


        :param intent_type: The intent_type of this ProjectTypeMappedResource.  # noqa: E501
        :type: str
        """

        self._intent_type = intent_type

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
        if issubclass(ProjectTypeMappedResource, dict):
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
        if not isinstance(other, ProjectTypeMappedResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
