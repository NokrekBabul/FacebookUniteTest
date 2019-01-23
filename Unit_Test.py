import unittest
from UnitTestExamples import Examples


class MyTestCase(unittest.TestCase):
    def test_add(self):
        result = Examples.add(self, 200, 100)
        self.assertEqual(result, 300)

    def test_sub(self):
        result = Examples.sub(self, 200, 100)
        self.assertEqual(result, 100)



# if __name__ == '__main__':
#     unittest.main()
