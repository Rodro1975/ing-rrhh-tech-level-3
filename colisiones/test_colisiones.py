import unittest
from colisiones import f

class TestColisiones(unittest.TestCase):
    
    def test_cases(self):
        self.assertEqual(f('LR'), '0 0')
        self.assertEqual(f('RL'), '1 1')
        self.assertEqual(f('RRR'), '0 0 0')
        self.assertEqual(f('RRL'), '1 2 1')
        # Agrega más casos de prueba aquí

if __name__ == '__main__':
    unittest.main()
