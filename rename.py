# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:15:29 2020

@author: Kubus
"""

import os
PATH = os.path.dirname(os.path.abspath(__file__))

file_list = os.listdir(PATH)
print(file_list)

subfolder="\\test_dir1"

initial_name = 'test_file.txt'
final_name = 'test_file2.txt'



#os.rename(r'C:\Users\user\Python_user\Ada_rename_videos\test_file.txt', r'C:\Users\user\Python_user\Ada_rename_videos\test_file2.txt')

def main(): 
    i = 0
    list_before = []
    list_after = []
      
    for filename in os.listdir(PATH + subfolder): 
        list_before.append(filename)
        dst = "\\test" + str(i) + ".txt"
        src = "\\" + filename 
 
        os.rename(PATH + subfolder+src, PATH + subfolder+dst) 
        i += 1
        list_after.append(dst)
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 