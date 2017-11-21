# [16.4.5. その他のユーティリティ](https://docs.python.jp/3/library/argparse.html#other-utilities)

< [16.4. argparse — コマンドラインオプション、引数、サブコマンドのパーサー](https://docs.python.jp/3/library/argparse.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/argparse.py](https://github.com/python/cpython/tree/3.6/Lib/argparse.py)

## [16.4.5.1. サブコマンド](https://docs.python.jp/3/library/argparse.html#sub-commands)

属性|概要
----|----
ArgumentParser.add_subparsers([title][, description][, prog][, parser_class][, action][, option_string][, dest][, help][, metavar])|多くのプログラムは、その機能をサブコマンドへと分割します。 例えば svn プログラムは svn checkout, svn update, svn commit などのサブコマンドを利用できます。 機能をサブコマンドに分割するのは、プログラムがいくつかの異なった機能を持っていて、 それぞれが異なるコマンドライン引数を必要とする場合には良いアイデアです。 ArgumentParser は add_subparsers() メソッドによりサブコマンドを サポートしています。 add_subparsers() メソッドは通常引数なしに呼び出され、 特殊なアクションオブジェクトを返します。このオブジェクトには1つのメソッド add_parser() があり、コマンド名と ArgumentParser コンストラクターの任意の引数を受け取り、通常の方法で操作できる ArgumentParser オブジェクトを返します。

> 引数の説明:

引数|説明
----|----
title|ヘルプ出力でのサブパーサーグループのタイトルです。デフォルトは、description が指定されている場合は "subcommands" に、指定されていない場合は位置引数のタイトルになります
description|ヘルプ出力に表示されるサブパーサーグループの説明です。デフォルトは None になります
prog|サブコマンドのヘルプに表示される使用方法の説明です。デフォルトではプログラム名と位置引数の後ろに、サブパーサーの引数が続きます
parser_class|サブパーサーのインスタンスを作成するときに使用されるクラスです。デフォルトでは現在のパーサーのクラス (例: ArgumentParser) になります
action|コマンドラインにこの引数があったときの基本のアクション。
dest|サブコマンド名を格納する属性の名前です。デフォルトは None で値は格納されません
help|ヘルプ出力に表示されるサブパーサーグループのヘルプです。デフォルトは None です
metavar|利用可能なサブコマンドをヘルプ内で表示するための文字列です。デフォルトは None で、サブコマンドを {cmd1, cmd2, ..} のような形式で表します

> いくつかの使用例:

```python
# create the top-level parser
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(help='sub-command help')

# create the parser for the "a" command
parser_a = subparsers.add_parser('a', help='a help')
parser_a.add_argument('bar', type=int, help='bar help')

# create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices='XYZ', help='baz help')

# parse some argument lists
parser.parse_args(['a', '12'])
parser.parse_args(['--foo', 'b', '--baz', 'Z'])
```

> parse_args() が返すオブジェクトにはメインパーサーとコマンドラインで選択されたサブパーサーによる属性だけが設定されており、選択されなかったサブコマンドのパーサーの属性が設定されていないことに注意してください。このため、上の例では、a コマンドが指定されたときは foo, bar 属性だけが存在し、b コマンドが指定されたときは foo, baz 属性だけが存在しています。

> 同じように、サブパーサーにヘルプメッセージが要求された場合は、そのパーサーに対するヘルプだけが表示されます。ヘルプメッセージには親パーサーや兄弟パーサーのヘルプメッセージを表示しません。 (ただし、各サブパーサーコマンドのヘルプメッセージは、上の例にもあるように add_parser() の help= 引数によって指定できます)

```sh
parser.parse_args(['--help'])
usage: PROG [-h] [--foo] {a,b}    

positional arguments:
  {a,b}   sub-command help
    a     a help
    b     b help

optional arguments:
  -h, --help  show this help message and exit
  --foo   foo help

parser.parse_args(['a', '--help'])
usage: PROG a [-h] bar

positional arguments:
  bar     bar help

optional arguments:
  -h, --help  show this help message and exit

parser.parse_args(['b', '--help'])
usage: PROG b [-h] [--baz {X,Y,Z}]

optional arguments:
  -h, --help     show this help message and exit
  --baz {X,Y,Z}  baz help
```

> add_subparsers() メソッドは title と description キーワード引数もサポートしています。どちらかが存在する場合、サブパーサーのコマンドはヘルプ出力でそれぞれのグループの中に表示されます。例えば:

```python
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands',
                                       description='valid subcommands',
                                       help='additional help')
subparsers.add_parser('foo')
subparsers.add_parser('bar')
parser.parse_args(['-h'])
usage:  [-h] {foo,bar}    

optional arguments:
  -h, --help  show this help message and exit

subcommands:
  valid subcommands

  {foo,bar}   additional help
```

> さらに、add_parser は aliases 引数もサポートしており、同じサブパーサーに対して複数の文字列で参照することもできます。以下の例では svn のように checkout の短縮形として co を使用できるようにしています:

```python
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
checkout = subparsers.add_parser('checkout', aliases=['co'])
checkout.add_argument('foo')
parser.parse_args(['co', 'bar'])
Namespace(foo='bar')
```

> サブコマンドを扱う1つの便利な方法は add_subparsers() メソッドと set_defaults() を組み合わせて、各サブパーサーにどの Python 関数を実行するかを教えることです。例えば:

```python
# sub-command functions
def foo(args):
        print(args.x * args.y)
   
def bar(args):
        print('((%s))' % args.z)
   
# create the top-level parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# create the parser for the "foo" command
parser_foo = subparsers.add_parser('foo')
parser_foo.add_argument('-x', type=int, default=1)
parser_foo.add_argument('y', type=float)
parser_foo.set_defaults(func=foo)

# create the parser for the "bar" command
parser_bar = subparsers.add_parser('bar')
parser_bar.add_argument('z')
parser_bar.set_defaults(func=bar)

# parse the args and call whatever function was selected
args = parser.parse_args('foo 1 -x 2'.split())
args.func(args)
2.0

# parse the args and call whatever function was selected
args = parser.parse_args('bar XYZYX'.split())
args.func(args)
((XYZYX))
```

> こうすると、parse_args() が引数の解析が終わってから適切な関数を呼び出すようになります。このように関数をアクションに関連付けるのは一般的にサブパーサーごとに異なるアクションを扱うもっとも簡単な方法です。ただし、実行されたサブパーサーの名前を確認する必要がある場合は、add_subparsers() を呼び出すときに dest キーワードを指定できます:

```python
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='subparser_name')
subparser1 = subparsers.add_parser('1')
subparser1.add_argument('-x')
subparser2 = subparsers.add_parser('2')
subparser2.add_argument('y')
parser.parse_args(['2', 'frobble'])
```

```python
# create the top-level parser
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(help='sub-command help')

# create the parser for the "a" command
parser_a = subparsers.add_parser('a', help='a help')
parser_a.add_argument('bar', type=int, help='bar help')

# create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices='XYZ', help='baz help')

# parse some argument lists
parser.parse_args(['a', '12'])
parser.parse_args(['--foo', 'b', '--baz', 'Z'])
```

> parse_args() が返すオブジェクトにはメインパーサーとコマンドラインで選択されたサブパーサーによる属性だけが設定されており、選択されなかったサブコマンドのパーサーの属性が設定されていないことに注意してください。このため、上の例では、a コマンドが指定されたときは foo, bar 属性だけが存在し、b コマンドが指定されたときは foo, baz 属性だけが存在しています。

> 同じように、サブパーサーにヘルプメッセージが要求された場合は、そのパーサーに対するヘルプだけが表示されます。ヘルプメッセージには親パーサーや兄弟パーサーのヘルプメッセージを表示しません。 (ただし、各サブパーサーコマンドのヘルプメッセージは、上の例にもあるように add_parser() の help= 引数によって指定できます)

```python
print(parser.parse_args(['--help']))
print(parser.parse_args(['a', '--help']))
```

> add_subparsers() メソッドは title と description キーワード引数もサポートしています。どちらかが存在する場合、サブパーサーのコマンドはヘルプ出力でそれぞれのグループの中に表示されます。例えば:

```python
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands',
                                   description='valid subcommands',
                                   help='additional help')
subparsers.add_parser('foo')
subparsers.add_parser('bar')
print(parser.parse_args(['-h']))
```

> さらに、add_parser は aliases 引数もサポートしており、同じサブパーサーに対して複数の文字列で参照することもできます。以下の例では svn のように checkout の短縮形として co を使用できるようにしています:

```python
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
checkout = subparsers.add_parser('checkout', aliases=['co'])
checkout.add_argument('foo')
print(parser.parse_args(['co', 'bar']))
```

> サブコマンドを扱う1つの便利な方法は add_subparsers() メソッドと set_defaults() を組み合わせて、各サブパーサーにどの Python 関数を実行するかを教えることです。例えば:

```python
# sub-command functions
def foo(args):
    print(args.x * args.y)

def bar(args):
    print('((%s))' % args.z)

# create the top-level parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# create the parser for the "foo" command
parser_foo = subparsers.add_parser('foo')
parser_foo.add_argument('-x', type=int, default=1)
parser_foo.add_argument('y', type=float)
parser_foo.set_defaults(func=foo)

# create the parser for the "bar" command
parser_bar = subparsers.add_parser('bar')
parser_bar.add_argument('z')
parser_bar.set_defaults(func=bar)

# parse the args and call whatever function was selected
args = parser.parse_args('foo 1 -x 2'.split())
args.func(args)

# parse the args and call whatever function was selected
args = parser.parse_args('bar XYZYX'.split())
args.func(args)
```

> こうすると、parse_args() が引数の解析が終わってから適切な関数を呼び出すようになります。このように関数をアクションに関連付けるのは一般的にサブパーサーごとに異なるアクションを扱うもっとも簡単な方法です。ただし、実行されたサブパーサーの名前を確認する必要がある場合は、add_subparsers() を呼び出すときに dest キーワードを指定できます:

```python
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='subparser_name')
subparser1 = subparsers.add_parser('1')
subparser1.add_argument('-x')
subparser2 = subparsers.add_parser('2')
subparser2.add_argument('y')
print(parser.parse_args(['2', 'frobble']))
```

### [16.4.5.2. FileType オブジェクト](https://docs.python.jp/3/library/argparse.html#filetype-objects)

属性|概要
----|----
class argparse.FileType(mode='r', bufsize=-1, encoding=None, errors=None)|FileType ファクトリは ArgumentParser.add_argument() の type 引数に渡すことができるオブジェクトを生成します。 type が FileType オブジェクトである引数はコマンドライン引数を、指定されたモード、バッファーサイズ、エンコーディング、エラー処理でファイルとして開きます (詳細は open() 関数を参照してください。):

```python
parser = argparse.ArgumentParser()
parser.add_argument('--raw', type=argparse.FileType('wb', 0))
parser.add_argument('out', type=argparse.FileType('w', encoding='UTF-8'))
print(parser.parse_args(['--raw', 'raw.dat', 'file.txt']))
```

> FileType オブジェクトは擬似引数 '-' を識別し、読み込み用の FileType であれば sys.stdin を、書き込み用の FileType であれば sys.stdout に変換します:

```python
parser = argparse.ArgumentParser()
parser.add_argument('infile', type=argparse.FileType('r'))
parser.parse_args(['-'])
print(Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>))
```

> バージョン 3.4 で追加: encoding および errors キーワードが追加されました。

### [16.4.5.3. 引数グループ](https://docs.python.jp/3/library/argparse.html#argument-groups)



ArgumentParser.add_argument_group(title=None, description=None)(原文)

    デフォルトでは、 ArgumentParser はヘルプメッセージを表示するときに、コマンドライン引数を "位置引数" と "オプション引数" にグループ化します。このデフォルトの動作よりも良い引数のグループ化方法がある場合、 add_argument_group() メソッドで適切なグループを作成できます:

```python
parser = argparse.ArgumentParser(prog='PROG', add_help=False)
group = parser.add_argument_group('group')
group.add_argument('--foo', help='foo help')
group.add_argument('bar', help='bar help')
parser.print_help()
usage: PROG [--foo FOO] bar

group:
  bar    bar help
  --foo FOO  foo help
```

    add_argument_group() メソッドは、通常の ArgumentParser と同じような add_argument() メソッドを持つ引数グループオブジェクトを返します。引数がグループに追加された時、パーサーはその引数を通常の引数のように扱いますが、ヘルプメッセージではその引数を分離されたグループの中に表示します。 add_argument_group() メソッドには、この表示をカスタマイズするための title と description 引数があります:

```python
parser = argparse.ArgumentParser(prog='PROG', add_help=False)
group1 = parser.add_argument_group('group1', 'group1 description')
group1.add_argument('foo', help='foo help')
group2 = parser.add_argument_group('group2', 'group2 description')
group2.add_argument('--bar', help='bar help')
parser.print_help()
usage: PROG [--bar BAR] foo

group1:
  group1 description

  foo    foo help

group2:
  group2 description

  --bar BAR  bar help
```
    ユーザー定義グループにないすべての引数は通常の "位置引数" と "オプション引数" セクションに表示されます。


### [16.4.5.4. 相互排他](https://docs.python.jp/3/library/argparse.html#mutual-exclusion)



ArgumentParser.add_mutually_exclusive_group(required=False)(原文)

    相互排他グループを作ります。argparse は相互排他グループの中でただ1つの引数のみが存在することを確認します:

```python
parser = argparse.ArgumentParser(prog='PROG')
group = parser.add_mutually_exclusive_group()
group.add_argument('--foo', action='store_true')
group.add_argument('--bar', action='store_false')
print(parser.parse_args(['--foo']))
print(parser.parse_args(['--bar']))
print(parser.parse_args(['--foo', '--bar']))
```

    add_mutually_exclusive_group() メソッドの引数 required に True 値を指定すると、その相互排他引数のどれか 1つを選ぶことが要求さます:

```python
parser = argparse.ArgumentParser(prog='PROG')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--foo', action='store_true')
group.add_argument('--bar', action='store_false')
print(parser.parse_args([]))
```

    現在のところ、相互排他引数グループは add_argument_group() の title と description 引数をサポートしていません。


### [16.4.5.5. パーサーのデフォルト値](https://docs.python.jp/3/library/argparse.html#parser-defaults)



ArgumentParser.set_defaults(**kwargs)(原文)

    ほとんどの場合、 parse_args() が返すオブジェクトの属性はコマンドライン引数の内容と引数のアクションによってのみ決定されます。 set_defaults() を使うと与えられたコマンドライン引数の内容によらず追加の属性を決定することが可能です:

```python
parser = argparse.ArgumentParser()
parser.add_argument('foo', type=int)
parser.set_defaults(bar=42, baz='badger')
print(parser.parse_args(['736']))
```

    パーサーレベルのデフォルト値は常に引数レベルのデフォルト値を上書きします:

```python
parser = argparse.ArgumentParser()
parser.add_argument('--foo', default='bar')
parser.set_defaults(foo='spam')
print(parser.parse_args([]))
```

    パーサーレベルの default は、複数のパーサーを扱うときに特に便利です。このタイプの例については add_subparsers() メソッドを参照してください。

ArgumentParser.get_default(dest)(原文)

    add_argument() か set_defaults() によって指定された、 namespace の属性のデフォルト値を取得します:

```python
parser = argparse.ArgumentParser()
parser.add_argument('--foo', default='badger')
print(parser.get_default('foo'))
```

### [16.4.5.6. ヘルプの表示](https://docs.python.jp/3/library/argparse.html#printing-help)



ほとんどの典型的なアプリケーションでは、parse_args() が使用法やエラーメッセージのフォーマットと表示について面倒を見ます。しかし、いくつかのフォーマットメソッドが利用できます:

ArgumentParser.print_usage(file=None)(原文)

    ArgumentParser がコマンドラインからどう実行されるべきかの短い説明を表示します。 file が None の時は、 sys.stdout に出力されます。

ArgumentParser.print_help(file=None)(原文)

    プログラムの使用法と ArgumentParser に登録された引数についての情報を含むヘルプメッセージを表示します。 file が None の時は、 sys.stdout に出力されます。

これらのメソッドの、表示する代わりにシンプルに文字列を返すバージョンもあります:

ArgumentParser.format_usage()(原文)

    ArgumentParser がコマンドラインからどう実行されるべきかの短い説明を格納した文字列を返します。

ArgumentParser.format_help()(原文)

    プログラムの使用法と ArgumentParser に登録された引数についての情報を含むヘルプメッセージを格納した文字列を返します。


### [16.4.5.7. 部分解析](https://docs.python.jp/3/library/argparse.html#partial-parsing)

ArgumentParser.parse_known_args(args=None, namespace=None)(原文)

ときどき、スクリプトがコマンドライン引数のいくつかだけを解析し、残りの引数は別のスクリプトやプログラムに渡すことがあります。こういった場合、 parse_known_args() メソッドが便利です。これは parse_args() と同じように動作しますが、余分な引数が存在してもエラーを生成しません。代わりに、評価された namespace オブジェクトと、残りの引数文字列のリストからなる2要素タプルを返します。

```python
parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_true')
parser.add_argument('bar')
print(parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam']))
```

警告

先頭文字でのマッチング ルールは parse_known_args() にも適用されます。たとえ既知のオプションの先頭文字に過ぎない場合でも、パーサは引数リストに残さずに、オプションを受け取る場合があります。


### [16.4.5.8. ファイル解析のカスタマイズ](https://docs.python.jp/3/library/argparse.html#customizing-file-parsing)



ArgumentParser.convert_arg_line_to_args(arg_line)(原文)

    ファイルから引数を読み込む場合 (ArgumentParser コンストラクターの fromfile_prefix_chars キーワード引数を参照)、1行につき1つの引数を読み込みます。 convert_arg_line_to_args() を変更することでこの動作をカスタマイズできます。

    このメソッドは、引数ファイルから読まれた文字列である1つの引数 arg_line を受け取ります。そしてその文字列を解析した結果の引数のリストを返します。このメソッドはファイルから1行読みこむごとに、順番に呼ばれます。

    このメソッドをオーバーライドすると便利なこととして、スペースで区切られた単語を 1 つの引数として扱えます。次の例でその方法を示します:

    class MyArgumentParser(argparse.ArgumentParser):
        def convert_arg_line_to_args(self, arg_line):
            return arg_line.split()



### [16.4.5.9. 終了メソッド](https://docs.python.jp/3/library/argparse.html#exiting-methods)



ArgumentParser.exit(status=0, message=None)(原文)

    このメソッドは、message が指定されていればそれを表示した後、指定された終了ステータス status でプログラムを終了します。

ArgumentParser.error(message)(原文)

    このメソッドは message を含む使用法メッセージを標準エラーに表示して、終了ステータス 2 でプログラムを終了します。

## [16.4.6. optparse からのアップグレード](https://docs.python.jp/3/library/argparse.html#upgrading-optparse-code)



もともと、argparse モジュールは optparse モジュールとの互換性を保って開発しようと試みられました。しかし、特に新しい nargs= 指定子とより良い使用法メッセージのために必要な変更のために、optparse を透過的に拡張することは難しかったのです。optparse のほとんどすべてがコピーアンドペーストされたりモンキーパッチを当てられたりしたとき、もはや後方互換性を保とうとすることは現実的ではありませんでした。

argparse モジュールは標準ライブラリ optparse モジュールを、以下を含むたくさんの方法で改善しています:

    位置指定引数を扱う
    サブコマンドのサポート
    +, / のような代替オプションプレフィクスを許容する
    zero-or-more スタイル、one-or-more スタイルの引数を扱う
    より有益な使用方法メッセージの生成
    カスタム type, カスタム action のために遥かに簡単なインターフェイスを提供する

optparse から argparse への現実的なアップグレードパス:

    すべての optparse.OptionParser.add_option() の呼び出しを、ArgumentParser.add_argument() の呼び出しに置き換える。
    Replace (options, args) = parser.parse_args() with args = parser.parse_args() and add additional ArgumentParser.add_argument() calls for the positional arguments. Keep in mind that what was previously called options, now in the argparse context is called args.
    Replace optparse.OptionParser.disable_interspersed_args() by setting nargs of a positional argument to argparse.REMAINDER, or use parse_known_args() to collect unparsed argument strings in a separate list.
    コールバック・アクションと callback_* キーワード引数を type や action 引数に置き換える。
    type キーワード引数に渡していた文字列の名前を、それに応じたオブジェクト (例: int, float, complex, …) に置き換える。
    optparse.Values を Namespace に置き換え、optparse.OptionError と optparse.OptionValueError を ArgumentError に置き換える。
    %default や %prog などの暗黙の引数を含む文字列を、%(default)s や %(prog)s などの、通常の Python で辞書を使う場合のフォーマット文字列に置き換える。
    OptionParser のコンストラクターの version 引数を、parser.add_argument('--version', action='version', version='<the version>') に置き換える

