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


class TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation(object):
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
        'coord': 'list[float]',
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'coord': 'coord',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, coord=None, id=None, type=None, _configuration=None):  # noqa: E501
        """TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._coord = None
        self._id = None
        self._type = None
        self.discriminator = None

        if coord is not None:
            self.coord = coord
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def coord(self):
        """Gets the coord of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation.  # noqa: E501

        Contains exactly two values: the first value is the latitude, the second value is the longitude. Although multiple instructions may reference the same location, this coordinate is specific to this particular instruction.   # noqa: E501

        :return: The coord of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation.  # noqa: E501
        :rtype: list[float]
        """
        return self._coord

    @coord.setter
    def coord(self, coord):
        """Sets the coord of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation.

        Contains exactly two values: the first value is the latitude, the second value is the longitude. Although multiple instructions may reference the same location, this coordinate is specific to this particular instruction.   # noqa: E501

        :param coord: The coord of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation.  # noqa: E501
        :type: list[float]
        """

        self._coord = coord

    @property
    def id(self):
        """Gets the id of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation.  # noqa: E501

        This the unique ID for the stop in which this instruction occurs.  # noqa: E501

        :return: The id of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation.

        This the unique ID for the stop in which this instruction occurs.  # noqa: E501

        :param id: The id of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation.  # noqa: E501

        This is the type of location in which this instruction occurs.  # noqa: E501

        :return: The type of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation.

        This is the type of location in which this instruction occurs.  # noqa: E501

        :param type: The type of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation.  # noqa: E501
        :type: str
        """
        allowed_values = ["poi", "singlehouse", "stop", "platform", "street", "locality", "suburb", "unknown"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation, dict):
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
        if not isinstance(other, TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation):
            return True

        return self.to_dict() != other.to_dict()
