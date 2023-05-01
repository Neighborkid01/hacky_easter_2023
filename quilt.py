# Importing Image class from PIL module
from PIL import Image
import cv2

# Opens a image in RGB mode
image = Image.open(r"/Users/razor_crest/Documents/GitHub/hacky_easter_2023/quilt.png")

def split_quilt(rows, cols):
  for i in range(rows):
    for j in range(cols):
      top = 69 * i
      bottom = 69 * (i + 1)
      left = 69 * j
      right = 69 * (j + 1)
      patch = image.crop((left, top, right, bottom))
      patch.save(r"/Users/razor_crest/Documents/GitHub/hacky_easter_2023/quilt_cropped/" + str((i*25)+j).zfill(4) + ".png")

def read_patch(patch_number):
  patch = cv2.imread(r"/Users/razor_crest/Documents/GitHub/hacky_easter_2023/quilt_cropped/" + str(patch_number).zfill(4) + ".png")
  detector = cv2.QRCodeDetector()
  data, bbox, straight_qrcode = detector.detectAndDecode(patch)
  return data

def read_quilt(patches):
  quilt = []
  for i in range(patches):
    quilt.append(read_patch(i))
  return quilt

rows = 28
cols = 25
split_quilt(rows, cols)
print("".join(read_quilt(rows*cols)))