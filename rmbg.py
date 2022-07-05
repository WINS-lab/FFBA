import cv2
import os
dirs1 = os.listdir("/content/drive/MyDrive/Source1-3/Self-Correction-Human-Parsing/outputs/104")
path = "/content/drive/MyDrive/Source1-3/Self-Correction-Human-Parsing/outputs/104/"
print(dirs1)
for file in dirs1:
  print(str(file))
  crop_image = cv2.imread(path+str(file))
  tmp = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
  _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
  b, g, r = cv2.split(crop_image)
  rgba = [b, g, r, alpha]
  dst = cv2.merge(rgba, 4)
  cv2.imwrite(path+str(file), dst)