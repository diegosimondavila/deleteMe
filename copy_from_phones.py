import os
import time
import datetime
import shutil

source_name = '/run/user/1000/gvfs/mtp:host=SAMSUNG_SAMSUNG_Android_R5CT603F8DW/Internal storage/WhatsApp/Media/WhatsApp Video/'
#destination_type = 'Mine'
destination_type = 'Received'

##############################################################################
##############################################################################

#I will put the pictures in a temporary folder to make sure I don't overwrite anything:
destination_name_images = '/home/diego/Pictures/Phones/' + destination_type + '/Images/'
destination_name_videos = '/home/diego/Pictures/Phones/' + destination_type + '/Videos/'

#Camera:
camera_name = 'PhoneCamera'

#Loop through all pictures in Source directory:
source_dir = os.fsencode(source_name)
for file in os.listdir(source_dir):
 filename = os.fsdecode(file)
 if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', 'raw', 'mp4', 'mov')):
  print("        "+os.path.join(source_name, filename))
  try:
   mtime = os.path.getmtime(os.path.join(source_name, filename))
  except OSError:
   mtime = 0
  last_modified_date = datetime.datetime.fromtimestamp(mtime).strftime("%Y_%m_%d")
  if filename.lower().endswith(('mp4', 'mov')):
   specificDestination_name = destination_name_videos + camera_name + "_" + last_modified_date
  else:
   specificDestination_name = destination_name_images + camera_name + "_" + last_modified_date
  specificDestination_dir = os.fsencode(specificDestination_name)
  #If the destination does not exist, create it:
  if not os.path.exists(specificDestination_dir):
   os.mkdir(specificDestination_dir)
  #Copy the pictures there:
  shutil.copy2(os.path.join(source_name, filename),specificDestination_name)
  try:
   shutil.copy2(os.path.join(source_name, filename+".xmp"),specificDestination_name)
  except IOError:
   continue
 else:
  #Type a message if the file is not ARW or JPG (or xmp!)
  if filename.endswith(".xmp"):
   continue
  else:
   print("Not copying the following file: "+os.path.join(source_name, filename))
