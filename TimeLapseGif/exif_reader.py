import os
import PIL.Image
import tkinter.filedialog as fd

img_list = []

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

        # this creates a dictionary for each image so that they can be accessed by ['image_name'] or ['exif']
        img_list.append({'image_name':filename, 'exif':exif_data})
        

if __name__ == '__main__':
    get_images()
    
    # this prints the first dictionary of exif data from the exif list
    # print(img_list[0]['exif'])
    
    # printing out each image name, associated with the date it was taken from the exif data
    for image in img_list:
        print(image['image_name'] + "\t" + image['exif'][306])