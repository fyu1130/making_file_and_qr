import os
import pandas as pd
import qrcode
from romkan import to_roma

# 入力ファイル設定
excel_file = "people_list.xlsx"
sheet_name = "Sheet1"
output_dir = "output"

# Excelファイル読み込み
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# QRコードの保存パス列を追加
qr_paths = []

# 出力ディレクトリ作成
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 各社員データの処理
for idx, row in df.iterrows():
    kanji_name = row['社員名（漢字）']
    kana_name = row['社員名（ひらがな）']
    emp_id = str(row['社員ID'])

    kana_split = kana_name.split(" ")
    first = kana_split[1] if len(kana_split) > 1 else kana_split[0]
    last = kana_split[0] if len(kana_split) > 1 else ""
    romaji_name = f"{to_roma(first)}_{to_roma(last)}".lower()

    emp_dir = os.path.join(output_dir, romaji_name)
    os.makedirs(emp_dir, exist_ok=True)

    qr_img = qrcode.make(emp_id)
    qr_filename = f"{emp_id}_qr.png"
    qr_path = os.path.join(emp_dir, qr_filename)
    qr_img.save(qr_path)

    qr_paths.append(qr_path)

# ExcelにQRコードパス列を追加して保存
df["QRコードパス"] = qr_paths
df.to_excel("people_list_with_qr.xlsx", index=False)

print("QRコードの作成とExcelへの出力が完了しました。")
