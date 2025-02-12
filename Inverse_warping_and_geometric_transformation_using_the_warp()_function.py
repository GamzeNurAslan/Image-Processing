import cv2
from skimage import io
import numpy as np
from matplotlib import pyplot as plt
from skimage.transform import swirl, SimilarityTransform, warp

im = io.imread("../images/yzx.jpg")

tform = SimilarityTransform(scale=0.9,
rotation=np.pi/4,translation=(im.shape[0]/2, -100))
warped = warp(im, tform)

import matplotlib.pyplot as plt
plt.imshow(warped), plt.axis('off'), plt.show()
