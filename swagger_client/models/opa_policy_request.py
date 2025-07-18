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

class OpaPolicyRequest(object):
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
        'policy_name': 'str',
        'stack_name': 'str',
        'description': 'str',
        'raw_policy': 'str',
        'cluster_ids': 'list[str]',
        'resource_types': 'list[str]',
        'resource_type_and_resource_names_map': 'dict(str, list[str])',
        'policy_type': 'str',
        'template_id': 'str',
        'flavours': 'list[str]',
        'input_data': 'dict(str, object)',
        'severity': 'str',
        'package_name': 'str',
        'disabled': 'bool'
    }

    attribute_map = {
        'policy_name': 'policyName',
        'stack_name': 'stackName',
        'description': 'description',
        'raw_policy': 'rawPolicy',
        'cluster_ids': 'clusterIds',
        'resource_types': 'resourceTypes',
        'resource_type_and_resource_names_map': 'resourceTypeAndResourceNamesMap',
        'policy_type': 'policyType',
        'template_id': 'templateId',
        'flavours': 'flavours',
        'input_data': 'inputData',
        'severity': 'severity',
        'package_name': 'packageName',
        'disabled': 'disabled'
    }

    def __init__(self, policy_name=None, stack_name=None, description=None, raw_policy=None, cluster_ids=None, resource_types=None, resource_type_and_resource_names_map=None, policy_type=None, template_id=None, flavours=None, input_data=None, severity=None, package_name=None, disabled=None):  # noqa: E501
        """OpaPolicyRequest - a model defined in Swagger"""  # noqa: E501
        self._policy_name = None
        self._stack_name = None
        self._description = None
        self._raw_policy = None
        self._cluster_ids = None
        self._resource_types = None
        self._resource_type_and_resource_names_map = None
        self._policy_type = None
        self._template_id = None
        self._flavours = None
        self._input_data = None
        self._severity = None
        self._package_name = None
        self._disabled = None
        self.discriminator = None
        if policy_name is not None:
            self.policy_name = policy_name
        if stack_name is not None:
            self.stack_name = stack_name
        if description is not None:
            self.description = description
        if raw_policy is not None:
            self.raw_policy = raw_policy
        if cluster_ids is not None:
            self.cluster_ids = cluster_ids
        if resource_types is not None:
            self.resource_types = resource_types
        if resource_type_and_resource_names_map is not None:
            self.resource_type_and_resource_names_map = resource_type_and_resource_names_map
        if policy_type is not None:
            self.policy_type = policy_type
        if template_id is not None:
            self.template_id = template_id
        if flavours is not None:
            self.flavours = flavours
        if input_data is not None:
            self.input_data = input_data
        if severity is not None:
            self.severity = severity
        if package_name is not None:
            self.package_name = package_name
        if disabled is not None:
            self.disabled = disabled

    @property
    def policy_name(self):
        """Gets the policy_name of this OpaPolicyRequest.  # noqa: E501


        :return: The policy_name of this OpaPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this OpaPolicyRequest.


        :param policy_name: The policy_name of this OpaPolicyRequest.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

    @property
    def stack_name(self):
        """Gets the stack_name of this OpaPolicyRequest.  # noqa: E501


        :return: The stack_name of this OpaPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this OpaPolicyRequest.


        :param stack_name: The stack_name of this OpaPolicyRequest.  # noqa: E501
        :type: str
        """

        self._stack_name = stack_name

    @property
    def description(self):
        """Gets the description of this OpaPolicyRequest.  # noqa: E501


        :return: The description of this OpaPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OpaPolicyRequest.


        :param description: The description of this OpaPolicyRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def raw_policy(self):
        """Gets the raw_policy of this OpaPolicyRequest.  # noqa: E501


        :return: The raw_policy of this OpaPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._raw_policy

    @raw_policy.setter
    def raw_policy(self, raw_policy):
        """Sets the raw_policy of this OpaPolicyRequest.


        :param raw_policy: The raw_policy of this OpaPolicyRequest.  # noqa: E501
        :type: str
        """

        self._raw_policy = raw_policy

    @property
    def cluster_ids(self):
        """Gets the cluster_ids of this OpaPolicyRequest.  # noqa: E501


        :return: The cluster_ids of this OpaPolicyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._cluster_ids

    @cluster_ids.setter
    def cluster_ids(self, cluster_ids):
        """Sets the cluster_ids of this OpaPolicyRequest.


        :param cluster_ids: The cluster_ids of this OpaPolicyRequest.  # noqa: E501
        :type: list[str]
        """

        self._cluster_ids = cluster_ids

    @property
    def resource_types(self):
        """Gets the resource_types of this OpaPolicyRequest.  # noqa: E501


        :return: The resource_types of this OpaPolicyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        """Sets the resource_types of this OpaPolicyRequest.


        :param resource_types: The resource_types of this OpaPolicyRequest.  # noqa: E501
        :type: list[str]
        """

        self._resource_types = resource_types

    @property
    def resource_type_and_resource_names_map(self):
        """Gets the resource_type_and_resource_names_map of this OpaPolicyRequest.  # noqa: E501


        :return: The resource_type_and_resource_names_map of this OpaPolicyRequest.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._resource_type_and_resource_names_map

    @resource_type_and_resource_names_map.setter
    def resource_type_and_resource_names_map(self, resource_type_and_resource_names_map):
        """Sets the resource_type_and_resource_names_map of this OpaPolicyRequest.


        :param resource_type_and_resource_names_map: The resource_type_and_resource_names_map of this OpaPolicyRequest.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._resource_type_and_resource_names_map = resource_type_and_resource_names_map

    @property
    def policy_type(self):
        """Gets the policy_type of this OpaPolicyRequest.  # noqa: E501


        :return: The policy_type of this OpaPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """Sets the policy_type of this OpaPolicyRequest.


        :param policy_type: The policy_type of this OpaPolicyRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["RAW", "TEMPLATED"]  # noqa: E501
        if policy_type not in allowed_values:
            raise ValueError(
                "Invalid value for `policy_type` ({0}), must be one of {1}"  # noqa: E501
                .format(policy_type, allowed_values)
            )

        self._policy_type = policy_type

    @property
    def template_id(self):
        """Gets the template_id of this OpaPolicyRequest.  # noqa: E501


        :return: The template_id of this OpaPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this OpaPolicyRequest.


        :param template_id: The template_id of this OpaPolicyRequest.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

    @property
    def flavours(self):
        """Gets the flavours of this OpaPolicyRequest.  # noqa: E501


        :return: The flavours of this OpaPolicyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._flavours

    @flavours.setter
    def flavours(self, flavours):
        """Sets the flavours of this OpaPolicyRequest.


        :param flavours: The flavours of this OpaPolicyRequest.  # noqa: E501
        :type: list[str]
        """

        self._flavours = flavours

    @property
    def input_data(self):
        """Gets the input_data of this OpaPolicyRequest.  # noqa: E501


        :return: The input_data of this OpaPolicyRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._input_data

    @input_data.setter
    def input_data(self, input_data):
        """Sets the input_data of this OpaPolicyRequest.


        :param input_data: The input_data of this OpaPolicyRequest.  # noqa: E501
        :type: dict(str, object)
        """

        self._input_data = input_data

    @property
    def severity(self):
        """Gets the severity of this OpaPolicyRequest.  # noqa: E501


        :return: The severity of this OpaPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this OpaPolicyRequest.


        :param severity: The severity of this OpaPolicyRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["ERROR", "WARNING"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def package_name(self):
        """Gets the package_name of this OpaPolicyRequest.  # noqa: E501


        :return: The package_name of this OpaPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this OpaPolicyRequest.


        :param package_name: The package_name of this OpaPolicyRequest.  # noqa: E501
        :type: str
        """

        self._package_name = package_name

    @property
    def disabled(self):
        """Gets the disabled of this OpaPolicyRequest.  # noqa: E501


        :return: The disabled of this OpaPolicyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this OpaPolicyRequest.


        :param disabled: The disabled of this OpaPolicyRequest.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

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
        if issubclass(OpaPolicyRequest, dict):
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
        if not isinstance(other, OpaPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
