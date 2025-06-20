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

class IntentResponseDTO(object):
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
        'type': 'str',
        'display_name': 'str',
        'intent_outputs': 'list[IntentOutput]',
        'source': 'str',
        'description': 'str',
        'icon_url': 'str',
        'inferred_from_module': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'display_name': 'displayName',
        'intent_outputs': 'intentOutputs',
        'source': 'source',
        'description': 'description',
        'icon_url': 'iconUrl',
        'inferred_from_module': 'inferredFromModule'
    }

    def __init__(self, name=None, type=None, display_name=None, intent_outputs=None, source=None, description=None, icon_url=None, inferred_from_module=None):  # noqa: E501
        """IntentResponseDTO - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._display_name = None
        self._intent_outputs = None
        self._source = None
        self._description = None
        self._icon_url = None
        self._inferred_from_module = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if display_name is not None:
            self.display_name = display_name
        if intent_outputs is not None:
            self.intent_outputs = intent_outputs
        if source is not None:
            self.source = source
        if description is not None:
            self.description = description
        if icon_url is not None:
            self.icon_url = icon_url
        if inferred_from_module is not None:
            self.inferred_from_module = inferred_from_module

    @property
    def name(self):
        """Gets the name of this IntentResponseDTO.  # noqa: E501


        :return: The name of this IntentResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IntentResponseDTO.


        :param name: The name of this IntentResponseDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this IntentResponseDTO.  # noqa: E501


        :return: The type of this IntentResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IntentResponseDTO.


        :param type: The type of this IntentResponseDTO.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def display_name(self):
        """Gets the display_name of this IntentResponseDTO.  # noqa: E501


        :return: The display_name of this IntentResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this IntentResponseDTO.


        :param display_name: The display_name of this IntentResponseDTO.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def intent_outputs(self):
        """Gets the intent_outputs of this IntentResponseDTO.  # noqa: E501


        :return: The intent_outputs of this IntentResponseDTO.  # noqa: E501
        :rtype: list[IntentOutput]
        """
        return self._intent_outputs

    @intent_outputs.setter
    def intent_outputs(self, intent_outputs):
        """Sets the intent_outputs of this IntentResponseDTO.


        :param intent_outputs: The intent_outputs of this IntentResponseDTO.  # noqa: E501
        :type: list[IntentOutput]
        """

        self._intent_outputs = intent_outputs

    @property
    def source(self):
        """Gets the source of this IntentResponseDTO.  # noqa: E501


        :return: The source of this IntentResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this IntentResponseDTO.


        :param source: The source of this IntentResponseDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["BUILT_IN", "CUSTOM"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def description(self):
        """Gets the description of this IntentResponseDTO.  # noqa: E501


        :return: The description of this IntentResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IntentResponseDTO.


        :param description: The description of this IntentResponseDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def icon_url(self):
        """Gets the icon_url of this IntentResponseDTO.  # noqa: E501


        :return: The icon_url of this IntentResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this IntentResponseDTO.


        :param icon_url: The icon_url of this IntentResponseDTO.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

    @property
    def inferred_from_module(self):
        """Gets the inferred_from_module of this IntentResponseDTO.  # noqa: E501


        :return: The inferred_from_module of this IntentResponseDTO.  # noqa: E501
        :rtype: bool
        """
        return self._inferred_from_module

    @inferred_from_module.setter
    def inferred_from_module(self, inferred_from_module):
        """Sets the inferred_from_module of this IntentResponseDTO.


        :param inferred_from_module: The inferred_from_module of this IntentResponseDTO.  # noqa: E501
        :type: bool
        """

        self._inferred_from_module = inferred_from_module

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
        if issubclass(IntentResponseDTO, dict):
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
        if not isinstance(other, IntentResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
