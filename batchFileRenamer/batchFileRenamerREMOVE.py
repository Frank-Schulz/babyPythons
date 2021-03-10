# Pythono3 code to rename multiple 
# files in a directory or folder 

# importing os module 
import os, random

# generate a random letter in range x - y
def randletter(x, y):
    return chr(random.randint(ord(x), ord(y)))

def stringGen():
    
    i = 0
    rand = ''
    while i < 15:
        if __name__ == '__main__':

            # generate a random letter in range a - z
            r = randletter('a', 'z')

            # generate a random letter in range A - Z
            R = randletter('A', 'Z')

            # randomly pick letter r or R
            rand += (r, R)[random.randint(0, 1)]
            i += 1
    return(rand)

dirList = os.listdir()
# print(dirList)

for x in dirList:
    
    if x == "batchFileRenamer.py" or x == "batchFileRenamerREMOVE.py":
        continue
    temp = os.path.splitext(x)
    
    randString = stringGen()
    
    randString += temp[1]
    print(randString)
    
    if randString != x:
        os.rename(x, randString)
    
    
try:
    os.remove("batchFileRenamer.py")
except:
    print('Remove tag "REMOVE" to delete')