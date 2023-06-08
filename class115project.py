import sys # work with system 
import time
import random 

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

source = "C:/Users/goluk/Downloads"
destination = "C:/Users/goluk/Desktop"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'], 
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    #Student Activity1

    

    def on_created(self, event): # doubt :=> self and event kyu likha  hai
        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name= os.path.basename(event.src_path)
                path1=source + "/" + file_name
                path2=destination + "/" + key
                path3=destination + "/" + key + "/" + file_name

                if os.path.exists(path2):
                     print("Directory exist")
                     time.sleep(1)
                     if os.path.exists(path3):
                          print("File already exists")
                          print("Renaming the file")
                          new_file_name = os.path.splitext(file_name)[0] + str(random.randint(0, 999)) + os.path.splitext(file_name)[1]
                          path4 = destination + '/' + key + '/' + new_file_name
                          print("Moving ...")
                          shutil.move(path1, path4)
                          time.sleep(1)
                     else:
                          print("Moving")
                          shutil.move(path1,path3)
                          time.sleep(1)

                else:
                        os.makedirs(path2)
                        print("moving")
                        shutil.move(path1,path3)
                        time.sleep(1)




# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, source, recursive=True) # "recursive= true" kyu likha hai 


# Start the Observer
observer.start()

#Student Activity2
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
     print("stop")
     observer.stop()

    