#!/usr/bin/python3

"""
unit test for basemodel
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class test_basemodel(unittest.TestCase):
    """Test cases for the BaseModel class"""
    def test_class_documentation(self):
        """Fails if BaseModel class is not documented"""
        self.assertGreater(len(BaseModel.__doc__), 1)
    
    def test_to_dict(self):
        """Fails if expected dict does not match basemodel dict"""
        baseModel = BaseModel()
        
        result_dict = baseModel.to_dict()
        
        self.assertIn('ids', result_dict)
        self.assertIsInstance(result_dict['id'], str)
        
        self.assertIn('created_at', result_dict)
        self.assertIsInstance(result_dict['created_at'], datetime)
        
        self.assertEqual(result_dict['id'], baseModel.id)
        self.assertEqual(result_dict['created_at'], baseModel.created_at)