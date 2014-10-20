#! /usr/bin/env python
"""
Simple graphical user interface for SoftPLC.

Created on Sat Oct 18 18:34:40 2014

@author: Christian Wichmann
"""

import logging
import logging.handlers
import sys

from spots import config
from spots import plc
from gui import gui
from spots.controller import CONTROLLER_TYPE


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


def start_gui():
    logger = create_logger()
    # build controller objects for reading and writing bits
    for key in config.CONTROLLER_ADDRESSES:
        #plc.create_controller(CONTROLLER_TYPE.Modbus, key, config.CONTROLLER_ADDRESSES[key])
        plc.create_controller(CONTROLLER_TYPE.Dummy, key)
    # start GUI
    logger.info('Starting SPotS gui...')
    gui.start_gui()


if __name__ == '__main__':
    start_gui()
