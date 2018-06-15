import os

def search(default_path):
    file_list = []
    for (path,dir,files) in os.walk(default_path):
        for filename in files:
            file_list.append(path+"\\"+filename)

    return file_list