# [16.4.4. parse_args() メソッド](https://docs.python.jp/3/library/argparse.html#the-parse-args-method)

< [16.4. argparse — コマンドラインオプション、引数、サブコマンドのパーサー](https://docs.python.jp/3/library/argparse.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/argparse.py](https://github.com/python/cpython/tree/3.6/Lib/argparse.py)

属性|概要
----|----
ArgumentParser.parse_args(args=None, namespace=None)|引数の文字列をオブジェクトに変換し、namespace オブジェクトの属性に代入します。結果の namespace オブジェクトを返します。

引数|概要
----|----
args|List of strings to parse. The default is taken from sys.argv.
namespace|An object to take the attributes. The default is a new empty Namespace object.

### [16.4.4.1. オプション値の文法](https://docs.python.jp/3/library/argparse.html#option-value-syntax)

> parse_args() メソッドは、オプションの値がある場合、そのオプションの値の指定に複数の方法をサポートしています。もっとも単純な場合には、オプションとその値は次のように2つの別々の引数として渡されます:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x')
>>> parser.add_argument('--foo')
>>> parser.parse_args(['-x', 'X'])
Namespace(foo=None, x='X')
>>> parser.parse_args(['--foo', 'FOO'])
Namespace(foo='FOO', x=None)
```

> 長いオプション (1文字よりも長い名前を持ったオプション) では、オプションとその値は次のように = で区切られた1つのコマンドライン引数として渡すこともできます:

```python
>>> parser.parse_args(['--foo=FOO'])
Namespace(foo='FOO', x=None)
```

短いオプション (1文字のオプション) では、オプションとその値は次のように連結して渡すことができます:

```python
>>> parser.parse_args(['-xX'])
Namespace(foo=None, x='X')
```

最後の1つのオプションだけが値を要求する場合、または値を要求するオプションがない場合、複数の短いオプションは次のように1つの接頭辞 - だけで連結できます:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x', action='store_true')
>>> parser.add_argument('-y', action='store_true')
>>> parser.add_argument('-z')
>>> parser.parse_args(['-xyzZ'])
Namespace(x=True, y=True, z='Z')
```

### [16.4.4.2. 不正な引数](https://docs.python.jp/3/library/argparse.html#invalid-arguments)

> parse_args() は、コマンドラインの解析中に、曖昧なオプション、不正な型、不正なオプション、位置引数の数の不一致などのエラーを検証します。それらのエラーが発生した場合、エラーメッセージと使用法メッセージを表示して終了します:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--foo', type=int)
>>> parser.add_argument('bar', nargs='?')

>>> # invalid type
>>> parser.parse_args(['--foo', 'spam'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: argument --foo: invalid int value: 'spam'

>>> # invalid option
>>> parser.parse_args(['--bar'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: no such option: --bar

>>> # wrong number of arguments
>>> parser.parse_args(['spam', 'badger'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: extra arguments found: badger
```

### [16.4.4.3. - を含む引数](https://docs.python.jp/3/library/argparse.html#arguments-containing)

> parse_args() メソッドは、ユーザーが明らかなミスをした場合はエラーを表示しますが、いくつか本質的に曖昧な場面があります。例えば、コマンドライン引数 -1 は、オプションの指定かもしれませんし位置引数かもしれません。parse_args() メソッドはこれを次のように扱います: 負の数として解釈でき、パーサーに負の数のように解釈できるオプションが存在しない場合にのみ、- で始まる位置引数になりえます:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x')
>>> parser.add_argument('foo', nargs='?')

>>> # no negative number options, so -1 is a positional argument
>>> parser.parse_args(['-x', '-1'])
Namespace(foo=None, x='-1')

>>> # no negative number options, so -1 and -5 are positional arguments
>>> parser.parse_args(['-x', '-1', '-5'])
Namespace(foo='-5', x='-1')

>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-1', dest='one')
>>> parser.add_argument('foo', nargs='?')

>>> # negative number options present, so -1 is an option
>>> parser.parse_args(['-1', 'X'])
Namespace(foo=None, one='X')

>>> # negative number options present, so -2 is an option
>>> parser.parse_args(['-2'])
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: no such option: -2

>>> # negative number options present, so both -1s are options
>>> parser.parse_args(['-1', '-1'])
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: argument -1: expected one argument
```

> - で始まる位置引数があって、それが負の数として解釈できない場合、ダミーの引数 '--' を挿入して、parse_args() にそれ以降のすべてが位置引数だと教えることができます:

```python
>>> parser.parse_args(['--', '-f'])
Namespace(foo='-f', one=None)
```

### [16.4.4.4. 引数の短縮形 (先頭文字でのマッチング)](https://docs.python.jp/3/library/argparse.html#argument-abbreviations-prefix-matching)

> parse_args() メソッドは、デフォルトで、長いオプションに曖昧さがない (先頭の文字が一意である) かぎり、先頭の一文字に短縮して指定できます:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-bacon')
>>> parser.add_argument('-badger')
>>> parser.parse_args('-bac MMM'.split())
Namespace(bacon='MMM', badger=None)
>>> parser.parse_args('-bad WOOD'.split())
Namespace(bacon=None, badger='WOOD')
>>> parser.parse_args('-ba BA'.split())
usage: PROG [-h] [-bacon BACON] [-badger BADGER]
PROG: error: ambiguous option: -ba could match -badger, -bacon
```

> 先頭の文字が同じ引数が複数ある場合に短縮指定を行うとエラーを発生させます。この機能は allow_abbrev に False を指定することで無効にできます。

### [16.4.4.5. sys.argv 以外](https://docs.python.jp/3/library/argparse.html#beyond-sys-argv)

> ArgumentParser が sys.argv 以外の引数を解析できると役に立つ場合があります。その場合は文字列のリストを parse_args() に渡します。これはインタラクティブプロンプトからテストするときに便利です:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument(
...     'integers', metavar='int', type=int, choices=range(10),
...     nargs='+', help='an integer in the range 0..9')
>>> parser.add_argument(
...     '--sum', dest='accumulate', action='store_const', const=sum,
...     default=max, help='sum the integers (default: find the max)')
>>> parser.parse_args(['1', '2', '3', '4'])
Namespace(accumulate=<built-in function max>, integers=[1, 2, 3, 4])
>>> parser.parse_args(['1', '2', '3', '4', '--sum'])
Namespace(accumulate=<built-in function sum>, integers=[1, 2, 3, 4])
```

### [16.4.4.6. Namespace オブジェクト](https://docs.python.jp/3/library/argparse.html#the-namespace-object)

属性|概要
----|----
class argparse.Namespace|parse_args() が属性を格納して返すためのオブジェクトにデフォルトで使用されるシンプルなクラスです。

> デフォルトでは、 parse_args() は Namespace の新しいオブジェクトに必要な属性を設定して返します。このクラスはシンプルに設計されており、単に読みやすい文字列表現を持った object のサブクラスです。もし属性を辞書のように扱える方が良ければ、標準的な Python のイディオム vars() を利用できます:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> args = parser.parse_args(['--foo', 'BAR'])
>>> vars(args)
{'foo': 'BAR'}
```

> ArgumentParser が、新しい Namespace オブジェクトではなく、既存のオブジェクトに属性を設定する方が良い場合があります。これは namespace= キーワード引数を指定することで可能です:

```python
>>> class C:
...     pass
...
>>> c = C()
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.parse_args(args=['--foo', 'BAR'], namespace=c)
>>> c.foo
'BAR'
```

