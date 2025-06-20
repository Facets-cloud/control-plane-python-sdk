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

class DaemonSetDTO(object):
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
        'desired': 'int',
        'current': 'int',
        'ready': 'int',
        'up_to_date': 'int',
        'available': 'int',
        'node_selector': 'dict(str, str)',
        'age_in_seconds': 'int'
    }

    attribute_map = {
        'name': 'name',
        'desired': 'desired',
        'current': 'current',
        'ready': 'ready',
        'up_to_date': 'upToDate',
        'available': 'available',
        'node_selector': 'nodeSelector',
        'age_in_seconds': 'ageInSeconds'
    }

    def __init__(self, name=None, desired=None, current=None, ready=None, up_to_date=None, available=None, node_selector=None, age_in_seconds=None):  # noqa: E501
        """DaemonSetDTO - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._desired = None
        self._current = None
        self._ready = None
        self._up_to_date = None
        self._available = None
        self._node_selector = None
        self._age_in_seconds = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if desired is not None:
            self.desired = desired
        if current is not None:
            self.current = current
        if ready is not None:
            self.ready = ready
        if up_to_date is not None:
            self.up_to_date = up_to_date
        if available is not None:
            self.available = available
        if node_selector is not None:
            self.node_selector = node_selector
        if age_in_seconds is not None:
            self.age_in_seconds = age_in_seconds

    @property
    def name(self):
        """Gets the name of this DaemonSetDTO.  # noqa: E501


        :return: The name of this DaemonSetDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DaemonSetDTO.


        :param name: The name of this DaemonSetDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def desired(self):
        """Gets the desired of this DaemonSetDTO.  # noqa: E501


        :return: The desired of this DaemonSetDTO.  # noqa: E501
        :rtype: int
        """
        return self._desired

    @desired.setter
    def desired(self, desired):
        """Sets the desired of this DaemonSetDTO.


        :param desired: The desired of this DaemonSetDTO.  # noqa: E501
        :type: int
        """

        self._desired = desired

    @property
    def current(self):
        """Gets the current of this DaemonSetDTO.  # noqa: E501


        :return: The current of this DaemonSetDTO.  # noqa: E501
        :rtype: int
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this DaemonSetDTO.


        :param current: The current of this DaemonSetDTO.  # noqa: E501
        :type: int
        """

        self._current = current

    @property
    def ready(self):
        """Gets the ready of this DaemonSetDTO.  # noqa: E501


        :return: The ready of this DaemonSetDTO.  # noqa: E501
        :rtype: int
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this DaemonSetDTO.


        :param ready: The ready of this DaemonSetDTO.  # noqa: E501
        :type: int
        """

        self._ready = ready

    @property
    def up_to_date(self):
        """Gets the up_to_date of this DaemonSetDTO.  # noqa: E501


        :return: The up_to_date of this DaemonSetDTO.  # noqa: E501
        :rtype: int
        """
        return self._up_to_date

    @up_to_date.setter
    def up_to_date(self, up_to_date):
        """Sets the up_to_date of this DaemonSetDTO.


        :param up_to_date: The up_to_date of this DaemonSetDTO.  # noqa: E501
        :type: int
        """

        self._up_to_date = up_to_date

    @property
    def available(self):
        """Gets the available of this DaemonSetDTO.  # noqa: E501


        :return: The available of this DaemonSetDTO.  # noqa: E501
        :rtype: int
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this DaemonSetDTO.


        :param available: The available of this DaemonSetDTO.  # noqa: E501
        :type: int
        """

        self._available = available

    @property
    def node_selector(self):
        """Gets the node_selector of this DaemonSetDTO.  # noqa: E501


        :return: The node_selector of this DaemonSetDTO.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this DaemonSetDTO.


        :param node_selector: The node_selector of this DaemonSetDTO.  # noqa: E501
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def age_in_seconds(self):
        """Gets the age_in_seconds of this DaemonSetDTO.  # noqa: E501


        :return: The age_in_seconds of this DaemonSetDTO.  # noqa: E501
        :rtype: int
        """
        return self._age_in_seconds

    @age_in_seconds.setter
    def age_in_seconds(self, age_in_seconds):
        """Sets the age_in_seconds of this DaemonSetDTO.


        :param age_in_seconds: The age_in_seconds of this DaemonSetDTO.  # noqa: E501
        :type: int
        """

        self._age_in_seconds = age_in_seconds

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
        if issubclass(DaemonSetDTO, dict):
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
        if not isinstance(other, DaemonSetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
