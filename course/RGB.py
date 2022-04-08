import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
file_path = r'C:\Users\samee\Masters Internship\course_material\course_material\excercises\d1\marsflagge.jpg'
rgb_img = np.array(Image.open(file_path))
plt.imshow(rgb_img)
plt.show()

#Red channel
plt.imshow(rgb_img [:,:,0],cmap='gray')
plt.show()

# Green channel
plt.imshow(rgb_img [:,:,1],cmap='gray')
plt.show()

# Blue channel
plt.imshow(rgb_img [:,:,2],cmap='gray')
plt.show()

