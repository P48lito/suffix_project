# Script deleting suffixes of mp3 files in the given folder


import os

dir = 'C:/Users/lesno/Desktop/PProjects/suffix_project/music/'

# Choose only one line uncommented below
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace(' [ ezmp3.cc ].mp3', '.mp3'))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace('(Lyrics)', ''))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace('(Audio)', ''))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace('HQ!', ''))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace('(Remastered)', ''))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace('(Official Audio)', ''))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace('(Official Video)', ''))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace('(Official Audio)', ''))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace('(Radio Edit)', ''))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace('(Album Version)', ''))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace('(Official Audio)', ''))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace(' (Official Video)', ''))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace(' (Original Version)', ''))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace(' (Original Version)', ''))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace(' Cover', ''))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace(' (Live)', ''))
for filename in os.listdir(dir):
    os.rename(dir + filename, dir + filename.replace(' [HQ]', ''))
