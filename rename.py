# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:15:29 2020

@author: Kubus
"""

import os
import csv
PATH = os.path.dirname(os.path.abspath(__file__))

#subfolder in which to change files
subfolder="test_dir1"
#Mouse names added to altered name. Every 4th file will be changed
myszy = [1,3,4,5,6,7,8,9,10,11,12,14,15,18,19,20,21,23,24,25,27,29,30,31,32,38,67,89,99]
#Directions of mice added to altered file name
kierunki=["W","E","S","N"]
#file extension needed for file name
fileextention = ".mpg"
#begining of file name
begining = "genetic_L1_3mies_M"


def main(): 
    #i iterates over files, used to add P1,P2,P3 or P4 to the file name
    i = 0
    #m iterates over myszy list, every 4 files goes to next item in list
    m = 0
    #2 list for files
    list_before = []
    list_after = []

    #Writing file in CURRENT folder
    result_file = open("zamiana.csv", "w", newline='')
    wr = csv.writer(result_file, dialect='excel')

    #iterating over list 
    for filename in os.listdir(PATH + "\\"+ subfolder): 
        list_before.append(filename)
        #dst -destination fil ename (altered)
        dst = "\\" + begining +str(myszy[m]) + "_P" + str(i%4+1) + "_" + str(kierunki[i%4]) + "_"+ subfolder + fileextention
        #src - previous filename
        src = "\\" + filename 
 
        os.rename(PATH + "\\"+ subfolder+src, PATH + "\\"+ subfolder+dst) 
        list_after.append(dst)
        #print filenames
        print(list_before[i] + " --> " + list_after[i])
        wr.writerow([list_before[i]] + [list_after[i]])
        #increas iterator
        i += 1
        #every 4th file change mouse name
        if i%4 == 0:
            m += 1

    result_file.close()
 
if __name__ == '__main__': 
    main() 