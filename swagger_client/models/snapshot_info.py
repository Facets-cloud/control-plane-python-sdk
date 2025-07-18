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

class SnapshotInfo(object):
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
        'cluster_id': 'str',
        'name': 'str',
        'cloud_specific_id': 'str',
        'resource_type': 'str',
        'instance_name': 'str',
        'source': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'storage_size': 'int',
        'pinned': 'bool'
    }

    attribute_map = {
        'cluster_id': 'clusterId',
        'name': 'name',
        'cloud_specific_id': 'cloudSpecificId',
        'resource_type': 'resourceType',
        'instance_name': 'instanceName',
        'source': 'source',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'storage_size': 'storageSize',
        'pinned': 'pinned'
    }

    def __init__(self, cluster_id=None, name=None, cloud_specific_id=None, resource_type=None, instance_name=None, source=None, start_time=None, end_time=None, storage_size=None, pinned=None):  # noqa: E501
        """SnapshotInfo - a model defined in Swagger"""  # noqa: E501
        self._cluster_id = None
        self._name = None
        self._cloud_specific_id = None
        self._resource_type = None
        self._instance_name = None
        self._source = None
        self._start_time = None
        self._end_time = None
        self._storage_size = None
        self._pinned = None
        self.discriminator = None
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if name is not None:
            self.name = name
        if cloud_specific_id is not None:
            self.cloud_specific_id = cloud_specific_id
        if resource_type is not None:
            self.resource_type = resource_type
        if instance_name is not None:
            self.instance_name = instance_name
        if source is not None:
            self.source = source
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if storage_size is not None:
            self.storage_size = storage_size
        if pinned is not None:
            self.pinned = pinned

    @property
    def cluster_id(self):
        """Gets the cluster_id of this SnapshotInfo.  # noqa: E501


        :return: The cluster_id of this SnapshotInfo.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this SnapshotInfo.


        :param cluster_id: The cluster_id of this SnapshotInfo.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def name(self):
        """Gets the name of this SnapshotInfo.  # noqa: E501


        :return: The name of this SnapshotInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnapshotInfo.


        :param name: The name of this SnapshotInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def cloud_specific_id(self):
        """Gets the cloud_specific_id of this SnapshotInfo.  # noqa: E501


        :return: The cloud_specific_id of this SnapshotInfo.  # noqa: E501
        :rtype: str
        """
        return self._cloud_specific_id

    @cloud_specific_id.setter
    def cloud_specific_id(self, cloud_specific_id):
        """Sets the cloud_specific_id of this SnapshotInfo.


        :param cloud_specific_id: The cloud_specific_id of this SnapshotInfo.  # noqa: E501
        :type: str
        """

        self._cloud_specific_id = cloud_specific_id

    @property
    def resource_type(self):
        """Gets the resource_type of this SnapshotInfo.  # noqa: E501


        :return: The resource_type of this SnapshotInfo.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this SnapshotInfo.


        :param resource_type: The resource_type of this SnapshotInfo.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def instance_name(self):
        """Gets the instance_name of this SnapshotInfo.  # noqa: E501


        :return: The instance_name of this SnapshotInfo.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this SnapshotInfo.


        :param instance_name: The instance_name of this SnapshotInfo.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def source(self):
        """Gets the source of this SnapshotInfo.  # noqa: E501


        :return: The source of this SnapshotInfo.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SnapshotInfo.


        :param source: The source of this SnapshotInfo.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def start_time(self):
        """Gets the start_time of this SnapshotInfo.  # noqa: E501


        :return: The start_time of this SnapshotInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SnapshotInfo.


        :param start_time: The start_time of this SnapshotInfo.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this SnapshotInfo.  # noqa: E501


        :return: The end_time of this SnapshotInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SnapshotInfo.


        :param end_time: The end_time of this SnapshotInfo.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def storage_size(self):
        """Gets the storage_size of this SnapshotInfo.  # noqa: E501


        :return: The storage_size of this SnapshotInfo.  # noqa: E501
        :rtype: int
        """
        return self._storage_size

    @storage_size.setter
    def storage_size(self, storage_size):
        """Sets the storage_size of this SnapshotInfo.


        :param storage_size: The storage_size of this SnapshotInfo.  # noqa: E501
        :type: int
        """

        self._storage_size = storage_size

    @property
    def pinned(self):
        """Gets the pinned of this SnapshotInfo.  # noqa: E501


        :return: The pinned of this SnapshotInfo.  # noqa: E501
        :rtype: bool
        """
        return self._pinned

    @pinned.setter
    def pinned(self, pinned):
        """Sets the pinned of this SnapshotInfo.


        :param pinned: The pinned of this SnapshotInfo.  # noqa: E501
        :type: bool
        """

        self._pinned = pinned

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
        if issubclass(SnapshotInfo, dict):
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
        if not isinstance(other, SnapshotInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
