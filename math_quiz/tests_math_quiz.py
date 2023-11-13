import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        """Test if random numbers generated are within the specified range."""
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        """Test if the result is one of the specified operators."""
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            operator = function_B()
            self.assertIn(operator, operators)

    def test_function_C(self):
        """Test the correctness of function_C for various scenarios."""
        test_cases = [
            (5, 2, '+', '5+2', 7),
            (3, 4, '*', '3*4', 12),
            (10, 7, '-', '10-7', 3),
            # Add more test cases
            (1, 5, '*', '1*5', 5),
            (8, 2, '+', '8+2', 10),
            (6, 3, '-', '6-3', 3),
        ]

        for numb1, numb2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = function_C(numb1, numb2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
