import easyocr
import cv2
import numpy as np
import requests

path = input("画像ファイルのパスまたはURLを入力してください: ")

if path.startswith('http'):
    response = requests.get(path)
    img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
else:
    img = cv2.imread(path)

img_1 = img.copy()

reader = easyocr.Reader(['ja', 'en'])

result = reader.readtext(img)

print("読み取ったテキスト:")
for i in range(len(result)):
    print(result[i][1])

for i in range(len(result)):
    pt1 = tuple(map(int, result[i][0][0]))
    pt2 = tuple(map(int, result[i][0][2]))
    cv2.rectangle(img_1, pt1, pt2, (0,255,0), 3)

# 画像を保存
cv2.imwrite('result.png', img_1)
print("枠付き画像をresult.pngとして保存しました。")
