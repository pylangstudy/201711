# [16.1. os — 雑多なオペレーティングシステムインタフェース](https://docs.python.jp/3/library/os.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/secrets.py](https://github.com/python/cpython/tree/3.6/Lib/secrets.py)

## [16.1.5. ファイルとディレクトリ](https://docs.python.jp/3/library/os.html#files-and-directories)

Linuxコマンドによるファイル操作系と同様のAPIがある。pathlibで代用できるものもある。それら以外の細かいファイルシステムに関するAPIについては、利用頻度が低いと思う。

> 一部の Unix プラットフォームでは、このセクションの関数の多くが以下の機能を一つ以上サポートしています。

* ファイル記述子の指定: 一部の関数では、path 引数はパス名を示す文字列だけでなく、ファイル記述子でも指定できます。関数はファイル記述子が参照するファイルを操作します。(POSIX システムでは、Python は関数の f... バージョンを呼び出します)
* そのプラットフォーム上で path にファイル記述子を使用できるかどうかは、os.supports_fd で確認できます。使用できない場合 NotImplementedError が送出されます。
* その関数が引数に dir_fd または follow_symlinks もサポートしている場合、path にファイル記述子を指定した時にそれらのいずれかを指定するとエラーになります。
* ディレクトリ記述子への相対パス: dir_fd が None ではない場合、そのファイル記述子はディレクトリを参照しているはずであり、操作するパスは相対パスであるべきです; パスはそのディレクトリへの相対パスになります。パスが絶対パスであった場合、dir_fd は無視されます。(POSIX システムでは、Python は関数の ...at または f...at バージョンを呼び出します)
* そのプラットフォーム上で dir_fd がサポートされているかどうかは、os.supports_dir_fd で確認できます。サポートされていない場合 NotImplementedError が送出されます。
* シンボリックリンクをたどらない: follow_symlinks が False で、かつ、操作するパスの末尾の要素がシンボリックリンクの場合、その関数はリンクの指し示す先のファイルではなく、シンボリックリンク自身を操作します。(POSIX システムでは、Python は関数の l... バージョンを呼び出します)
* そのプラットフォーム上で follow_symlinks がサポートされているかどうかは、os.supports_follow_symlinks で確認できます。利用できない場合 NotImplementedError が送出されます。

属性|概要
----|----
os.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)|実 uid/gid を使って path に対するアクセスが可能か調べます。ほとんどのオペレーティングシステムは実効 uid/gid を使うため、このルーチンは suid/sgid 環境において、プログラムを起動したユーザーが path に対するアクセス権をもっているかを調べるために使われます。 path が存在するかどうかを調べるには mode を F_OK にします。ファイルアクセス権限 ( パーミッション ) を調べるには、 R_OK, W_OK, X_OK から一つまたはそれ以上のフラグを論理和指定でとることもできます。アクセスが許可されている場合 True を、そうでない場合 False を返します。詳細は access(2) の Unix マニュアルページを参照してください。
os.F_OK, os.R_OK, os.W_OK, os.X_OK|access() で path をテストする時に mode 引数に渡す値です。上からそれぞれ、ファイルの存在、読み込み許可、書き込み許可、および実行許可になります。
os.chdir(path)|現在の作業ディレクトリを path に設定します。
os.chflags(path, flags, *, follow_symlinks=True)|path のフラグを flags に変更します。 flags は、以下の値 (stat モジュールで定義されているもの ) をビット単位の論理和で組み合わせることができます :stat.UF_NODUMP, stat.UF_IMMUTABLE, stat.UF_APPEND, stat.UF_OPAQUE, stat.UF_NOUNLINK, stat.UF_COMPRESSED, stat.UF_HIDDEN, stat.SF_ARCHIVED, stat.SF_IMMUTABLE, stat.SF_APPEND, stat.SF_NOUNLINK, stat.SF_SNAPSHOT
os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True)|path のモードを数値 mode に変更します。 mode は、 (stat モジュールで定義されている ) 以下の値のいずれかまたはビット単位の論理和で組み合わせた値を取り得ます :stat.S_ISUID, stat.S_ISGID, stat.S_ENFMT, stat.S_ISVTX, stat.S_IREAD, stat.S_IWRITE, stat.S_IEXEC, stat.S_IRWXU, stat.S_IRUSR, stat.S_IWUSR, stat.S_IXUSR, stat.S_IRWXG, stat.S_IRGRP, stat.S_IWGRP, stat.S_IXGRP, stat.S_IRWXO, stat.S_IROTH, stat.S_IWOTH, stat.S_IXOTH
os.chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True)|path の所有者 id およびグループ id を、数値 uid および gid に変更します。いずれかの id を変更せずにおくには、その値として -1 を指定します。
os.chroot(path)|現在のプロセスのルートディレクトリを path に変更します。
os.fchdir(fd)|現在の作業ディレクトリをファイル記述子 fd が表すディレクトリに変更します。記述子はオープンしているファイルではなく、オープンしたディレクトリを参照していなければなりません。Python 3.3 以降では os.chdir(fd) と等価です。
os.getcwd()|現在の作業ディレクトリを表す文字列を返します。
os.getcwdb()|現在の作業ディレクトリを表すバイト列を返します。
os.lchflags(path, flags)|path のフラグを数値 flags に設定します。chflags() に似ていますが、シンボリックリンクをたどりません。Python 3.3 以降では os.chflags(path, flags, follow_symlinks=False) と等価です。
os.lchmod(path, mode)|path のモードを数値 mode に変更します。パスがシンボリックリンクの場合はそのリンク先ではなくシンボリックリンクそのものに対して作用します。mode に指定できる値については chmod() のドキュメントを参照してください。Python 3.3 以降では os.chmod(path, mode, follow_symlinks=False) と等価です。
os.lchown(path, uid, gid)|path の所有者 id およびグループ id を、数値 uid および gid に変更します。この関数はシンボリックリンクをたどりません。Python 3.3 以降では os.chown(path, uid, gid, follow_symlinks=False) と等価です。
os.link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)|src を指し示すハードリンク dst を作成します。
os.listdir(path='.')|path で指定されたディレクトリ内のエントリ名が入ったリストを返します。リスト内の順番は不定です。特殊エントリ '.' および '..' は、それらがディレクトリ内に存在してもリストには含められません。
os.lstat(path, *, dir_fd=None)|与えられたパスに対して lstat() システムコールと同じ処理を行います。stat() と似ていますが、シンボリックリンクをたどりません。 stat_result オブジェクトを返します。
os.mkdir(path, mode=0o777, *, dir_fd=None)|ディレクトリ path を数値モード mode で作成します。
os.makedirs(name, mode=0o777, exist_ok=False)|再帰的にディレクトリを作成する関数です。mkdir() と似ていますが、末端ディレクトリを作成するために必要なすべての中間ディレクトリも作成します。
os.mkfifo(path, mode=0o666, *, dir_fd=None)|FIFO (名前付きパイプ) path を数値モード mode で作成します。先に現在の umask 値でマスクされます。
os.mknod(path, mode=0o600, device=0, *, dir_fd=None)|path という名前で、ファイルシステムノード (ファイル、デバイス特殊ファイル、または名前つきパイプ) を作成します。mode は、作成するノードのアクセス権限とタイプの両方を stat.S_IFREG、stat.S_IFCHR、stat.S_IFBLK、および stat.S_IFIFO の組み合わせ (ビット単位の論理和) で指定します (これらの定数は stat で利用可能です)。stat.S_IFCHR と stat.S_IFBLK を指定した場合、devide は新しく作成されたデバイス特殊ファイルを (おそらく os.makedev() を使って) 定義し、それ以外の定数を指定した場合は無視されます。
os.major(device)|RAW デバイス番号から、デバイスのメジャー番号を取り出します ( 通常 stat の st_dev か st_rdev フィールドです ) 。
os.minor(device)|RAW デバイス番号から、デバイスのマイナー番号を取り出します ( 通常 stat の st_dev か st_rdev フィールドです ) 。
os.makedev(major, minor)|メジャーおよびマイナーデバイス番号から、新しく RAW デバイス番号を作成します。
os.pathconf(path, name)|名前付きファイルに関連するシステム設定情報を返します。 name には取得したい設定名を指定します ; これは定義済みのシステム値名の文字列で、多くの標準 (POSIX.1 、 Unix 95 、 Unix 98 その他 ) で定義されています。プラットフォームによっては別の名前も定義しています。ホストオペレーティングシステムの関知する名前は pathconf_names 辞書で与えられています。このマップ型オブジェクトに入っていない設定変数については、 name に整数を渡してもかまいません。
os.pathconf_names|pathconf() および fpathconf() が受理するシステム設定名を、ホストオペレーティングシステムで定義されている整数値に対応付けている辞書です。この辞書はシステムでどの設定名が定義されているかを知るために利用できます。
os.readlink(path, *, dir_fd=None)|シンボリックリンクが指しているパスを表す文字列を返します。返される値は絶対パスにも、相対パスにもなり得ます ; 相対パスの場合、 os.path.join(os.path.dirname(path), result) を使って絶対パスに変換することができます。
os.remove(path, *, dir_fd=None)|ファイル path を削除します。 path がディレクトリの場合、OSError が送出されます; ディレクトリの削除には rmdir() を使用してください。
os.removedirs(name)|再帰的なディレクトリ削除関数です。 rmdir() と同じように動作しますが、末端ディレクトリがうまく削除できるかぎり、 removedirs() は path に現れる親ディレクトリをエラーが送出されるまで ( このエラーは通常、指定したディレクトリの親ディレクトリが空でないことを意味するだけなので無視されます ) 順に削除することを試みます。例えば、 os.removedirs('foo/bar/baz') では最初にディレクトリ 'foo/bar/baz' を削除し、次に 'foo/bar' さらに 'foo' をそれらが空ならば削除します。末端のディレクトリが削除できなかった場合には OSError が送出されます。
os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)|ファイルまたはディレクトリ src の名前を dst へ変更します。dst がディレクトリの場合 OSError が送出されます。Unixでは、dst が存在し、かつファイルの場合、ユーザーの権限があるかぎり暗黙のうちに置き換えられます。この操作は、一部の Unix 系システムにおいて src と dst が異なるファイルシステム上にあると失敗することがあります。ファイル名の変更が成功する場合はアトミック操作となります (これは POSIX 要求仕様です)。Windows では、dst がすでに存在する場合には、たとえファイルの場合でも OSError が送出されます。
os.renames(old, new)|再帰的にディレクトリやファイル名を変更する関数です。 rename() のように動作しますが、新たなパス名を持つファイルを配置するために必要な途中のディレクトリ構造をまず作成しようと試みます。名前変更の後、元のファイル名のパス要素は removedirs() を使って右側から順に削除されます。
os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)|ファイルまたはディレクトリ src の名前を dst へ変更します。dst がディレクトリの場合 OSError が送出されます。dst が存在し、かつファイルの場合、ユーザーの権限がある限り暗黙のうちに置き換えられます。src と dst が異なるファイルシステム上にあると失敗することがあります。ファイル名の変更が成功する場合はアトミック操作となります (これは POSIX 要求仕様です)。
os.rmdir(path, *, dir_fd=None)|ディレクトリ path を削除します。ディレクトリが空の場合にだけ正常に動作します。そうでなければ OSError が送出されます。ディレクトリツリー全体を削除するには shutil.rmtree() を使います。
os.scandir(path='.')|path で指定されたディレクトリ内のエントリに対応する os.DirEntry オブジェクトのイテレータを返します。このエントリは、任意の順序で yield され、特殊エントリ '.' および '..' は含められません。
scandir.close()|イテレータを閉じ、獲得した資源を開放します。
class os.DirEntry|ディレクトリエントリのファイルパスとその他のファイル属性を公開するために、scandir() が yield するオブジェクトです。
name|scandir() の path 引数に対して相対的な、エントリのベースファイル名です。
path|os.path.join(scandir_path, entry.name) と等価の、エントリの絶対パス名です。ここで、scandir_path は scandir() の path 引数です。このパスは、scandir() の path 引数が絶対パスの場合にのみ、絶対パスです。
inode()|項目の inode 番号を返します。
is_dir(*, follow_symlinks=True)|この項目がディレクトリまたはディレクトリへのシンボリックリンクである場合、 True を返します。項目がそれ以外のファイルやそれ以外のファイルへのシンボリックリンクである場合や、もはや存在しない場合は False を返します。
is_file(*, follow_symlinks=True)|この項目がファイルまたはファイルへのシンボリックリンクである場合、 True を返します。項目がディレクトリやファイル以外の項目へのシンボリックリンクである場合や、もはや存在しない場合は False を返します。
is_symlink()|この項目がシンボリックリンクの場合 (たとえ破損していても)、True を返します。項目がディレクトリやあらゆる種類のファイルの場合、またはもはや存在しない場合は False を返します。
stat(*, follow_symlinks=True)|この項目の stat_result オブジェクトを返します。このメソッドは、デフォルトでシンボリックリンクをたどります。シンボリックリンクを開始するには、 follow_symlinks=False 引数を追加します。
os.stat(path, *, dir_fd=None, follow_symlinks=True)|Get the status of a file or a file descriptor. Perform the equivalent of a stat() system call on the given path. path may be specified as either a string or bytes – directly or indirectly through the PathLike interface – or as an open file descriptor. Return a stat_result object.
class os.stat_result|おおむね stat 構造体のメンバーに対応する属性を持つオブジェクトです。os.stat() 、 os.fstat() 、 os.lstat() の結果に使用されます。
st_mode|ファイルモード。ファイルタイプとファイルモードのビット （権限）。
st_ino|Iノード番号。
st_dev|このファイルが存在するデバイスの識別子。
st_nlink|ハードリンクの数。
st_uid|ファイル所有者のユーザ識別子。
st_gid|ファイル所有者のグループ識別子。
st_size|ファイルが通常のファイルまたはシンボリックリンクの場合、そのファイルのバイト単位でのサイズです。シンボリックリンクのサイズは、含まれるパス名の長さで、null バイトで終わることはありません。

>タイムスタンプ:

属性|概要
----|----
st_atime|秒で表した最終アクセス時刻。
st_mtime|秒で表した最終内容更新時刻。
st_ctime|プラットフォーム依存: Unix ではメタデータの最終更新時刻, Windows では作成時刻、単位は秒
st_atime_ns|ナノ秒 (整数) で表した最終アクセス時刻。
st_mtime_ns|ナノ秒 (整数) で表した最終内容更新時刻。
st_ctime_ns|プラットフォーム依存: Unix ではメタデータの最終更新時刻, Windows で、ナノ秒 (整数) で表した作成時刻。

>(Linux のような ) 一部の Unix システムでは、以下の属性が利用できる場合があります :

属性|概要
----|----
st_blocks|ファイルに対して割り当てられている 512 バイトのブロックの数です。ファイルにホール (hole) が含まれている場合、st_size/512 より小さくなる場合があります。
st_blksize|効率的なファイルシステム I/O のための「推奨される」ブロックサイズです。ファイルに、これより小さいチャンクで書き込むと、非効率的な読み込み、編集、再書き込みが起こる場合があります。
st_rdev|inode デバイスの場合デバイスタイプ
st_flags|ファイルのユーザ定義フラグ

>他の (FreeBSD のような ) Unix システムでは、以下の属性が利用できる場合があります ( ただし root ユーザ以外が使うと値が入っていない場合があります ):

属性|概要
----|----
st_gen|ファイル生成番号
st_birthtime|ファイル作成時刻

>Mac OS システムでは、以下の属性も利用できる場合があります:

属性|概要
----|----
st_rsize|ファイルの実際のサイズ
st_creator|ファイルの作成者
st_type|ファイルタイプ

>Windows システムでは以下の属性も利用できます:

属性|概要
----|----
st_file_attributes|Windows のファイルの属性。GetFileInformationByHandle() の返す BY_HANDLE_FILE_INFORMATION 構造の dwFileAttributes メンバーです。stat モジュールの FILE_ATTRIBUTE_* 定数を参照してください。

属性|概要
----|----
os.stat_float_times([newvalue])|stat_result がタイムスタンプに浮動小数点オブジェクトを使うかどうかを決定します。 newvalue が True の場合、以後の stat() 呼び出しは浮動小数点を返し、 False の場合には以後整数を返します。 newvalue が省略された場合、現在の設定どおりの返り値になります。
os.statvfs(path)|与えられたパスに対して statvfs() システムコールを実行します。返り値はオブジェクトで、その属性は与えられたパスが格納されているファイルシステムについて記述したものです。各属性は statvfs 構造体のメンバーに対応します : f_bsize, f_frsize, f_blocks, f_bfree, f_bavail, f_files, f_ffree, f_favail, f_flag, f_namemax 。
os.supports_dir_fd|os モジュールのどの関数が dir_fd 引数の使用を許可するかを示す、Set オブジェクト。異なるプラットフォームでは、異なる機能を持ち、あるプラットフォームで動作するオプションが、別のプラットフォームでは動作しない場合があります。一貫性を保つため、 dir_fd をサポートする関数は常に引数の指定を許可しますが、機能が実際に使用できない場合には、例外を送出します。
os.supports_effective_ids|os モジュールのどの関数が os.access() の effective_ids 引数の使用を許可するかを示す、Set オブジェクト。ローカルプラットフォームでサポートされている場合、このコレクションは os.access() を含みます。サポートされていない場合、空になります。
os.supports_fd|os モジュールのどの関数が、path 引数をオープンしているファイル記述子として指定するかを示す、Set オブジェクト。異なるプラットフォームでは、異なる機能を持ち、あるプラットフォームで動作するオプションが、別のプラットフォームでは動作しない場合があります。一貫性を保つため、 fd をサポートする関数は常に引数の指定を許可しますが、機能が実際に使用できない場合には、例外を送出します。
os.supports_follow_symlinks|os モジュールのどの関数が follow_symlinks 引数の使用を許可するかを示す、Set オブジェクト。異なるプラットフォームでは、異なる機能を持ち、あるプラットフォームで動作するオプションが、別のプラットフォームでは動作しない場合があります。一貫性を保つため、 follow_symlinks をサポートする関数は常に引数の指定を許可しますが、機能が実際に使用できない場合には、例外を送出します。
os.symlink(src, dst, target_is_directory=False, *, dir_fd=None)|src を指し示すシンボリックリンク dst を作成します。
os.sync()|ディスクキャッシュのディスクへの書き出しを強制します。
os.truncate(path, length)|path に対応するファイルを、サイズが最大で length バイトになるよう切り詰めます。
os.unlink(path, *, dir_fd=None)|ファイル path を削除します。意味上は remove() と等価です。 unlink の名前は伝統的な Unix の関数名です。詳細は remove() のドキュメントを参照してください。
os.utime(path, times=None, *, [ns, ]dir_fd=None, follow_symlinks=True)|path で指定されたファイルに最終アクセス時刻および最終修正時刻を設定します。
os.walk(top, topdown=True, onerror=None, followlinks=False)|ディレクトリツリー以下のファイル名を、ツリーをトップダウンもしくはボトムアップに走査することで作成します。ディレクトリ top を根に持つディレクトリツリーに含まれる、各ディレクトリ (top 自身を含む ) ごとに、タプル (dirpath, dirnames, filenames) を yield します。
