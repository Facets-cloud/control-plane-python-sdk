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

class ActionExecution(object):
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
        'action': 'ApplicationAction',
        'application_id': 'str',
        'id': 'str',
        'output': 'str',
        'trigger_exception': 'str',
        'trigger_status': 'str',
        'trigger_time': 'int'
    }

    attribute_map = {
        'action': 'action',
        'application_id': 'applicationId',
        'id': 'id',
        'output': 'output',
        'trigger_exception': 'triggerException',
        'trigger_status': 'triggerStatus',
        'trigger_time': 'triggerTime'
    }

    def __init__(self, action=None, application_id=None, id=None, output=None, trigger_exception=None, trigger_status=None, trigger_time=None):  # noqa: E501
        """ActionExecution - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._application_id = None
        self._id = None
        self._output = None
        self._trigger_exception = None
        self._trigger_status = None
        self._trigger_time = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if application_id is not None:
            self.application_id = application_id
        if id is not None:
            self.id = id
        if output is not None:
            self.output = output
        if trigger_exception is not None:
            self.trigger_exception = trigger_exception
        if trigger_status is not None:
            self.trigger_status = trigger_status
        if trigger_time is not None:
            self.trigger_time = trigger_time

    @property
    def action(self):
        """Gets the action of this ActionExecution.  # noqa: E501


        :return: The action of this ActionExecution.  # noqa: E501
        :rtype: ApplicationAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ActionExecution.


        :param action: The action of this ActionExecution.  # noqa: E501
        :type: ApplicationAction
        """

        self._action = action

    @property
    def application_id(self):
        """Gets the application_id of this ActionExecution.  # noqa: E501


        :return: The application_id of this ActionExecution.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ActionExecution.


        :param application_id: The application_id of this ActionExecution.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def id(self):
        """Gets the id of this ActionExecution.  # noqa: E501


        :return: The id of this ActionExecution.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ActionExecution.


        :param id: The id of this ActionExecution.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def output(self):
        """Gets the output of this ActionExecution.  # noqa: E501


        :return: The output of this ActionExecution.  # noqa: E501
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this ActionExecution.


        :param output: The output of this ActionExecution.  # noqa: E501
        :type: str
        """

        self._output = output

    @property
    def trigger_exception(self):
        """Gets the trigger_exception of this ActionExecution.  # noqa: E501


        :return: The trigger_exception of this ActionExecution.  # noqa: E501
        :rtype: str
        """
        return self._trigger_exception

    @trigger_exception.setter
    def trigger_exception(self, trigger_exception):
        """Sets the trigger_exception of this ActionExecution.


        :param trigger_exception: The trigger_exception of this ActionExecution.  # noqa: E501
        :type: str
        """

        self._trigger_exception = trigger_exception

    @property
    def trigger_status(self):
        """Gets the trigger_status of this ActionExecution.  # noqa: E501


        :return: The trigger_status of this ActionExecution.  # noqa: E501
        :rtype: str
        """
        return self._trigger_status

    @trigger_status.setter
    def trigger_status(self, trigger_status):
        """Sets the trigger_status of this ActionExecution.


        :param trigger_status: The trigger_status of this ActionExecution.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILURE"]  # noqa: E501
        if trigger_status not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger_status` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger_status, allowed_values)
            )

        self._trigger_status = trigger_status

    @property
    def trigger_time(self):
        """Gets the trigger_time of this ActionExecution.  # noqa: E501


        :return: The trigger_time of this ActionExecution.  # noqa: E501
        :rtype: int
        """
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self, trigger_time):
        """Sets the trigger_time of this ActionExecution.


        :param trigger_time: The trigger_time of this ActionExecution.  # noqa: E501
        :type: int
        """

        self._trigger_time = trigger_time

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
        if issubclass(ActionExecution, dict):
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
        if not isinstance(other, ActionExecution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
