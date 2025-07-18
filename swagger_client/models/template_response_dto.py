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

class TemplateResponseDTO(object):
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
        'group': 'str',
        'clouds': 'list[str]',
        'type': 'str',
        'display_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'group': 'group',
        'clouds': 'clouds',
        'type': 'type',
        'display_name': 'displayName',
        'description': 'description'
    }

    def __init__(self, name=None, group=None, clouds=None, type=None, display_name=None, description=None):  # noqa: E501
        """TemplateResponseDTO - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._group = None
        self._clouds = None
        self._type = None
        self._display_name = None
        self._description = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if group is not None:
            self.group = group
        if clouds is not None:
            self.clouds = clouds
        if type is not None:
            self.type = type
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this TemplateResponseDTO.  # noqa: E501


        :return: The name of this TemplateResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateResponseDTO.


        :param name: The name of this TemplateResponseDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def group(self):
        """Gets the group of this TemplateResponseDTO.  # noqa: E501


        :return: The group of this TemplateResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this TemplateResponseDTO.


        :param group: The group of this TemplateResponseDTO.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def clouds(self):
        """Gets the clouds of this TemplateResponseDTO.  # noqa: E501


        :return: The clouds of this TemplateResponseDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._clouds

    @clouds.setter
    def clouds(self, clouds):
        """Sets the clouds of this TemplateResponseDTO.


        :param clouds: The clouds of this TemplateResponseDTO.  # noqa: E501
        :type: list[str]
        """

        self._clouds = clouds

    @property
    def type(self):
        """Gets the type of this TemplateResponseDTO.  # noqa: E501


        :return: The type of this TemplateResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TemplateResponseDTO.


        :param type: The type of this TemplateResponseDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["MULTI_INSTANCE", "SINGLE_INSTANCE", "AUTO_INJECT"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def display_name(self):
        """Gets the display_name of this TemplateResponseDTO.  # noqa: E501


        :return: The display_name of this TemplateResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TemplateResponseDTO.


        :param display_name: The display_name of this TemplateResponseDTO.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this TemplateResponseDTO.  # noqa: E501


        :return: The description of this TemplateResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateResponseDTO.


        :param description: The description of this TemplateResponseDTO.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(TemplateResponseDTO, dict):
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
        if not isinstance(other, TemplateResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
