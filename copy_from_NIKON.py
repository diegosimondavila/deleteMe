import os
import os.path
import time
import datetime
import shutil

source_name = '/run/media/diego/9016-4EF8/'

#I will put the pictures in a temporary folder to make sure I don't overwrite anything:
destination_name = '/run/media/diego/Data/Pictures/Diego/Buffer/'

#Camera:
camera_name = 'NikonW100'

#Loop through all pictures in Source directory:

for root, dirs, files in os.walk(source_name):
 for file in files:
  if file.endswith(".JPG"):
   print(os.path.join(root, file))
   try:
    mtime = os.path.getmtime(os.path.join(root, file))
   except OSError:
    mtime = 0
   last_modified_date = datetime.datetime.fromtimestamp(mtime).strftime("%Y_%m_%d")
   specificDestination_name = destination_name + camera_name + "_" + last_modified_date
   specificDestination_dir = os.fsencode(specificDestination_name)
   #If the destination does not exist, create it:
   if not os.path.exists(specificDestination_dir):
    os.mkdir(specificDestination_dir)
   #Copy the pictures there:
   shutil.copy2(os.path.join(root, file),specificDestination_name)
   try:
    shutil.copy2(os.path.join(root, file+".xmp"),specificDestination_name)
   except IOError:
    continue
  elif file.endswith(".MP4"):
   specificDestination_name = destination_name + camera_name + "_VIDEOS"
   specificDestination_dir = os.fsencode(specificDestination_name)
   #If the destination does not exist, create it:
   if not os.path.exists(specificDestination_dir):
    os.mkdir(specificDestination_dir)
   #Copy the pictures there:
   shutil.copy2(os.path.join(root, file),specificDestination_name)
  else:
   #Type a message if the file is not ARW or JPG (or xmp!)
   if file.endswith(".xmp"):
    continue
   else:
    print("Not copying the following file: "+os.path.join(root, file))
