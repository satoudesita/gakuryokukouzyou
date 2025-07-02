import easyocr
import cv2
import numpy as np
import requests

# 画像パスまたはURLを入力
path = input("画像ファイルのパスまたはURLを入力してください: ")

# 画像の読み込み（ローカル or URL）
if path.startswith('http'):
    response = requests.get(path)
    img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
else:
    img = cv2.imread(path)

img_1 = img.copy()

# easyocrのReaderを作成（日本語と英語対応）
reader = easyocr.Reader(['ja', 'en'])

# 画像からテキストと座標を抽出
result = reader.readtext(img)

# 読み込んだ文字の結果を出力
print("読み取ったテキスト:")
for i in range(len(result)):
    print(result[i][1])

# 文字ごとに枠を作成
for i in range(len(result)):
    pt1 = tuple(map(int, result[i][0][0]))
    pt2 = tuple(map(int, result[i][0][2]))
    cv2.rectangle(img_1, pt1, pt2, (0,255,0), 3)

# 画像を保存
cv2.imwrite('result.png', img_1)
print("枠付き画像をresult.pngとして保存しました。")
