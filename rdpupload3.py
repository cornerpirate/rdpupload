# Created by CornerPirate on 10/11/2017
# This zips any file and then base64 encodes it.
# It then delays for 10 seconds so you can get your mouse pointer in place.
# This will then  type the encoded characters wherever your pointer has focus.
# Useful when uploading files to RDP/VNC if he system does not allow 
# Drag and drop of files or paste.
from pyautogui import press, typewrite, hotkey
from playsound import playsound
from tqdm import tqdm
from multiprocessing import Process
import sys
import os
import zipfile
import base64
import time
import argparse


####################### Library Functions #########################

# Splits a string (s) into chunks of size (n)
def nsplit(s, n):
    return [s[k:k+n] for k in range(0, len(s), n)]

# Plays the typewriter sound
def playTypewriter():
    while True:
        playsound('typewriter.mp3')

###################################################################

# Defining the arguments and parsing the args.
parser = argparse.ArgumentParser()
parser.add_argument("file", help="file that you want to upload")
parser.add_argument("-d", "--delay", type=int, help="time in seconds to delay before pasting (default is 10)", default=10)
parser.add_argument("-s", "--sound", help="plays a typewriter sound until upload is finished", action='store_true')
args = parser.parse_args()

# Zip the intended file, might save some space if what you are uploading 
# Can save some space by zipping.
zfile = args.file + ".zip"

zipf = zipfile.ZipFile(zfile, 'w')
zipf.write(args.file)
zipf.close()

# Tell the user
print("[*] Zipped up: " + zfile)
print("[*] Base64 encoding zipped file ")

# Base64 encode the zipped file
b64 = base64.b64encode(open(zfile,'rb').read())
encodedfile = open(args.file + ".b64", "w")
encodedfile.write(b64.decode("utf-8"))
encodedfile.close()
print("[*] Saved encoded file to " + args.file + ".b64")

# Cleanup the zipped file
print("[*] Deleting the zip that was made")
#os.remove(zfile)

# Sleep to give the user time to get their mouse pointer in place
print("[*] Sleeping for " + str(args.delay) + " seconds. Get your mouse pointer into Notepad within your RDP Session")
time.sleep(args.delay)

# Tested the time for uploading the entire file versus splitting into chunks and saw no difference really.
# So might as well split so we can get a progress update.
splits = nsplit(b64, 64)
max = len(splits) # number of slices of size 256

# Lets be classy eh? Let you know when it is finished.
p = None
if args.sound:
    p = Process(target=playTypewriter)
    p.start()

# Do the typing and use tqdm to display a progress bar
for split in tqdm(splits):
	typewrite(split.decode("utf-8"))
	time.sleep(0.4)
	

# We got through it. Kill the sounds
if args.sound and p !=None:
    p.terminate()

# Close down routine and tell the user how to retrieve their file
print("[*] Upload complete")
print("[*] Save the file in your text editor on the windows system")
print("[*] Use 'certutil' to base64 decode to retrieve the intended file")
print("[*] certutil -decode <input_file> <output_file>")
print("[*] The output file needs a .zip extension. You can then unpack that as Windows has a zip util")
