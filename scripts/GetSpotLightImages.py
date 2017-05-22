import os, shutil, stat, errno
from PIL import Image

# ============================ CONFIG ================================

user = os.environ['USERPROFILE']
dest_folder = "_tmp_"       # Destination folder in Downloads
delete_portraits = False    # delete portraits or not?
min_size = 500              # dimension in pixels

# ============================= PATHS ================================

local_packages = "AppData\Local\Packages"
spotlight_folder = "Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"

# destination = r"C:\Users\{0}\Downloads\{1}".format(user, dest_folder)
origin = os.path.join(user, local_packages, spotlight_folder) 
destination = os.path.join(user, 'Downloads', dest_folder)

# ======================== COLOR MESSAGES ============================

class bcolors:
    HEAD = '\033[95m'
    OK   = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

color_msg_fail_origin       = bcolors.FAIL + "origin path does not exists:\n" + bcolors.ENDC 
color_msg_fail_copy         = bcolors.FAIL + "copy fail:\n"                 + bcolors.ENDC
color_msg_fail_rename       = bcolors.FAIL + "rename fail:\n"               + bcolors.ENDC
color_msg_fail_identify     = bcolors.FAIL + "identify fail  -> deleted"    + bcolors.ENDC
color_msg_warn_exists       = bcolors.WARN + "already exists -> not copied" + bcolors.ENDC
color_msg_ok_del_small      = bcolors.FAIL + "too small      -> deleted"    + bcolors.ENDC
color_msg_ok_del_portrait   = bcolors.FAIL + "portrait       -> deleted"    + bcolors.ENDC
color_msg_ok_keep_portrait  = bcolors.OK   + "portrait       -> kept"       + bcolors.ENDC
color_msg_ok_keep_landscape = bcolors.OK   + "landscape      -> kept"       + bcolors.ENDC

print(bcolors.HEAD + "Made by `SylannBin` (copyleft)\n\
Thank you for using this simple script. I hope it serves you well.\n\
Attention! This script works for Windows only.\n\
Thanks to Microsoft for bringing us beautiful images.\n" + bcolors.ENDC)

# ============================= FUNCS ================================

# handle access error function
def handleRemoveReadonly(func, path, exc):
    excvalue = exc[1]
    if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
        func(path)
    else:
        raise

# ============================= SCRIPT ===============================

# I could delete the whole folder and all its content ...
# shutil.rmtree(destination, ignore_errors=False, onerror=handleRemoveReadonly)

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
    
    # check the copy file
    if not os.path.isfile(destpath):
        print(color_msg_fail_copy + destpath)
        break
    
    # rename copy file
    os.rename(destpath, bestpath)

    # check renamed copy file
    if not os.path.isfile(bestpath):
        print(color_msg_fail_rename + bestpath)
        break
    
    # Get dimensions
    try:
        width, height = Image.open(bestpath).size
    except:
        print(shortname + ": ---- x ---- | " + color_msg_fail_identify)

    # format a label for display purpose
    # label = shortname +': ' + str(width).rjust(4) + ' x ' + str(height).rjust(4) + ' | '
    label = "{0}: {1:>4} x {2:>4} | ".format(shortname, width, height)

    # remove small images
    # [remove portraits]
    # keep landscapes
    if height < min_size or width < min_size:
        print(label + color_msg_ok_del_small)
        os.unlink(bestpath)
    elif height > width:
        if delete_portraits:
            print(label + color_msg_ok_del_portrait)
            os.unlink(bestpath)
        else:
            print(label + color_msg_ok_keep_portrait)
    else:
        print(label + color_msg_ok_keep_landscape)


