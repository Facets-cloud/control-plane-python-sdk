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

class PersistentVolumeClaimVolumeSource(object):
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
        'claim_name': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'claim_name': 'claimName',
        'read_only': 'readOnly'
    }

    def __init__(self, claim_name=None, read_only=None):  # noqa: E501
        """PersistentVolumeClaimVolumeSource - a model defined in Swagger"""  # noqa: E501
        self._claim_name = None
        self._read_only = None
        self.discriminator = None
        if claim_name is not None:
            self.claim_name = claim_name
        if read_only is not None:
            self.read_only = read_only

    @property
    def claim_name(self):
        """Gets the claim_name of this PersistentVolumeClaimVolumeSource.  # noqa: E501


        :return: The claim_name of this PersistentVolumeClaimVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._claim_name

    @claim_name.setter
    def claim_name(self, claim_name):
        """Sets the claim_name of this PersistentVolumeClaimVolumeSource.


        :param claim_name: The claim_name of this PersistentVolumeClaimVolumeSource.  # noqa: E501
        :type: str
        """

        self._claim_name = claim_name

    @property
    def read_only(self):
        """Gets the read_only of this PersistentVolumeClaimVolumeSource.  # noqa: E501


        :return: The read_only of this PersistentVolumeClaimVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this PersistentVolumeClaimVolumeSource.


        :param read_only: The read_only of this PersistentVolumeClaimVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

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
        if issubclass(PersistentVolumeClaimVolumeSource, dict):
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
        if not isinstance(other, PersistentVolumeClaimVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
