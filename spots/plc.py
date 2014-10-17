
"""
Providing classes and functions for handling and running a Soft-PLC.

Created on Fri Oct 17 15:41:17 2014

@author: Christian Wichmann
"""

import config

from pymodbus.client.sync import ModbusTcpClient as ModbusClient


class IOModule():
    def __init__(self, io_module_name):
        ip = config.MODULES[io_module_name]
        self.client = ModbusClient(ip, port=config.DEFAULT_MODBUS_PORT)
        self.client.connect()

    def __del__(self):
        self.client.close()

    def get_bit(self, address):
        result = self.client.read_coils(address)
        return result.bits[0]

    def set_bit(self, address, value):
        self.client.write_coil(address, value)


def read_input_bits():
    input_image = {}
    for key in config.INPUT_BITS:
        input_image[key] = read_bit_from_input(config.INPUT_BITS[key])
    return input_image


def read_bit_from_input(port_id):
    controller, address = port_id.split(':')
    value = config.CONTROLLER[controller].get_bit(int(address))
    print('reading value from address ' + str(address) + ': ' + str(value))
    return value


def process_input_to_output(input_image):
    output_image = {}
    for key in config.OUTPUT_BITS:
        output_image[key] = False
    if input_image['I1'] == True:
        output_image['O9'] = True
        output_image['O10'] = True
        output_image['O14'] = True
    return output_image


def write_output_bits(output_image):
    for key in output_image:
        write_bit_into_output(config.OUTPUT_BITS[key], output_image[key])


def write_bit_into_output(port_id, value):
    controller, address = port_id.split(':')
    print('writing value of ' + str(value) + ' to address ' + str(address))
    config.CONTROLLER[controller].set_bit(int(address), value)
