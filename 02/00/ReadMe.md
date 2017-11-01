# [13.5. zipfile — ZIP アーカイブの処理](https://docs.python.jp/3/library/zipfile.html)

< [13. データ圧縮とアーカイブ](https://docs.python.jp/3/library/archiving.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/zipfile.py](https://github.com/python/cpython/tree/3.6/Lib/zipfile.py)

> ZIP は一般によく知られているアーカイブ (書庫化) および圧縮の標準ファイルフォーマットです。このモジュールでは ZIP 形式のファイルの作成、読み書き、追記、書庫内のファイル一覧の作成を行うためのツールを提供します。より高度な使い方でこのモジュールを利用したいのであれば、 PKZIP Application Note に定義されている ZIP ファイルフォーマットの理解が必要になるでしょう。

> このモジュールは現在マルチディスク ZIP ファイルを扱うことはできません。ZIP64 拡張を利用する ZIP ファイル (サイズが 4 GiB を超えるような ZIP ファイル) は扱えます。このモジュールは暗号化されたアーカイブの復号をサポートしますが、現在暗号化ファイルを作成することはできません。C 言語ではなく、Python で実装されているため、復号は非常に遅くなっています。

python実装なので遅いらしい。使いたくない。

> このモジュールは以下の項目を定義しています:

属性|概要
----|----
exception zipfile.BadZipFile|正常ではない ZIP ファイルに対して送出されるエラーです。
exception zipfile.BadZipfile|BadZipFile の別名です。過去のバージョンの Python との互換性のために用意されています。
exception zipfile.LargeZipFile|ZIP ファイルが ZIP64 の機能を必要としているが、その機能が有効化されていない場合に送出されるエラーです。
class zipfile.ZipFile|ZIP ファイルの読み書きのためのクラスです。コンストラクタの詳細については、ZipFile オブジェクト 節を参照してください。
class zipfile.PyZipFile|Python ライブラリを含む、ZIP アーカイブを作成するためのクラスです。
class zipfile.ZipInfo(filename='NoName', date_time=(1980, 1, 1, 0, 0, 0))|アーカイブ内の 1 個のメンバの情報を取得するために使うクラスです。このクラスのインスタンスは ZipFile オブジェクトの getinfo() および infolist() メソッドを返します。ほとんどの zipfile モジュールの利用者はこれらを作成する必要はなく、このモジュールによって作成されたものを使用できます。filename はアーカイブメンバのフルネームでなければならず、date_time はファイルが最後に変更された日時を表す 6 個のフィールドのタプルでなければなりません; フィールドは ZipInfo オブジェクト 節で説明されています。
zipfile.is_zipfile(filename)|filename が正しいマジックナンバをもつ ZIP ファイルの時に True を返し、そうでない場合 False を返します。filename にはファイルやファイルライクオブジェクトを渡すこともできます。|バージョン 3.1 で変更: ファイルおよびファイルライクオブジェクトをサポートしました。
zipfile.ZIP_STORED|アーカイブメンバを圧縮しない (複数ファイルを一つにまとめるだけ) ことを表す数値定数です。
zipfile.ZIP_DEFLATED|通常の ZIP 圧縮方法を表す数値定数です。これには zlib モジュールが必要です。
zipfile.ZIP_BZIP2|BZIP2 圧縮方法を表す数値定数です。これには bz2 モジュールが必要です。|バージョン 3.3 で追加.
zipfile.ZIP_LZMA|LZMA 圧縮方法を表す数値定数です。これには lzma モジュールが必要です。|バージョン 3.3 で追加.|注釈|ZIP ファイルフォーマット仕様は 2001 年より bzip2 圧縮を、2006 年より LZMA 圧縮をサポートしていますが、(過去の Python リリースを含む) 一部のツールはこれら圧縮方式をサポートしていないため、ZIP ファイルの処理を全く受け付けないか、あるいは個々のファイルの抽出に失敗する場合があります。

### 参考

URL|概要
---|----
[PKZIP Application Note](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)|ZIP ファイルフォーマットおよびアルゴリズムを作成した Phil Katz によるドキュメント。
[Info-ZIP Home Page](http://www.info-zip.org/)|Info-ZIP プロジェクトによる ZIP アーカイブプログラムおよびプログラム開発ライブラリに関する情報。

## [13.5.1. ZipFile オブジェクト](https://docs.python.jp/3/library/zipfile.html#zipfile-objects)

class zipfile.ZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True)|Open a ZIP file, where file can be a path to a file (a string), a file-like object or a path-like object. The mode parameter should be 'r' to read an existing file, 'w' to truncate and write a new file, 'a' to append to an existing file, or 'x' to exclusively create and write a new file. If mode is 'x' and file refers to an existing file, a FileExistsError will be raised. If mode is 'a' and file refers to an existing ZIP file, then additional files are added to it. If file does not refer to a ZIP file, then a new ZIP archive is appended to the file. This is meant for adding a ZIP archive to another file (such as python.exe). If mode is 'a' and the file does not exist at all, it is created. If mode is 'r' or 'a', the file should be seekable. compression is the ZIP compression method to use when writing the archive, and should be ZIP_STORED, ZIP_DEFLATED, ZIP_BZIP2 or ZIP_LZMA; unrecognized values will cause NotImplementedError to be raised. If ZIP_DEFLATED, ZIP_BZIP2 or ZIP_LZMA is specified but the corresponding module (zlib, bz2 or lzma) is not available, RuntimeError is raised. The default is ZIP_STORED. If allowZip64 is True (the default) zipfile will create ZIP files that use the ZIP64 extensions when the zipfile is larger than 4 GiB. If it is false zipfile will raise an exception when the ZIP file would require ZIP64 extensions.(ZIPファイルを開きます。ファイルはファイル（文字列）、ファイルのようなオブジェクト、パスのようなオブジェクトへのパスです。モードパラメータは、既存のファイルを読み込むには 'r'、新しいファイルを切り詰めて書き込むには 'w'、既存のファイルに追加するには 'a'、新しいファイルを作成して書き込むには 'x'にする必要があります。 modeが 'x'でfileが既存のファイルを参照する場合、FileExistsErrorが発生します。モードが 'a'で、ファイルが既存のZIPファイルを参照する場合は、追加のファイルが追加されます。ファイルがZIPファイルを参照していない場合は、新しいZIPアーカイブがファイルに追加されます。これは、ZIPアーカイブを別のファイル（python.exeなど）に追加するためのものです。モードが 'a'で、ファイルがまったく存在しない場合は作成されます。 modeが 'r'または 'a'の場合、ファイルはシーク可能でなければなりません。圧縮は、アーカイブを書くときに使用するZIP圧縮方法であり、ZIP_STORED、ZIP_DEFLATED、ZIP_BZIP2またはZIP_LZMAでなければなりません。認識されない値はNotImplementedErrorを発生させます。 ZIP_DEFLATED、ZIP_BZIP2またはZIP_LZMAが指定されていても、対応するモジュール（zlib、bz2またはlzma）が使用できない場合、RuntimeErrorが発生します。デフォルトはZIP_STOREDです。 allowZip64がTrue（デフォルト）の場合、zipファイルは4 GiBより大きい場合にZIP64拡張を使用するZIPファイルを作成します。偽であれば、ZIPファイルはZIP64拡張が必要な​​ときに例外を発生させます。)
ZipFile.close()|アーカイブファイルをクローズします。close() はプログラムを終了する前に必ず呼び出さなければなりません。さもないとアーカイブ上の重要なレコードが書き込まれません。
ZipFile.getinfo(name)|アーカイブメンバ name に関する情報を持つ ZipInfo オブジェクトを返します。アーカイブに含まれないファイル名に対して getinfo() を呼び出すと、KeyError が送出されます。
ZipFile.infolist()|アーカイブに含まれる各メンバの ZipInfo オブジェクトからなるリストを返します。既存のアーカイブファイルを開いている場合、リストの順番は実際の ZIP ファイル中のメンバの順番と同じになります。
ZipFile.namelist()|アーカイブメンバの名前のリストを返します。
ZipFile.open(name, mode='r', pwd=None, *, force_zip64=False)|Access a member of the archive as a binary file-like object. name can be either the name of a file within the archive or a ZipInfo object. The mode parameter, if included, must be 'r' (the default) or 'w'. pwd is the password used to decrypt encrypted ZIP files.(バイナリファイルのようなオブジェクトとしてアーカイブのメンバーにアクセスします。 nameは、アーカイブ内のファイル名またはZipInfoオブジェクトのいずれかです。 モードパラメータが含まれている場合は、 'r'（デフォルト）または 'w'でなければなりません。 pwdは、暗号化されたZIPファイルを復号化するために使用されるパスワードです。)
ZipFile.extract(member, path=None, pwd=None)|メンバをアーカイブから現在の作業ディレクトリに展開します。member は展開するファイルのフルネームまたは ZipInfo オブジェクトでなければなりません。ファイル情報は可能な限り正確に展開されます。path は展開先のディレクトリを指定します。member はファイル名または ZipInfo オブジェクトです。pwd は暗号化ファイルに使われるパスワードです。
ZipFile.extractall(path=None, members=None, pwd=None)|すべてのメンバをアーカイブから現在の作業ディレクトリに展開します。path は展開先のディレクトリを指定します。members は、オプションで、namelist() で返されるリストの部分集合でなければなりません。pwd は、暗号化ファイルに使われるパスワードです。
ZipFile.printdir()|アーカイブの内容の一覧を sys.stdout に出力します。
ZipFile.setpassword(pwd)|pwd を展開する圧縮ファイルのデフォルトパスワードとして指定します。
ZipFile.read(name, pwd=None)|Return the bytes of the file name in the archive. name is the name of the file in the archive, or a ZipInfo object. The archive must be open for read or append. pwd is the password used for encrypted files and, if specified, it will override the default password set with setpassword(). Calling read() on a ZipFile that uses a compression method other than ZIP_STORED, ZIP_DEFLATED, ZIP_BZIP2 or ZIP_LZMA will raise a NotImplementedError. An error will also be raised if the corresponding compression module is not available.(アーカイブ内のファイル名のバイトを返します。 nameは、アーカイブ内のファイル名、またはZipInfoオブジェクトです。 アーカイブは、読み取りまたは追加のために開いている必要があります。 pwdは暗号化されたファイルに使用されるパスワードで、指定されていればsetpassword（）で設定されたデフォルトのパスワードを上書きします。 ZIP_STORED、ZIP_DEFLATED、ZIP_BZIP2またはZIP_LZMA以外の圧縮メソッドを使用するZipFileでread（）を呼び出すと、NotImplementedErrorが発生します。 対応する圧縮モジュールが利用できない場合にも、エラーが発生します。)
ZipFile.testzip()|Read all the files in the archive and check their CRC’s and file headers. Return the name of the first bad file, or else return None.(アーカイブ内のすべてのファイルを読み、CRCおよびファイルヘッダーを確認します。 最初の不良ファイルの名前を返し、そうでない場合はNoneを返します。)
ZipFile.write(filename, arcname=None, compress_type=None)|Write the file named filename to the archive, giving it the archive name arcname (by default, this will be the same as filename, but without a drive letter and with leading path separators removed). If given, compress_type overrides the value given for the compression parameter to the constructor for the new entry. The archive must be open with mode 'w', 'x' or 'a'.(filenameという名前のファイルをアーカイブに書き出し、アーカイブ名arcnameを与えます（デフォルトではfilenameと同じですが、ドライブレターがなく、先頭のパス区切り文字は削除されます）。 指定された場合、compress_typeは、圧縮パラメータに指定された値を新しいエントリのコンストラクタにオーバーライドします。 アーカイブは、モード 'w'、 'x'または 'a'で開いている必要があります。)
ZipFile.writestr(zinfo_or_arcname, data[, compress_type])|Write the string data to the archive; zinfo_or_arcname is either the file name it will be given in the archive, or a ZipInfo instance. If it’s an instance, at least the filename, date, and time must be given. If it’s a name, the date and time is set to the current date and time. The archive must be opened with mode 'w', 'x' or 'a'.(文字列データをアーカイブに書き込みます。 zinfo_or_arcnameは、アーカイブで指定されるファイル名かZipInfoインスタンスのいずれかです。 インスタンスの場合は、少なくともファイル名、日付、時刻を指定する必要があります。 名前の場合、日付と時刻は現在の日付と時刻に設定されます。 アーカイブは、モード 'w'、 'x'または 'a'で開く必要があります。)

```python
import zipfile

with zipfile.ZipFile('spam.zip', 'w') as f:
    f.write('0.py')

with zipfile.ZipFile('spam.zip') as myzip:
    with myzip.open('0.py') as myfile:
        print(myfile.read())
```
```sh
$ python 0.py 
b"import zipfile\n\ndata = b'Insert Data Here'\nwith zipfile.ZipFile('spam.zip', 'w') as f:\n#    f.write(data)\n    f.write('0.py')\n\nwith zipfile.ZipFile('spam.zip') as myzip:\n    with myzip.open('0.py') as myfile:\n        print(myfile.read())\n\n"
```

> 以下のデータ属性も利用することができます:

属性|概要
----|----
ZipFile.filename|Name of the ZIP file.(ZIPファイルの名前。)
ZipFile.debug|使用するデバッグ出力レベルです。この属性は 0 (デフォルト、何も出力しない) から 3 (最も多く出力する) までの値に設定することができます。デバッグ情報は sys.stdout に出力されます。
ZipFile.comment|ZIP ファイルに関連付けられたコメント文字列です。モード 'w' 、 'x' または 'a' で作成された ZipFile インスタンスへコメントを割り当てる場合、文字列長は 65535 バイトまででにしてください。それを超えた場合は close() が呼び出されてアーカイブへ書き込む際に切り捨てられます。

## [13.5.2. PyZipFile オブジェクト](https://docs.python.jp/3/library/zipfile.html#pyzipfile-objects)

> PyZipFile コンストラクタは ZipFile コンストラクタと同じパラメータに加え、optimize パラメータをとります。

属性|概要
----|----
class zipfile.PyZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True, optimize=-1)|バージョン 3.2 で追加: パラメータに optimize を追加しました。バージョン 3.4 で変更: ZIP64 拡張がデフォルトで有効になりました。インスタンスは ZipFile オブジェクトのメソッドの他に、追加のメソッドを 1 個持ちます:
    writepy(pathname, basename='', filterfunc=None)|    *.py ファイルを探し、一致するファイルをアーカイブに追加します。

## [13.5.3. ZipInfo オブジェクト](https://docs.python.jp/3/library/zipfile.html#zipinfo-objects)

> ZipInfo クラスのインスタンスは、ZipFile オブジェクトの getinfo() および infolist() メソッドによって返されます。各オブジェクトは ZIP アーカイブ内の 1 個のメンバに関する情報を格納します。

> There is one classmethod to make a ZipInfo instance for a filesystem file:

classmethod ZipInfo.from_file(filename, arcname=None)|Construct a ZipInfo instance for a file on the filesystem, in preparation for adding it to a zip file.(zipファイルに追加する準備として、ファイルシステム上のファイルのZipInfoインスタンスを構築します。)

> Instances have the following methods and attributes:(インスタンスには、次のメソッドと属性があります。)

属性|概要
----|----
ZipInfo.is_dir()|Return True if this archive member is a directory.
ZipInfo.filename|アーカイブ中のファイル名。
ZipInfo.date_time|アーカイブメンバの最終更新日時。6 つの値からなるタプルになります: index 0〜5(西暦年,月,日,時,分,秒)
ZipInfo.compress_type|アーカイブメンバの圧縮形式。
ZipInfo.comment|各アーカイブメンバに対するコメント。
ZipInfo.extra|拡張フィールドデータ。この文字列に含まれているデータの内部構成については、PKZIP Application Note でコメントされています。
ZipInfo.create_system|ZIP アーカイブを作成したシステムを記述する文字列。
ZipInfo.create_version|このアーカイブを作成した PKZIP のバージョン。
ZipInfo.extract_version|このアーカイブを展開する際に必要な PKZIP のバージョン。
ZipInfo.reserved|予約領域。ゼロでなくてはなりません。
ZipInfo.flag_bits|ZIP フラグビット列。
ZipInfo.volume|ファイルヘッダのボリューム番号。
ZipInfo.internal_attr|内部属性。
ZipInfo.external_attr|外部ファイル属性。
ZipInfo.header_offset|ファイルヘッダへのバイトオフセット。
ZipInfo.CRC|圧縮前のファイルの CRC-32 チェックサム。
ZipInfo.compress_size|圧縮後のデータのサイズ。
ZipInfo.file_size|圧縮前のファイルのサイズ。

## [13.5.4. コマンドラインインターフェイス](https://docs.python.jp/3/library/zipfile.html#command-line-interface)

zipfile モジュールは、 ZIP アーカイブを操作するための簡単なコマンドラインインターフェースを提供しています。

ZIP アーカイブを新規に作成したい場合、-c オプションの後にまとめたいファイルを列挙してください:

```sh
$ python -m zipfile -c monty.zip spam.txt eggs.txt
```

ディレクトリを渡すこともできます:

```sh
$ python -m zipfile -c monty.zip life-of-brian_1979/
```

ZIP アーカイブを特定のディレクトリに展開したい場合、-e オプションを使用してください:

```sh
$ python -m zipfile -e monty.zip target-dir/
```

ZIP アーカイブ内のファイル一覧を表示するには -l を使用してください:

```sh
$ python -m zipfile -l monty.zip
```

### [13.5.4.1. コマンドラインオプション](https://docs.python.jp/3/library/zipfile.html#command-line-options)

引数|概要
----|----
-l <zipfile>|zipfile 内のファイル一覧を表示します。
-c <zipfile> <source1> ... <sourceN>|ソースファイルから zipfile を作成します。
-e <zipfile> <output_dir>|zipfile を対象となるディレクトリに展開します。
-t <zipfile>|zipfile が有効かどうか調べます。

