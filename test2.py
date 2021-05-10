import os
import shutil
path = "D:\Aditya\Whitehat Jr\Module 3\99"
source = "D:\Aditya\Whitehat Jr\Module 3\99\ a.txt"
destination  =  "D:\Aditya\Whitehat Jr\Module 3\99\ file2.txt"
#dest = shutil.copy(source,destination)
#print("after copying file :")
#print(os.listdir(path))

cwd = os.getcwd()
print("current working directory after change of directory", cwd)

import os
import shutil
path = "D:\Aditya\Whitehat Jr\Module 3\99"
source = "D:\Aditya\Whitehat Jr\Module 3\99\ a.txt"
destination  =  "D:\Aditya\Whitehat Jr\Module 3\99\ file2.txt"
dest = shutil.move(source,destination)
print("after moving the files")
print(os.listdir(path))