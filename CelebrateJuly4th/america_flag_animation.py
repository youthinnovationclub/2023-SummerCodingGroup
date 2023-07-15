"""
Hello. This script is a rotating display of images in pictures.

Pictures must have the file name 'picture_X.jpg' where X is a number. 
The first picture file should be 'picture_1.jpg'.
"""

from tkinter import *
from PIL import ImageTk,Image  


# Settings
PICTURE_FILE_EXTENSION = ".jpg"
NUMBER_OF_IMAGES = 4
WINDOW_HEIGHT = 800 # This is in pixels
WINDOW_WIDTH = 800 # This is in pixels
TIME_BETWEEN_PHOTOS = 500 # This is in seconds.
NUMBER_OF_ANIMATIONS = 100

def main():
    root = Tk()
    canvas = Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.pack()
    images = setup_images()
    canvas.create_image(0,0,anchor=NW, image=images[0], tag='img1')
    canvas.delete('img1')
    update_images(root, canvas, images)
    root.mainloop()
    

def update_images(root, canvas, images, current_image=1, i=0):
    '''
    Rotate images
    '''

    if i <= NUMBER_OF_ANIMATIONS:
        # Delete Image
        canvas.delete(f'img{current_image}')

        # Update Image
        if current_image == len(images):
            # First Image
            canvas.create_image(0,0,anchor=NW, image=images[0], tag='img1')
            new_image = 1    
        else:
            # Second Image
            new_image = current_image + 1
            canvas.create_image(0,0,anchor=NW, image=images[new_image-1], tag=f'img{new_image}')
    
        root.after(TIME_BETWEEN_PHOTOS,update_images, root, canvas, images, new_image, i+1)


def setup_images():
    '''
    Loads all images
    '''
    images = []
    for i in range(1,NUMBER_OF_IMAGES+1):
        images.append(
            ImageTk.PhotoImage(
                Image.open(f"pictures/picture_{i}{PICTURE_FILE_EXTENSION}")))
    return images
    
if __name__ == "__main__":
    main()