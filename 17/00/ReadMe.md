# [16.2. io — ストリームを扱うコアツール](https://docs.python.jp/3/library/io.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/io.py](https://github.com/python/cpython/tree/3.6/Lib/io.py)

io.BytesIO, io.StringIO, の2つをストリームとして使うことだけ覚えれば大体OK。

## [16.2.1. 概要](https://docs.python.jp/3/library/io.html#overview)

> io モジュールは様々な種類の I/O を扱う Python の主要な機能を提供しています。 I/O には主に3つの種類があります; テキスト I/O, バイナリ I/O, raw I/O です。これらは汎用的なカテゴリで、各カテゴリには様々なストレージが利用されます。これらのいずれかのカテゴリに属する具象オブジェクトは全て file object と呼ばれます。他によく使われる用語として ストリーム と file-like オブジェクト があります。

> それぞれの具象ストリームオブジェクトは、カテゴリに応じた機能を持ちます。ストリームは読み出し専用、書き込み専用、読み書き可能のいずかになります。任意のランダムアクセス（前方、後方の任意の場所にシークする）が可能かもしれませんし、シーケンシャルアクセスしかできないかもしれません（例えばソケットやパイプなど）。

> 全てのストリームは、与えられたデータの型に対して厳密です。例えば、バイナリストリームの write() メソッドに対して str オブジェクトを渡すと TypeError 例外を発生させます。テキストストリームの write() メソッドに bytes オブジェクトを渡しても同じです。

> バージョン 3.3 で変更: 以前 IOError を送出していた操作が OSError を送出するようになりました。 IOError は今は OSError の別名です。

### [16.2.1.1. テキスト I/O](https://docs.python.jp/3/library/io.html#text-i-o)

> テキスト I/O は、 str オブジェクトを受け取り、生成します。すなわち、背後にあるストレージがバイト列 (例えばファイルなど) を格納するときは常に、透過的にデータのエンコード・デコードを行ない、オプションでプラットフォーム依存の改行文字変換を行います。

> テキストストリームを作る一番簡単な方法は、オプションでエンコーディングを指定して、 open() を利用することです:

```python
f = open("myfile.txt", "r", encoding="utf-8")
```

> StringIO オブジェクトはインメモリーのテキストストリームです:

```python
f = io.StringIO("some initial text data")
```

> テキストストリームの API は TextIOBase のドキュメントで詳しく解説します。

### [16.2.1.2. バイナリ I/O](https://docs.python.jp/3/library/io.html#binary-i-o)

> バイナリー I/O (buffered I/O とも呼ばれます) は bytes-like オブジェクト を受け取り bytes オブジェクトを生成します。エンコード、デコード、改行文字変換は一切行いません。このカテゴリのストリームは全ての非テキストデータや、テキストデータの扱いを手動で管理したい場合に利用することができます。

> バイナリーストリームを生成する一番簡単な方法は、 open() の mode 文字列に 'b' を指定することです:

```python
f = open("myfile.jpg", "rb")
```

> BytesIO はインメモリーのバイナリストリームです:

```python
f = io.BytesIO(b"some initial binary data: \x00\x01")
```

> バイナリーストリーム API は BufferedIOBase のドキュメントで詳しく解説します。

> 他のライブラリモジュールが、別のテキスト・バイナリーストリームを生成する方法を提供しています。例えば socket.socket.makefile() などです。

### [16.2.1.3. Raw I/O](https://docs.python.jp/3/library/io.html#raw-i-o)

> Raw I/O (unbuffered I/O とも呼ばれます) は、バイナリーストリームやテキストストリームの低水準の部品としてよく利用されます。ユーザーコードで直接 raw ストリームを扱うべき場面は滅多にありません。とはいえ、バッファリングを無効にしてファイルをバイナリーモードで開くことで raw ストリームを作ることができます:

```python
f = open("myfile.jpg", "rb", buffering=0)
```

> raw ストリーム API は RawIOBase のドキュメントで詳しく解説します。

## [16.2.2. 高水準のモジュールインターフェイス](https://docs.python.jp/3/library/io.html#high-level-module-interface)

属性|概要
----|----
io.DEFAULT_BUFFER_SIZE|このモジュールの buffered I/O クラスで利用されるデフォルトのバッファーサイズを表す整数です。可能であれば、open() は file の blksize (os.stat() で取得される) を利用します。
exception io.BlockingIOError|互換性のための、組み込みの BlockingIOError 例外のエイリアスです。
exception io.UnsupportedOperation|OSError と ValueError を継承した例外です。ストリームがサポートしていない操作を行おうとした時に送出されます。

### [16.2.2.1. インメモリー ストリーム](https://docs.python.jp/3/library/io.html#in-memory-streams)

> str や bytes-like オブジェクト を、読み書き可能なファイルのように扱うことができます。 StringIO は文字列に対して、テキストモードで開かれたファイルのように使うことができます。 BytesIO はバイナリーモードで開いたファイルのように扱うことができます。この2つのクラスは、読み書き可能で、ランダムアクセス可能です。

#### 参考

モジュール|概要
----------|----
[sys](https://docs.python.jp/3/library/sys.html#module-sys)|標準 IO ストリームを持っています: sys.stdin, sys.stdout, sys.stderr。

## [16.2.3. クラス階層](https://docs.python.jp/3/library/io.html#class-hierarchy)

> I/O ストリームの実装はクラス階層に分けて整理されています。まずストリームのカテゴリを分類するための抽象基底クラス群(abstract base class, ABC) があり、続いて標準のストリーム実装を行う具象クラス群があります。

> 注釈

> 抽象基底クラス群は、具象ストリームクラスの実装を助けるために、いくつかのデフォルトの実装を提供しています。例えば、 BufferedIOBase は readinto() と readline() の最適化されていない実装を提供しています。

> I/O 階層の最上位には抽象基底クラスの IOBase があります。 IOBase ではストリームに対して基本的なインタフェースを定義しています。 しかしながら、ストリームに対する読み込みと書き込みが分離されていないことに注意してください。 実装においては与えられた操作をサポートしない場合は UnsupportedOperation を送出することが許されています。

> RawIOBase ABC は IOBase を拡張します。このクラスはストリームからの bytes の読み書きを扱います。 FileIO は、 RawIOBase を継承してマシンのファイルシステム中のファイルへのインタフェースを提供します。

> BufferedIOBase ABC は生のバイトストリーム (RawIOBase) 上にバッファ処理を追加します。そのサブクラスの BufferedWriter, 

> BufferedReader, BufferedRWPair では、 それぞれ読み込み専用、書き込み専用、読み書き可能なストリームをバッファします。 

> BufferedRandom ではランダムアクセスストリームに対してバッファされたインタフェースを提供します。 BytesIO も BufferedIOBase のサブクラスで、インメモリのバイト列へのシンプルなストリームです。

> もう一つの IOBase のサブクラスである TextIOBase ABC は、 テキストを表すバイトストリームを扱い、文字列とのエンコードやデコードといった処理を行います。 TextIOWrapper はその拡張で、バッファ付き raw ストリーム (BufferedIOBase) へのバッファされたテキストインタフェースです。 最後に StringIO はテキストに対するインメモリストリームです。

> 引数名は規約に含まれていません。 そして open() の引数だけがキーワード引数として用いられることが意図されています。

> 次のテーブルは io モジュールが提供する ABC の概要です:

ABC|継承元|スタブメソッド|Mixin するメソッドとプロパティ
---|------|--------------|------------------------------
IOBase| |fileno, seek, truncate|close, closed, __enter__, __exit__, flush, isatty, __iter__, __next__, readable, readline, readlines, seekable, tell, writable, writelines
RawIOBase|IOBase|readinto, write|IOBase から継承したメソッド、 read, readall
BufferedIOBase|IOBase|detach, read, read1, write|IOBase から継承したメソッド、 readinto
TextIOBase|IOBase|detach, read, readline, write|IOBase から継承したメソッド、 encoding, errors, newlines

* io モジュール
    * [IOBase](https://docs.python.jp/3/library/io.html#io.IOBase)
        * [RawIOBase](https://docs.python.jp/3/library/io.html#io.RawIOBase)
            * [FileIO](https://docs.python.jp/3/library/io.html#io.FileIO)
            * [BufferedIOBase](https://docs.python.jp/3/library/io.html#io.BufferedIOBase)
                * [BufferedWriter](https://docs.python.jp/3/library/io.html#io.BufferedWriter)
                * [BufferedReader](https://docs.python.jp/3/library/io.html#io.BufferedReader)
                * [BufferedRWPair](https://docs.python.jp/3/library/io.html#io.BufferedRWPair)
                * [BufferedRandom](https://docs.python.jp/3/library/io.html#io.BufferedRandom)
                * [BytesIO](https://docs.python.jp/3/library/io.html#io.BytesIO)
        * [TextIOBase](https://docs.python.jp/3/library/io.html#io.TextIOBase)
            * [TextIOWrapper](https://docs.python.jp/3/library/io.html#io.TextIOWrapper)
            * [StringIO](https://docs.python.jp/3/library/io.html#io.StringIO)

### [16.2.3.1. I/O 基底クラス](https://docs.python.jp/3/library/io.html#i-o-base-classes)

属性|概要
----|----
class io.IOBase|すべての I/O クラスの抽象基底クラスです。バイトストリームへの操作を行います。パブリックなコンストラクタはありません。
close()|このストリームをフラッシュして閉じます。このメソッドはファイルが既に閉じられていた場合は特に何の効果もありません。いったんファイルが閉じられると、すべてのファイルに対する操作 (例えば読み込みや書き込み) で ValueError が発生します。
closed|ストリームが閉じられていた場合 True になります。
fileno()|ストリームが保持しているファイル記述子 (整数値) が存在する場合はそれを返します。もし IO オブジェクトがファイル記述子を使っていない場合は OSError が発生します。
flush()|適用可能であればストリームの書き込みバッファをフラッシュします。読み出し専用や非ブロッキングストリームでは何もしません。
isatty()|ストリームが対話的であれば (つまりターミナルや tty デバイスにつながっている場合) True を返します。
readable()|ストリームが読み込める場合 True を返します。 False の場合は read() は OSError を発生させます。
readline(size=-1)|ストリームから 1 行読み込んで返します。もし size が指定された場合、最大で size バイトが読み込まれます。
readlines(hint=-1)|ストリームから行のリストを読み込んで返します。 hint を指定することで、読み込む行数を制御できます。もし読み込んだすべての行のサイズ (バイト数、もしくは文字数) が hint の値を超えた場合、読み込みをそこで終了します。
seek(offset[, whence])|ストリーム位置を指定された offset バイトに変更します。offset は whence で指定された位置からの相対位置として解釈されます。 whence のデフォルト値は SEEK_SET です。 whence に指定できる値は: SEEK_SET, SEEK_CUR, SEEK_END
seekable()|ストリームがランダムアクセスをサポートしている場合、 True を返します。 False の場合、 seek()、 tell()、 truncate() を使用すると OSError を発生させます。
tell()|現在のストリーム位置を返します。
truncate(size=None)|ストリームのサイズを、指定された size バイト (または size が指定されていない場合、現在位置) に変更します。現在のストリーム位置は変更されません。このサイズ変更により、現在のファイルサイズを拡大または縮小させることができます。拡大の場合には、新しいファイル領域の内容はプラットホームによって異なります (ほとんどのシステムでは、追加のバイトが 0 で埋められます)。新しいファイルサイズが返されます。
writable()|ストリームが書き込みをサポートしている場合 True を返します。 False の場合は write()、 truncate() は OSError を返します。
writelines(lines)|ストリームに行のリストを書き込みます。行区切り文字は追加されないので、書き込む各行の行末に行区切り文字を含ませるのが一般的です。
__del__()|オブジェクトの破壊の用意をします。このメソッドはインスタンスの close() メソッドを呼びます。 IOBase はこのメソッドのデフォルトの実装を提供します
class io.RawIOBase|生のバイナリ I/O への基底クラスです。 IOBase を継承しています。パブリックコンストラクタはありません。
read(size=-1)|オブジェクトを size バイトまで読み込み、それを返します。簡単のため、 size が指定されていないか -1 の場合、 readall() が呼び出されます。その他の場合、システムコール呼び出しが一度だけ行われます。既に EOF に達していたら空のバイトオブジェクトが返されます。オペレーティングシステムコールが返すバイトのサイズが size より小さい場合、 size バイトより少ないバイトが返されることがあります。
readall()|EOF までストリームからすべてのバイトを読み込みます。必要な場合はストリームに対して複数の呼び出しをします。
readinto(b)|あらかじめ確保された書き込み可能な bytes-like object b にバイト列を読み込み、読み込んだバイト数を返します。オブジェクトがノンブロッキングモードで、 1 バイトも読み込めなければ、 None が返されます。
write(b)|与えられた bytes-like オブジェクト b を生ストリームに書き込み、書き込んだバイト数を返します。これは、根底の生ストリームの性質や、特にノンブロッキングである場合に、 b のバイト数より小さくなることがあります。生ストリームがブロックされないように設定されていて、かつ1バイトも即座に書き込むことができなければ、 None が返されます。このメソッドから返った後で呼び出し元は b を解放したり変更したりするかもしれないので、実装はメソッド呼び出しの間だけ b にアクセスすべきです。
class io.BufferedIOBase|何らかのバッファリングをサポートするバイナリストリームの基底クラスです。 IOBase を継承します。パブリックなコンストラクタはありません。
raw|BufferedIOBase が扱う根底の生ストリーム (RawIOBase インスタンス) を返します。これは BufferedIOBase API には含まれず、よって実装に含まれないことがあります。
detach()|根底の生ストリームをバッファから分離して返します。
read(size=-1)|最大で size バイト読み込んで返します。 引数が省略されるか、 None か、または負の値であった場合、 データは EOF に到達するまで読み込まれます。 ストリームが既に EOF に到達していた場合は空の bytes オブジェクトが返されます。
read1(size=-1)|根底の raw ストリームの read() (または readinto() ) メソッドを高々 1 回呼び出し、最大で size バイト読み込み、返します。これは、 BufferedIOBase オブジェクトの上に独自のバッファリングを実装するときに便利です。
readinto(b)|あらかじめ確保された書き込み可能な bytes-like オブジェクト b にバイト列を読み込み、読み込んだバイト数を返します。
readinto1(b)|根底の raw ストリームの read() (または readinto()) メソッドを高々 1 回呼び出し、あらかじめ確保された書き込み可能な bytes-like オブジェクト b にバイト列を読み込みます。読み込んだバイト数を返します。
write(b)|与えられた bytes-like オブジェクト b を書き込み、書き込んだバイト数を返します (これは常に b のバイト数と等しくなります。なぜなら、もし書き込みに失敗した場合は OSError が発生するからです)。実際の実装に依存して、これらのバイト列は根底のストリームに即座に書き込まれることもあれば、パフォーマンスやレイテンシの関係でバッファに保持されることもあります。

### [16.2.3.2. 生ファイルI/O](https://docs.python.jp/3/library/io.html#raw-file-i-o)

属性|概要
----|----
class io.FileIO(name, mode='r', closefd=True, opener=None)|FileIO はバイトデータを含む OS レベルのファイルを表します。 RawIOBase インタフェースを (したがって IOBase インタフェースも) 実装しています。
mode|コンストラクタに渡されたモードです。
name|ファイル名。コンストラクタに名前が渡されなかったときはファイル記述子になります。

### [16.2.3.3. バッファ付きストリーム](https://docs.python.jp/3/library/io.html#buffered-streams)

> バッファ付き I/O ストリームは、I/O デバイスに生 I/O より高レベルなインタフェースを提供します。

属性|概要
----|----
class io.BytesIO([initial_bytes])|インメモリの bytes バッファを利用したストリームの実装です。 BufferedIOBase を継承します。バッファは close() メソッドが呼び出された際に破棄されます。
getbuffer()|バッファの内容をコピーすることなく、その内容の上に、読み込み及び書き込みが可能なビューを返します。また、このビューを変更すると、バッファの内容は透過的に更新されます:
getvalue()|バッファの全内容を含む bytes を返します。
read1()|BytesIO においては、このメソッドは read() と同じです。
readinto1()|BytesIO においては、このメソッドは readinto() と同じです。
class io.BufferedReader(raw, buffer_size=DEFAULT_BUFFER_SIZE)|読み込み可能でシーケンシャルな RawIOBase オブジェクトへの高水準のアクセスを提供するバッファです。 BufferedIOBase を継承します。このオブジェクトからデータを読み込むとき、より大きい量のデータが根底の raw ストリームから要求され、内部バッファに保存される場合があります。バッファされたデータは、その次の読み込み時に直接返されます。
peek([size])|位置を進めずにストリームからバイト列を返します。これを果たすために生ストリームに対して行われる read は高々一度だけです。返されるバイト数は、要求より少ないかもしれませんし、多いかもしれません。
read([size])|size バイトを読み込んで返します。size が与えられないか負の値ならば、EOF まで、または非ブロッキングモード中で read 呼び出しがブロックされるまでを返します。
read1(size)|raw ストリームに対しただ一度の呼び出しで最大 size バイトを読み込んで返します。少なくとも 1 バイトがバッファされていれば、バッファされているバイト列だけが返されます。それ以外の場合は raw ストリームの読み込みが一回呼び出されます。
class io.BufferedWriter(raw, buffer_size=DEFAULT_BUFFER_SIZE)|書き込み可能でシーケンシャルな RawIOBase オブジェクトへの、高レベルなアクセスを提供するバッファです。 BufferedIOBase を継承します。このオブジェクトに書き込むとき、データは通常内部バッファに保持されます。このバッファは、以下のような種々の状況で根底の RawIOBase オブジェクトに書き込まれます。
flush()|バッファに保持されたバイト列を生ストリームに強制的に流し込みます。生ストリームがブロックした場合 BlockingIOError が送出されます。
write(b)|bytes-like オブジェクト b を書き込み、書き込んだバイト数を返します。ノンブロッキング時、バッファが書き込まれるべきなのに生ストリームがブロックした場合 BlockingIOError が送出されます。
class io.BufferedRandom(raw, buffer_size=DEFAULT_BUFFER_SIZE)|ランダムアクセスストリームへのバッファ付きインタフェース。 BufferedReader および BufferedWriter を継承し、さらに seek() および tell() をサポートしています。
class io.BufferedRWPair(reader, writer, buffer_size=DEFAULT_BUFFER_SIZE)|2つの単方向 RawIOBase オブジェクト – 一つは読み込み可能、他方が書き込み可能 – を組み合わせてバッファ付きの双方向 I/O オブジェクトにしたものです。 BufferedIOBase を継承しています。

### [16.2.3.4. テキスト I/O](https://docs.python.jp/3/library/io.html#id1)

属性|概要
----|----
class io.TextIOBase|テキストストリームの基底クラスです。このクラスはストリーム I/O への文字と行に基づいたインタフェースを提供します。 Python の unicode 文字列は変更不可能なので、 readinto() メソッドは存在しません。 IOBase を継承します。パブリックなコンストラクタはありません。
encoding|エンコーディング名で、ストリームのバイト列を文字列にデコードするとき、また文字列をバイト列にエンコードするときに使われます。
errors|このエンコーダやデコーダのエラー設定です。
newlines|文字列、文字列のタプル、または None で、改行がどのように読み換えられるかを指定します。実装や内部コンストラクタのフラグに依って、これは利用できないことがあります。
buffer|TextIOBase が扱う根底のバイナリバッファ (BufferedIOBase インスタンス) です。これは TextIOBase API には含まれず、よって実装に含まれない場合があります。
detach()|根底のバイナリバッファを TextIOBase から分離して返します。
read(size)|最大 size 文字をストリームから読み込み、一つの str にして返します。 size が負の値または None ならば、 EOF まで読みます。
readline(size=-1)|改行または EOF まで読み込み、一つの str を返します。ストリームが既に EOF に到達している場合、空文字列が返されます。
seek(offset[, whence])|指定された offset にストリーム位置を変更します。 挙動は whence 引数によります。 whence のデフォルト値は SEEK_SET です。:SEEK_SET, SEEK_CUR, SEEK_END
tell()|ストリームの現在位置を不透明な数値で返します。この値は根底のバイナリストレージ内でのバイト数を表すとは限りません。
write(s)|文字列 s をストリームに書き出し、書き出された文字数を返します。
class io.TextIOWrapper(buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False)|BufferedIOBase バイナリストリーム上のバッファ付きテキストストリーム。 TextIOBase を継承します。line_buffering|行バッファリングが有効かどうか。
class io.StringIO(initial_value='', newline='\n')|テキストIO のためのインメモリストリーム。テキストバッファは close() メソッドが呼び出された際に破棄されます。
getvalue()|バッファの全内容を含む str を返します。改行コードのデコードは read() によって行われますが、これによるストリーム位置の変更は起こりません。
class io.IncrementalNewlineDecoder|改行を universal newlines モードにデコードするヘルパーコーデックです。 codecs.IncrementalDecoder を継承しています。

## [16.2.4. 性能](https://docs.python.jp/3/library/io.html#performance)

> このセクションでは与えられた具体的な I/O 実装の性能について議論します。

### [16.2.4.1. バイナリ I/O](https://docs.python.jp/3/library/io.html#id2)

> バッファ付き I/O は、ユーザが 1 バイトだけ要求した場合でさえ、データを大きな塊でのみ読み書きします。これにより、オペレーティングシステムのバッファ無し I/O ルーチンを呼び出して実行する非効率性はすべて隠されます。その成果は、OS と、実行される I/O の種類によって異なります。例えば、Linux のような現行の OS では、バッファ無しディスク I/O がバッファ付き I/O と同じくらい早いことがあります。しかし、どのプラットフォームとデバイスにおいても、バッファ付き I/O は最低でも予測可能なパフォーマンスを提供します。ですから、バイナリデータに対しては、バッファ無し I/O を使用するより、バッファ付きの I/O を使用するほうが望ましい場合がほとんどです。

### [16.2.4.2. テキスト I/O](https://docs.python.jp/3/library/io.html#id3)

> (ファイルなどの) バイナリストレージ上のテキスト I/O は、同じストレージ上のバイナリ I/O より非常に遅いです。なぜならこれには、文字コーデックを使った Unicode とバイナリデータ間の変換を必要とするからです。これは大量のテキストデータ、例えば大きなログファイルを扱うときに顕著に成り得ます。同様に、 TextIOWrapper.tell() や TextIOWrapper.seek() はどちらも、使われている復元アルゴリズムのために遅くなります。

> しかし StringIO は、ネイティブなインメモリ Unicode コンテナで、 BytesIO と同程度の速度を示します。

### [16.2.4.3. マルチスレッディング](https://docs.python.jp/3/library/io.html#multi-threading)

> (Unix における read(2) のような) オペレーティングシステムコールの、それがラッピングするものがスレッドセーフであるような範囲内では、 FileIO オブジェクトもまた、スレッドセーフです。

> バイナリバッファ付きオブジェクト (BufferedReader, BufferedWriter, BufferedRandom および BufferedRWPair のインスタンス) は、その内部構造をロックを使って保護します。このため、これらを複数のスレッドから同時に呼び出しても安全です。

> TextIOWrapper オブジェクトはスレッドセーフではありません。

### [16.2.4.4. リエントラント性](https://docs.python.jp/3/library/io.html#reentrancy)

> バイナリバッファ付きオブジェクト (BufferedReader, BufferedWriter, BufferedRandom および BufferedRWPair のインスタンス) は、リエントラント (再入可能) ではありません。リエントラントな呼び出しは普通の状況では起こりませんが、 I/O を signal ハンドラで行なっているときに起こりえます。スレッドが、すでにアクセスしているバッファ付きオブジェクトに再び入ろうとすると RuntimeError が送出されます。これは、バッファ付きオブジェクトに複数のスレッドから入ることを禁止するわけではありません。

> open() 関数は TextIOWrapper 内部のバッファ付きオブジェクトをラップするため、テキストファイルにも暗黙に拡張されます。これは、標準ストリームを含むので、組み込み関数 print() にも同様に影響します。

