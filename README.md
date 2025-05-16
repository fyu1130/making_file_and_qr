# make_qr_and_file

社員名簿から社員IDをもとにQRコードを生成し、ローマ字ディレクトリを作成して格納するPythonスクリプトです。

## ✅ 実行環境

1. Ubuntu 22.04 以降
2. Python 3.12.4
3. 必要ライブラリ（requirements.txtに記載）

---

## ✅ 準備手順

### 1. Pythonのインストール（Ubuntuの場合）

Ubuntu 22.04 では python3 が標準です。以下で `python` コマンドも有効化できます：

```bash
sudo apt update
sudo apt install -y python-is-python3
```

---

### 2. 必要ライブラリのインストール

```bash
pip install -r requirements.txt
```

---

### 3. ディレクトリ構成（初期状態）

```
.
├── README.md
├── main.py
├── people_list.xlsx
├── requirements.txt
└── .gitignore
```

---

## ✅ 使用方法

1. `people_list.xlsx` に以下の列を持つ社員データを記述します：

| 社員名（漢字） | 社員名（ひらがな） | 社員ID |
|----------------|--------------------|--------|
| 山田 太郎     | やまだ たろう      | EMP0001 |

2. スクリプトを実行：

```bash
python main.py
```

3. 処理内容：

- `output/firstname_lastname/` ディレクトリをローマ字で作成
- 社員IDをQRコードとして生成し、PNGで保存
- QRコードファイルのパスを `people_list_with_qr.xlsx` に追記出力

---

## ✅ セキュリティ注意点

- `output/` や `people_list_with_qr.xlsx` は `.gitignore` に追加済み
- 個人情報や社員データの取り扱いにはご注意ください

---

## ✅ 今後の改善案

- 氏名の漢字→ローマ字変換をAIベースで対応
- QRコードに社員情報全体を含める
- Excelのフォーマットチェックを自動化
