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

class FCVolumeSource(object):
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
        'fs_type': 'str',
        'lun': 'int',
        'read_only': 'bool',
        'target_wwns': 'list[str]',
        'wwids': 'list[str]'
    }

    attribute_map = {
        'fs_type': 'fsType',
        'lun': 'lun',
        'read_only': 'readOnly',
        'target_wwns': 'targetWWNs',
        'wwids': 'wwids'
    }

    def __init__(self, fs_type=None, lun=None, read_only=None, target_wwns=None, wwids=None):  # noqa: E501
        """FCVolumeSource - a model defined in Swagger"""  # noqa: E501
        self._fs_type = None
        self._lun = None
        self._read_only = None
        self._target_wwns = None
        self._wwids = None
        self.discriminator = None
        if fs_type is not None:
            self.fs_type = fs_type
        if lun is not None:
            self.lun = lun
        if read_only is not None:
            self.read_only = read_only
        if target_wwns is not None:
            self.target_wwns = target_wwns
        if wwids is not None:
            self.wwids = wwids

    @property
    def fs_type(self):
        """Gets the fs_type of this FCVolumeSource.  # noqa: E501


        :return: The fs_type of this FCVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this FCVolumeSource.


        :param fs_type: The fs_type of this FCVolumeSource.  # noqa: E501
        :type: str
        """

        self._fs_type = fs_type

    @property
    def lun(self):
        """Gets the lun of this FCVolumeSource.  # noqa: E501


        :return: The lun of this FCVolumeSource.  # noqa: E501
        :rtype: int
        """
        return self._lun

    @lun.setter
    def lun(self, lun):
        """Sets the lun of this FCVolumeSource.


        :param lun: The lun of this FCVolumeSource.  # noqa: E501
        :type: int
        """

        self._lun = lun

    @property
    def read_only(self):
        """Gets the read_only of this FCVolumeSource.  # noqa: E501


        :return: The read_only of this FCVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this FCVolumeSource.


        :param read_only: The read_only of this FCVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def target_wwns(self):
        """Gets the target_wwns of this FCVolumeSource.  # noqa: E501


        :return: The target_wwns of this FCVolumeSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_wwns

    @target_wwns.setter
    def target_wwns(self, target_wwns):
        """Sets the target_wwns of this FCVolumeSource.


        :param target_wwns: The target_wwns of this FCVolumeSource.  # noqa: E501
        :type: list[str]
        """

        self._target_wwns = target_wwns

    @property
    def wwids(self):
        """Gets the wwids of this FCVolumeSource.  # noqa: E501


        :return: The wwids of this FCVolumeSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._wwids

    @wwids.setter
    def wwids(self, wwids):
        """Sets the wwids of this FCVolumeSource.


        :param wwids: The wwids of this FCVolumeSource.  # noqa: E501
        :type: list[str]
        """

        self._wwids = wwids

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
        if issubclass(FCVolumeSource, dict):
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
        if not isinstance(other, FCVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
