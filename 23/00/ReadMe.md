# [16.5. getopt — C 言語スタイルのコマンドラインオプションパーサ](https://docs.python.jp/3/library/getopt.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/getopt.py](https://github.com/python/cpython/tree/3.6/Lib/getopt.py)

## 注釈

> getopt モジュールは、C 言語の getopt() 関数に慣れ親しんだ人ためにデザインされた API を持つコマンドラインオプションのパーサです。getopt() 関数に慣れ親しんでない人や、コードを少なくしてよりよいヘルプメッセージを表示させたい場合は、argparse モジュールの使用を検討してください。

> このモジュールは sys.argv に入っているコマンドラインオプションの構文解析を支援します。'-' や '--' の特別扱いも含めて、Unix の getopt() と同じ記法をサポートしています。3番目の引数 (省略可能) を設定することで、GNU のソフトウェアでサポートされているような長形式のオプションも利用できます。

> このモジュールは2つの関数と1つの例外を提供しています:

属性|概要
----|----
getopt.getopt(args, shortopts, longopts=[])|コマンドラインオプションとパラメータのリストを構文解析します。args は構文解析の対象になる引数のリストです。これは先頭のプログラム名を除いたもので、通常 sys.argv[1:] で与えられます。shortopts はスクリプトで認識させたいオプション文字と、引数が必要な場合にはコロン (':') をつけます。つまり Unix の getopt() と同じフォーマットになります。
getopt.gnu_getopt(args, shortopts, longopts=[])|この関数はデフォルトで GNU スタイルのスキャンモードを使う以外は getopt() と同じように動作します。つまり、オプションとオプションでない引数とを混在させることができます。getopt() 関数はオプションでない引数を見つけると解析を停止します。
exception getopt.GetoptError|引数リストの中に認識できないオプションがあった場合か、引数が必要なオプションに引数が与えられなかった場合に発生します。例外の引数は原因を示す文字列です。長形式のオプションについては、不要な引数が与えられた場合にもこの例外が発生します。 msg 属性と opt 属性で、エラーメッセージと関連するオプションを取得できます。特に関係するオプションが無い場合には opt は空文字列となります。
exception getopt.error|GetoptError へのエイリアスです。後方互換性のために残されています。

> Unix スタイルのオプションを使った例です:

```python
>>> import getopt
>>> args = '-a -b -cfoo -d bar a1 a2'.split()
>>> args
['-a', '-b', '-cfoo', '-d', 'bar', 'a1', 'a2']
>>> optlist, args = getopt.getopt(args, 'abc:d:')
>>> optlist
[('-a', ''), ('-b', ''), ('-c', 'foo'), ('-d', 'bar')]
>>> args
['a1', 'a2']
```

> 長形式のオプションを使っても同様です:

```python
>>> s = '--condition=foo --testing --output-file abc.def -x a1 a2'
>>> args = s.split()
>>> args
['--condition=foo', '--testing', '--output-file', 'abc.def', '-x', 'a1', 'a2']
>>> optlist, args = getopt.getopt(args, 'x', [
...     'condition=', 'output-file=', 'testing'])
>>> optlist
[('--condition', 'foo'), ('--testing', ''), ('--output-file', 'abc.def'), ('-x', '')]
>>> args
['a1', 'a2']
```

> スクリプト中での典型的な使い方は以下のようになります:

```python
import getopt, sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"
    # ...

if __name__ == "__main__":
    main()
```

> argparse モジュールを使えば、より良いヘルプメッセージとエラーメッセージを持った同じコマンドラインインタフェースをより少ないコードで実現できます:

```python
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output')
    parser.add_argument('-v', dest='verbose', action='store_true')
    args = parser.parse_args()
    # ... do something with args.output ...
    # ... do something with args.verbose ..
```

### 参考

モジュール|概要
----------|----
argparse|別のコマンドラインオプションと引数の解析ライブラリ。

