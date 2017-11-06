# [15.1. hashlib — セキュアハッシュおよびメッセージダイジェスト](https://docs.python.jp/3/library/hashlib.html)

< [15. 暗号関連のサービス](https://docs.python.jp/3/library/crypto.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/hashlib.py](https://github.com/python/cpython/tree/3.6/Lib/hashlib.py)

> このモジュールは、セキュアハッシュやメッセージダイジェスト用のさまざまなアルゴリズムを実装したものです。FIPSのセキュアなハッシュアルゴリズムである SHA1、SHA224、SHA256、SHA384およびSHA512 (FIPS 180-2 で定義されているもの) だけでなくRSAのMD5アルゴリズム (Internet RFC 1321 で定義されています)も実装しています。「セキュアなハッシュ」と「メッセージダイジェスト」はどちらも同じ意味です。古くからあるアルゴリズムは「メッセージダイジェスト」と呼ばれていますが、最近は「セキュアハッシュ」という用語が用いられています。

> 注釈

> adler32 や crc32 ハッシュ関数は zlib モジュールで提供されています。

> 警告

> 幾つかのアルゴリズムはハッシュの衝突に弱いことが知られています。最後の "参考" セクションを見てください。 

## [15.1.1. ハッシュアルゴリズム](https://docs.python.jp/3/library/hashlib.html#hash-algorithms)

> There is one constructor method named for each type of hash. All return a hash object with the same simple interface. For example: use sha256() to create a SHA-256 hash object. You can now feed this object with bytes-like objects (normally bytes) using the update() method. At any point you can ask it for the digest of the concatenation of the data fed to it so far using the digest() or hexdigest() methods.

> それぞれのタイプのハッシュに名前が付けられたコンストラクタメソッドが1つあります。 すべて同じ単純なインタフェースを持つハッシュオブジェクトを返します。 たとえば、sha256（）を使用してSHA-256ハッシュオブジェクトを作成します。 update（）メソッドを使用して、このオブジェクトにバイトのようなオブジェクト（通常はバイト）を供給できるようになりました。 いつでも、digest（）メソッドまたはhexdigest（）メソッドを使用して、それまでに供給されたデータの連結のダイジェストを求めることができます。

> 注釈

> マルチスレッドにおける良好なパフォーマンスを得るために、オブジェクトの生成時または更新時に与えるデータが 2047 バイトを超えている場合、Python GIL が解除されます。

> 注釈

> 文字列オブジェクトを update() に渡すのはサポートされていません。ハッシュはバイトには機能しますが、文字には機能しないからです。

> Constructors for hash algorithms that are always present in this module are sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), and blake2s(). md5() is normally available as well, though it may be missing if you are using a rare "FIPS compliant" build of Python. Additional algorithms may also be available depending upon the OpenSSL library that Python uses on your platform. On most platforms the sha3_224(), sha3_256(), sha3_384(), sha3_512(), shake_128(), shake_256() are also available.

> このモジュールに常に存在するハッシュアルゴリズムのコンストラクターは、sha1（）、sha224（）、sha256（）、sha384（）、sha512（）、blake2b（）、およびblake2s（）です。 まれな "FIPS準拠"のPythonビルドを使用している場合、md5（）も欠けているかもしれませんが、通常はmd5（）も利用できます。 Pythonがあなたのプラットフォームで使用するOpenSSLライブラリに応じて、追加のアルゴリズムを利用することもできます。 ほとんどのプラットフォームでは、sha3_224（）、sha3_256（）、sha3_384（）、sha3_512（）、shake_128（）、shake_256（）も使用できます。

> バージョン 3.6 で追加: SHA3 (Keccak) ならびに SHAKE コンストラクタ sha3_224(), sha3_256(), sha3_384(), sha3_512(), shake_128(), shake_256()。

> バージョン 3.6 で追加: blake2b() と blake2s() が追加されました。

> たとえば、b'Nobody inspects the spammish repetition' というバイト文字列のダイジェストを取得するには次のようにします:

```python
>>> import hashlib
>>> m = hashlib.sha256()
>>> m.update(b"Nobody inspects")
>>> m.update(b" the spammish repetition")
>>> m.digest()
b'\x03\x1e\xdd}Ae\x15\x93\xc5\xfe\\\x00o\xa5u+7\xfd\xdf\xf7\xbcN\x84:\xa6\xaf\x0c\x95\x0fK\x94\x06'
>>> m.digest_size
32
>>> m.block_size
64
```

> もっと簡潔に書くと、このようになります:

```python
>>> hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest()
'a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2'
```

属性|概要
----|----
hashlib.new(name[, data])|一般的なコンストラクタで、第一引数にアルゴリズム名を文字列で受け取ります。他にも、上記ハッシュだけでなく OpenSSL ライブラリーが提供するような他のアルゴリズムにアクセスすることができます。名前のあるコンストラクタの方が new() よりもずっと速いので望ましいです。

> new() にOpenSSLのアルゴリズムを指定する例です:

```python
>>> h = hashlib.new('ripemd160')
>>> h.update(b"Nobody inspects the spammish repetition")
>>> h.hexdigest()
'cc4a5ce1b3df48aec5d22d1f16b894a0b894eccc'
```

> Hashlib は以下の定数属性を提供しています:

属性|概要
----|----
hashlib.algorithms_guaranteed|A set containing the names of the hash algorithms guaranteed to be supported by this module on all platforms. Note that 'md5' is in this list despite some upstream vendors offering an odd "FIPS compliant" Python build that excludes it.
hashlib.algorithms_available|実行中の Python インタープリタで利用可能なハッシュアルゴリズム名の set です。これらの名前は new() に渡すことができます。algorithms_guaranteed は常にサブセットです。この set の中に同じアルゴリズムが違う名前で複数回現れることがあります (OpenSSL 由来)。
hash.digest_size|生成されたハッシュのバイト数。
hash.block_size|内部で使われるハッシュアルゴリズムのブロックのバイト数。

> ハッシュオブジェクトには次のような属性があります:

属性|概要
----|----
hash.name|このハッシュの正規名です。常に小文字で、new() の引数として渡してこのタイプの別のハッシュを生成することができます。

> ハッシュオブジェクトには次のようなメソッドがあります:

属性|概要
----|----
hash.update(arg)|オブジェクト arg でハッシュオブジェクトを更新します。arg はバイトのバッファとして解釈可能でなければなりません。繰り返し呼び出すことは引数全ての連結で一回呼び出すことと等価です。例えば m.update(a); m.update(b) は m.update(a+b) と等価です。
hash.digest()|これまで update() メソッドに渡されたデータのダイジェスト値を返します。これは digest_size と同じ長さの、0 から 255 の範囲全てを含み得るバイトの列です。
hash.hexdigest()|digest() と似ていますが、倍の長さの、16進形式文字列を返します。これは、電子メールなどの非バイナリ環境で値を交換する場合に便利です。
hash.copy()|ハッシュオブジェクトのコピー ("クローン") を返します。これは、最初の部分文字列が共通なデータのダイジェストを効率的に計算するために使用します。

