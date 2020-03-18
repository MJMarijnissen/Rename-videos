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

subfolder="03.12.2018"
kierunki=["W","E","S","N"]
myszy = [1,3,4,5,6,7,8,9,10,11,12,14,15,18,19,20,21,23,24,25,27,29,30,31,32,38,67,89,99]
fileextention = ".mpg"


def main(): 
    i = 0
    m=0
    list_before = []
    list_after = []

    
    result_file = open("zamiana.csv", "w")
    wr = csv.writer(result_file, dialect='excel')
      
    for filename in os.listdir(PATH + "\\"+ subfolder): 
        list_before.append(filename)

        dst = "\\reference_L1_3mies_M"+str(myszy[m])+ "_P" + str(i%4+1) + "_"+ str(kierunki[i%4]) + "_"+ subfolder + fileextention
        src = "\\" + filename 
 
        os.rename(PATH + "\\"+ subfolder+src, PATH + "\\"+ subfolder+dst) 
        list_after.append(dst)
        i += 1
        if i%4 == 0:
            m += 1
    print(list_before, list_after)
    
    # 
    # for j in range(len(list_before)):
    #     result_file.writerow(list_before[j] + ", " + list_after[j] + "\n")
    wr.writerow(list_before)
    wr.writerow(list_after)
    result_file.close()

  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 