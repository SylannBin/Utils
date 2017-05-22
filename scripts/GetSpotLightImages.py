import os
import shutil
from PIL import Image

# ============================ CONFIG ================================

user = os.environ['USERPROFILE']
dest_folder = r"Downloads\_tmp_"  # Destination folder in Downloads
delete_portraits = False          # delete portraits or not?
min_size = 500                    # dimension in pixels

# ============================= PATHS ================================

local_packages = r"AppData\Local\Packages"
spotlight_folder = r"Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"

origin = os.path.join(user, local_packages, spotlight_folder)
destination = os.path.join(user, dest_folder)

# ======================== COLOR MESSAGES ============================

COLOR_HEAD = '\033[95m'
COLOR_OK   = '\033[92m'
COLOR_WARN = '\033[93m'
COLOR_FAIL = '\033[91m'
COLOR_ENDC = '\033[0m'

color_msg_fail_origin       = COLOR_FAIL + "origin path does not exists:\n" + COLOR_ENDC
color_msg_fail_copy         = COLOR_FAIL + "copy fail:\n"                 + COLOR_ENDC
color_msg_fail_rename       = COLOR_FAIL + "rename fail:\n"               + COLOR_ENDC
color_msg_fail_identify     = COLOR_FAIL + "identify fail  -> deleted"    + COLOR_ENDC
color_msg_warn_exists       = COLOR_WARN + "already exists -> not copied" + COLOR_ENDC
color_msg_ok_del_small      = COLOR_FAIL + "too small      -> deleted"    + COLOR_ENDC
color_msg_ok_del_portrait   = COLOR_FAIL + "portrait       -> deleted"    + COLOR_ENDC
color_msg_ok_keep_portrait  = COLOR_OK   + "portrait       -> kept"       + COLOR_ENDC
color_msg_ok_keep_landscape = COLOR_OK   + "landscape      -> kept"       + COLOR_ENDC

print(COLOR_HEAD + "Made by `SylannBin` (copyleft)\n\
Thank you for using this simple script. I hope it serves you well.\n\
Attention! This script works for Windows only.\n\
Thanks to Microsoft for bringing us beautiful images.\n" + COLOR_ENDC)

# ============================= SCRIPT ===============================

# Ensure destination folder exists
if not os.path.exists(destination):
    os.makedirs(destination)

print("Copying files from:\n{0}\nto: {1}\n\nProcessing...\n".format(origin, destination))

# Fetch images from origin and work on each of them
for filename in os.listdir(origin):
    # prepare all paths and names
    shortname = filename[:16] + '.jpg'
    origpath = os.path.join(origin, filename)
    destpath = os.path.join(destination, filename)
    bestpath = os.path.join(destination, shortname)

    # check the origin file
    if not os.path.isfile(origpath):
        print(color_msg_fail_origin + origpath)
        break

    # check that file does not aready exist in destination folder
    if os.path.isfile(bestpath):
        print(shortname + ": ---- x ---- | " + color_msg_warn_exists)
        continue

    # make copy
    shutil.copy(origpath, destination)
    # check
    if not os.path.isfile(destpath):
        print(color_msg_fail_copy + destpath)
        break

    # rename copy file
    os.rename(destpath, bestpath)
    # check
    if not os.path.isfile(bestpath):
        print(color_msg_fail_rename + bestpath)
        break

    # Get dimensions
    try:
        width, height = Image.open(bestpath).size
    except:
        width, height = 0,0

    # format a label for display purpose
    # label = shortname +': ' + str(width).rjust(4) + ' x ' + str(height).rjust(4) + ' | '
    label = "{0}: {1:>4} x {2:>4} | ".format(shortname, width, height)

    # remove small images
    # [remove portraits]
    # keep landscapes
    if height == 0 and width == 0:
        os.unlink(bestpath)
        print(label + color_msg_fail_identify)
    elif height < min_size or width < min_size:
        os.unlink(bestpath)
        print(label + color_msg_ok_del_small)
    elif height > width and delete_portraits:
        os.unlink(bestpath)
        print(label + color_msg_ok_del_portrait)
    elif height > width:
        print(label + color_msg_ok_keep_portrait)
    else:
        print(label + color_msg_ok_keep_landscape)
