import unittest
import lab5 as prog

class TestMyProgram(unittest.TestCase):
    def test_EngineType(self):
        vios = prog.Vehicle('4','petrol',5,180)
        self.assertEqual(vios.tank, 'petrol')

if __name__ == '__main__':
    unittest.main()
