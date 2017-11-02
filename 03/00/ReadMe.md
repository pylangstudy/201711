# [13.6. tarfile — tar アーカイブファイルの読み書き](https://docs.python.jp/3/library/tarfile.html)

< [13. データ圧縮とアーカイブ](https://docs.python.jp/3/library/archiving.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/tarfile.py](https://github.com/python/cpython/tree/3.6/Lib/tarfile.py)

> tarfile モジュールは、gzip、bz2、および lzma 圧縮されたものを含む、tar アーカイブを読み書きできます。.zip ファイルの読み書きには zipfile モジュールか、あるいは shutil の高水準関数を使用してください。

> いくつかの事実と形態:

* モジュールが利用可能な場合、gzip、bz2 ならびに lzma で圧縮されたアーカイブを読み書きします。
* POSIX.1-1988 (ustar) フォーマットの読み書きをサポートしています。
* longname および longlink 拡張を含む GNU tar フォーマットの読み書きをサポートしています。スパースファイルの復元を含む sparse 拡張は読み込みのみサポートしています。
* POSIX.1-2001 (pax) フォーマットの読み書きをサポートしています。
* ディレクトリ、一般ファイル、ハードリンク、シンボリックリンク、fifo、キャラクターデバイスおよびブロックデバイスを処理します。また、タイムスタンプ、アクセス許可や所有者のようなファイル情報の取得および保存が可能です。

> バージョン 3.3 で変更: lzma 圧縮をサポートしました。

属性|概要
----|----
tarfile.open(name=None, mode='r', fileobj=None, bufsize=10240, **kwargs)|パス名 name の TarFile オブジェクトを返します。TarFile オブジェクトと、利用できるキーワード引数に関する詳細な情報については、TarFile オブジェクト 節を参照してください。
class tarfile.TarFile|tar アーカイブを読み書きするためのクラスです。このクラスを直接使わないこと: 代わりに tarfile.open() を使ってください。TarFile オブジェクト を参照してください。
tarfile.is_tarfile(name)|もし name が tar アーカイブファイルであり、tarfile モジュールで読み込める場合に True を返します。
exception tarfile.TarError|すべての tarfile 例外のための基本クラスです。
exception tarfile.ReadError|tar アーカイブがオープンされた時、tarfile モジュールで操作できないか、あるいは何か無効であるとき送出されます。
exception tarfile.CompressionError|圧縮方法がサポートされていないか、あるいはデータを正しくデコードできない時に送出されます。
exception tarfile.StreamError|ストリームのような TarFile オブジェクトで典型的な制限のために送出されます。
exception tarfile.ExtractError|TarFile.extract() を使った時に 致命的でない エラーに対して送出されます。ただし TarFile.errorlevel== 2 の場合に限ります。
exception tarfile.HeaderError|TarInfo.frombuf() メソッドが取得したバッファーが不正だったときに送出されます。

> モジュールレベルで以下の定数が利用できます。

属性|概要
----|----
tarfile.ENCODING|既定の文字エンコーディング。Windows では 'utf-8' 、それ以外では sys.getfilesystemencoding() の返り値です。

> 以下の各定数は、tarfile モジュールが作成できる tar アーカイブフォーマットを定義しています。詳細は、サポートしている tar フォーマット を参照してください。

属性|概要
----|----
tarfile.USTAR_FORMAT|POSIX.1-1988 (ustar) フォーマット。
tarfile.GNU_FORMAT|GNU tar フォーマット。
tarfile.PAX_FORMAT|POSIX.1-2001 (pax) フォーマット。
tarfile.DEFAULT_FORMAT|アーカイブを作成する際のデフォルトのフォーマット。現在は GNU_FORMAT です。

`open()`のmode引数値は以下の通り。

mode|action
----|------
`r` または `r:*`|圧縮方法に関して透過的に、読み込み用にオープンします (推奨)。
`r:`|非圧縮で読み込み用に排他的にオープンします。
`r:gz`|gzip 圧縮で読み込み用にオープンします。
`r:bz2`|bzip2 圧縮で読み込み用にオープンします。
`r:xz`|lzma 圧縮で読み込み用にオープンします。
`x` or `x:`|圧縮せずに tarfile を排他的に作成します。tarfile が既存の場合 FileExistsError 例外を送出します。
`x:gz`|gzip 圧縮で tarfile を作成します。tarfile が既存の場合 FileExistsError 例外を送出します。
`x:bz2`|bzip2 圧縮で tarfile を作成します。tarfile が既存の場合 FileExistsError 例外を送出します。
`x:xz`|lzma 圧縮で tarfile を作成します。tarfile が既存の場合 FileExistsError 例外を送出します。
`a` または `a:`|非圧縮で追記用にオープンします。ファイルが存在しない場合は新たに作成されます。
`w` または `w:`|非圧縮で書き込み用にオープンします。
`w:gz`|gzip 圧縮で書き込み用にオープンします。
`w:bz2`|bzip2 圧縮で書き込み用にオープンします。
`w:xz`|lzma 圧縮で書き込み用にオープンします。

モード|動作
------|----
`r|*`|tar ブロックの stream を圧縮方法に関して透過的に読み込み用にオープンします。
`r|`|非圧縮 tar ブロックの stream を読み込み用にオープンします。
`r|gz`|gzip 圧縮の stream を読み込み用にオープンします。
`r|bz2`|bzip2 圧縮の stream を読み込み用にオープンします。
`r|xz`|lzma 圧縮の stream を読み込み用にオープンします。
`w|`|非圧縮の stream を書き込み用にオープンします。
`w|gz`|gzip 圧縮の stream を書き込み用にオープンします。
`w|bz2`|bzip2 圧縮の stream を書き込み用にオープンします。
`w|xz`|lzma 圧縮の stream を書き込み用にオープンします。

### 参考

モジュール|概要
----------|----
[zipfile](https://docs.python.jp/3/library/zipfile.html#module-zipfile)|zipfile 標準モジュールのドキュメント。
[アーカイブ化操作](https://docs.python.jp/3/library/shutil.html#archiving-operations)|shutil が提供するより高水準のアーカイブ機能についてのドキュメント。
[GNU tar manual, Basic Tar Format](https://www.gnu.org/software/tar/manual/html_node/Standard.html)|GNU tar 拡張機能を含む、tar アーカイブファイルのためのドキュメント。

## [13.6.1. TarFile オブジェクト](https://docs.python.jp/3/library/tarfile.html#tarfile-objects)

> TarFile オブジェクトは、tar アーカイブへのインターフェースを提供します。tar アーカイブは一連のブロックです。アーカイブメンバー (保存されたファイル) は、ヘッダーブロックとそれに続くデータブロックで構成されています。一つの tar アーカイブにファイルを何回も保存することができます。各アーカイブメンバーは、TarInfo オブジェクトで確認できます。詳細については TarInfo オブジェクト を参照してください。

> TarFile オブジェクトは with 文のコンテキストマネージャーとして利用できます。with ブロックが終了したときにオブジェクトはクローズされます。例外が発生した時、内部で利用されているファイルオブジェクトのみがクローズされ、書き込み用にオープンされたアーカイブのファイナライズは行われないことに注意してください。使用例 節のユースケースを参照してください。

> バージョン 3.2 で追加: コンテキスト管理のプロトコルがサポートされました。

属性|概要
----|----
class tarfile.TarFile(name=None, mode='r', fileobj=None, format=DEFAULT_FORMAT, tarinfo=TarInfo, dereference=False, ignore_zeros=False, encoding=ENCODING, errors='surrogateescape', pax_headers=None, debug=0, errorlevel=0)|以下のすべての引数はオプションで、インスタンス属性としてもアクセスできます。
classmethod TarFile.open(...)|代替コンストラクターです。モジュールレベルでの tarfile.open() 関数は、実際はこのクラスメソッドへのショートカットです。
TarFile.getmember(name)|メンバー name に対する TarInfo オブジェクトを返します。name がアーカイブに見つからなければ、KeyError が送出されます。
TarFile.getmembers()|TarInfo アーカイブのメンバーをオブジェクトのリストとして返します。このリストはアーカイブ内のメンバーと同じ順番です。
TarFile.getnames()|メンバーをその名前のリストを返します。これは getmembers() で返されるリストと同じ順番です。
TarFile.list(verbose=True, *, members=None)|内容の一覧を sys.stdout に出力します。verbose が False の場合、メンバー名のみ表示します。True の場合、 ls -l に似た出力を生成します。オプションの members を与える場合、 getmembers() が返すリストのサブセットである必要があります。
TarFile.next()|TarFile が読み込み用にオープンされている時、アーカイブの次のメンバーを TarInfo オブジェクトとして返します。もしそれ以上利用可能なものがなければ、None を返します。
TarFile.extractall(path=".", members=None, *, numeric_owner=False)|すべてのメンバーをアーカイブから現在の作業ディレクトリまたは path に抽出します。オプションの members が与えられるときには、getmembers() で返されるリストの一部でなければなりません。所有者、変更時刻、アクセス権限のようなディレクトリ情報はすべてのメンバーが抽出された後にセットされます。これは二つの問題を回避するためです。一つはディレクトリの変更時刻はその中にファイルが作成されるたびにリセットされるということ、もう一つはディレクトリに書き込み許可がなければその中のファイル抽出は失敗してしまうということです。
TarFile.extract(member, path="", set_attrs=True, *, numeric_owner=False)|アーカイブからメンバーの完全な名前を使って、現在のディレクトリに展開します。ファイル情報はできる限り正確に展開されます。 member はファイル名もしくは TarInfo オブジェクトです。 path を使って別のディレクトリを指定することもできます。 path は　path-like object でも構いません。set_attrs が false でない限り、ファイルの属性 (所有者、最終更新時刻、モード) は設定されます。
TarFile.extractfile(member)|アーカイブからメンバーをファイルオブジェクトとして抽出します。member はファイル名でも TarInfo オブジェクトでも構いません。member が一般ファイルまたはリンクの場合、io.BufferedReader オブジェクトが返されます。それ以外の場合、None が返されます。
TarFile.add(name, arcname=None, recursive=True, exclude=None, *, filter=None)|ファイル name をアーカイブに追加します。name は、任意のファイルタイプ (ディレクトリ、fifo、シンボリックリンク等)です。arcname を与える場合、アーカイブ内のファイルの代替名を指定します。デフォルトではディレクトリは再帰的に追加されます。これは、recursive を False に設定することで抑止できます。exclude を指定する場合、1 つのファイル名を引数にとってブール値を返す関数である必要があります。この関数の戻り値が True の場合、そのファイルが除外されます。False の場合、そのファイルは追加されます。filter を指定する場合は、キーワード引数でなくてはなりません。これは TarInfo オブジェクトを引数として受け取り、操作した TarInfo オブジェクトを返す関数でなければなりません。代わりに None を返した場合、TarInfo オブジェクトはアーカイブから除外されます。使用例 にある例を参照してください。
TarFile.addfile(tarinfo, fileobj=None)|TarInfo オブジェクト tarinfo をアーカイブに追加します。fileobj を与える場合、binary file にしなければならず、 tarinfo.size バイトがそれから読まれ、アーカイブに追加されます。TarInfo オブジェクトを直接作成するか、gettarinfo() を使って作成することができます。
TarFile.gettarinfo(name=None, arcname=None, fileobj=None)|os.stat() の結果か、既存のファイルに相当するものから、TarInfo オブジェクトを作成します。このファイルは、name で名付けられるか、ファイル記述子を持つ file object fileobj として指定されます。name は:term:path-like object でも構いません。 arcname が与えられた場合、アーカイブ内のファイルに対して代替名を指定します。与えられない場合、名前は fileobj の name 属性 name 属性から取られます。名前はテキスト文字列にしてください。
TarFile.close()|TarFile をクローズします。書き込みモードでは、完了ゼロブロックが 2 個アーカイブに追加されます。
TarFile.pax_headers|pax グローバルヘッダーに含まれる key-value ペアの辞書です。

## [13.6.2. TarInfo オブジェクト](https://docs.python.jp/3/library/tarfile.html#tarinfo-objects)

> TarInfo オブジェクトは TarFile の一つのメンバーを表します。ファイルに必要なすべての属性 (ファイルタイプ、ファイルサイズ、時刻、アクセス権限、所有者等のような) を保存する他に、そのタイプを決定するのに役に立ついくつかのメソッドを提供します。これにはファイルのデータそのものは 含まれません 。

> TarInfo オブジェクトは TarFile のメソッド getmember()、 getmembers() および gettarinfo() によって返されます。

属性|概要
----|----
class tarfile.TarInfo(name="")|TarInfo オブジェクトを作成します。
classmethod TarInfo.frombuf(buf, encoding, errors)|TarInfo オブジェクトを文字列バッファー buf から作成して返します。
classmethod TarInfo.fromtarfile(tarfile)|TarFile オブジェクトの tarfile から、次のメンバーを読み込んで、それを TarInfo オブジェクトとして返します。
TarInfo.tobuf(format=DEFAULT_FORMAT, encoding=ENCODING, errors='surrogateescape')|TarInfo オブジェクトから文字列バッファーを作成します。引数についての情報は、TarFile クラスのコンストラクターを参照してください。

> TarInfo オブジェクトには以下のデータ属性があります:

属性|概要
----|----
TarInfo.name|アーカイブメンバーの名前。
TarInfo.size|バイト単位でのサイズ。
TarInfo.mtime|最後に変更された時刻。
TarInfo.mode|許可ビット。
TarInfo.type|ファイルタイプ。type は通常、定数 REGTYPE、AREGTYPE、LNKTYPE、SYMTYPE、DIRTYPE、FIFOTYPE、CONTTYPE、CHRTYPE、BLKTYPE、あるいは GNUTYPE_SPARSE のいずれかです。TarInfo オブジェクトのタイプをもっと簡単に解決するには、下記の is*() メソッドを使って下さい。
TarInfo.linkname|リンク先ファイルの名前。これはタイプ LNKTYPE と SYMTYPE の TarInfo オブジェクトにだけ存在します。
TarInfo.uid|ファイルメンバーを保存した元のユーザーのユーザー ID。
TarInfo.gid|ファイルメンバーを保存した元のユーザーのグループ ID。
TarInfo.uname|ファイルメンバーを保存した元のユーザーのユーザー名。
TarInfo.gname|ファイルメンバーを保存した元のユーザーのグループ名。
TarInfo.pax_headers|pax 拡張ヘッダーに関連付けられた、key-value ペアの辞書。
TarInfo オブジェクトは便利な照会用のメソッドもいくつか提供しています:
TarInfo.isfile()|Tarinfo オブジェクトが一般ファイルの場合に、True を返します。
TarInfo.isreg()|isfile() と同じです。
TarInfo.isdir()|ディレクトリの場合に True を返します。
TarInfo.issym()|シンボリックリンクの場合に True を返します。
TarInfo.islnk()|ハードリンクの場合に True を返します。
TarInfo.ischr()|キャラクターデバイスの場合に True を返します。
TarInfo.isblk()|ブロックデバイスの場合に True を返します。
TarInfo.isfifo()|FIFO の場合に True を返します。
TarInfo.isdev()|キャラクターデバイス、ブロックデバイスあるいは FIFO のいずれかの場合に True を返します。

## [13.6.3. コマンドラインインターフェイス](https://docs.python.jp/3/library/tarfile.html#command-line-interface)

> バージョン 3.4 で追加.

> tarfile モジュールは、 tar アーカイブを操作するための簡単なコマンドラインインターフェースを提供しています。

> tar アーカイブを新規に作成したい場合、-c オプションの後にまとめたいファイル名のリストを指定してください:

```sh
$ python -m tarfile -c monty.tar  spam.txt eggs.txt
```

> ディレクトリを渡すこともできます:

```sh
$ python -m tarfile -c monty.tar life-of-brian_1979/
```

> tar アーカイブをカレントディレクトリに展開したい場合、-e オプションを使用してください:

```sh
$ python -m tarfile -e monty.tar
```

> ディレクトリ名を渡すことで tar アーカイブを別のディレクトリに取り出すこともできます:

```sh
$ python -m tarfile -e monty.tar  other-dir/
```

> tar アーカイブ内のファイル一覧を表示するには -l を使用してください:

```sh
$ python -m tarfile -l monty.tar
```

### [13.6.3.1. コマンドラインオプション](https://docs.python.jp/3/library/tarfile.html#command-line-options)

短|長|概要
--|--|----
-l <tarfile>|--list <tarfile>|tarfile 内のファイル一覧を表示します。
-c <tarfile> <source1> ... <sourceN>|--create <tarfile> <source1> ... <sourceN>|ソースファイルから tarfile を作成します。
-e <tarfile> [<output_dir>]|--extract <tarfile> [<output_dir>]|output_dir が指定されていない場合、カレントディレクトリに tarfile を展開します。
-t <tarfile>|--test <tarfile>|tarfile が有効かどうか調べます。
-v|--verbose|詳細も出力します。

## [13.6.4. 使用例](https://docs.python.jp/3/library/tarfile.html#examples)

tar アーカイブから現在のディレクトリにすべて抽出する方法:

import tarfile
tar = tarfile.open("sample.tar.gz")
tar.extractall()
tar.close()

tar アーカイブの一部を、リストの代わりにジェネレーター関数を利用して TarFile.extractall() で展開する方法:

import os
import tarfile

def py_files(members):
    for tarinfo in members:
        if os.path.splitext(tarinfo.name)[1] == ".py":
            yield tarinfo

tar = tarfile.open("sample.tar.gz")
tar.extractall(members=py_files(tar))
tar.close()

非圧縮 tar アーカイブをファイル名のリストから作成する方法:

import tarfile
tar = tarfile.open("sample.tar", "w")
for name in ["foo", "bar", "quux"]:
    tar.add(name)
tar.close()

with 文を利用した同じ例:

import tarfile
with tarfile.open("sample.tar", "w") as tar:
    for name in ["foo", "bar", "quux"]:
        tar.add(name)

gzip 圧縮 tar アーカイブを作成してメンバー情報のいくつかを表示する方法:

import tarfile
tar = tarfile.open("sample.tar.gz", "r:gz")
for tarinfo in tar:
    print(tarinfo.name, "is", tarinfo.size, "bytes in size and is", end="")
    if tarinfo.isreg():
        print("a regular file.")
    elif tarinfo.isdir():
        print("a directory.")
    else:
        print("something else.")
tar.close()

TarFile.add() 関数の filter 引数を利用してユーザー情報をリセットしながらアーカイブを作成する方法:

import tarfile
def reset(tarinfo):
    tarinfo.uid = tarinfo.gid = 0
    tarinfo.uname = tarinfo.gname = "root"
    return tarinfo
tar = tarfile.open("sample.tar.gz", "w:gz")
tar.add("foo", filter=reset)
tar.close()

## [13.6.5. サポートしている tar フォーマット](https://docs.python.jp/3/library/tarfile.html#supported-tar-formats)

> tarfile モジュールは 3 種類の tar フォーマットを作成することができます:

* POSIX.1-1988 ustar format (USTAR_FORMAT). ファイル名の長さは256文字までで、リンク名の長さは100文字までです。最大のファイルサイズは8GiBです。このフォーマットは古くて制限が多いですが、広くサポートされています。

* GNU tar format (GNU_FORMAT). 長いファイル名とリンク名、8GiBを超えるファイルやスパース(sparse)ファイルをサポートしています。これは GNU/Linux システムにおいてデファクト・スタンダードになっています。 tarfile モジュールは長いファイル名を完全にサポートしています。 スパースファイルは読み込みのみサポートしています。

* POSIX.1-2001 pax フォーマット (PAX_FORMAT)。最も柔軟性があり、ほぼ制限が無いフォーマットです。長いファイル名やリンク名、大きいファイルをサポートし、パス名をポータブルな方法で保存します。しかし、現在のところ、すべての tar の実装が pax フォーマットを正しく扱えるわけではありません。  pax フォーマットは既存の ustar フォーマットの拡張です。ustar では保存できない情報を追加のヘッダーを利用して保存します。pax には 2 種類のヘッダーがあります。1 つ目は拡張ヘッダーで、その次のファイルヘッダーに影響します。2 つ目はグローバルヘッダーで、アーカイブ全体に対して有効で、それ以降のすべてのファイルに影響します。すべての pax ヘッダーの内容は、ポータブル性のために UTF-8 で保存されます。

> 他にも、読み込みのみサポートしている tar フォーマットがいくつかあります:

* ancient V7 フォーマット。これは Unix 7th Edition から存在する、最初の tar フォーマットです。通常のファイルとディレクトリのみ保存します。名前は 100 文字を超えてはならず、ユーザー/グループ名に関する情報は保存されません。いくつかのアーカイブは、フィールドが ASCII でない文字を含む場合に、ヘッダーのチェックサムの計算を誤ります。
* SunOS tar 拡張フォーマット。POSIX.1-2001 pax フォーマットの亜流ですが、互換性がありません。

### [13.6.6. Unicode に関する問題](https://docs.python.jp/3/library/tarfile.html#unicode-issues)

> tar フォーマットは、もともとテープドライブにファイルシステムのバックアップをとる目的で設計されました。現在、tarアーカイブはファイルを配布する際に一般的に用いられ、ネットワーク上で交換されています。オリジナルフォーマットが抱える一つの問題は (他の多くのフォーマットでも同じですが)、様々な文字エンコーディングのサポートについて考慮していないことです。例えば、UTF-8 システム上で作成された通常の tar アーカイブは、非 ASCII 文字を含んでいた場合、Latin-1 システムでは正しく読み取ることができません。テキストのメタデータ (ファイル名、リンク名、ユーザー/グループ名など) は破壊されます。残念なことに、アーカイブのエンコーディングを自動検出する方法はありません。pax フォーマットはこの問題を解決するために設計されました。これは非 ASCII メタデータをユニバーサル文字エンコーディング UTF-8 を使用して格納します。

> tarfile における文字変換処理の詳細は TarFile クラスのキーワード引数 encoding および errors によって制御されます。

> encoding はアーカイブのメタデータに使用する文字エンコーディングを指定します。デフォルト値は sys.getfilesystemencoding() で、フォールバックとして 'ascii' が使用されます。アーカイブの読み書き時に、メタデータはそれぞれデコードまたはエンコードしなければなりません。encoding に適切な値が設定されていない場合、その変換は失敗することがあります。

> 引数 errors は文字を変換できない時の扱いを指定します。指定できる値は エラーハンドラ 節を参照してください。デフォルトのスキームは 'surrogateescape' で、Python はそのファイルシステムの呼び出しも使用します。ファイル名、コマンドライン引数、および環境変数 を参照してください。

> PAX_FORMAT アーカイブの場合、メタデータはすべて UTF-8 で格納されるため、encoding は通常指定する必要はありません。encoding は、まれにある、バイナリの pax ヘッダーがデコードされた場合、あるいはサロゲート文字を含む文字列が格納されていた場合に使用されます。

