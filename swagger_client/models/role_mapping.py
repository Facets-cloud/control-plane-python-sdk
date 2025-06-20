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

class RoleMapping(object):
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
        'role_name': 'str',
        'label': 'str',
        'entities': 'list[str]',
        'k8s_role': 'str',
        'k8s_cluster_role': 'str',
        'description': 'str',
        'role_type': 'str',
        'last_modified_date': 'datetime',
        'last_modified_by': 'str',
        'base_role': 'bool'
    }

    attribute_map = {
        'role_name': 'roleName',
        'label': 'label',
        'entities': 'entities',
        'k8s_role': 'k8sRole',
        'k8s_cluster_role': 'k8sClusterRole',
        'description': 'description',
        'role_type': 'roleType',
        'last_modified_date': 'lastModifiedDate',
        'last_modified_by': 'lastModifiedBy',
        'base_role': 'baseRole'
    }

    def __init__(self, role_name=None, label=None, entities=None, k8s_role=None, k8s_cluster_role=None, description=None, role_type=None, last_modified_date=None, last_modified_by=None, base_role=None):  # noqa: E501
        """RoleMapping - a model defined in Swagger"""  # noqa: E501
        self._role_name = None
        self._label = None
        self._entities = None
        self._k8s_role = None
        self._k8s_cluster_role = None
        self._description = None
        self._role_type = None
        self._last_modified_date = None
        self._last_modified_by = None
        self._base_role = None
        self.discriminator = None
        if role_name is not None:
            self.role_name = role_name
        if label is not None:
            self.label = label
        if entities is not None:
            self.entities = entities
        if k8s_role is not None:
            self.k8s_role = k8s_role
        if k8s_cluster_role is not None:
            self.k8s_cluster_role = k8s_cluster_role
        if description is not None:
            self.description = description
        if role_type is not None:
            self.role_type = role_type
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if base_role is not None:
            self.base_role = base_role

    @property
    def role_name(self):
        """Gets the role_name of this RoleMapping.  # noqa: E501


        :return: The role_name of this RoleMapping.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this RoleMapping.


        :param role_name: The role_name of this RoleMapping.  # noqa: E501
        :type: str
        """

        self._role_name = role_name

    @property
    def label(self):
        """Gets the label of this RoleMapping.  # noqa: E501


        :return: The label of this RoleMapping.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this RoleMapping.


        :param label: The label of this RoleMapping.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def entities(self):
        """Gets the entities of this RoleMapping.  # noqa: E501


        :return: The entities of this RoleMapping.  # noqa: E501
        :rtype: list[str]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this RoleMapping.


        :param entities: The entities of this RoleMapping.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ACCOUNTS_WRITE", "ACCOUNTS_DELETE", "ALERTS_CONFIGURE", "ARTIFACTORY_WRITE", "ARTIFACTORY_DELETE", "ARTIFACTS_DELETE", "ARTIFACTS_WRITE", "ARTIFACT_ROUTING_RULE_WRITE", "ARTIFACT_ROUTING_RULE_DELETE", "APPLICATION_ROLLING_RESTART", "APPLICATION_DEPLOYMENT_PROMOTE", "APPLICATION_DEPLOYMENT_ABORT", "BILLING_MANAGE", "CHANNEL_WRITE", "CHANNEL_DELETE", "ENVIRONMENT_CONFIGURE", "ENVIRONMENT_DELETE", "ENVIRONMENT_WRITE", "ENVIRONMENT_DESTROY", "ENVIRONMENT_LAUNCH", "OAUTH_INTEGRATION_DELETE", "OAUTH_INTEGRATION_WRITE", "RESOURCE_OVERRIDE", "RESOURCE_WRITE", "RESOURCE_DELETE", "RESOURCE_GROUP_READ", "RESOURCE_GROUP_WRITE", "RESOURCE_GROUP_DELETE", "RELEASE_APPROVAL_AUTHORITY", "RELEASE_FULL", "RELEASE_PLAN", "RELEASE_APPLY_PLAN", "RELEASE_SELECTIVE", "RELEASE_CUSTOM", "RELEASE_MAINTENANCE", "RELEASE_TERRAFORM_EXPORT", "RELEASE_SCALE_UP", "RELEASE_SCALE_DOWN", "RELEASE_FULL_ALLOW_DESTROY", "RELEASE_SELECTIVE_ALLOW_DESTROY", "RELEASE_CUSTOM_ALLOW_DESTROY", "RELEASE_PAUSE", "STACK_CONFIGURE", "STACK_WRITE", "STACK_DELETE", "SUBSCRIPTION_WRITE", "SUBSCRIPTION_DELETE", "SETTINGS_WRITE", "USER_READ", "USER_WRITE", "USER_DELETE", "TEMPLATE_WRITE", "TEMPLATE_DELETE", "TRASH_RESTORE", "TRASH_DELETE", "USER_GROUP_READ", "USER_GROUP_WRITE", "USER_GROUP_DELETE", "CUSTOM_ROLE_READ", "CUSTOM_ROLE_WRITE", "CUSTOM_ROLE_DELETE", "K8S_READER", "K8S_DEBUGGER", "K8S_CUSTOM", "K8S_CREDENTIALS", "CLI_ARTIFACT_PUSH", "K8S_PERMISSION", "PIPELINE_WRITE", "ARTIFACT_CI_WRITE", "ARTIFACT_CI_DELETE", "PROMOTIONAL_WORKFLOW_WRITE", "PROMOTIONAL_WORKFLOW_DELETE", "VIEW_RESOURCE_SECRETS", "COST_EXPLORER_VIEW", "RELEASE_STREAM_WRITE", "RELEASE_STREAM_DELETE", "BLUEPRINT_TEMPLATE_WRITE", "BLUEPRINT_TEMPLATE_DELETE", "VPN_CONNECT", "OPA_WRITE", "OPA_EXECUTE", "OPA_DELETE", "AUDIT_LOGS_VIEW", "CI_CD_CONFIGURE", "VIEW_SECRETS", "MAINTENANCE_WINDOW_EDIT", "MODULE_READ", "MODULE_WRITE", "MODULE_DELETE", "PROJECT_TYPE_WRITE", "PROJECT_TYPE_DELETE", "WEB_COMPONENT_WRITE", "WEB_COMPONENT_DELETE"]  # noqa: E501
        if not set(entities).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `entities` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(entities) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._entities = entities

    @property
    def k8s_role(self):
        """Gets the k8s_role of this RoleMapping.  # noqa: E501


        :return: The k8s_role of this RoleMapping.  # noqa: E501
        :rtype: str
        """
        return self._k8s_role

    @k8s_role.setter
    def k8s_role(self, k8s_role):
        """Sets the k8s_role of this RoleMapping.


        :param k8s_role: The k8s_role of this RoleMapping.  # noqa: E501
        :type: str
        """

        self._k8s_role = k8s_role

    @property
    def k8s_cluster_role(self):
        """Gets the k8s_cluster_role of this RoleMapping.  # noqa: E501


        :return: The k8s_cluster_role of this RoleMapping.  # noqa: E501
        :rtype: str
        """
        return self._k8s_cluster_role

    @k8s_cluster_role.setter
    def k8s_cluster_role(self, k8s_cluster_role):
        """Sets the k8s_cluster_role of this RoleMapping.


        :param k8s_cluster_role: The k8s_cluster_role of this RoleMapping.  # noqa: E501
        :type: str
        """

        self._k8s_cluster_role = k8s_cluster_role

    @property
    def description(self):
        """Gets the description of this RoleMapping.  # noqa: E501


        :return: The description of this RoleMapping.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoleMapping.


        :param description: The description of this RoleMapping.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def role_type(self):
        """Gets the role_type of this RoleMapping.  # noqa: E501


        :return: The role_type of this RoleMapping.  # noqa: E501
        :rtype: str
        """
        return self._role_type

    @role_type.setter
    def role_type(self, role_type):
        """Sets the role_type of this RoleMapping.


        :param role_type: The role_type of this RoleMapping.  # noqa: E501
        :type: str
        """
        allowed_values = ["SYSTEM_DEFINED", "USER_DEFINED"]  # noqa: E501
        if role_type not in allowed_values:
            raise ValueError(
                "Invalid value for `role_type` ({0}), must be one of {1}"  # noqa: E501
                .format(role_type, allowed_values)
            )

        self._role_type = role_type

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this RoleMapping.  # noqa: E501


        :return: The last_modified_date of this RoleMapping.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this RoleMapping.


        :param last_modified_date: The last_modified_date of this RoleMapping.  # noqa: E501
        :type: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this RoleMapping.  # noqa: E501


        :return: The last_modified_by of this RoleMapping.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this RoleMapping.


        :param last_modified_by: The last_modified_by of this RoleMapping.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def base_role(self):
        """Gets the base_role of this RoleMapping.  # noqa: E501


        :return: The base_role of this RoleMapping.  # noqa: E501
        :rtype: bool
        """
        return self._base_role

    @base_role.setter
    def base_role(self, base_role):
        """Sets the base_role of this RoleMapping.


        :param base_role: The base_role of this RoleMapping.  # noqa: E501
        :type: bool
        """

        self._base_role = base_role

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
        if issubclass(RoleMapping, dict):
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
        if not isinstance(other, RoleMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
