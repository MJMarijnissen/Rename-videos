# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:15:29 2020

@author: Kubus
"""

import os
PATH = os.path.dirname(os.path.abspath(__file__))


list_subfolders_with_paths = [f.path for f in os.scandir(PATH) if f.is_dir() and ".git" not in f.path]

print(list_subfolders_with_paths)


def main(): 
    i = 0
    for directory in list_subfolders_with_paths:  
        for filename in os.listdir(directory): 
            dst = "\\test" + str(i) + ".txt"
            src = "\\" + filename 
 
            os.rename(directory+src, directory+dst) 
            i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 