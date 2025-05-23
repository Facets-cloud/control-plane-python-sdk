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

class InputStreamResource(object):
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
        'file': 'File',
        'filename': 'str',
        'input_stream': 'InputStream',
        'open': 'bool',
        'readable': 'bool',
        'uri': 'URI',
        'url': 'URL'
    }

    attribute_map = {
        'description': 'description',
        'file': 'file',
        'filename': 'filename',
        'input_stream': 'inputStream',
        'open': 'open',
        'readable': 'readable',
        'uri': 'uri',
        'url': 'url'
    }

    def __init__(self, description=None, file=None, filename=None, input_stream=None, open=None, readable=None, uri=None, url=None):  # noqa: E501
        """InputStreamResource - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._file = None
        self._filename = None
        self._input_stream = None
        self._open = None
        self._readable = None
        self._uri = None
        self._url = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if file is not None:
            self.file = file
        if filename is not None:
            self.filename = filename
        if input_stream is not None:
            self.input_stream = input_stream
        if open is not None:
            self.open = open
        if readable is not None:
            self.readable = readable
        if uri is not None:
            self.uri = uri
        if url is not None:
            self.url = url

    @property
    def description(self):
        """Gets the description of this InputStreamResource.  # noqa: E501


        :return: The description of this InputStreamResource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InputStreamResource.


        :param description: The description of this InputStreamResource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def file(self):
        """Gets the file of this InputStreamResource.  # noqa: E501


        :return: The file of this InputStreamResource.  # noqa: E501
        :rtype: File
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this InputStreamResource.


        :param file: The file of this InputStreamResource.  # noqa: E501
        :type: File
        """

        self._file = file

    @property
    def filename(self):
        """Gets the filename of this InputStreamResource.  # noqa: E501


        :return: The filename of this InputStreamResource.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this InputStreamResource.


        :param filename: The filename of this InputStreamResource.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def input_stream(self):
        """Gets the input_stream of this InputStreamResource.  # noqa: E501


        :return: The input_stream of this InputStreamResource.  # noqa: E501
        :rtype: InputStream
        """
        return self._input_stream

    @input_stream.setter
    def input_stream(self, input_stream):
        """Sets the input_stream of this InputStreamResource.


        :param input_stream: The input_stream of this InputStreamResource.  # noqa: E501
        :type: InputStream
        """

        self._input_stream = input_stream

    @property
    def open(self):
        """Gets the open of this InputStreamResource.  # noqa: E501


        :return: The open of this InputStreamResource.  # noqa: E501
        :rtype: bool
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this InputStreamResource.


        :param open: The open of this InputStreamResource.  # noqa: E501
        :type: bool
        """

        self._open = open

    @property
    def readable(self):
        """Gets the readable of this InputStreamResource.  # noqa: E501


        :return: The readable of this InputStreamResource.  # noqa: E501
        :rtype: bool
        """
        return self._readable

    @readable.setter
    def readable(self, readable):
        """Sets the readable of this InputStreamResource.


        :param readable: The readable of this InputStreamResource.  # noqa: E501
        :type: bool
        """

        self._readable = readable

    @property
    def uri(self):
        """Gets the uri of this InputStreamResource.  # noqa: E501


        :return: The uri of this InputStreamResource.  # noqa: E501
        :rtype: URI
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this InputStreamResource.


        :param uri: The uri of this InputStreamResource.  # noqa: E501
        :type: URI
        """

        self._uri = uri

    @property
    def url(self):
        """Gets the url of this InputStreamResource.  # noqa: E501


        :return: The url of this InputStreamResource.  # noqa: E501
        :rtype: URL
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InputStreamResource.


        :param url: The url of this InputStreamResource.  # noqa: E501
        :type: URL
        """

        self._url = url

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
        if issubclass(InputStreamResource, dict):
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
        if not isinstance(other, InputStreamResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
