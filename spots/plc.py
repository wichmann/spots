
"""
Providing classes and functions for handling and running a Soft-PLC.

Created on Fri Oct 17 15:41:17 2014

@author: Christian Wichmann
"""

import logging
from enum import Enum

from spots import config
from spots import controller
from spots import st


logger = logging.getLogger('spots.plc')


# list with all controller instances for all modules, e.g. ModbusModule
CONTROLLER = {
}


CONTROLLER_TYPE = Enum('Modbus', 'Dummy')


def create_controller(controller_type, name, ip=''):
    """Creates a new controller that can be used as I/O module for this
    SoftPLC. The given name has to be distinct and unique because it has to be
    used to identify I/O ports in those modules via the config file.

    Currently the following types of controller are supported:
     - Modbus
     - Dummy

    :param controller_type: type of controller to be created
    :param name: distinct and unique name for this controller
    :param ip: Optional parameter with the ip address of the controller
    """
    if controller_type == CONTROLLER_TYPE.Modbus:
        CONTROLLER[name] = controller.ModbusModule(name, ip)
    elif controller_type == CONTROLLER_TYPE.Dummy:
        CONTROLLER[name] = controller.DummyModule(name)
    else:
        logger.error('Could not create controller because invalid controller type.')


def read_input_bits():
    input_image = {}
    for key in config.INPUT_BITS:
        input_image[key] = read_bit_from_input(config.INPUT_BITS[key])
    return input_image


def read_bit_from_input(port_id):
    controller, address = port_id.split(':')
    value = CONTROLLER[controller].get_bit(int(address))
    logger.debug('reading value from address ' + str(address) + ': ' + str(value))
    return value


def process_input_to_output(source, input_image):
    """Processes the given input image and executes the source to determine
    the values of all outputs. Currently it handles only source code in ST
    (IEC 61131).
    
    :param source: string containing the source to be executed
    :param input_image: input image with value of all inputs
    :returns: output image with all output values
    """
    # TODO Handle different languages besides ST.
    st.parse_source(source)
    output_image = st.execute_source(input_image)
    return output_image


def write_output_bits(output_image):
    for key in output_image:
        write_bit_into_output(config.OUTPUT_BITS[key], output_image[key])


def write_bit_into_output(port_id, value):
    controller, address = port_id.split(':')
    logger.debug('writing value of ' + str(value) + ' to address ' + str(address))
    CONTROLLER[controller].set_bit(int(address), value)
