import hmac
print(hmac.new(b'abc'))
h = hmac.new(b'abc')
print(h)
print(h.digest())

