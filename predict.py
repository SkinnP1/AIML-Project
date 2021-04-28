from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import sys

# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(224, 224))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 224, 224, 3)
	# center pixel data
	img = img.astype('float32')
	img = img - [123.68, 116.779, 103.939]
	return img


 
# entry point, run the example
filename = str(sys.argv[1])
# load the image
img = load_image(filename)
# load model
model = load_model('model.h5')
# predict the class
result = model.predict(img)
if result[0]==1:
	print("dog")
else :
	print("cat")
