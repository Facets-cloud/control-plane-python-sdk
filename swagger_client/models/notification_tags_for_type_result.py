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

class NotificationTagsForTypeResult(object):
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
        'label': 'str',
        'tooltip': 'str'
    }

    attribute_map = {
        'id': 'id',
        'label': 'label',
        'tooltip': 'tooltip'
    }

    def __init__(self, id=None, label=None, tooltip=None):  # noqa: E501
        """NotificationTagsForTypeResult - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._label = None
        self._tooltip = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if tooltip is not None:
            self.tooltip = tooltip

    @property
    def id(self):
        """Gets the id of this NotificationTagsForTypeResult.  # noqa: E501


        :return: The id of this NotificationTagsForTypeResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationTagsForTypeResult.


        :param id: The id of this NotificationTagsForTypeResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLUSTER_NAME", "CLUSTER_TYPE", "QASUITE_RESULT", "DR_ACTION", "DR_STATUS", "STACK_NAME", "SEVERITY", "ALERT_NAME", "DEPLOYMENT_STATUS", "APPLICATION_NAME", "SEND_RESOLVED", "RELEASE_TYPE"]  # noqa: E501
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"  # noqa: E501
                .format(id, allowed_values)
            )

        self._id = id

    @property
    def label(self):
        """Gets the label of this NotificationTagsForTypeResult.  # noqa: E501


        :return: The label of this NotificationTagsForTypeResult.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this NotificationTagsForTypeResult.


        :param label: The label of this NotificationTagsForTypeResult.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def tooltip(self):
        """Gets the tooltip of this NotificationTagsForTypeResult.  # noqa: E501


        :return: The tooltip of this NotificationTagsForTypeResult.  # noqa: E501
        :rtype: str
        """
        return self._tooltip

    @tooltip.setter
    def tooltip(self, tooltip):
        """Sets the tooltip of this NotificationTagsForTypeResult.


        :param tooltip: The tooltip of this NotificationTagsForTypeResult.  # noqa: E501
        :type: str
        """

        self._tooltip = tooltip

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
        if issubclass(NotificationTagsForTypeResult, dict):
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
        if not isinstance(other, NotificationTagsForTypeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
