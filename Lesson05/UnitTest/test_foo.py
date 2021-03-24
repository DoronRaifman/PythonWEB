import unittest
from Lesson05.UnitTest.Foo import Foo


class TestFoo(unittest.TestCase):
    def test_add(self):
        foo = Foo(5)
        self.assertEqual(foo.value, 5)
        foo.add(15)
        self.assertEqual(foo.value, 20)

