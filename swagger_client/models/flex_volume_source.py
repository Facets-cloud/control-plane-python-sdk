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

class FlexVolumeSource(object):
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
        'driver': 'str',
        'fs_type': 'str',
        'options': 'dict(str, str)',
        'read_only': 'bool',
        'secret_ref': 'LocalObjectReference'
    }

    attribute_map = {
        'driver': 'driver',
        'fs_type': 'fsType',
        'options': 'options',
        'read_only': 'readOnly',
        'secret_ref': 'secretRef'
    }

    def __init__(self, driver=None, fs_type=None, options=None, read_only=None, secret_ref=None):  # noqa: E501
        """FlexVolumeSource - a model defined in Swagger"""  # noqa: E501
        self._driver = None
        self._fs_type = None
        self._options = None
        self._read_only = None
        self._secret_ref = None
        self.discriminator = None
        if driver is not None:
            self.driver = driver
        if fs_type is not None:
            self.fs_type = fs_type
        if options is not None:
            self.options = options
        if read_only is not None:
            self.read_only = read_only
        if secret_ref is not None:
            self.secret_ref = secret_ref

    @property
    def driver(self):
        """Gets the driver of this FlexVolumeSource.  # noqa: E501


        :return: The driver of this FlexVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this FlexVolumeSource.


        :param driver: The driver of this FlexVolumeSource.  # noqa: E501
        :type: str
        """

        self._driver = driver

    @property
    def fs_type(self):
        """Gets the fs_type of this FlexVolumeSource.  # noqa: E501


        :return: The fs_type of this FlexVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """Sets the fs_type of this FlexVolumeSource.


        :param fs_type: The fs_type of this FlexVolumeSource.  # noqa: E501
        :type: str
        """

        self._fs_type = fs_type

    @property
    def options(self):
        """Gets the options of this FlexVolumeSource.  # noqa: E501


        :return: The options of this FlexVolumeSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this FlexVolumeSource.


        :param options: The options of this FlexVolumeSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._options = options

    @property
    def read_only(self):
        """Gets the read_only of this FlexVolumeSource.  # noqa: E501


        :return: The read_only of this FlexVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this FlexVolumeSource.


        :param read_only: The read_only of this FlexVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def secret_ref(self):
        """Gets the secret_ref of this FlexVolumeSource.  # noqa: E501


        :return: The secret_ref of this FlexVolumeSource.  # noqa: E501
        :rtype: LocalObjectReference
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """Sets the secret_ref of this FlexVolumeSource.


        :param secret_ref: The secret_ref of this FlexVolumeSource.  # noqa: E501
        :type: LocalObjectReference
        """

        self._secret_ref = secret_ref

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
        if issubclass(FlexVolumeSource, dict):
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
        if not isinstance(other, FlexVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
