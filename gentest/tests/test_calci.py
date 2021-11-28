from unittest import TestCase
from src.calci import Calci, StringCalci


class TestCalci(TestCase):
    def setUp(self):
        
        self.calci = Calci()
    
    
        def test_add(self):
            
            a = None
            b = None

            # Handle keyword arguments

            actual_result = self.calci.add(a, b)
            
            expected_result = None

            self.assertEqual(actual_result, expected_result)

    
        def test_sub(self):
            
            a = None
            b = None

            # Handle keyword arguments

            actual_result = self.calci.sub(a, b)
            
            expected_result = None

            self.assertEqual(actual_result, expected_result)

    


    def tearDown(self):
        pass

class TestStringCalci(TestCase):
    def setUp(self):
        
        self.string_calci = StringCalci()
    
    
        def test_concat(self):
            
            a = None
            b = None

            # Handle keyword arguments

            actual_result = self.string_calci.concat(a, b)
            
            expected_result = None

            self.assertEqual(actual_result, expected_result)

    
        def test_repeat(self):
            
            a = None
            b = None

            # Handle keyword arguments

            actual_result = self.string_calci.repeat(a, b)
            
            expected_result = None

            self.assertEqual(actual_result, expected_result)

    


    def tearDown(self):
        pass
