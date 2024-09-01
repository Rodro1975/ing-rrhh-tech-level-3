import unittest
from colisiones import f

class TestColisiones(unittest.TestCase):
    """
    Test class for function `f` of module `collisions`.
    Use the `unittest` module to define and execute test cases.
    """
    def test_cases(self):
        self.assertEqual(f('LR'), '0 0')
        self.assertEqual(f('RL'), '1 1')
        self.assertEqual(f('RRR'), '0 0 0')
        self.assertEqual(f('RRL'), '1 2 1')
        # Add more test cases here

if __name__ == '__main__':
    unittest.main()
