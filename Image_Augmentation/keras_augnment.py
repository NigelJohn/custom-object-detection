from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import array_to_img, img_to_array, load_img

img_generator = ImageDataGenerator(rotation_range=40, 
                                   width_shift_range=0.2,
                                   height_shift_range=0.2, 
                                   shear_range=0.2,
                                   zoom_range=0.2, 
                                   channel_shift_range=4.,
                                   horizontal_flip=True, 
                                   vertical_flip=True,
                                   fill_mode='nearest')


import os
import glob

new_dicrectory = r"C:\Users\prati\OneDrive\Desktop\Custon_Object_Detection_GUI\Image_Capturing\images"
os.chdir(new_dicrectory)
img_path = glob.glob("*.jpg")

print("Images found: ",len(img_path))

for i in range(len(img_path)):
    ig = img_path[i]
    print(ig)

    img = load_img(ig)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    i = 0
    for batch in img_generator.flow(x,batch_size =1,save_to_dir="preview",save_prefix="cat",save_format="jpg"):
        i+= 1

        if i > 20:
            break
