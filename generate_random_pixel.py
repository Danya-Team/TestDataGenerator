import numpy as np
from PIL import Image

arr = np.random.randint(low = 0, high = 255, size = (4201, 2401, 3))

im = Image.fromarray(arr.astype('uint8'))
im.save("image.png")
im.show()
