import os
import imageio

myfiles = os.listdir('assignment8/Images')

images = []
for i in range(len(myfiles)):
    image = imageio.imread('assignment8/Images/' + myfiles[i])
    images.append(image)
    
imageio.mimsave('assignment8/ghese-haye-mano-babam.gif', images)