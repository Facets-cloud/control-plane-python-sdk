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

class UserVCSTokenResponse(object):
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
        'user_id': 'str',
        'host_name': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'userId',
        'host_name': 'hostName',
        'user_name': 'userName'
    }

    def __init__(self, id=None, user_id=None, host_name=None, user_name=None):  # noqa: E501
        """UserVCSTokenResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._user_id = None
        self._host_name = None
        self._user_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if host_name is not None:
            self.host_name = host_name
        if user_name is not None:
            self.user_name = user_name

    @property
    def id(self):
        """Gets the id of this UserVCSTokenResponse.  # noqa: E501


        :return: The id of this UserVCSTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserVCSTokenResponse.


        :param id: The id of this UserVCSTokenResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this UserVCSTokenResponse.  # noqa: E501


        :return: The user_id of this UserVCSTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserVCSTokenResponse.


        :param user_id: The user_id of this UserVCSTokenResponse.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def host_name(self):
        """Gets the host_name of this UserVCSTokenResponse.  # noqa: E501


        :return: The host_name of this UserVCSTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this UserVCSTokenResponse.


        :param host_name: The host_name of this UserVCSTokenResponse.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def user_name(self):
        """Gets the user_name of this UserVCSTokenResponse.  # noqa: E501


        :return: The user_name of this UserVCSTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserVCSTokenResponse.


        :param user_name: The user_name of this UserVCSTokenResponse.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(UserVCSTokenResponse, dict):
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
        if not isinstance(other, UserVCSTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
