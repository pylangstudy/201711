import secrets

print(secrets.choice([100,200,300]))#100,200,300
print(secrets.randbelow(10))#0〜10
print(secrets.randbits(8))#0〜255(2**8())

print(secrets.token_bytes(8))
print(secrets.token_hex(8))
print(secrets.token_urlsafe(8))

print(secrets.compare_digest('a','a'))
print(secrets.compare_digest('a','b'))
