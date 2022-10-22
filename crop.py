from PIL import Image
import os.path

path = "Screens"
source_directory = os.listdir(path)
target_directory = os.path.join(os.path.abspath(os.getcwd()), "updated")
print(target_directory)


def crop(path, dirs, target_directory):
    for item in dirs:
        fullpath = os.path.join(path, item)
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            # f, e = os.path.splitext(fullpath)
            imCrop = im.crop((0, 0, 974, 691))  # left, top, right, bottom
            # imCrop = im.crop((0, 0, 1920, 920)) #corrected
            upd_path = os.path.join(target_directory, item[:-4])  # remove extension .png
            imCrop.save(upd_path + '_Updated.png', "PNG", quality=100)


crop(path, source_directory, target_directory)
