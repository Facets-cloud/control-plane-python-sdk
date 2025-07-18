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

class DeploymentStatusCountDto(object):
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
        '_date': 'date',
        'status': 'str',
        'count': 'int'
    }

    attribute_map = {
        '_date': 'date',
        'status': 'status',
        'count': 'count'
    }

    def __init__(self, _date=None, status=None, count=None):  # noqa: E501
        """DeploymentStatusCountDto - a model defined in Swagger"""  # noqa: E501
        self.__date = None
        self._status = None
        self._count = None
        self.discriminator = None
        if _date is not None:
            self._date = _date
        if status is not None:
            self.status = status
        if count is not None:
            self.count = count

    @property
    def _date(self):
        """Gets the _date of this DeploymentStatusCountDto.  # noqa: E501


        :return: The _date of this DeploymentStatusCountDto.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this DeploymentStatusCountDto.


        :param _date: The _date of this DeploymentStatusCountDto.  # noqa: E501
        :type: date
        """

        self.__date = _date

    @property
    def status(self):
        """Gets the status of this DeploymentStatusCountDto.  # noqa: E501


        :return: The status of this DeploymentStatusCountDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeploymentStatusCountDto.


        :param status: The status of this DeploymentStatusCountDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCEEDED", "FAILED", "FAULT", "TIMED_OUT", "IN_PROGRESS", "STOPPED", "INVALID", "STARTED", "UNKNOWN", "QUEUED", "PENDING_APPROVAL", "APPROVED", "REJECTED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def count(self):
        """Gets the count of this DeploymentStatusCountDto.  # noqa: E501


        :return: The count of this DeploymentStatusCountDto.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this DeploymentStatusCountDto.


        :param count: The count of this DeploymentStatusCountDto.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if issubclass(DeploymentStatusCountDto, dict):
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
        if not isinstance(other, DeploymentStatusCountDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
