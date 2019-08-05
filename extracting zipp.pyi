import zipfile

#os.chdir(Enter Directory)
examplezip=zipfile.ZipFile('Enterzippedfoldername.zip')
examplezip.extractall()

#To extract a single file
examplezip.extract('filename')

