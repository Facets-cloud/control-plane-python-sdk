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

class ClusterSchedule(object):
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
        'by_day': 'list[str]',
        'by_time': 'LocalTime',
        'cluster_id': 'str',
        'created_by': 'str',
        'creation_date': 'datetime',
        'description': 'str',
        'frequency': 'str',
        'id': 'str',
        'interval': 'int',
        'is_paused': 'bool',
        'last_modified_by': 'str',
        'last_modified_date': 'datetime',
        'release_type': 'str',
        'server_time_zone': 'str',
        'time_zone': 'TimeZone'
    }

    attribute_map = {
        'by_day': 'byDay',
        'by_time': 'byTime',
        'cluster_id': 'clusterId',
        'created_by': 'createdBy',
        'creation_date': 'creationDate',
        'description': 'description',
        'frequency': 'frequency',
        'id': 'id',
        'interval': 'interval',
        'is_paused': 'isPaused',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_date': 'lastModifiedDate',
        'release_type': 'releaseType',
        'server_time_zone': 'serverTimeZone',
        'time_zone': 'timeZone'
    }

    def __init__(self, by_day=None, by_time=None, cluster_id=None, created_by=None, creation_date=None, description=None, frequency=None, id=None, interval=None, is_paused=None, last_modified_by=None, last_modified_date=None, release_type=None, server_time_zone=None, time_zone=None):  # noqa: E501
        """ClusterSchedule - a model defined in Swagger"""  # noqa: E501
        self._by_day = None
        self._by_time = None
        self._cluster_id = None
        self._created_by = None
        self._creation_date = None
        self._description = None
        self._frequency = None
        self._id = None
        self._interval = None
        self._is_paused = None
        self._last_modified_by = None
        self._last_modified_date = None
        self._release_type = None
        self._server_time_zone = None
        self._time_zone = None
        self.discriminator = None
        if by_day is not None:
            self.by_day = by_day
        if by_time is not None:
            self.by_time = by_time
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if created_by is not None:
            self.created_by = created_by
        if creation_date is not None:
            self.creation_date = creation_date
        if description is not None:
            self.description = description
        if frequency is not None:
            self.frequency = frequency
        if id is not None:
            self.id = id
        if interval is not None:
            self.interval = interval
        if is_paused is not None:
            self.is_paused = is_paused
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if release_type is not None:
            self.release_type = release_type
        if server_time_zone is not None:
            self.server_time_zone = server_time_zone
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def by_day(self):
        """Gets the by_day of this ClusterSchedule.  # noqa: E501


        :return: The by_day of this ClusterSchedule.  # noqa: E501
        :rtype: list[str]
        """
        return self._by_day

    @by_day.setter
    def by_day(self, by_day):
        """Sets the by_day of this ClusterSchedule.


        :param by_day: The by_day of this ClusterSchedule.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]  # noqa: E501
        if not set(by_day).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `by_day` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(by_day) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._by_day = by_day

    @property
    def by_time(self):
        """Gets the by_time of this ClusterSchedule.  # noqa: E501


        :return: The by_time of this ClusterSchedule.  # noqa: E501
        :rtype: LocalTime
        """
        return self._by_time

    @by_time.setter
    def by_time(self, by_time):
        """Sets the by_time of this ClusterSchedule.


        :param by_time: The by_time of this ClusterSchedule.  # noqa: E501
        :type: LocalTime
        """

        self._by_time = by_time

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ClusterSchedule.  # noqa: E501


        :return: The cluster_id of this ClusterSchedule.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ClusterSchedule.


        :param cluster_id: The cluster_id of this ClusterSchedule.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def created_by(self):
        """Gets the created_by of this ClusterSchedule.  # noqa: E501


        :return: The created_by of this ClusterSchedule.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ClusterSchedule.


        :param created_by: The created_by of this ClusterSchedule.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def creation_date(self):
        """Gets the creation_date of this ClusterSchedule.  # noqa: E501


        :return: The creation_date of this ClusterSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ClusterSchedule.


        :param creation_date: The creation_date of this ClusterSchedule.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def description(self):
        """Gets the description of this ClusterSchedule.  # noqa: E501


        :return: The description of this ClusterSchedule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClusterSchedule.


        :param description: The description of this ClusterSchedule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def frequency(self):
        """Gets the frequency of this ClusterSchedule.  # noqa: E501


        :return: The frequency of this ClusterSchedule.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this ClusterSchedule.


        :param frequency: The frequency of this ClusterSchedule.  # noqa: E501
        :type: str
        """
        allowed_values = ["PER_MINUTE", "HOURLY", "DAILY", "WEEKLY"]  # noqa: E501
        if frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(frequency, allowed_values)
            )

        self._frequency = frequency

    @property
    def id(self):
        """Gets the id of this ClusterSchedule.  # noqa: E501


        :return: The id of this ClusterSchedule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterSchedule.


        :param id: The id of this ClusterSchedule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def interval(self):
        """Gets the interval of this ClusterSchedule.  # noqa: E501


        :return: The interval of this ClusterSchedule.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ClusterSchedule.


        :param interval: The interval of this ClusterSchedule.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def is_paused(self):
        """Gets the is_paused of this ClusterSchedule.  # noqa: E501


        :return: The is_paused of this ClusterSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._is_paused

    @is_paused.setter
    def is_paused(self, is_paused):
        """Sets the is_paused of this ClusterSchedule.


        :param is_paused: The is_paused of this ClusterSchedule.  # noqa: E501
        :type: bool
        """

        self._is_paused = is_paused

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this ClusterSchedule.  # noqa: E501


        :return: The last_modified_by of this ClusterSchedule.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this ClusterSchedule.


        :param last_modified_by: The last_modified_by of this ClusterSchedule.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this ClusterSchedule.  # noqa: E501


        :return: The last_modified_date of this ClusterSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this ClusterSchedule.


        :param last_modified_date: The last_modified_date of this ClusterSchedule.  # noqa: E501
        :type: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def release_type(self):
        """Gets the release_type of this ClusterSchedule.  # noqa: E501


        :return: The release_type of this ClusterSchedule.  # noqa: E501
        :rtype: str
        """
        return self._release_type

    @release_type.setter
    def release_type(self, release_type):
        """Sets the release_type of this ClusterSchedule.


        :param release_type: The release_type of this ClusterSchedule.  # noqa: E501
        :type: str
        """
        allowed_values = ["HOTFIX", "RELEASE", "LAUNCH", "DESTROY", "CUSTOM", "UNLOCK_STATE", "PLAN", "HOTFIX_PLAN", "APPLY_PLAN", "APPLY_HOTFIX_PLAN", "SCALE_UP", "SCALE_DOWN", "MAINTENANCE", "TERRAFORM_EXPORT", "ROLLBACK_PLAN", "APPLY_ROLLBACK_PLAN"]  # noqa: E501
        if release_type not in allowed_values:
            raise ValueError(
                "Invalid value for `release_type` ({0}), must be one of {1}"  # noqa: E501
                .format(release_type, allowed_values)
            )

        self._release_type = release_type

    @property
    def server_time_zone(self):
        """Gets the server_time_zone of this ClusterSchedule.  # noqa: E501


        :return: The server_time_zone of this ClusterSchedule.  # noqa: E501
        :rtype: str
        """
        return self._server_time_zone

    @server_time_zone.setter
    def server_time_zone(self, server_time_zone):
        """Sets the server_time_zone of this ClusterSchedule.


        :param server_time_zone: The server_time_zone of this ClusterSchedule.  # noqa: E501
        :type: str
        """

        self._server_time_zone = server_time_zone

    @property
    def time_zone(self):
        """Gets the time_zone of this ClusterSchedule.  # noqa: E501


        :return: The time_zone of this ClusterSchedule.  # noqa: E501
        :rtype: TimeZone
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ClusterSchedule.


        :param time_zone: The time_zone of this ClusterSchedule.  # noqa: E501
        :type: TimeZone
        """

        self._time_zone = time_zone

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
        if issubclass(ClusterSchedule, dict):
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
        if not isinstance(other, ClusterSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
