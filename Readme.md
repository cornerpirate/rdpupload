# Overview

Use this if you have the need to upload a file to RDP where perhaps copy/paste and local disks cannot be used.

Disclaimer: *Only use this on services where you are legally allowed to do so. Doing otherwise risks your liberty.*

This works by:

 1. Creating a zip of the file you want to upload (may save some space for some files)
 2. Base64 encoding that file.
 3. Typing the Base64 string programatically.

While 3) is happening you cannot use your mouse or keyboard. The data rate is low so be careful and plan what you want to upload.



## Install Pre-Requisites

We need "pyautogui" which has an installation guide for various platforms here:

http://pyautogui.readthedocs.io/en/latest/install.html

For Kali Linux, the required commands were:

```bash
pip install python3-xlib
apt-get install scrot python3-dev
pip install pyautogui
```

Any problems installing pyautogui then refer to their documentation for your OS. My script is only tested on Kali Linux, your mileage and support will vary from there.

Additionally we need this for the progress bar:

```bash
pip install tqdm
```

Finally, this for sound:

```bash
pip install playsound
```

## Install rdpupload
Pretty simple here clone the repo:

```bash
git clone https://github.com/cornerpirate/rdpupload.git
```

As you already have the pre-requisites you are now all set to get this done.
