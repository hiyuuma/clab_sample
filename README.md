# clab_sample
サンプルノートブックです。

## 概要
このリポジトリは、Google Colaboratory と GitHub の連携方法を学ぶためのサンプルプロジェクトです。

## 内容
- `github.ipynb`: ColabとGitHubの連携についての説明と、CIFAR-10データセットを使ったCNNのサンプルコード
- `hello_ml.py`: シンプルな線形回帰のデモスクリプト（可視化オプション付き）
- `test_hello_ml.py`: hello_ml.pyのユニットテスト

## 必要なライブラリ
- numpy
- keras
- matplotlib (github.ipynbで使用)

## 使い方
1. Google Colaboratoryで `github.ipynb` を開く
2. ローカルで実験する場合は `hello_ml.py` を実行

```bash
# 必要なライブラリをインストール
pip install numpy matplotlib

# スクリプトを実行（標準モード）
python hello_ml.py

# スクリプトを実行（可視化モード）
python hello_ml.py --visualize

# ユニットテストを実行
python -m unittest test_hello_ml.py
```
