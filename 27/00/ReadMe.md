# [16.9. getpass — 可搬性のあるパスワード入力機構](https://docs.python.jp/3/library/getpass.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/getpass.py](https://github.com/python/cpython/tree/3.6/Lib/getpass.py)

> getpass モジュールは二つの関数を提供します:

属性|概要
----|----
getpass.getpass(prompt='Password: ', stream=None)|エコーなしでユーザーにパスワードを入力させるプロンプト。ユーザーは prompt の文字列をプロンプトに使え、デフォルトは 'Password: ' です。 Unixではプロンプトはファイルに似たオブジェクト stream へ、必要なら置き換えられたエラーハンドラを使って出力されます。 stream のデフォルトは、制御端末(/dev/tty)か、それが利用できない場合は sys.stderr です (この引数は Windowsでは無視されます)。

### 注釈

> IDLE から getpass を呼び出した場合、入力はIDLEのウィンドウではなく、IDLE を起動したターミナルから行われます。

属性|概要
----|----
exception getpass.GetPassWarning|UserWarning のサブクラスで、入力がエコーされてしまった場合に発生します。
getpass.getuser()|ユーザーの "ログイン名"を返します。

> この関数は環境変数 LOGNAME USER LNAME USERNAME の順序でチェックして、最初の空ではない文字列が設定された値を返します。もし、なにも設定されていない場合は pwd モジュールが提供するシステム上のパスワードデータベースから返します。それ以外は、例外が上がります。

