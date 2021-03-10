# Python code to rename multiple files 
# in a directory or folder using regex

# importing os module 
import os, re, time

# set regex exp
badString = ("episode", "uncut", "reupload")
pattern = r'[0-9]'
pat = r'SUB'


dirList = os.listdir()

for file in dirList:
    
    if file == "regexFileRenamer.py" or file == "regexFileRenamerREMOVE.py":
        continue
    # split file extension and save 
    splitFile = os.path.splitext(file)
    fileName, fileExt = splitFile
    
    for string in badString:
        fileName = fileName.lower().replace(string,'')
    
    fileName = fileName.replace('naruto ','Naruto ')
    fileName = fileName.replace('shippuden ','Shippuden ')
    fileName = fileName.replace('shippuuden ','Shippuden ')
    fileName = fileName.replace('dub ','DUB ')
    fileName = re.sub(r"\s{2,}", ' ', fileName)
    
    num = [int(i) for i in fileName.split() if i.isdigit()]
    
    # Match all digits in the string and replace them by empty string
    fileName = re.sub(pattern, '', fileName)
    
    if re.search(r"DUB", fileName):
        fileName = re.sub(r"DUB ", '', fileName)
        fileName += "DUB "
    
    if len(num) > 0:
        fileName += f"Episode {num[0]:03d}"
    
    fileName += fileExt
    
    if fileName != file:
        os.rename(file, fileName)
        
# delete this file the "REMOVE" tag has been removed
# upon failure rename file to alert user of tag removal option
try:
    os.remove("regexFileRenamer.py")
except:
    os.rename("regexFileRenamerREMOVE.py", "Remove tag 'REMOVE' to delete after run")
    time.sleep(3)
    os.rename("Remove tag 'REMOVE' to delete after run", "regexFileRenamerREMOVE.py")

