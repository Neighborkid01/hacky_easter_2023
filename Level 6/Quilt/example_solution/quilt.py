# Importing Image class from PIL module
from PIL import Image
import cv2

image = Image.open(r"../quilt.png")

def split_quilt(rows, cols):
  for i in range(rows):
    for j in range(cols):
      top = 69 * i
      bottom = 69 * (i + 1)
      left = 69 * j
      right = 69 * (j + 1)
      patch = image.crop((left, top, right, bottom))
      patch.save(r"quilt_patches/" + str((i*25)+j).zfill(4) + ".png")

def read_patch(patch_number):
  patch = cv2.imread(r"quilt_patches/" + str(patch_number).zfill(4) + ".png")
  detector = cv2.QRCodeDetector()
  data, _, _ = detector.detectAndDecode(patch)
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