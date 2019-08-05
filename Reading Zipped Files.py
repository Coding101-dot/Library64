import zipfile, os

os.chdir('Enter directory here')

exampleZip = zipfile.ZipFile('Enter File name')

exampleZip.namelist()

getinfo = exampleZip.getinfo('Enter folder in zipped folder')

