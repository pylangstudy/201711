import lzma#ModuleNotFoundError: No module named '_lzma'

data = b"Insert Data Here"
with lzma.open("file.xz", "w") as f:
    f.write(data)

with lzma.open("file.xz") as f:
    file_content = f.read()

data_in = b"Insert Data Here"
data_out = lzma.compress(data_in)
print(data_out)

# 逐次圧縮
lzc = lzma.LZMACompressor()
out1 = lzc.compress(b"Some data\n")
out2 = lzc.compress(b"Another piece of data\n")
out3 = lzc.compress(b"Even more data\n")
out4 = lzc.flush()
# Concatenate all the partial results:
result = b"".join([out1, out2, out3, out4])
print(result)

# すでにオープンしているファイルへの圧縮データの書き出し:
with open("file.xz", "wb") as f:
    f.write(b"This data will not be compressed\n")
    with lzma.open(f, "w") as lzf:
        lzf.write(b"This *will* be compressed\n")
    f.write(b"Not compressed\n")

# カスタムフィルタチェインを使った圧縮ファイルの作成:
my_filters = [
    {"id": lzma.FILTER_DELTA, "dist": 5},
    {"id": lzma.FILTER_LZMA2, "preset": 7 | lzma.PRESET_EXTREME},
]
with lzma.open("file.xz", "w", filters=my_filters) as f:
    f.write(b"blah blah blah")

