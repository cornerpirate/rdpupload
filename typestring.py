# Created by CornerPirate on 14/04/2020
# This types the contents of sys.argv[1] into a remote session.
# Bypassing restrictive copy/paste environments for fun and profit.
from pyautogui import press, typewrite, hotkey
from tqdm import tqdm
from multiprocessing import Process
import sys
import os
import time


####################### Library Functions #########################

# Splits a string (s) into chunks of size (n)
def nsplit(s, n):
    return [s[k:k+n] for k in range(0, len(s), n)]

###################################################################

# defining global variables
tosend = sys.argv[1]
delay = 3 # number of seconds to get pointer into remote session.

print("[*] you said (" + tosend + ")")

# Sleep to give the user time to get their mouse pointer in place
print("[*] Sleeping for " + str(delay) + " seconds. Get your mouse pointer into Notepad within your RDP Session")
time.sleep(delay)

# Tested the time for uploading the entire file versus splitting into chunks and saw no difference really.
# So might as well split so we can get a progress update.
splits = nsplit(tosend, 256)
max = len(splits) # number of slices of size 256

# Lets be classy eh? Let you know when it is finished.
p = None

# Do the typing and use tqdm to display a progress bar
for split in tqdm(splits):
	typewrite(split)

# Close down routine and tell the user how to retrieve their file
print("[*] Upload complete, have a nice day")

