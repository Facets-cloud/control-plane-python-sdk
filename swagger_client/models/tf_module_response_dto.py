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

class TFModuleResponseDTO(object):
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
        'created_by': 'str',
        'creation_date': 'datetime',
        'last_modified_date': 'datetime',
        'last_modified_by': 'str',
        'intent_details': 'IntentResponseDTO',
        'intent': 'str',
        'flavor': 'str',
        'alias_flavors': 'list[str]',
        'version': 'str',
        'clouds': 'list[str]',
        'source': 'str',
        'stage': 'str',
        'preview_module_id': 'str',
        'published_module_id': 'str',
        'type': 'str',
        'git_url': 'str',
        'git_ref': 'str',
        'sample_json': 'str',
        'spec': 'str',
        'metadata': 'str',
        'inputs': 'dict(str, Input)',
        'outputs': 'list[IntentOutput]',
        'versioning_key': 'str',
        'description': 'str',
        'readme_md': 'str',
        'other_versions': 'list[OtherVersion]',
        'latest_version': 'OtherVersion',
        'tags': 'list[str]',
        'allowed_test_projects': 'list[str]',
        'iac_tool': 'list[str]',
        'name_length_limit': 'int',
        'feature_branch': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'creation_date': 'creationDate',
        'last_modified_date': 'lastModifiedDate',
        'last_modified_by': 'lastModifiedBy',
        'intent_details': 'intentDetails',
        'intent': 'intent',
        'flavor': 'flavor',
        'alias_flavors': 'aliasFlavors',
        'version': 'version',
        'clouds': 'clouds',
        'source': 'source',
        'stage': 'stage',
        'preview_module_id': 'previewModuleId',
        'published_module_id': 'publishedModuleId',
        'type': 'type',
        'git_url': 'gitUrl',
        'git_ref': 'gitRef',
        'sample_json': 'sampleJson',
        'spec': 'spec',
        'metadata': 'metadata',
        'inputs': 'inputs',
        'outputs': 'outputs',
        'versioning_key': 'versioningKey',
        'description': 'description',
        'readme_md': 'readmeMd',
        'other_versions': 'otherVersions',
        'latest_version': 'latestVersion',
        'tags': 'tags',
        'allowed_test_projects': 'allowedTestProjects',
        'iac_tool': 'iacTool',
        'name_length_limit': 'nameLengthLimit',
        'feature_branch': 'featureBranch'
    }

    def __init__(self, id=None, created_by=None, creation_date=None, last_modified_date=None, last_modified_by=None, intent_details=None, intent=None, flavor=None, alias_flavors=None, version=None, clouds=None, source=None, stage=None, preview_module_id=None, published_module_id=None, type=None, git_url=None, git_ref=None, sample_json=None, spec=None, metadata=None, inputs=None, outputs=None, versioning_key=None, description=None, readme_md=None, other_versions=None, latest_version=None, tags=None, allowed_test_projects=None, iac_tool=None, name_length_limit=None, feature_branch=None):  # noqa: E501
        """TFModuleResponseDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_by = None
        self._creation_date = None
        self._last_modified_date = None
        self._last_modified_by = None
        self._intent_details = None
        self._intent = None
        self._flavor = None
        self._alias_flavors = None
        self._version = None
        self._clouds = None
        self._source = None
        self._stage = None
        self._preview_module_id = None
        self._published_module_id = None
        self._type = None
        self._git_url = None
        self._git_ref = None
        self._sample_json = None
        self._spec = None
        self._metadata = None
        self._inputs = None
        self._outputs = None
        self._versioning_key = None
        self._description = None
        self._readme_md = None
        self._other_versions = None
        self._latest_version = None
        self._tags = None
        self._allowed_test_projects = None
        self._iac_tool = None
        self._name_length_limit = None
        self._feature_branch = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_by is not None:
            self.created_by = created_by
        if creation_date is not None:
            self.creation_date = creation_date
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if intent_details is not None:
            self.intent_details = intent_details
        if intent is not None:
            self.intent = intent
        if flavor is not None:
            self.flavor = flavor
        if alias_flavors is not None:
            self.alias_flavors = alias_flavors
        if version is not None:
            self.version = version
        if clouds is not None:
            self.clouds = clouds
        if source is not None:
            self.source = source
        if stage is not None:
            self.stage = stage
        if preview_module_id is not None:
            self.preview_module_id = preview_module_id
        if published_module_id is not None:
            self.published_module_id = published_module_id
        if type is not None:
            self.type = type
        if git_url is not None:
            self.git_url = git_url
        if git_ref is not None:
            self.git_ref = git_ref
        if sample_json is not None:
            self.sample_json = sample_json
        if spec is not None:
            self.spec = spec
        if metadata is not None:
            self.metadata = metadata
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if versioning_key is not None:
            self.versioning_key = versioning_key
        if description is not None:
            self.description = description
        if readme_md is not None:
            self.readme_md = readme_md
        if other_versions is not None:
            self.other_versions = other_versions
        if latest_version is not None:
            self.latest_version = latest_version
        if tags is not None:
            self.tags = tags
        if allowed_test_projects is not None:
            self.allowed_test_projects = allowed_test_projects
        if iac_tool is not None:
            self.iac_tool = iac_tool
        if name_length_limit is not None:
            self.name_length_limit = name_length_limit
        if feature_branch is not None:
            self.feature_branch = feature_branch

    @property
    def id(self):
        """Gets the id of this TFModuleResponseDTO.  # noqa: E501


        :return: The id of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TFModuleResponseDTO.


        :param id: The id of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this TFModuleResponseDTO.  # noqa: E501


        :return: The created_by of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this TFModuleResponseDTO.


        :param created_by: The created_by of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def creation_date(self):
        """Gets the creation_date of this TFModuleResponseDTO.  # noqa: E501


        :return: The creation_date of this TFModuleResponseDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this TFModuleResponseDTO.


        :param creation_date: The creation_date of this TFModuleResponseDTO.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this TFModuleResponseDTO.  # noqa: E501


        :return: The last_modified_date of this TFModuleResponseDTO.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this TFModuleResponseDTO.


        :param last_modified_date: The last_modified_date of this TFModuleResponseDTO.  # noqa: E501
        :type: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this TFModuleResponseDTO.  # noqa: E501


        :return: The last_modified_by of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this TFModuleResponseDTO.


        :param last_modified_by: The last_modified_by of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def intent_details(self):
        """Gets the intent_details of this TFModuleResponseDTO.  # noqa: E501


        :return: The intent_details of this TFModuleResponseDTO.  # noqa: E501
        :rtype: IntentResponseDTO
        """
        return self._intent_details

    @intent_details.setter
    def intent_details(self, intent_details):
        """Sets the intent_details of this TFModuleResponseDTO.


        :param intent_details: The intent_details of this TFModuleResponseDTO.  # noqa: E501
        :type: IntentResponseDTO
        """

        self._intent_details = intent_details

    @property
    def intent(self):
        """Gets the intent of this TFModuleResponseDTO.  # noqa: E501

        Intent of the TF Module  # noqa: E501

        :return: The intent of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._intent

    @intent.setter
    def intent(self, intent):
        """Sets the intent of this TFModuleResponseDTO.

        Intent of the TF Module  # noqa: E501

        :param intent: The intent of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._intent = intent

    @property
    def flavor(self):
        """Gets the flavor of this TFModuleResponseDTO.  # noqa: E501

        Flavor of the TF Module  # noqa: E501

        :return: The flavor of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this TFModuleResponseDTO.

        Flavor of the TF Module  # noqa: E501

        :param flavor: The flavor of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._flavor = flavor

    @property
    def alias_flavors(self):
        """Gets the alias_flavors of this TFModuleResponseDTO.  # noqa: E501

        Alias flavors for the module  # noqa: E501

        :return: The alias_flavors of this TFModuleResponseDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._alias_flavors

    @alias_flavors.setter
    def alias_flavors(self, alias_flavors):
        """Sets the alias_flavors of this TFModuleResponseDTO.

        Alias flavors for the module  # noqa: E501

        :param alias_flavors: The alias_flavors of this TFModuleResponseDTO.  # noqa: E501
        :type: list[str]
        """

        self._alias_flavors = alias_flavors

    @property
    def version(self):
        """Gets the version of this TFModuleResponseDTO.  # noqa: E501

        Version of the TF Module  # noqa: E501

        :return: The version of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TFModuleResponseDTO.

        Version of the TF Module  # noqa: E501

        :param version: The version of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def clouds(self):
        """Gets the clouds of this TFModuleResponseDTO.  # noqa: E501

        Supported cloud providers  # noqa: E501

        :return: The clouds of this TFModuleResponseDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._clouds

    @clouds.setter
    def clouds(self, clouds):
        """Sets the clouds of this TFModuleResponseDTO.

        Supported cloud providers  # noqa: E501

        :param clouds: The clouds of this TFModuleResponseDTO.  # noqa: E501
        :type: list[str]
        """

        self._clouds = clouds

    @property
    def source(self):
        """Gets the source of this TFModuleResponseDTO.  # noqa: E501

        Source of the TF Module  # noqa: E501

        :return: The source of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this TFModuleResponseDTO.

        Source of the TF Module  # noqa: E501

        :param source: The source of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["BUILT_IN", "CUSTOM"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def stage(self):
        """Gets the stage of this TFModuleResponseDTO.  # noqa: E501

        Stage of the TF Module in its lifecycle  # noqa: E501

        :return: The stage of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this TFModuleResponseDTO.

        Stage of the TF Module in its lifecycle  # noqa: E501

        :param stage: The stage of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["PREVIEW", "PUBLISHED"]  # noqa: E501
        if stage not in allowed_values:
            raise ValueError(
                "Invalid value for `stage` ({0}), must be one of {1}"  # noqa: E501
                .format(stage, allowed_values)
            )

        self._stage = stage

    @property
    def preview_module_id(self):
        """Gets the preview_module_id of this TFModuleResponseDTO.  # noqa: E501


        :return: The preview_module_id of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._preview_module_id

    @preview_module_id.setter
    def preview_module_id(self, preview_module_id):
        """Sets the preview_module_id of this TFModuleResponseDTO.


        :param preview_module_id: The preview_module_id of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._preview_module_id = preview_module_id

    @property
    def published_module_id(self):
        """Gets the published_module_id of this TFModuleResponseDTO.  # noqa: E501


        :return: The published_module_id of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._published_module_id

    @published_module_id.setter
    def published_module_id(self, published_module_id):
        """Sets the published_module_id of this TFModuleResponseDTO.


        :param published_module_id: The published_module_id of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._published_module_id = published_module_id

    @property
    def type(self):
        """Gets the type of this TFModuleResponseDTO.  # noqa: E501

        Type of the TF Module  # noqa: E501

        :return: The type of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TFModuleResponseDTO.

        Type of the TF Module  # noqa: E501

        :param type: The type of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["SIMPLE", "ADD_ON"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def git_url(self):
        """Gets the git_url of this TFModuleResponseDTO.  # noqa: E501

        URL of the GIT repository  # noqa: E501

        :return: The git_url of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        """Sets the git_url of this TFModuleResponseDTO.

        URL of the GIT repository  # noqa: E501

        :param git_url: The git_url of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._git_url = git_url

    @property
    def git_ref(self):
        """Gets the git_ref of this TFModuleResponseDTO.  # noqa: E501

        Reference to a specific GIT branch or commit  # noqa: E501

        :return: The git_ref of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._git_ref

    @git_ref.setter
    def git_ref(self, git_ref):
        """Sets the git_ref of this TFModuleResponseDTO.

        Reference to a specific GIT branch or commit  # noqa: E501

        :param git_ref: The git_ref of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._git_ref = git_ref

    @property
    def sample_json(self):
        """Gets the sample_json of this TFModuleResponseDTO.  # noqa: E501

        Sample JSON configuration  # noqa: E501

        :return: The sample_json of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._sample_json

    @sample_json.setter
    def sample_json(self, sample_json):
        """Sets the sample_json of this TFModuleResponseDTO.

        Sample JSON configuration  # noqa: E501

        :param sample_json: The sample_json of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._sample_json = sample_json

    @property
    def spec(self):
        """Gets the spec of this TFModuleResponseDTO.  # noqa: E501

        Specification details of the module  # noqa: E501

        :return: The spec of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this TFModuleResponseDTO.

        Specification details of the module  # noqa: E501

        :param spec: The spec of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._spec = spec

    @property
    def metadata(self):
        """Gets the metadata of this TFModuleResponseDTO.  # noqa: E501

        Metadata of the module  # noqa: E501

        :return: The metadata of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this TFModuleResponseDTO.

        Metadata of the module  # noqa: E501

        :param metadata: The metadata of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def inputs(self):
        """Gets the inputs of this TFModuleResponseDTO.  # noqa: E501

        Input parameters for this module  # noqa: E501

        :return: The inputs of this TFModuleResponseDTO.  # noqa: E501
        :rtype: dict(str, Input)
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this TFModuleResponseDTO.

        Input parameters for this module  # noqa: E501

        :param inputs: The inputs of this TFModuleResponseDTO.  # noqa: E501
        :type: dict(str, Input)
        """

        self._inputs = inputs

    @property
    def outputs(self):
        """Gets the outputs of this TFModuleResponseDTO.  # noqa: E501


        :return: The outputs of this TFModuleResponseDTO.  # noqa: E501
        :rtype: list[IntentOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this TFModuleResponseDTO.


        :param outputs: The outputs of this TFModuleResponseDTO.  # noqa: E501
        :type: list[IntentOutput]
        """

        self._outputs = outputs

    @property
    def versioning_key(self):
        """Gets the versioning_key of this TFModuleResponseDTO.  # noqa: E501


        :return: The versioning_key of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._versioning_key

    @versioning_key.setter
    def versioning_key(self, versioning_key):
        """Sets the versioning_key of this TFModuleResponseDTO.


        :param versioning_key: The versioning_key of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._versioning_key = versioning_key

    @property
    def description(self):
        """Gets the description of this TFModuleResponseDTO.  # noqa: E501

        Module description  # noqa: E501

        :return: The description of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TFModuleResponseDTO.

        Module description  # noqa: E501

        :param description: The description of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def readme_md(self):
        """Gets the readme_md of this TFModuleResponseDTO.  # noqa: E501

        Readme content in markdown format  # noqa: E501

        :return: The readme_md of this TFModuleResponseDTO.  # noqa: E501
        :rtype: str
        """
        return self._readme_md

    @readme_md.setter
    def readme_md(self, readme_md):
        """Sets the readme_md of this TFModuleResponseDTO.

        Readme content in markdown format  # noqa: E501

        :param readme_md: The readme_md of this TFModuleResponseDTO.  # noqa: E501
        :type: str
        """

        self._readme_md = readme_md

    @property
    def other_versions(self):
        """Gets the other_versions of this TFModuleResponseDTO.  # noqa: E501


        :return: The other_versions of this TFModuleResponseDTO.  # noqa: E501
        :rtype: list[OtherVersion]
        """
        return self._other_versions

    @other_versions.setter
    def other_versions(self, other_versions):
        """Sets the other_versions of this TFModuleResponseDTO.


        :param other_versions: The other_versions of this TFModuleResponseDTO.  # noqa: E501
        :type: list[OtherVersion]
        """

        self._other_versions = other_versions

    @property
    def latest_version(self):
        """Gets the latest_version of this TFModuleResponseDTO.  # noqa: E501


        :return: The latest_version of this TFModuleResponseDTO.  # noqa: E501
        :rtype: OtherVersion
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this TFModuleResponseDTO.


        :param latest_version: The latest_version of this TFModuleResponseDTO.  # noqa: E501
        :type: OtherVersion
        """

        self._latest_version = latest_version

    @property
    def tags(self):
        """Gets the tags of this TFModuleResponseDTO.  # noqa: E501

        Tags associated with the module  # noqa: E501

        :return: The tags of this TFModuleResponseDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TFModuleResponseDTO.

        Tags associated with the module  # noqa: E501

        :param tags: The tags of this TFModuleResponseDTO.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def allowed_test_projects(self):
        """Gets the allowed_test_projects of this TFModuleResponseDTO.  # noqa: E501

        List of test projects where this module will be available. If absent, it is available globally.  # noqa: E501

        :return: The allowed_test_projects of this TFModuleResponseDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_test_projects

    @allowed_test_projects.setter
    def allowed_test_projects(self, allowed_test_projects):
        """Sets the allowed_test_projects of this TFModuleResponseDTO.

        List of test projects where this module will be available. If absent, it is available globally.  # noqa: E501

        :param allowed_test_projects: The allowed_test_projects of this TFModuleResponseDTO.  # noqa: E501
        :type: list[str]
        """

        self._allowed_test_projects = allowed_test_projects

    @property
    def iac_tool(self):
        """Gets the iac_tool of this TFModuleResponseDTO.  # noqa: E501


        :return: The iac_tool of this TFModuleResponseDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._iac_tool

    @iac_tool.setter
    def iac_tool(self, iac_tool):
        """Sets the iac_tool of this TFModuleResponseDTO.


        :param iac_tool: The iac_tool of this TFModuleResponseDTO.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["TERRAFORM", "OPENTOFU"]  # noqa: E501
        if not set(iac_tool).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `iac_tool` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(iac_tool) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._iac_tool = iac_tool

    @property
    def name_length_limit(self):
        """Gets the name_length_limit of this TFModuleResponseDTO.  # noqa: E501

        Maximum allowed length for resource names using this module  # noqa: E501

        :return: The name_length_limit of this TFModuleResponseDTO.  # noqa: E501
        :rtype: int
        """
        return self._name_length_limit

    @name_length_limit.setter
    def name_length_limit(self, name_length_limit):
        """Sets the name_length_limit of this TFModuleResponseDTO.

        Maximum allowed length for resource names using this module  # noqa: E501

        :param name_length_limit: The name_length_limit of this TFModuleResponseDTO.  # noqa: E501
        :type: int
        """

        self._name_length_limit = name_length_limit

    @property
    def feature_branch(self):
        """Gets the feature_branch of this TFModuleResponseDTO.  # noqa: E501


        :return: The feature_branch of this TFModuleResponseDTO.  # noqa: E501
        :rtype: bool
        """
        return self._feature_branch

    @feature_branch.setter
    def feature_branch(self, feature_branch):
        """Sets the feature_branch of this TFModuleResponseDTO.


        :param feature_branch: The feature_branch of this TFModuleResponseDTO.  # noqa: E501
        :type: bool
        """

        self._feature_branch = feature_branch

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
        if issubclass(TFModuleResponseDTO, dict):
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
        if not isinstance(other, TFModuleResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
