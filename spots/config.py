
"""
Configuration data.

Created on Fri Oct 17 15:41:58 2014

@author: Christian Wichmann
"""


DEFAULT_CYCLE_TIME_MS = 500.
DEFAULT_MODBUS_PORT = 502

CONTROLLER_ADDRESSES = {
    'WAGO-IPC': '192.168.10.130',
    'WAGO-IO': '192.168.10.129'
}

# TODO Move the dictionaries for inputs and outputs to module 'spots.plc'
INPUT_BITS = {
    'I1': 'WAGO-IPC:0',
    'I2': 'WAGO-IPC:1',
    'I3': 'WAGO-IPC:2',
    'I4': 'WAGO-IPC:3'
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

# source to be executed
SAMPLE_SOURCE = """O9:=true;
O13:=I1 or I2;
O8:=false;
O7:=not I1 and I3;
O6:= not true;
O5:=I1 and I2 and I3;
O4:= not I3;
"""
