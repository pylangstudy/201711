# [15.3. secrets — 機密を扱うために安全な乱数を生成する](https://docs.python.jp/3/library/secrets.html)

< [15. 暗号関連のサービス](https://docs.python.jp/3/library/crypto.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/secrets.py](https://github.com/python/cpython/tree/3.6/Lib/secrets.py)

> secrets モジュールを使って、パスワードやアカウント認証、セキュリティトークンなどの機密を扱うのに適した、暗号学的に強い乱数を生成することができます。

> 特に、 random モジュールのデフォルトの擬似乱数よりも secrets を使用するべきです。 random モジュールはモデル化やシミュレーション向けで、セキュリティや暗号学的に設計されてはいません。

* [PEP 506](https://www.python.org/dev/peps/pep-0506)

## [15.3.1. 乱数](https://docs.python.jp/3/library/secrets.html#random-numbers)

> secrets モジュールは OS が提供する最も安全な乱雑性のソースへのアクセスを提供します。

属性|概要
----|----
class secrets.SystemRandom|OS が提供する最も高品質なソースを用いて乱数を生成するためのクラスです。更に詳しいことについては random.SystemRandom を参照してください。
secrets.choice(sequence)|空でないシーケンスから要素をランダムに選択して返します。
secrets.randbelow(n)|[0, n) のランダムな整数を返します。
secrets.randbits(k)|ランダムな k ビットの整数を返します。

## [15.3.2. トークンの生成](https://docs.python.jp/3/library/secrets.html#generating-tokens)

> secrets モジュールはパスワードのリセットや想像しにくい URL などの用途に適した、安全なトークンを生成するための関数を提供します。

属性|概要
----|----
secrets.token_bytes([nbytes=None])|nbytes バイトを含むバイト文字列を返します。nbytes が None の場合や与えられなかった場合は妥当なデフォルト値が使われます。
secrets.token_hex([nbytes=None])|十六進数のランダムなテキスト文字列を返します。文字列は nbytes のランダムなバイトを持ち、各バイトは二つの十六進数に変換されます。nbytes が None の場合や与えられなかった場合は妥当なデフォルト値が使われます。
secrets.token_urlsafe([nbytes=None])|nbytes のランダムなバイトを持つ URL 安全なテキスト文字列を返します。テキストは Base64 でエンコードされていて、平均的に各バイトは約 1.3 文字になります。 nbytes が None の場合や与えられなかった場合は妥当なデフォルト値が使われます。

### [15.3.2.1. トークンは何バイト使うべきか？](https://docs.python.jp/3/library/secrets.html#how-many-bytes-should-tokens-use)

> 総当たり攻撃 に耐えるには、トークンは十分にランダムでなければなりません。残念なことに、コンピュータの性能が向上し、より短時間により多くの推測ができるようになるにつれ、十分とされるランダムさというのは必然的に増えます。2015 年の時点で、secrets モジュールに想定される通常の用途では、32 バイト (256 ビット) のランダムさは十分と考えられています。

> 独自の長さのトークンを扱いたい場合、様々な token_* 関数に int 引数で渡すことで、トークンに使用するランダムさを明示的に指定することができます。引数はランダムさのバイト数として使用されます。

> それ以外の場合、すなわち引数がない場合や None の場合、token_* 関数は妥当なデフォルト値を代わりに使います。

#### 注釈

> デフォルトはメンテナンスリリースの間を含め、いつでも変更される可能性があります。

## [15.3.3. その他の関数](https://docs.python.jp/3/library/secrets.html#other-functions)

属性|概要
----|----
secrets.compare_digest(a, b)|文字列 a と b が等しければ True を、そうでなければ False を返します。比較は タイミング攻撃 のリスクを減らす方法で行われます。詳細については hmac.compare_digest() を参照してください。

## [15.3.4. レシピとベストプラクティス](https://docs.python.jp/3/library/secrets.html#recipes-and-best-practices)

> この節では secrets を使用してセキュリティの基礎的なレベルを扱う際のレシピとベストプラクティスを説明します。

> 8文字のアルファベットと数字を含むパスワードを生成するには:

```python
import string
alphabet = string.ascii_letters + string.digits
password = ''.join(choice(alphabet) for i in range(8))
```

### 注釈

> アプリケーションは、平文であろうと暗号化されていようと、復元可能な形式でパスワードを保存 してはいけません。パスワードは暗号学的に強い一方向 (非可逆) ハッシュ関数を用いてソルトしハッシュしなければなりません。

> アルファべットと数字からなり、小文字を少なくとも1つと数字を少なくとも3つ含む、10文字のパスワードを生成するには:

```python
import string
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(choice(alphabet) for i in range(10))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break
```

> XKCD スタイルのパスフレーズ を生成するには:

```python
# On standard Linux systems, use a convenient dictionary file.
# Other platforms may need to provide their own word-list.
with open('/usr/share/dict/words') as f:
    words = [word.strip() for word in f]
    password = ' '.join(choice(words) for i in range(4))
```

> パスワードの復元用途に適したセキュリティトークンを含む、推測しにくい一時 URL を生成するには:

```python
url = 'https://mydomain.com/reset=' + token_urlsafe()
```

