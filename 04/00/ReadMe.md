# [14.1. csv — CSV ファイルの読み書き](https://docs.python.jp/3/library/csv.html)

< [14. ファイルフォーマット](https://docs.python.jp/3/library/fileformats.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/csv.py](https://github.com/python/cpython/tree/3.6/Lib/csv.py)

> CSV (Comma Separated Values、カンマ区切り値列) と呼ばれる形式は、 スプレッドシートやデータベース間でのデータのインポートやエクスポートにおける最も一般的な形式です。 CSVフォーマットは、 RFC 4180 によって標準的な方法でフォーマットを記述する試みが行われる以前から長年使用されました。明確に定義された標準がないということは、異なるアプリケーション によって生成されたり取り込まれたりするデータ間では、しばしば微妙な違いが発生するということを意味します。こうした違いのために、複数のデータ源から得られた CSV ファイルを処理する作業が鬱陶しいものになることがあります。とはいえ、デリミタ (delimiter) やクオート文字の 相違はあっても、全体的な形式は十分似通っているため、こうしたデータを効率的に操作し、データの読み書きにおける細々としたことをプログラマ から隠蔽するような単一のモジュールを書くことは可能です。

> csv モジュールでは、CSV 形式で書かれたテーブル状のデータを読み書きするためのクラスを実装しています。このモジュールを使うことで、プログラマは Excel で使われている CSV 形式に関して詳しい知識をもっていなくても、 "このデータを Excel で推奨されている形式で書いてください" とか、 "データを Excel で作成されたこのファイルから読み出してください" と言うことができます。プログラマはまた、他のアプリケーションが解釈できる CSV 形式を記述したり、独自の特殊な目的をもった CSV 形式を定義することができます。

> csv モジュールの reader および writer オブジェクトはシーケンス型を読み書きします。プログラマは DictReader や DictWriter クラスを使うことで、データを辞書形式で読み書きすることもできます。

> 参考

> PEP 305 - CSV File API

>    Python へのこのモジュールの追加を提案している Python 改良案 (PEP: Python Enhancement Proposal)。

* [PEP 305](https://www.python.org/dev/peps/pep-0305)

## [14.1.1. モジュールコンテンツ](https://docs.python.jp/3/library/csv.html#module-contents)

> csv モジュールでは以下の関数を定義しています:

属性|概要
----|----
csv.reader(csvfile, dialect='excel', **fmtparams)|与えられた csvfile 内の行を反復処理するような reader オブジェクトを返します。 csvfile はイテレータ(iterator)プロトコルをサポートし、 __next__() メソッドが呼ばれた際に常に文字列を返すような任意のオブジェクトにすることができます — ファイルオブジェクト でもリストでも構いません。 csvfile がファイルオブジェクトの場合、 newline='' として開くべきです。 [1] オプションとして dialect パラメータを与えることができ、特定の CSV 表現形式 (dialect) 特有のパラメータの集合を定義するために使われます。 dialect 引数は Dialect クラスのサブクラスのインスタンスか、 list_dialects() 関数が返す文字列の一つにすることができます。別のオプションである fmtparams キーワード引数は、現在の表現形式における個々の書式パラメータを上書きするために与えることができます。表現形式および書式化パラメータの詳細については、 Dialect クラスと書式化パラメータ 節を参照してください。
csv.writer(csvfile, dialect='excel', **fmtparams)|ユーザが与えたデータをデリミタで区切られた文字列に変換し、与えられたファイルオブジェクトに書き込むための writer オブジェクトを返します。 csvfile は write() メソッドを持つ任意のオブジェクトです。 csvfile がファイルオブジェクトの場合、 newline='' として開くべきです [1] 。オプションとして dialect 引数を与えることができ、利用するCSV表現形式(dialect)を指定することができます。 dialect パラメータは Dialect クラスのサブクラスのインスタンスか、 list_dialects() 関数が返す文字列の1つにすることができます。別のオプション引数である fmtparams キーワード引数は、現在の表現形式における個々の書式パラメータを上書きするために与えることができます。dialect と書式パラメータについての詳細は、 Dialect クラスと書式化パラメータ 節を参照してください。 DB API を実装するモジュールとのインタフェースを可能な限り容易にするために、 None は空文字列として書き込まれます。この処理は可逆な変換ではありませんが、SQL で NULL データ値を CSV にダンプする処理を、 cursor.fetch* 呼び出しによって返されたデータを前処理することなく簡単に行うことができます。他の非文字列データは、書き出される前に str() を使って文字列に変換されます。
csv.register_dialect(name[, dialect[, **fmtparams]])|dialect を name と関連付けます。 name は文字列でなければなりません。表現形式(dialect)は Dialect のサブクラスを渡すか、またはキーワード引数 fmtparams 、もしくは両方で指定できますが、キーワード引数の方が優先されます。表現形式と書式化パラメータについての詳細は、 Dialect クラスと書式化パラメータ 節を参照してください。
csv.unregister_dialect(name)|name に関連づけられた表現形式を表現形式レジストリから削除します。 name が表現形式名でない場合には Error を送出します。
csv.get_dialect(name)|name に関連づけられた表現形式を返します。 name が表現形式名でない場合には Error を送出します。この関数は不変の Dialect を返します。
csv.list_dialects()|登録されている全ての表現形式を返します。
csv.field_size_limit([new_limit])|パーサが許容する現在の最大フィールドサイズを返します。 new_limit が渡されたときは、その値が新しい上限になります。
class csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)|通常の writer のように動作しますが、辞書を出力行にマップするオブジェクトを生成します。 fieldnames パラメータは、writerow() メソッドに渡された辞書の値がどのような順番でファイル f に書かれるかを指定するキーの sequence です。 writerow() メソッドに渡された辞書に fieldnames には存在しないキーが含まれている場合、オプションの extrasaction パラメータによってどんな動作を行うかが指定されます。この値がデフォルト値である 'raise' に設定されている場合、 ValueError が送出されます。 'ignore' に設定されている場合、辞書の余分な値は無視されます。その他のパラメータはベースになっている writer インスタンスに渡されます。
class csv.Dialect|Dialect クラスはコンテナクラスで、基本的な用途としては、その属性を特定の reader や writer インスタンスのパラメータを定義するために用います。
class csv.excel|excel クラスは Excel で生成される CSV ファイルの通常のプロパティを定義します。これは 'excel' という名前の dialect として登録されています。
class csv.excel_tab|excel_tab クラスは Excel で生成されるタブ分割ファイルの通常のプロパティを定義します。これは 'excel-tab' という名前の dialect として登録されています。
class csv.unix_dialect|unix_dialect クラスは UNIX システムで生成される CSV ファイルの通常のプロパティ (行終端記号として '\n' を用い全てのフィールドをクォートするもの) を定義します。これは 'unix' という名前の dialect として登録されています。
class csv.Sniffer|Sniffer クラスは CSV ファイルの書式を推理するために用いられるクラスです。
    sniff(sample, delimiters=None)|    与えられた sample を解析し、発見されたパラメータを反映した Dialect サブクラスを返します。オプションの delimiters パラメータを与えた場合、有効なデリミタ文字を含んでいるはずの文字列として解釈されます。
    has_header(sample)|    (CSV 形式と仮定される) サンプルテキストを解析して、最初の行がカラムヘッダの羅列のように推察される場合 True を返します。

> csv モジュールでは以下の定数を定義しています:

属性|概要
----|----
csv.QUOTE_ALL|writer オブジェクトに対し、全てのフィールドをクオートするように指示します。
csv.QUOTE_MINIMAL|writer オブジェクトに対し、 delimiter 、 quotechar または lineterminator に含まれる任意の文字のような特別な文字を含むフィールドだけをクオートするように指示します。
csv.QUOTE_NONNUMERIC|writer オブジェクトに対し、全ての非数値フィールドをクオートするように指示します。
csv.QUOTE_NONE|writer オブジェクトに対し、フィールドを決してクオートしないように指示します。現在の delimiter が出力データ中に現れた場合、現在設定されている escapechar 文字が前に付けられます。 escapechar がセットされていない場合、エスケープが必要な文字に遭遇した writer は Error を送出します。

> csv モジュールでは以下の例外を定義しています:

属性|概要
----|----
exception csv.Error|全ての関数において、エラーが検出された際に送出される例外です。

## [14.1.2. Dialect クラスと書式化パラメータ](https://docs.python.jp/3/library/csv.html#dialects-and-formatting-parameters)

> レコードに対する入出力形式の指定をより簡単にするために、特定の書式化パラメータは表現形式 (dialect) にまとめてグループ化されます。表現形式は Dialect クラスのサブクラスで、様々なクラス特有のメソッドと、 validate() メソッドを一つ持っています。 reader または writer オブジェクトを生成するとき、プログラマは文字列または Dialect クラスのサブクラスを表現形式パラメータとして渡さなければなりません。さらに、 dialect パラメータの代りに、プログラマは上で定義されている属性と同じ名前を持つ個々の書式化パラメータを Dialect クラスに指定することができます。

> Dialect は以下の属性をサポートしています:

属性|概要
----|----
Dialect.delimiter|フィールド間を分割するのに用いられる 1 文字からなる文字列です。デフォルトでは ',' です。
Dialect.doublequote|フィールド内に現れた quotechar のインスタンスで、クオートではないその文字自身でなければならない文字をどのようにクオートするかを制御します。 True の場合、この文字は二重化されます。 False の場合、 escapechar は quotechar の前に置かれます。デフォルトでは True です。
Dialect.escapechar|writer が、 quoting が QUOTE_NONE に設定されている場合に delimiter をエスケープするため、および、 doublequote が False の場合に quotechar をエスケープするために用いられる、 1 文字からなる文字列です。読み込み時には escapechar はそれに引き続く文字の特別な意味を取り除きます。デフォルトでは None で、エスケープを行ないません。
Dialect.lineterminator|writer が作り出す各行を終端する際に用いられる文字列です。デフォルトでは '\r\n' です。
Dialect.quotechar|delimiter や quotechar といった特殊文字を含むか、改行文字を含むフィールドをクオートする際に用いられる 1 文字からなる文字列です。デフォルトでは '"' です。
Dialect.quoting|クオートがいつ writer によって生成されるか、また reader によって認識されるかを制御します。 QUOTE_* 定数のいずれか (モジュールコンテンツ 節参照) をとることができ、デフォルトでは QUOTE_MINIMAL です。
Dialect.skipinitialspace|True の場合、 delimiter の直後に続く空白は無視されます。デフォルトでは False です。
Dialect.strict|True の場合、 不正な CSV 入力に対して Error を送出します。デフォルトでは False です。

## [14.1.3. reader オブジェクト](https://docs.python.jp/3/library/csv.html#reader-objects)

> reader オブジェクト(DictReader インスタンス、および reader() 関数によって返されたオブジェクト) は、以下の public なメソッドを持っています:

属性|概要
----|----
csvreader.__next__()|Return the next row of the reader’s iterable object as a list (if the object was returned from reader()) or a dict (if it is a DictReader instance), parsed according to the current dialect. Usually you should call this as next(reader).

> reader オブジェクトには以下の公開属性があります:

属性|概要
----|----
csvreader.dialect|パーサで使われる表現形式の読み出し専用の記述です。
csvreader.line_num|ソースイテレータから読んだ行数です。この数は返されるレコードの数とは、レコードが複数行に亘ることがあるので、一致しません。

> DictReader オブジェクトは、以下の public な属性を持っています:

属性|概要
----|----
csvreader.fieldnames|オブジェクトを生成するときに渡されなかった場合、この属性は最初のアクセス時か、ファイルから最初のレコードを読み出したときに初期化されます。

## [14.1.4. writer オブジェクト](https://docs.python.jp/3/library/csv.html#writer-objects)

> Writer オブジェクト(DictWriter インスタンス、および writer() 関数によって返されたオブジェクト) は、以下の public なメソッドを持っています: row には、 Writer オブジェクトの場合には文字列か数値のイテラブルを指定し、 DictWriter オブジェクトの場合はフィールド名をキーとして対応する文字列か数値を格納した辞書オブジェクトを指定します(数値は str() で変換されます)。複素数を出力する場合、値をかっこで囲んで出力します。このため、CSV ファイルを読み込むアプリケーションで（そのアプリケーションが複素数をサポートしていたとしても）問題が発生する場合があります。

属性|概要
----|----
csvwriter.writerow(row)|row パラメータを現在の表現形式に基づいて書式化し、 writer のファイルオブジェクトに書き込みます。
csvwriter.writerows(rows)|rows 引数(上記 row のリスト)全てを現在の表現形式に基づいて書式化し、writer のファイルオブジェクトに書き込みます。

> writer オブジェクトには以下の公開属性があります:

属性|概要
----|----
csvwriter.dialect|writer で使われる表現形式の読み出し専用の記述です。

> DictWriter のオブジェクトは以下の public メソッドを持っています:

属性|概要
----|----
DictWriter.writeheader()|(コンストラクタで指定された)フィールド名の行を出力します。

## [14.1.5. 使用例](https://docs.python.jp/3/library/csv.html#examples)

> 最も簡単な CSV ファイル読み込みの例です:

```python
import csv
with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

> 別の書式での読み込み:

```python
import csv
with open('passwd', newline='') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)
```

> 上に対して、単純な書き込みのプログラム例は以下のようになります。

```python
import csv
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)
```

> open() が CSV ファイルの読み込みに使われるため、ファイルはデフォルトではシステムのデフォルトエンコーディングでユニコード文字列にデコードされます (locale.getpreferredencoding() を参照)。他のエンコーディングを用いてデコードするには、open の引数 encoding を設定して、以下のようにします:

```python
import csv
with open('some.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

> システムのデフォルトエンコーディング以外で書き込む場合も同様です。出力ファイルを開く際に引数 encoding を明示してください。

> 新しい表現形式の登録:

```python
import csv
csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)
with open('passwd', newline='') as f:
    reader = csv.reader(f, 'unixpwd')
```

> もう少し手の込んだ reader の使い方 — エラーを捉えてレポートします。

```python
import csv, sys
filename = 'some.csv'
with open(filename, newline='') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
```

> このモジュールは文字列の解析は直接サポートしませんが、簡単にできます。

```python
import csv
for row in csv.reader(['one,two,three']):
    print(row)
```

簡単な読み書き。
```python
import csv
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id','name'])
    writer.writerows([['0','Yamada'],['1','Sanada']])

with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```
```sh
$ python 0.py 
['id', 'name']
['0', 'Yamada']
['1', 'Sanada']
```
