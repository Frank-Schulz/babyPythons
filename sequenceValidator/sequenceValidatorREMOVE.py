# Python code to check for holes in a sequence of files

# import modules
import os, re, time

# set file name
search = "Naruto Shippuden Episode "
# set var for checking previous file
lastFileNum = 0
# set full name of last file
lastFile = f"{search}{lastFileNum}"
# save directory list
dirList = os.listdir()

# for every file in current directory
for file in dirList:
    # skip this python file
    if file == "sequenceValidator.py" or file == "sequenceValidatorREMOVE.py":
        continue
    # split file extension and save 
    splitFile = os.path.splitext(file)
    fileName, fileExt = splitFile
    # remove any files with extension ".temp"
    if fileExt == ".temp":
        os.remove(file)
    
    # save number of current file
    if re.search(search, fileName):
        fileNum = [int(i) for i in fileName.split() if i.isdigit()]
        fileNum = fileNum[0]
        # check difference between current and last checked file
        diff = fileNum - lastFileNum - 1
        # if a difference greater than 0 is found1
        if diff > 0:
            # create temporary files to show missing files
            for x in range(diff):
                lastFileNum += 1
                newFileName = f"{search}{lastFileNum:03d} --------------------------.temp"
                f= open(newFileName,"w+")
                f.close
        # set current file as previous
        lastFileNum = fileNum
        
# delete this file the "REMOVE" tag has been removed
# upon failure rename file to alert user of tag removal option
try:
    os.remove("sequenceValidator.py")
except:
    os.rename("sequenceValidatorREMOVE.py", "Remove tag 'REMOVE' to delete after run")
    time.sleep(3)
    os.rename("Remove tag 'REMOVE' to delete after run", "sequenceValidatorREMOVE.py")

