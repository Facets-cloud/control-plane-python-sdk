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

class Result(object):
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
        'error': 'list[Error]',
        'kind': 'str',
        'name': 'str',
        'details': 'str',
        'parent_object': 'str'
    }

    attribute_map = {
        'error': 'error',
        'kind': 'kind',
        'name': 'name',
        'details': 'details',
        'parent_object': 'parentObject'
    }

    def __init__(self, error=None, kind=None, name=None, details=None, parent_object=None):  # noqa: E501
        """Result - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self._kind = None
        self._name = None
        self._details = None
        self._parent_object = None
        self.discriminator = None
        if error is not None:
            self.error = error
        if kind is not None:
            self.kind = kind
        if name is not None:
            self.name = name
        if details is not None:
            self.details = details
        if parent_object is not None:
            self.parent_object = parent_object

    @property
    def error(self):
        """Gets the error of this Result.  # noqa: E501


        :return: The error of this Result.  # noqa: E501
        :rtype: list[Error]
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Result.


        :param error: The error of this Result.  # noqa: E501
        :type: list[Error]
        """

        self._error = error

    @property
    def kind(self):
        """Gets the kind of this Result.  # noqa: E501


        :return: The kind of this Result.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Result.


        :param kind: The kind of this Result.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this Result.  # noqa: E501


        :return: The name of this Result.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Result.


        :param name: The name of this Result.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def details(self):
        """Gets the details of this Result.  # noqa: E501


        :return: The details of this Result.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Result.


        :param details: The details of this Result.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def parent_object(self):
        """Gets the parent_object of this Result.  # noqa: E501


        :return: The parent_object of this Result.  # noqa: E501
        :rtype: str
        """
        return self._parent_object

    @parent_object.setter
    def parent_object(self, parent_object):
        """Sets the parent_object of this Result.


        :param parent_object: The parent_object of this Result.  # noqa: E501
        :type: str
        """

        self._parent_object = parent_object

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
        if issubclass(Result, dict):
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
        if not isinstance(other, Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
