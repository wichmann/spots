
"""
Configuration data.

Created on Fri Oct 17 15:41:58 2014

@author: Christian Wichmann
"""


DEFAULT_CYCLE_TIME_MS = 500.
DEFAULT_MODBUS_PORT = 502

MODULES = {
    'WAGO-IPC': '192.168.10.130',
    'WAGO-IO': '192.168.10.129'
}

INPUT_BITS = {
    'I1': 'WAGO-IPC:0'
}

OUTPUT_BITS = {
    'O1': 'WAGO-IO:512',
    'O2': 'WAGO-IO:513',
    'O3': 'WAGO-IO:514',
    'O4': 'WAGO-IO:515',
    'O5': 'WAGO-IO:516',
    'O6': 'WAGO-IO:517',
    'O7': 'WAGO-IO:518',
    'O8': 'WAGO-IO:519',
    'O9': 'WAGO-IO:520',
    'O10': 'WAGO-IO:521',
    'O11': 'WAGO-IPC:0',
    'O12': 'WAGO-IPC:1',
    'O13': 'WAGO-IPC:2',
    'O14': 'WAGO-IPC:3'
}
