# [16.12. curses.ascii — ASCII 文字に関するユーティリティ](https://docs.python.jp/3/library/curses.ascii.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> curses.ascii モジュールでは、 ASCII 文字を指す名前定数と、様々な ASCII 文字区分についてある文字が帰属するかどうかを調べる関数を提供します。このモジュールで提供されている定数は以下の制御文字の名前です:

名前|意味
----|----
NUL| 
SOH|ヘディング開始、コンソール割り込み
STX|テキスト開始
ETX|テキスト終了
EOT|テキスト伝送終了
ENQ|問い合わせ、 ACK フロー制御時に使用
ACK|肯定応答
BEL|ベル
BS|一文字後退
TAB|タブ
HT|TAB の別名: "水平タブ"
LF|改行
NL|LF の別名: "改行"
VT|垂直タブ
FF|改頁
CR|復帰
SO|シフトアウト、他の文字セットの開始
SI|シフトイン、標準の文字セットに復帰
DLE|データリンクでのエスケープ
DC1|装置制御 1、フロー制御のための XON
DC2|装置制御 2、ブロックモードフロー制御
DC3|装置制御 3、フロー制御のための XOFF
DC4|装置制御 4
NAK|否定応答
SYN|同期信号
ETB|ブロック転送終了
CAN|キャンセル (Cancel)
EM|媒体終端
SUB|代入文字
ESC|エスケープ文字
FS|ファイル区切り文字
GS|グループ区切り文字
RS|レコード区切り文字、ブロックモード終了子
US|単位区切り文字
SP|空白文字
DEL|削除

> これらの大部分は、最近は実際に定数の意味通りに使われることがほとんどないので注意してください。これらのニーモニック符号はデジタル計算機より前のテレプリンタにおける慣習から付けられたものです。

> このモジュールでは、標準 C ライブラリの関数を雛型とする以下の関数をサポートしています:

属性|概要
----|----
curses.ascii.isalnum(c)|ASCII 英数文字かどうかを調べます; isalpha(c) or isdigit(c) と等価です。
curses.ascii.isalpha(c)|ASCII アルファベット文字かどうかを調べます; isupper(c) or islower(c) と等価です。
curses.ascii.isascii(c)|文字が 7 ビット ASCII 文字に合致するかどうかを調べます。
curses.ascii.isblank(c)|ASCII 余白文字、すなわち空白または水平タブかどうかを調べます。
curses.ascii.iscntrl(c)|ASCII 制御文字 (0x00 から 0x1f の範囲または 0x7f) かどうかを調べます。
curses.ascii.isdigit(c)|ASCII 10 進数字、すなわち '0' から '9' までの文字かどうかを調べます。c in string.digits と等価です。
curses.ascii.isgraph(c)|空白以外の ASCII 印字可能文字かどうかを調べます。
curses.ascii.islower(c)|ASCII 小文字かどうかを調べます。
curses.ascii.isprint(c)|空白文字を含め、ASCII 印字可能文字かどうかを調べます。
curses.ascii.ispunct(c)|空白または英数字以外の ASCII 印字可能文字かどうかを調べます。
curses.ascii.isspace(c)|ASCII 余白文字、すなわち空白、改行、復帰、改頁、水平タブ、垂直タブかどうかを調べます。
curses.ascii.isupper(c)|ASCII 大文字かどうかを調べます。
curses.ascii.isxdigit(c)|ASCII 16 進数字かどうかを調べます。c in string.hexdigits と等価です。
curses.ascii.isctrl(c)|ASCII 制御文字 (0 から 31 までの値) かどうかを調べます。
curses.ascii.ismeta(c)|非 ASCII 文字 (0x80 またはそれ以上の値) かどうかを調べます。

> These functions accept either integers or single-character strings; when the argument is a string, it is first converted using the built-in function ord().

> Note that all these functions check ordinal bit values derived from the character of the string you pass in; they do not actually know anything about the host machine’s character encoding.

> 以下の 2 つの関数は、引数として 1 文字の文字列または整数で表したバイト値のどちらでもとり得ます; これらの関数は引数と同じ型で値を返します。

属性|概要
----|----
curses.ascii.ascii(c)|ASCII 値を返します。c の下位 7 ビットに対応します。
curses.ascii.ctrl(c)|与えた文字に対応する制御文字を返します (0x1f とビット単位で論理積を取ります)。
curses.ascii.alt(c)|与えた文字に対応する 8 ビット文字を返します (0x80 とビット単位で論理和を取ります)。

> 以下の関数は 1 文字からなる文字列値または整数値を引数に取り、文字列を返します。

属性|概要
----|----
curses.ascii.unctrl(c)|ASCII 文字 c の文字列表現を返します。 もし c が印字可能文字であれば、返される文字列は c そのものになります。 もし c が制御文字 (0x00–0x1f) であれば、キャレット ('^') と、その後ろに続く c に対応した大文字からなる文字列になります。 c が ASCII 削除文字 (0x7f) であれば、文字列は '^?' になります。 c のメタビット (0x80) がセットされていれば、メタビットは取り去られ、前述のルールが適用され、'!' が前につけられます。
curses.ascii.controlnames|0 (NUL) から 0x1f (US) までの 32 の ASCII 制御文字と、空白文字 SP のニーモニック符号名からなる 33 要素の文字列によるシーケンスです。

