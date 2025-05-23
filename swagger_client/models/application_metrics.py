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

class ApplicationMetrics(object):
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
        'alerts': 'int',
        'application_id': 'str',
        'build_failures': 'int',
        'critical_code_smells': 'int',
        '_date': 'datetime',
        'errors': 'int',
        'fatal_errors_from_logs': 'int',
        'issues_reported': 'int',
        'outages': 'int',
        'regression_coverage': 'int',
        'regression_failures': 'int',
        'response_time': 'float',
        'sonar_url': 'str',
        'unit_test_coverage': 'int',
        'unit_tests': 'int'
    }

    attribute_map = {
        'alerts': 'alerts',
        'application_id': 'applicationId',
        'build_failures': 'buildFailures',
        'critical_code_smells': 'criticalCodeSmells',
        '_date': 'date',
        'errors': 'errors',
        'fatal_errors_from_logs': 'fatalErrorsFromLogs',
        'issues_reported': 'issuesReported',
        'outages': 'outages',
        'regression_coverage': 'regressionCoverage',
        'regression_failures': 'regressionFailures',
        'response_time': 'responseTime',
        'sonar_url': 'sonarUrl',
        'unit_test_coverage': 'unitTestCoverage',
        'unit_tests': 'unitTests'
    }

    def __init__(self, alerts=None, application_id=None, build_failures=None, critical_code_smells=None, _date=None, errors=None, fatal_errors_from_logs=None, issues_reported=None, outages=None, regression_coverage=None, regression_failures=None, response_time=None, sonar_url=None, unit_test_coverage=None, unit_tests=None):  # noqa: E501
        """ApplicationMetrics - a model defined in Swagger"""  # noqa: E501
        self._alerts = None
        self._application_id = None
        self._build_failures = None
        self._critical_code_smells = None
        self.__date = None
        self._errors = None
        self._fatal_errors_from_logs = None
        self._issues_reported = None
        self._outages = None
        self._regression_coverage = None
        self._regression_failures = None
        self._response_time = None
        self._sonar_url = None
        self._unit_test_coverage = None
        self._unit_tests = None
        self.discriminator = None
        if alerts is not None:
            self.alerts = alerts
        if application_id is not None:
            self.application_id = application_id
        if build_failures is not None:
            self.build_failures = build_failures
        if critical_code_smells is not None:
            self.critical_code_smells = critical_code_smells
        if _date is not None:
            self._date = _date
        if errors is not None:
            self.errors = errors
        if fatal_errors_from_logs is not None:
            self.fatal_errors_from_logs = fatal_errors_from_logs
        if issues_reported is not None:
            self.issues_reported = issues_reported
        if outages is not None:
            self.outages = outages
        if regression_coverage is not None:
            self.regression_coverage = regression_coverage
        if regression_failures is not None:
            self.regression_failures = regression_failures
        if response_time is not None:
            self.response_time = response_time
        if sonar_url is not None:
            self.sonar_url = sonar_url
        if unit_test_coverage is not None:
            self.unit_test_coverage = unit_test_coverage
        if unit_tests is not None:
            self.unit_tests = unit_tests

    @property
    def alerts(self):
        """Gets the alerts of this ApplicationMetrics.  # noqa: E501


        :return: The alerts of this ApplicationMetrics.  # noqa: E501
        :rtype: int
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this ApplicationMetrics.


        :param alerts: The alerts of this ApplicationMetrics.  # noqa: E501
        :type: int
        """

        self._alerts = alerts

    @property
    def application_id(self):
        """Gets the application_id of this ApplicationMetrics.  # noqa: E501


        :return: The application_id of this ApplicationMetrics.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApplicationMetrics.


        :param application_id: The application_id of this ApplicationMetrics.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def build_failures(self):
        """Gets the build_failures of this ApplicationMetrics.  # noqa: E501


        :return: The build_failures of this ApplicationMetrics.  # noqa: E501
        :rtype: int
        """
        return self._build_failures

    @build_failures.setter
    def build_failures(self, build_failures):
        """Sets the build_failures of this ApplicationMetrics.


        :param build_failures: The build_failures of this ApplicationMetrics.  # noqa: E501
        :type: int
        """

        self._build_failures = build_failures

    @property
    def critical_code_smells(self):
        """Gets the critical_code_smells of this ApplicationMetrics.  # noqa: E501


        :return: The critical_code_smells of this ApplicationMetrics.  # noqa: E501
        :rtype: int
        """
        return self._critical_code_smells

    @critical_code_smells.setter
    def critical_code_smells(self, critical_code_smells):
        """Sets the critical_code_smells of this ApplicationMetrics.


        :param critical_code_smells: The critical_code_smells of this ApplicationMetrics.  # noqa: E501
        :type: int
        """

        self._critical_code_smells = critical_code_smells

    @property
    def _date(self):
        """Gets the _date of this ApplicationMetrics.  # noqa: E501


        :return: The _date of this ApplicationMetrics.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ApplicationMetrics.


        :param _date: The _date of this ApplicationMetrics.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def errors(self):
        """Gets the errors of this ApplicationMetrics.  # noqa: E501


        :return: The errors of this ApplicationMetrics.  # noqa: E501
        :rtype: int
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ApplicationMetrics.


        :param errors: The errors of this ApplicationMetrics.  # noqa: E501
        :type: int
        """

        self._errors = errors

    @property
    def fatal_errors_from_logs(self):
        """Gets the fatal_errors_from_logs of this ApplicationMetrics.  # noqa: E501


        :return: The fatal_errors_from_logs of this ApplicationMetrics.  # noqa: E501
        :rtype: int
        """
        return self._fatal_errors_from_logs

    @fatal_errors_from_logs.setter
    def fatal_errors_from_logs(self, fatal_errors_from_logs):
        """Sets the fatal_errors_from_logs of this ApplicationMetrics.


        :param fatal_errors_from_logs: The fatal_errors_from_logs of this ApplicationMetrics.  # noqa: E501
        :type: int
        """

        self._fatal_errors_from_logs = fatal_errors_from_logs

    @property
    def issues_reported(self):
        """Gets the issues_reported of this ApplicationMetrics.  # noqa: E501


        :return: The issues_reported of this ApplicationMetrics.  # noqa: E501
        :rtype: int
        """
        return self._issues_reported

    @issues_reported.setter
    def issues_reported(self, issues_reported):
        """Sets the issues_reported of this ApplicationMetrics.


        :param issues_reported: The issues_reported of this ApplicationMetrics.  # noqa: E501
        :type: int
        """

        self._issues_reported = issues_reported

    @property
    def outages(self):
        """Gets the outages of this ApplicationMetrics.  # noqa: E501


        :return: The outages of this ApplicationMetrics.  # noqa: E501
        :rtype: int
        """
        return self._outages

    @outages.setter
    def outages(self, outages):
        """Sets the outages of this ApplicationMetrics.


        :param outages: The outages of this ApplicationMetrics.  # noqa: E501
        :type: int
        """

        self._outages = outages

    @property
    def regression_coverage(self):
        """Gets the regression_coverage of this ApplicationMetrics.  # noqa: E501


        :return: The regression_coverage of this ApplicationMetrics.  # noqa: E501
        :rtype: int
        """
        return self._regression_coverage

    @regression_coverage.setter
    def regression_coverage(self, regression_coverage):
        """Sets the regression_coverage of this ApplicationMetrics.


        :param regression_coverage: The regression_coverage of this ApplicationMetrics.  # noqa: E501
        :type: int
        """

        self._regression_coverage = regression_coverage

    @property
    def regression_failures(self):
        """Gets the regression_failures of this ApplicationMetrics.  # noqa: E501


        :return: The regression_failures of this ApplicationMetrics.  # noqa: E501
        :rtype: int
        """
        return self._regression_failures

    @regression_failures.setter
    def regression_failures(self, regression_failures):
        """Sets the regression_failures of this ApplicationMetrics.


        :param regression_failures: The regression_failures of this ApplicationMetrics.  # noqa: E501
        :type: int
        """

        self._regression_failures = regression_failures

    @property
    def response_time(self):
        """Gets the response_time of this ApplicationMetrics.  # noqa: E501


        :return: The response_time of this ApplicationMetrics.  # noqa: E501
        :rtype: float
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        """Sets the response_time of this ApplicationMetrics.


        :param response_time: The response_time of this ApplicationMetrics.  # noqa: E501
        :type: float
        """

        self._response_time = response_time

    @property
    def sonar_url(self):
        """Gets the sonar_url of this ApplicationMetrics.  # noqa: E501


        :return: The sonar_url of this ApplicationMetrics.  # noqa: E501
        :rtype: str
        """
        return self._sonar_url

    @sonar_url.setter
    def sonar_url(self, sonar_url):
        """Sets the sonar_url of this ApplicationMetrics.


        :param sonar_url: The sonar_url of this ApplicationMetrics.  # noqa: E501
        :type: str
        """

        self._sonar_url = sonar_url

    @property
    def unit_test_coverage(self):
        """Gets the unit_test_coverage of this ApplicationMetrics.  # noqa: E501


        :return: The unit_test_coverage of this ApplicationMetrics.  # noqa: E501
        :rtype: int
        """
        return self._unit_test_coverage

    @unit_test_coverage.setter
    def unit_test_coverage(self, unit_test_coverage):
        """Sets the unit_test_coverage of this ApplicationMetrics.


        :param unit_test_coverage: The unit_test_coverage of this ApplicationMetrics.  # noqa: E501
        :type: int
        """

        self._unit_test_coverage = unit_test_coverage

    @property
    def unit_tests(self):
        """Gets the unit_tests of this ApplicationMetrics.  # noqa: E501


        :return: The unit_tests of this ApplicationMetrics.  # noqa: E501
        :rtype: int
        """
        return self._unit_tests

    @unit_tests.setter
    def unit_tests(self, unit_tests):
        """Sets the unit_tests of this ApplicationMetrics.


        :param unit_tests: The unit_tests of this ApplicationMetrics.  # noqa: E501
        :type: int
        """

        self._unit_tests = unit_tests

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
        if issubclass(ApplicationMetrics, dict):
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
        if not isinstance(other, ApplicationMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
