import unittest
import task
import math


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


if __name__ == '__main__':
    unittest.main()
