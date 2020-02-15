'''
After having incredibly slow programs I present:

 _____ ______   ___  ________   _______   ________  ________  ________  ________ _________                    
|\   _ \  _   \|\  \|\   ___  \|\  ___ \ |\   ____\|\   __  \|\   __  \|\  _____\\___   ___\                  
\ \  \\\__\ \  \ \  \ \  \\ \  \ \   __/|\ \  \___|\ \  \|\  \ \  \|\  \ \  \__/\|___ \  \_|                  
 \ \  \\|__| \  \ \  \ \  \\ \  \ \  \_|/_\ \  \    \ \   _  _\ \   __  \ \   __\    \ \  \                   
  \ \  \    \ \  \ \  \ \  \\ \  \ \  \_|\ \ \  \____\ \  \\  \\ \  \ \  \ \  \_|     \ \  \                  
   \ \__\    \ \__\ \__\ \__\\ \__\ \_______\ \_______\ \__\\ _\\ \__\ \__\ \__\       \ \__\                 
    \|__|     \|__|\|__|\|__| \|__|\|_______|\|_______|\|__|\|__|\|__|\|__|\|__|        \|__|    (bedrock)          
                                                                                                              
                                                                                                              
                                                                                                              
 ___  _____ ______   ________  ________  _______           _________  ________                                
|\  \|\   _ \  _   \|\   __  \|\   ____\|\  ___ \         |\___   ___\\   __  \                               
\ \  \ \  \\\__\ \  \ \  \|\  \ \  \___|\ \   __/|        \|___ \  \_\ \  \|\  \                              
 \ \  \ \  \\|__| \  \ \   __  \ \  \  __\ \  \_|/__           \ \  \ \ \  \\\  \                             
  \ \  \ \  \    \ \  \ \  \ \  \ \  \|\  \ \  \_|\ \           \ \  \ \ \  \\\  \                            
   \ \__\ \__\    \ \__\ \__\ \__\ \_______\ \_______\           \ \__\ \ \_______\                           
    \|__|\|__|     \|__|\|__|\|__|\|_______|\|_______|            \|__|  \|_______|                           
                                                                                                              
                                                                                                              
                                                                                                              
 ________  ___       ________  ________  ___  __            ___  ___  ___   _________  ________  ________     
|\   __  \|\  \     |\   __  \|\   ____\|\  \|\  \         |\  \|\  \|\  \ |\___   ___\\   __  \|\   __  \    
\ \  \|\ /\ \  \    \ \  \|\  \ \  \___|\ \  \/  /|_       \ \  \\\  \ \  \\|___ \  \_\ \  \|\  \ \  \|\  \   
 \ \   __  \ \  \    \ \  \\\  \ \  \    \ \   ___  \       \ \  \\\  \ \  \    \ \  \ \ \   _  _\ \   __  \  
  \ \  \|\  \ \  \____\ \  \\\  \ \  \____\ \  \\ \  \       \ \  \\\  \ \  \____\ \  \ \ \  \\  \\ \  \ \  \ 
   \ \_______\ \_______\ \_______\ \_______\ \__\\ \__\       \ \_______\ \_______\ \__\ \ \__\\ _\\ \__\ \__\
    \|_______|\|_______|\|_______|\|_______|\|__| \|__|        \|_______|\|_______|\|__|  \|__|\|__|\|__|\|__|                                                                                      
                                                                                            
Extreme speed!
Edits the world files using a humble github module

The program will download the necessary module automagically if you don't have it
WARNING: If you for some reason have a module named bedrock that is not for
editing minecraft worlds then it will get deleted unless you change the minecraft
module name via the downloader code

I know the code is messy but it works
'''
#Please note this is for bedrock becuase no tool exists for bedrock edition.
#Just download some software from the web if you have java edition.

#Made by:
#Jacob Vermeulen
#Contributions and testing from:
#Connor Irwin

from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
try:
    import bedrock #if the user has not dowloaded this module we won't spit a mean error leaving noobs confused
except ImportError:#I am feeling nice and I will downloaded the rather difficult to install module for them
    print("looks like you don't have the right module. It is difficult to install so I will do it for you.\nTHERE IS NO GUARANTEE THIS WILL WORK")
    import urllib.request
    import zipfile
    from shutil import copytree
    bedrock_url = "https://github.com/BluCodeGH/bedrock/archive/master.zip"
    download_name = os.path.expanduser('~')+"\\Downloads\\bedrock-master.zip"
    print("Downloading zip from internet...")
    filename, header = urllib.request.urlretrieve(bedrock_url, download_name)#download zip from github
    print("Extracting zip...")
    with zipfile.ZipFile(filename, 'r') as zip_ref:#exract zip file
        zip_ref.extractall(filename[0:len(filename)-4])  
    print("Copying into new directory...")
    copytree(filename[0:len(filename)-4]+'\\bedrock-master\\bedrock', os.path.expanduser('~')+"\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\bedrock")#copy into python modules
    import bedrock
    print("Done.")

colors = {(127, 178, 56) : bedrock.Block("minecraft:slime", 0),
          (247, 233, 163) : bedrock.Block("minecraft:sandstone", 0),
          (255, 0, 0) : bedrock.Block("minecraft:redstone_block", 0),
          (160, 160, 255) : bedrock.Block("minecraft:ice", 0),
          (167, 167, 167) : bedrock.Block("minecraft:iron_block", 0),
          (255, 255, 255) : bedrock.Block("minecraft:wool", 0),
          (164, 168, 184) : bedrock.Block("minecraft:clay", 0),
          (151, 109, 77) : bedrock.Block("minecraft:dirt", 0),
          (112, 112, 112) : bedrock.Block("minecraft:stone", 0),
          (143, 119, 72) : bedrock.Block("minecraft:planks", 0),
          (255, 252, 245) : bedrock.Block("minecraft:quartz_block", 0),
          (216, 127, 51) : bedrock.Block("minecraft:wool", 1),
          (178, 76, 216) : bedrock.Block("minecraft:wool", 2),
          (102, 153, 216) : bedrock.Block("minecraft:wool", 3),
          (229, 229, 51) : bedrock.Block("minecraft:wool", 4),
          (127, 204, 25) : bedrock.Block("minecraft:wool", 5),
          (242, 127, 165) : bedrock.Block("minecraft:wool", 6),
          (76, 76, 76) : bedrock.Block("minecraft:wool", 7),
          (153, 153, 153) : bedrock.Block("minecraft:wool", 8),
          (76, 127, 153) : bedrock.Block("minecraft:wool", 9),
          (127, 63, 178) : bedrock.Block("minecraft:wool", 10),
          (51, 76, 178) : bedrock.Block("minecraft:wool", 11),
          (102, 76, 51) : bedrock.Block("minecraft:wool", 12),
          (102, 127, 51) : bedrock.Block("minecraft:wool", 13),
          (153, 51, 51) : bedrock.Block("minecraft:wool", 14),
          (25, 25, 25) : bedrock.Block("minecraft:wool", 15),
          (250, 238, 77) : bedrock.Block("minecraft:gold_block", 0),
          (92, 219, 213) : bedrock.Block("minecraft:diamond_block", 0),
          (74, 128, 255) : bedrock.Block("minecraft:lapis_block", 0),
          (0, 217, 58) : bedrock.Block("minecraft:emerald_block", 0),
          (129, 86, 49) : bedrock.Block("minecraft:planks", 1),
          (112, 2, 0) : bedrock.Block("minecraft:netherrack", 0),
          (209, 177, 161) : bedrock.Block("minecraft:stained_hardened_clay", 0),
          (159, 82, 36) : bedrock.Block("minecraft:stained_hardened_clay", 1),
          (149, 87, 108) : bedrock.Block("minecraft:stained_hardened_clay", 2),
          (112, 108, 138) : bedrock.Block("minecraft:stained_hardened_clay", 3),
          (186, 133, 36) : bedrock.Block("minecraft:stained_hardened_clay", 4),
          (103, 117, 53) : bedrock.Block("minecraft:stained_hardened_clay", 5),
          (160, 77, 78) : bedrock.Block("minecraft:stained_hardened_clay", 6),
          (57, 41, 35) : bedrock.Block("minecraft:stained_hardened_clay", 7),
          (135, 107, 98) : bedrock.Block("minecraft:stained_hardened_clay", 8),
          (87, 92, 92) : bedrock.Block("minecraft:stained_hardened_clay", 9),
          (122, 73, 88) : bedrock.Block("minecraft:stained_hardened_clay", 10),
          (76, 62, 92) : bedrock.Block("minecraft:stained_hardened_clay", 11),
          (76, 50, 35) : bedrock.Block("minecraft:stained_hardened_clay", 12),
          (76, 82, 42) : bedrock.Block("minecraft:stained_hardened_clay", 13),
          (142, 60, 46) : bedrock.Block("minecraft:stained_hardened_clay", 14),
          (37, 22, 16) : bedrock.Block("minecraft:stained_hardened_clay", 15)}

def scale_to_world(image):
    if image.height > 255: #minecraft worlds have limited height. make any image thats to tall smaller
        image = image.resize((int(255*image.width/image.height),255))
    image = image.rotate(180)#minecraft has the bottom as y=0 but images have the TOP as y=0. rotates the image 180 degrees
    image = image.convert("RGBA")#must be able to detect alpha values as to not place blocks where transparent
    return image

def gen_block(image):
    blocks = []
    percent = 0
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x,y))#retreive the current pixel's (R)ed, (G)reen, (B)lue, (A)lpha values
            compare = []
            for col in range(len(colors)):#every pixel is compared to every block color to find the closest block.
                red = abs(pixel[0]-list(colors)[col][0])#by getting the absolute value of the difference between each pixel's red, green, and blue values
                green = abs(pixel[1]-list(colors)[col][1])#and the all of the block's red, green, and blue values, we can sum it up and the block with the
                blue = abs(pixel[2]-list(colors)[col][2])#lowest value is closest in color (mathematically)
                compare += [red+green+blue]
            if pixel[3] < 127: #if the block is transparent make it air
                blocks += [bedrock.Block('air', 0)]
            else:
                blocks += [colors[list(colors)[compare.index(min(compare))]]]#figure out which block had the lowest value and add that block to the image
            blocks[len(blocks)-1] = (x, y, blocks[len(blocks)-1])#inject that block's x and y values
        if int((x*y) / (image.width*image.height)*100) != percent:#if how far it is to being done changes by 1 run below
            percent = int(((x*y) / (image.width*image.height))*100)#update the percentage to being done
            print(str(percent) + "% complete")#print to the user how far it is to completion
    return blocks

def choose_world():
    worlds = []
    for world in os.listdir(os.path.expanduser('~')+'\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\'):#return all the immediate subdirectories under minecraftWorlds
        world_name = open(os.path.expanduser('~')+'\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\'+world+'\\levelname.txt', 'r').read()#open the name of each world
        remove = []#minecraft text can be colored with the seciton symbol but when not in minecraft it can make worlds with fancy names hard to read 
        for letter in range(len(world_name)):#python doesn't read the minecraft section symbol right and puts a weird A in front with the section symbol
            if world_name[letter] == 'Â':
                remove += [letter, letter+1, letter+2]#the Â§ is followed by a letter to give color. remove the extra letter too
        world_name = list(world_name)#convert the string to a list so we can delete characters
        for delete in range(len(remove)-1, -1, -1):
            del world_name[remove[delete]]#delete unwanted characters working backwards to keep the list numbers from going over
        world_name = ''.join(world_name)#turn the list back into a string
        worlds += [[world_name, os.path.expanduser('~')+'\\AppData\\Local\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\games\\com.mojang\\minecraftWorlds\\'+world+'\\']]#add the world and world path to worlds
        print(len(worlds)-1, ': '+worlds[len(worlds)-1][0])#present worlds to user
    select = input('choose the number corrisponding to your world: ')#choose world
    print('you chose ', worlds[int(select)][0])
    world_path = worlds[int(select)][1]
    return world_path

def build_image(image, blocks, xpos, zpos):
    skip = 0 #used for skipping blocks when rows get placed and air blocks
    percent = 0
    shift = int(image.width/2)#have the player at the center of the image
    with bedrock.World(world_path) as world:#open the minecraft world to be edited
        for bck in range(len(blocks)):
            world.setBlock(int(xpos)+(blocks[bck][0]-shift), blocks[bck][1], int(zpos)+1, blocks[bck][2])
            if int(bck / (image.width*image.height)*100) != percent:#if how far it is to being done changes by 1 run below
                percent = int((bck / (image.width*image.height))*100)#update the percentage to being done
                print(str(percent) + "% complete")#print to the user how far it is to completion
        
if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    image = Image.open(askopenfilename(initialdir="C:/User/jacob/Pictures/",
                                   filetypes=(("PNG Image", "*.png"),("JPEG Image", "*.jpg"),("GIF Image", "*.gif")),
                                   title="Choose Image"), 'r')
    print("Processing Image...")
    image = scale_to_world(image)
    print("Generating Blocks...")
    blocks = gen_block(image)
    print("""Use the width and height below to determine the place to set your image\nThe coordinates you choose will be for the center of the image\n
       image center
            |
    <-------o------->
            X
            ^
    your coordinate input (X)\nis moved up one block\non the Z axis this is\njust incase you are\nstanding where you want\nthe image\n""")
    print('image width (x): ', image.width)
    print('image height (y): ',str(image.height)+"\n")
    print("It's time to start building!\nMAKE SURE YOU ARE NOT IN YOUR MINECRAFT WORLD!\nBEFORE GETTING OFF FLY AROUND THE BUILD SPOT WITH YOUR RENDER DISTANCE MAXED\n")
    xpos = int(input('enter the image center x position: '))
    zpos = int(input('enter the image center z position: '))
    world_path = choose_world()
    print('Starting image building...')
    build_image(image, blocks, xpos, zpos)
    print('Done.')
    
        
