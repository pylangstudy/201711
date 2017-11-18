# [16.4. argparse — コマンドラインオプション、引数、サブコマンドのパーサー](https://docs.python.jp/3/library/argparse.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/argparse.py](https://github.com/python/cpython/tree/3.6/Lib/argparse.py)

> argparse モジュールはユーザーフレンドリなコマンドラインインターフェースの作成を簡単にします。プログラムがどんな引数を必要としているのかを定義すると、argparse が sys.argv からそのオプションを解析する方法を見つけ出します。argparse モジュールは自動的にヘルプと使用方法メッセージを生成し、ユーザーが不正な引数をプログラムに指定したときにエラーを発生させます。

* [Tutorial](https://docs.python.jp/3/howto/argparse.html#id1)

## [16.4.1. 使用例](https://docs.python.jp/3/library/argparse.html#example)

> 次のコードは、整数のリストを受け取って合計か最大値を返す Python プログラムです:

```python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
```

上の Python コードが prog.py という名前のファイルに保存されたと仮定します。コマンドラインから便利なヘルプメッセージを表示できます:


```python
$ python prog.py -h
usage: prog.py [-h] [--sum] N [N ...]

Process some integers.

positional arguments:
 N           an integer for the accumulator

optional arguments:
 -h, --help  show this help message and exit
 --sum       sum the integers (default: find the max)
```

> 適切な引数を与えて実行した場合、このプログラムはコマンドライン引数の整数列の合計か最大値を表示します:

```python
$ python prog.py 1 2 3 4
4

$ python prog.py 1 2 3 4 --sum
10
```

> 不正な引数が与えられた場合、エラーを発生させます:

```python
$ python prog.py a b c
usage: prog.py [-h] [--sum] N [N ...]
prog.py: error: argument N: invalid int value: 'a'
```

> 以降の節では、この例をひと通り説明して行きます。


### [16.4.1.1. パーサーを作る](https://docs.python.jp/3/library/argparse.html#creating-a-parser)

> argparse を使うときの最初のステップは、ArgumentParser オブジェクトを生成することです:

```python
>>> parser = argparse.ArgumentParser(description='Process some integers.')
```

> ArgumentParser オブジェクトはコマンドラインを解析して Python データ型にするために必要なすべての情報を保持します。

### [16.4.1.2. 引数を追加する](https://docs.python.jp/3/library/argparse.html#adding-arguments)

> ArgumentParser にプログラム引数の情報を与えるために、add_argument() メソッドを呼び出します。一般的に、このメソッドの呼び出しは ArgumentParser に、コマンドラインの文字列を受け取ってそれをオブジェクトにする方法を教えます。この情報は保存され、parse_args() が呼び出されたときに利用されます。例えば:

```python
>>> parser.add_argument('integers', metavar='N', type=int, nargs='+',
...                     help='an integer for the accumulator')
>>> parser.add_argument('--sum', dest='accumulate', action='store_const',
...                     const=sum, default=max,
...                     help='sum the integers (default: find the max)')
```

> あとで parse_args() を呼び出すと、integers と accumulate という2つの属性を持ったオブジェクトを返します。integers 属性は1つ以上の整数のリストで、accumulate 属性はコマンドラインから --sum が指定された場合は sum() 関数に、それ以外の場合は max() 関数になります。

### [16.4.1.3. 引数を解析する](https://docs.python.jp/3/library/argparse.html#parsing-arguments)

> ArgumentParser は引数を parse_args() メソッドで解析します。このメソッドはコマンドラインを調べ、各引数を正しい型に変換して、適切なアクションを実行します。ほとんどの場合、これはコマンドラインの解析結果から、シンプルな Namespace オブジェクトを構築することを意味します:

```python
>>> parser.parse_args(['--sum', '7', '-1', '42'])
Namespace(accumulate=<built-in function sum>, integers=[7, -1, 42])
```

> スクリプト内では、parse_args() は通常引数なしで呼び出され、ArgumentParser は自動的に sys.argv からコマンドライン引数を取得します。

