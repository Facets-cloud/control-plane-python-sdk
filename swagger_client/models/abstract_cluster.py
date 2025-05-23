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

class AbstractCluster(object):
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
        'auto_sign_off_schedule': 'str',
        'base_cluster_id': 'str',
        'base_cluster_name': 'str',
        'branch': 'str',
        'cd_pipeline_parent': 'str',
        'cloud': 'str',
        'cloud_account_id': 'str',
        'cloud_account_secret_id': 'str',
        'cluster_code': 'str',
        'cluster_state': 'str',
        'common_environment_variables': 'dict(str, str)',
        'component_versions': 'dict(str, str)',
        'configured': 'bool',
        'created_by': 'str',
        'creation_date': 'datetime',
        'deleted': 'bool',
        'dynamic_launch': 'bool',
        'enable_auto_sign_off': 'bool',
        'entity_type': 'str',
        'global_variables': 'dict(str, str)',
        'id': 'str',
        'is_ephemeral': 'bool',
        'k8s_requests_to_limits_ratio': 'float',
        'last_modified_by': 'str',
        'last_modified_date': 'datetime',
        'name': 'str',
        'namespace': 'str',
        'number_of_versions': 'int',
        'pause_releases': 'bool',
        'release_stream': 'str',
        'require_sign_off': 'bool',
        'schedules': 'dict(str, str)',
        'secrets': 'dict(str, str)',
        'secrets_uid': 'str',
        'stack_name': 'str',
        'tz': 'str',
        'variables': 'dict(str, Variables)',
        'versioning_key': 'str'
    }

    attribute_map = {
        'auto_sign_off_schedule': 'autoSignOffSchedule',
        'base_cluster_id': 'baseClusterId',
        'base_cluster_name': 'baseClusterName',
        'branch': 'branch',
        'cd_pipeline_parent': 'cdPipelineParent',
        'cloud': 'cloud',
        'cloud_account_id': 'cloudAccountId',
        'cloud_account_secret_id': 'cloudAccountSecretId',
        'cluster_code': 'clusterCode',
        'cluster_state': 'clusterState',
        'common_environment_variables': 'commonEnvironmentVariables',
        'component_versions': 'componentVersions',
        'configured': 'configured',
        'created_by': 'createdBy',
        'creation_date': 'creationDate',
        'deleted': 'deleted',
        'dynamic_launch': 'dynamicLaunch',
        'enable_auto_sign_off': 'enableAutoSignOff',
        'entity_type': 'entityType',
        'global_variables': 'globalVariables',
        'id': 'id',
        'is_ephemeral': 'isEphemeral',
        'k8s_requests_to_limits_ratio': 'k8sRequestsToLimitsRatio',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_date': 'lastModifiedDate',
        'name': 'name',
        'namespace': 'namespace',
        'number_of_versions': 'numberOfVersions',
        'pause_releases': 'pauseReleases',
        'release_stream': 'releaseStream',
        'require_sign_off': 'requireSignOff',
        'schedules': 'schedules',
        'secrets': 'secrets',
        'secrets_uid': 'secretsUid',
        'stack_name': 'stackName',
        'tz': 'tz',
        'variables': 'variables',
        'versioning_key': 'versioningKey'
    }

    def __init__(self, auto_sign_off_schedule=None, base_cluster_id=None, base_cluster_name=None, branch=None, cd_pipeline_parent=None, cloud=None, cloud_account_id=None, cloud_account_secret_id=None, cluster_code=None, cluster_state=None, common_environment_variables=None, component_versions=None, configured=None, created_by=None, creation_date=None, deleted=None, dynamic_launch=None, enable_auto_sign_off=None, entity_type=None, global_variables=None, id=None, is_ephemeral=None, k8s_requests_to_limits_ratio=None, last_modified_by=None, last_modified_date=None, name=None, namespace=None, number_of_versions=None, pause_releases=None, release_stream=None, require_sign_off=None, schedules=None, secrets=None, secrets_uid=None, stack_name=None, tz=None, variables=None, versioning_key=None):  # noqa: E501
        """AbstractCluster - a model defined in Swagger"""  # noqa: E501
        self._auto_sign_off_schedule = None
        self._base_cluster_id = None
        self._base_cluster_name = None
        self._branch = None
        self._cd_pipeline_parent = None
        self._cloud = None
        self._cloud_account_id = None
        self._cloud_account_secret_id = None
        self._cluster_code = None
        self._cluster_state = None
        self._common_environment_variables = None
        self._component_versions = None
        self._configured = None
        self._created_by = None
        self._creation_date = None
        self._deleted = None
        self._dynamic_launch = None
        self._enable_auto_sign_off = None
        self._entity_type = None
        self._global_variables = None
        self._id = None
        self._is_ephemeral = None
        self._k8s_requests_to_limits_ratio = None
        self._last_modified_by = None
        self._last_modified_date = None
        self._name = None
        self._namespace = None
        self._number_of_versions = None
        self._pause_releases = None
        self._release_stream = None
        self._require_sign_off = None
        self._schedules = None
        self._secrets = None
        self._secrets_uid = None
        self._stack_name = None
        self._tz = None
        self._variables = None
        self._versioning_key = None
        self.discriminator = None
        if auto_sign_off_schedule is not None:
            self.auto_sign_off_schedule = auto_sign_off_schedule
        if base_cluster_id is not None:
            self.base_cluster_id = base_cluster_id
        if base_cluster_name is not None:
            self.base_cluster_name = base_cluster_name
        if branch is not None:
            self.branch = branch
        if cd_pipeline_parent is not None:
            self.cd_pipeline_parent = cd_pipeline_parent
        if cloud is not None:
            self.cloud = cloud
        if cloud_account_id is not None:
            self.cloud_account_id = cloud_account_id
        if cloud_account_secret_id is not None:
            self.cloud_account_secret_id = cloud_account_secret_id
        if cluster_code is not None:
            self.cluster_code = cluster_code
        if cluster_state is not None:
            self.cluster_state = cluster_state
        if common_environment_variables is not None:
            self.common_environment_variables = common_environment_variables
        if component_versions is not None:
            self.component_versions = component_versions
        if configured is not None:
            self.configured = configured
        if created_by is not None:
            self.created_by = created_by
        if creation_date is not None:
            self.creation_date = creation_date
        if deleted is not None:
            self.deleted = deleted
        if dynamic_launch is not None:
            self.dynamic_launch = dynamic_launch
        if enable_auto_sign_off is not None:
            self.enable_auto_sign_off = enable_auto_sign_off
        if entity_type is not None:
            self.entity_type = entity_type
        if global_variables is not None:
            self.global_variables = global_variables
        if id is not None:
            self.id = id
        if is_ephemeral is not None:
            self.is_ephemeral = is_ephemeral
        if k8s_requests_to_limits_ratio is not None:
            self.k8s_requests_to_limits_ratio = k8s_requests_to_limits_ratio
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if number_of_versions is not None:
            self.number_of_versions = number_of_versions
        if pause_releases is not None:
            self.pause_releases = pause_releases
        if release_stream is not None:
            self.release_stream = release_stream
        if require_sign_off is not None:
            self.require_sign_off = require_sign_off
        if schedules is not None:
            self.schedules = schedules
        if secrets is not None:
            self.secrets = secrets
        if secrets_uid is not None:
            self.secrets_uid = secrets_uid
        if stack_name is not None:
            self.stack_name = stack_name
        if tz is not None:
            self.tz = tz
        if variables is not None:
            self.variables = variables
        if versioning_key is not None:
            self.versioning_key = versioning_key

    @property
    def auto_sign_off_schedule(self):
        """Gets the auto_sign_off_schedule of this AbstractCluster.  # noqa: E501


        :return: The auto_sign_off_schedule of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._auto_sign_off_schedule

    @auto_sign_off_schedule.setter
    def auto_sign_off_schedule(self, auto_sign_off_schedule):
        """Sets the auto_sign_off_schedule of this AbstractCluster.


        :param auto_sign_off_schedule: The auto_sign_off_schedule of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._auto_sign_off_schedule = auto_sign_off_schedule

    @property
    def base_cluster_id(self):
        """Gets the base_cluster_id of this AbstractCluster.  # noqa: E501


        :return: The base_cluster_id of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._base_cluster_id

    @base_cluster_id.setter
    def base_cluster_id(self, base_cluster_id):
        """Sets the base_cluster_id of this AbstractCluster.


        :param base_cluster_id: The base_cluster_id of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._base_cluster_id = base_cluster_id

    @property
    def base_cluster_name(self):
        """Gets the base_cluster_name of this AbstractCluster.  # noqa: E501


        :return: The base_cluster_name of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._base_cluster_name

    @base_cluster_name.setter
    def base_cluster_name(self, base_cluster_name):
        """Sets the base_cluster_name of this AbstractCluster.


        :param base_cluster_name: The base_cluster_name of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._base_cluster_name = base_cluster_name

    @property
    def branch(self):
        """Gets the branch of this AbstractCluster.  # noqa: E501


        :return: The branch of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this AbstractCluster.


        :param branch: The branch of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def cd_pipeline_parent(self):
        """Gets the cd_pipeline_parent of this AbstractCluster.  # noqa: E501


        :return: The cd_pipeline_parent of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._cd_pipeline_parent

    @cd_pipeline_parent.setter
    def cd_pipeline_parent(self, cd_pipeline_parent):
        """Sets the cd_pipeline_parent of this AbstractCluster.


        :param cd_pipeline_parent: The cd_pipeline_parent of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._cd_pipeline_parent = cd_pipeline_parent

    @property
    def cloud(self):
        """Gets the cloud of this AbstractCluster.  # noqa: E501


        :return: The cloud of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this AbstractCluster.


        :param cloud: The cloud of this AbstractCluster.  # noqa: E501
        :type: str
        """
        allowed_values = ["AWS", "AZURE", "LOCAL", "GCP", "KUBERNETES"]  # noqa: E501
        if cloud not in allowed_values:
            raise ValueError(
                "Invalid value for `cloud` ({0}), must be one of {1}"  # noqa: E501
                .format(cloud, allowed_values)
            )

        self._cloud = cloud

    @property
    def cloud_account_id(self):
        """Gets the cloud_account_id of this AbstractCluster.  # noqa: E501


        :return: The cloud_account_id of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._cloud_account_id

    @cloud_account_id.setter
    def cloud_account_id(self, cloud_account_id):
        """Sets the cloud_account_id of this AbstractCluster.


        :param cloud_account_id: The cloud_account_id of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._cloud_account_id = cloud_account_id

    @property
    def cloud_account_secret_id(self):
        """Gets the cloud_account_secret_id of this AbstractCluster.  # noqa: E501


        :return: The cloud_account_secret_id of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._cloud_account_secret_id

    @cloud_account_secret_id.setter
    def cloud_account_secret_id(self, cloud_account_secret_id):
        """Sets the cloud_account_secret_id of this AbstractCluster.


        :param cloud_account_secret_id: The cloud_account_secret_id of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._cloud_account_secret_id = cloud_account_secret_id

    @property
    def cluster_code(self):
        """Gets the cluster_code of this AbstractCluster.  # noqa: E501


        :return: The cluster_code of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._cluster_code

    @cluster_code.setter
    def cluster_code(self, cluster_code):
        """Sets the cluster_code of this AbstractCluster.


        :param cluster_code: The cluster_code of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._cluster_code = cluster_code

    @property
    def cluster_state(self):
        """Gets the cluster_state of this AbstractCluster.  # noqa: E501


        :return: The cluster_state of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._cluster_state

    @cluster_state.setter
    def cluster_state(self, cluster_state):
        """Sets the cluster_state of this AbstractCluster.


        :param cluster_state: The cluster_state of this AbstractCluster.  # noqa: E501
        :type: str
        """
        allowed_values = ["STOPPED", "RUNNING", "LAUNCHING", "DESTROYING", "LAUNCH_FAILED", "DESTROY_FAILED", "UNKNOWN", "SCALE_DOWN", "SCALING_DOWN", "SCALE_DOWN_FAILED", "SCALING_UP", "SCALE_UP_FAILED"]  # noqa: E501
        if cluster_state not in allowed_values:
            raise ValueError(
                "Invalid value for `cluster_state` ({0}), must be one of {1}"  # noqa: E501
                .format(cluster_state, allowed_values)
            )

        self._cluster_state = cluster_state

    @property
    def common_environment_variables(self):
        """Gets the common_environment_variables of this AbstractCluster.  # noqa: E501


        :return: The common_environment_variables of this AbstractCluster.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._common_environment_variables

    @common_environment_variables.setter
    def common_environment_variables(self, common_environment_variables):
        """Sets the common_environment_variables of this AbstractCluster.


        :param common_environment_variables: The common_environment_variables of this AbstractCluster.  # noqa: E501
        :type: dict(str, str)
        """

        self._common_environment_variables = common_environment_variables

    @property
    def component_versions(self):
        """Gets the component_versions of this AbstractCluster.  # noqa: E501


        :return: The component_versions of this AbstractCluster.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._component_versions

    @component_versions.setter
    def component_versions(self, component_versions):
        """Sets the component_versions of this AbstractCluster.


        :param component_versions: The component_versions of this AbstractCluster.  # noqa: E501
        :type: dict(str, str)
        """

        self._component_versions = component_versions

    @property
    def configured(self):
        """Gets the configured of this AbstractCluster.  # noqa: E501


        :return: The configured of this AbstractCluster.  # noqa: E501
        :rtype: bool
        """
        return self._configured

    @configured.setter
    def configured(self, configured):
        """Sets the configured of this AbstractCluster.


        :param configured: The configured of this AbstractCluster.  # noqa: E501
        :type: bool
        """

        self._configured = configured

    @property
    def created_by(self):
        """Gets the created_by of this AbstractCluster.  # noqa: E501


        :return: The created_by of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this AbstractCluster.


        :param created_by: The created_by of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def creation_date(self):
        """Gets the creation_date of this AbstractCluster.  # noqa: E501


        :return: The creation_date of this AbstractCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this AbstractCluster.


        :param creation_date: The creation_date of this AbstractCluster.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def deleted(self):
        """Gets the deleted of this AbstractCluster.  # noqa: E501


        :return: The deleted of this AbstractCluster.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this AbstractCluster.


        :param deleted: The deleted of this AbstractCluster.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def dynamic_launch(self):
        """Gets the dynamic_launch of this AbstractCluster.  # noqa: E501


        :return: The dynamic_launch of this AbstractCluster.  # noqa: E501
        :rtype: bool
        """
        return self._dynamic_launch

    @dynamic_launch.setter
    def dynamic_launch(self, dynamic_launch):
        """Sets the dynamic_launch of this AbstractCluster.


        :param dynamic_launch: The dynamic_launch of this AbstractCluster.  # noqa: E501
        :type: bool
        """

        self._dynamic_launch = dynamic_launch

    @property
    def enable_auto_sign_off(self):
        """Gets the enable_auto_sign_off of this AbstractCluster.  # noqa: E501


        :return: The enable_auto_sign_off of this AbstractCluster.  # noqa: E501
        :rtype: bool
        """
        return self._enable_auto_sign_off

    @enable_auto_sign_off.setter
    def enable_auto_sign_off(self, enable_auto_sign_off):
        """Sets the enable_auto_sign_off of this AbstractCluster.


        :param enable_auto_sign_off: The enable_auto_sign_off of this AbstractCluster.  # noqa: E501
        :type: bool
        """

        self._enable_auto_sign_off = enable_auto_sign_off

    @property
    def entity_type(self):
        """Gets the entity_type of this AbstractCluster.  # noqa: E501


        :return: The entity_type of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this AbstractCluster.


        :param entity_type: The entity_type of this AbstractCluster.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLUSTER", "BLUE_PRINT", "TEMPLATE_INPUT", "CONTROL_PLANE", "IAC", "ARTIFACT_CI", "USER_GROUP", "ACCOUNT", "ARTIFACTORY"]  # noqa: E501
        if entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def global_variables(self):
        """Gets the global_variables of this AbstractCluster.  # noqa: E501


        :return: The global_variables of this AbstractCluster.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._global_variables

    @global_variables.setter
    def global_variables(self, global_variables):
        """Sets the global_variables of this AbstractCluster.


        :param global_variables: The global_variables of this AbstractCluster.  # noqa: E501
        :type: dict(str, str)
        """

        self._global_variables = global_variables

    @property
    def id(self):
        """Gets the id of this AbstractCluster.  # noqa: E501


        :return: The id of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AbstractCluster.


        :param id: The id of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_ephemeral(self):
        """Gets the is_ephemeral of this AbstractCluster.  # noqa: E501


        :return: The is_ephemeral of this AbstractCluster.  # noqa: E501
        :rtype: bool
        """
        return self._is_ephemeral

    @is_ephemeral.setter
    def is_ephemeral(self, is_ephemeral):
        """Sets the is_ephemeral of this AbstractCluster.


        :param is_ephemeral: The is_ephemeral of this AbstractCluster.  # noqa: E501
        :type: bool
        """

        self._is_ephemeral = is_ephemeral

    @property
    def k8s_requests_to_limits_ratio(self):
        """Gets the k8s_requests_to_limits_ratio of this AbstractCluster.  # noqa: E501


        :return: The k8s_requests_to_limits_ratio of this AbstractCluster.  # noqa: E501
        :rtype: float
        """
        return self._k8s_requests_to_limits_ratio

    @k8s_requests_to_limits_ratio.setter
    def k8s_requests_to_limits_ratio(self, k8s_requests_to_limits_ratio):
        """Sets the k8s_requests_to_limits_ratio of this AbstractCluster.


        :param k8s_requests_to_limits_ratio: The k8s_requests_to_limits_ratio of this AbstractCluster.  # noqa: E501
        :type: float
        """

        self._k8s_requests_to_limits_ratio = k8s_requests_to_limits_ratio

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this AbstractCluster.  # noqa: E501


        :return: The last_modified_by of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this AbstractCluster.


        :param last_modified_by: The last_modified_by of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this AbstractCluster.  # noqa: E501


        :return: The last_modified_date of this AbstractCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this AbstractCluster.


        :param last_modified_date: The last_modified_date of this AbstractCluster.  # noqa: E501
        :type: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def name(self):
        """Gets the name of this AbstractCluster.  # noqa: E501


        :return: The name of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AbstractCluster.


        :param name: The name of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this AbstractCluster.  # noqa: E501


        :return: The namespace of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this AbstractCluster.


        :param namespace: The namespace of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def number_of_versions(self):
        """Gets the number_of_versions of this AbstractCluster.  # noqa: E501


        :return: The number_of_versions of this AbstractCluster.  # noqa: E501
        :rtype: int
        """
        return self._number_of_versions

    @number_of_versions.setter
    def number_of_versions(self, number_of_versions):
        """Sets the number_of_versions of this AbstractCluster.


        :param number_of_versions: The number_of_versions of this AbstractCluster.  # noqa: E501
        :type: int
        """

        self._number_of_versions = number_of_versions

    @property
    def pause_releases(self):
        """Gets the pause_releases of this AbstractCluster.  # noqa: E501


        :return: The pause_releases of this AbstractCluster.  # noqa: E501
        :rtype: bool
        """
        return self._pause_releases

    @pause_releases.setter
    def pause_releases(self, pause_releases):
        """Sets the pause_releases of this AbstractCluster.


        :param pause_releases: The pause_releases of this AbstractCluster.  # noqa: E501
        :type: bool
        """

        self._pause_releases = pause_releases

    @property
    def release_stream(self):
        """Gets the release_stream of this AbstractCluster.  # noqa: E501


        :return: The release_stream of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._release_stream

    @release_stream.setter
    def release_stream(self, release_stream):
        """Sets the release_stream of this AbstractCluster.


        :param release_stream: The release_stream of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._release_stream = release_stream

    @property
    def require_sign_off(self):
        """Gets the require_sign_off of this AbstractCluster.  # noqa: E501


        :return: The require_sign_off of this AbstractCluster.  # noqa: E501
        :rtype: bool
        """
        return self._require_sign_off

    @require_sign_off.setter
    def require_sign_off(self, require_sign_off):
        """Sets the require_sign_off of this AbstractCluster.


        :param require_sign_off: The require_sign_off of this AbstractCluster.  # noqa: E501
        :type: bool
        """

        self._require_sign_off = require_sign_off

    @property
    def schedules(self):
        """Gets the schedules of this AbstractCluster.  # noqa: E501


        :return: The schedules of this AbstractCluster.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """Sets the schedules of this AbstractCluster.


        :param schedules: The schedules of this AbstractCluster.  # noqa: E501
        :type: dict(str, str)
        """

        self._schedules = schedules

    @property
    def secrets(self):
        """Gets the secrets of this AbstractCluster.  # noqa: E501


        :return: The secrets of this AbstractCluster.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """Sets the secrets of this AbstractCluster.


        :param secrets: The secrets of this AbstractCluster.  # noqa: E501
        :type: dict(str, str)
        """

        self._secrets = secrets

    @property
    def secrets_uid(self):
        """Gets the secrets_uid of this AbstractCluster.  # noqa: E501


        :return: The secrets_uid of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._secrets_uid

    @secrets_uid.setter
    def secrets_uid(self, secrets_uid):
        """Sets the secrets_uid of this AbstractCluster.


        :param secrets_uid: The secrets_uid of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._secrets_uid = secrets_uid

    @property
    def stack_name(self):
        """Gets the stack_name of this AbstractCluster.  # noqa: E501


        :return: The stack_name of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this AbstractCluster.


        :param stack_name: The stack_name of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._stack_name = stack_name

    @property
    def tz(self):
        """Gets the tz of this AbstractCluster.  # noqa: E501


        :return: The tz of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._tz

    @tz.setter
    def tz(self, tz):
        """Sets the tz of this AbstractCluster.


        :param tz: The tz of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._tz = tz

    @property
    def variables(self):
        """Gets the variables of this AbstractCluster.  # noqa: E501


        :return: The variables of this AbstractCluster.  # noqa: E501
        :rtype: dict(str, Variables)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this AbstractCluster.


        :param variables: The variables of this AbstractCluster.  # noqa: E501
        :type: dict(str, Variables)
        """

        self._variables = variables

    @property
    def versioning_key(self):
        """Gets the versioning_key of this AbstractCluster.  # noqa: E501


        :return: The versioning_key of this AbstractCluster.  # noqa: E501
        :rtype: str
        """
        return self._versioning_key

    @versioning_key.setter
    def versioning_key(self, versioning_key):
        """Sets the versioning_key of this AbstractCluster.


        :param versioning_key: The versioning_key of this AbstractCluster.  # noqa: E501
        :type: str
        """

        self._versioning_key = versioning_key

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
        if issubclass(AbstractCluster, dict):
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
        if not isinstance(other, AbstractCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
