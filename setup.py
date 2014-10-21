#! /usr/bin/env python

from cx_Freeze import setup, Executable
#try:
#    from setuptools.core import setup
#except ImportError:
#    from distutils.core import setup


# Dependencies are automatically detected, but it might need fine tuning.
buildOptions = dict(packages=['pymodbus', 'pypeg2'], excludes=[])

executables = [
    Executable('spots_gui.py'),
    Executable('spots_plc.py')
]

setup(
    name='SPotS',
    version='0.1',
    author='Christian Wichmann',
    author_email='wichmann@bbs-os-brinkstr.de',
    packages=['spots', 'gui'],
    url='',
    license='LICENSE',
    description='SoftPLC to control multiple I/O nodes via ModbusTCP',
    options=dict(build_exe=buildOptions),
    executables=executables
)
