# print sys.path and then append cwd to the sys.path then print again
import os
import pandas as pd
import sys

sys.path.append(os.getcwd())
print(sys.path)
