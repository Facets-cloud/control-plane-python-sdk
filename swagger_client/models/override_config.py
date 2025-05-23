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

class OverrideConfig(object):
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
        'branch_name': 'str',
        'git_org_name': 'str',
        'git_override_url': 'str',
        'migration_failure_message': 'str',
        'overrides_migration_status': 'str',
        'overrides_repo_name': 'str',
        'ui_overrides_enabled': 'bool'
    }

    attribute_map = {
        'branch_name': 'branchName',
        'git_org_name': 'gitOrgName',
        'git_override_url': 'gitOverrideUrl',
        'migration_failure_message': 'migrationFailureMessage',
        'overrides_migration_status': 'overridesMigrationStatus',
        'overrides_repo_name': 'overridesRepoName',
        'ui_overrides_enabled': 'uiOverridesEnabled'
    }

    def __init__(self, branch_name=None, git_org_name=None, git_override_url=None, migration_failure_message=None, overrides_migration_status=None, overrides_repo_name=None, ui_overrides_enabled=None):  # noqa: E501
        """OverrideConfig - a model defined in Swagger"""  # noqa: E501
        self._branch_name = None
        self._git_org_name = None
        self._git_override_url = None
        self._migration_failure_message = None
        self._overrides_migration_status = None
        self._overrides_repo_name = None
        self._ui_overrides_enabled = None
        self.discriminator = None
        if branch_name is not None:
            self.branch_name = branch_name
        if git_org_name is not None:
            self.git_org_name = git_org_name
        if git_override_url is not None:
            self.git_override_url = git_override_url
        if migration_failure_message is not None:
            self.migration_failure_message = migration_failure_message
        if overrides_migration_status is not None:
            self.overrides_migration_status = overrides_migration_status
        if overrides_repo_name is not None:
            self.overrides_repo_name = overrides_repo_name
        if ui_overrides_enabled is not None:
            self.ui_overrides_enabled = ui_overrides_enabled

    @property
    def branch_name(self):
        """Gets the branch_name of this OverrideConfig.  # noqa: E501


        :return: The branch_name of this OverrideConfig.  # noqa: E501
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """Sets the branch_name of this OverrideConfig.


        :param branch_name: The branch_name of this OverrideConfig.  # noqa: E501
        :type: str
        """

        self._branch_name = branch_name

    @property
    def git_org_name(self):
        """Gets the git_org_name of this OverrideConfig.  # noqa: E501


        :return: The git_org_name of this OverrideConfig.  # noqa: E501
        :rtype: str
        """
        return self._git_org_name

    @git_org_name.setter
    def git_org_name(self, git_org_name):
        """Sets the git_org_name of this OverrideConfig.


        :param git_org_name: The git_org_name of this OverrideConfig.  # noqa: E501
        :type: str
        """

        self._git_org_name = git_org_name

    @property
    def git_override_url(self):
        """Gets the git_override_url of this OverrideConfig.  # noqa: E501


        :return: The git_override_url of this OverrideConfig.  # noqa: E501
        :rtype: str
        """
        return self._git_override_url

    @git_override_url.setter
    def git_override_url(self, git_override_url):
        """Sets the git_override_url of this OverrideConfig.


        :param git_override_url: The git_override_url of this OverrideConfig.  # noqa: E501
        :type: str
        """

        self._git_override_url = git_override_url

    @property
    def migration_failure_message(self):
        """Gets the migration_failure_message of this OverrideConfig.  # noqa: E501


        :return: The migration_failure_message of this OverrideConfig.  # noqa: E501
        :rtype: str
        """
        return self._migration_failure_message

    @migration_failure_message.setter
    def migration_failure_message(self, migration_failure_message):
        """Sets the migration_failure_message of this OverrideConfig.


        :param migration_failure_message: The migration_failure_message of this OverrideConfig.  # noqa: E501
        :type: str
        """

        self._migration_failure_message = migration_failure_message

    @property
    def overrides_migration_status(self):
        """Gets the overrides_migration_status of this OverrideConfig.  # noqa: E501


        :return: The overrides_migration_status of this OverrideConfig.  # noqa: E501
        :rtype: str
        """
        return self._overrides_migration_status

    @overrides_migration_status.setter
    def overrides_migration_status(self, overrides_migration_status):
        """Sets the overrides_migration_status of this OverrideConfig.


        :param overrides_migration_status: The overrides_migration_status of this OverrideConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "PENDING", "COMPLETED", "FAILED"]  # noqa: E501
        if overrides_migration_status not in allowed_values:
            raise ValueError(
                "Invalid value for `overrides_migration_status` ({0}), must be one of {1}"  # noqa: E501
                .format(overrides_migration_status, allowed_values)
            )

        self._overrides_migration_status = overrides_migration_status

    @property
    def overrides_repo_name(self):
        """Gets the overrides_repo_name of this OverrideConfig.  # noqa: E501


        :return: The overrides_repo_name of this OverrideConfig.  # noqa: E501
        :rtype: str
        """
        return self._overrides_repo_name

    @overrides_repo_name.setter
    def overrides_repo_name(self, overrides_repo_name):
        """Sets the overrides_repo_name of this OverrideConfig.


        :param overrides_repo_name: The overrides_repo_name of this OverrideConfig.  # noqa: E501
        :type: str
        """

        self._overrides_repo_name = overrides_repo_name

    @property
    def ui_overrides_enabled(self):
        """Gets the ui_overrides_enabled of this OverrideConfig.  # noqa: E501


        :return: The ui_overrides_enabled of this OverrideConfig.  # noqa: E501
        :rtype: bool
        """
        return self._ui_overrides_enabled

    @ui_overrides_enabled.setter
    def ui_overrides_enabled(self, ui_overrides_enabled):
        """Sets the ui_overrides_enabled of this OverrideConfig.


        :param ui_overrides_enabled: The ui_overrides_enabled of this OverrideConfig.  # noqa: E501
        :type: bool
        """

        self._ui_overrides_enabled = ui_overrides_enabled

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
        if issubclass(OverrideConfig, dict):
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
        if not isinstance(other, OverrideConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
