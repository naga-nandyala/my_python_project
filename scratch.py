# print sys.path and then append cwd to the sys.path then print again
import os
import sys

print(os.getcwd())
sys.path.append(os.getcwd())
print(sys.path)
