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


class AdditionalInfoResponse(object):
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
        'infos': 'AdditionalInfoResponseInfos',
        'timestamp': 'str',
        'version': 'str'
    }

    attribute_map = {
        'error': 'error',
        'infos': 'infos',
        'timestamp': 'timestamp',
        'version': 'version'
    }

    def __init__(self, error=None, infos=None, timestamp=None, version=None, _configuration=None):  # noqa: E501
        """AdditionalInfoResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error = None
        self._infos = None
        self._timestamp = None
        self._version = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if infos is not None:
            self.infos = infos
        if timestamp is not None:
            self.timestamp = timestamp
        if version is not None:
            self.version = version

    @property
    def error(self):
        """Gets the error of this AdditionalInfoResponse.  # noqa: E501

        If an error has occurred, this element contains information about the error.   # noqa: E501

        :return: The error of this AdditionalInfoResponse.  # noqa: E501
        :rtype: ApiErrorResponse
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this AdditionalInfoResponse.

        If an error has occurred, this element contains information about the error.   # noqa: E501

        :param error: The error of this AdditionalInfoResponse.  # noqa: E501
        :type: ApiErrorResponse
        """

        self._error = error

    @property
    def infos(self):
        """Gets the infos of this AdditionalInfoResponse.  # noqa: E501


        :return: The infos of this AdditionalInfoResponse.  # noqa: E501
        :rtype: AdditionalInfoResponseInfos
        """
        return self._infos

    @infos.setter
    def infos(self, infos):
        """Sets the infos of this AdditionalInfoResponse.


        :param infos: The infos of this AdditionalInfoResponse.  # noqa: E501
        :type: AdditionalInfoResponseInfos
        """

        self._infos = infos

    @property
    def timestamp(self):
        """Gets the timestamp of this AdditionalInfoResponse.  # noqa: E501

        A timestamp in `YYYY-MM-DDTHH:MM:SSZ` format  # noqa: E501

        :return: The timestamp of this AdditionalInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this AdditionalInfoResponse.

        A timestamp in `YYYY-MM-DDTHH:MM:SSZ` format  # noqa: E501

        :param timestamp: The timestamp of this AdditionalInfoResponse.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def version(self):
        """Gets the version of this AdditionalInfoResponse.  # noqa: E501

        The version of the API that provided the response. Note that if this value is different to above, then the returned data may be different than expected. You can set the expected version using the `version` request parameter.   # noqa: E501

        :return: The version of this AdditionalInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AdditionalInfoResponse.

        The version of the API that provided the response. Note that if this value is different to above, then the returned data may be different than expected. You can set the expected version using the `version` request parameter.   # noqa: E501

        :param version: The version of this AdditionalInfoResponse.  # noqa: E501
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
        if issubclass(AdditionalInfoResponse, dict):
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
        if not isinstance(other, AdditionalInfoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdditionalInfoResponse):
            return True

        return self.to_dict() != other.to_dict()
