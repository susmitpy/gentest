from unittest import TestCase
from src.pay_handler import PayHandler


class TestPayHandler(TestCase):
    def setUp(self):
        
        self.pay_handler = PayHandler()
    
    
        def test___init__(self):
            

            # Handle keyword arguments

            actual_result = self.pay_handler.__init__()
            
            expected_result = None

            self.assertEqual(actual_result, expected_result)

    
        def test_get_amount(self):
            
            task = None

            # Handle keyword arguments

            actual_result = self.pay_handler.get_amount(task)
            
            expected_result = None

            self.assertEqual(actual_result, expected_result)

    


    def tearDown(self):
        pass
