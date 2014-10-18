#! /usr/bin/env python
"""
Simple implementation of a Soft-PLC that controls decentralized I/O modules
via MODBUS/TCP.

This script starts and does not return to the OS. It reads all inputs every so
often (depending on the cycle time) and writes values back to outputs.

Created on Thu Oct 16 18:34:40 2014

@author: Christian Wichmann
"""

import time

from spots import config
from spots import plc


source = """O9 := I1;O10 := I1;O11 := I1;O12 := I1;"""


def setup_logging():
    import logging
    logging.basicConfig()
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)


def start_plc():
    # build controller objects for reading and writing bits
    for key in config.MODULES:
        config.CONTROLLER[key] = plc.IOModule(key)
    # process inputs into outputs
    try:
        while True:
            input_image = plc.read_input_bits()
            output_image = plc.process_input_to_output(source, input_image)
            plc.write_output_bits(output_image)
            time.sleep(config.DEFAULT_CYCLE_TIME_MS / 1000.)
    except KeyboardInterrupt:
        print('Good bye!')


if __name__ == '__main__':
    start_plc()
