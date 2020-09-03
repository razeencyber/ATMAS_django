import os
import numpy as np
import cv2
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, "images")

def getImagesWithID(path):
	imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
	
	faces = []
	Ids = []
	for imagePath in imagePaths:
		faceImg = Image.open(imagePath).convert('L')
		size = (550, 550)
		final_image = faceImg.resize(size, Image.ANTIALIAS)
		image_array = np.array(final_image, "uint8")
		ID = int(os.path.split(imagePath)[-1].split('.')[1])
		#print(image_array)
		Ids.append(ID)
		faces.append(image_array)
		cv2.imshow("training", image_array )
		cv2.waitKey(10)
	return np.array(Ids), np.array(faces)
ids, faces = getImagesWithID(path)
print(ids)
recognizer.train(faces, ids)

recognizer.save(BASE_DIR + '/trainer.yml')
cv2.destroyAllWindows()
