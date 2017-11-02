import tarfile

with tarfile.open('0.tar.gz', 'w:gz') as f:
    for name in ['a.txt', 'b.txt']:
        f.add(name)

with tarfile.open('0.tar.gz', 'r:gz') as f:
    f.extractall()

