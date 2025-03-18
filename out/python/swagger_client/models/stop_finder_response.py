# coding: utf-8

"""
    Trip Planner

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 10.2.1.42
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class StopFinderResponse(object):
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
        'error': 'ApiErrorResponse',
        'locations': 'list[StopFinderLocation]',
        'version': 'str'
    }

    attribute_map = {
        'error': 'error',
        'locations': 'locations',
        'version': 'version'
    }

    def __init__(self, error=None, locations=None, version=None, _configuration=None):  # noqa: E501
        """StopFinderResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error = None
        self._locations = None
        self._version = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if locations is not None:
            self.locations = locations
        if version is not None:
            self.version = version

    @property
    def error(self):
        """Gets the error of this StopFinderResponse.  # noqa: E501

        If an error has occurred, this element contains information about the error.   # noqa: E501

        :return: The error of this StopFinderResponse.  # noqa: E501
        :rtype: ApiErrorResponse
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this StopFinderResponse.

        If an error has occurred, this element contains information about the error.   # noqa: E501

        :param error: The error of this StopFinderResponse.  # noqa: E501
        :type: ApiErrorResponse
        """

        self._error = error

    @property
    def locations(self):
        """Gets the locations of this StopFinderResponse.  # noqa: E501

        An array of all locations that were found using the specified search input. To display the results in a way that makes sense to the end user, you can sort this list by `matchQuality`. Alternatively, you can group the results by their type and/or sort them alphabetically.   # noqa: E501

        :return: The locations of this StopFinderResponse.  # noqa: E501
        :rtype: list[StopFinderLocation]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this StopFinderResponse.

        An array of all locations that were found using the specified search input. To display the results in a way that makes sense to the end user, you can sort this list by `matchQuality`. Alternatively, you can group the results by their type and/or sort them alphabetically.   # noqa: E501

        :param locations: The locations of this StopFinderResponse.  # noqa: E501
        :type: list[StopFinderLocation]
        """

        self._locations = locations

    @property
    def version(self):
        """Gets the version of this StopFinderResponse.  # noqa: E501

        The version of the API that provided the response. Note that if this value is different to above, then the returned data may be different than expected. You can set the expected version using the `version` request parameter.   # noqa: E501

        :return: The version of this StopFinderResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this StopFinderResponse.

        The version of the API that provided the response. Note that if this value is different to above, then the returned data may be different than expected. You can set the expected version using the `version` request parameter.   # noqa: E501

        :param version: The version of this StopFinderResponse.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(StopFinderResponse, dict):
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
        if not isinstance(other, StopFinderResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StopFinderResponse):
            return True

        return self.to_dict() != other.to_dict()
