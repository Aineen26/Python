# Program to print the contents of a directory using the os module.
import os

#selects the directories you want to list
directory_path ='/'

#list all the files and directories in the selected path
contents = os.listdir(directory_path)

#print each file and directory name
for item in contents:
    print(item)