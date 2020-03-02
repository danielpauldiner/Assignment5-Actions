import unittest
import task
import math
import datetime


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testradius1(self):
        expected = "Enter a float or int for the radius."
        self.assertEqual(expected, task.areaofcircle("test"))

    def testradius2(self):
        expected = "Enter a positive number for the radius."
        self.assertEqual(expected, task.areaofcircle(0))

    def testradius3(self):
        expected = math.pi * 100
        self.assertEqual(expected, task.areaofcircle(10))

    def testfirstlast1(self):
        expected = "Enter a list."
        self.assertEqual(expected, task.firstlastlist("test"))

    def testfirstlast2(self):
        expected = "Enter a list that isn't empty"
        self.assertEqual(expected, task.firstlastlist([]))

    def testfirstlast3(self):
        expected = [2, 8]
        self.assertEqual(expected, task.firstlastlist([2, 4, 6, 8]))

    def testcalcdate1(self):
        expected = "Enter dates into the function."
        self.assertEqual(expected, task.calcdates("june", "july"))

    def testcalcdate2(self):
        expected = 29
        self.assertEqual(expected, task.calcdates(datetime.date(2020, 3, 1), datetime.date(2020, 2, 1)))


if __name__ == '__main__':
    unittest.main()
