import os
#print(os.getrandom(1))#AttributeError: module 'os' has no attribute 'getrandom'
#print(os.getrandom(1, os.GRND_NONBLOCK | os.GRND_RANDOM))
print(os.urandom(1))

