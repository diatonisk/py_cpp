
import unittest
from py_cpp import Mod
from py_cpp import add


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

    def test_add(self):
        """Verify CPP function add works as expected."""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 123), 128)


if __name__ == '__main__':
    unittest.main()
