#! /usr/bin/env python
"""
Simple implementation of a Soft-PLC that controls decentralized I/O modules
via MODBUS/TCP.

This script starts and does not return to the OS. It reads all inputs every so
often (depending on the cycle time) and writes values back to outputs.

TODO:
 - Check out http://fdik.org/iec2xml/.
 - 

Created on Thu Oct 16 18:34:40 2014

@author: Christian Wichmann
"""

import logging
import logging.handlers
import sys
import time

from spots import config
from spots import plc
from spots.plc import CONTROLLER_TYPE


# source to be executed
source = """O9 := I1;O10 := I1;O11 := I1;O12 := I1;"""


def create_logger():
    """Creates logger for this application."""
    LOG_FILENAME = 'spots.log'
    logger = logging.getLogger('spots')
    logger.setLevel(logging.DEBUG)
    log_to_file = logging.handlers.RotatingFileHandler(LOG_FILENAME,
                                                       maxBytes=262144,
                                                       backupCount=5)
    log_to_file.setLevel(logging.DEBUG)
    logger.addHandler(log_to_file)
    log_to_screen = logging.StreamHandler(sys.stdout)
    log_to_screen.setLevel(logging.INFO)
    logger.addHandler(log_to_screen)
    return logger


def start_plc():
    logger = create_logger()
    # build controller objects for reading and writing bits
    for key in config.MODULES:
        #plc.create_controller(CONTROLLER_TYPE.Modbus, key, config.MODULES[key])
        plc.create_controller(CONTROLLER_TYPE.Dummy, key)
    # process inputs into outputs
    try:
        while True:
            input_image = plc.read_input_bits()
            output_image = plc.process_input_to_output(source, input_image)
            plc.write_output_bits(output_image)
            time.sleep(config.DEFAULT_CYCLE_TIME_MS / 1000.)
    except KeyboardInterrupt:
        logger.info('Good bye!')


if __name__ == '__main__':
    start_plc()
