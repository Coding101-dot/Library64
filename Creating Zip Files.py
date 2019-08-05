import zipfile , os
#os.chdir('Go to directory where file that needs to be compressed is located')

newzip = zipfile.ZipFile('new.zip', 'w')
newzip.write('special.txt', compress_type=zipfile.ZIP_DEFLATED)