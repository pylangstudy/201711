# [16.4.3. add_argument() メソッド](https://docs.python.jp/3/library/argparse.html#the-add-argument-method)

< [16.4. argparse — コマンドラインオプション、引数、サブコマンドのパーサー](https://docs.python.jp/3/library/argparse.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/argparse.py](https://github.com/python/cpython/tree/3.6/Lib/argparse.py)

属性|概要
----|----
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])|1つのコマンドライン引数がどう解析されるかを定義します。

引数|概要
----|----
name または flags|名前か、あるいはオプション文字列のリスト (例: foo や -f, --foo)。
action|コマンドラインにこの引数があったときのアクション。
nargs|受け取るべきコマンドライン引数の数。
const|一部の action と nargs の組み合わせで利用される定数。
default|コマンドラインに引数がなかった場合に生成される値。
type|コマンドライン引数が変換されるべき型。
choices|引数として許される値のコンテナー。
required|コマンドラインオプションが省略可能かどうか (オプション引数のみ)。
help|引数が何なのかを示す簡潔な説明。
metavar|使用法メッセージの中で使われる引数の名前。
dest|parse_args() が返すオブジェクトに追加される属性名。

### [16.4.3.1. name または flags](https://docs.python.jp/3/library/argparse.html#name-or-flags)

> add_argument() メソッドは、指定されている引数が -f や --foo のようなオプション引数なのか、ファイル名リストなどの位置引数なのかを知る必要があります。そのため、add_argument() の第1引数は、フラグのリストか、シンプルな引数名のどちらかになります。例えば、オプション引数は次のようにして作成します:

```python
>>> parser.add_argument('-f', '--foo')
```

> 一方、位置引数は次のように作成します:

```python
>>> parser.add_argument('bar')
```

> parse_args() が呼ばれたとき、オプション引数は接頭辞 - により識別され、それ以外の引数は位置引数として扱われます:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-f', '--foo')
>>> parser.add_argument('bar')
>>> parser.parse_args(['BAR'])
Namespace(bar='BAR', foo=None)
>>> parser.parse_args(['BAR', '--foo', 'FOO'])
Namespace(bar='BAR', foo='FOO')
>>> parser.parse_args(['--foo', 'FOO'])
usage: PROG [-h] [-f FOO] bar
PROG: error: too few arguments
```

### [16.4.3.2. action](https://docs.python.jp/3/library/argparse.html#action)

> ArgumentParser オブジェクトはコマンドライン引数にアクションを割り当てます。このアクションは、割り当てられたコマンドライン引数に関してどんな処理でもできますが、ほとんどのアクションは単に parse_args() が返すオブジェクトに属性を追加するだけです。action キーワード引数は、コマンドライン引数がどう処理されるかを指定します。提供されているアクションは:

* 'store' - これは単に引数の値を格納します。これはデフォルトのアクションです。例えば:
    
```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.parse_args('--foo 1'.split())
Namespace(foo='1')
```

* 'store_const' - このアクションは const キーワード引数で指定された値を格納します。'store_const' アクションは、何かの種類のフラグを指定するオプション引数によく使われます。例えば:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='store_const', const=42)
>>> parser.parse_args(['--foo'])
Namespace(foo=42)
```

* 'store_true', 'store_false' - これらは 'store_const' の、それぞれ True と False を格納する特別版になります。加えて、これらはそれぞれデフォルト値を順に False と True にします。例えば:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='store_true')
>>> parser.add_argument('--bar', action='store_false')
>>> parser.add_argument('--baz', action='store_false')
>>> parser.parse_args('--foo --bar'.split())
Namespace(foo=True, bar=False, baz=True)
```

* 'append' - このアクションはリストを格納して、各引数の値をそのリストに追加します。このアクションは複数回指定を許可したいオプションに便利です。利用例:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action='append')
>>> parser.parse_args('--foo 1 --foo 2'.split())
Namespace(foo=['1', '2'])
```

* 'append_const' - このアクションはリストを格納して、const キーワード引数に与えられた値をそのリストに追加します (const キーワード引数のデフォルト値はあまり役に立たない None であることに注意)。'append_const' アクションは、定数を同じリストに複数回格納する場合に便利です。例えば:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--str', dest='types', action='append_const', const=str)
>>> parser.add_argument('--int', dest='types', action='append_const', const=int)
>>> parser.parse_args('--str --int'.split())
Namespace(types=[<class 'str'>, <class 'int'>])
```

* 'count' - このアクションはキーワード引数の数を数えます。例えば、verboseレベルを上げるのに役立ちます:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--verbose', '-v', action='count')
>>> parser.parse_args(['-vvv'])
Namespace(verbose=3)
```

* 'help' - このアクションは現在のパーサー中のすべてのオプションのヘルプメッセージを表示し、終了します。出力の生成方法の詳細については ArgumentParser を参照してください。

* 'version' - このアクションは add_argument() の呼び出しに version= キーワード引数を期待します。指定されたときはバージョン情報を表示して終了します:

```python
>>> import argparse
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--version', action='version', version='%(prog)s 2.0')
>>> parser.parse_args(['--version'])
PROG 2.0
```

> Action のサブクラスまたは同じインターフェイスを実装したほかのオブジェクト渡すことで、任意のアクションを指定することもできます。これをするお奨めの方法は、 argparse.Action を継承して、 __call__ と、必要であれば __init__ をオーバライドすることです。

> カスタムアクションの例です:

```python
>>> class FooAction(argparse.Action):
...     def __init__(self, option_strings, dest, nargs=None, **kwargs):
...         if nargs is not None:
...             raise ValueError("nargs not allowed")
...         super(FooAction, self).__init__(option_strings, dest, **kwargs)
...     def __call__(self, parser, namespace, values, option_string=None):
...         print('%r %r %r' % (namespace, values, option_string))
...         setattr(namespace, self.dest, values)
...
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', action=FooAction)
>>> parser.add_argument('bar', action=FooAction)
>>> args = parser.parse_args('1 --foo 2'.split())
Namespace(bar=None, foo=None) '1' None
Namespace(bar='1', foo=None) '2' '--foo'
>>> args
Namespace(bar='1', foo='2')
```

> 詳細は Action を参照してください。

### [16.4.3.3. nargs](https://docs.python.jp/3/library/argparse.html#nargs)

> ArgumentParser オブジェクトは通常1つのコマンドライン引数を1つのアクションに渡します。nargs キーワード引数は1つのアクションにそれ以外の数のコマンドライン引数を割り当てます。指定できる値は:

* N (整数) – N 個の引数がコマンドラインから集められ、リストに格納されます。例えば:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', nargs=2)
>>> parser.add_argument('bar', nargs=1)
>>> parser.parse_args('c --foo a b'.split())
Namespace(bar=['c'], foo=['a', 'b'])
```

* nargs=1 は1要素のリストを作ることに注意してください。これはデフォルトの、要素がそのまま属性になる動作とは異なります。

* '?' – 可能なら1つの引数がコマンドラインから取られ、1つのアイテムを作ります。コマンドライン引数が存在しない場合、default の値が生成されます。オプション引数の場合、さらにオプション引数が指定され、その後にコマンドライン引数がないというケースもありえます。この場合は const の値が生成されます。この動作の例です:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', nargs='?', const='c', default='d')
>>> parser.add_argument('bar', nargs='?', default='d')
>>> parser.parse_args(['XX', '--foo', 'YY'])
Namespace(bar='XX', foo='YY')
>>> parser.parse_args(['XX', '--foo'])
Namespace(bar='XX', foo='c')
>>> parser.parse_args([])
Namespace(bar='d', foo='d')
```

* nargs='?' のよくある利用例の1つは、入出力ファイルの指定オプションです:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
...                     default=sys.stdin)
>>> parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
...                     default=sys.stdout)
>>> parser.parse_args(['input.txt', 'output.txt'])
Namespace(infile=<_io.TextIOWrapper name='input.txt' encoding='UTF-8'>,
          outfile=<_io.TextIOWrapper name='output.txt' encoding='UTF-8'>)
>>> parser.parse_args([])
Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>,
          outfile=<_io.TextIOWrapper name='<stdout>' encoding='UTF-8'>)
```

* '*' – すべてのコマンドライン引数がリストに集められます。複数の位置引数が nargs='*' を持つことにあまり意味はありませんが、複数のオプション引数が nargs='*' を持つことはありえます。例えば:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', nargs='*')
>>> parser.add_argument('--bar', nargs='*')
>>> parser.add_argument('baz', nargs='*')
>>> parser.parse_args('a b --foo x y --bar 1 2'.split())
Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])
```

* '+' – '*' と同じように、すべてのコマンドライン引数をリストに集めます。加えて、最低でも1つのコマンドライン引数が存在しない場合にエラーメッセージを生成します。例えば:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('foo', nargs='+')
>>> parser.parse_args(['a', 'b'])
Namespace(foo=['a', 'b'])
>>> parser.parse_args([])
usage: PROG [-h] foo [foo ...]
PROG: error: too few arguments
```

* argparse.REMAINDER – コマンドライン引数の残りすべてをリストとして集めます。これは他のコマンドラインツールに対して処理を渡すようなツールによく使われます。例えば:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--foo')
>>> parser.add_argument('command')
>>> parser.add_argument('args', nargs=argparse.REMAINDER)
>>> print(parser.parse_args('--foo B cmd --arg1 XX ZZ'.split()))
Namespace(args=['--arg1', 'XX', 'ZZ'], command='cmd', foo='B')
```

> nargs キーワード引数が指定されない場合、受け取る引数の数は action によって決定されます。通常これは、1つのコマンドライン引数は1つのアイテムになる (リストにはならない) ことを意味します。

### [16.4.3.4. const](https://docs.python.jp/3/library/argparse.html#const)

> add_argument() の const 引数は、コマンドライン引数から読み込まれないけれども ArgumentParser のいくつかのアクションで必要とされる値のために使われます。この引数のよくある2つの使用法は:

* add_argument() が action='store_const' か action='append_const' で呼び出されたとき、これらのアクションは const の値を parse_args() が返すオブジェクトの属性に追加します。サンプルは action の説明を参照してください。
* add_argument() がオプション文字列 (-f や --foo) と nargs='?' で呼び出された場合。この場合0個か1つのコマンドライン引数を取るオプション引数が作られます。オプション引数にコマンドライン引数が続かなかった場合、 const の値が代わりに利用されます。サンプルは nargs の説明を参照してください。

> 'store_const' と 'append_const' アクションでは、 const キーワード引数を与える必要があります。他のアクションでは、デフォルトは None になります。

### [16.4.3.5. default](https://docs.python.jp/3/library/argparse.html#default)

> すべてのオプション引数といくつかの位置引数はコマンドライン上で省略されることがあります。 add_argument() の default キーワード引数 (デフォルト: None) は、コマンドライン引数が存在しなかった場合に利用する値を指定します。オプション引数では、オプション文字列がコマンドライン上に存在しなかったときに default の値が利用されます:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default=42)
>>> parser.parse_args(['--foo', '2'])
Namespace(foo='2')
>>> parser.parse_args([])
Namespace(foo=42)
```

> default の値が文字列の場合、パーサーは値をコマンドライン引数のように解析します。具体的には、パーサーは返り値 Namespace の属性を設定する前に、type 変換引数が与えられていればそれらを適用します。そうでない場合、パーサーは値をそのまま使用します:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--length', default='10', type=int)
>>> parser.add_argument('--width', default=10.5, type=int)
>>> parser.parse_args()
Namespace(length=10, width=10.5)
```

> nargs が ? か * である位置引数では、コマンドライン引数が指定されなかった場合 default の値が使われます。例えば:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('foo', nargs='?', default=42)
>>> parser.parse_args(['a'])
Namespace(foo='a')
>>> parser.parse_args([])
Namespace(foo=42)
```

> default=argparse.SUPPRESS を渡すと、コマンドライン引数が存在しないときに属性の追加をしなくなります。:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', default=argparse.SUPPRESS)
>>> parser.parse_args([])
Namespace()
>>> parser.parse_args(['--foo', '1'])
Namespace(foo='1')
```

### [16.4.3.6. type](https://docs.python.jp/3/library/argparse.html#type)

> デフォルトでは、ArgumentParser オブジェクトはコマンドライン引数を単なる文字列として読み込みます。しかし、コマンドラインの文字列は float, int など別の型として扱うべき事がよくあります。add_argument() の type キーワード引数により型チェックと型変換を行うことができます。一般的なビルトインデータ型や関数を type 引数の値として直接指定できます:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('foo', type=int)
>>> parser.add_argument('bar', type=open)
>>> parser.parse_args('2 temp.txt'.split())
Namespace(bar=<_io.TextIOWrapper name='temp.txt' encoding='UTF-8'>, foo=2)
```

type 引数がデフォルト引数に適用されている場合の情報は、default キーワード引数の節を参照してください。

いろいろな種類のファイルを簡単に扱うために、 argparse モジュールは open() 関数の mode=, bufsize=, encoding= および errors= 引数を取る FileType ファクトリを提供しています。例えば、書き込み可能なファイルを作るために FileType('w') を利用できます:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('bar', type=argparse.FileType('w'))
>>> parser.parse_args(['out.txt'])
Namespace(bar=<_io.TextIOWrapper name='out.txt' encoding='UTF-8'>)
```

> type= には1つの文字列を引数に受け取って変換結果を返すような任意の呼び出し可能オブジェクトを渡すことができます:

```python
>>> def perfect_square(string):
...     value = int(string)
...     sqrt = math.sqrt(value)
...     if sqrt != int(sqrt):
...         msg = "%r is not a perfect square" % string
...         raise argparse.ArgumentTypeError(msg)
...     return value
...
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('foo', type=perfect_square)
>>> parser.parse_args(['9'])
Namespace(foo=9)
>>> parser.parse_args(['7'])
usage: PROG [-h] foo
PROG: error: argument foo: '7' is not a perfect square
```

> さらに、choices キーワード引数を使って、値の範囲をチェックすることもできます:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('foo', type=int, choices=range(5, 10))
>>> parser.parse_args(['7'])
Namespace(foo=7)
>>> parser.parse_args(['11'])
usage: PROG [-h] {5,6,7,8,9}
PROG: error: argument foo: invalid choice: 11 (choose from 5, 6, 7, 8, 9)
```

> 詳細は choices 節を参照してください。

### [16.4.3.7. choices](https://docs.python.jp/3/library/argparse.html#choices)

> コマンドライン引数をいくつかの選択肢の中から選ばせたい場合があります。 これは add_argument() に choices キーワード引数を渡すことで可能です。コマンドラインを解析するとき、引数の値がチェックされ、その値が選択肢の中に含まれていない場合はエラーメッセージを表示します:

```python
>>> parser = argparse.ArgumentParser(prog='game.py')
>>> parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
>>> parser.parse_args(['rock'])
Namespace(move='rock')
>>> parser.parse_args(['fire'])
usage: game.py [-h] {rock,paper,scissors}
game.py: error: argument move: invalid choice: 'fire' (choose from 'rock',
'paper', 'scissors')
```

> choices コンテナーに含まれているかどうかのチェックは、type による型変換が実行された後であることに注意してください。このため、choices に格納するオブジェクトの型は指定された type にマッチしている必要があります:

```python
>>> parser = argparse.ArgumentParser(prog='doors.py')
>>> parser.add_argument('door', type=int, choices=range(1, 4))
>>> print(parser.parse_args(['3']))
Namespace(door=3)
>>> parser.parse_args(['4'])
usage: doors.py [-h] {1,2,3}
doors.py: error: argument door: invalid choice: 4 (choose from 1, 2, 3)
```

> in 演算をサポートしている任意のオブジェクトを choices に渡すことができます。すなわち、dict 、 set、カスタムコンテナーなどはすべてサポートされています。

### [16.4.3.8. required](https://docs.python.jp/3/library/argparse.html#required)

> 通常 argparse モジュールは、-f や --bar といったフラグは 任意 の引数 (オプション引数) だと仮定し、コマンドライン上になくても良いものとして扱います。フラグの指定を 必須 にするには、add_argument() の required= キーワード引数に True を指定します:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', required=True)
>>> parser.parse_args(['--foo', 'BAR'])
Namespace(foo='BAR')
>>> parser.parse_args([])
usage: argparse.py [-h] [--foo FOO]
argparse.py: error: option --foo is required
```

> 上の例のように、引数が required と指定されると、parse_args() はそのフラグがコマンドラインに存在しないときにエラーを表示します。

#### 注釈

> ユーザーは、通常 フラグ の指定は 任意 であると認識しているため、必須にするのは一般的には悪いやり方で、できる限り避けるべきです。 

### [16.4.3.9. help](https://docs.python.jp/3/library/argparse.html#help)

> help の値はその引数の簡潔な説明を含む文字列です。ユーザーが (コマンドライン上で -h か --help を指定するなどして) ヘルプを要求したとき、この help の説明が各引数に表示されます:

```python
>>> parser = argparse.ArgumentParser(prog='frobble')
>>> parser.add_argument('--foo', action='store_true',
...                     help='foo the bars before frobbling')
>>> parser.add_argument('bar', nargs='+',
...                     help='one of the bars to be frobbled')
>>> parser.parse_args(['-h'])
usage: frobble [-h] [--foo] bar [bar ...]

positional arguments:
 bar     one of the bars to be frobbled

optional arguments:
 -h, --help  show this help message and exit
 --foo   foo the bars before frobbling
```

> help 文字列には、プログラム名や引数の default などを繰り返し記述するのを避けるためのフォーマット指定子を含めることができます。利用できる指定子には、プログラム名 %(prog)s と、 %(default)s や %(type)s など add_argument() のキーワード引数の多くが含まれます:

```python
>>> parser = argparse.ArgumentParser(prog='frobble')
>>> parser.add_argument('bar', nargs='?', type=int, default=42,
...                     help='the bar to %(prog)s (default: %(default)s)')
>>> parser.print_help()
usage: frobble [-h] [bar]

positional arguments:
 bar     the bar to frobble (default: 42)

optional arguments:
 -h, --help  show this help message and exit
```

> ヘルプ文字列は %-フォーマットをサポートしているので、ヘルプ文字列内にリテラル % を表示したい場合は %% のようにエスケープしなければなりません。

> argparse は help に argparse.SUPPRESS を設定することで、特定のオプションをヘルプに表示させないことができます:

```python
>>> parser = argparse.ArgumentParser(prog='frobble')
>>> parser.add_argument('--foo', help=argparse.SUPPRESS)
>>> parser.print_help()
usage: frobble [-h]

optional arguments:
  -h, --help  show this help message and exit
```

### [16.4.3.10. metavar](https://docs.python.jp/3/library/argparse.html#metavar)

> ArgumentParser がヘルプメッセージを出力するとき、各引数に対してなんらかの参照方法が必要です。デフォルトでは、 ArgumentParser オブジェクトは各オブジェクトの "名前" として dest を利用します。デフォルトでは、位置引数には dest の値をそのまま 利用し、オプション引数については dest の値を大文字に変換して利用します。このため、1つの dest='bar' である位置引数は bar として参照されます。 1つのオプション引数 --foo が1つのコマンドライン引数を要求するときは、その引数は FOO として参照されます。以下に例を示します:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.add_argument('bar')
>>> parser.parse_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
>>> parser.print_help()
usage:  [-h] [--foo FOO] bar

positional arguments:
 bar

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO
```

> 代わりの名前を、metavar として指定できます:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', metavar='YYY')
>>> parser.add_argument('bar', metavar='XXX')
>>> parser.parse_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
>>> parser.print_help()
usage:  [-h] [--foo YYY] XXX

positional arguments:
 XXX

optional arguments:
 -h, --help  show this help message and exit
 --foo YYY
```

> metavar は 表示される 名前だけを変更することに注意してください。parse_args() の返すオブジェクトの属性名は dest の値のままです。

> nargs を指定した場合、metavar が複数回利用されるかもしれません。metavar にタプルを渡すと、各引数に対して異なる名前を指定できます:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x', nargs=2)
>>> parser.add_argument('--foo', nargs=2, metavar=('bar', 'baz'))
>>> parser.print_help()
usage: PROG [-h] [-x X X] [--foo bar baz]

optional arguments:
 -h, --help     show this help message and exit
 -x X X
 --foo bar baz
```

### [16.4.3.11. dest](https://docs.python.jp/3/library/argparse.html#dest)

> ほとんどの ArgumentParser のアクションは parse_args() が返すオブジェクトに対する属性として値を追加します。この属性の名前は add_argument() の dest キーワード引数によって決定されます。位置引数のアクションについては、 dest は通常 add_argument() の第一引数として渡します:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('bar')
>>> parser.parse_args(['XXX'])
Namespace(bar='XXX')
```

> オプション引数のアクションについては、 dest の値は通常オプション文字列から生成されます。 ArgumentParser は最初の長いオプション文字列を選択し、先頭の -- を除去することで dest の値を生成します。長いオプション文字列が指定されていない場合、最初の短いオプション文字列から先頭の - 文字を除去することで dest を生成します。先頭以外のすべての - 文字は、妥当な属性名になるように _ 文字へ変換されます。次の例はこの動作を示しています:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('-f', '--foo-bar', '--foo')
>>> parser.add_argument('-x', '-y')
>>> parser.parse_args('-f 1 -x 2'.split())
Namespace(foo_bar='1', x='2')
>>> parser.parse_args('--foo 1 -y 2'.split())
Namespace(foo_bar='1', x='2')
```

> dest にカスタムの属性名を与えることも可能です:

```python
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', dest='bar')
>>> parser.parse_args('--foo XXX'.split())
Namespace(bar='XXX')
```

### [16.4.3.12. Action クラス](https://docs.python.jp/3/library/argparse.html#action-classes)

> Acrtion クラスは Action API、すなわちコマンドラインからの引数を処理する呼び出し可能オブジェクトを返す呼び出し可能オブジェクトを実装します。この API に従うあらゆるオブジェクトは action 引数として add_argument() に渡すことができます。

* class argparse.Action(option_strings, dest, nargs=None, const=None, default=None, type=None, choices=None, required=False, help=None, metavar=None)

> Action オブジェクトは、コマンドラインからの一つ以上の文字列から単一の引数を解析するのに必要とされる情報を表現するために ArgumentParser によって使われます。Action クラス 2 つの位置引数と、action それ自身を除く ArgumentParser.add_argument() に渡されるすべてのキーワード引数を受け付けなければなりません。

> Action のインスタンス (あるいは action 引数に渡す任意の呼び出し可能オブジェクトの返り値) は、属性 "dest", "option_strings", "default", "type", "required", "help", などを定義しなければなりません。これらの属性を定義するのを確実にするためにもっとも簡単な方法は、Action.__init__ を呼び出すことです。

> Action インスタンスは呼び出し可能でなければならず、したがって、サブクラスは 4 つの引数を受け取る __call__ メソッドをオーバライドしなければなりません:

* parser - このアクションを持っている ArgumentParser オブジェクト。
* namespace - parse_args() が返す Namespace オブジェクト。ほとんどのアクションはこのオブジェクトに属性を setattr() を使って追加します。
* values - 型変換が適用された後の、関連付けられたコマンドライン引数。型変換は add_argument() メソッドの type キーワード引数で指定されます。
* option_string - このアクションを実行したオプション文字列。option_string 引数はオプションで、アクションが位置引数に関連付けられた場合は渡されません。

> __call__ メソッドでは任意のアクションを行えますが、 典型的にはそれは dest, values に基づく namespace に属性をセットすることでしょう。

