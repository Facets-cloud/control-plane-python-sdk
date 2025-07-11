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

class BlueprintFile(object):
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
        'stack_name': 'str',
        'cluster_id': 'str',
        'version': 'str',
        'sync_ctx_md5': 'str',
        'sync_id': 'str',
        'filename': 'str',
        'directory': 'str',
        'content': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'alpha': 'bool',
        'info': 'Info',
        'overridden': 'bool',
        'override': 'dict(str, object)',
        'edges': 'list[Edge]',
        'expressions': 'list[RefExpression]',
        'errors': 'list[BlueprintValidationError]',
        'parent_resource_id': 'str',
        'children_resource_ids': 'list[str]',
        'icon_url': 'str',
        'substack': 'bool',
        'templated_resource': 'bool'
    }

    attribute_map = {
        'stack_name': 'stackName',
        'cluster_id': 'clusterId',
        'version': 'version',
        'sync_ctx_md5': 'syncCtxMd5',
        'sync_id': 'syncId',
        'filename': 'filename',
        'directory': 'directory',
        'content': 'content',
        'resource_name': 'resourceName',
        'resource_type': 'resourceType',
        'alpha': 'alpha',
        'info': 'info',
        'overridden': 'overridden',
        'override': 'override',
        'edges': 'edges',
        'expressions': 'expressions',
        'errors': 'errors',
        'parent_resource_id': 'parentResourceId',
        'children_resource_ids': 'childrenResourceIds',
        'icon_url': 'iconUrl',
        'substack': 'substack',
        'templated_resource': 'templatedResource'
    }

    def __init__(self, stack_name=None, cluster_id=None, version=None, sync_ctx_md5=None, sync_id=None, filename=None, directory=None, content=None, resource_name=None, resource_type=None, alpha=None, info=None, overridden=None, override=None, edges=None, expressions=None, errors=None, parent_resource_id=None, children_resource_ids=None, icon_url=None, substack=None, templated_resource=None):  # noqa: E501
        """BlueprintFile - a model defined in Swagger"""  # noqa: E501
        self._stack_name = None
        self._cluster_id = None
        self._version = None
        self._sync_ctx_md5 = None
        self._sync_id = None
        self._filename = None
        self._directory = None
        self._content = None
        self._resource_name = None
        self._resource_type = None
        self._alpha = None
        self._info = None
        self._overridden = None
        self._override = None
        self._edges = None
        self._expressions = None
        self._errors = None
        self._parent_resource_id = None
        self._children_resource_ids = None
        self._icon_url = None
        self._substack = None
        self._templated_resource = None
        self.discriminator = None
        if stack_name is not None:
            self.stack_name = stack_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if version is not None:
            self.version = version
        if sync_ctx_md5 is not None:
            self.sync_ctx_md5 = sync_ctx_md5
        if sync_id is not None:
            self.sync_id = sync_id
        if filename is not None:
            self.filename = filename
        if directory is not None:
            self.directory = directory
        if content is not None:
            self.content = content
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if alpha is not None:
            self.alpha = alpha
        if info is not None:
            self.info = info
        if overridden is not None:
            self.overridden = overridden
        if override is not None:
            self.override = override
        if edges is not None:
            self.edges = edges
        if expressions is not None:
            self.expressions = expressions
        if errors is not None:
            self.errors = errors
        if parent_resource_id is not None:
            self.parent_resource_id = parent_resource_id
        if children_resource_ids is not None:
            self.children_resource_ids = children_resource_ids
        if icon_url is not None:
            self.icon_url = icon_url
        if substack is not None:
            self.substack = substack
        if templated_resource is not None:
            self.templated_resource = templated_resource

    @property
    def stack_name(self):
        """Gets the stack_name of this BlueprintFile.  # noqa: E501


        :return: The stack_name of this BlueprintFile.  # noqa: E501
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this BlueprintFile.


        :param stack_name: The stack_name of this BlueprintFile.  # noqa: E501
        :type: str
        """

        self._stack_name = stack_name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this BlueprintFile.  # noqa: E501


        :return: The cluster_id of this BlueprintFile.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this BlueprintFile.


        :param cluster_id: The cluster_id of this BlueprintFile.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def version(self):
        """Gets the version of this BlueprintFile.  # noqa: E501


        :return: The version of this BlueprintFile.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BlueprintFile.


        :param version: The version of this BlueprintFile.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def sync_ctx_md5(self):
        """Gets the sync_ctx_md5 of this BlueprintFile.  # noqa: E501


        :return: The sync_ctx_md5 of this BlueprintFile.  # noqa: E501
        :rtype: str
        """
        return self._sync_ctx_md5

    @sync_ctx_md5.setter
    def sync_ctx_md5(self, sync_ctx_md5):
        """Sets the sync_ctx_md5 of this BlueprintFile.


        :param sync_ctx_md5: The sync_ctx_md5 of this BlueprintFile.  # noqa: E501
        :type: str
        """

        self._sync_ctx_md5 = sync_ctx_md5

    @property
    def sync_id(self):
        """Gets the sync_id of this BlueprintFile.  # noqa: E501


        :return: The sync_id of this BlueprintFile.  # noqa: E501
        :rtype: str
        """
        return self._sync_id

    @sync_id.setter
    def sync_id(self, sync_id):
        """Sets the sync_id of this BlueprintFile.


        :param sync_id: The sync_id of this BlueprintFile.  # noqa: E501
        :type: str
        """

        self._sync_id = sync_id

    @property
    def filename(self):
        """Gets the filename of this BlueprintFile.  # noqa: E501


        :return: The filename of this BlueprintFile.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this BlueprintFile.


        :param filename: The filename of this BlueprintFile.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def directory(self):
        """Gets the directory of this BlueprintFile.  # noqa: E501


        :return: The directory of this BlueprintFile.  # noqa: E501
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this BlueprintFile.


        :param directory: The directory of this BlueprintFile.  # noqa: E501
        :type: str
        """

        self._directory = directory

    @property
    def content(self):
        """Gets the content of this BlueprintFile.  # noqa: E501


        :return: The content of this BlueprintFile.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this BlueprintFile.


        :param content: The content of this BlueprintFile.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def resource_name(self):
        """Gets the resource_name of this BlueprintFile.  # noqa: E501


        :return: The resource_name of this BlueprintFile.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this BlueprintFile.


        :param resource_name: The resource_name of this BlueprintFile.  # noqa: E501
        :type: str
        """

        self._resource_name = resource_name

    @property
    def resource_type(self):
        """Gets the resource_type of this BlueprintFile.  # noqa: E501


        :return: The resource_type of this BlueprintFile.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this BlueprintFile.


        :param resource_type: The resource_type of this BlueprintFile.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def alpha(self):
        """Gets the alpha of this BlueprintFile.  # noqa: E501


        :return: The alpha of this BlueprintFile.  # noqa: E501
        :rtype: bool
        """
        return self._alpha

    @alpha.setter
    def alpha(self, alpha):
        """Sets the alpha of this BlueprintFile.


        :param alpha: The alpha of this BlueprintFile.  # noqa: E501
        :type: bool
        """

        self._alpha = alpha

    @property
    def info(self):
        """Gets the info of this BlueprintFile.  # noqa: E501


        :return: The info of this BlueprintFile.  # noqa: E501
        :rtype: Info
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this BlueprintFile.


        :param info: The info of this BlueprintFile.  # noqa: E501
        :type: Info
        """

        self._info = info

    @property
    def overridden(self):
        """Gets the overridden of this BlueprintFile.  # noqa: E501


        :return: The overridden of this BlueprintFile.  # noqa: E501
        :rtype: bool
        """
        return self._overridden

    @overridden.setter
    def overridden(self, overridden):
        """Sets the overridden of this BlueprintFile.


        :param overridden: The overridden of this BlueprintFile.  # noqa: E501
        :type: bool
        """

        self._overridden = overridden

    @property
    def override(self):
        """Gets the override of this BlueprintFile.  # noqa: E501


        :return: The override of this BlueprintFile.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._override

    @override.setter
    def override(self, override):
        """Sets the override of this BlueprintFile.


        :param override: The override of this BlueprintFile.  # noqa: E501
        :type: dict(str, object)
        """

        self._override = override

    @property
    def edges(self):
        """Gets the edges of this BlueprintFile.  # noqa: E501


        :return: The edges of this BlueprintFile.  # noqa: E501
        :rtype: list[Edge]
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this BlueprintFile.


        :param edges: The edges of this BlueprintFile.  # noqa: E501
        :type: list[Edge]
        """

        self._edges = edges

    @property
    def expressions(self):
        """Gets the expressions of this BlueprintFile.  # noqa: E501


        :return: The expressions of this BlueprintFile.  # noqa: E501
        :rtype: list[RefExpression]
        """
        return self._expressions

    @expressions.setter
    def expressions(self, expressions):
        """Sets the expressions of this BlueprintFile.


        :param expressions: The expressions of this BlueprintFile.  # noqa: E501
        :type: list[RefExpression]
        """

        self._expressions = expressions

    @property
    def errors(self):
        """Gets the errors of this BlueprintFile.  # noqa: E501


        :return: The errors of this BlueprintFile.  # noqa: E501
        :rtype: list[BlueprintValidationError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this BlueprintFile.


        :param errors: The errors of this BlueprintFile.  # noqa: E501
        :type: list[BlueprintValidationError]
        """

        self._errors = errors

    @property
    def parent_resource_id(self):
        """Gets the parent_resource_id of this BlueprintFile.  # noqa: E501


        :return: The parent_resource_id of this BlueprintFile.  # noqa: E501
        :rtype: str
        """
        return self._parent_resource_id

    @parent_resource_id.setter
    def parent_resource_id(self, parent_resource_id):
        """Sets the parent_resource_id of this BlueprintFile.


        :param parent_resource_id: The parent_resource_id of this BlueprintFile.  # noqa: E501
        :type: str
        """

        self._parent_resource_id = parent_resource_id

    @property
    def children_resource_ids(self):
        """Gets the children_resource_ids of this BlueprintFile.  # noqa: E501


        :return: The children_resource_ids of this BlueprintFile.  # noqa: E501
        :rtype: list[str]
        """
        return self._children_resource_ids

    @children_resource_ids.setter
    def children_resource_ids(self, children_resource_ids):
        """Sets the children_resource_ids of this BlueprintFile.


        :param children_resource_ids: The children_resource_ids of this BlueprintFile.  # noqa: E501
        :type: list[str]
        """

        self._children_resource_ids = children_resource_ids

    @property
    def icon_url(self):
        """Gets the icon_url of this BlueprintFile.  # noqa: E501


        :return: The icon_url of this BlueprintFile.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this BlueprintFile.


        :param icon_url: The icon_url of this BlueprintFile.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

    @property
    def substack(self):
        """Gets the substack of this BlueprintFile.  # noqa: E501


        :return: The substack of this BlueprintFile.  # noqa: E501
        :rtype: bool
        """
        return self._substack

    @substack.setter
    def substack(self, substack):
        """Sets the substack of this BlueprintFile.


        :param substack: The substack of this BlueprintFile.  # noqa: E501
        :type: bool
        """

        self._substack = substack

    @property
    def templated_resource(self):
        """Gets the templated_resource of this BlueprintFile.  # noqa: E501


        :return: The templated_resource of this BlueprintFile.  # noqa: E501
        :rtype: bool
        """
        return self._templated_resource

    @templated_resource.setter
    def templated_resource(self, templated_resource):
        """Sets the templated_resource of this BlueprintFile.


        :param templated_resource: The templated_resource of this BlueprintFile.  # noqa: E501
        :type: bool
        """

        self._templated_resource = templated_resource

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
        if issubclass(BlueprintFile, dict):
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
        if not isinstance(other, BlueprintFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
