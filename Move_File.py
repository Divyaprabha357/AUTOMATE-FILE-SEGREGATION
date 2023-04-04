import shutil
import os

from_dir="C:/Users/Divyaprabha/Downloads"
to_dir="C:/Users/Divyaprabha/Desktop/github.com"

list_of_files= os.listdir(from_dir)
print(list_of_files)

for filename in list_of_files:
    name, extension= os.path.splitext(filename)
    print(name)
    print(extension)

    if extension == '':
        continue
    if extension in [".txt", ".doc", ".docx", ".pdf"]:
        path1= from_dir+"/"+filename
        path2= to_dir + "/" + "Document_Files"
        path3= to_dir + "/" + "Document_Files" + "/" + filename
        print("path1",path1)
        print("path3", path3)

    if os.path.exists(path2):
        print("Moving"+ filename +".....")
        shutil.move(path1,path3)

    else:
        os.makedirs(path2)
        print('Moving'+filename+".....")
        shutil.move(path1,path3)
