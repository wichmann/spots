SPotS
=====

DESCRIPTION
-----------
SoftPLC to control multiple I/O nodes via ModbusTCP.


KNOWN PROBLEMS AND BUGS
-----------------------


LICENSE
-------
SPotS is released under the GNU General Public License v2 or newer.


REQUIREMENTS
------------
SPotS runs with Python 2.7 and 3.4. It requires also the following packages:

* pymodbus (connection to I/O modules via ModbusTCP)
* pypeg2 (parser for IEC 61131-3 ST)
* enum (enum support under Python 2.7)
* pyQt4 (graphical user interface)

To get pyPEG2 running under Windows insert into pyPEG2\__init__.py the
following lines:

    import itertools
    range = lambda stop: iter(itertools.count().next, stop)

	
THIRD PARTY SOFTWARE
--------------------
pyPardy includes parts of or links with the following software packages and 
programs, so give the developers lots of thanks sometime! 

* ...
* ...
