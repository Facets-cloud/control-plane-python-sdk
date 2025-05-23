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

class ExpandedUser(object):
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
        'accessible_accounts': 'list[IdName]',
        'accessible_environments': 'list[EnvInfo]',
        'accessible_projects': 'list[str]',
        'associated_resource_groups': 'list[IdName]',
        'base_role': 'RoleInfo',
        'env_specific_roles': 'list[EnvSpecificAccess]',
        'groups': 'list[IdName]',
        'picture': 'str',
        'user_id': 'str',
        'user_roles': 'list[RoleInfo]',
        'username': 'str'
    }

    attribute_map = {
        'accessible_accounts': 'accessibleAccounts',
        'accessible_environments': 'accessibleEnvironments',
        'accessible_projects': 'accessibleProjects',
        'associated_resource_groups': 'associatedResourceGroups',
        'base_role': 'baseRole',
        'env_specific_roles': 'envSpecificRoles',
        'groups': 'groups',
        'picture': 'picture',
        'user_id': 'userId',
        'user_roles': 'userRoles',
        'username': 'username'
    }

    def __init__(self, accessible_accounts=None, accessible_environments=None, accessible_projects=None, associated_resource_groups=None, base_role=None, env_specific_roles=None, groups=None, picture=None, user_id=None, user_roles=None, username=None):  # noqa: E501
        """ExpandedUser - a model defined in Swagger"""  # noqa: E501
        self._accessible_accounts = None
        self._accessible_environments = None
        self._accessible_projects = None
        self._associated_resource_groups = None
        self._base_role = None
        self._env_specific_roles = None
        self._groups = None
        self._picture = None
        self._user_id = None
        self._user_roles = None
        self._username = None
        self.discriminator = None
        if accessible_accounts is not None:
            self.accessible_accounts = accessible_accounts
        if accessible_environments is not None:
            self.accessible_environments = accessible_environments
        if accessible_projects is not None:
            self.accessible_projects = accessible_projects
        if associated_resource_groups is not None:
            self.associated_resource_groups = associated_resource_groups
        if base_role is not None:
            self.base_role = base_role
        if env_specific_roles is not None:
            self.env_specific_roles = env_specific_roles
        if groups is not None:
            self.groups = groups
        if picture is not None:
            self.picture = picture
        if user_id is not None:
            self.user_id = user_id
        if user_roles is not None:
            self.user_roles = user_roles
        if username is not None:
            self.username = username

    @property
    def accessible_accounts(self):
        """Gets the accessible_accounts of this ExpandedUser.  # noqa: E501


        :return: The accessible_accounts of this ExpandedUser.  # noqa: E501
        :rtype: list[IdName]
        """
        return self._accessible_accounts

    @accessible_accounts.setter
    def accessible_accounts(self, accessible_accounts):
        """Sets the accessible_accounts of this ExpandedUser.


        :param accessible_accounts: The accessible_accounts of this ExpandedUser.  # noqa: E501
        :type: list[IdName]
        """

        self._accessible_accounts = accessible_accounts

    @property
    def accessible_environments(self):
        """Gets the accessible_environments of this ExpandedUser.  # noqa: E501


        :return: The accessible_environments of this ExpandedUser.  # noqa: E501
        :rtype: list[EnvInfo]
        """
        return self._accessible_environments

    @accessible_environments.setter
    def accessible_environments(self, accessible_environments):
        """Sets the accessible_environments of this ExpandedUser.


        :param accessible_environments: The accessible_environments of this ExpandedUser.  # noqa: E501
        :type: list[EnvInfo]
        """

        self._accessible_environments = accessible_environments

    @property
    def accessible_projects(self):
        """Gets the accessible_projects of this ExpandedUser.  # noqa: E501


        :return: The accessible_projects of this ExpandedUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._accessible_projects

    @accessible_projects.setter
    def accessible_projects(self, accessible_projects):
        """Sets the accessible_projects of this ExpandedUser.


        :param accessible_projects: The accessible_projects of this ExpandedUser.  # noqa: E501
        :type: list[str]
        """

        self._accessible_projects = accessible_projects

    @property
    def associated_resource_groups(self):
        """Gets the associated_resource_groups of this ExpandedUser.  # noqa: E501


        :return: The associated_resource_groups of this ExpandedUser.  # noqa: E501
        :rtype: list[IdName]
        """
        return self._associated_resource_groups

    @associated_resource_groups.setter
    def associated_resource_groups(self, associated_resource_groups):
        """Sets the associated_resource_groups of this ExpandedUser.


        :param associated_resource_groups: The associated_resource_groups of this ExpandedUser.  # noqa: E501
        :type: list[IdName]
        """

        self._associated_resource_groups = associated_resource_groups

    @property
    def base_role(self):
        """Gets the base_role of this ExpandedUser.  # noqa: E501


        :return: The base_role of this ExpandedUser.  # noqa: E501
        :rtype: RoleInfo
        """
        return self._base_role

    @base_role.setter
    def base_role(self, base_role):
        """Sets the base_role of this ExpandedUser.


        :param base_role: The base_role of this ExpandedUser.  # noqa: E501
        :type: RoleInfo
        """

        self._base_role = base_role

    @property
    def env_specific_roles(self):
        """Gets the env_specific_roles of this ExpandedUser.  # noqa: E501


        :return: The env_specific_roles of this ExpandedUser.  # noqa: E501
        :rtype: list[EnvSpecificAccess]
        """
        return self._env_specific_roles

    @env_specific_roles.setter
    def env_specific_roles(self, env_specific_roles):
        """Sets the env_specific_roles of this ExpandedUser.


        :param env_specific_roles: The env_specific_roles of this ExpandedUser.  # noqa: E501
        :type: list[EnvSpecificAccess]
        """

        self._env_specific_roles = env_specific_roles

    @property
    def groups(self):
        """Gets the groups of this ExpandedUser.  # noqa: E501


        :return: The groups of this ExpandedUser.  # noqa: E501
        :rtype: list[IdName]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ExpandedUser.


        :param groups: The groups of this ExpandedUser.  # noqa: E501
        :type: list[IdName]
        """

        self._groups = groups

    @property
    def picture(self):
        """Gets the picture of this ExpandedUser.  # noqa: E501


        :return: The picture of this ExpandedUser.  # noqa: E501
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this ExpandedUser.


        :param picture: The picture of this ExpandedUser.  # noqa: E501
        :type: str
        """

        self._picture = picture

    @property
    def user_id(self):
        """Gets the user_id of this ExpandedUser.  # noqa: E501


        :return: The user_id of this ExpandedUser.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ExpandedUser.


        :param user_id: The user_id of this ExpandedUser.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def user_roles(self):
        """Gets the user_roles of this ExpandedUser.  # noqa: E501


        :return: The user_roles of this ExpandedUser.  # noqa: E501
        :rtype: list[RoleInfo]
        """
        return self._user_roles

    @user_roles.setter
    def user_roles(self, user_roles):
        """Sets the user_roles of this ExpandedUser.


        :param user_roles: The user_roles of this ExpandedUser.  # noqa: E501
        :type: list[RoleInfo]
        """

        self._user_roles = user_roles

    @property
    def username(self):
        """Gets the username of this ExpandedUser.  # noqa: E501


        :return: The username of this ExpandedUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ExpandedUser.


        :param username: The username of this ExpandedUser.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(ExpandedUser, dict):
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
        if not isinstance(other, ExpandedUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
