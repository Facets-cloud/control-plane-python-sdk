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

class WebComponentDTO(object):
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
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'remote_url': 'str',
        'icon_url': 'str',
        'enabled': 'bool',
        'tooltip': 'str',
        'order': 'int',
        'contextual_attributes': 'dict(str, object)',
        'last_modified_date': 'datetime',
        'last_modified_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'remote_url': 'remoteURL',
        'icon_url': 'iconURL',
        'enabled': 'enabled',
        'tooltip': 'tooltip',
        'order': 'order',
        'contextual_attributes': 'contextualAttributes',
        'last_modified_date': 'lastModifiedDate',
        'last_modified_by': 'lastModifiedBy'
    }

    def __init__(self, id=None, name=None, type=None, remote_url=None, icon_url=None, enabled=None, tooltip=None, order=None, contextual_attributes=None, last_modified_date=None, last_modified_by=None):  # noqa: E501
        """WebComponentDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._type = None
        self._remote_url = None
        self._icon_url = None
        self._enabled = None
        self._tooltip = None
        self._order = None
        self._contextual_attributes = None
        self._last_modified_date = None
        self._last_modified_by = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        self.type = type
        self.remote_url = remote_url
        if icon_url is not None:
            self.icon_url = icon_url
        self.enabled = enabled
        if tooltip is not None:
            self.tooltip = tooltip
        if order is not None:
            self.order = order
        if contextual_attributes is not None:
            self.contextual_attributes = contextual_attributes
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by

    @property
    def id(self):
        """Gets the id of this WebComponentDTO.  # noqa: E501

        Unique identifier for the web component  # noqa: E501

        :return: The id of this WebComponentDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebComponentDTO.

        Unique identifier for the web component  # noqa: E501

        :param id: The id of this WebComponentDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this WebComponentDTO.  # noqa: E501

        Unique identifier for the web component  # noqa: E501

        :return: The name of this WebComponentDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebComponentDTO.

        Unique identifier for the web component  # noqa: E501

        :param name: The name of this WebComponentDTO.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this WebComponentDTO.  # noqa: E501

        Type of web component (NAV_TYPE or TAB_TYPE)  # noqa: E501

        :return: The type of this WebComponentDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebComponentDTO.

        Type of web component (NAV_TYPE or TAB_TYPE)  # noqa: E501

        :param type: The type of this WebComponentDTO.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["NAV_APP", "TAB_APP"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def remote_url(self):
        """Gets the remote_url of this WebComponentDTO.  # noqa: E501

        Hosted location of the component script  # noqa: E501

        :return: The remote_url of this WebComponentDTO.  # noqa: E501
        :rtype: str
        """
        return self._remote_url

    @remote_url.setter
    def remote_url(self, remote_url):
        """Sets the remote_url of this WebComponentDTO.

        Hosted location of the component script  # noqa: E501

        :param remote_url: The remote_url of this WebComponentDTO.  # noqa: E501
        :type: str
        """
        if remote_url is None:
            raise ValueError("Invalid value for `remote_url`, must not be `None`")  # noqa: E501

        self._remote_url = remote_url

    @property
    def icon_url(self):
        """Gets the icon_url of this WebComponentDTO.  # noqa: E501

        URL of the icon to be displayed in the UI  # noqa: E501

        :return: The icon_url of this WebComponentDTO.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this WebComponentDTO.

        URL of the icon to be displayed in the UI  # noqa: E501

        :param icon_url: The icon_url of this WebComponentDTO.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

    @property
    def enabled(self):
        """Gets the enabled of this WebComponentDTO.  # noqa: E501

        Flag to enable/disable component visibility  # noqa: E501

        :return: The enabled of this WebComponentDTO.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this WebComponentDTO.

        Flag to enable/disable component visibility  # noqa: E501

        :param enabled: The enabled of this WebComponentDTO.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def tooltip(self):
        """Gets the tooltip of this WebComponentDTO.  # noqa: E501

        Tooltip text to display on hover  # noqa: E501

        :return: The tooltip of this WebComponentDTO.  # noqa: E501
        :rtype: str
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """Sets the tooltip of this WebComponentDTO.

        Tooltip text to display on hover  # noqa: E501

        :param tooltip: The tooltip of this WebComponentDTO.  # noqa: E501
        :type: str
        """

        self._tooltip = tooltip

    @property
    def order(self):
        """Gets the order of this WebComponentDTO.  # noqa: E501

        Position priority of the component  # noqa: E501

        :return: The order of this WebComponentDTO.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this WebComponentDTO.

        Position priority of the component  # noqa: E501

        :param order: The order of this WebComponentDTO.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def contextual_attributes(self):
        """Gets the contextual_attributes of this WebComponentDTO.  # noqa: E501

        Additional contextual attributes for component configuration  # noqa: E501

        :return: The contextual_attributes of this WebComponentDTO.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._contextual_attributes

    @contextual_attributes.setter
    def contextual_attributes(self, contextual_attributes):
        """Sets the contextual_attributes of this WebComponentDTO.

        Additional contextual attributes for component configuration  # noqa: E501

        :param contextual_attributes: The contextual_attributes of this WebComponentDTO.  # noqa: E501
        :type: dict(str, object)
        """

        self._contextual_attributes = contextual_attributes

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this WebComponentDTO.  # noqa: E501


        :return: The last_modified_date of this WebComponentDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this WebComponentDTO.


        :param last_modified_date: The last_modified_date of this WebComponentDTO.  # noqa: E501
        :type: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this WebComponentDTO.  # noqa: E501


        :return: The last_modified_by of this WebComponentDTO.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this WebComponentDTO.


        :param last_modified_by: The last_modified_by of this WebComponentDTO.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

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
        if issubclass(WebComponentDTO, dict):
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
        if not isinstance(other, WebComponentDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
