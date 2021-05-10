
import os
path = "D:\Aditya\Whitehat Jr\Module 3\99"
dir_list = os.listdir(path)
print("files and directories in", path,":")
print(dir_list)

import os 
file = "file1.txt"
location = "D:\Aditya\Whitehat Jr\Module 3\99"
path = os.path.join(location,file)
#os.remove(path)

import os 
directory = "MyProject"
location = "D:\Aditya\Whitehat Jr\Module 3\99"
path = os.path.join(location, directory)
#os.rmdir(path)

import os 
print(os.name)

