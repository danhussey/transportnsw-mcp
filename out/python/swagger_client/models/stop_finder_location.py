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


class StopFinderLocation(object):
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
        'assigned_stops': 'list[StopFinderAssignedStop]',
        'building_number': 'str',
        'coord': 'list[float]',
        'disassembled_name': 'str',
        'id': 'str',
        'is_best': 'bool',
        'is_global_id': 'bool',
        'match_quality': 'int',
        'modes': 'list[int]',
        'name': 'str',
        'parent': 'ParentLocation',
        'street_name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'assigned_stops': 'assignedStops',
        'building_number': 'buildingNumber',
        'coord': 'coord',
        'disassembled_name': 'disassembledName',
        'id': 'id',
        'is_best': 'isBest',
        'is_global_id': 'isGlobalId',
        'match_quality': 'matchQuality',
        'modes': 'modes',
        'name': 'name',
        'parent': 'parent',
        'street_name': 'streetName',
        'type': 'type'
    }

    def __init__(self, assigned_stops=None, building_number=None, coord=None, disassembled_name=None, id=None, is_best=None, is_global_id=None, match_quality=None, modes=None, name=None, parent=None, street_name=None, type=None, _configuration=None):  # noqa: E501
        """StopFinderLocation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assigned_stops = None
        self._building_number = None
        self._coord = None
        self._disassembled_name = None
        self._id = None
        self._is_best = None
        self._is_global_id = None
        self._match_quality = None
        self._modes = None
        self._name = None
        self._parent = None
        self._street_name = None
        self._type = None
        self.discriminator = None

        if assigned_stops is not None:
            self.assigned_stops = assigned_stops
        if building_number is not None:
            self.building_number = building_number
        if coord is not None:
            self.coord = coord
        if disassembled_name is not None:
            self.disassembled_name = disassembled_name
        if id is not None:
            self.id = id
        if is_best is not None:
            self.is_best = is_best
        if is_global_id is not None:
            self.is_global_id = is_global_id
        if match_quality is not None:
            self.match_quality = match_quality
        if modes is not None:
            self.modes = modes
        if name is not None:
            self.name = name
        if parent is not None:
            self.parent = parent
        if street_name is not None:
            self.street_name = street_name
        if type is not None:
            self.type = type

    @property
    def assigned_stops(self):
        """Gets the assigned_stops of this StopFinderLocation.  # noqa: E501

        This is a list of stops that are assigned to this location. This means if you're in the current location and want to catch public transport, these assigned stops are directly available to you.   # noqa: E501

        :return: The assigned_stops of this StopFinderLocation.  # noqa: E501
        :rtype: list[StopFinderAssignedStop]
        """
        return self._assigned_stops

    @assigned_stops.setter
    def assigned_stops(self, assigned_stops):
        """Sets the assigned_stops of this StopFinderLocation.

        This is a list of stops that are assigned to this location. This means if you're in the current location and want to catch public transport, these assigned stops are directly available to you.   # noqa: E501

        :param assigned_stops: The assigned_stops of this StopFinderLocation.  # noqa: E501
        :type: list[StopFinderAssignedStop]
        """

        self._assigned_stops = assigned_stops

    @property
    def building_number(self):
        """Gets the building_number of this StopFinderLocation.  # noqa: E501

        This is the number of the property, included only if the `type` value is set to `singlehouse`. Note that it is a string, as it may include non-numeric characters.   # noqa: E501

        :return: The building_number of this StopFinderLocation.  # noqa: E501
        :rtype: str
        """
        return self._building_number

    @building_number.setter
    def building_number(self, building_number):
        """Sets the building_number of this StopFinderLocation.

        This is the number of the property, included only if the `type` value is set to `singlehouse`. Note that it is a string, as it may include non-numeric characters.   # noqa: E501

        :param building_number: The building_number of this StopFinderLocation.  # noqa: E501
        :type: str
        """

        self._building_number = building_number

    @property
    def coord(self):
        """Gets the coord of this StopFinderLocation.  # noqa: E501

        Contains exactly two values: the first value is the latitude, the second value is the longitude.   # noqa: E501

        :return: The coord of this StopFinderLocation.  # noqa: E501
        :rtype: list[float]
        """
        return self._coord

    @coord.setter
    def coord(self, coord):
        """Sets the coord of this StopFinderLocation.

        Contains exactly two values: the first value is the latitude, the second value is the longitude.   # noqa: E501

        :param coord: The coord of this StopFinderLocation.  # noqa: E501
        :type: list[float]
        """

        self._coord = coord

    @property
    def disassembled_name(self):
        """Gets the disassembled_name of this StopFinderLocation.  # noqa: E501

        This is the short version of the location name, which does not include the suburb or other information.   # noqa: E501

        :return: The disassembled_name of this StopFinderLocation.  # noqa: E501
        :rtype: str
        """
        return self._disassembled_name

    @disassembled_name.setter
    def disassembled_name(self, disassembled_name):
        """Sets the disassembled_name of this StopFinderLocation.

        This is the short version of the location name, which does not include the suburb or other information.   # noqa: E501

        :param disassembled_name: The disassembled_name of this StopFinderLocation.  # noqa: E501
        :type: str
        """

        self._disassembled_name = disassembled_name

    @property
    def id(self):
        """Gets the id of this StopFinderLocation.  # noqa: E501

        This is a unique ID for the returned location. Certain types of ID can be used for subsequent searches performed with `stop_finder`, or can be used as the origin or destination in an `trip` request. The format of a location ID differs greatly, depending on the type of location it is.   # noqa: E501

        :return: The id of this StopFinderLocation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StopFinderLocation.

        This is a unique ID for the returned location. Certain types of ID can be used for subsequent searches performed with `stop_finder`, or can be used as the origin or destination in an `trip` request. The format of a location ID differs greatly, depending on the type of location it is.   # noqa: E501

        :param id: The id of this StopFinderLocation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_best(self):
        """Gets the is_best of this StopFinderLocation.  # noqa: E501

        Indicates whether or not this is the best match out of all the returned locations.  # noqa: E501

        :return: The is_best of this StopFinderLocation.  # noqa: E501
        :rtype: bool
        """
        return self._is_best

    @is_best.setter
    def is_best(self, is_best):
        """Sets the is_best of this StopFinderLocation.

        Indicates whether or not this is the best match out of all the returned locations.  # noqa: E501

        :param is_best: The is_best of this StopFinderLocation.  # noqa: E501
        :type: bool
        """

        self._is_best = is_best

    @property
    def is_global_id(self):
        """Gets the is_global_id of this StopFinderLocation.  # noqa: E501

        This determines whether the id property is a global stop id or not   # noqa: E501

        :return: The is_global_id of this StopFinderLocation.  # noqa: E501
        :rtype: bool
        """
        return self._is_global_id

    @is_global_id.setter
    def is_global_id(self, is_global_id):
        """Sets the is_global_id of this StopFinderLocation.

        This determines whether the id property is a global stop id or not   # noqa: E501

        :param is_global_id: The is_global_id of this StopFinderLocation.  # noqa: E501
        :type: bool
        """

        self._is_global_id = is_global_id

    @property
    def match_quality(self):
        """Gets the match_quality of this StopFinderLocation.  # noqa: E501

        This value indicates how well the returned stop matches the search query. A higher number indicates a better match.  # noqa: E501

        :return: The match_quality of this StopFinderLocation.  # noqa: E501
        :rtype: int
        """
        return self._match_quality

    @match_quality.setter
    def match_quality(self, match_quality):
        """Sets the match_quality of this StopFinderLocation.

        This value indicates how well the returned stop matches the search query. A higher number indicates a better match.  # noqa: E501

        :param match_quality: The match_quality of this StopFinderLocation.  # noqa: E501
        :type: int
        """

        self._match_quality = match_quality

    @property
    def modes(self):
        """Gets the modes of this StopFinderLocation.  # noqa: E501

        This is included only if the `type` value is set to `stop`. Contains a list of modes of transport that service this stop. This can be useful for showing relevant wayfinding icons when presenting users with a list of matching stops to choose from.  The following values may be present:  * `1`: Train * `2`: Metro * `4`: Light Rail * `5`: Bus * `7`: Coach * `9`: Ferry * `11`: School Bus   # noqa: E501

        :return: The modes of this StopFinderLocation.  # noqa: E501
        :rtype: list[int]
        """
        return self._modes

    @modes.setter
    def modes(self, modes):
        """Sets the modes of this StopFinderLocation.

        This is included only if the `type` value is set to `stop`. Contains a list of modes of transport that service this stop. This can be useful for showing relevant wayfinding icons when presenting users with a list of matching stops to choose from.  The following values may be present:  * `1`: Train * `2`: Metro * `4`: Light Rail * `5`: Bus * `7`: Coach * `9`: Ferry * `11`: School Bus   # noqa: E501

        :param modes: The modes of this StopFinderLocation.  # noqa: E501
        :type: list[int]
        """

        self._modes = modes

    @property
    def name(self):
        """Gets the name of this StopFinderLocation.  # noqa: E501

        This is the long version of the location name, which may include the suburb or other information.   # noqa: E501

        :return: The name of this StopFinderLocation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StopFinderLocation.

        This is the long version of the location name, which may include the suburb or other information.   # noqa: E501

        :param name: The name of this StopFinderLocation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent(self):
        """Gets the parent of this StopFinderLocation.  # noqa: E501

        If available, contains information about this location's parent location. For example, if the stop has a type of `platform`, then this field may contain information about the station in which the platform is located.   # noqa: E501

        :return: The parent of this StopFinderLocation.  # noqa: E501
        :rtype: ParentLocation
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this StopFinderLocation.

        If available, contains information about this location's parent location. For example, if the stop has a type of `platform`, then this field may contain information about the station in which the platform is located.   # noqa: E501

        :param parent: The parent of this StopFinderLocation.  # noqa: E501
        :type: ParentLocation
        """

        self._parent = parent

    @property
    def street_name(self):
        """Gets the street_name of this StopFinderLocation.  # noqa: E501

        This is included only if the `type` value is set to `street` or `singlehouse`.  # noqa: E501

        :return: The street_name of this StopFinderLocation.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this StopFinderLocation.

        This is included only if the `type` value is set to `street` or `singlehouse`.  # noqa: E501

        :param street_name: The street_name of this StopFinderLocation.  # noqa: E501
        :type: str
        """

        self._street_name = street_name

    @property
    def type(self):
        """Gets the type of this StopFinderLocation.  # noqa: E501

        This is the type of location being returned. It may represent a stop or platform that a public transport service physically stops at for passenger boarding, or it may represent somebody's house. A value of `unknown` likely indicates bad data coming from the server. If a location is returned with this type, you can safely ignore it.   # noqa: E501

        :return: The type of this StopFinderLocation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StopFinderLocation.

        This is the type of location being returned. It may represent a stop or platform that a public transport service physically stops at for passenger boarding, or it may represent somebody's house. A value of `unknown` likely indicates bad data coming from the server. If a location is returned with this type, you can safely ignore it.   # noqa: E501

        :param type: The type of this StopFinderLocation.  # noqa: E501
        :type: str
        """
        allowed_values = ["poi", "singlehouse", "stop", "platform", "street", "locality", "suburb", "address", "unknown"]  # noqa: E501
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
        if issubclass(StopFinderLocation, dict):
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
        if not isinstance(other, StopFinderLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StopFinderLocation):
            return True

        return self.to_dict() != other.to_dict()
