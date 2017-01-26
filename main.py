"""Version 1.0 of my Picture Indexer script.
This current version combines 3 images together for each folder and names the image the same as the folder.
With the current implementation, you need to specify the number of layers of folders that there are from the given path.
There are no longer any bugs in this program that I am aware of.

Future goals:
Have the program intelligently parse all folders and create thumbnails without being told the number of folder layers.
Create a version with a GUI that will not require the user to have python or pillow installed.
"""

import os
import imghdr
from PIL import Image


# Receives the path and name of the thumbnails folder and then creates a list called folders which contains all folders
# that are in the provided directory. It then returns this list.
def parse_folders(path, thumb_fold_name):
    folders = os.listdir(path)

    # Looks for the thumbnails folder and removes it if found.
    for x in range(len(folders)):
        if folders[x] == thumb_fold_name:
            folders.pop(x)
            break

    return folders


# Performs the same function as parse_folders but returns a list of images instead.
def parse_images(path):
    images = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        images.extend(filenames)
        break

    return images


"""This function is used to dig one layer deeper into the folder structure. If layers is larger than 1, the function
will call itself for each folder present and run the process again with layer being 1 number lower. Once layers becomes
1 it will call final_folder_layer and stop."""
def folder_layer(path, layers, thumb_fold_name):
    folders = parse_folders(path, thumb_fold_name)
    layers -= 1

    if layers == 1:
        for x in range(len(folders)):
            final_folder_layer(path + folders[x] + "/", thumb_fold_name)
    else:
        for x in range(len(folders)):
            folder_layer(path + folders[x] + "/", layers, thumb_fold_name)


# This function determines the images that will be used in the image sheet and passes them to that function.
def final_folder_layer(path, thumb_fold_name):
    folders = parse_folders(path, thumb_fold_name)
    thumb_path = path + thumb_fold_name + "/"

    for x in range(len(folders)):
        # Acquires a list of all image files in the folder
        images = parse_images(path + folders[x])

        # Checks to see if there is more than 10 items in the folder. If there isn't then no image sheet will be created
        if len(images) > 10:
            # Creates the folder that will house the image sheet if one has not already been created.
            os.makedirs(thumb_path, exist_ok=True)
            file_loc = path + folders[x] + "/"
            pic_check = 1

            # Create the initial list of chosen pictures to use.
            pics = [4, int(len(images)/2), -5]
            imgs = ["", "", ""]

            for y in range(len(pics)):
                i = 1
                initial_pic = pics[y]

                """ This loop checks to see if the item at the specified location is actually a picture. If it is not,
                then it will iterate the pointer by 1 and then check again to see if the new item is an image.
                This will run infinitely until an image file is found or until all files have been checked."""
                while i == 1 & pic_check == 1:
                    imgs[y] = file_loc + images[pics[y]]
                    if str(imghdr.what(imgs[y])) != "None":
                        i = 0
                    else:
                        pics[y] += 1
                        if pics[y] == int(len(images)):
                            pics[y] = 0
                        elif pics[y] == initial_pic:
                            i = 0
                            pic_check = 0

            # Ensures a image sheet is only created if there a image files in the folder.
            if pic_check == 1:
                sheet_name = thumb_path + folders[x]
                image_sheet_creator(imgs[0], imgs[1], imgs[2], sheet_name)


# Receives the image file paths and then creates an image sheet from them.
def image_sheet_creator(img1, img2, img3, sheet_name):
    images = list(map(Image.open, [img1, img2, img3]))
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0

    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.save(sheet_name+'.jpg')


def main():
    # The name of the folder where all image sheets will be placed.
    thumb_fold_name = "Album Previews"
    path = input("Please state the directory you would like to parse thumbnails for:\n")

    # Adds a closing forward slash if none exists.
    if path[-1] != "/":
        path += "/"

    layers = input("Please state the number of subdirectories there are:\n")

    # Converts layers from a string to an int.
    layers = int(layers)

    if layers == 1:
        final_folder_layer(path, thumb_fold_name)

    if layers > 1:
        folder_layer(path, layers, thumb_fold_name)


main()