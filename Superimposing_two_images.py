import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im1 = Image.open("../images/yz.png")
im2 = Image.open("../images/me.png").convert('RGB').resize((im1.width, im1.height))

im1_np = np.array(im1)
im2_np = np.array(im2)

result = cv2.multiply(im1_np, im2_np)

plt.figure(figsize=(10, 10))
plt.imshow(result)
plt.axis('off')
plt.title("Result of cv2.multiply")
plt.show()
