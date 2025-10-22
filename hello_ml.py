"""
シンプルな機械学習デモスクリプト
"""

import numpy as np

def simple_linear_regression():
    """
    簡単な線形回帰のデモ
    """
    # サンプルデータの生成
    np.random.seed(42)
    x = np.linspace(0, 10, 50)
    y = 2 * x + 1 + np.random.randn(50) * 2

    # 最小二乗法で係数を計算
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)

    slope = numerator / denominator
    intercept = y_mean - slope * x_mean

    print(f"回帰直線: y = {slope:.2f}x + {intercept:.2f}")
    print(f"理論値: y = 2.00x + 1.00")

    return slope, intercept

if __name__ == "__main__":
    print("=== 簡単な線形回帰デモ ===")
    simple_linear_regression()
