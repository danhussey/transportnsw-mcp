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


class TripTransportation(object):
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
        'destination': 'TripTransportationDestination',
        'disassembled_name': 'str',
        'icon_id': 'int',
        'id': 'str',
        'name': 'str',
        'number': 'str',
        'operator': 'TripTransportationOperator',
        'product': 'RouteProduct',
        'properties': 'TripTransportationProperties'
    }

    attribute_map = {
        'description': 'description',
        'destination': 'destination',
        'disassembled_name': 'disassembledName',
        'icon_id': 'iconId',
        'id': 'id',
        'name': 'name',
        'number': 'number',
        'operator': 'operator',
        'product': 'product',
        'properties': 'properties'
    }

    def __init__(self, description=None, destination=None, disassembled_name=None, icon_id=None, id=None, name=None, number=None, operator=None, product=None, properties=None, _configuration=None):  # noqa: E501
        """TripTransportation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._destination = None
        self._disassembled_name = None
        self._icon_id = None
        self._id = None
        self._name = None
        self._number = None
        self._operator = None
        self._product = None
        self._properties = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if destination is not None:
            self.destination = destination
        if disassembled_name is not None:
            self.disassembled_name = disassembled_name
        if icon_id is not None:
            self.icon_id = icon_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if number is not None:
            self.number = number
        if operator is not None:
            self.operator = operator
        if product is not None:
            self.product = product
        if properties is not None:
            self.properties = properties

    @property
    def description(self):
        """Gets the description of this TripTransportation.  # noqa: E501

        Contains a description of this route.   # noqa: E501

        :return: The description of this TripTransportation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TripTransportation.

        Contains a description of this route.   # noqa: E501

        :param description: The description of this TripTransportation.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def destination(self):
        """Gets the destination of this TripTransportation.  # noqa: E501


        :return: The destination of this TripTransportation.  # noqa: E501
        :rtype: TripTransportationDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this TripTransportation.


        :param destination: The destination of this TripTransportation.  # noqa: E501
        :type: TripTransportationDestination
        """

        self._destination = destination

    @property
    def disassembled_name(self):
        """Gets the disassembled_name of this TripTransportation.  # noqa: E501

        Contains a very short name for the route.   # noqa: E501

        :return: The disassembled_name of this TripTransportation.  # noqa: E501
        :rtype: str
        """
        return self._disassembled_name

    @disassembled_name.setter
    def disassembled_name(self, disassembled_name):
        """Sets the disassembled_name of this TripTransportation.

        Contains a very short name for the route.   # noqa: E501

        :param disassembled_name: The disassembled_name of this TripTransportation.  # noqa: E501
        :type: str
        """

        self._disassembled_name = disassembled_name

    @property
    def icon_id(self):
        """Gets the icon_id of this TripTransportation.  # noqa: E501

        Contains an ID for the icon that can be used for this route. Different values here are used to differentiate differents types of the same route type. For example, private ferries have a different wayfinding icon to ferries operated by Sydney Ferries.  * `1`: Sydney Trains (product class `1`) * `2`: Intercity Trains (product class `1`) * `3`: Regional Trains (product class `1`) * `19`: Temporary Trains (product class `1`)  * `24`: Sydney Metro (product class `2`)  * `13`: Sydney Light Rail (product class `4`) * `20`: Temporary Light Rail (product class `4`) * `21`: Newcastle Light Rail (product class `4`)  * `4`: Blue Mountains Buses (product class `5`) * `5`: Sydney Buses (product class `5`) * `6`: Central Coast Buses (product class `5`) * `14`: Temporary Buses (product class `5`) * `15`: Hunter Buses (product class `5`) * `23`: On Demand (product class `5`) * `31`: Central West and Orana (product class `5`) * `32`: Far West (product class `5`) * `33`: New England North West (product class `5`) * `34`: Newcastle and Hunter (product class `5`) * `35`: North Coast (product class `5`) * `36`: Riverina Murray (product class `5`) * `37`: South East and Tablelands (product class `5`) * `38`: Sydney and Surrounds (product class `5`)  * `9`: Private Buses (product class `5`) * `17`: Private Coaches (product class `5`)  * `7`: Regional Coaches (product class `7`) * `22`: Temporary Coaches (product class `7`)  * `10`: Sydney Ferries (product class `9`) * `11`: Newcastle Ferries (product class `9`) * `12`: Private Ferries (product class `9`) * `18`: Temporary Ferries (product class `9`)  * `8`: School Buses (product class `11`)   # noqa: E501

        :return: The icon_id of this TripTransportation.  # noqa: E501
        :rtype: int
        """
        return self._icon_id

    @icon_id.setter
    def icon_id(self, icon_id):
        """Sets the icon_id of this TripTransportation.

        Contains an ID for the icon that can be used for this route. Different values here are used to differentiate differents types of the same route type. For example, private ferries have a different wayfinding icon to ferries operated by Sydney Ferries.  * `1`: Sydney Trains (product class `1`) * `2`: Intercity Trains (product class `1`) * `3`: Regional Trains (product class `1`) * `19`: Temporary Trains (product class `1`)  * `24`: Sydney Metro (product class `2`)  * `13`: Sydney Light Rail (product class `4`) * `20`: Temporary Light Rail (product class `4`) * `21`: Newcastle Light Rail (product class `4`)  * `4`: Blue Mountains Buses (product class `5`) * `5`: Sydney Buses (product class `5`) * `6`: Central Coast Buses (product class `5`) * `14`: Temporary Buses (product class `5`) * `15`: Hunter Buses (product class `5`) * `23`: On Demand (product class `5`) * `31`: Central West and Orana (product class `5`) * `32`: Far West (product class `5`) * `33`: New England North West (product class `5`) * `34`: Newcastle and Hunter (product class `5`) * `35`: North Coast (product class `5`) * `36`: Riverina Murray (product class `5`) * `37`: South East and Tablelands (product class `5`) * `38`: Sydney and Surrounds (product class `5`)  * `9`: Private Buses (product class `5`) * `17`: Private Coaches (product class `5`)  * `7`: Regional Coaches (product class `7`) * `22`: Temporary Coaches (product class `7`)  * `10`: Sydney Ferries (product class `9`) * `11`: Newcastle Ferries (product class `9`) * `12`: Private Ferries (product class `9`) * `18`: Temporary Ferries (product class `9`)  * `8`: School Buses (product class `11`)   # noqa: E501

        :param icon_id: The icon_id of this TripTransportation.  # noqa: E501
        :type: int
        """

        self._icon_id = icon_id

    @property
    def id(self):
        """Gets the id of this TripTransportation.  # noqa: E501

        This is an ID that uniquely identifies this route.   # noqa: E501

        :return: The id of this TripTransportation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TripTransportation.

        This is an ID that uniquely identifies this route.   # noqa: E501

        :param id: The id of this TripTransportation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TripTransportation.  # noqa: E501

        This contains the full name of the route.   # noqa: E501

        :return: The name of this TripTransportation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TripTransportation.

        This contains the full name of the route.   # noqa: E501

        :param name: The name of this TripTransportation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this TripTransportation.  # noqa: E501

        Contains a short name for the route.   # noqa: E501

        :return: The number of this TripTransportation.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TripTransportation.

        Contains a short name for the route.   # noqa: E501

        :param number: The number of this TripTransportation.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def operator(self):
        """Gets the operator of this TripTransportation.  # noqa: E501


        :return: The operator of this TripTransportation.  # noqa: E501
        :rtype: TripTransportationOperator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this TripTransportation.


        :param operator: The operator of this TripTransportation.  # noqa: E501
        :type: TripTransportationOperator
        """

        self._operator = operator

    @property
    def product(self):
        """Gets the product of this TripTransportation.  # noqa: E501

        This element contains additional properties about the route.  # noqa: E501

        :return: The product of this TripTransportation.  # noqa: E501
        :rtype: RouteProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this TripTransportation.

        This element contains additional properties about the route.  # noqa: E501

        :param product: The product of this TripTransportation.  # noqa: E501
        :type: RouteProduct
        """

        self._product = product

    @property
    def properties(self):
        """Gets the properties of this TripTransportation.  # noqa: E501


        :return: The properties of this TripTransportation.  # noqa: E501
        :rtype: TripTransportationProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this TripTransportation.


        :param properties: The properties of this TripTransportation.  # noqa: E501
        :type: TripTransportationProperties
        """

        self._properties = properties

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
        if issubclass(TripTransportation, dict):
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
        if not isinstance(other, TripTransportation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TripTransportation):
            return True

        return self.to_dict() != other.to_dict()
