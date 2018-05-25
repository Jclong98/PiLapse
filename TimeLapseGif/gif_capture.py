from time import sleep
from picamera import PiCamera
import os
from os import system
import datetime

camera = PiCamera()
camera.resolution = (1024, 768)
#camera.rotation = 180

date = datetime.datetime.now().strftime('%m:%d:%Y_%H:%M:%S')

folder = 'frame_storage_{}'.format(date)
if not os.path.exists(folder):
    os.makedirs(folder)

   
for i in range(96):
    temp = os.popen('vcgencmd measure_temp').readline()
    temp = temp[5:9]
    print(temp)
    image_name = '{0}/image{1:04d}_{2}_{3}.jpg'.format(folder, i, date, temp)
    camera.capture(image_name)
    print("image captured at {}".format(datetime.datetime.now().strftime('%m:%d:%Y_%H:%M:%S')))
    
    sleep(900) #15 minutes
    
    #this would turn off the camera until sunrise
    #if int(datetime.datetime.now().strftime('%H%M')) > 1500:
    #    sleep(36000)

gifname =  "timelapse_" + datetime.datetime.now().strftime('%m:%d:%Y_%H:%M:%S')
print("Creating Gif: {}".format(gifname))
# needs imagemagick to work
system('convert -delay 10 -loop 0 {0}/image*.jpg {0}/{1}.gif'.format(folder, gifname))
print('done')
