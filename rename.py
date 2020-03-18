# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:15:29 2020

@author: Kubus
"""

import os
import csv
PATH = os.path.dirname(os.path.abspath(__file__))

file_list = os.listdir(PATH)
print(file_list)

subfolder="\\"+"test_dir1"


def main(): 
    i = 0
    list_before = []
    list_after = []
      
    for filename in os.listdir(PATH + subfolder): 
        list_before.append(filename)
        dst = subfolder + "_mysza"+str(i)+ "_P" + str(i%4+1) + "_"+ filename
        src = "\\" + filename 
 
        os.rename(PATH + subfolder+src, PATH + subfolder+dst) 
        i += 1
        list_after.append(dst)
    print(list_before, list_after)
    
    result_file = open("zamiana.csv", "w")
    for j in range(len(list_before)):
        result_file.write(list_before[j] + ", " + list_after[j] + "\n")
    result_file.close()

  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 