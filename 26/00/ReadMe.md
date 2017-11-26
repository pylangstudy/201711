# [16.8. logging.handlers — ロギングハンドラ](https://docs.python.jp/3/library/logging.handlers.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/logging/handlers.py](https://github.com/python/cpython/tree/3.6/Lib/logging/handlers.py)

> このパッケージでは、以下の便利なハンドラが提供されています。なお、これらのハンドラのうち、3 つ (StreamHandler, FileHandler および NullHandler) は、実際には logging モジュール自身で定義されていますが、他のハンドラと一緒にここでドキュメント化します。

## Important

* [基本チュートリアル](https://docs.python.jp/3/howto/logging.html#logging-basic-tutorial)
* [上級チュートリアル](https://docs.python.jp/3/howto/logging.html#logging-advanced-tutorial)
* [ロギングクックブック](https://docs.python.jp/3/howto/logging-cookbook.html#logging-cookbook)

## 一覧

Handler|概要
-------|----
[16.8.1. StreamHandler](https://docs.python.jp/3/library/logging.handlers.html#streamhandler)|sys.stdout, sys.stderr, file-likeなどwrite()、flush()メソッドをサポートする何らかのオブジェクトに送信します。
[16.8.2. FileHandler](https://docs.python.jp/3/library/logging.handlers.html#filehandler)|ディスク上のファイルに送信します。
[16.8.3. NullHandler](https://docs.python.jp/3/library/logging.handlers.html#nullhandler)|いかなる書式化も出力も行いません。これは本質的には、ライブラリ開発者に使われる 'no-op' ハンドラです。
[16.8.4. WatchedFileHandler](https://docs.python.jp/3/library/logging.handlers.html#watchedfilehandler)|ログ記録先のファイルを監視する FileHandler の一種です。ファイルが変更された場合、ファイルを閉じてからファイル名を使って開き直します。
[16.8.5. BaseRotatingHandler](https://docs.python.jp/3/library/logging.handlers.html#baserotatinghandler)|ローテートを行うファイルハンドラ RotatingFileHandler と TimedRotatingFileHandler のベースクラスです。
[16.8.6. RotatingFileHandler](https://docs.python.jp/3/library/logging.handlers.html#rotatingfilehandler)|ディスク上のログファイルに対するローテーション処理をサポートします。
[16.8.7. TimedRotatingFileHandler](https://docs.python.jp/3/library/logging.handlers.html#timedrotatingfilehandler)|特定の時間間隔でのログローテーションをサポートしています。
[16.8.8. SocketHandler](https://docs.python.jp/3/library/logging.handlers.html#sockethandler)|ログ出力をネットワークソケットに送信します。基底クラスでは TCP ソケットを用います。
[16.8.9. DatagramHandler](https://docs.python.jp/3/library/logging.handlers.html#datagramhandler)|UDP ソケットを介したログ記録メッセージの送信をサポートしています。
[16.8.10. SysLogHandler](https://docs.python.jp/3/library/logging.handlers.html#sysloghandler)|ログ記録メッセージを遠隔またはローカルの Unix syslog に送信する機能をサポートしています。
[16.8.11. NTEventLogHandler](https://docs.python.jp/3/library/logging.handlers.html#nteventloghandler)|ログ記録メッセージをローカルな Windows NT, Windows 2000, または Windows XP のイベントログに送信する機能をサポートします。この機能を使えるようにするには、 Mark Hammond による Python 用 Win32 拡張パッケージをインストールする必要があります。
[16.8.12. SMTPHandler](https://docs.python.jp/3/library/logging.handlers.html#smtphandler)|SMTP を介したログ記録メッセージの送信機能をサポートします。
[16.8.13. MemoryHandler](https://docs.python.jp/3/library/logging.handlers.html#memoryhandler)|ログ記録するレコードをメモリ上にバッファリングし、定期的にその内容をターゲット (target) となるハンドラにフラッシュする機能をサポートしています。
[16.8.14. HTTPHandler](https://docs.python.jp/3/library/logging.handlers.html#httphandler)|ログ記録メッセージを GET または POST セマンティクスを使って Web サーバに送信する機能をサポートしています。
[16.8.15. QueueHandler](https://docs.python.jp/3/library/logging.handlers.html#queuehandler)|queue モジュールや multiprocessing のモジュールで実装されるようなキューにログメッセージを送信する機能をサポートしています。
[16.8.16. QueueListener](https://docs.python.jp/3/library/logging.handlers.html#queuelistener)|queue モジュールや multiprocessing のモジュールで実装されるようなキューからログメッセージを受信する機能をサポートしています。メッセージは内部スレッドのキューから受信され、同じスレッド上の複数のハンドラに渡されて処理されます。 QueueListener それ自体はハンドラではありませんが、 QueueHandler と連携して動作するのでここで文書化されています。

## [16.8.1. StreamHandler](https://docs.python.jp/3/library/logging.handlers.html#streamhandler)

> logging コアパッケージに含まれる StreamHandler クラスは、ログ出力を sys.stdout, sys.stderr あるいは何らかのファイル風 (file-like) オブジェクト (あるいは、より正確に言えば write() および flush() メソッドをサポートする何らかのオブジェクト) といったストリームに送信します。

属性|概要
----|----
class logging.StreamHandler(stream=None)|StreamHandler クラスの新たなインスタンスを返します。 stream が指定された場合、インスタンスはログ出力先として指定されたストリームを使います; そうでない場合、 sys.stderr が使われます。
emit(record)|フォーマッタが指定されていれば、フォーマッタを使ってレコードを書式化します。 次に、レコードが終端記号とともにストリームに書き込まれます。 例外情報が存在する場合、 traceback.print_exception() を使って書式化され、 ストリームの末尾につけられます。
flush()|ストリームの flush() メソッドを呼び出してバッファをフラッシュします。 close() メソッドは Handler から継承しているため何も出力を行わないので、 flush() 呼び出しを明示的に行う必要があるかもしれません。

> バージョン 3.2 で変更: StreamHandler クラスに terminator 属性が追加されました (デフォルト値は '\n')。これは、書式化されたレコードをストリームに書き込むときの終端記号として使用されます。このような改行による終端を望まなければ、ハンドラ・インスタンスの terminator 属性を空の文字列に設定することができます。初期のバージョンでは、終端記号は '\n' としてハードコードされていました。

## [16.8.2. FileHandler](https://docs.python.jp/3/library/logging.handlers.html#filehandler)

> logging コアパッケージに含まれる FileHandler クラスは、ログ出力をディスク上のファイルに送信します。このクラスは出力機能を StreamHandler から継承しています。

属性|概要
----|----
class logging.FileHandler(filename, mode='a', encoding=None, delay=False)|FileHandler クラスの新たなインスタンスを返します。 指定されたファイルが開かれ、ログ記録のためのストリームとして使われます。 mode が指定されなかった場合、 'a' が使われます。 encoding が None でない場合、その値はファイルを開くときのエンコーディングとして使われます。 delay が真ならば、ファイルを開くのは最初の emit() 呼び出しまで遅らせられます。 デフォルトでは、ファイルは無制限に大きくなりつづけます。
close()|ファイルを閉じます。
emit(record)|record をファイルに出力します。

## [16.8.3. NullHandler](https://docs.python.jp/3/library/logging.handlers.html#nullhandler)

> バージョン 3.1 で追加.

> logging コアパッケージに含まれる NullHandler クラスは、いかなる書式化も出力も行いません。これは本質的には、ライブラリ開発者に使われる 'no-op' ハンドラです。

属性|概要
----|----
class logging.NullHandler|NullHandler クラスの新しいインスタンスを返します。
emit(record)|このメソッドは何もしません。
handle(record)|このメソッドは何もしません。
createLock()|アクセスが特殊化される必要がある I/O が下にないので、このメソッドはロックに対して None を返します。

> NullHandler の使い方の詳しい情報は、 ライブラリのためのロギングの設定 を参照してください。

## [16.8.4. WatchedFileHandler](https://docs.python.jp/3/library/logging.handlers.html#watchedfilehandler)

> logging.handlers モジュールに含まれる WatchedFileHandler クラスは、ログ記録先のファイルを監視する FileHandler の一種です。ファイルが変更された場合、ファイルを閉じてからファイル名を使って開き直します。

> ファイルはログファイルをローテーションさせる newsyslog や logrotate のようなプログラムを使うことで変更されることがあります。このハンドラは、 Unix/Linux で使われることを意図していますが、ファイルが最後にログを出力してから変わったかどうかを監視します。 (ファイルはデバイスや inode が変わることで変わったと判断します。) ファイルが変わったら古いファイルのストリームは閉じて、現在のファイルを新しいストリームを取得するために開きます。

> このハンドラを Windows で使うことは適切ではありません。というのも Windows では開いているログファイルを移動したり削除したりできないからです - logging はファイルを排他的ロックを掛けて開きます - そのためこうしたハンドラは必要ないのです。さらに、 Windows では ST_INO がサポートされていません; stat() はこの値として常に 0 を返します。

属性|概要
----|----
class logging.handlers.WatchedFileHandler(filename, mode='a', encoding=None, delay=False)|WatchedFileHandler クラスの新たなインスタンスを返します。 指定されたファイルが開かれ、ログ記録のためのストリームとして使われます。 mode が指定されなかった場合、 'a' が使われます。 encoding が None でない場合、その値はファイルを開くときのエンコーディングとして使われます。 delay が真ならば、ファイルを開くのは最初の emit() 呼び出しまで遅らせられます。 デフォルトでは、ファイルは無制限に大きくなりつづけます。
reopenIfNeeded()|Checks to see if the file has changed. If it has, the existing stream is flushed and closed and the file opened again, typically as a precursor to outputting the record to the file.
emit(record)|Outputs the record to the file, but first calls reopenIfNeeded() to reopen the file if it has changed.

## [16.8.5. BaseRotatingHandler](https://docs.python.jp/3/library/logging.handlers.html#baserotatinghandler)

> logging.handlers モジュールに存在する BaseRotatingHandler クラスは、ローテートを行うファイルハンドラ RotatingFileHandler と TimedRotatingFileHandler のベースクラスです。このクラスをインスタンス化する必要はありませんが、オーバーライドすることになるかもしれない属性とメソッドを持っています。

属性|概要
----|----
class logging.handlers.BaseRotatingHandler(filename, mode, encoding=None, delay=False)|パラメータは FileHandler と同じです。属性は次の通りです:
namer|この属性に callable がセットされた場合、 rotation_filename() メソッドはこの callable に委譲されます。 callable に渡されるパラメータは rotation_filename() に渡されたものです。
rotator|この属性に callable がセットされた場合、 rotate() メソッドはこの callable に委譲されます。 callable に渡されるパラメータは rotate() に渡されたものです。
rotation_filename(default_name)|ローテートを行う際にログファイルのファイル名を変更します。
rotate(source, dest)|ローテートが行われる時、現在のログをローテートします。

> これらの属性が存在する理由は、サブクラス化を省略できるようにするためです。 RotatingFileHandler と TimedRotatingFileHandler のインスタンスに対して同じ callable が使えます。もし namer や rotator callable が例外を上げれば、 emit() 呼び出しで発生した他の例外と同じ方法で、つまりハンドラの handleError() メソッドによって扱われます。

> ローテート処理に大幅な変更を加える必要があれば、メソッドをオーバーライドすることができます。

> 例えば、 rotator と namer を使ってログローテートをカスタマイズする を参照してください。

## [16.8.6. RotatingFileHandler](https://docs.python.jp/3/library/logging.handlers.html#rotatingfilehandler)

> logging.handlers モジュールに含まれる RotatingFileHandler クラスは、ディスク上のログファイルに対するローテーション処理をサポートします。

属性|概要
----|----
class logging.handlers.RotatingFileHandler(filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=False)|RotatingFileHandler クラスの新たなインスタンスを返します。 指定されたファイルが開かれ、ログ記録のためのストリームとして使われます。 mode が指定されなかった場合、 'a' が使われます。 encoding が None でない場合、その値はファイルを開くときのエンコーディングとして使われます。 delay が真ならば、ファイルを開くのは最初の emit() 呼び出しまで遅らせられます。 デフォルトでは、ファイルは無制限に大きくなりつづけます。
doRollover()|上述のような方法でロールオーバを行います。
emit(record)|上述のようなロールオーバを行いながら、レコードをファイルに出力します。

## [16.8.7. TimedRotatingFileHandler](https://docs.python.jp/3/library/logging.handlers.html#timedrotatingfilehandler)

> logging.handlers モジュールに含まれる TimedRotatingFileHandler クラスは、特定の時間間隔でのログローテーションをサポートしています。

属性|概要
----|----
class logging.handlers.TimedRotatingFileHandler(filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None)|TimedRotatingFileHandler クラスの新たなインスタンスを返します。 filename に指定したファイルを開き、ログ出力先のストリームとして使います。ログファイルのローテーション時には、ファイル名に拡張子 (suffix) をつけます。ログファイルのローテーションは when および interval の積に基づいて行います。
doRollover()|上述のような方法でロールオーバを行います。
emit(record)|上で説明した方法でロールオーバを行いながら、レコードをファイルに出力します。

> when は interval の単位を指定するために使います。使える値は下表の通りです。大小文字の区別は行いません。

値|interval の単位|If/how atTime is used
--|---------------|---------------------
'S'|秒|無視
'M'|分|無視
'H'|時間|無視
'D'|日|無視
'W0'-'W6'|曜日 (0=月曜)|Used to compute initial rollover time
'midnight'|Roll over at midnight, if atTime not specified, else at time atTime|Used to compute initial rollover time

> 曜日ベースのローテーションを使う場合は、月曜として 'W0' を、火曜として 'W1' を、…、日曜として 'W6' を指定します。このケースの場合は、 interval は使われません。

> 古いログファイルの保存時、ロギングシステムによりファイル名に拡張子が付けられます。 ロールオーバ間隔によって、strftime の %Y-%m-%d_%H-%M-%S 形式またはその前方の一部を使って、日付と時間に基づいた拡張子が付けられます。

> 最初に次のロールオーバー時間を計算するとき (ハンドラが生成されるとき)、次のローテーションがいつ起こるかを計算するために、既存のログファイルの最終変更時刻または現在の時間が使用されます。

> utc 引数が true の場合時刻は UTC になり、それ以外では現地時間が使われます。

> backupCount がゼロでない場合、保存されるファイル数は高々 backupCount 個で、それ以上のファイルがロールオーバされる時に作られるならば、一番古いものが削除されます。削除のロジックは interval で決まるファイルを削除するので、 interval を変えると古いファイルが残ったままになることもあります。

> delay が true なら、ファイルを開くのは emit() の最初の呼び出しまで延期されます。

> If atTime is not None, it must be a datetime.time instance which specifies the time of day when rollover occurs, for the cases where rollover is set to happen "at midnight" or "on a particular weekday". Note that in these cases, the atTime value is effectively used to compute the initial rollover, and subsequent rollovers would be calculated via the normal interval calculation.

翻訳

> atTimeがNoneでない場合は、ロールオーバーが "真夜中"または "特定の曜日に"に設定されている場合の、ロールオーバーが発生する時刻を指定するdatetime.timeインスタンスでなければなりません。 これらの場合、atTime値は初期ロールオーバを計算するために有効に使用され、その後のロールオーバは通常のインターバル計算によって計算されることに注意してください。

### 注釈

> Calculation of the initial rollover time is done when the handler is initialised. Calculation of subsequent rollover times is done only when rollover occurs, and rollover occurs only when emitting output. If this is not kept in mind, it might lead to some confusion. For example, if an interval of "every minute" is set, that does not mean you will always see log files with times (in the filename) separated by a minute; if, during application execution, logging output is generated more frequently than once a minute, then you can expect to see log files with times separated by a minute. If, on the other hand, logging messages are only output once every five minutes (say), then there will be gaps in the file times corresponding to the minutes where no output (and hence no rollover) occurred.

翻訳

> 初期ロールオーバー時間の計算は、ハンドラが初期化されたときに行われます。 後続のロールオーバ時間の計算は、ロールオーバが発生した場合にのみ行われ、ロールオーバーは出力を出力する場合にのみ発生します。 これが覚えていないと、混乱が生じる可能性があります。 たとえば、「1分ごと」の間隔が設定されている場合、1分ごとに区切られた（ファイル名の）ログファイルが常に表示されるわけではありません。 アプリケーションの実行中にログ出力が1分に1回よりも頻繁に生成される場合は、分単位でログファイルを表示することが期待できます。 一方、ロギングメッセージが5分ごとに出力される（たとえば）場合、出力がない（したがってロールオーバーが発生しなかった）分に対応するファイル時間にギャップが存在します。

## [16.8.8. SocketHandler](https://docs.python.jp/3/library/logging.handlers.html#sockethandler)

> logging.handlers モジュールに含まれる SocketHandler クラスは、ログ出力をネットワークソケットに送信します。基底クラスでは TCP ソケットを用います。

属性|概要
----|----
class logging.handlers.SocketHandler(host, port)|アドレスが host および port で与えられた遠隔のマシンと通信するようにした SocketHandler クラスのインスタンスを生成して返します。
close()|ソケットを閉じます。
emit()|レコードの属性辞書を pickle して、バイナリ形式でソケットに書き込みます。ソケット操作でエラーが生じた場合、暗黙のうちにパケットは捨てられます。事前に接続が失われていた場合、接続を再度確立します。受信端でレコードを unpickle して LogRecord にするには、 makeLogRecord() 関数を使ってください。
handleError()|emit() の処理中に発生したエラーを処理します。よくある原因は接続の消失です。次のイベント発生時に再試行できるようにソケットを閉じます。
makeSocket()|サブクラスで必要なソケット形式を詳細に定義できるようにするためのファクトリメソッドです。デフォルトの実装では、 TCP ソケット (socket.SOCK_STREAM) を生成します。
makePickle(record)|レコードの属性辞書を pickle してから先頭に長さ情報を付けてバイナリ形式にして、ソケットを介して送信できるようにして返します。
send(packet)|pickle された文字列 packet をソケットに送信します。この関数はネットワークがビジーの時に発生する部分的送信に対応しています。
createSocket()|ソケットの生成を試みます。失敗時には、指数的な減速アルゴリズムを使います。最初の失敗時には、ハンドラは送ろうとしていたメッセージを落とします。続くメッセージが同じインスタンスで扱われたとき、幾らかの時間が経過するまで接続を試みません。デフォルトのパラメタは、最初の遅延時間が 1 秒で、その遅延時間の後でそれでも接続が確保できないなら、遅延時間は 2 倍づつになり、最大で 30 秒になります。

> この働きは、以下のハンドラ属性で制御されます:

ハンドラ属性|説明
------------|----
retryStart|最初の遅延時間、デフォルトは 1.0 秒
retryFactor|乗数、デフォルトは 2.0
retryMax|最大遅延時間、デフォルトは 30.0 秒

> つまり、ハンドラが使われた 後に リモートリスナが起動した場合、メッセージが失われてしまうことがあります (ハンドラは、遅延時間が経過するまで接続を試みようとさえせず、その遅延時間中に通知なくメッセージを捨てるので)。

## [16.8.9. DatagramHandler](https://docs.python.jp/3/library/logging.handlers.html#datagramhandler)

> logging.handlers モジュールに含まれる DatagramHandler クラスは、 SocketHandler を継承しており、 UDP ソケットを介したログ記録メッセージの送信をサポートしています。

属性|概要
----|----
class logging.handlers.DatagramHandler(host, port)|アドレスが host および port で与えられた遠隔のマシンと通信するようにした DatagramHandler クラスのインスタンスを生成して返します。
emit()|レコードの属性辞書を pickle して、バイナリ形式でソケットに書き込みます。ソケット操作でエラーが生じた場合、暗黙のうちにパケットは捨てられます。事前に接続が失われていた場合、接続を再度確立します。受信端でレコードを unpickle して LogRecord にするには、 makeLogRecord() 関数を使ってください。
makeSocket()|ここで SocketHandler のファクトリメソッドをオーバライドして、 UDP ソケット (socket.SOCK_DGRAM) を生成しています。
send(s)|pickle された文字列をソケットに送信します。

## [16.8.10. SysLogHandler](https://docs.python.jp/3/library/logging.handlers.html#sysloghandler)

> logging.handlers モジュールに含まれる SysLogHandler クラスは、ログ記録メッセージを遠隔またはローカルの Unix syslog に送信する機能をサポートしています。

属性|概要
----|----
class logging.handlers.SysLogHandler(address=('localhost', SYSLOG_UDP_PORT), facility=LOG_USER, socktype=socket.SOCK_DGRAM)|遠隔の Unix マシンと通信するための、 SysLogHandler クラスの新たなインスタンスを返します。マシンのアドレスは (host, port) のタプル形式をとる address で与えられます。 address が指定されない場合、 ('localhost', 514) が使われます。アドレスは UDP ソケットを使って開かれます。 (host, port) のタプル形式の代わりに文字列で "/dev/log" のように与えることもできます。この場合、 Unix ドメインソケットが syslog にメッセージを送るのに使われます。 facility が指定されない場合、 LOG_USER が使われます。開かれるソケットの型は、 socktype 引数に依り、デフォルトは socket.SOCK_DGRAM で、UDP ソケットを開きます。 (rsyslog のような新しい syslog デーモンと使うために) TCP ソケットを開くには、 socket.SOCK_STREAM の値を指定してください。
close()|遠隔ホストへのソケットを閉じます。
emit(record)|レコードは書式化された後、 syslog サーバに送信されます。例外情報が存在しても、サーバには 送信されません 。
encodePriority(facility, priority)|ファシリティおよび優先度を整数に符号化します。値は文字列でも整数でも渡すことができます。文字列が渡された場合、内部の対応付け辞書が使われ、整数に変換されます。
mapPriority(levelname)|ログレベル名を syslog 優先度名に対応付けます。カスタムレベルを使用している場合や、デフォルトアルゴリズムがニーズに適していない場合には、このメソッドをオーバーライドする必要があるかもしれません。デフォルトアルゴリズムは、 DEBUG, INFO, WARNING, ERROR, CRITICAL を等価な syslog 名に、他のすべてのレベル名を "warning" に対応付けます。


> シンボリックな LOG_ 値は SysLogHandler で定義されています。これは sys/syslog.h ヘッダーファイルで定義された値を反映しています。

#### 優先度

名前 (文字列)|シンボル値
-------------|----------
alert|LOG_ALERT
crit or critical|LOG_CRIT
debug|LOG_DEBUG
emerg or panic|LOG_EMERG
err or error|LOG_ERR
info|LOG_INFO
notice|LOG_NOTICE
warn or warning|LOG_WARNING

#### ファシリティ

名前 (文字列)|シンボル値
-------------|----------
auth|LOG_AUTH
authpriv|LOG_AUTHPRIV
cron|LOG_CRON
daemon|LOG_DAEMON
ftp|LOG_FTP
kern|LOG_KERN
lpr|LOG_LPR
mail|LOG_MAIL
news|LOG_NEWS
syslog|LOG_SYSLOG
user|LOG_USER
uucp|LOG_UUCP
local0|LOG_LOCAL0
local1|LOG_LOCAL1
local2|LOG_LOCAL2
local3|LOG_LOCAL3
local4|LOG_LOCAL4
local5|LOG_LOCAL5
local6|LOG_LOCAL6
local7|LOG_LOCAL7

## [16.8.11. NTEventLogHandler](https://docs.python.jp/3/library/logging.handlers.html#nteventloghandler)

> logging.handlers モジュールに含まれる NTEventLogHandler クラスは、ログ記録メッセージをローカルな Windows NT, Windows 2000, または Windows XP のイベントログに送信する機能をサポートします。この機能を使えるようにするには、 Mark Hammond による Python 用 Win32 拡張パッケージをインストールする必要があります。

属性|概要
----|----
class logging.handlers.NTEventLogHandler(appname, dllname=None, logtype='Application')|NTEventLogHandler クラスの新たなインスタンスを返します。 appname はイベントログに表示する際のアプリケーション名を定義するために使われます。この名前を使って適切なレジストリエントリが生成されます。 dllname はログに保存するメッセージ定義の入った .dll または .exe ファイルへの完全修飾パス名を与えなければなりません (指定されない場合、 'win32service.pyd' が使われます - このライブラリは Win32 拡張とともにインストールされ、いくつかのプレースホルダとなるメッセージ定義を含んでいます)。これらのプレースホルダを利用すると、メッセージの発信源全体がログに記録されるため、イベントログは巨大になるので注意してください。 logtype は 'Application', 'System', 'Security' のいずれかで、デフォルトは 'Application' です。
close()|現時点では、イベントログエントリの発信源としてのアプリケーション名をレジストリから除去することはできます。しかしこれを行うと、イベントログビューアで意図した通りにログが見えなくなるでしょう - これはイベントログが .dll 名を取得するためにレジストリにアクセスできなければならないからです。現在のバージョンではこの操作を行いません。
emit(record)|メッセージ ID、イベントカテゴリ、イベント型を決定し、メッセージを NT イベントログに記録します。
getEventCategory(record)|レコードに対するイベントカテゴリを返します。自作のカテゴリを指定したい場合、このメソッドをオーバライドしてください。このクラスのバージョンのメソッドは 0 を返します。
getEventType(record)|レコードのイベント型を返します。自作の型を指定したい場合、このメソッドをオーバライドしてください。このクラスのバージョンのメソッドは、ハンドラの typemap 属性を使って対応付けを行います。この属性は __init__() で初期化され、 DEBUG, INFO, WARNING, ERROR, CRITICAL が入っています。自作のレベルを使っているのなら、このメソッドをオーバライドするか、ハンドラの typemap 属性に適切な辞書を配置する必要があるでしょう。
getMessageID(record)|レコードのメッセージ ID を返します。自作のメッセージを使っているのなら、ロガーに渡される msg を書式化文字列ではなく ID にします。その上で、辞書参照を行ってメッセージ ID を得ます。このクラスのバージョンでは 1 を返します。この値は win32service.pyd における基本メッセージ ID です。

## [16.8.12. SMTPHandler](https://docs.python.jp/3/library/logging.handlers.html#smtphandler)

> logging.handlers モジュールに含まれる SMTPHandler クラスは、 SMTP を介したログ記録メッセージの送信機能をサポートします。

属性|概要
----|----
class logging.handlers.SMTPHandler(mailhost, fromaddr, toaddrs, subject, credentials=None, secure=None, timeout=1.0)|新たな SMTPHandler クラスのインスタンスを返します。インスタンスは email の from および to アドレス行、および subject 行とともに初期化されます。 toaddrs は文字列からなるリストでなければなりません。非標準の SMTP ポートを指定するには、 mailhost 引数に (host, port) のタプル形式を指定します。文字列を使った場合、標準の SMTP ポートが使われます。もし SMTP サーバが認証を必要とするならば、 (username, password) のタプル形式を credentials 引数に指定することができます。
emit(record)|レコードを書式化し、指定されたアドレスに送信します。
getSubject(record)|レコードに応じたサブジェクト行を指定したいなら、このメソッドをオーバライドしてください。

## [16.8.13. MemoryHandler](https://docs.python.jp/3/library/logging.handlers.html#memoryhandler)

> logging.handlers モジュールに含まれる MemoryHandler は、ログ記録するレコードをメモリ上にバッファリングし、定期的にその内容をターゲット (target) となるハンドラにフラッシュする機能をサポートしています。フラッシュ処理はバッファが一杯になるか、ある深刻度かそれ以上のレベルを持つイベントが観測された際に行われます。

> MemoryHandler はより一般的な抽象クラス、 BufferingHandler のサブクラスです。この抽象クラスでは、ログ記録するレコードをメモリ上にバッファリングします。各レコードがバッファに追加される毎に、 shouldFlush() を呼び出してバッファをフラッシュすべきかどうか調べます。フラッシュする必要がある場合、 flush() がフラッシュ処理を行うものと想定されます。

属性|概要
----|----
class logging.handlers.BufferingHandler(capacity)|指定した許容量のバッファでハンドラを初期化します。
emit(record)|レコードをバッファに追加します。 shouldFlush() が true を返す場合、バッファを処理するために flush() を呼び出します。
flush()|このメソッドをオーバライドして、自作のフラッシュ動作を実装することができます。このクラスのバージョンのメソッドでは、単にバッファの内容を削除して空にします。
shouldFlush(record)|バッファが許容量に達している場合に true を返します。このメソッドは自作のフラッシュ処理方針を実装するためにオーバライドすることができます。
class logging.handlers.MemoryHandler(capacity, flushLevel=ERROR, target=None, flushOnClose=True)|Returns a new instance of the MemoryHandler class. The instance is initialized with a buffer size of capacity. If flushLevel is not specified, ERROR is used. If no target is specified, the target will need to be set using setTarget() before this handler does anything useful. If flushOnClose is specified as False, then the buffer is not flushed when the handler is closed. If not specified or specified as True, the previous behaviour of flushing the buffer will occur when the handler is closed.(MemoryHandlerクラスの新しいインスタンスを返します。 インスタンスは、容量のバッファサイズで初期化されます。 flushLevelが指定されていない場合、ERRORが使用されます。 ターゲットが指定されていない場合、このハンドラが有用な処理を行う前にターゲットをsetTarget（）を使用して設定する必要があります。 flushOnCloseがFalseに指定されている場合、ハンドラが閉じられるとバッファはフラッシュされません。 指定されていない場合、またはTrueとして指定されている場合、バッファをフラッシュする前の動作は、ハンドラが閉じられたときに発生します。)
close()|flush() を呼び出し、ターゲットを None に設定してバッファを消去します。
flush()|MemoryHandler の場合、フラッシュ処理は単に、バッファされたレコードをターゲットがあれば送信することを意味します。これと異なる動作を行いたい場合、オーバライドしてください。
setTarget(target)|ターゲットハンドラをこのハンドラに設定します。
shouldFlush(record)|バッファが一杯になっているか、 flushLevel またはそれ以上のレコードでないかを調べます。

## [16.8.14. HTTPHandler](https://docs.python.jp/3/library/logging.handlers.html#httphandler)

> logging.handlers モジュールに含まれる HTTPHandler クラスは、ログ記録メッセージを GET または POST セマンティクスを使って Web サーバに送信する機能をサポートしています。

属性|概要
----|----
class logging.handlers.HTTPHandler(host, url, method='GET', secure=False, credentials=None, context=None)|HTTPHandler クラスの新たなインスタンスを返します。特別なポートを使う必要がある場合、host は host:port の形式で使うことができます。 method が指定されない場合、 GET が使われます。 secure が真の場合、HTTPS 接続が使われます。 HTTPS 接続で使用する SSL 設定のために context 引数を ssl.SSLContext のインスタンスに設定することができます。 credentials を指定する場合、BASIC 認証の際の HTTP 'Authorization' ヘッダに使われるユーザIDとパスワードからなる 2要素タプルを渡してください。 credentials を指定する場合、ユーザIDとパスワードが通信中に平文として剥き出しにならないよう、secure=True も指定すべきです。
mapLogRecord(record)|URL エンコードされて Web サーバに送信することになる、 record に基づく辞書を供給します。デフォルトの実装では単に record.__dict__ を返します。例えば LogRecord のサブセットのみを Web サーバに送信する場合や、 サーバーに送信する内容を特別にカスタマイズする必要がある場合には、このメソッドをオーバライドできます。
emit(record)|レコードを URL エンコードされた辞書形式で Web サーバに送信します。レコードを送信のために辞書に変換するために mapLogRecord() が呼び出されます。

### 注釈

> Web server に送信するためのレコードを準備することは一般的な書式化操作とは同じではありませんので、 setFormatter() を使って Formatter を指定することは、 HTTPHandler には効果はありません。 format() を呼び出す代わりに、このハンドラは mapLogRecord() を呼び出し、その後その返却辞書を Web server に送信するのに適した様式にエンコードするために urllib.parse.urlencode() を呼び出します。

## [16.8.15. QueueHandler](https://docs.python.jp/3/library/logging.handlers.html#queuehandler)

> バージョン 3.2 で追加.

> logging.handlers モジュールに含まれる QueueHandler クラスは、 queue モジュールや multiprocessing のモジュールで実装されるようなキューにログメッセージを送信する機能をサポートしています。

> QueueListener クラスとともに QueueHandler を使うと、ロギングを行うスレッドから分離されたスレッド上でハンドラを動かすことができます。これは、クライアントに対してサービスするスレッドができるだけ速く応答する必要がある一方、別のスレッド上で (SMTPHandler によって電子メールを送信するような) 潜在的に遅い操作が行われるような、ウェブアプリケーションおよびその他のサービスアプリケーションにおいて重要です。

属性|概要
----|----
class logging.handlers.QueueHandler(queue)|QueueHandler クラスの新しいインスタンスを返します。インスタンスは、キューにメッセージを送るように初期化されます。キューは任意のキューのようなオブジェクトが可能です; それはそのまま enqueue() メソッドによって使用されます。そのメソッドはメッセージを送る方法を知っている必要があります。
emit(record)|準備した LogRecord の結果をキューに追加します。
prepare(record)|キューに追加するためレコードを準備します。このメソッドが返したオブジェクトがキューに追加されます。
enqueue(record)|キューにレコードを put_nowait() を使ってエンキューします; ブロッキングやタイムアウト、あるいはなにか特別なキューの実装を使いたければ、これをオーバライドしてみてください。

## [16.8.16. QueueListener](https://docs.python.jp/3/library/logging.handlers.html#queuelistener)

> バージョン 3.2 で追加.

> logging.handlers モジュールに含まれる QueueListener クラスは、 queue モジュールや multiprocessing のモジュールで実装されるようなキューからログメッセージを受信する機能をサポートしています。メッセージは内部スレッドのキューから受信され、同じスレッド上の複数のハンドラに渡されて処理されます。 QueueListener それ自体はハンドラではありませんが、 QueueHandler と連携して動作するのでここで文書化されています。

> QueueHandler クラスとともに QueueListener を使うと、ロギングを行うスレッドから分離されたスレッド上でハンドラを動かすことができます。これは、クライアントに対してサービスするスレッドができるだけ速く応答する必要がある一方、別のスレッド上で (SMTPHandler によって電子メールを送信するような) 潜在的に遅い操作が行われるような、ウェブアプリケーションおよびその他のサービスアプリケーションにおいて重要です。

属性|概要
----|----
class logging.handlers.QueueListener(queue, *handlers, respect_handler_level=False)|QueueListener クラスの新しいインスタンスを返します。インスタンスは、メッセージの送信先キューと、キュー上に配置されたエントリーを扱うハンドラのリストとともに初期化されます。キューには、任意のキューのようなオブジェクトを使用できます。キューのようなオブジェクトは、そのまま dequeue() メソッドに渡されます。そのメソッドはメッセージをキューから取得する方法を知っている必要があります。 respect_handler_level が True の場合、メッセージをそのハンドラーに渡すかどうかを判断する際、(メッセージに対するレベルと比較して)ハンドラのレベルは尊重されます。False の場合、以前の Python のバージョンと同様に動作し、各メッセージを各ハンドラに常に渡します。
dequeue(block)|キューからレコードを取り除き、それを返します。ブロッキングすることがあります。
prepare(record)|レコードを扱うための準備をします。
handle(record)|レコードを処理します。
start()|リスナーを開始します。
stop()|リスナーを停止します。
enqueue_sentinel()|リスナーに停止するように指示するためキューに番兵を書き込みます。この実装は put_nowait() を使用します。タイムアウトを有効にしたい場合や、カスタムのキュー実装を使いたい場合は、このメソッドをオーバーライドすると良いでしょう。

### 参考

モジュール|説明
----------|----
[logging](https://docs.python.jp/3/library/logging.html#module-logging)|logging モジュールの API リファレンス。
[logging.config](https://docs.python.jp/3/library/logging.config.html#module-logging.config)|logging モジュールの環境設定 API です。

