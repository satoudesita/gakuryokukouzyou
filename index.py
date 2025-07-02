from PIL import Image
import pyocr
# import cv2
# from google.colab.patches import cv2_imshow
import pyocr.builders
import requests
from io import BytesIO

# pyocrが使えることを確認する
tools = pyocr.get_available_tools()
# tesseractのみダウンロードしたため0番目を指定
tool = tools[0]
print(tool.get_name())
# Tesseract (sh)と出力されればOK
img1_path = "https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F2418172%2Fa0c5fdfe-64c8-38b6-c5e8-6c4995dc10a0.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=94584b0a6add13056b9a6ad31724c8c5"
img1 = Image.open(img1_path)
img1
txt1 = tool.image_to_string(
    img1,
    lang='jpn+eng',
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)

print(txt1)
