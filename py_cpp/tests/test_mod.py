
import unittest
from py_cpp import Mod
class TestMod(unittest.TestCase):

    def test_get(self):
        """Verify we can retrieve the class property."""
        a = 5
        m = Mod(a)
        self.assertEqual(m.dummy, a)

    def test_set(self):
        """Verify we can set the class property."""
        a = 5
        m = Mod(3)
        m.dummy = a
        self.assertEqual(m.dummy, a)

if __name__ == '__main__':
    unittest.main()