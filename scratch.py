# print sys.path and then append cwd to the sys.path then print again
import os
import sys

print(sys.path)
sys.path.append(os.getcwd())
print(sys.path)

# added ci test
