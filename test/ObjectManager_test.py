import unittest

# import selected elements, ex.:
from src.App.Environment.ObjectManager import *


class IDTagTests(unittest.TestCase):
    def test_get_id(self):  # a == b
        OM = ObjectManager()
        id1 = OM.get_id()
        id2 = OM.get_id()
        self.assertEqual(id1, 1)
        self.assertEqual(id2, 1)

    # def test_assert_equal(self):  # a == b
    #     one = 1
    #     self.assertEqual(one, 1)
    #
    # def test_assert_is(self):  # a is b
    #     one = 1
    #     self.assertIs(one, 1)
    #
    # def test_assert_in(self):  # a is in b
    #     elem = 2
    #     store = [1, 2]
    #     self.assertIn(elem, store)
    #
    # def test_assert_is_instance(self):  # isinstance(a, b)
    #     dronelib = DroneLib()
    #     self.assertIsInstance(dronelib, DroneLib)
    #
    # def test_assert_true(self):  # bool(x) is True
    #     one = 1
    #     self.assertTrue(one)
    #
    # def test_assert_false(self):  # bool(x) is False
    #     zero = 0
    #     self.assertFalse(zero)
    #
    # def test_assert_raises(self):  # fun(*args, **kwargs) raises exc
    #     one = 1
    #     zero = 0
    #     with self.assertRaises(ZeroDivisionError):
    #          one / zero


if __name__ == '__main__':
    unittest.main()
