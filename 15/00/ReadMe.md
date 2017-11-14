# [16.1. os — 雑多なオペレーティングシステムインタフェース](https://docs.python.jp/3/library/os.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/secrets.py](https://github.com/python/cpython/tree/3.6/Lib/secrets.py)

## [16.1.7. スケジューラーへのインターフェイス](https://docs.python.jp/3/library/os.html#interface-to-the-scheduler)

> 以下の関数は、オペレーティングシステムがプロセスに CPU 時間を割り当てる方法を制御します。これらは一部の Unix プラットフォームでのみ利用可能です。詳しくは Unix マニュアルページを参照してください。

> バージョン 3.3 で追加.

> 次のスケジューリングポリシーは、オペレーティングシステムでサポートされていれば公開されます。

属性|概要
----|----
os.SCHED_OTHER|デフォルトのスケジューリングポリシーです。
os.SCHED_BATCH|常にCPUに負荷のかかる (CPU-intensive) プロセス用のポリシーです。他の対話式プロセスなどの応答性を維持するよう試みます。
os.SCHED_IDLE|非常に優先度の低いバックグラウンドタスク用のスケジューリングポリシーです。
os.SCHED_SPORADIC|散発的なサーバープログラム用のスケジューリングポリシーです。
os.SCHED_FIFO|FIFO (First In, First Out) 型のスケジューリングポリシーです。
os.SCHED_RR|ラウンドロビン型のスケジューリングポリシーです。
os.SCHED_RESET_ON_FORK|このフラグは他のスケジューリングポリシーとともに論理和指定できます。このフラグが与えられたプロセスが fork されると、その子プロセスのスケジューリングポリシーおよび優先度はデフォルトにリセットされます。
class os.sched_param(sched_priority)|このクラスは、sched_setparam()、sched_setscheduler()、および sched_getparam() で使用される、調節可能なスケジューリングパラメーターを表します。これはイミュータブルです。
sched_priority|スケジューリングポリシーのスケジューリング優先度です。
os.sched_get_priority_min(policy)|policy の最小優先度値を取得します。policy には上記のスケジューリングポリシー定数の一つを指定します。
os.sched_get_priority_max(policy)|policy の最大優先度値を取得します。policy には上記のスケジューリングポリシー定数の一つを指定します。
os.sched_setscheduler(pid, policy, param)|PID pid のプロセスのスケジューリングポリシーを設定します。pid が 0 の場合、呼び出しプロセスを意味します。policy には上記のスケジューリングポリシー定数の一つを指定します。param は sched_param のインスタンスです。
os.sched_getscheduler(pid)|PID pid のプロセスのスケジューリングポリシーを返します。pid が 0 の場合、呼び出しプロセスを意味します。返り値は上記のスケジューリングポリシー定数の一つになります。
os.sched_setparam(pid, param)|PID pid のプロセスのスケジュールパラメーターを設定します。pid が 0 の場合、呼び出しプロセスを意味します。param は sched_param のインスタンスです。
os.sched_getparam(pid)|PID pid のプロセスのスケジューリングパラメーターを sched_param のインスタンスとして返します。pid が 0 の場合、呼び出しプロセスを意味します。
os.sched_rr_get_interval(pid)|PID pid のプロセスのラウンドロビンクォンタム (秒) を返します。pid が 0 の場合、呼び出しプロセスを意味します。
os.sched_yield()|自発的に CPU を解放します。
os.sched_setaffinity(pid, mask)|PID pid のプロセス (0 であれば現在のプロセス) を CPU の集合に制限します。mask はプロセスを制限する CPU の集合を表す整数のイテラブルなオブジェクトです。
os.sched_getaffinity(pid)|PID pid のプロセス (0 の場合、現在のプロセス) が制限されている CPU の集合を返します。

## [16.1.8. 雑多なシステム情報](https://docs.python.jp/3/library/os.html#miscellaneous-system-information)

属性|概要
----|----
os.confstr(name)|システム設定値を文字列で返します。 name には取得したい設定名を指定します ; この値は定義済みのシステム値名を表す文字列にすることができます ; 名前は多くの標準 (POSIX.1 、 Unix 95 、 Unix 98 その他 ) で定義されています。ホストオペレーティングシステムの関知する名前は confstr_names 辞書のキーとして与えられています。このマップ型オブジェクトに入っていない設定変数については、 name に整数を渡してもかまいません。
os.confstr_names|confstr() が受理する名前を、ホストオペレーティングシステムで定義されている整数値に対応付けている辞書です。この辞書はシステムでどの設定名が定義されているかを決定するために利用できます。
os.cpu_count()|システムの CPU 数を返します。未定の場合は None を返します。
os.getloadavg()|過去 1 分、 5 分、および 15 分間の、システムの実行キューの平均プロセス数を返します。平均負荷が得られない場合には OSError を送出します。
os.sysconf(name)|整数値のシステム設定値を返します。 name で指定された設定値が定義されていない場合、 -1 が返されます。 name に関するコメントとしては、 confstr() で述べた内容が同様に当てはまります ; 既知の設定名についての情報を与える辞書は sysconf_names で与えられています。
os.sysconf_names|sysconf() が受理する名前を、ホストオペレーティングシステムで定義されている整数値に対応付けている辞書です。この辞書はシステムでどの設定名が定義されているかを決定するために利用できます。

> 以下のデータ値はパス名編集操作をサポートするために利用されます。これらの値はすべてのプラットフォームで定義されています。

> パス名に対する高水準の操作は os.path モジュールで定義されています。

属性|概要
----|----
os.curdir|現在のディレクトリ参照するためにオペレーティングシステムで使われる文字列定数です。 POSIX と Windows では '.' になります。 os.path からも利用できます。
os.pardir|親ディレクトリを参照するためにオペレーティングシステムで使われる文字列定数です。 POSIX と Windows では '..' になります。 os.path からも利用できます。
os.sep|パス名を要素に分割するためにオペレーティングシステムで利用されている文字です。例えば POSIX では '/' で、 Windows では '\\' です。しかし、このことを知っているだけではパス名を解析したり、パス名同士を結合したりするには不十分です — こうした操作には os.path.split() や os.path.join() を使用してください — が、たまに便利なこともあります。 os.path からも利用できます。
os.altsep|文字パス名を要素に分割する際にオペレーティングシステムで利用されるもう一つの文字で、分割文字が一つしかない場合には None になります。この値は sep がバックスラッシュとなっている DOS や Windows システムでは '/' に設定されています。 os.path からも利用できます。
os.extsep|ベースのファイル名と拡張子を分ける文字です。例えば、 os.py であれば '.' です。 os.path からも利用できます。
os.pathsep|(PATH のような ) サーチパス内の要素を分割するためにオペレーティングシステムが慣習的に用いる文字で、 POSIX における ':' や DOS および Windows における ';' に相当します。 os.path からも利用できます。
os.defpath|exec*p* や spawn*p* において、環境変数辞書内に 'PATH' キーがない場合に使われる標準設定のサーチパスです。 os.path からも利用できます。
os.linesep|現在のプラットフォーム上で行を分割 ( あるいは終端 ) するために用いられている文字列です。この値は例えば POSIX での '\n' や Mac OS での '\r' のように、単一の文字にもなりますし、例えば Windows での '\r\n' のように複数の文字列にもなります。テキストモードで開いたファイルに書き込む時には、 os.linesep を利用しないでください。すべてのプラットフォームで、単一の '\n' を使用してください。
os.devnull|ヌルデバイスのファイルパスです。例えば POSIX では '/dev/null' で、 Windows では 'nul' です。この値は os.path からも利用できます。
os.RTLD_LAZY, os.RTLD_NOW, os.RTLD_GLOBAL, os.RTLD_LOCAL, os.RTLD_NODELETE, os.RTLD_NOLOAD, os.RTLD_DEEPBIND|setdlopenflags() 関数と getdlopenflags() 関数と一緒に使用するフラグ。それぞれのフラグの意味については、Unix マニュアルの dlopen(3) ページを参照してください。

