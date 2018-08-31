# A script using Pillow to mirror one side of an image, producing hilarious results

from PIL import Image
import os.path

# Intakes file path
filePath = input("enter path to image: ")

# Creates a boolean to check whether image has been successfully modified and should be saved
saveImg = True

# Takes user input for file path and checks if the file existsfilePath = input("enter path to image: ")
if(os.path.isfile(filePath)):
    img = Image.open(filePath)
    # Copies image, flips it, crops out the unneeded side and pastes back onto image
    mirror = img.copy()
    mirror = mirror.transpose(Image.FLIP_LEFT_RIGHT)
    # Allows user to select which side of image to be mirrored
    side = input("which side of the picture should be mirrored? (r/l) ")
    if(side == "l"):
        mirror = mirror.crop((img.size[0]/2, 0, img.size[0], img.size[1]))
        img.paste(mirror, ((int(img.size[0]/2), 0)))
    elif (side == "r"):
        mirror = mirror.crop((0, 0, img.size[0]/2, img.size[1]))
        img.paste(mirror, (0, 0))
    else:
        # Cancels if image side is invalid
        print("please enter a valid side")
        saveImg = False
        
else:
    # Cancels if image does not exist
    print("image does not exist")
    saveImg = False

# Checks that image saving has not been canceled, the saves
if saveImg:
    img.save("mirrored.png")
