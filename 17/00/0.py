import io
with open("myfile.txt", "r", encoding="utf-8") as f:
    print(f.read())
with io.StringIO("some initial text data") as f:
    print(f.read())

with open("myfile.txt", "rb") as f:
    print(f.read())
with io.BytesIO(b"some initial binary data: \x00\x01") as f:
    print(f.read())

print('io.DEFAULT_BUFFER_SIZE:', io.DEFAULT_BUFFER_SIZE)
