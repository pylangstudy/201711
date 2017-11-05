# [14.3. netrc — netrc ファイルの処理](https://docs.python.jp/3/library/netrc.html)

< [14. ファイルフォーマット](https://docs.python.jp/3/library/fileformats.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/netrc.py](https://github.com/python/cpython/tree/3.6/Lib/netrc.py)

FTPは使う機会がなく、サーバも今用意できないためパス。netrcの日本語情報もほ見つからない。

> netrc クラスは、Unix ftp プログラムや他の FTP クライアントで用いられる netrc ファイル形式を解析し、カプセル化 (encapsulate) します。

属性|概要
----|----
class netrc.netrc([file])|netrc のインスタンスやサブクラスのインスタンスは netrc ファイルのデータをカプセル化します。 初期化の際の引数が存在する場合、解析対象となるファイルの指定になります。 引数がない場合、ユーザのホームディレクトリ下にある .netrc が読み出されます。 解析エラーが発生した場合、ファイル名、行番号、解析を中断したトークンに関する情報の入った NetrcParseError を送出します。 POSIX システムにおいて引数を指定しない場合、ファイルのオーナシップやパーミッションが安全でない (プロセスを実行しているユーザ以外が所有者であるか、誰にでも読み書き出来てしまう) のに .netrc ファイル内にパスワードが含まれていると、 NetrcParseError を送出します。 このセキュリティ的な振る舞いは、 ftp などの .netrc を使うプログラムと同じものです。
exception netrc.NetrcParseError|ソースファイルのテキスト中で文法エラーに遭遇した場合に netrc クラスによって送出される例外です。 この例外のインスタンスは 3 つのインスタンス変数を持っています: msg はテキストによるエラーの説明、 filename はソースファイルの名前、そして lineno はエラーが発見された行番号です。

## [14.3.1. netrc オブジェクト](https://docs.python.jp/3/library/netrc.html#netrc-objects)

> netrc インスタンスは以下のメソッドを持っています:

属性|概要
----|----
netrc.authenticators(host)|host の認証情報として、三要素のタプル (login, account, password) を返します。与えられた host に対するエントリが netrc ファイルにない場合、'default' エントリに関連付けられたタプルが返されます。host に対応するエントリがなく、default エントリもない場合、None を返します。
netrc.__repr__()|クラスの持っているデータを netrc ファイルの書式に従った文字列で出力します。(コメントは無視され、エントリが並べ替えられる可能性があります。)

> netrc のインスタンスは以下の public なインスタンス変数を持っています:

属性|概要
----|----
netrc.hosts|ホスト名を (login, account, password) からなるタプルに対応づけている辞書です。'default' エントリがある場合、その名前の擬似ホスト名として表現されます。
netrc.macros|マクロ名を文字列のリストに対応付けている辞書です。

### 注釈

> 利用可能なパスワードの文字セットは、ASCII のサブセットのみです。全ての ASCII の記号を使用することができます。しかし、空白文字と印刷不可文字を使用することはできません。この制限は .netrc ファイルの解析方法によるものであり、将来解除されます。

