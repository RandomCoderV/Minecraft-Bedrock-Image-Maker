# Minecraft Bedrock Image Maker
Simple python program to create images in Minecraft bedrock edition.

No tool exists yet and not everyone can program.
So your welcome poor bedrock users! (windows only)

Easy to use. Run the program and it should install the required packages. There is no guarantee this will work.
If you run into a problem this can be due to your python site-packages folder being in a different place.
Future updates may come allowing for the detection of python module directories. If you run into a problem
you can manually install it. Follow the instructions at the bottom to install the module manually.

## Using The Image Maker
1. Find a spot in you world (Use flat worlds!). With your render distance maxed look around the world to 
generate chunks. To find a spot simply stand where you want the center of your
image to be. then move -1 on the Z axis. Look at the image below. The diamond blocks represents the cooridinates
choosen for the image. This should give you an idea of the coordinates to use.
![Image Placement](https://i.imgur.com/LcrIGEY.png)
2. Write down the X and Z axis for the spot and EXIT MINECRAFT.
3. Run the program.
4. Select the image you would like to use.
5. Let the program process the image.
6. The program will give you about the same instructions as the first instruction above. 
It will aso give the size of the image in blocks.
7. Enter the X coordinate
8. Enter the Z coordinate
9. A list of your worlds will appear. Enter the number corresponding to your world.
(the program automatically removes symbols involved in text color to make it easier to read)
10. Let it build the image.
11. Enter your minecraft world to see a massive image awaiting you!
![Completed Image](https://i.imgur.com/b65TDCb.png)

## Common Errors (and how to fix them)
```
Traceback (most recent call last):
  File >Your program file path<, line 55, in <module>
    import bedrock #if the user has not dowloaded this module we won't spit a mean error leaving noobs confused
ModuleNotFoundError: No module named 'bedrock'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File >Your program file path<, line 70, in <module>
    import bedrock
ModuleNotFoundError: No module named 'bedrock'
```
The bedrock module can't be found meaning installation failed.
Follow the Manual Packages Install at the bottom to fix.

```
Traceback (most recent call last):
  File ">Location of bedrock folder<\bedrock.py", line 82, in _loadVersion
    version = ldb.get(db, self.keyBase + b"v")
  File ">Location of bedrock folder<\leveldb.py", line 168, in get
    raise KeyError("Key {} not found in database.".format(key))
KeyError: "Key b'\\xf5\\xff\\xff\\xff\\x00\\x00\\x00\\x00v' not found in database."

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File ">Your program file path", line 196, in <module>
    world.setBlock((int(xpos)+(blocks[bck][0]-shift)), (blocks[bck][1]), (int(zpos)+1), (blocks[bck][2]))
  File ">Location of bedrock folder<\bedrock.py", line 47, in setBlock
    chunk = self.getChunk(cx, cz)
  File ">Location of bedrock folder<\bedrock.py", line 30, in getChunk
    chunk = Chunk(self.db, x, z)
  File ">Location of bedrock folder<\bedrock.py", line 65, in __init__
    self.version = self._loadVersion(db)
  File ">Location of bedrock folder<\bedrock.py", line 87, in _loadVersion
    raise KeyError("Chunk at {}, {} does not exist.".format(self.x, self.z))
KeyError: 'Chunk at >Chunk X<, >Chunk Y< does not exist.'
```
Some of the chunks your image will be in don't exist.
Fly around the buildsite with your render distance maxed to generate chunks.

```
Traceback (most recent call last):
  File >Location of site-packages<\PIL\Image.py, line 2774, in open
    fp.seek(0)
AttributeError: 'str' object has no attribute 'seek'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File >Your program file path<, line 186, in <module>
    title="Choose Image"), 'r')
  File ">Location of site-packages<\PIL\Image.py", line 2776, in open
    fp = io.BytesIO(fp.read())
AttributeError: 'str' object has no attribute 'read'
```
You didn't select an image dude!

```
Traceback (most recent call last):
  File >Your program file path<, line 50, in <module>
    from PIL import Image
ModuleNotFoundError: No module named 'PIL'
```
You don't have the Python Image Library
Install by opening the windows command prompt and typing:
```
pip install pillow
```

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
