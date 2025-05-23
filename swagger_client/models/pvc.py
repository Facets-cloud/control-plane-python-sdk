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

class PVC(object):
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
        'access_mode': 'str',
        'mount_path': 'str',
        'name': 'str',
        'storage_size': 'int',
        'volume_directory': 'str'
    }

    attribute_map = {
        'access_mode': 'accessMode',
        'mount_path': 'mountPath',
        'name': 'name',
        'storage_size': 'storageSize',
        'volume_directory': 'volumeDirectory'
    }

    def __init__(self, access_mode=None, mount_path=None, name=None, storage_size=None, volume_directory=None):  # noqa: E501
        """PVC - a model defined in Swagger"""  # noqa: E501
        self._access_mode = None
        self._mount_path = None
        self._name = None
        self._storage_size = None
        self._volume_directory = None
        self.discriminator = None
        if access_mode is not None:
            self.access_mode = access_mode
        if mount_path is not None:
            self.mount_path = mount_path
        if name is not None:
            self.name = name
        if storage_size is not None:
            self.storage_size = storage_size
        if volume_directory is not None:
            self.volume_directory = volume_directory

    @property
    def access_mode(self):
        """Gets the access_mode of this PVC.  # noqa: E501


        :return: The access_mode of this PVC.  # noqa: E501
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this PVC.


        :param access_mode: The access_mode of this PVC.  # noqa: E501
        :type: str
        """
        allowed_values = ["ReadWriteOnce", "ReadOnlyMany", "ReadWriteMany"]  # noqa: E501
        if access_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `access_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(access_mode, allowed_values)
            )

        self._access_mode = access_mode

    @property
    def mount_path(self):
        """Gets the mount_path of this PVC.  # noqa: E501


        :return: The mount_path of this PVC.  # noqa: E501
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        """Sets the mount_path of this PVC.


        :param mount_path: The mount_path of this PVC.  # noqa: E501
        :type: str
        """

        self._mount_path = mount_path

    @property
    def name(self):
        """Gets the name of this PVC.  # noqa: E501


        :return: The name of this PVC.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PVC.


        :param name: The name of this PVC.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def storage_size(self):
        """Gets the storage_size of this PVC.  # noqa: E501


        :return: The storage_size of this PVC.  # noqa: E501
        :rtype: int
        """
        return self._storage_size

    @storage_size.setter
    def storage_size(self, storage_size):
        """Sets the storage_size of this PVC.


        :param storage_size: The storage_size of this PVC.  # noqa: E501
        :type: int
        """

        self._storage_size = storage_size

    @property
    def volume_directory(self):
        """Gets the volume_directory of this PVC.  # noqa: E501


        :return: The volume_directory of this PVC.  # noqa: E501
        :rtype: str
        """
        return self._volume_directory

    @volume_directory.setter
    def volume_directory(self, volume_directory):
        """Sets the volume_directory of this PVC.


        :param volume_directory: The volume_directory of this PVC.  # noqa: E501
        :type: str
        """

        self._volume_directory = volume_directory

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
        if issubclass(PVC, dict):
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
        if not isinstance(other, PVC):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
