# [16.1.9. 乱数](https://docs.python.jp/3/library/os.html#random-numbers)

< [16.1. os — 雑多なオペレーティングシステムインタフェース](https://docs.python.jp/3/library/os.html) < [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/secrets.py](https://github.com/python/cpython/tree/3.6/Lib/secrets.py)

属性|概要
----|----
os.getrandom(size, flags=0)|最大で size バイトからなるランダムなバイト列を返します。この関数は要求されたバイト数よりも少ないバイト数を返すことがあります。
os.urandom(size)|暗号に関する用途に適した size バイトからなるランダムな文字列を返します。
os.GRND_NONBLOCK|By default, when reading from /dev/random, getrandom() blocks if no random bytes are available, and when reading from /dev/urandom, it blocks if the entropy pool has not yet been initialized.(デフォルトでは、/ dev / randomから読み込むとき、ランダムなバイトがない場合にはgetrandom（）をブロックし、/ dev / urandomから読み取る場合にはエントロピープールがまだ初期化されていない場合にブロックする。)
os.GRND_RANDOM|If this bit is set, then random bytes are drawn from the /dev/random pool instead of the /dev/urandom pool.(このビットが設定されている場合、/ dev / randomプールの代わりに/ dev / randomプールからランダムバイトが引き出されます。)


