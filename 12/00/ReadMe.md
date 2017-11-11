# [16.1. os — 雑多なオペレーティングシステムインタフェース](https://docs.python.jp/3/library/os.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/secrets.py](https://github.com/python/cpython/tree/3.6/Lib/secrets.py)

## [16.1.4.1. ターミナルのサイズの問い合わせ](https://docs.python.jp/3/library/os.html#querying-the-size-of-a-terminal)

> バージョン 3.3 で追加.

属性|概要
----|----
os.get_terminal_size(fd=STDOUT_FILENO)|ターミナル (端末) のサイズ (columns, lines) を、terminal_size 型のタプルで返します。
class os.terminal_size|ターミナルウィンドウのサイズ (columns, lines) を保持するタプルのサブクラスです。
columns|ターミナルウィンドウの横幅 (文字数) です。
lines|ターミナルウィンドウの高さ (文字数) です。

## [16.1.4.2. ファイル記述子の継承](https://docs.python.jp/3/library/os.html#inheritance-of-file-descriptors)

> バージョン 3.4 で追加.

> ファイル記述子には「継承可能 (inheritable)」フラグというものがあって、これにより子プロセスにファイル記述子が引き継がれるかどうかが決定されます。Python 3.4 より、 Python によって作成されるファイル記述子はデフォルトで継承不可 (non-inheritable) となりました。

> UNIX の場合、継承不可のファイル記述子は新規プロセス実行時にクローズされ、そうでないファイル記述子は引き継がれます。

> Windows の場合は、標準ストリームを除き、継承不可のハンドルと継承不可のファイル記述子は子プロセスでクローズされます。標準ストリーム (ファイル記述子の 0, 1, 2: 標準入力, 標準出力, 標準エラー出力) は常に引き継がれます。 spawn* 関数を使う場合、全ての継承可能なハンドルと全ての継承可能なファイル記述子は引き継がれます。 subprocess モジュールを使う場合、標準ストリームを除く全てのファイル記述子はクローズされ、継承可能なハンドルは close_fds 引数が False の場合にのみ引き継がれます。

属性|概要
----|----
os.get_inheritable(fd)|指定したファイル記述子の「継承可能 (inheritable)」フラグを取得します (boolean)。
os.set_inheritable(fd, inheritable)|指定したファイル記述子の「継承可能 (inheritable)」フラグをセットします。
os.get_handle_inheritable(handle)|指定したハンドルの「継承可能 (inheritable)」フラグを取得します (boolean)。
os.set_handle_inheritable(handle, inheritable)|指定したハンドルの「継承可能 (inheritable)」フラグをセットします。


