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

class TemplateGitDetails(object):
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
        'git_url': 'str',
        'git_ref': 'str',
        'path': 'str',
        'account_id': 'str'
    }

    attribute_map = {
        'git_url': 'gitUrl',
        'git_ref': 'gitRef',
        'path': 'path',
        'account_id': 'accountId'
    }

    def __init__(self, git_url=None, git_ref=None, path=None, account_id=None):  # noqa: E501
        """TemplateGitDetails - a model defined in Swagger"""  # noqa: E501
        self._git_url = None
        self._git_ref = None
        self._path = None
        self._account_id = None
        self.discriminator = None
        self.git_url = git_url
        self.git_ref = git_ref
        self.path = path
        self.account_id = account_id

    @property
    def git_url(self):
        """Gets the git_url of this TemplateGitDetails.  # noqa: E501

        Git repository URL  # noqa: E501

        :return: The git_url of this TemplateGitDetails.  # noqa: E501
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        """Sets the git_url of this TemplateGitDetails.

        Git repository URL  # noqa: E501

        :param git_url: The git_url of this TemplateGitDetails.  # noqa: E501
        :type: str
        """
        if git_url is None:
            raise ValueError("Invalid value for `git_url`, must not be `None`")  # noqa: E501

        self._git_url = git_url

    @property
    def git_ref(self):
        """Gets the git_ref of this TemplateGitDetails.  # noqa: E501

        Git reference (branch or tag)  # noqa: E501

        :return: The git_ref of this TemplateGitDetails.  # noqa: E501
        :rtype: str
        """
        return self._git_ref

    @git_ref.setter
    def git_ref(self, git_ref):
        """Sets the git_ref of this TemplateGitDetails.

        Git reference (branch or tag)  # noqa: E501

        :param git_ref: The git_ref of this TemplateGitDetails.  # noqa: E501
        :type: str
        """
        if git_ref is None:
            raise ValueError("Invalid value for `git_ref`, must not be `None`")  # noqa: E501

        self._git_ref = git_ref

    @property
    def path(self):
        """Gets the path of this TemplateGitDetails.  # noqa: E501

        Path within the Git repository  # noqa: E501

        :return: The path of this TemplateGitDetails.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this TemplateGitDetails.

        Path within the Git repository  # noqa: E501

        :param path: The path of this TemplateGitDetails.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def account_id(self):
        """Gets the account_id of this TemplateGitDetails.  # noqa: E501

        Account ID associated with the Git repository  # noqa: E501

        :return: The account_id of this TemplateGitDetails.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this TemplateGitDetails.

        Account ID associated with the Git repository  # noqa: E501

        :param account_id: The account_id of this TemplateGitDetails.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

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
        if issubclass(TemplateGitDetails, dict):
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
        if not isinstance(other, TemplateGitDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
