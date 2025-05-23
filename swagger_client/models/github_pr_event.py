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

class GithubPREvent(object):
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
        'action': 'str',
        'number': 'int',
        'pull_request': 'GithubPRField'
    }

    attribute_map = {
        'action': 'action',
        'number': 'number',
        'pull_request': 'pull_request'
    }

    def __init__(self, action=None, number=None, pull_request=None):  # noqa: E501
        """GithubPREvent - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._number = None
        self._pull_request = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if number is not None:
            self.number = number
        if pull_request is not None:
            self.pull_request = pull_request

    @property
    def action(self):
        """Gets the action of this GithubPREvent.  # noqa: E501


        :return: The action of this GithubPREvent.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this GithubPREvent.


        :param action: The action of this GithubPREvent.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def number(self):
        """Gets the number of this GithubPREvent.  # noqa: E501


        :return: The number of this GithubPREvent.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this GithubPREvent.


        :param number: The number of this GithubPREvent.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def pull_request(self):
        """Gets the pull_request of this GithubPREvent.  # noqa: E501


        :return: The pull_request of this GithubPREvent.  # noqa: E501
        :rtype: GithubPRField
        """
        return self._pull_request

    @pull_request.setter
    def pull_request(self, pull_request):
        """Sets the pull_request of this GithubPREvent.


        :param pull_request: The pull_request of this GithubPREvent.  # noqa: E501
        :type: GithubPRField
        """

        self._pull_request = pull_request

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
        if issubclass(GithubPREvent, dict):
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
        if not isinstance(other, GithubPREvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
