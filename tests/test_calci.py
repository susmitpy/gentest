
from unittest import TestCase
from examples.calci import Calci, StringCalci


class TestCalci(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.calci = Calci()
    
    
    def test___init__(self):
        """ Test initialiser """
        self.obj = Calci()
    
    
    
    def test_add(self):
        
        a = None
        b = None
        actual_result = self.calci.add(a, b)
        expected_result = None
        self.assertEqual(actual_result, expected_result)
    
    
    
    def test_sub(self):
        
        a = None
        b = None
        actual_result = self.calci.sub(a, b)
        expected_result = None
        self.assertEqual(actual_result, expected_result)
    
    
    def tearDown(self):
        """ Destroy objects after each test """

class TestStringCalci(TestCase):
    def setUp(self):
        """ Set up objects for each test """
        
        self.string_calci = StringCalci()
    
    
    def test_concat(self):
        
        a = None
        b = None
        actual_result = self.string_calci.concat(a, b)
        expected_result = None
        self.assertEqual(actual_result, expected_result)
    
    
    
    def test_repeat(self):
        
        a = None
        b = None
        actual_result = self.string_calci.repeat(a, b)
        expected_result = None
        self.assertEqual(actual_result, expected_result)
    
    
    def tearDown(self):
        """ Destroy objects after each test """
