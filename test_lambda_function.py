import unittest
from lambda_function import add
# lambda_function.py

# Define a basic lambda function

# Unit test cases for the lambda function

class TestLambdaFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), 3)
    
    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 2), 1)
    
    def test_add_zeros(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()