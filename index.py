from PIL import Image, ImageFilter
import os

input_path = "input"
outputPath = "output"

files = []
for element in os.listdir(input_path):
    if os.path.isfile(os.path.join(input_path, element)):
        files.append(os.path.join(input_path, element))


for file_name in files:
    im = Image.open(file_name)
    im.show()

    # width, height = im.size

    # print(im.size)

    # im_sharp = im.resize((int(width/2), int(height/2)))

    # im_sharp.save('input/'+image_name, 'JPEG')

    # im_sharp.show()