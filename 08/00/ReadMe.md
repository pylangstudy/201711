# [15.2. hmac — メッセージ認証のための鍵付きハッシュ化](https://docs.python.jp/3/library/hmac.html)

< [15. 暗号関連のサービス](https://docs.python.jp/3/library/crypto.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/hmac.py](https://github.com/python/cpython/tree/3.6/Lib/hmac.py)

> このモジュールでは RFC 2104 で記述されている HMAC アルゴリズムを実装しています。

hmac.new(key, msg=None, digestmod=None)|新しい hmac オブジェクトを返します。 key は秘密鍵を与える bytes または bytearray オブジェクトです。msg が与えられると、update(msg) が呼び出されます。digestmod は利用するダイジェスト名、ダイジェストコンストラクターまたは HMAC オブジェクトのモジュールです。hashlib.new() に与えることができる任意の名前をサポートし、デフォルトは hashlib.md5 のコンストラクターです。

> HMAC オブジェクトは以下のメソッドを持っています:

属性|概要
----|----
HMAC.update(msg)|hmac オブジェクトを msg で更新します。このメソッドの呼出の繰り返しは、それらの引数を全て結合した引数で単一の呼び出しをした際と同じになります。すなわち m.update(a); m.update(b) は m.update(a + b) と等価です。
HMAC.digest()|これまで update() メソッドに渡されたバイト列のダイジェスト値を返します。これはコンストラクタに与えられた digest_size と同じ長さのバイト列で、 NUL バイトを含む非 ASCII 文字が含まれることがあります。
HMAC.copy()|hmac オブジェクトのコピー ("クローン") を返します。このコピーは最初の部分文字列が共通になっている文字列のダイジェスト値を効率よく計算するために使うことができます。

> ハッシュオブジェクトには次のような属性があります:

属性|概要
----|----
HMAC.digest_size|生成された HMAC ダイジェストのバイト数。
HMAC.block_size|内部で使われるハッシュアルゴリズムのブロックのバイト数。
HMAC.name|このHMAC の正規名で、例えば hmac-md5 のように常に小文字です。

> このモジュールは以下のヘルパ関数も提供しています:

属性|概要
----|----
hmac.compare_digest(a, b)|a == b を返します。この関数は、内容ベースの短絡的な振る舞いを避けることによってタイミング分析を防ぐよう設計されたアプローチを用い、暗号化に用いるのに相応しいものとしています。 a と b は両方が同じ型でなければなりません: (例えば HMAC.hexdigest() が返したような ASCII のみの) str または bytes-like object のどちらか一方。

### 参考

モジュール|説明
----------|----
[hashlib](https://docs.python.jp/3/library/hashlib.html#module-hashlib)|セキュアハッシュ関数を提供する Python モジュールです。

