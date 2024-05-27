import shutil as sh
import os
import time
source_dir = r'path/to/source/directory'
destination_dir = r'path/to/destination/directory'

list_of_files = os.listdir(source_dir)

for file_name in list_of_files:
    if '.jpg' in file_name or '.jfif' in file_name or '.png' in file_name:
        print(source_dir + file_name)
        sh.copyfile(source_dir + '/' + file_name,
                    destination_dir + '/' + file_name)
        os.remove(source_dir + '/' + file_name)
        time.sleep(0.2)

print('Files in', source_dir, 'are successfuly moved to path', destination_dir)
