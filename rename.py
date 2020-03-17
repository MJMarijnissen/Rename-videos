# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:15:29 2020

@author: Kubus
"""

import os
PATH = os.path.dirname(os.path.abspath(__file__))

file_list = os.listdir(PATH)
print(file_list)

initial_name = 'test_file.txt'
final_name = 'test_file2.txt'



os.rename(r'C:\Users\user\Python_user\Ada_rename_videos\test_file.txt', r'C:\Users\user\Python_user\Ada_rename_videos\test_file2.txt')