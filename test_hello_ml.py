"""
hello_ml.pyのユニットテスト
"""

import unittest
import numpy as np
from hello_ml import simple_linear_regression


class TestSimpleLinearRegression(unittest.TestCase):
    """線形回帰のテストケース"""

    def test_regression_returns_tuple(self):
        """回帰関数が2つの値を返すことを確認"""
        result = simple_linear_regression()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

    def test_regression_values_are_numbers(self):
        """回帰の結果が数値であることを確認"""
        slope, intercept = simple_linear_regression()
        self.assertIsInstance(slope, (int, float, np.number))
        self.assertIsInstance(intercept, (int, float, np.number))

    def test_regression_values_reasonable(self):
        """回帰の結果が理論値に近いことを確認"""
        slope, intercept = simple_linear_regression()
        # 理論値: y = 2x + 1
        # ノイズがあるので許容範囲を設定
        self.assertAlmostEqual(slope, 2.0, delta=0.5)
        self.assertAlmostEqual(intercept, 1.0, delta=1.0)


if __name__ == "__main__":
    unittest.main()
