import os

print(os.openpty())
print(os.pipe())

print(os.pipe2(os.O_NONBLOCK | os.O_CLOEXEC))
#print(os.posix_fallocate(fd, offset, len))
#print(os.posix_fadvise(fd, offset, len, advice))

import pathlib
path = pathlib.Path('./0.txt').resolve()
print(path)
with os.open(path, os.O_RDONLY) as f: #FileNotFoundError: [Errno 2] No such file or directory:
    print(f)

