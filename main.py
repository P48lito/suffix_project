import os, glob

# This script deletes files with extensions: .png .jpg from given path

def scandirs(path):
    for currentFile in glob.glob( os.path.join(path, '*') ):
        if os.path.isdir(currentFile):
            print('got a directory: ' + currentFile)
            scandirs(currentFile)
        print("processing file: " + currentFile)
        png = "png";
        jpg = "jpg";
        if currentFile.endswith(png) or currentFile.endswith(jpg):
            os.remove(currentFile)

# scandirs('C:\Program Files (x86)\music\Songs')
scandirs(r"C:\Users\lesno\Desktop\PProjects\suffix_project\music")