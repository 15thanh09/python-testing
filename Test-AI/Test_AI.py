import Test_Cancer_BvsM as ai_cancer
import unittest


class Test_AI(unittest.TestCase):
    def test_AI_cancer(self): 
        actual = ai_cancer.evaluate()
        expected = 0.9
        msg = "expected is : {:.2f}, actual is : {:.2f}".format(expected, actual)
        self.assertGreater(actual, expected, msg)