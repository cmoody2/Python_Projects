
import os
import time


"""--------------------------------------------------------
    First we print out a list of all files in a specific
    directory using the os.listdir function from os module.
-----------------------------------------------------------"""

dir1 = os.listdir('C:\\Users\Moody\Documents\GitHub\Python_projects\exercises\OS_module_test')


#This creates a new empty list to drop all matching files into
txtList = []


"""--------------------------------------------------------
    Use a for loop to iterate through our directory list.
    for each element that contains the characters '.txt':
    - add it to new list
    - create a absolute file path for each using the path.join()
      method passing in the string and a directory absolute path
    - get the last time a file was modified using .getmtime() method
    - convert last modified time to more readable string using
      .ctime method from time module
    - print to console
-----------------------------------------------------------"""
print("\nThese are all '.txt' files in specified directory:")
    
for i in dir1:
    if '.txt' in i:
        txtList += [i]
        docName = i
        docPath = 'C:\\Users\Moody\Documents\GitHub\Python_projects\exercises\OS_module_test'
        abPath = os.path.join(docPath, docName)
        modTime = os.path.getmtime(abPath)
        convModTime = time.ctime(modTime)
        print("\n\n{}  last modified: {}".format(abPath, convModTime))
    else:
        continue


    
