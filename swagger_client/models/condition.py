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

class Condition(object):
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
        'error_threshold': 'str',
        'metric': 'str',
        'metric_label': 'str',
        'operator': 'str',
        'status': 'str',
        'value': 'str'
    }

    attribute_map = {
        'error_threshold': 'errorThreshold',
        'metric': 'metric',
        'metric_label': 'metricLabel',
        'operator': 'operator',
        'status': 'status',
        'value': 'value'
    }

    def __init__(self, error_threshold=None, metric=None, metric_label=None, operator=None, status=None, value=None):  # noqa: E501
        """Condition - a model defined in Swagger"""  # noqa: E501
        self._error_threshold = None
        self._metric = None
        self._metric_label = None
        self._operator = None
        self._status = None
        self._value = None
        self.discriminator = None
        if error_threshold is not None:
            self.error_threshold = error_threshold
        if metric is not None:
            self.metric = metric
        if metric_label is not None:
            self.metric_label = metric_label
        if operator is not None:
            self.operator = operator
        if status is not None:
            self.status = status
        if value is not None:
            self.value = value

    @property
    def error_threshold(self):
        """Gets the error_threshold of this Condition.  # noqa: E501


        :return: The error_threshold of this Condition.  # noqa: E501
        :rtype: str
        """
        return self._error_threshold

    @error_threshold.setter
    def error_threshold(self, error_threshold):
        """Sets the error_threshold of this Condition.


        :param error_threshold: The error_threshold of this Condition.  # noqa: E501
        :type: str
        """

        self._error_threshold = error_threshold

    @property
    def metric(self):
        """Gets the metric of this Condition.  # noqa: E501


        :return: The metric of this Condition.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this Condition.


        :param metric: The metric of this Condition.  # noqa: E501
        :type: str
        """

        self._metric = metric

    @property
    def metric_label(self):
        """Gets the metric_label of this Condition.  # noqa: E501


        :return: The metric_label of this Condition.  # noqa: E501
        :rtype: str
        """
        return self._metric_label

    @metric_label.setter
    def metric_label(self, metric_label):
        """Sets the metric_label of this Condition.


        :param metric_label: The metric_label of this Condition.  # noqa: E501
        :type: str
        """

        self._metric_label = metric_label

    @property
    def operator(self):
        """Gets the operator of this Condition.  # noqa: E501


        :return: The operator of this Condition.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this Condition.


        :param operator: The operator of this Condition.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def status(self):
        """Gets the status of this Condition.  # noqa: E501


        :return: The status of this Condition.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Condition.


        :param status: The status of this Condition.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def value(self):
        """Gets the value of this Condition.  # noqa: E501


        :return: The value of this Condition.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Condition.


        :param value: The value of this Condition.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(Condition, dict):
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
        if not isinstance(other, Condition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
