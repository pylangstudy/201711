import hashlib
m = hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
print(m.digest())
print(m.digest_size)
print(m.block_size)

h = hashlib.new('ripemd160')
h.update(b"Nobody inspects the spammish repetition")
print(h.hexdigest())

