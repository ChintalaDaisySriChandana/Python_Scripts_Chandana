import random

import sys

import os

print(random.randint(2,5))


for i in range(2,5):
    print(i)

print(sys.argv[0])
print(sys.path)

os.chdir("/home/ubuntu")

os.makedirs("Directory", exist_ok=True)
print(os.getcwd())

print(os.listdir("/home/ubuntu"))

print(os.walk("/home/ubuntu"))

#for path,dir,files in os.walk("/home/ubuntu"):
 #   print(path)
  #  print(dir)
   # print(files)
