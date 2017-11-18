# [16.4.2. ArgumentParser オブジェクト](https://docs.python.jp/3/library/argparse.html#argumentparser-objects)

< [16.4. argparse — コマンドラインオプション、引数、サブコマンドのパーサー](https://docs.python.jp/3/library/argparse.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/argparse.py](https://github.com/python/cpython/tree/3.6/Lib/argparse.py)

## [16.4.2. ArgumentParser オブジェクト](https://docs.python.jp/3/library/argparse.html#argumentparser-objects)

属性|概要
----|----
class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True)|新しい ArgumentParser オブジェクトを生成します。すべての引数はキーワード引数として渡すべきです。

引数|概要|デフォルト
----|----|----------
prog|プログラム名|sys.argv[0]
usage|プログラムの利用方法を記述する文字列|パーサーに追加された引数から生成されます
description|引数のヘルプの前に表示されるテキスト|none
epilog|引数のヘルプの後で表示されるテキスト|none
parents|ArgumentParser オブジェクトのリストで、このオブジェクトの引数が追加されます| 
formatter_class|ヘルプ出力をカスタマイズするためのクラス| 
prefix_chars|オプションの引数の prefix になる文字集合|'-'
fromfile_prefix_chars|追加の引数を読み込むファイルの prefix になる文字集合|None
argument_default|引数のグローバルなデフォルト値|None
conflict_handler|衝突するオプションを解決する方法 (通常は不要)| 
add_help|-h/--help オプションをパーサーに追加する|True
allow_abbrev|長いオプションが先頭の 1 文字に短縮可能 (先頭の文字が一意) である場合に短縮指定を許可する。|True

> 以下の節では各オプションの利用方法を説明します。

### [16.4.2.1. prog](https://docs.python.jp/3/library/argparse.html#prog)

> デフォルトでは、ArgumentParser オブジェクトはヘルプメッセージ中に表示するプログラム名を sys.argv[0] から取得します。 このデフォルトの動作は、プログラムがコマンドライン上の起動方法に合わせてヘルプメッセージを作成するため、ほとんどの場合望ましい挙動になります。 例えば、myprogram.py という名前のファイルに次のコードがあるとします:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()
```

> このプログラムのヘルプは、プログラム名として (プログラムがどこから起動されたのかに関わらず) myprogram.py を表示します:

```sh
$ python myprogram.py --help
usage: myprogram.py [-h] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo help
$ cd ..
$ python subdir/myprogram.py --help
usage: myprogram.py [-h] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo help
```

> このデフォルトの動作を変更するには、ArgumentParser の prog= 引数に他の値を指定します:

```python
>>> parser = argparse.ArgumentParser(prog='myprogram')
>>> parser.print_help()
usage: myprogram [-h]

optional arguments:
 -h, --help  show this help message and exit
```

> プログラム名は、sys.argv[0] から取られた場合でも prog= 引数で与えられた場合でも、ヘルプメッセージ中では %(prog)s フォーマット指定子で利用できます。

```python
>>> parser = argparse.ArgumentParser(prog='myprogram')
>>> parser.add_argument('--foo', help='foo of the %(prog)s program')
>>> parser.print_help()
usage: myprogram [-h] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo of the myprogram program
```

### [16.4.2.2. usage](https://docs.python.jp/3/library/argparse.html#usage)

> デフォルトでは、 ArgumentParser は使用法メッセージを、保持している引数から生成します:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--foo', nargs='?', help='foo help')
>>> parser.add_argument('bar', nargs='+', help='bar help')
>>> parser.print_help()
usage: PROG [-h] [--foo [FOO]] bar [bar ...]

positional arguments:
 bar          bar help

optional arguments:
 -h, --help   show this help message and exit
 --foo [FOO]  foo help
```

> デフォルトのメッセージは usage= キーワード引数で変更できます:

```python
>>> parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
>>> parser.add_argument('--foo', nargs='?', help='foo help')
>>> parser.add_argument('bar', nargs='+', help='bar help')
>>> parser.print_help()
usage: PROG [options]

positional arguments:
 bar          bar help

optional arguments:
 -h, --help   show this help message and exit
 --foo [FOO]  foo help
```

> %(prog)s フォーマット指定子を、使用法メッセージ内でプログラム名として利用できます。

### [16.4.2.3. description](https://docs.python.jp/3/library/argparse.html#description)

> 多くの場合、ArgumentParser のコンストラクターを呼び出すときに description= キーワード引数が使用されます。この引数はプログラムが何をしてどう動くのかについての短い説明になります。ヘルプメッセージで、この説明がコマンドラインの利用法と引数のヘルプメッセージの間に表示されます:

```python
>>> parser = argparse.ArgumentParser(description='A foo that bars')
>>> parser.print_help()
usage: argparse.py [-h]

A foo that bars

optional arguments:
 -h, --help  show this help message and exit
```

> デフォルトでは、説明は与えられたスペースに合わせて折り返されます。この挙動を変更するには、formatter_class 引数を参照してください。

### [16.4.2.4. epilog](https://docs.python.jp/3/library/argparse.html#epilog)

> いくつかのプログラムは、プログラムについての追加の説明を引数の説明の後に表示します。このテキストは ArgumentParser の epilog= 引数に指定できます:

```python
>>> parser = argparse.ArgumentParser(
...     description='A foo that bars',
...     epilog="And that's how you'd foo a bar")
>>> parser.print_help()
usage: argparse.py [-h]

A foo that bars

optional arguments:
 -h, --help  show this help message and exit

And that's how you'd foo a bar
```

> description 引数と同じく、epilog= テキストもデフォルトで折り返され、ArgumentParser の formatter_class 引数で動作を調整できます。

### [16.4.2.5. parents](https://docs.python.jp/3/library/argparse.html#parents)

> ときどき、いくつかのパーサーが共通の引数セットを共有することがあります。それらの引数を繰り返し定義する代わりに、すべての共通引数を持ったパーサーを ArgumentParser の parents= 引数に渡すことができます。 parents= 引数は ArgumentParser オブジェクトのリストを受け取り、すべての位置アクションとオプションのアクションをそれらから集め、そのアクションを構築中の ArgumentParser オブジェクトに追加します:

```python
>>> parent_parser = argparse.ArgumentParser(add_help=False)
>>> parent_parser.add_argument('--parent', type=int)

>>> foo_parser = argparse.ArgumentParser(parents=[parent_parser])
>>> foo_parser.add_argument('foo')
>>> foo_parser.parse_args(['--parent', '2', 'XXX'])
Namespace(foo='XXX', parent=2)

>>> bar_parser = argparse.ArgumentParser(parents=[parent_parser])
>>> bar_parser.add_argument('--bar')
>>> bar_parser.parse_args(['--bar', 'YYY'])
Namespace(bar='YYY', parent=None)
```

> 一番親になるパーサーに add_help=False を指定していることに注目してください。こうしないと、ArgumentParser は2つの -h/--help オプションを与えられる (1つは親から、もうひとつは子から) ことになり、エラーを発生します。

> 注釈

> parents= に渡す前にパーサーを完全に初期化する必要があります。子パーサーを作成してから親パーサーを変更した場合、その変更は子パーサーに反映されません。

### [16.4.2.6. formatter_class](https://docs.python.jp/3/library/argparse.html#formatter-class)

> ArgumentParser オブジェクトは代わりのフォーマットクラスを指定することでヘルプのフォーマットをカスタマイズできます。現在、4つのフォーマットクラスがあります:

* class argparse.RawDescriptionHelpFormatter
* class argparse.RawTextHelpFormatter
* class argparse.ArgumentDefaultsHelpFormatter
* class argparse.MetavarTypeHelpFormatter

> RawDescriptionHelpFormatter と RawTextHelpFormatter はどのようにテキストの説明を表示するかを指定できます。デフォルトでは ArgumentParser オブジェクトはコマンドラインヘルプの中の description と epilog を折り返して表示します:

```python
>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     description='''this description
...         was indented weird
...             but that is okay''',
...     epilog='''
...             likewise for this epilog whose whitespace will
...         be cleaned up and whose words will be wrapped
...         across a couple lines''')
>>> parser.print_help()
usage: PROG [-h]

this description was indented weird but that is okay

optional arguments:
 -h, --help  show this help message and exit

likewise for this epilog whose whitespace will be cleaned up and whose words
will be wrapped across a couple lines

formatter_class= に RawDescriptionHelpFormatter を渡した場合、 description と epilog は整形済みとされ改行されません:
>>>

>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     formatter_class=argparse.RawDescriptionHelpFormatter,
...     description=textwrap.dedent('''\
...         Please do not mess up this text!
...         --------------------------------
...             I have indented it
...             exactly the way
...             I want it
...         '''))
>>> parser.print_help()
usage: PROG [-h]

Please do not mess up this text!
--------------------------------
   I have indented it
   exactly the way
   I want it

optional arguments:
 -h, --help  show this help message and exit

RawTextHelpFormatter maintains whitespace for all sorts of help text, including argument descriptions. However, multiple new lines are replaced with one. If you wish to preserve multiple blank lines, add spaces between the newlines.
```

> ArgumentDefaultsHelpFormatter は各引数のデフォルト値を自動的にヘルプに追加します:

```python
>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
>>> parser.add_argument('--foo', type=int, default=42, help='FOO!')
>>> parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
>>> parser.print_help()
usage: PROG [-h] [--foo FOO] [bar [bar ...]]

positional arguments:
 bar         BAR! (default: [1, 2, 3])

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   FOO! (default: 42)

MetavarTypeHelpFormatter は、各引数の値の表示名に type 引数の値を使用します (通常は dest の値が使用されます):
>>>

>>> parser = argparse.ArgumentParser(
...     prog='PROG',
...     formatter_class=argparse.MetavarTypeHelpFormatter)
>>> parser.add_argument('--foo', type=int)
>>> parser.add_argument('bar', type=float)
>>> parser.print_help()
usage: PROG [-h] [--foo int] float

positional arguments:
  float

optional arguments:
  -h, --help  show this help message and exit
  --foo int
```

### [16.4.2.7. prefix_chars](https://docs.python.jp/3/library/argparse.html#prefix-chars)

> ほとんどのコマンドラインオプションは、-f/--foo のように接頭辞に - を使います。+f や /foo のような、他の、あるいは追加の接頭辞文字をサポートしなければならない場合、ArgumentParser のコンストラクターに prefix_chars= 引数を使って指定します:

```python
>>> parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
>>> parser.add_argument('+f')
>>> parser.add_argument('++bar')
>>> parser.parse_args('+f X ++bar Y'.split())
Namespace(bar='Y', f='X')
```

> prefix_chars= 引数のデフォルトは '-' です。- を含まない文字セットを指定すると、-f/--foo オプションが使用できなくなります。

### [16.4.2.8. fromfile_prefix_chars](https://docs.python.jp/3/library/argparse.html#fromfile-prefix-chars)

> ときどき、例えば非常に長い引数リストを扱う場合に、その引数リストを毎回コマンドラインにタイプする代わりにファイルに置いておきたい場合があります。ArgumentParser のコンストラクターに fromfile_prefix_chars= 引数が渡された場合、指定された文字のいずれかで始まる引数はファイルとして扱われ、そのファイルに含まれる引数リストに置換されます。例えば:

```python
>>> with open('args.txt', 'w') as fp:
...     fp.write('-f\nbar')
>>> parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
>>> parser.add_argument('-f')
>>> parser.parse_args(['-f', 'foo', '@args.txt'])
Namespace(f='bar')
```

> ファイルから読み込まれる引数は、デフォルトでは1行に1つ (ただし、convert_arg_line_to_args() も参照してください) で、コマンドライン上でファイルを参照する引数があった場所にその引数があったものとして扱われます。このため、上の例では、['-f', 'foo', '@args.txt'] は ['-f', 'foo', '-f', 'bar'] と等価になります。

> fromfile_prefix_chars= 引数のデフォルト値は None で、引数がファイル参照として扱われることがないことを意味しています。

### [16.4.2.9. argument_default](https://docs.python.jp/3/library/argparse.html#argument-default)

> 一般的には、引数のデフォルト値は add_argument() メソッドにデフォルト値を渡すか、set_defaults() メソッドに名前と値のペアを渡すことで指定します。しかしまれに、1つのパーサー全体に適用されるデフォルト引数が便利なことがあります。これを行うには、 ArgumentParser に argument_default= キーワード引数を渡します。例えば、全体で parse_args() メソッド呼び出しの属性の生成を抑制するには、argument_default=SUPPRESS を指定します:

```python
>>> parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
>>> parser.add_argument('--foo')
>>> parser.add_argument('bar', nargs='?')
>>> parser.parse_args(['--foo', '1', 'BAR'])
Namespace(bar='BAR', foo='1')
>>> parser.parse_args([])
Namespace()
```

### [16.4.2.10. allow_abbrev](https://docs.python.jp/3/library/argparse.html#allow-abbrev)

> 通常、ArgumentParser の parse_args() に引数のリストを渡すとき、長いオプションは 短縮しても認識されます。

> この機能は、allow_abbrev に False を指定することで無効にできます:

```python
>>> parser = argparse.ArgumentParser(prog='PROG', allow_abbrev=False)
>>> parser.add_argument('--foobar', action='store_true')
>>> parser.add_argument('--foonley', action='store_false')
>>> parser.parse_args(['--foon'])
usage: PROG [-h] [--foobar] [--foonley]
PROG: error: unrecognized arguments: --foon
```

### [16.4.2.11. conflict_handler](https://docs.python.jp/3/library/argparse.html#conflict-handler)

> ArgumentParser オブジェクトは同じオプション文字列に対して複数のアクションを許可していません。 デフォルトでは、ArgumentParser オブジェクトは、すでに利用されているオプション文字列を使って新しい引数をつくろうとしたときに例外を送出します:

```python
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-f', '--foo', help='old foo help')
>>> parser.add_argument('--foo', help='new foo help')
Traceback (most recent call last):
 ..
ArgumentError: argument --foo: conflicting option string(s): --foo
```

> ときどき (例えば parents を利用する場合など)、古い引数を同じオプション文字列で上書きするほうが便利な場合があります。この動作をするには、ArgumentParser の conflict_handler= 引数に 'resolve' を渡します:

```python
>>> parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')
>>> parser.add_argument('-f', '--foo', help='old foo help')
>>> parser.add_argument('--foo', help='new foo help')
>>> parser.print_help()
usage: PROG [-h] [-f FOO] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 -f FOO      old foo help
 --foo FOO   new foo help
```

> ArgumentParser オブジェクトは、すべてのオプション文字列が上書きされた場合にだけアクションを削除することに注目してください。上の例では、 --foo オプション文字列だけが上書きされているので、古い -f/--foo アクションは -f アクションとして残っています。

### [16.4.2.12. add_help](https://docs.python.jp/3/library/argparse.html#add-help)

> デフォルトでは、ArgumentParser オブジェクトはシンプルにパーサーのヘルプメッセージを表示するオプションを自動的に追加します。例えば、以下のコードを含む myprogram.py ファイルについて考えてください:


```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()
```

> コマンドラインに -h か --help が指定された場合、ArgumentParser の help が表示されます:

```sh
$ python myprogram.py --help
usage: myprogram.py [-h] [--foo FOO]

optional arguments:
 -h, --help  show this help message and exit
 --foo FOO   foo help
```

> 必要に応じて、この help オプションを無効にする場合があります。これは ArgumentParser の add_help= 引数に False を渡すことで可能です:

```python
>>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
>>> parser.add_argument('--foo', help='foo help')
>>> parser.print_help()
usage: PROG [--foo FOO]

optional arguments:
 --foo FOO  foo help
```

> ヘルプオプションは通常 -h/--help です。例外は prefix_chars= が指定されてその中に - が無かった場合で、その場合は -h と --help は有効なオプションではありません。この場合、prefix_chars の最初の文字がヘルプオプションの接頭辞として利用されます:

```python
>>> parser = argparse.ArgumentParser(prog='PROG', prefix_chars='+/')
>>> parser.print_help()
usage: PROG [+h]

optional arguments:
  +h, ++help  show this help message and exit
```

