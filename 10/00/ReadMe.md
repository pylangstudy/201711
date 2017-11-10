# [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html)

< [15. 暗号関連のサービス](https://docs.python.jp/3/library/crypto.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/secrets.py](https://github.com/python/cpython/tree/3.6/Lib/secrets.py)

> このモジュールは、 OS 依存の機能を利用するポータブルな方法を提供します。単純なファイルの読み書きについては、 open() を参照してください。パス操作については、 os.path モジュールを参照してください。コマンドラインに与えられたすべてのファイルから行を読み込んでいくには、 fileinput モジュールを参照してください。一時ファイルや一時ディレクトリの作成については、 tempfile モジュールを参照してください。高水準のファイルとディレクトリの操作については、 shutil モジュールを参照してください。

### 利用可能性に関する注意

* Python の、すべての OS 依存モジュールの設計方針は、可能な限り同一のインタフェースで同一の機能を利用できるようにする、というものです。例えば、 os.stat(path) は path に関する stat 情報を、 (POSIX を元にした ) 同じフォーマットで返します。
* 特定のオペレーティングシステム固有の拡張も os を介して利用することができますが、これらの利用はもちろん、可搬性を脅かします。
* パスやファイル名を受け付けるすべての関数は、バイト列型および文字列型両方のオブジェクトを受け付け、パスやファイル名を返す時は、同じ型のオブジェクトを返します。
* 「利用できる環境 : Unix 」の意味はこの関数が Unix システムにあることが多いということです。このことは特定の OS における存在を主張するものではありません。
* 特に記述がない場合、「利用できる環境 : Unix 」と書かれている関数は、 Unix をコアにしている Mac OS X でも利用することができます。

属性|概要
----|----
exception os.error|組み込みの OSError 例外に対するエイリアスです。
os.name|import されているオペレーティングシステムに依存するモジュールの名前です。現在次の名前が登録されています: 'posix', 'nt', 'java'。

#### 注釈

> このモジュール内のすべての関数は、間違った、あるいはアクセス出来ないファイル名やファイルパス、その他型が合っていても OS が受理しない引数に対して、 OSError を送出します。 

#### 参考

> sys.platform はより細かな粒度を持っています。 os.uname() はシステム依存のバージョン情報を提供します。

> platform モジュールはシステムの詳細な識別情報をチェックする機能を提供しています。

## [16.1.1. ファイル名、コマンドライン引数、および環境変数](https://docs.python.jp/3/library/os.html#file-names-command-line-arguments-and-environment-variables)

スルーしていいと思う。

> Python では、ファイル名、コマンドライン引数、および環境変数を表すのに文字列型を使用します。一部のシステムでは、これらをオペレーティングシステムに渡す前に、文字列からバイト列へ、またはその逆のデコードが必要です。Python はこの変換を行うためにファイルシステムのエンコーディングを使用します (sys.getfilesystemencoding() 参照)。

> バージョン 3.1 で変更: 一部のシステムでは、ファイルシステムのエンコーディングを使用して変換すると失敗する場合があります。この場合、Python は surrogateescape エンコーディングエラーハンドラー を使用します。これは、デコード時にデコードできないバイト列は Unicode 文字 U+DCxx に置き換えられ、それらはエンコード時に再び元のバイト列に変換されることを意味します。

> ファイルシステムのエンコーディングでは、すべてが 128 バイト以下に正常にデコードされることが保証されなくてはなりません。ファイルシステムのエンコーディングでこれが保証されなかった場合は、API 関数が UnicodeError を送出します。

## [16.1.2. プロセスのパラメーター](https://docs.python.jp/3/library/os.html#process-parameters)

os.PathLikeクラスの使い方が不明。でも、pathlibモジュールはそれを使っているようなので、pathlibが使えればOKか。

> これらの関数とデータアイテムは、現在のプロセスおよびユーザーに対する情報提供および操作のための機能を提供しています。

属性|概要
----|----
os.ctermid()|プロセスの制御端末に対応するファイル名を返します。
os.environ|文字列の環境を表す マップ型 オブジェクトです。例えば、 environ['HOME'] は (一部のプラットフォームでは) ホームディレクトリのパス名であり、 C における getenv("HOME") と等価です。
os.environb|environ のバイト列版です。環境変数をバイト文字列で表す マップ型 オブジェクトです。environ と environb は同期されます。(environb を変更すると environ が更新され、逆の場合も同様に更新されます)。
os.fsencode(filename)|Encode path-like filename to the filesystem encoding with 'surrogateescape' error handler, or 'strict' on Windows; return bytes unchanged.
os.fsdecode(filename)|Decode the path-like filename from the filesystem encoding with 'surrogateescape' error handler, or 'strict' on Windows; return str unchanged.
os.fspath(path)|path のファイルシステム表現を返します。
class os.PathLike|ファイルシステムパスを表すオブジェクト(例: pathlib.PurePath) 向けの abstract base class です。
    abstractmethod __fspath__()|    このオブジェクトが表現するファイルシステムパスを返します。
os.getenv(key, default=None)|環境変数 key が存在すればその値を返し、存在しなければ default を返します。key、default、および返り値は文字列です。
os.getenvb(key, default=None)|環境変数 key が存在すればその値を返し、存在しなければ default を返します。key、default、および返り値はバイト列型です。
os.get_exec_path(env=None)|プロセスを起動する時に名前付き実行ファイルを検索するディレクトリのリストを返します。 env が指定されると、それを環境変数の辞書とみなし、その辞書からキー PATH の値を探します。 デフォルトでは env は None であり、environ が使用されます。
os.getegid()|現在のプロセスの実効グループ id を返します。この id は現在のプロセスで実行されているファイルの "set id" ビットに対応します。
os.geteuid()|現在のプロセスの実効ユーザー id を返します。
os.getgid()|現在のプロセスの実グループ id を返します。
os.getgrouplist(user, group)|user が所属するグループ id のリストを返します。group がリストにない場合、それを追加します。通常、group にはユーザー user のパスワードレコードに書かれているグループ ID を指定します。
os.getgroups()|現在のプロセスに関連付けられた従属グループ id のリストを返します。
os.getlogin()|プロセスの制御端末にログインしているユーザー名を返します。ほとんどの場合、ユーザーが誰かを知りたい時には環境変数 LOGNAME や USERNAME を、現在の実ユーザー id のログイン名を知りたい時は pwd.getpwuid(os.getuid())[0] を使う方が便利です。
os.getpgid(pid)|プロセス id pid のプロセスのプロセスグループ id を返します。 pid が 0 の場合、現在のプロセスのプロセスグループ id を返します。
os.getpgrp()|現在のプロセスグループの id を返します。
os.getpid()|現在のプロセス id を返します。
os.getppid()|親プロセスのプロセス id を返します。親プロセスが終了していた場合、Unix では init プロセスの id (1) が返され、Windows では親のプロセス id だったもの (別のプロセスで再利用されているかもしれない) がそのまま返されます。
os.getpriority(which, who)|プログラムのスケジューリング優先度を取得します。which の値は PRIO_PROCESS、PRIO_PGRP、あるいは PRIO_USER のいずれか一つで、who の値は which に応じて解釈されます (PRIO_PROCESS であればプロセス識別子、PRIO_PGRP であればプロセスグループ識別子、そして PRIO_USER であればユーザー ID)。who の値がゼロの場合、呼び出したプロセス、呼び出したプロセスのプロセスグループ、および呼び出したプロセスの実ユーザー id を (それぞれ) 意味します。
os.PRIO_PROCESS, os.PRIO_PGRP, os.PRIO_USER|getpriority() と setpriority() 用のパラメーターです。
os.getresuid()|現在のプロセスの実ユーザー id 、実効ユーザー id 、および保存ユーザー id を示す、 (ruid, euid, suid) のタプルを返します。
os.getresgid()|現在のプロセスの実グループ id 、実効グループ id 、および保存グループ id を示す、 (rgid, egid, sgid) のタプルを返します。
os.getuid()|現在のプロセスの実ユーザー id を返します。
os.initgroups(username, gid)|システムの initgroups() を呼び出し、指定された username がメンバーである全グループと gid で指定されたグループでグループアクセスリストを初期化します。
os.putenv(key, value)|key という名前の環境変数に文字列 value を設定します。このような環境変数の変更は、os.system()、popen()、または fork() と execv() で起動されたサブプロセスに影響を与えます。
os.setegid(egid)|現在のプロセスに実効グループ id をセットします。
os.seteuid(euid)|現在のプロセスに実効ユーザー id をセットします。
os.setgid(gid)|現在のプロセスにグループ id をセットします。
os.setgroups(groups)|現在のグループに関連付けられた従属グループ id のリストを groups に設定します。 groups はシーケンス型でなくてはならず、各要素はグループを特定する整数でなくてはなりません。通常、この操作はスーパユーザーしか利用できません。
os.setpgrp()|システムコール setpgrp() か setpgrp(0, 0) のどちらか(実装されているもの)を呼び出します。機能については UNIX マニュアルを参照して下さい。
os.setpgid(pid, pgrp)|システムコール setpgid() を呼び出してプロセス id pid のプロセスのプロセスグループ id を pgrp に設定します。この動作に関しては Unix のマニュアルを参照してください。
os.setpriority(which, who, priority)|プログラムのスケジューリング優先度を設定します。which は PRIO_PROCESS、PRIO_PGRP、あるいは PRIO_USER のいずれか一つで、who の値は which に応じて解釈されます (PRIO_PROCESS であればプロセス識別子、PRIO_PGRP であればプロセスグループ識別子、そして PRIO_USER であればユーザー ID)。who の値がゼロの場合、呼び出したプロセス、呼び出したプロセスのプロセスグループ、および呼び出したプロセスの実ユーザー id を (それぞれ) 意味します。priority は -20 から 19 の整数値で、デフォルトの優先度は 0 です。小さい数値ほど優先されるスケジューリングとなります。
os.setregid(rgid, egid)|現在のプロセスの実グループ id および実効グループ id を設定します。
os.setresgid(rgid, egid, sgid)|現在のプロセスの、実グループ id 、実効グループ id 、および保存グループ id を設定します。
os.setresuid(ruid, euid, suid)|現在のプロセスの実ユーザー id 、実効ユーザー id 、および保存ユーザー id を設定します。
os.setreuid(ruid, euid)|現在のプロセスの実ユーザー id および実効ユーザー id を設定します。
os.getsid(pid)|getsid() システムコールを呼び出します。機能については Unix のマニュアルを参照してください。
os.setsid()|setsid() システムコールを呼び出します。機能については Unix のマニュアルを参照してください。
os.setuid(uid)|現在のプロセスのユーザー id を設定します。
os.strerror(code)|エラーコード code に対応するエラーメッセージを返します。未知のエラーコードの対して strerror() が NULL を返すプラットフォームでは、 ValueError が送出されます。
os.supports_bytes_environ|環境のネイティブ OS タイプがバイト型の場合、 True です (例: Windows では、 False です)。
os.umask(mask)|現在の数値 umask を設定し、以前の umask 値を返します。
os.uname()|現在のオペレーティングシステムを識別する情報を返します。返り値は 5 個の属性を持つオブジェクトです:
os.unsetenv(key)|key という名前の環境変数を unset (削除) します。このような環境変数の変更は、os.system()、popen()、または fork() と execv() で起動されたサブプロセスに影響を与えます。

