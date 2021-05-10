import math
print(math.pi)

from math import pi 
print(pi)

from math import *
print(factorial(6))

#import mathematics
#print(mathematics.pi)

import os 
cwd = os.getcwd()
print(" current working directory ", cwd)


import os 
os.chdir("../")
cwd = os.getcwd()
print("current working directoyr after change of directory", cwd)

import os 
def current_path():
    print("current working directory before")
    print(os.getcwd())

current_path()
os.chdir("D:\Aditya\Whitehat Jr")
current_path()

import os
directory = "MyProject"
parent_dir = "D:\Aditya\Whitehat Jr\Module 3\99"
path = os.path.join(parent_dir,directory)
#os.mkdir(path)

#os.mkdir("D:\Aditya\Whitehat Jr\Module 3\99\MyProject1")

cwd = os.getcwd()
print("current working directory after change of directory", cwd)

import os
directory = "Aditya"
parent_dir = "D:\Aditya\Whitehat Jr\Module 3\99"
path = os.path.join(parent_dir,directory)
#os.makedirs(path)

path = "D:\Aditya"
isExist = os.path.exists(path)
print(isExist)
