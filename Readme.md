# Overview

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

```bash
git clone https://github.com/cornerpirate/rdpupload.git
```

