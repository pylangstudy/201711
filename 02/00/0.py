import zipfile

with zipfile.ZipFile('spam.zip', 'w') as f:
    f.write('0.py')

with zipfile.ZipFile('spam.zip') as myzip:
    with myzip.open('0.py') as myfile:
        print(myfile.read())

