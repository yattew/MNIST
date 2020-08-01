import pickle
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open('test.jpg')
image = image.convert('1')
image = image.resize((28,28))
np_image = np.asarray(image)
with open('model (2).bin','rb') as f:
    model = pickle.load(f)
# plt.imshow(np_image)
# plt.show()
print(model.predict([np_image.flatten()]))