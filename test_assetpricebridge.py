# test_assetpricebridge.py
"""
Tests for AssetPriceBridge module.
"""

import unittest
from assetpricebridge import AssetPriceBridge

class TestAssetPriceBridge(unittest.TestCase):
    """Test cases for AssetPriceBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AssetPriceBridge()
        self.assertIsInstance(instance, AssetPriceBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AssetPriceBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
