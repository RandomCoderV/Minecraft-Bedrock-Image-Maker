# Minecraft-Bedrock-Image-Maker
Simple python program to create images in Minecraft bedrock edition.

No tool exists yet and not everyone can program.
So your welcome poor bedrock users! (windows only)

Easy to use. Run the program and it should install the required packages. There is no guarantee this will work.
If you run into a problem this can be due to your python site-packages folder being in a different place.
Future updates may come allowing for the detection of python module directories. If you run into a problem
you can manually install it. Follow the instructions at the bottom to install the module manually.

## Using The Image Maker
1. Find a spot in you world. Use flat worlds! To find spot simply stand where you want the center of your
image to be. and move -1 on the Z axis. Look at the image below. The diamond blocks represents the cooridinates
choosen for the image. This should give you an idea of the cooridinates to use.


## Manual Packages Install
1. Run the program and look in your downloads folder. It will have downloaded and extracted the files already
2. Look inside the 'bedrock-master' folder and find the 'bedrock' folder
3. Run the following lines below in IDLE:
```
import sys
```
and then
```
print(sys.path)
```
4. Look in the list. find where the 'site-packages' folder is
5. Copy the 'bedrock' folder into the 'site-packages' folder
6. Check if it has worked by running this in IDLE:
```
import bedrock
```
7. If no errors occur then great! you can run the program with the instructions above.
If problems persist put it in the issues for this project
