
"""
Provides controller modules for connecting to decentralized I/O controllers
via different bus systems or field buses.

Info:
 - https://github.com/bashwork/pymodbus/
 - 

Created on Sat Oct 18 12:40:04 2014

@author: christian
"""

import logging
from enum import Enum

from spots import config

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.client.sync import ConnectionException


logger = logging.getLogger('spots.controller')


# TODO Change this to NOT use Enums! See: 
# http://stackoverflow.com/questions/1969005/enumerations-in-python/1970200#1970200
#CONTROLLER_TYPE = Enum('CONTROLLER_TYPE', 'Modbus Dummy')
class CONTROLLER_TYPE(Enum):
    __order__ = 'Modbus Dummy'
    Modbus = 1
    Dummy = 2


class ModbusModule():
    def __init__(self, io_module_name, ip):
        self.io_module_name = io_module_name
        self.ip_address = ip
        self.controller_type = CONTROLLER_TYPE.Modbus
        # build connection object
        self.client = ModbusClient(ip, port=config.DEFAULT_MODBUS_PORT)
        self.client.connect()

    def __del__(self):
        self.client.close()

    def __str__(self):
        return 'Controller "{}" at address {}'.format(self.io_module_name, self.ip_address)

    def get_bit(self, address):
        try:
            result = self.client.read_coils(address)
            bit_value = result.bits[0]
        except ConnectionException:
            logger.error('Could not connect to Modbus module "{}"!'
                         .format(self.io_module_name))
            bit_value = False
        return bit_value

    def set_bit(self, address, value):
        try:
            self.client.write_coil(address, value)
        except ConnectionException:
            logger.error('Could not connect to Modbus module "{}"!'
                         .format(self.io_module_name))


class DummyModule():
    def __init__(self, io_module_name):
        self.io_module_name = io_module_name
        self.ip_address = ''
        self.controller_type = CONTROLLER_TYPE.Dummy

    def __del__(self):
        pass

    def __str__(self):
        return 'Controller Dummy "{}"'.format(self.io_module_name)

    def get_bit(self, address):
        logger.debug('Getting random bit...')
        import random
        return bool(random.randint(0, 1))

    def set_bit(self, address, value):
        logger.debug('Setting bit...')
