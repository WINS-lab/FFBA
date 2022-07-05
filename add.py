from PIL import Image 
import os 
dirs1 = os.listdir("/content/drive/MyDrive/Source1-3/Self-Correction-Human-Parsing/outputs/104")
dirs2 = os.listdir("/content/drive/MyDrive/Source1-3/Self-Correction-Human-Parsing/inputs/PRCCv2/104v2")
path1 = "/content/drive/MyDrive/Source1-3/Self-Correction-Human-Parsing/inputs/PRCCv2/104v2/"
path2 = "/content/drive/MyDrive/Source1-3/Self-Correction-Human-Parsing/outputs/104/"
for file in dirs2:
  print(str(file))
  imageA = Image.open(path1+str(file))
  file = str(file).replace("jpg","png")
  print(str(file))
  imageA.save(path1+str(file))
for file in dirs1:
  
  imageA = Image.open(path1+file)
  imageA = imageA.convert('RGBA')
  widthA , heightA = imageA.size

  imageB = Image.open(path2+file)
  imageB = imageB.convert('RGBA')
  widthB , heightB = imageB.size

  imageB_size = imageB.resize((widthB, heightB))

  resultPicture = Image.new('RGBA', imageA.size, (0, 0, 0, 0))
  resultPicture.paste(imageA,(0,0))
  right_bottom = (widthA - widthB, heightA - heightB)
  resultPicture.paste(imageB_size, right_bottom, imageB_size)


  resultPicture.save("/content/drive/MyDrive/Source1-3/Self-Correction-Human-Parsing/Final/104/"+file)
  print(str(file)+" done")

