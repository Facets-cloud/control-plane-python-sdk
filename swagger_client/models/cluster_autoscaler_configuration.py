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

class ClusterAutoscalerConfiguration(object):
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
        'autoscaling_group': 'str',
        'max_size': 'int',
        'min_size': 'int'
    }

    attribute_map = {
        'autoscaling_group': 'autoscalingGroup',
        'max_size': 'maxSize',
        'min_size': 'minSize'
    }

    def __init__(self, autoscaling_group=None, max_size=None, min_size=None):  # noqa: E501
        """ClusterAutoscalerConfiguration - a model defined in Swagger"""  # noqa: E501
        self._autoscaling_group = None
        self._max_size = None
        self._min_size = None
        self.discriminator = None
        if autoscaling_group is not None:
            self.autoscaling_group = autoscaling_group
        if max_size is not None:
            self.max_size = max_size
        if min_size is not None:
            self.min_size = min_size

    @property
    def autoscaling_group(self):
        """Gets the autoscaling_group of this ClusterAutoscalerConfiguration.  # noqa: E501


        :return: The autoscaling_group of this ClusterAutoscalerConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._autoscaling_group

    @autoscaling_group.setter
    def autoscaling_group(self, autoscaling_group):
        """Sets the autoscaling_group of this ClusterAutoscalerConfiguration.


        :param autoscaling_group: The autoscaling_group of this ClusterAutoscalerConfiguration.  # noqa: E501
        :type: str
        """

        self._autoscaling_group = autoscaling_group

    @property
    def max_size(self):
        """Gets the max_size of this ClusterAutoscalerConfiguration.  # noqa: E501


        :return: The max_size of this ClusterAutoscalerConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        """Sets the max_size of this ClusterAutoscalerConfiguration.


        :param max_size: The max_size of this ClusterAutoscalerConfiguration.  # noqa: E501
        :type: int
        """

        self._max_size = max_size

    @property
    def min_size(self):
        """Gets the min_size of this ClusterAutoscalerConfiguration.  # noqa: E501


        :return: The min_size of this ClusterAutoscalerConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._min_size

    @min_size.setter
    def min_size(self, min_size):
        """Sets the min_size of this ClusterAutoscalerConfiguration.


        :param min_size: The min_size of this ClusterAutoscalerConfiguration.  # noqa: E501
        :type: int
        """

        self._min_size = min_size

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
        if issubclass(ClusterAutoscalerConfiguration, dict):
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
        if not isinstance(other, ClusterAutoscalerConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
