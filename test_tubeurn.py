# test_tubeurn.py
"""
Tests for TubeUrn module.
"""

import unittest
from tubeurn import TubeUrn

class TestTubeUrn(unittest.TestCase):
    """Test cases for TubeUrn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TubeUrn()
        self.assertIsInstance(instance, TubeUrn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TubeUrn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
