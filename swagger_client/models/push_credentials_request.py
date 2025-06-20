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

class PushCredentialsRequest(object):
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
        'blueprint_name': 'str',
        'artifactory': 'str',
        'application_name': 'str'
    }

    attribute_map = {
        'blueprint_name': 'blueprintName',
        'artifactory': 'artifactory',
        'application_name': 'applicationName'
    }

    def __init__(self, blueprint_name=None, artifactory=None, application_name=None):  # noqa: E501
        """PushCredentialsRequest - a model defined in Swagger"""  # noqa: E501
        self._blueprint_name = None
        self._artifactory = None
        self._application_name = None
        self.discriminator = None
        self.blueprint_name = blueprint_name
        self.artifactory = artifactory
        self.application_name = application_name

    @property
    def blueprint_name(self):
        """Gets the blueprint_name of this PushCredentialsRequest.  # noqa: E501

        Blueprint name for which credentials are requested.  # noqa: E501

        :return: The blueprint_name of this PushCredentialsRequest.  # noqa: E501
        :rtype: str
        """
        return self._blueprint_name

    @blueprint_name.setter
    def blueprint_name(self, blueprint_name):
        """Sets the blueprint_name of this PushCredentialsRequest.

        Blueprint name for which credentials are requested.  # noqa: E501

        :param blueprint_name: The blueprint_name of this PushCredentialsRequest.  # noqa: E501
        :type: str
        """
        if blueprint_name is None:
            raise ValueError("Invalid value for `blueprint_name`, must not be `None`")  # noqa: E501

        self._blueprint_name = blueprint_name

    @property
    def artifactory(self):
        """Gets the artifactory of this PushCredentialsRequest.  # noqa: E501

        Name of the artifactory.  # noqa: E501

        :return: The artifactory of this PushCredentialsRequest.  # noqa: E501
        :rtype: str
        """
        return self._artifactory

    @artifactory.setter
    def artifactory(self, artifactory):
        """Sets the artifactory of this PushCredentialsRequest.

        Name of the artifactory.  # noqa: E501

        :param artifactory: The artifactory of this PushCredentialsRequest.  # noqa: E501
        :type: str
        """
        if artifactory is None:
            raise ValueError("Invalid value for `artifactory`, must not be `None`")  # noqa: E501

        self._artifactory = artifactory

    @property
    def application_name(self):
        """Gets the application_name of this PushCredentialsRequest.  # noqa: E501

        Application name associated with the request.  # noqa: E501

        :return: The application_name of this PushCredentialsRequest.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this PushCredentialsRequest.

        Application name associated with the request.  # noqa: E501

        :param application_name: The application_name of this PushCredentialsRequest.  # noqa: E501
        :type: str
        """
        if application_name is None:
            raise ValueError("Invalid value for `application_name`, must not be `None`")  # noqa: E501

        self._application_name = application_name

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
        if issubclass(PushCredentialsRequest, dict):
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
        if not isinstance(other, PushCredentialsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
