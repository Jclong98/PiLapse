import os
import PIL.Image
import tkinter.filedialog as fd

img_list = []
exif_list = []

def get_images():
    # asking where the images are stored
    root = fd.Tk()
    root.withdraw()
    path = fd.askdirectory()

    # adding each image name to the img_list and adding the exif data of 
    # each image to the exif_list
    for filename in os.listdir(path):
        img = PIL.Image.open(path + "/" + filename)
        exif_data = img._getexif()

        img_list.append(filename)
        exif_list.append(exif_data)

if __name__ == '__main__':
    get_images()
    
    # this prints the first dictionary of exif data from the exif list
    # print(exif_list[0])

    # printing out each image name, associated with the date it was taken from the exif data
    for i in range(len(img_list)):
        print(img_list[i] + "\t" + exif_list[i][306])