from PIL import ImageTk, Image
import tkinter as tk
import random

def crop_dice_images(): 
    image_path = "dice.jpg"
    spritesheet = Image.open(image_path)
    color = "purple"
    
    colors = {
        "red" : 0,
        "gold" : 1,
        "green": 2,
        "blue" : 3,
        "purple": 4,
        "gray" : 5
    }
    w, h = spritesheet.size
    dice_images = []
    
    for i in range(6):
        left = 0 + (i * w//6)
        top = 0 + (colors[color] * h//6)
        right = w//6* (1+i) #w // 6 + (i * w//6)
        bottom = h//6 + (colors[color] * h//6)
    
        red_die = spritesheet.crop((left, top, right, bottom))
        dice_images.append(ImageTk.PhotoImage(red_die))
    return dice_images
    
class Die:
    IMAGES = crop_dice_images()
    turn = 0

    def __init__(self, window, position, label):
        self.position = position
        self.value = None
        self.holding = tk.BooleanVar(value=False)
        self.image = None
        self.label = label
        self.checkbutton = tk.Checkbutton(
            window,
            text="Hold",
            variable=self.holding
        )
        
       
    def roll(self):
        self.value = random.randint(1,6)
        self.image = self.IMAGES[self.value -1] # Because index 0 has the picure with one dot
        print(self.value)
        if self.label:
            self.label["image"] = self.image
            self.label.grid(column=self.position, row=2)
        self.checkbutton.grid(column=self.position, row=3)