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

class SecurityReportSummary(object):
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
        'low': 'int',
        'high': 'int',
        'medium': 'int',
        'unknown': 'int',
        'critical': 'int'
    }

    attribute_map = {
        'low': 'low',
        'high': 'high',
        'medium': 'medium',
        'unknown': 'unknown',
        'critical': 'critical'
    }

    def __init__(self, low=None, high=None, medium=None, unknown=None, critical=None):  # noqa: E501
        """SecurityReportSummary - a model defined in Swagger"""  # noqa: E501
        self._low = None
        self._high = None
        self._medium = None
        self._unknown = None
        self._critical = None
        self.discriminator = None
        if low is not None:
            self.low = low
        if high is not None:
            self.high = high
        if medium is not None:
            self.medium = medium
        if unknown is not None:
            self.unknown = unknown
        if critical is not None:
            self.critical = critical

    @property
    def low(self):
        """Gets the low of this SecurityReportSummary.  # noqa: E501


        :return: The low of this SecurityReportSummary.  # noqa: E501
        :rtype: int
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this SecurityReportSummary.


        :param low: The low of this SecurityReportSummary.  # noqa: E501
        :type: int
        """

        self._low = low

    @property
    def high(self):
        """Gets the high of this SecurityReportSummary.  # noqa: E501


        :return: The high of this SecurityReportSummary.  # noqa: E501
        :rtype: int
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this SecurityReportSummary.


        :param high: The high of this SecurityReportSummary.  # noqa: E501
        :type: int
        """

        self._high = high

    @property
    def medium(self):
        """Gets the medium of this SecurityReportSummary.  # noqa: E501


        :return: The medium of this SecurityReportSummary.  # noqa: E501
        :rtype: int
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """Sets the medium of this SecurityReportSummary.


        :param medium: The medium of this SecurityReportSummary.  # noqa: E501
        :type: int
        """

        self._medium = medium

    @property
    def unknown(self):
        """Gets the unknown of this SecurityReportSummary.  # noqa: E501


        :return: The unknown of this SecurityReportSummary.  # noqa: E501
        :rtype: int
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        """Sets the unknown of this SecurityReportSummary.


        :param unknown: The unknown of this SecurityReportSummary.  # noqa: E501
        :type: int
        """

        self._unknown = unknown

    @property
    def critical(self):
        """Gets the critical of this SecurityReportSummary.  # noqa: E501


        :return: The critical of this SecurityReportSummary.  # noqa: E501
        :rtype: int
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        """Sets the critical of this SecurityReportSummary.


        :param critical: The critical of this SecurityReportSummary.  # noqa: E501
        :type: int
        """

        self._critical = critical

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
        if issubclass(SecurityReportSummary, dict):
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
        if not isinstance(other, SecurityReportSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
