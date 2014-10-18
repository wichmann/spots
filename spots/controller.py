
"""
Provides controller modules for connecting to decentralized I/O controllers
via different bus systems or field buses.

Created on Sat Oct 18 12:40:04 2014

@author: christian
"""

import logging

from spots import config

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.client.sync import ConnectionException


logger = logging.getLogger('spots.controller')


class ModbusModule():
    def __init__(self, io_module_name, ip):
        self.io_module_name = io_module_name
        self.client = ModbusClient(ip, port=config.DEFAULT_MODBUS_PORT)
        self.client.connect()

    def __del__(self):
        self.client.close()

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
        pass

    def __del__(self):
        pass

    def get_bit(self, address):
        logger.debug('Getting random bit...')
        import random
        return bool(random.randint(0, 1))

    def set_bit(self, address, value):
        logger.debug('Setting bit...')
