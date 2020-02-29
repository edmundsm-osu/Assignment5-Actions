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

    def test_area(self):
        # radius = 1
        expected = math.pi
        self.assertEqual(expected, task.calc_area(1))

        # radius = negative
        self.assertEqual(expected, task.calc_area(-1))

        # radius = (1 / sqrt(pi))
        expected = 1
        self.assertAlmostEqual(expected, task.calc_area(1 / math.sqrt(math.pi)), delta=0.001)

        # radius > 1
        expected = 25 * math.pi
        self.assertEqual(expected, task.calc_area(5))

    def test_first_last(self):
        test_list1 = []
        test_list2 = [1]
        test_list3 = [1, 8]
        test_list4 = [2, 8, -9]
        # check empty list
        self.assertEqual(test_list1, task.first_last(test_list1))
        # check one element list
        self.assertEqual([1, 1], task.first_last(test_list2))
        # check two element list
        self.assertEqual(test_list3, task.first_last(test_list3))
        # check three element list
        self.assertEqual([2, -9], task.first_last(test_list4))

    def test_days_between(self):
        # one simple day apart
        date1 = datetime.date(2020, 2, 28)
        date2 = datetime.date(2020, 2, 27)
        self.assertEqual(1, task.days_between(date1, date2))

        # date swap
        date1 = datetime.date(2020, 2, 27)
        date2 = datetime.date(2020, 2, 28)
        self.assertEqual(1, task.days_between(date1, date2))

        # same date
        date1 = datetime.date(2020, 2, 27)
        date2 = datetime.date(2020, 2, 27)
        self.assertEqual(0, task.days_between(date1, date2))

        # > year off
        date1 = datetime.date(2019, 2, 27)
        date2 = datetime.date(2020, 2, 28)
        self.assertEqual(366, task.days_between(date1, date2))

        # with a leap year
        date1 = datetime.date(2020, 2, 27)
        date2 = datetime.date(2016, 2, 27)
        self.assertEqual(365 * 4 + 1, task.days_between(date1, date2))


if __name__ == '__main__':
    unittest.main()
