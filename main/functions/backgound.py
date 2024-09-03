# import 3rd part libs
import tkinter
import pygame
from pygame.locals import *

#getting screen size
app = tkinter.Tk()
W = app.winfo_screenwidth()
H = app.winfo_screenheight()

#init screen
screen = pygame.display.set_mode((W,H))

#images path
image_path = r"C:\Users\joss\Downloads\tower-game-main\tower-game-main\main\assets\background0.png"

#loads selected image from image path
def background(image,W,H,screen):
    #loads the image
    image = pygame.image.load(image_path)
    #scales the image to fit the screen, even tho all back ground art will be made for 16:9 ratio
    scaled_image = pygame.transform.scale(image, (W, H))
    #draws the the screen
    screen.blit(scaled_image, (0, 0))


