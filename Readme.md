# Overview

Use this if you have the need to upload a file to RDP where perhaps copy/paste and local disks cannot be used. 

Additionally this can be used in cloud environments such as Azure within Bastion hosts where copy/paste can be particularly tricky at times.

Disclaimer: *Only use this on services where you are legally allowed to do so. Doing otherwise risks your liberty.*

For more information about this check out my blog on it:

[https://cornerpirate.com/2020/04/14/uploading-file-when-all-else-fails//](https://cornerpirate.com/2020/04/14/uploading-file-when-all-else-fails/)

It works by:

 1. Creating a zip of the file you want to upload (may save some space for some files)
 2. Base64 encoding that file.
 3. Typing the Base64 string programatically.

While 3) is happening you cannot use your mouse or keyboard. The data rate is low so be careful and plan what you want to upload.

## Install rdpupload
Pretty simple here clone the repo using this command, or download and extract the zip:

```bash
git clone https://github.com/cornerpirate/rdpupload.git
```

Install pre-requisites using the requirements.txt file as shown:

```bash
pip install -r requirements.txt
```

## Usage

I have now converted to Python3 and provided it as "rdpupload3.py" which you can run like this:

```bash
python rdpupload3.py -d 3 nc.exe
```

This has been tested on a Windows environment and worked fine with the exception of the sounds playing when "-s" was specified. This is not a core feature so I am not losing sleep. Sounds played fine on Kali for me.

The legacy version remains as "rdpupload.py" which works with Python 2 and uses the same running syntax.

Additioanlly, I have added "typestring.py" which is Python 3. For use where you just want to reliably paste a string into a restricted environment. Specify the string within double quotes as the argument to the script like this:

```bash
python typestring "I want to type this in here"
```

This has a hardcoded 3 second delay before the string is typed so you have 3 seconds to put the mouse pointer within the correct part of your remote session.

Note: If your string includes double quotes or shell restrictive characters then be sure to escape them appropriately.

