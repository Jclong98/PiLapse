import os
import imageio as io
import tkinter.filedialog as fd

def create_gif():
    root = fd.Tk()
    root.withdraw()
    path = fd.askdirectory()

    with io.get_writer(path + "/" + 'PiLapse.gif', mode='I', duration=0.15) as writer:
        for filename in os.listdir(path):
            image = io.imread(path + "/" + filename)
            writer.append_data(image)
    writer.close()

if __name__ == '__main__':
    create_gif()
