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


class TripRequestResponseMessage(object):
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
        'code': 'int',
        'error': 'str',
        'module': 'str',
        'type': 'str'
    }

    attribute_map = {
        'code': 'code',
        'error': 'error',
        'module': 'module',
        'type': 'type'
    }

    def __init__(self, code=None, error=None, module=None, type=None, _configuration=None):  # noqa: E501
        """TripRequestResponseMessage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._error = None
        self._module = None
        self._type = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if error is not None:
            self.error = error
        if module is not None:
            self.module = module
        if type is not None:
            self.type = type

    @property
    def code(self):
        """Gets the code of this TripRequestResponseMessage.  # noqa: E501

        This is an error/warning code for the message. Note that the same code may be returned with a different meaning, depending on the context. The following error codes are possible:  * `-1000` (`PLACE_INVALID`) - Invalid locality input * `-1001` (`PLACE_WITHOUT_STOPS`) - Verified locality does not have stops * `-1010` (`PLACE_UNKNOWN_POOL`) - Locality not in locality tree * `-1020` (`PLACE_ALPHA_INVALID`) - Invalid alpha list  * `-2000` (`STOP_INVALID`) - Invalid stop input * `-2001` (`STOP_PLACE_ID_INVALID`) - Stop number not in locality  * `-3000` (`ADDRESS_INVALID`) - Invalid address input * `-3001` (`ADDRESS_PLACE_WITHOUT_ADDR`) - Locality does not have any addresses  * `-1000` (`IT_COORD_UNKNOWN`) - Transferred coordinate not supported (incorrect coordinate system) * `-1001` (`IT_COORD_OUT_OF_REGION`) - Transferred coordinates not supported (outside of region) * `-1002` (`IT_COORD_FORMAT_UNKNOWN`) - Transferred coordinate is ok, but the format does not match the value * `-200` (`IT_GEOREF_UNKNOWN`) - Invalid georeference * `-201` (`IT_GEOREF_OUT_OF_REGION`) - Invalid georeference section < 0 or > length of route section * `-300` (`IT_NO_START`) - No origin entered * `-301` (`IT_NO_DESTINATION`) - No destination entered * `-302` (`IT_NO_CONNECTION`) - No journey found * `-303` (`IT_NO_TRANSITIONS`) - No transition point  * `-3000` (`IT_ADDRESS_INVALID`) - Address invalid * `-3001` (`IT_ADDRESS_PLACE_WITHOUT_ADDR`) - Locality does not have any addresses * `-3002` (`IT_ADDRESS_EMPTY`) - Empty address input  * `-5000` (`IT_LOCATOR_INVALID`) - Input locality is invalid * `-5001` (`IT_LOCATOR_INVALID_POOL`) - Input locality not available in locality tree * `-5002` (`IT_LOCATOR_BULK_POSTCODE`) - Bulk postcode, postcode with addresses  * `-4000` (`IT_STREET_INVALID`) - Input street is invalid * `-4001` (`IT_STREE_PLACE_WITHOUT_ADDR`) - Locality does not have any streets  * `-8010` (`ANY_UNIQUE`) - Any input uniquely verified * `-8011` (`ANY_LIST`) - Any list verified * `-8012` (`ANY_INVALID`) - Any input invalid * `-8013` (`ANY_PLACE_WITHOUT_MATCHES`) - Any location found, but cannot be verified * `-8014` (`ANY_TOO_MANY_MATCHES`) - Any input has too many matches * `-8020` (`ANY_MATCH_NONE`) - No matches * `-8031` (`ANY_MATCH`) - Matches (e.g. buildings) found for a street * `-8032` (`ANY_NO_MATCH`) - No matches found (e.g. buildings) for a street  * `-4000` (`NO_CONNECTION`) - No journey found for the time entered * `-4001` (`DATE_INVALID`) - Date not possible in the current timetable period * `-4002` (`NO_ORIGIN`) - No origin verified * `-4003` (`NO_DESTINATION`) - No destination verified * `-4004` (`ORIGIN_UNKNOWN`) - Origin exists, but cannot be identified * `-4005` (`DESTINATION_UNKNOWN`) - Destination exists, but cannot be identified * `-4006` (`JUST_WALK`) - Only a walk has been found * `-4007` (`ORIGIN_EQUI_DEST`) - Origin and destination are identical * `-4008` (`VIA_UNKNOWN`) - Unknown via-point * `-4009` (`TIMESPAN_INVALID`) - Time interval is invalid * `-4010` (`VIA_NOINTERCHANGE`) - Via stop point is not an interchange stop * `-4011` (`VIA_INVALID`) - Invalid via input * `+4011` (`TRIPSTATUS_ALREADYFOUND`) - Moved journey already exists * `-4012` (`ORIGIN_OUTOFPERMITTEDAREA`) - Origin outside the valid zone (e.g. fare zone) * `-4013` (`DESTINATION_OUTOFPERMITTEDAREA`) - Destination outside the valid zone (e.g. fare zone) * `-4014` (`VIA_OUTOFPERMITTEDAREA`) - Via outside the valid zone (e.g. fare zone) * `-4020` (`NO_TRANSITION`) - No transition point found * `-4030` (`NO_DEPARTURE`) - No departures found * `-4040` (`NO_ARRIVAL`) - No arrivals found * `-4050` (`NO_SERVINGLINES`) - No services found at this stop * `-4060` (`NO_MATCHINGOPERATORS`) - No matching operators  * `-4100` (`NO_CONNECTION_BECAUSE_OF_RULE`) - No journey because of a rule * `-4101` (`RULE_CHANGED_OPTIONS`) - Rule changed the options * `-4102` (`RULE_CHANGED_USEONLY`) - Rule chagned the permitted vehicles * `-4103` (`RECOMPUTE_BECAUSE_OF_RULE`) - Journey has been recalculated due to a rule with different parameters * `-4104` (`RULE_CHANGED_WITHOUTVIA`) - Rule removed the via point * `-4300` (`NO_CONNECTION_BECAUSE_OF_PREFERTOEXCLUDE_SETTINGS`) - Invalid prefer-to-exclude parameter * `-4301` (`NO_CONNECTION_BECAUSE_OF_PREFERTOINCLUDE_SETTINGS`) - Invalid prefer-to-include parameter * `-4302` (`NO_CONNECTION_BECAUSE_OF_MIXEDSETTING_SETTINGS`) - Invalid mixing of prefer-to-exclude/include parameters * `-4303` (`NO_CONNECTION_BECAUSE_OF_WALKING_SETTINGS`) - Invalid footpath parameter * `-9999` (`TRIP_CANCELLED`) - Trip has been cancelled * `-10015` (`ERROR_ITROUTER_NO_IT_CONN`) - No journey found   # noqa: E501

        :return: The code of this TripRequestResponseMessage.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this TripRequestResponseMessage.

        This is an error/warning code for the message. Note that the same code may be returned with a different meaning, depending on the context. The following error codes are possible:  * `-1000` (`PLACE_INVALID`) - Invalid locality input * `-1001` (`PLACE_WITHOUT_STOPS`) - Verified locality does not have stops * `-1010` (`PLACE_UNKNOWN_POOL`) - Locality not in locality tree * `-1020` (`PLACE_ALPHA_INVALID`) - Invalid alpha list  * `-2000` (`STOP_INVALID`) - Invalid stop input * `-2001` (`STOP_PLACE_ID_INVALID`) - Stop number not in locality  * `-3000` (`ADDRESS_INVALID`) - Invalid address input * `-3001` (`ADDRESS_PLACE_WITHOUT_ADDR`) - Locality does not have any addresses  * `-1000` (`IT_COORD_UNKNOWN`) - Transferred coordinate not supported (incorrect coordinate system) * `-1001` (`IT_COORD_OUT_OF_REGION`) - Transferred coordinates not supported (outside of region) * `-1002` (`IT_COORD_FORMAT_UNKNOWN`) - Transferred coordinate is ok, but the format does not match the value * `-200` (`IT_GEOREF_UNKNOWN`) - Invalid georeference * `-201` (`IT_GEOREF_OUT_OF_REGION`) - Invalid georeference section < 0 or > length of route section * `-300` (`IT_NO_START`) - No origin entered * `-301` (`IT_NO_DESTINATION`) - No destination entered * `-302` (`IT_NO_CONNECTION`) - No journey found * `-303` (`IT_NO_TRANSITIONS`) - No transition point  * `-3000` (`IT_ADDRESS_INVALID`) - Address invalid * `-3001` (`IT_ADDRESS_PLACE_WITHOUT_ADDR`) - Locality does not have any addresses * `-3002` (`IT_ADDRESS_EMPTY`) - Empty address input  * `-5000` (`IT_LOCATOR_INVALID`) - Input locality is invalid * `-5001` (`IT_LOCATOR_INVALID_POOL`) - Input locality not available in locality tree * `-5002` (`IT_LOCATOR_BULK_POSTCODE`) - Bulk postcode, postcode with addresses  * `-4000` (`IT_STREET_INVALID`) - Input street is invalid * `-4001` (`IT_STREE_PLACE_WITHOUT_ADDR`) - Locality does not have any streets  * `-8010` (`ANY_UNIQUE`) - Any input uniquely verified * `-8011` (`ANY_LIST`) - Any list verified * `-8012` (`ANY_INVALID`) - Any input invalid * `-8013` (`ANY_PLACE_WITHOUT_MATCHES`) - Any location found, but cannot be verified * `-8014` (`ANY_TOO_MANY_MATCHES`) - Any input has too many matches * `-8020` (`ANY_MATCH_NONE`) - No matches * `-8031` (`ANY_MATCH`) - Matches (e.g. buildings) found for a street * `-8032` (`ANY_NO_MATCH`) - No matches found (e.g. buildings) for a street  * `-4000` (`NO_CONNECTION`) - No journey found for the time entered * `-4001` (`DATE_INVALID`) - Date not possible in the current timetable period * `-4002` (`NO_ORIGIN`) - No origin verified * `-4003` (`NO_DESTINATION`) - No destination verified * `-4004` (`ORIGIN_UNKNOWN`) - Origin exists, but cannot be identified * `-4005` (`DESTINATION_UNKNOWN`) - Destination exists, but cannot be identified * `-4006` (`JUST_WALK`) - Only a walk has been found * `-4007` (`ORIGIN_EQUI_DEST`) - Origin and destination are identical * `-4008` (`VIA_UNKNOWN`) - Unknown via-point * `-4009` (`TIMESPAN_INVALID`) - Time interval is invalid * `-4010` (`VIA_NOINTERCHANGE`) - Via stop point is not an interchange stop * `-4011` (`VIA_INVALID`) - Invalid via input * `+4011` (`TRIPSTATUS_ALREADYFOUND`) - Moved journey already exists * `-4012` (`ORIGIN_OUTOFPERMITTEDAREA`) - Origin outside the valid zone (e.g. fare zone) * `-4013` (`DESTINATION_OUTOFPERMITTEDAREA`) - Destination outside the valid zone (e.g. fare zone) * `-4014` (`VIA_OUTOFPERMITTEDAREA`) - Via outside the valid zone (e.g. fare zone) * `-4020` (`NO_TRANSITION`) - No transition point found * `-4030` (`NO_DEPARTURE`) - No departures found * `-4040` (`NO_ARRIVAL`) - No arrivals found * `-4050` (`NO_SERVINGLINES`) - No services found at this stop * `-4060` (`NO_MATCHINGOPERATORS`) - No matching operators  * `-4100` (`NO_CONNECTION_BECAUSE_OF_RULE`) - No journey because of a rule * `-4101` (`RULE_CHANGED_OPTIONS`) - Rule changed the options * `-4102` (`RULE_CHANGED_USEONLY`) - Rule chagned the permitted vehicles * `-4103` (`RECOMPUTE_BECAUSE_OF_RULE`) - Journey has been recalculated due to a rule with different parameters * `-4104` (`RULE_CHANGED_WITHOUTVIA`) - Rule removed the via point * `-4300` (`NO_CONNECTION_BECAUSE_OF_PREFERTOEXCLUDE_SETTINGS`) - Invalid prefer-to-exclude parameter * `-4301` (`NO_CONNECTION_BECAUSE_OF_PREFERTOINCLUDE_SETTINGS`) - Invalid prefer-to-include parameter * `-4302` (`NO_CONNECTION_BECAUSE_OF_MIXEDSETTING_SETTINGS`) - Invalid mixing of prefer-to-exclude/include parameters * `-4303` (`NO_CONNECTION_BECAUSE_OF_WALKING_SETTINGS`) - Invalid footpath parameter * `-9999` (`TRIP_CANCELLED`) - Trip has been cancelled * `-10015` (`ERROR_ITROUTER_NO_IT_CONN`) - No journey found   # noqa: E501

        :param code: The code of this TripRequestResponseMessage.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def error(self):
        """Gets the error of this TripRequestResponseMessage.  # noqa: E501

        This is the error summary for the given message.  # noqa: E501

        :return: The error of this TripRequestResponseMessage.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this TripRequestResponseMessage.

        This is the error summary for the given message.  # noqa: E501

        :param error: The error of this TripRequestResponseMessage.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def module(self):
        """Gets the module of this TripRequestResponseMessage.  # noqa: E501

        Indicates the server module that provided this system message.  # noqa: E501

        :return: The module of this TripRequestResponseMessage.  # noqa: E501
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this TripRequestResponseMessage.

        Indicates the server module that provided this system message.  # noqa: E501

        :param module: The module of this TripRequestResponseMessage.  # noqa: E501
        :type: str
        """

        self._module = module

    @property
    def type(self):
        """Gets the type of this TripRequestResponseMessage.  # noqa: E501

        Indicates the type of system message.  # noqa: E501

        :return: The type of this TripRequestResponseMessage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TripRequestResponseMessage.

        Indicates the type of system message.  # noqa: E501

        :param type: The type of this TripRequestResponseMessage.  # noqa: E501
        :type: str
        """

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
        if issubclass(TripRequestResponseMessage, dict):
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
        if not isinstance(other, TripRequestResponseMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TripRequestResponseMessage):
            return True

        return self.to_dict() != other.to_dict()
