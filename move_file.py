import os
import shutil

source="C:/Users/aggar/Downloads"
destination="C:/Users/aggar/Downloads"
filesList=os.listdir(source)

for i in filesList:
    root,ext=os.path.splitext(i)
    if ext=="":
        continue
    if ext in ['.zip']:
        path1=source+"/"+i
        path2=destination+"/"+"compressed"
        path3=destination+"/compressed/"+i

        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)


