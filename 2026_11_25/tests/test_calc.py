import unittest

from calc import divide


class TestCalc(unittest.TestCase):
    def test_divide_normal(self) -> None:
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(-9, 3), -3.0)
        self.assertAlmostEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(0, 5), 0.0)

    def test_divide_by_zero_raises_value_error(self) -> None:
        for zero in (0, 0.0):
            with self.subTest(divisor=zero):
                with self.assertRaises(ValueError) as ctx:
                    divide(10, zero)
                self.assertEqual(str(ctx.exception), "除數不可為零")


if __name__ == "__main__":
    unittest.main()
