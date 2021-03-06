#!/usr/bin/env python3
"""Test the mib_ciscocdp module."""

import os
import sys
import unittest
from mock import Mock

# Try to create a working PYTHONPATH
TEST_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
SWITCHMAP_DIRECTORY = os.path.abspath(os.path.join(TEST_DIRECTORY, os.pardir))
ROOT_DIRECTORY = os.path.abspath(os.path.join(SWITCHMAP_DIRECTORY, os.pardir))
if TEST_DIRECTORY.endswith('/switchmap-ng/switchmap/test') is True:
    sys.path.append(ROOT_DIRECTORY)
else:
    print(
        'This script is not installed in the "switchmap-ng/bin" directory. '
        'Please fix.')
    sys.exit(2)

from switchmap.snmp.cisco import mib_ciscostack as testimport


class Query(object):
    """Class for snmp_manager.Query mock.

    A detailed tutorial about Python mocks can be found here:
    http://www.drdobbs.com/testing/using-mocks-in-python/240168251

    """

    def query(self):
        """Do an SNMP query."""
        pass

    def oid_exists(self):
        """Determine existence of OID on device."""
        pass

    def swalk(self):
        """Do a failsafe SNMPwalk."""
        pass

    def walk(self):
        """Do a SNMPwalk."""
        pass


class KnownValues(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    # SNMPwalk results used by Mocks.

    # Normalized walk returning integers
    nwalk_results_integer = {
        100: 100,
        200: 100
    }

    # Set the stage for SNMPwalk for integer results
    snmpobj_integer = Mock(spec=Query)
    mock_spec_integer = {
        'swalk.return_value': nwalk_results_integer,
        'walk.return_value': nwalk_results_integer,
        }
    snmpobj_integer.configure_mock(**mock_spec_integer)

    # Initializing key variables
    expected_dict = {
        100: {
            'portDuplex': 100
        },
        200: {
            'portDuplex': 100
        }
    }

    def test_get_query(self):
        """Testing function get_query."""
        pass

    def test_init_query(self):
        """Testing function init_query."""
        pass

    def test___init__(self):
        """Testing function __init__."""
        pass

    def test_layer1(self):
        """Testing function layer1."""
        pass

    def test_portduplex(self):
        """Testing function portduplex."""
        # Initialize key variables
        oid_key = 'portDuplex'
        oid = '.1.3.6.1.4.1.9.5.1.4.1.1.10'

        # Get results
        testobj = testimport.init_query(self.snmpobj_integer)
        results = testobj.portduplex()

        # Basic testing of results
        for key, value in results.items():
            self.assertEqual(isinstance(key, int), True)
            self.assertEqual(value, self.expected_dict[key][oid_key])

        # Test that we are getting the correct OID
        results = testobj.portduplex(oidonly=True)
        self.assertEqual(results, oid)

    def test__portifindex(self):
        """Testing function _portifindex."""
        # Initialize key variables
        oid_key = 'portDuplex'
        oid = '.1.3.6.1.4.1.9.5.1.4.1.1.11'

        # Get results
        testobj = testimport.init_query(self.snmpobj_integer)
        results = testobj._portifindex()

        # Basic testing of results
        for key, value in results.items():
            self.assertEqual(isinstance(key, int), True)
            self.assertEqual(value, self.expected_dict[key][oid_key])

        # Test that we are getting the correct OID
        results = testobj._portifindex(oidonly=True)
        self.assertEqual(results, oid)


if __name__ == '__main__':

    # Do the unit test
    unittest.main()
