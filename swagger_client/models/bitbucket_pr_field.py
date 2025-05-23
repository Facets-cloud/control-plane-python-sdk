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

class BitbucketPRField(object):
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
        'description': 'str',
        'destination': 'BitbucketPRBranchRef',
        'id': 'int',
        'links': 'BitbucketPRLinks',
        'source': 'BitbucketPRBranchRef',
        'state': 'str',
        'type': 'str',
        'updated_on': 'str'
    }

    attribute_map = {
        'description': 'description',
        'destination': 'destination',
        'id': 'id',
        'links': 'links',
        'source': 'source',
        'state': 'state',
        'type': 'type',
        'updated_on': 'updated_on'
    }

    def __init__(self, description=None, destination=None, id=None, links=None, source=None, state=None, type=None, updated_on=None):  # noqa: E501
        """BitbucketPRField - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._destination = None
        self._id = None
        self._links = None
        self._source = None
        self._state = None
        self._type = None
        self._updated_on = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if destination is not None:
            self.destination = destination
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if source is not None:
            self.source = source
        if state is not None:
            self.state = state
        if type is not None:
            self.type = type
        if updated_on is not None:
            self.updated_on = updated_on

    @property
    def description(self):
        """Gets the description of this BitbucketPRField.  # noqa: E501


        :return: The description of this BitbucketPRField.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BitbucketPRField.


        :param description: The description of this BitbucketPRField.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def destination(self):
        """Gets the destination of this BitbucketPRField.  # noqa: E501


        :return: The destination of this BitbucketPRField.  # noqa: E501
        :rtype: BitbucketPRBranchRef
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this BitbucketPRField.


        :param destination: The destination of this BitbucketPRField.  # noqa: E501
        :type: BitbucketPRBranchRef
        """

        self._destination = destination

    @property
    def id(self):
        """Gets the id of this BitbucketPRField.  # noqa: E501


        :return: The id of this BitbucketPRField.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BitbucketPRField.


        :param id: The id of this BitbucketPRField.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this BitbucketPRField.  # noqa: E501


        :return: The links of this BitbucketPRField.  # noqa: E501
        :rtype: BitbucketPRLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this BitbucketPRField.


        :param links: The links of this BitbucketPRField.  # noqa: E501
        :type: BitbucketPRLinks
        """

        self._links = links

    @property
    def source(self):
        """Gets the source of this BitbucketPRField.  # noqa: E501


        :return: The source of this BitbucketPRField.  # noqa: E501
        :rtype: BitbucketPRBranchRef
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this BitbucketPRField.


        :param source: The source of this BitbucketPRField.  # noqa: E501
        :type: BitbucketPRBranchRef
        """

        self._source = source

    @property
    def state(self):
        """Gets the state of this BitbucketPRField.  # noqa: E501


        :return: The state of this BitbucketPRField.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BitbucketPRField.


        :param state: The state of this BitbucketPRField.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def type(self):
        """Gets the type of this BitbucketPRField.  # noqa: E501


        :return: The type of this BitbucketPRField.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BitbucketPRField.


        :param type: The type of this BitbucketPRField.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def updated_on(self):
        """Gets the updated_on of this BitbucketPRField.  # noqa: E501


        :return: The updated_on of this BitbucketPRField.  # noqa: E501
        :rtype: str
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this BitbucketPRField.


        :param updated_on: The updated_on of this BitbucketPRField.  # noqa: E501
        :type: str
        """

        self._updated_on = updated_on

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
        if issubclass(BitbucketPRField, dict):
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
        if not isinstance(other, BitbucketPRField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
