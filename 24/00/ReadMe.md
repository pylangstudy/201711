# [16.6. logging — Python 用ロギング機能](https://docs.python.jp/3/library/logging.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/logging/__init__.py](https://github.com/python/cpython/tree/3.6/Lib/logging/__init__.py)

> このモジュールは、アプリケーションやライブラリのための柔軟なエラーログ記録 (logging) システムを実装するための関数やクラスを定義しています。

> 標準ライブラリモジュールとしてログ記録 API が提供される利点は、すべての Python モジュールがログ記録に参加できることであり、これによってあなたが書くアプリケーションのログにサードパーティーのモジュールが出力するメッセージを含ませることができます。

> このモジュールは、多くの機能性と柔軟性を提供します。ロギングに慣れていないなら、つかむのに一番いいのはチュートリアルを読むことです (右のリンクを参照してください)。

> モジュールで定義されている基本的なクラスと関数を、以下に列挙します。

* ロガーは、アプリケーションコードが直接使うインタフェースを公開します。
* ハンドラは、(ロガーによって生成された) ログ記録を適切な送信先に送ります。
* フィルタは、どのログ記録を出力するかを決定する、きめ細かい機能を提供します。
* フォーマッタは、ログ記録が最終的に出力されるレイアウトを指定します。

## Important

* [基本チュートリアル](https://docs.python.jp/3/howto/logging.html#logging-basic-tutorial)
* [上級チュートリアル](https://docs.python.jp/3/howto/logging.html#logging-advanced-tutorial)
* [ロギングクックブック](https://docs.python.jp/3/howto/logging-cookbook.html#logging-cookbook)

## [16.6.1. ロガーオブジェクト](https://docs.python.jp/3/library/logging.html#logger-objects)

> ロガーには以下のような属性とメソッドがあります。ロガーを直接インスタンス化することはできず、常にモジュール関数 logging.getLogger(name) を介してインスタンス化することに注意してください。同じ name で getLogger() を複数回呼び出すと、常に同じロガー・オブジェクトへの参照が返されます。

> name は foo.bar.baz のようにピリオドで分割された (ただし単なるプレーンな foo もありえます) 潜在的に階層的な値です。階層リスト中でより下位のロガーは、上位のロガーの子です。例えば、foo という名前を持つロガーがあるとき、foo.bar, foo.bar.baz, foo.bam という名前を持つロガーはすべて foo の子孫です。ロガー名の階層は Python パッケージ階層と類似していて、推奨される構築方法 logging.getLogger(__name__) を使用してロガーをモジュール単位で構成すれば、Python パッケージ階層と同一になります。これは、モジュールの中では __name__ が Python パッケージ名前空間におけるモジュール名だからです。

* class logging.Logger

属性|概要
----|----
Logger.propagate|これが真と評価されると、記録されたイベントがこのロガーに向けられるとそれはこのロガーに所属する全てのハンドラに渡されるとともに、上位 (祖先) ロガーのハンドラにも渡されます。メッセージは、祖先ロガーのハンドラに直接渡されます - 今問題にしている祖先ロガーのレベルもフィルタも、どちらも考慮されません。
Logger.setLevel(lvl)|このロガーの閾値を lvl に設定します。ログ記録しようとするメッセージで、 lvl よりも深刻でないものは無視されます。ロガーが生成された際、レベルは NOTSET (これによりすべてのメッセージについて、ロガーがルートロガーであれば処理される、そうでなくてロガーが非ルートロガーの場合には親ロガーに委譲させる) に設定されます。ルートロガーは WARNING レベルで生成されることに注意してください。
Logger.isEnabledFor(lvl)|深刻度が lvl のメッセージが、このロガーで処理されることになっているかどうかを示します。このメソッドはまず、 logging.disable(lvl) で設定されるモジュールレベルの深刻度レベルを調べ、次にロガーの実効レベルを getEffectiveLevel() で調べます。
Logger.getEffectiveLevel()|このロガーの実効レベルを示します。 NOTSET 以外の値が setLevel() で設定されていた場合、その値が返されます。そうでない場合、 NOTSET 以外の値が見つかるまでロガーの階層をルートロガーの方向に追跡します。見つかった場合、その値が返されます。返される値は整数で、典型的には logging.DEBUG, logging.INFO 等のうち一つです。
Logger.getChild(suffix)|このロガーの子であるロガーを、接頭辞によって決定し、返します。従って、logging.getLogger('abc').getChild('def.ghi') は、logging.getLogger('abc.def.ghi') によって返されるのと同じロガーを返すことになります。これは簡便なメソッドで、親ロガーがリテラルでなく __name__ などを使って名付けられているときに便利です。
Logger.debug(msg, *args, **kwargs)|レベル DEBUG のメッセージをこのロガーで記録します。 msg はメッセージの書式文字列で、 args は msg に文字列書式化演算子を使って取り込むための引数です。 (これは、書式化文字列の中でキーワードを使い、引数として単一の辞書を渡すことができる、ということを意味します。)
Logger.info(msg, *args, **kwargs)|レベル INFO のメッセージをこのロガーで記録します。引数は debug() と同じように解釈されます。
Logger.warning(msg, *args, **kwargs)|レベル WARNING のメッセージをこのロガーで記録します。引数は debug() と同じように解釈されます。注釈: warning と機能的に等価な古いメソッド warn があります。warn は廃止予定なので使わないでください - 代わりに warning を使ってください。
Logger.error(msg, *args, **kwargs)|レベル ERROR のメッセージをこのロガーで記録します。引数は debug() と同じように解釈されます。
Logger.critical(msg, *args, **kwargs)|レベル CRITICAL のメッセージをこのロガーで記録します。引数は debug() と同じように解釈されます。
Logger.log(lvl, msg, *args, **kwargs)|整数で表したレベル lvl のメッセージをこのロガーで記録します。その他の引数は debug() と同じように解釈されます。
Logger.exception(msg, *args, **kwargs)|レベル ERROR のメッセージをこのロガーで記録します。引数は debug() と同じように解釈されます。例外情報がログメッセージに追加されます。このメソッドは例外ハンドラからのみ呼び出されるべきです。
Logger.addFilter(filt)|指定されたフィルタ filt をこのロガーに追加します。
Logger.removeFilter(filt)|指定されたフィルタ filt をこのロガーから取り除きます。
Logger.filter(record)|レコードに対してこのロガーのフィルタを適用し、レコードが処理されるべき場合に真を返します。フィルタのいずれかの値が偽を返すまで、それらは順番に試されていきます。いずれも偽を返さなければ、レコードは処理される(ハンドラに渡される)ことになります。ひとつでも偽を返せば、発生したレコードはもはや処理されることはありません。
Logger.addHandler(hdlr)|指定されたハンドラ hdlr をこのロガーに追加します。
Logger.removeHandler(hdlr)|指定されたハンドラ hdlr をこのロガーから取り除きます。
Logger.findCaller(stack_info=False)|呼び出し元のソースファイル名と行番号を調べます。ファイル名と行番号、関数名、スタック情報を 4 要素のタプルで返します。stack_info が True でなければ、スタック情報は None が返されます。
Logger.handle(record)|レコードを、このロガーおよびその上位ロガー (ただし propagate の値が false になったところまで) に関連付けられているすべてのハンドラに渡して処理します。このメソッドは、ローカルで生成されたレコードだけでなく、ソケットから受信した unpickle されたレコードに対しても同様に用いられます。 filter() によって、ロガーレベルでのフィルタが適用されます。
Logger.makeRecord(name, lvl, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None)|このメソッドは、特殊な LogRecord インスタンスを生成するためにサブクラスでオーバライドできるファクトリメソッドです。
Logger.hasHandlers()|このロガーにハンドラが設定されているかどうかを調べます。 そのために、このロガーとロガー階層におけるその祖先についてハンドラ探していきます。 ハンドラが見つかれば True 、そうでなければ False を返します。 このメソッドは、'propagate' 属性が偽に設定されたロガーを見つけると、さらに上位の探索をやめます - そのロガーが、ハンドラが存在するかどうかチェックされる最後のロガー、という意味です。

## [16.6.2. ロギングレベル](https://docs.python.jp/3/library/logging.html#logging-levels)

> ログレベルの数値は以下の表のように与えられています。これらは基本的に自分でレベルを定義したい人のためのもので、定義するレベルを既存のレベルの間に位置づけるためには具体的な値が必要になります。もし数値が他のレベルと同じだったら、既存の値は上書きされその名前は失われます。

レベル|数値
------|----
CRITICAL|50
ERROR|40
WARNING|30
INFO|20
DEBUG|10
NOTSET|0

## [16.6.3. ハンドラオブジェクト](https://docs.python.jp/3/library/logging.html#handler-objects)

> ハンドラ (Handler) は以下の属性とメソッドを持ちます。 Handler は直接インスタンス化されることはありません; このクラスはより便利なサブクラスの基底クラスとして働きます。しかしながら、サブクラスにおける __init__() メソッドでは、 Handler.__init__() を呼び出す必要があります。

属性|概要
----|----
Handler.__init__(level=NOTSET)|レベルを設定して、 Handler インスタンスを初期化します。空のリストを使ってフィルタを設定し、 I/O 機構へのアクセスを直列化するために (createLock() を使って) ロックを生成します。
Handler.createLock()|スレッドセーフでない背後の I/O 機能に対するアクセスを直列化するために用いられるスレッドロック (thread lock) を初期化します。
Handler.acquire()|createLock() で生成されたスレッドロックを獲得します。
Handler.release()|acquire() で獲得したスレッドロックを解放します。\
Handler.setLevel(lvl)|このハンドラに対する閾値を lvl に設定します。ログ記録しようとするメッセージで、 lvl よりも深刻でないものは無視されます。ハンドラが生成された際、レベルは NOTSET (すべてのメッセージが処理される) に設定されます。
Handler.setFormatter(form)|このハンドラの Formatter を form に設定します。
Handler.addFilter(filt)|指定されたフィルタ filt をこのハンドラに追加します。
Handler.removeFilter(filt)|指定されたフィルタ filt をこのハンドラから除去します。
Handler.filter(record)|レコードに対してこのハンドラのフィルタを適用し、レコードが処理されるべき場合に真を返します。フィルタのいずれかの値が偽を返すまで、それらは順番に試されていきます。いずれも偽を返さなければ、レコードは発行されることになります。ひとつでも偽を返せば、ハンドラはレコードを発行しません。
Handler.flush()|すべてのログ出力がフラッシュされるようにします。このクラスのバージョンではなにも行わず、サブクラスで実装するためのものです。
Handler.close()|ハンドラで使われているすべてのリソースの後始末を行います。このバージョンでは何も出力せず、 shutdown() が呼ばれたときに閉じられたハンドラを内部リストから削除します。サブクラスではオーバライドされた close() メソッドからこのメソッドが必ず呼ばれるようにしてください。
Handler.handle(record)|ハンドラに追加されたフィルタの条件に応じて、指定されたログレコードを出力します。このメソッドは I/O スレッドロックの獲得/解放を伴う実際のログ出力をラップします。
Handler.handleError(record)|このメソッドは emit() の呼び出し中に例外に遭遇した際にハンドラから呼び出されます。モジュールレベル属性 raiseExceptions が False の場合、例外は暗黙のまま無視されます。ほとんどの場合、これがロギングシステムの望ましい動作です - というのは、ほとんどのユーザはロギングシステム自体のエラーは気にせず、むしろアプリケーションのエラーに興味があるからです。しかしながら、望むならこのメソッドを自作のハンドラと置き換えることもできます。 record には、例外発生時に処理されていたレコードが入ります。 (raiseExceptions のデフォルト値は True です。これは開発中はその方が便利だからです)。
Handler.format(record)|レコードに対する書式化を行います - フォーマッタが設定されていれば、それを使います。そうでない場合、モジュールにデフォルト指定されたフォーマッタを使います。
Handler.emit(record)|指定されたログ記録レコードを実際にログ記録する際のすべての処理を行います。このメソッドはサブクラスで実装されることを意図しており、そのためこのクラスのバージョンは NotImplementedError を送出します。

## [16.6.4. フォーマッタオブジェクト](https://docs.python.jp/3/library/logging.html#formatter-objects)

> Formatter オブジェクトは以下の属性とメソッドを持っています。 Formatter は LogRecord を (通常は) 人間か外部のシステムで解釈できる文字列に変換する役割を担っています。基底クラスの Formatter では書式文字列を指定することができます。何も指定されなかった場合、ロギングコール中のメッセージ以外の情報だけを持つ '%(message)s' の値が使われます。フォーマットされた出力に情報の要素 (タイムスタンプなど) を追加したいなら、このまま読み進めてください。

> Formatter は LogRecord 属性の知識を利用できるような書式文字列を用いて初期化することができます。例えば、上で言及したデフォルト値では、ユーザによるメッセージと引数はあらかじめフォーマットされて、 LogRecord の message 属性に入っていることを利用しています。この書式文字列は、 Python 標準の % を使った変換文字列で構成されます。文字列整形に関する詳細は printf 形式の文字列書式化 を参照してください。

> LogRecord の便利なマッピングキーは、 LogRecord 属性 の節で与えられます。

class logging.Formatter(fmt=None, datefmt=None, style='%')|Formatter クラスの新たなインスタンスを返します。インスタンスは全体としてのメッセージに対する書式文字列と、メッセージの日付/時刻部分のための書式文字列を伴って初期化されます。 fmt が指定されない場合、 '%(message)s' が使われます。 datefmt が指定されない場合、 ISO8601 日付書式が使われます。

    style パラメーターは '%', '{', '$' のうちのいずれかで、書式文字列がどのようにデータとマージされるかを決めます: %-format 、 str.format() 、 string.Template のうちのどれかが使用されます。ログメッセージに使用する { および $ 形式のフォーマットの情報は 固有の書式化スタイルをアプリケーション全体で使う を参照してください。

    バージョン 3.2 で変更: style パラメータが追加されました。

    format(record)|    レコードの属性辞書が、文字列を書式化する演算で被演算子として使われます。書式化された結果の文字列を返します。辞書を書式化する前に、二つの準備段階を経ます。レコードの message 属性が msg % args を使って処理されます。書式化された文字列が '(asctime)' を含むなら、 formatTime() が呼び出され、イベントの発生時刻を書式化します。例外情報が存在する場合、 formatException() を使って書式化され、メッセージに追加されます。ここで注意していただきたいのは、書式化された例外情報は exc_text にキャッシュされるという点です。これが有用なのは例外情報がピックル化されて回線上を送ることができるからですが、しかし二つ以上の Formatter サブクラスで例外情報の書式化をカスタマイズしている場合には注意が必要になります。この場合、フォーマッタが書式化を終えるごとにキャッシュをクリアして、次のフォーマッタがキャッシュされた値を使わずに新鮮な状態で再計算するようにしなければならないことになります。

        スタック情報が利用可能な場合、(必要ならば formatStack() を使って整形した上で) スタック情報が例外情報の後に追加されます。

    formatTime(record, datefmt=None)|    このメソッドは、フォーマッタが書式化された時間を利用したい際に、 format() から呼び出されます。このメソッドは特定の要求を提供するためにフォーマッタで上書きすることができますが、基本的な振る舞いは以下のようになります: datefmt (文字列) が指定された場合、レコードが生成された時刻を書式化するために time.strftime() で使われます。そうでない場合、 ISO8601 書式が使われます。結果の文字列が返されます。

        この関数は、ユーザが設定できる関数を使って、生成時刻をタプルに変換します。デフォルトでは、 time.localtime() が使われます。特定のフォーマッタインスタンスに対してこれを変更するには、 converter 属性を time.localtime() や time.gmtime() と同じ署名をもつ関数に設定してください。すべてのフォーマッタインスタンスに対してこれを変更するには、例えば全てのロギング時刻を GMT で表示するには、 Formatter クラスの converter 属性を設定してください。

        バージョン 3.3 で変更: 以前は、デフォルトの ISO 8601 フォーマットがこの例のようにハードコーディングされていました: 2010-09-06 22:38:15,292 ここで、コンマの前の部分は strptime フォーマット文字列 ('%Y-%m-%d %H:%M:%S') によって扱われる部分で、コンマの後の部分はミリ秒値です。strptime にミリ秒のフォーマットプレースホルダーがないので、ミリ秒値は別のフォーマット文字列 '%s,%03d' を使用して追加されます。そして、これらのフォーマット文字列は両方ともこのメソッドでハードコーディングされていました。変更後は、これらの文字列はクラスレベル属性として定義され、必要ならインスタンスレベルでオーバーライドすることができます。属性の名前は default_time_format (strptime 書式文字列用) と default_msec_format (ミリ秒値の追加用) です。

    formatException(exc_info)|    指定された例外情報 (sys.exc_info() が返すような標準例外のタプル) を文字列として書式化します。デフォルトの実装は単に traceback.print_exception() を使います。結果の文字列が返されます。

    formatStack(stack_info)|    指定されたスタック情報を文字列としてフォーマットします (traceback.print_stack() によって返される文字列ですが、最後の改行が取り除かれています)。このデフォルト実装は、単に入力値をそのまま返します。


## [16.6.5. フィルタオブジェクト](https://docs.python.jp/3/library/logging.html#filter-objects)

> フィルタ (Filter) は、ハンドラ や ロガー によって使われ、レベルによって提供されるのよりも洗練されたフィルタリングを実現します。基底のフィルタクラスは、ロガー階層構造内の特定地点の配下にあるイベントだけを許可します。例えば、'A.B' で初期化されたフィルタは、ロガー 'A.B', 'A.B.C', 'A.B.C.D', 'A.B.D' 等によって記録されたイベントは許可しますが、'A.BB', 'B.A.B' などは許可しません。空の文字列で初期化された場合、すべてのイベントを通過させます。

属性|概要
----|----
class logging.Filter(name='')|Filter クラスのインスタンスを返します。 name が指定されていれば、 name はロガーの名前を表します。指定されたロガーとその子ロガーのイベントがフィルタを通過できるようになります。 name が指定されなければ、すべてのイベントを通過させます。
filter(record)|指定されたレコードがログされるべきか？no ならばばゼロを、yes ならばゼロでない値を返します。適切と判断されれば、このメソッドによってレコードはその場で修正されることがあります。

> ハンドラに対するフィルタはハンドラがイベントを発行する前に試され、一方ではロガーに対するフィルタは、イベントが(debug(), info() などによって)ロギングされる際には、ハンドラにイベントが送信される前にはいつでも試されることに注意してください。そのフィルタがそれら子孫ロガーにも適用されていない限り、子孫ロガーによって生成されたイベントはロガーのフィルタ設定によってフィルタされることはありません。

> 実際には、Filter をサブクラス化する必要はありません。同じ意味の filter メソッドを持つ、すべてのインスタンスを通せます。

> バージョン 3.2 で変更: 特殊な Filter クラスを作ったり、 filter メソッドを持つ他のクラスを使う必要はありません: 関数 (あるいは他の callable) をフィルタとして使用することができます。フィルタロジックは、フィルタオブジェクトが filter 属性を持っているかどうかチェックします: もし filter 属性を持っていたら、それは Filter であると仮定され、その filter() メソッドが呼び出されます。そうでなければ、それは callable であると仮定され、レコードを単一のパラメータとして呼び出されます。返される値は filter() によって返されるものと一致すべきです。

> フィルタは本来、レコードをレベルよりも洗練された基準に基づいてフィルタするために使われますが、それが取り付けられたハンドラやロガーによって処理されるレコードをすべて監視します。これは、特定のロガーやハンドラに処理されたレコードの数を数えたり、処理されている LogRecord の属性を追加、変更、削除したりするときに便利です。もちろん、LogRecord を変更するには注意が必要ですが、これにより、ログにコンテキスト情報を注入できます (Filter を使ったコンテキスト情報の伝達 を参照してください)。

## [16.6.6. LogRecord オブジェクト](https://docs.python.jp/3/library/logging.html#logrecord-objects)

> LogRecord インスタンスは、何かをログ記録するたびに Logger によって生成されます。また、 makeLogRecord() を通して (例えば、ワイヤを通して受け取られた pickle 化されたイベントから) 手動で生成することも出来ます。

属性|概要
----|----
class logging.LogRecord(name, level, pathname, lineno, msg, args, exc_info, func=None, sinfo=None)|ロギングされているイベントに適切なすべての情報を含みます。
getMessage()|ユーザが提供した引数をメッセージに交ぜた後、この LogRecord インスタンスへのメッセージを返します。ユーザがロギングの呼び出しに与えた引数が文字列でなければ、その引数に str() が呼ばれ、文字列に変換されます。これにより、 __str__ メソッドが実際のフォーマット文字列を返せるようなユーザ定義のクラスをメッセージとして使えます。

### logging.LogRecordの引数

引数|説明
----|----
name|この LogRecord で表されるイベントをロギングするのに使われるロガーの名前です。ここで与える名前が、たとえ他の(祖先の)ロガーに結び付けられたハンドラによって発せられるとしても、与えたこの値のままであることに注意してください。
level|このロギングイベントの数値のレベル (DEBUG, INFO などのいずれか) です。なお、これは LogRecord の 2つの 属性に変換されます。数値 levelno と、対応するレベル名 levelname です。
pathname|ロギングの呼び出しが発せられたファイルの完全なパス名。
lineno|ロギングの呼び出しが発せられたソース行番号。
msg|イベント記述メッセージで、これは変数データのプレースホルダを持つフォーマット文字列になり得ます。
args|msg 引数と組み合わせてイベント記述を得るための変数データです。
exc_info|現在の例外情報を含む例外タプルか、利用できる例外情報がない場合は None です。
func|ロギングの呼び出しを行った関数またはメソッドの名前です。
sinfo|現在のスレッドのスタックベースからログ呼び出しまでの間のスタック情報を表わすテキスト文字列。

### 例

```python
old_factory = logging.getLogRecordFactory()

def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.custom_attribute = 0xdecafbad
    return record

logging.setLogRecordFactory(record_factory)
```


## [16.6.7. LogRecord 属性](https://docs.python.jp/3/library/logging.html#logrecord-attributes)

> LogRecord には幾つかの属性があり、そのほとんどはコンストラクタの引数から得られます。(なお、LogRecord コンストラクタの引数と LogRecord 属性が常に厳密に対応するわけではありません。) これらの属性は、レコードからのデータをフォーマット文字列に統合するのに使えます。以下のテーブルに、属性名、意味、そして % 形式フォーマット文字列における対応するプレースホルダを (アルファベット順に) 列挙します。

> {}-フォーマット (str.format()) を使用していれば、書式文字列の中でプレースホールダーとして {attrname} を使うことができます。 $-フォーマット (string.Template) を使用している場合は、 ${attrname} 形式にしてください。もちろん、両方の場合で attrname は使用したい実際の属性名に置き換えてください。

> {}-フォーマットの場合には、属性名の後にフォーマットフラグを指定することができます。属性名とフォーマットフラグの間はコロンで分割します。例: プレースホールダー {msecs:03d} は、ミリセカンド値 4 を 004 としてフォーマットします。利用可能なオプション上の全詳細に関しては str.format() ドキュメンテーションを参照してください。

属性名|フォーマット|説明
------|------------|----
args|このフォーマットを自分で使う必要はないでしょう。|msg に組み合わせて message を生成するための引数のタプル、または、マージに用いられる辞書(引数が一つしかなく、かつそれが辞書の場合)。
asctime|%(asctime)s|LogRecord が生成された時刻を人間が読める書式で表したもの。デフォルトでは "2003-07-08 16:49:45,896" 形式 (コンマ以降の数字は時刻のミリ秒部分) です。
created|%(created)f|LogRecord が生成された時刻 (time.time() によって返される形式で)。
exc_info|このフォーマットを自分で使う必要はないでしょう。|(sys.exc_info 風の) 例外タプルか、例外が起こっていない場合は None。
ファイル名|%(filename)s|pathname のファイル名部分。
funcName|%(funcName)s|ロギングの呼び出しを含む関数の名前。
levelname|%(levelname)s|メッセージのための文字のロギングレベル ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')。
levelno|%(levelno)s|メッセージのための数値のロギングレベル (DEBUG, INFO, WARNING, ERROR, CRITICAL)。
lineno|%(lineno)d|ロギングの呼び出しが発せられたソース行番号 (利用できる場合のみ)。
module|%(module)s|モジュール (filename の名前部分)。
msecs|%(msecs)d|LogRecord が生成された時刻のミリ秒部分。
message|%(message)s|msg % args として求められた、ログメッセージ。 Formatter.format() が呼び出されたときに設定されます。
msg|このフォーマットを自分で使う必要はないでしょう。|元のロギングの呼び出しで渡されたフォーマット文字列。 args と合わせて、 message 、または任意のオブジェクトを生成します (任意のオブジェクトをメッセージに使用する 参照)。
名前|%(name)s|ロギングに使われたロガーの名前。
pathname|%(pathname)s|ロギングの呼び出しが発せられたファイルの完全なパス名 (利用できる場合のみ)。
process|%(process)d|プロセス ID (利用可能な場合のみ)。
processName|%(processName)s|プロセス名 (利用可能な場合のみ)。
relativeCreated|%(relativeCreated)d|logging モジュールが読み込まれた時刻に対する、LogRecord が生成された時刻を、ミリ秒で表したもの。
stack_info|このフォーマットを自分で使う必要はないでしょう。|現在のスレッドでのスタックの底からこのレコードの生成に帰着したログ呼び出しまでのスタックフレーム情報 (利用可能な場合)。
thread|%(thread)d|スレッド ID (利用可能な場合のみ)。
threadName|%(threadName)s|スレッド名 (利用可能な場合のみ)。

## [16.6.8. LoggerAdapter オブジェクト](https://docs.python.jp/3/library/logging.html#loggeradapter-objects)

> LoggerAdapter インスタンスは文脈情報をログ記録呼び出しに渡すのを簡単にするために使われます。使い方の例は コンテキスト情報をログ記録出力に付加する を参照してください。

属性|概要
----|----
class logging.LoggerAdapter(logger, extra)|内部で使う Logger インスタンスと辞書風 (dict-like) オブジェクトで初期化した LoggerAdapter のインスタンスを返します。
process(msg, kwargs)|文脈情報を挿入するために、ログ記録呼び出しに渡されたメッセージおよび/またはキーワード引数に変更を加えます。ここでの実装は extra としてコンストラクタに渡されたオブジェクトを取り、'extra' キーを使って kwargs に加えます。返り値は (msg, kwargs) というタプルで、(変更されているはずの) 渡された引数を含みます。

> LoggerAdapter は上記に加え Logger のメソッド debug(), info(), warning(), error(), exception(), critical(), log(), isEnabledFor(), getEffectiveLevel(), setLevel(), hasHandlers() をサポートします。これらは Logger の対応するメソッドと同じシグニチャを持つため、2つのインスタンスは区別せずに利用出来ます。

> バージョン 3.2 で変更: isEnabledFor(), getEffectiveLevel(), setLevel(), hasHandlers() が LoggerAdapter に追加されました。これらメソッドは元のロガーに処理を委譲します。

## [16.6.9. スレッドセーフ性](https://docs.python.jp/3/library/logging.html#thread-safety)

> logging モジュールは、クライアントで特殊な作業を必要としない限りスレッドセーフになっています。このスレッドセーフ性はスレッドロックによって達成されています; モジュールの共有データへのアクセスを直列化するためのロックが一つ存在し、各ハンドラでも背後にある I/O へのアクセスを直列化するためにロックを生成します。

> signal モジュールを使用して非同期シグナルハンドラを実装している場合、そのようなハンドラからはログ記録を使用できないかもしれません。これは、 threading モジュールにおけるロック実装が常にリエントラントではなく、そのようなシグナルハンドラから呼び出すことができないからです。

## [16.6.10. モジュールレベルの関数](https://docs.python.jp/3/library/logging.html#module-level-functions)

上で述べたクラスに加えて、いくつかのモジュールレベルの関数が存在します。

属性|概要
----|----
logging.getLogger(name=None)|指定された名前のロガーを返します。名前が None であれば、ロガー階層のルート (root) にあるロガーを返します。name を指定する場合には、通常は 'a', 'a.b', 'a.b.c.d' といったドット区切りの階層的な名前にします。名前の付け方はログ機能を使う開発者次第です。
logging.getLoggerClass()|標準の Logger クラスか、最後に setLoggerClass() に渡したクラスを返します。この関数は、新たなクラス定義の中で呼び出して、カスタマイズした Logger クラスのインストールが既に他のコードで適用したカスタマイズを取り消さないことを保証するために使われることがあります。例えば以下のようにします:
logging.getLogRecordFactory()|LogRecord を生成するのに使われる callable を返します。
logging.debug(msg, *args, **kwargs)|レベル DEBUG のメッセージをルートロガーで記録します。 msg はメッセージの書式文字列で、 args は msg に文字列書式化演算子を使って取り込むための引数です。 (これは、書式文字列の中でキーワードを使い、引数として単一の辞書を渡すことができる、ということを意味します。)
logging.info(msg, *args, **kwargs)|レベル INFO のメッセージをルートロガーで記録します。引数は debug() と同じように解釈されます。
logging.warning(msg, *args, **kwargs)|レベル WARNING のメッセージをルートロガーで記録します。引数は debug() と同じように解釈されます。
logging.error(msg, *args, **kwargs)|レベル ERROR のメッセージをルートロガーで記録します。引数は debug() と同じように解釈されます。
logging.critical(msg, *args, **kwargs)|レベル CRITICAL のメッセージをルートロガーで記録します。引数は debug() と同じように解釈されます。
logging.exception(msg, *args, **kwargs)|レベル ERROR のメッセージをルートロガーで記録します。引数は debug() と同じように解釈されます。例外情報がログメッセージに追加されます。このメソッドは例外ハンドラからのみ呼び出されます。
logging.log(level, msg, *args, **kwargs)|レベル level のメッセージをルートロガーで記録します。その他の引数は debug() と同じように解釈されます。
logging.disable(lvl)|全てのロガーのレベル lvl を上書きし、これはロガー自身の出力レベルよりも優先されます。アプリケーション全体を横断するログ出力を一時的に調整する必要が生じたら、この関数は便利でしょう。これの効果は重大度 lvl 以下の全てのロギング呼び出しを無効にすることですので、INFO で呼び出しをすれば、INFO と DEBUG イベントが捨てられる一方で、重大度 WARNING 以上のものは、ロガーの有効レベルに基いて処理されます。 logging.disable(logging.NOTSET) が呼び出されると、この上書きレベルは削除され、ログ出力は再び個々のロガーの有効レベルに依存するようになります。
logging.addLevelName(lvl, levelName)|内部的な辞書の中でレベル lvl をテキスト levelName に関連付けます。これは例えば Formatter でメッセージを書式化する際のように、数字のレベルをテキスト表現に対応付ける際に用いられます。この関数は自作のレベルを定義するために使うこともできます。使われるレベルに対する唯一の制限は、レベルは正の整数でなくてはならず、メッセージの深刻度が上がるに従ってレベルの数も上がらなくてはならないということです。
logging.getLevelName(lvl)|ログ記録レベル lvl のテキスト表現を返します。レベルが定義済みのレベル CRITICAL, ERROR, WARNING, INFO, DEBUG のいずれかである場合、対応する文字列が返されます。 addLevelName() を使ってレベルに名前を関連付けていた場合、 lvl に関連付けられた名前が返されます。定義済みのレベルに対応する数値を指定した場合、レベルに対応した文字列表現を返します。そうでない場合、文字列 'Level %s' % lvl を返します。
logging.makeLogRecord(attrdict)|属性が attrdict で定義された、新しい LogRecord インスタンスを生成して返します。この関数は、 pickle された LogRecord 属性の辞書をソケットを介して送信し、受信端で LogRecord インスタンスとして再構成する場合に便利です。
logging.basicConfig(**kwargs)|デフォルトの Formatter を持つ StreamHandler を生成してルートロガーに追加し、ロギングシステムの基本的な環境設定を行います。関数 debug(), info(), warning(), error(), critical() は、ルートロガーにハンドラが定義されていない場合に自動的に basicConfig() を呼び出します。
logging.shutdown()|ロギングシステムに対して、バッファのフラッシュを行い、すべてのハンドラを閉じることで順次シャットダウンを行うように告知します。この関数はアプリケーションの終了時に呼ばれるべきであり、また呼び出し以降はそれ以上ロギングシステムを使ってはなりません。
logging.setLoggerClass(klass)|ロギングシステムに対して、ロガーをインスタンス化する際にクラス klass を使うように指示します。指定するクラスは引数として名前だけをとるようなメソッド __init__() を定義していなければならず、 __init__() では Logger.__init__() を呼び出さなければなりません。典型的な利用法として、この関数は自作のロガーを必要とするようなアプリケーションにおいて、他のロガーがインスタンス化される前にインスタンス化されます。
logging.setLogRecordFactory(factory)|LogRecord を生成するのに使われる callable をセットします。パラメータ:	factory – ログレコードを生成するファクトリとして振舞う callable。


> logging.basicConfig(**kwargs)は以下のキーワード引数がサポートされます。

フォーマット|説明
------------|----
filename|StreamHandler ではなく指定された名前で FileHandler が作られます。
filemode|filename が指定されているとき、ファイルモードを指定します (filemode が指定されない場合デフォルトは 'a' です)。
format|指定された書式文字列をハンドラで使います。
datefmt|指定された日付/時刻の書式を使います。
style|format が指定された場合は、書式文字列にこのスタイルを使用します。 '%', '{', '$' のうちの1つで、それぞれ %-format 、 str.format() 、 string.Template に対応します。指定されなかった場合、デフォルトで '%' になります。
level|ルートロガーのレベルを指定されたものにします。
stream|指定されたストリームを StreamHandler の初期化に使います。この引数は 'filename' と同時には使えないことに注意してください。両方が指定されたときには ValueError が送出されます。
handlers|もし指定されれば、これは root ロガーに追加される既に作られたハンドラのイテラブルになります。まだフォーマッタがセットされていないすべてのハンドラは、この関数で作られたデフォルトフォーマッタが割り当てられることになります。この引数は 'filename' や 'stream' と互換性がないことに注意してください。両方が存在する場合 ValueError が上げられます。

> logging.setLogRecordFactory(factory)のファクトリは以下のようなシグネチャを持っています:

* factory(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)

引数|説明
----|----
name|ロガーの名前。
level|ログレベル (数値)。
fn|ログ呼び出しが行われたファイルのフルパス名。
lno|ログ呼び出しが行われたファイルの行数。
msg|ログメッセージ。
args|ログメッセージに対する引数。
exc_info|例外タプルまたは None。
func|ログ呼び出しを起動した関数またはメソッドの名前。
sinfo|traceback.print_stack() で提供されるような、呼び出し階層を示すスタックトレースバック。
kwargs|追加のキーワード引数。

## [16.6.11. モジュールレベル属性](https://docs.python.jp/3/library/logging.html#module-level-attributes)

属性|概要
----|----
logging.lastResort|「最後の手段のハンドラ」が、この属性で利用可能です。これは StreamHandler が sys.stderr に WARNING レベルで書き出しているのがそうですし、ロギングの設定がなにか不在のロギングイベントを扱う場合に使われます。最終的な結果は、メッセージを単に sys.stderr に出力することです。これはかつて「logger XYZ についてのハンドラが見つかりません」と言っていたエラーメッセージを置き換えています。もしも何らかの理由でその昔の振る舞いが必要な場合は、 lastResort に None をセットすれば良いです。

## [16.6.12. warnings モジュールとの統合](https://docs.python.jp/3/library/logging.html#integration-with-the-warnings-module)

> captureWarnings() 関数を使って、 logging を warnings モジュールと統合できます。

属性|概要
----|----
logging.captureWarnings(capture)|この関数は、logging による警告の補足を、有効にまたは無効にします。

### 参考

URL|概要
---|----
[logging.config](https://docs.python.jp/3/library/logging.config.html#module-logging.config)|logging モジュールの環境設定 API です。
[logging.handlers](https://docs.python.jp/3/library/logging.handlers.html#module-logging.handlers)|logging モジュールに含まれる、便利なハンドラです。
[PEP 282 - ログシステム](https://www.python.org/dev/peps/pep-0282)|この機能を Python 標準ライブラリに含めることを述べた提案です。
[Original Python logging package](https://www.red-dove.com/python_logging.html)|これは、 logging パッケージのオリジナルのソースです。このサイトから利用できるバージョンのパッケージは、 logging パッケージを標準ライブラリに含まない、 Python 1.5.2, 2.1.x および 2.2.x で使うのに適しています。


