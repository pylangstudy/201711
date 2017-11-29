# [16.14. platform — 実行中プラットフォームの固有情報を参照する](https://docs.python.jp/3/library/platform.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/platform.py](https://github.com/python/cpython/tree/3.6/Lib/platform.py)

## [16.14.1. クロスプラットフォーム](https://docs.python.jp/3/library/platform.html#cross-platform)

属性|概要
----|----
platform.architecture(executable=sys.executable, bits='', linkage='')|executable で指定した実行可能ファイル（省略時はPythonインタープリタのバイナリ）の各種アーキテクチャ情報を調べます。
platform.machine()|'i386' のような、機種を返します。不明な場合は空文字列を返します。
platform.node()|コンピュータのネットワーク名を返します。ネットワーク名は完全修飾名とは限りません。不明な場合は空文字列を返します。
platform.platform(aliased=0, terse=0)|実行中プラットフォームを識別する文字列を返します。この文字列には、有益な情報をできるだけ多く付加しています。
platform.processor()|'amdk6' のような、（現実の）プロセッサ名を返します。
platform.python_build()|Pythonのビルド番号と日付を、(buildno, builddate) のタプルで返します。
platform.python_compiler()|Pythonをコンパイルする際に使用したコンパイラを示す文字列を返します。
platform.python_branch()|Python実装のバージョン管理システム上のブランチを特定する文字列を返します。
platform.python_implementation()|Python実装を指定する文字列を返します。戻り値は: 'CPython', 'IronPython', 'Jython', 'PyPy' のいずれかです。
platform.python_revision()|Python実装のバージョン管理システム上のリビジョンを特定する文字列を返します。
platform.python_version()|Python のバージョンを、'major.minor.patchlevel' 形式の文字列で返します。
platform.python_version_tuple()|Pythonのバージョンを、文字列のタプル (major, minor, patchlevel) で返します。
platform.release()|'2.2.0' や 'NT' のような、システムのリリース情報を返します。不明な場合は空文字列を返します。
platform.system()|'Linux', 'Windows', 'Java' のような、システム/OS 名を返します。不明な場合は空文字列を返します。
platform.system_alias(system, release, version)|マーケティング目的で使われる一般的な別名に変換して (system, release, version) を返します。混乱を避けるために、情報を並べなおす場合があります。
platform.version()|'#3 on degas' のような、システムのリリース情報を返します。不明な場合は空文字列を返します。
platform.uname()|極めて可搬性の高い uname インタフェースです。 system, node, release, version, machine, processor の6つの属性を持った namedtuple() を返します。

## [16.14.2. Java プラットフォーム](https://docs.python.jp/3/library/platform.html#java-platform)

属性|概要
----|----
platform.java_ver(release='', vendor='', vminfo=('', '', ''), osinfo=('', '', ''))|Jython用のバージョンインターフェースです。

## [16.14.3. Windows プラットフォーム](https://docs.python.jp/3/library/platform.html#windows-platform)

属性|概要
----|----
platform.win32_ver(release='', version='', csd='', ptype='')|Windows レジストリから追加のバージョン情報を取得して、タプル (release, version, csd, ptype) を返します。それぞれ、OS リリース、バージョン番号、CSD レベル (サービスパック)、OS タイプ (マルチ/シングルプロセッサー) を指しています。

### [16.14.3.1. Win95/98 固有](https://docs.python.jp/3/library/platform.html#win95-98-specific)

属性|概要
----|----
platform.popen(cmd, mode='r', bufsize=-1)|可搬性の高い popen() インターフェースで、可能なら win32pipe.popen() を使用します。 win32pipe.popen() はWindows NTでは利用可能ですが、Windows 9xではハングしてしまいます。

## [16.14.4. Mac OS プラットフォーム](https://docs.python.jp/3/library/platform.html#mac-os-platform)

属性|概要
----|----
platform.mac_ver(release='', versioninfo=('', '', ''), machine='')|Mac OSのバージョン情報を、タプル (release, versioninfo, machine) で返します。versioninfo は、タプル (version, dev_stage, non_release_version) です。

## [16.14.5. Unix プラットフォーム](https://docs.python.jp/3/library/platform.html#unix-platforms)

属性|概要
----|----
platform.dist(distname='', version='', id='', supported_dists=('SuSE', 'debian', 'redhat', 'mandrake', ...))|これは linux_distribution() の別名です。
platform.linux_distribution(distname='', version='', id='', supported_dists=('SuSE', 'debian', 'redhat', 'mandrake', ...), full_distribution_name=1)|OSディストリビューション名の取得を試みます。
platform.libc_ver(executable=sys.executable, lib='', version='', chunksize=2048)|executableで指定したファイル（省略時はPythonインタープリタ）がリンクしているlibcバージョンの取得を試みます。戻り値は文字列のタプル (lib, version) で、不明な項目は引数で指定した値となります。

