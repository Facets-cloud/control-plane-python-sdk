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

class ApplicationAction(object):
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
        'action_type': 'str',
        'application_id': 'str',
        'arguments': 'str',
        'arguments_regex': 'str',
        'build_type': 'str',
        'id': 'str',
        'metadata': 'object',
        'name': 'str',
        'path': 'str'
    }

    attribute_map = {
        'action_type': 'actionType',
        'application_id': 'applicationId',
        'arguments': 'arguments',
        'arguments_regex': 'argumentsRegex',
        'build_type': 'buildType',
        'id': 'id',
        'metadata': 'metadata',
        'name': 'name',
        'path': 'path'
    }

    def __init__(self, action_type=None, application_id=None, arguments=None, arguments_regex=None, build_type=None, id=None, metadata=None, name=None, path=None):  # noqa: E501
        """ApplicationAction - a model defined in Swagger"""  # noqa: E501
        self._action_type = None
        self._application_id = None
        self._arguments = None
        self._arguments_regex = None
        self._build_type = None
        self._id = None
        self._metadata = None
        self._name = None
        self._path = None
        self.discriminator = None
        if action_type is not None:
            self.action_type = action_type
        if application_id is not None:
            self.application_id = application_id
        if arguments is not None:
            self.arguments = arguments
        if arguments_regex is not None:
            self.arguments_regex = arguments_regex
        if build_type is not None:
            self.build_type = build_type
        if id is not None:
            self.id = id
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path

    @property
    def action_type(self):
        """Gets the action_type of this ApplicationAction.  # noqa: E501


        :return: The action_type of this ApplicationAction.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this ApplicationAction.


        :param action_type: The action_type of this ApplicationAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["GENERIC", "CUSTOM"]  # noqa: E501
        if action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"  # noqa: E501
                .format(action_type, allowed_values)
            )

        self._action_type = action_type

    @property
    def application_id(self):
        """Gets the application_id of this ApplicationAction.  # noqa: E501


        :return: The application_id of this ApplicationAction.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApplicationAction.


        :param application_id: The application_id of this ApplicationAction.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def arguments(self):
        """Gets the arguments of this ApplicationAction.  # noqa: E501


        :return: The arguments of this ApplicationAction.  # noqa: E501
        :rtype: str
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this ApplicationAction.


        :param arguments: The arguments of this ApplicationAction.  # noqa: E501
        :type: str
        """

        self._arguments = arguments

    @property
    def arguments_regex(self):
        """Gets the arguments_regex of this ApplicationAction.  # noqa: E501


        :return: The arguments_regex of this ApplicationAction.  # noqa: E501
        :rtype: str
        """
        return self._arguments_regex

    @arguments_regex.setter
    def arguments_regex(self, arguments_regex):
        """Sets the arguments_regex of this ApplicationAction.


        :param arguments_regex: The arguments_regex of this ApplicationAction.  # noqa: E501
        :type: str
        """

        self._arguments_regex = arguments_regex

    @property
    def build_type(self):
        """Gets the build_type of this ApplicationAction.  # noqa: E501


        :return: The build_type of this ApplicationAction.  # noqa: E501
        :rtype: str
        """
        return self._build_type

    @build_type.setter
    def build_type(self, build_type):
        """Sets the build_type of this ApplicationAction.


        :param build_type: The build_type of this ApplicationAction.  # noqa: E501
        :type: str
        """
        allowed_values = ["MVN", "MVN_SONAR_BRANCH", "MVN_SONAR_BRANCH_UT_STRICT", "JDK11_MAVEN3", "JDK11_MVN3_SONAR_BRANCH", "JDK17_MVN3_SONAR_BRANCH", "JDK17_MVN3_SONAR_BRANCH_OVERLAY2", "JDK17_MVN3_LIBRARY_SONAR_BRANCH", "JAVA8_LIBRARY", "JAVA8_LIBRARY_SONAR_BRANCH", "FREESTYLE_DOCKER", "DOTNET_CORE", "MVN_IONIC", "MVN_IONIC_SONAR_BRANCH", "JDK6_MAVEN2", "MJ_NUGET", "DOTNET_CORE22", "DOTNET_CORE3", "SBT", "NPM", "NPM_SONAR_BRANCH", "NPM_LTS_V18_SONAR_BRANCH", "NPM_UI", "NPM_UI_SONAR_BRANCH", "NPM_UI_V14_SONAR_BRANCH", "THRIFT8_LIBRARY", "THRIFT9_LIBRARY", "THRIFT8_WITH_FLAGS_LIBRARY", "SCALA_LIBRARY", "CHEETAH_LIBRARY", "SHARINGAN_LIBRARY", "NPM_LTS_V20_SONAR_BRANCH", "JDK11_MVN3_LIBRARY_SONAR_BRANCH", "JDK21_MVN3_LIBRARY_SONAR_BRANCH", "JDK21_MVN3_SONAR_BRANCH"]  # noqa: E501
        if build_type not in allowed_values:
            raise ValueError(
                "Invalid value for `build_type` ({0}), must be one of {1}"  # noqa: E501
                .format(build_type, allowed_values)
            )

        self._build_type = build_type

    @property
    def id(self):
        """Gets the id of this ApplicationAction.  # noqa: E501


        :return: The id of this ApplicationAction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationAction.


        :param id: The id of this ApplicationAction.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this ApplicationAction.  # noqa: E501


        :return: The metadata of this ApplicationAction.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ApplicationAction.


        :param metadata: The metadata of this ApplicationAction.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this ApplicationAction.  # noqa: E501


        :return: The name of this ApplicationAction.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationAction.


        :param name: The name of this ApplicationAction.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this ApplicationAction.  # noqa: E501


        :return: The path of this ApplicationAction.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ApplicationAction.


        :param path: The path of this ApplicationAction.  # noqa: E501
        :type: str
        """

        self._path = path

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
        if issubclass(ApplicationAction, dict):
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
        if not isinstance(other, ApplicationAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
