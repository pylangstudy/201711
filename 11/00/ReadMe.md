# [16.1. os — 雑多なオペレーティングシステムインタフェース](https://docs.python.jp/3/library/os.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/secrets.py](https://github.com/python/cpython/tree/3.6/Lib/secrets.py)

## [16.1.3. ファイルオブジェクトの生成](https://docs.python.jp/3/library/os.html#file-object-creation)

> 以下の関数は新しい ファイルオブジェクト を作成します。(open() も参照してください)

属性|概要
----|----
os.fdopen(fd, *args, **kwargs)|ファイル記述子 fd に接続し、オープンしたファイルオブジェクトを返します。これは組み込み関数 open() の別名であり、同じ引数を受け取ります。唯一の違いは fdopen() の第一引数が常に整数でなければならないことです。

## [16.1.4. ファイル記述子の操作](https://docs.python.jp/3/library/os.html#file-descriptor-operations)

> これらの関数は、ファイル記述子を使って参照されている I/O ストリームを操作します。

> ファイル記述子とは現在のプロセスで開かれたファイルに対応する小さな整数です。例えば、標準入力のファイル記述子は通常 0 で、標準出力は 1 、標準エラーは 2 です。プロセスから開かれたその他のファイルには 3 、 4 、 5 と割り振られていきます。「ファイル記述子」という名称は少し誤解を与えるものかもしれません。Unix プラットフォームでは、ソケットやパイプもファイル記述子によって参照されます。

> fileno() メソッドを使用して、必要な場合に file object に関連付けられているファイル記述子を取得することができます。ファイル記述子を直接使用すると、ファイルオブジェクトのメソッドが使用されないため、データの内部バッファなどの性質は無視されることに注意してください。

属性|概要
----|----
os.close(fd)|ファイル記述子 fd をクローズします。
os.closerange(fd_low, fd_high)|fd_low 以上 fd_high 未満のすべてのファイル記述子をエラーを無視してクローズします。
os.device_encoding(fd)|fd に関連付けられたデバイスが端末 (ターミナル) に接続されている場合に、そのデバイスのエンコーディングを表す文字列を返します。端末に接続されていない場合、 None を返します。
os.dup(fd)|ファイル記述子 fd の複製を返します。新しいファイル記述子は 継承不可 です。
os.dup2(fd, fd2, inheritable=True)|ファイル記述子 fd を fd2 に複製し、必要な場合には後者を先に閉じます。 fd2 はデフォルトでは 継承可能 で、inheritable が False の場合は継承不可です。
os.fchmod(fd, mode)|fd で指定されたファイルのモードを mode に変更します。mode に指定できる値については、chmod() のドキュメントを参照してください。Python 3.3 以降では os.chmod(fd, mode) と等価です。
os.fchown(fd, uid, gid)|fd で指定されたファイルの所有者 id およびグループ id を数値 uid および gid に変更します。いずれかの id を変更せずにおくにはその値として -1 を指定します。chown() を参照してください。Python 3.3 以降では os.chown(fd, uid, gid) と等価です。
os.fdatasync(fd)|ファイル記述子 fd を持つファイルのディスクへの書き込みを強制します。メタデータの更新は強制しません。
os.fpathconf(fd, name)|開いているファイルに関連するシステム設定情報を返します。 name は取得する設定名を指定します。これは、いくつかの標準 (POSIX.1 、 Unix 95 、 Unix 98 その他 ) で定義された定義済みのシステム値名の文字列である場合があります。プラットフォームによっては別の名前も定義されています。ホストオペレーティングシステムの関知する名前は pathconf_names 辞書で与えられています。このマップ型オブジェクトに含まれていない構成変数については、 name に整数を渡してもかまいません。
os.fstat(fd)|ファイル記述子 fd の状態を取得します。stat_result オブジェクトを返します。
os.fstatvfs(fd)|statvfs() と同様に、ファイル記述子 fd に関連付けられたファイルが格納されているファイルシステムに関する情報を返します。Python 3.3 以降では os.statvfs(fd) と等価です。
os.fsync(fd)|ファイル記述子 fd を持つファイルのディスクへの書き込みを強制します。 Unix では、ネイティブの fsync() 関数を、 Windows では _commit() 関数を呼び出します。
os.ftruncate(fd, length)|ファイル記述子 fd に対応するファイルを、サイズが最長で length バイトになるように切り詰めます。Python 3.3 以降では os.truncate(fd, length) と等価です。
os.get_blocking(fd)|記述子のブロッキングモードを取得します。 O_NONBLOCK フラグが設定されている場合は False で、フラグがクリアされている場合は True です。
os.isatty(fd)|ファイル記述子 fd がオープンされていて、 tty (のような) デバイスに接続されている場合、 True を返します。そうでない場合は False を返します。
os.lockf(fd, cmd, len)|オープンされたファイル記述子に対して、POSIX ロックの適用、テスト、解除を行います。fd はオープンされたファイル記述子です。cmd には使用するコマンド (F_LOCK、F_TLOCK、F_ULOCK、あるいは F_TEST のいずれか一つ) を指定します。len にはロックするファイルのセクションを指定します。
os.F_LOCK, os.F_TLOCK, os.F_ULOCK, os.F_TEST|lockf() がとる動作を指定するフラグです。
os.lseek(fd, pos, how)|ファイル記述子 fd の現在の位置を pos に設定します。 pos の意味は how で次のように修飾されます。ファイルの先頭からの相対位置には SEEK_SET か 0 を、現在の位置からの相対位置には SEEK_CUR か 1 を、ファイルの末尾からの相対位置には SEEK_END か 2 を設定します。戻り値は、新しいカーソル位置のファイルの先頭からのバイト数です。
os.SEEK_SET, os.SEEK_CUR, os.SEEK_END|lseek() 関数に渡すパラメーター。値は順に 0, 1, 2 です。
os.open(path, flags, mode=0o777, *, dir_fd=None)|ファイル path を開き、flag に従って様々なフラグを設定し、可能なら mode に従ってファイルモードを設定します。mode を計算する際、まず現在の umask 値でマスクされます。新たに開いたファイルのファイル記述子を返します。新しいファイル記述子は 継承不可 です。

> 以下の定数は open() 関数の flags 引数に利用します。これらの定数は、ビット単位に OR 演算子 | で組み合わせることができます。一部、すべてのプラットフォームでは使用できない定数があります。利用可能かどうかや使い方については、Unix では open(2)、Windows では MSDN を参照してください。

属性|概要
----|----
os.O_RDONLY, os.O_WRONLY, os.O_RDWR, os.O_APPEND, os.O_CREAT, os.O_EXCL, os.O_TRUNC|上記の定数は Unix および Windows で利用可能です。
os.O_DSYNC, os.O_RSYNC, os.O_SYNC, os.O_NDELAY, os.O_NONBLOCK, os.O_NOCTTY, os.O_CLOEXEC|上記の定数は Unix でのみ利用可能です。
os.O_BINARY, os.O_NOINHERIT, os.O_SHORT_LIVED, os.O_TEMPORARY, os.O_RANDOM, os.O_SEQUENTIAL, os.O_TEXT|上記の定数は Windows でのみ利用可能です。
os.openpty()|新しい擬似端末のペアを開きます。pty および tty を表すファイル記述子のペア (master, slave) を返します。新しいファイル記述子は 継承不可 です。(若干) 可搬性の高いアプローチには pty を使用してください。
os.pipe()|パイプを作成します。読み込み、書き込みに使うことの出来るファイル記述子のペア (r, w) を返します。新しいファイル記述子は 継承不可 です。
os.pipe2(flags)|flags を設定したパイプをアトミックに作成します。flags には値 O_NONBLOCK と O_CLOEXEC を一つ以上論理和指定できます。読み込み、書き込みに使うことの出来るファイル記述子のペア (r, w) を返します。
os.posix_fallocate(fd, offset, len)|fd で指定されたファイルに対し、開始位置 offset から len バイト分割り当てるに十分なディスクスペースを確保します。
os.posix_fadvise(fd, offset, len, advice)|データへアクセスする意思を、パターンを指定して宣言します。これによりカーネルが最適化を行えるようになります。advice は fd で指定されたファイルに対し、開始位置 offset から len バイト分の領域に適用されます。advice には POSIX_FADV_NORMAL、POSIX_FADV_SEQUENTIAL、POSIX_FADV_RANDOM、POSIX_FADV_NOREUSE、POSIX_FADV_WILLNEED、または POSIX_FADV_DONTNEED のいずれか一つを指定します。
os.POSIX_FADV_NORMAL, os.POSIX_FADV_SEQUENTIAL, os.POSIX_FADV_RANDOM, os.POSIX_FADV_NOREUSE, os.POSIX_FADV_WILLNEED, os.POSIX_FADV_DONTNEED|posix_fadvise() において、使われるであろうアクセスパターンを指定する advice に使用できるフラグです。
os.pread(fd, buffersize, offset)|ファイル記述子 fd に対し、位置 offset から読み込みます。読み込み量は最大で buffersize バイトです。ファイルオフセットは変化しません。
os.pwrite(fd, str, offset)|ファイル記述子 fd に対し、位置 offset から bytestring を書き出します。ファイルオフセットは変化しません。
os.read(fd, n)|ファイル記述子 fd から最大で n バイト読み込みます。読み込んだバイト分のバイト列を返します。fd が参照しているファイルの終端に達した場合、空のバイト列が返されます。
os.set_blocking(fd, blocking)|指定されたファイル記述子のブロッキングモードを設定します。 ブロッキングが False の場合 O_NONBLOCK フラグを設定し、そうでない場合はクリアします。
os.SF_NODISKIO, os.SF_MNOWAIT, os.SF_SYNC|実装がサポートしている場合 sendfile() 関数に渡すパラメーターです。
os.readv(fd, buffers)|ファイル記述子 fd から、いくつかのミュータブルな バイトライクオブジェクト buffers に読み込みます。 readv() は、各バッファーにいっぱいになるまでデータを転送したのちシーケンス内の次のバッファーに移動し、データの残りを転送します。 readv() は、読み込んだ合計バイト数 (すべてのオブジェクトの合計容量より小さい場合があります) を返します。
os.tcgetpgrp(fd)|fd (os.open() が返すオープンしたファイル記述子 ) で与えられる端末に関連付けられたプロセスグループを返します。
os.tcsetpgrp(fd, pg)|fd (os.open() が返すオープンしたファイル記述子 ) で与えられる端末に関連付けられたプロセスグループを pg に設定します。
os.ttyname(fd)|ファイル記述子 fd に関連付けられている端末デバイスを特定する文字列を返します。 fd が端末に関連付けられていない場合、例外が送出されます。
os.write(fd, str)|str のバイト列をファイル記述子 fd に書き出します。実際に書き出されたバイト数が返されます。
os.writev(fd, buffers)|buffers の内容をファイル記述子 fd へ書き出します。 buffers は bytes-like オブジェクト のシーケンスでなければなりません。バッファは配列の順番で処理されます。最初のバッファの内容全体は 2 番目のバッファに進む前に書き込まれ、その次も同様です。オペレーティングシステムは使われるバッファの数を制限するかもしれません (sysconf() 値の SC_IOV_MAX) 。

低レベルAPI。ここまで低レベルなのは利用頻度が低いと思われる。`os.pread`, `os.pwrite`のファイルへのランダムアクセスは使えるかも知れない。しかし、普通はもっと上級のAPIを使う。たとえばデータベース用API(sqlite3)や、固有ファイル形式用API(png, midi)を使うだろう。独自の仕様を作り、専用の入出力APIを作るときでもないかぎり、ランダムアクセスAPIを使う機会はないと思われる。

本章の`os.open`メソッドを使っても`FileNotFoundError`エラーでファイルを開けなかったので、本章はスルー。

普通にファイル操作したいなら、組み込み関数`open()`を使えばいい。

