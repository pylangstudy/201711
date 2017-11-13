# [16.1. os — 雑多なオペレーティングシステムインタフェース](https://docs.python.jp/3/library/os.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/secrets.py](https://github.com/python/cpython/tree/3.6/Lib/secrets.py)

## [16.1.5.1. Linux 拡張属性](https://docs.python.jp/3/library/os.html#linux-extended-attributes)

> バージョン 3.3 で追加.

> 以下の関数はすべて Linux でのみ使用可能です。

属性|概要
----|----
os.getxattr(path, attribute, *, follow_symlinks=True)|Return the value of the extended filesystem attribute attribute for path. attribute can be bytes or str (directly or indirectly through the PathLike interface). If it is str, it is encoded with the filesystem encoding.(pathの拡張ファイルシステム属性属性の値を返します。 属性はバイトまたはstr（PathLikeインターフェイスを介して直接的または間接的に）です。 strの場合、ファイルシステムのエンコーディングでエンコードされます。)
os.listxattr(path=None, *, follow_symlinks=True)|path の拡張ファイルシステム属性のリストを返します。リスト内の属性はファイルシステムのエンコーディングでデコードされた文字列で表されます。path が None の場合、listxattr() はカレントディレクトリを調べます。
os.removexattr(path, attribute, *, follow_symlinks=True)|Removes the extended filesystem attribute attribute from path. attribute should be bytes or str (directly or indirectly through the PathLike interface). If it is a string, it is encoded with the filesystem encoding.(pathから拡張ファイルシステム属性属性を削除します。 属性はバイトまたはstr（PathLikeインターフェイスを介して直接的または間接的に）でなければなりません。 文字列の場合は、ファイルシステムのエンコーディングでエンコードされます。)
os.setxattr(path, attribute, value, flags=0, *, follow_symlinks=True)|Set the extended filesystem attribute attribute on path to value. attribute must be a bytes or str with no embedded NULs (directly or indirectly through the PathLike interface). If it is a str, it is encoded with the filesystem encoding. flags may be XATTR_REPLACE or XATTR_CREATE. If XATTR_REPLACE is given and the attribute does not exist, EEXISTS will be raised. If XATTR_CREATE is given and the attribute already exists, the attribute will not be created and ENODATA will be raised.(pathの拡張ファイルシステム属性属性をvalueに設定します。 属性は、（PathLikeインタフェースを介して直接的または間接的に）埋め込まれたNULのないバイトまたはstrでなければなりません。 それがstrの場合、ファイルシステムのエンコーディングでエンコードされます。 フラグはXATTR_REPLACEまたはXATTR_CREATEです。 XATTR_REPLACEが指定され、その属性が存在しない場合、EEXISTSが生成されます。 XATTR_CREATEが指定され、属性がすでに存在する場合、属性は作成されず、ENODATAが生成されます。)
os.XATTR_SIZE_MAX|拡張属性の値にできる最大サイズです。現在、Linux では 64 キロバイトです。
os.XATTR_CREATE|setxattr() の引数 flags に指定できる値です。その操作で属性を作成しなければならないことを意味します。
os.XATTR_REPLACE|setxattr() の引数 flags に指定できる値です。その操作で既存の属性を置き換えなければならないことを意味します。

## [16.1.6. プロセス管理](https://docs.python.jp/3/library/os.html#process-management)

> 以下の関数はプロセスの生成や管理に利用できます。

> さまざまな exec* 関数は、プロセス内にロードされる新しいプログラムに与えるための、引数のリストを取ります。どの関数の場合でも、新しいプログラムに渡されるリストの最初の引数は、ユーザがコマンドラインで入力する引数ではなく、そのプログラム自体の名前です。 C プログラマならば、プログラムの main() に渡される argv[0] だと考えれば良いでしょう。たとえば、 os.execv('/bin/echo', ['foo', 'bar']) が標準出力に出力するのは bar だけで、 foo は無視されたかのように見えることになります。

属性|概要
----|----
os.abort()|SIGABRT シグナルを現在のプロセスに対して生成します。 Unix では、デフォルトの動作はコアダンプの生成です ; Windows では、プロセスは即座に終了コード 3 を返します。この関数の呼び出しは signal.signal() を使って SIGABRT に対し登録された Python シグナルハンドラーを呼び出さないことに注意してください。
os.execl(path, arg0, arg1, ...), os.execle(path, arg0, arg1, ..., env), os.execlp(file, arg0, arg1, ...), os.execlpe(file, arg0, arg1, ..., env), os.execv(path, args), os.execve(path, args, env), os.execvp(file, args), os.execvpe(file, args, env)|これらの関数はすべて、現在のプロセスを置き換える形で新たなプログラムを実行します ; 現在のプロセスは返り値を返しません。 Unix では、新たに実行される実行コードは現在のプロセス内に読み込まれ、呼び出し側と同じプロセス ID を持つことになります。エラーは OSError 例外として報告されます。
os.EX_OK|エラーが起きなかったことを表す終了コード。
os.EX_USAGE|誤った個数の引数が渡された時など、コマンドが間違って使われたことを表す終了コード。
os.EX_DATAERR|入力データが誤っていたことを表す終了コード。
os.EX_NOINPUT|入力ファイルが存在しなかった、または、読み込み不可だったことを表す終了コード。
os.EX_NOUSER|指定されたユーザーが存在しなかったことを表す終了コード。
os.EX_NOHOST|指定されたホストが存在しなかったことを表す終了コード。
os.EX_UNAVAILABLE|要求されたサービスが利用できないことを表す終了コード。
os.EX_SOFTWARE|内部ソフトウェアエラーが検出されたことを表す終了コード。
os.EX_OSERR|fork できない、 pipe の作成ができないなど、オペレーティングシステムのエラーが検出されたことを表す終了コード。
os.EX_OSFILE|システムファイルが存在しなかった、開けなかった、あるいはその他のエラーが起きたことを表す終了コード。
os.EX_CANTCREAT|ユーザーには作成できない出力ファイルを指定したことを表す終了コード。
os.EX_IOERR|ファイルの I/O を行っている途中にエラーが発生した時の終了コード。
os.EX_TEMPFAIL|一時的な失敗が発生したことを表す終了コード。これは、再試行可能な操作の途中に、ネットワークに接続できないというような、実際にはエラーではないかも知れないことを意味します。
os.EX_PROTOCOL|プロトコル交換が不正、不適切、または理解不能なことを表す終了コード。
os.EX_NOPERM|操作を行うために十分な許可がなかった（ファイルシステムの問題を除く）ことを表す終了コード。
os.EX_CONFIG|設定エラーが起こったことを表す終了コード。
os.EX_NOTFOUND|"an entry was not found" のようなことを表す終了コード。
os.fork()|子プロセスを fork します。子プロセスでは 0 が返り、親プロセスでは子プロセスの id が返ります。エラーが発生した場合は、 OSError を送出します。
os.forkpty()|子プロセスを fork します。この時新しい擬似端末を子プロセスの制御端末として使います。親プロセスでは (pid, fd) からなるペアが返り、 fd は擬似端末のマスター側のファイル記述子となります。可搬性のあるアプローチを取るには、 pty モジュールを利用してください。エラーが発生した場合は、 OSError を送出します。
os.kill(pid, sig)|プロセス pid にシグナル sig を送ります。ホストプラットフォームで利用可能なシグナルを特定する定数は signal モジュールで定義されています。
os.nice(increment)|プロセスの "nice 値 " に increment を加えます。新たな nice 値を返します。
os.plock(op)|プログラムのセグメントをメモリ内にロックします。 op (<sys/lock.h> で定義されています ) にはどのセグメントをロックするかを指定します。
os.popen(cmd, mode='r', buffering=-1)|コマンド cmd への、または cmd からのパイプ入出力を開きます。戻り値はパイプに接続されている開かれたファイルオブジェクトで、 mode が 'r' (デフォルト) または 'w' かによって読み出しまたは書き込みを行うことができます。引数 bufsize は、組み込み関数 open() における対応する引数と同じ意味を持ちます。 返されるファイルオブジェクトは、バイトではなくテキスト文字列を読み書きします。
os.spawnl(mode, path, ...), os.spawnle(mode, path, ..., env), os.spawnlp(mode, file, ...), os.spawnlpe(mode, file, ..., env), os.spawnv(mode, path, args), os.spawnve(mode, path, args, env), os.spawnvp(mode, file, args), os.spawnvpe(mode, file, args, env)|新たなプロセス内でプログラム path を実行します。
os.P_NOWAIT, os.P_NOWAITO|spawn* 関数ファミリに対する mode パラメタとして取れる値です。この値のいずれかを mode として与えた場合、 spawn*() 関数は新たなプロセスが生成されるとすぐに、プロセスの ID を戻り値として返ります。
os.P_WAIT|spawn* 関数ファミリに対する mode パラメタとして取れる値です。この値を mode として与えた場合、 spawn*() 関数は新たなプロセスを起動して完了するまで返らず、プロセスがうまく終了した場合には終了コードを、シグナルによってプロセスが kill された場合には -signal を返します。
os.P_DETACH, os.P_OVERLAY|spawn* 関数ファミリに対する mode パラメタとして取れる値です。これらの値は上の値よりもやや可搬性において劣っています。 P_DETACH は P_NOWAIT に似ていますが、新たなプロセスは呼び出しプロセスのコンソールから切り離され (detach) ます。 P_OVERLAY が使われた場合、現在のプロセスは置き換えられます。したがって spawn* は返りません。
os.startfile(path[, operation])|ファイルを関連付けられたアプリケーションを使ってスタートします。
os.system(command)|サブシェル内でコマンド (文字列) を実行します。この関数は標準 C 関数 system() を使って実装されており、system() と同じ制限があります。sys.stdin などに対する変更を行っても、実行されるコマンドの環境には反映されません。command が何らかの出力を生成した場合、インタープリターの標準出力ストリームに送られます。
os.times()|現在の全体的なプロセス時間を返します。返り値は 5 個の属性を持つオブジェクトになります:
os.wait()|子プロセスの実行完了を待機し、子プロセスの pid と終了コードインジケーター — 16 ビットの数値で、下位バイトがプロセスを kill したシグナル番号、上位バイトが終了ステータス ( シグナル番号がゼロの場合 ) — の入ったタプルを返します ; コアダンプファイルが生成された場合、下位バイトの最上桁ビットが立てられます。
os.waitid(idtype, id, options)|一つ以上のプロセスの完了を待機します。idtype には P_PID、P_PGID、または P_ALL を指定できます。id は待機する pid を指定します。options は WEXITED、WSTOPPED、または WCONTINUED を一つ以上、論理和で指定でき、他に WNOHANG または WNOWAIT も追加できます。返り値は siginfo_t 構造体に含まれるデータ (si_pid、si_uid、si_signo、si_status、および si_code) を表すオブジェクトになります。WNOHANG が指定され、待機状態の子プロセスがない場合は None を返します。
os.P_PID, os.P_PGID, os.P_ALL|waitid() の idtype に指定できる値です。これらは id がどう解釈されるかに影響します。
os.WEXITED, os.WSTOPPED, os.WNOWAIT|waitid() の options で使用できるフラグです。子プロセスのどのシグナルを待機するかを指定します。
os.waitpid(pid, options)|この関数の詳細は Unix と Windows で異なります。
os.wait3(options)|waitpid() に似ていますが、プロセス id を引数に取らず、子プロセス id 、終了ステータスインジケータ、リソース使用情報の 3 要素からなるタプルを返します。リソース使用情報の詳しい情報は resource. getrusage() を参照してください。 オプション引数は waitpid() および wait4() と同じです。
os.wait4(pid, options)|waitpid() に似ていますが、子プロセス id 、終了ステータスインジケータ、リソース使用情報の 3 要素からなるタプルを返します。リソース使用情報の詳しい情報は resource. getrusage() を参照してください。 wait4() の引数は waitpid() に与えられるものと同じです。
os.WNOHANG|子プロセス状態がすぐに取得できなかった場合に直ちに終了するようにするための waitpid() のオプションです。この場合、関数は (0, 0) を返します。
os.WCONTINUED|このオプションによって子プロセスは前回状態が報告された後にジョブ制御による停止状態から実行を再開された場合に報告されるようになります。
os.WUNTRACED|このオプションによって子プロセスは停止されていながら停止されてから状態が報告されていない場合に報告されるようになります。
os.WCOREDUMP(status)|プロセスに対してコアダンプが生成されていた場合には True を、それ以外の場合は False を返します。
os.WIFCONTINUED(status)|プロセスがジョブ制御による停止状態から実行を再開された (continue) 場合に True を、それ以外の場合は False を返します。
os.WIFSTOPPED(status)|プロセスが停止された (stop) 場合に True を、それ以外の場合は False を返します。
os.WIFSIGNALED(status)|プロセスがシグナルによって終了した (exit) 場合に True を、それ以外の場合は False を返します。
os.WIFEXITED(status)|プロセスが exit(2) システムコールで終了した場合に True を、それ以外の場合は False を返します。
os.WEXITSTATUS(status)|WIFEXITED(status) が真の場合、 exit(2) システムコールに渡された整数の引数を返します。そうでない場合、返り値に意味はありません。
os.WSTOPSIG(status)|プロセスを停止させたシグナル番号を返します。
os.WTERMSIG(status)|プロセスを終了させたシグナル番号を返します。

