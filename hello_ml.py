"""
シンプルな機械学習デモスクリプト
"""

import numpy as np
import matplotlib.pyplot as plt

def simple_linear_regression(visualize=False):
    """
    簡単な線形回帰のデモ
    
    Args:
        visualize (bool): Trueの場合、結果をプロット表示
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

    # 可視化オプション
    if visualize:
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, alpha=0.5, label='データ点')
        plt.plot(x, slope * x + intercept, 'r-', label=f'回帰直線: y = {slope:.2f}x + {intercept:.2f}')
        plt.plot(x, 2 * x + 1, 'g--', label='理論値: y = 2.00x + 1.00')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('線形回帰デモ')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig('regression_plot.png', dpi=100, bbox_inches='tight')
        print("グラフを regression_plot.png に保存しました")
        plt.close()

    return slope, intercept

if __name__ == "__main__":
    import sys
    
    print("=== 簡単な線形回帰デモ ===")
    
    # コマンドライン引数で可視化オプションを制御
    visualize = '--visualize' in sys.argv or '-v' in sys.argv
    
    if visualize:
        print("可視化モードで実行します")
    
    simple_linear_regression(visualize=visualize)
