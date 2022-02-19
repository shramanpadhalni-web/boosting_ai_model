# -*- coding: utf-8 -*-
import unittest
import boosting_ai_model.models.deep_api as deep_api

class TestModelMethods(unittest.TestCase):
    
    def setUp(self):
        self.meta = deep_api.get_metadata()
        
    def test_model_metadata_type(self):
        """
        Test that get_metadata() returns dict
        """
        self.assertTrue(type(self.meta) is dict)
        
    def test_model_metadata_values(self):
        """
        Test that get_metadata() returns right values (subset)
        """
        self.assertEqual(self.meta['name'].lower().replace('-','_'),
                        'boosting_ai_model'.lower().replace('-','_'))
        self.assertEqual(self.meta['author'].lower(),
                         'Hem Chandra'.lower())
        self.assertEqual(self.meta['author-email'].lower(),
                         'sh@xyz.com'.lower())
        self.assertEqual(self.meta['license'].lower(), 
                         'No license file'.lower())


if __name__ == '__main__':
    unittest.main()
