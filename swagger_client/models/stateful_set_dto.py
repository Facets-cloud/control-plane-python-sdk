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

class StatefulSetDTO(object):
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
        'age_in_seconds': 'int',
        'desired_replicas': 'int',
        'name': 'str',
        'pod_count': 'int',
        'ready_replicas': 'int',
        'replicas': 'int',
        'status': 'str'
    }

    attribute_map = {
        'age_in_seconds': 'ageInSeconds',
        'desired_replicas': 'desiredReplicas',
        'name': 'name',
        'pod_count': 'podCount',
        'ready_replicas': 'readyReplicas',
        'replicas': 'replicas',
        'status': 'status'
    }

    def __init__(self, age_in_seconds=None, desired_replicas=None, name=None, pod_count=None, ready_replicas=None, replicas=None, status=None):  # noqa: E501
        """StatefulSetDTO - a model defined in Swagger"""  # noqa: E501
        self._age_in_seconds = None
        self._desired_replicas = None
        self._name = None
        self._pod_count = None
        self._ready_replicas = None
        self._replicas = None
        self._status = None
        self.discriminator = None
        if age_in_seconds is not None:
            self.age_in_seconds = age_in_seconds
        if desired_replicas is not None:
            self.desired_replicas = desired_replicas
        if name is not None:
            self.name = name
        if pod_count is not None:
            self.pod_count = pod_count
        if ready_replicas is not None:
            self.ready_replicas = ready_replicas
        if replicas is not None:
            self.replicas = replicas
        if status is not None:
            self.status = status

    @property
    def age_in_seconds(self):
        """Gets the age_in_seconds of this StatefulSetDTO.  # noqa: E501


        :return: The age_in_seconds of this StatefulSetDTO.  # noqa: E501
        :rtype: int
        """
        return self._age_in_seconds

    @age_in_seconds.setter
    def age_in_seconds(self, age_in_seconds):
        """Sets the age_in_seconds of this StatefulSetDTO.


        :param age_in_seconds: The age_in_seconds of this StatefulSetDTO.  # noqa: E501
        :type: int
        """

        self._age_in_seconds = age_in_seconds

    @property
    def desired_replicas(self):
        """Gets the desired_replicas of this StatefulSetDTO.  # noqa: E501


        :return: The desired_replicas of this StatefulSetDTO.  # noqa: E501
        :rtype: int
        """
        return self._desired_replicas

    @desired_replicas.setter
    def desired_replicas(self, desired_replicas):
        """Sets the desired_replicas of this StatefulSetDTO.


        :param desired_replicas: The desired_replicas of this StatefulSetDTO.  # noqa: E501
        :type: int
        """

        self._desired_replicas = desired_replicas

    @property
    def name(self):
        """Gets the name of this StatefulSetDTO.  # noqa: E501


        :return: The name of this StatefulSetDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StatefulSetDTO.


        :param name: The name of this StatefulSetDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pod_count(self):
        """Gets the pod_count of this StatefulSetDTO.  # noqa: E501


        :return: The pod_count of this StatefulSetDTO.  # noqa: E501
        :rtype: int
        """
        return self._pod_count

    @pod_count.setter
    def pod_count(self, pod_count):
        """Sets the pod_count of this StatefulSetDTO.


        :param pod_count: The pod_count of this StatefulSetDTO.  # noqa: E501
        :type: int
        """

        self._pod_count = pod_count

    @property
    def ready_replicas(self):
        """Gets the ready_replicas of this StatefulSetDTO.  # noqa: E501


        :return: The ready_replicas of this StatefulSetDTO.  # noqa: E501
        :rtype: int
        """
        return self._ready_replicas

    @ready_replicas.setter
    def ready_replicas(self, ready_replicas):
        """Sets the ready_replicas of this StatefulSetDTO.


        :param ready_replicas: The ready_replicas of this StatefulSetDTO.  # noqa: E501
        :type: int
        """

        self._ready_replicas = ready_replicas

    @property
    def replicas(self):
        """Gets the replicas of this StatefulSetDTO.  # noqa: E501


        :return: The replicas of this StatefulSetDTO.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this StatefulSetDTO.


        :param replicas: The replicas of this StatefulSetDTO.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def status(self):
        """Gets the status of this StatefulSetDTO.  # noqa: E501


        :return: The status of this StatefulSetDTO.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StatefulSetDTO.


        :param status: The status of this StatefulSetDTO.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(StatefulSetDTO, dict):
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
        if not isinstance(other, StatefulSetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
