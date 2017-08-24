import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from skimage import data
from skimage.feature import register_translation
from skimage.feature.register_translation import _upsampled_dft
from scipy.ndimage import fourier_shift

%matplotlib inline

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

arr = []
arr = np.loadtxt('bigimg.txt')
ax1.set_title("Total NV")
ax1.imshow(arr, extent = [0,5, 0, 5])

arr1 = []
arr1 = np.loadtxt('smallimg.txt')
ax2.set_title("Target NVs")
ax2.imshow(arr1, extent = [0,5,0,5])



def






plt.tight_layout()
plt.show()