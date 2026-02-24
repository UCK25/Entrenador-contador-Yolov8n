# YOLOv8 トレーニング手順

このリポジトリにあるデータセットから YOLOv8 モデル（.pt）を生成する手順です。

前提:
- `data.yaml` がリポジトリルートにある（既に存在します）
- 適切な `torch` ビルド（CUDA/CPU に合わせたもの）をインストールすること

手順 (Windows PowerShell の例):

1. 仮想環境を作成して有効化（任意だが推奨）:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. 依存関係をインストール:

```powershell
# まず torch を環境に合わせてインストールしてください（以下は CPU の例）
pip install torch --index-url https://download.pytorch.org/whl/cpu

# その後、その他の依存をインストール
pip install -r requirements.txt
```

3. トレーニングを実行:

```powershell
python train_yolov8.py
```

短時間で動作確認（すぐに `.pt` を得たい場合）:

train_yolov8.py の `epochs` を `1` に変更して実行すると、1エポックで `runs/ppe-yolov8/weights/` に `best.pt` や `last.pt` が生成されます。

出力ファイル:
- 学習済み重み: `runs/ppe-yolov8/weights/best.pt`（または `last.pt`）

次のステップの提案:
- 本格的な学習を行う（エポック数・バッチサイズ・モデルサイズを調整）
- 学習済み `.pt` をエクスポートして配布する（必要に応じて）
