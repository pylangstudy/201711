# [16.11. curses.textpad — curses プログラムのためのテキスト入力ウィジェット](https://docs.python.jp/3/library/curses.html#module-curses.textpad)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> curses.textpad モジュールでは、curses ウィンドウ内での基本的なテキスト編集を処理し、Emacs に似た (すなわち Netscape Navigator, BBedit 6.x, FrameMaker, その他諸々のプログラムとも似た) キーバインドをサポートしている Textbox クラスを提供します。このモジュールではまた、テキストボックスを枠で囲むなどの目的のために有用な、矩形描画関数を提供しています。

> curses.textpad モジュールでは以下の関数を定義しています:

> curses.textpad.rectangle(win, uly, ulx, lry, lrx)|矩形を描画します。最初の引数はウィンドウオブジェクトでなければなりません; 残りの引数はそのウィンドウからの相対座標になります。2 番目および 3 番目の引数は描画すべき矩形の左上角の y および x 座標です; 4 番目および 5 番目の引数は右下角の y および x 座標です。矩形は、VT100/IBM PC におけるフォーム文字を利用できる端末 (xterm やその他のほとんどのソフトウェア端末エミュレータを含む) ではそれを使って描画されます。そうでなければ ASCII 文字のダッシュ、垂直バー、およびプラス記号で描画されます。

## [16.11.1. Textbox オブジェクト](https://docs.python.jp/3/library/curses.html#textbox-objects)

> 以下のような Textbox オブジェクトをインスタンス生成することができます:

属性|概要
----|----
class curses.textpad.Textbox(win)|Return a textbox widget object. The win argument should be a curses window object in which the textbox is to be contained. The edit cursor of the textbox is initially located at the upper left hand corner of the containing window, with coordinates (0, 0). The instance’s stripspaces flag is initially on.
edit([validator])|普段使うことになるエントリポイントです。終了キーストロークの一つが入力されるまで編集キーストロークを受け付けます。validator を与える場合、関数でなければなりません。validator はキーストロークが入力されるたびにそのキーストロークが引数となって呼び出されます; 返された値に対して、コマンドキーストロークとして解釈が行われます。このメソッドはウィンドウの内容を文字列として返します; ウィンドウ内の空白が含められるかどうかは stripspaces 属性で決められます。
do_command(ch)|単一のコマンドキーストロークを処理します。以下にサポートされている特殊キーストロークを示します:
gather()|ウィンドウの内容を文字列として返します; ウィンドウ内の空白が含められるかどうかは stripspaces メンバ変数で決められます。
stripspaces|この属性はウィンドウ内の空白領域の解釈方法を制御するためのフラグです。フラグがオンに設定されている場合、各行の末端にある空白領域は無視されます; すなわち、末端空白領域にカーソルが入ると、その場所の代わりに行の末尾にカーソルが移動します。また、末端の空白領域はウィンドウの内容を取得する際に剥ぎ取られます。

* do_command(ch)

キーストローク|動作
--------------|----
Control-A|ウィンドウの左端に移動します。
Control-B|カーソルを左へ移動し、必要なら前の行に折り返します。
Control-D|カーソル下の文字を削除します。
Control-E|右端 (stripspaces がオフのとき) または行末 (stripspaces がオンのとき) に移動します。
Control-F|カーソルを右に移動し、必要なら次の行に折り返します。
Control-G|ウィンドウを終了し、その内容を返します。
Control-H|逆方向に文字を削除します。
Control-J|ウィンドウが 1 行であれば終了し、そうでなければ新しい行を挿入します。
Control-K|行が空白行ならその行全体を削除し、そうでなければカーソル以降行末までを消去します。
Control-L|スクリーンを更新します。
Control-N|カーソルを下に移動します; 1 行下に移動します。
Control-O|カーソルの場所に空行を 1 行挿入します。
Control-P|カーソルを上に移動します; 1 行上に移動します。

> 移動操作は、カーソルがウィンドウの縁にあって移動ができない場合には何も行いません。場合によっては、以下のような同義のキーストロークがサポートされています:

定数|キーストローク
----|--------------
KEY_LEFT|Control-B
KEY_RIGHT|Control-F
KEY_UP|Control-P
KEY_DOWN|Control-N
KEY_BACKSPACE|Control-h

> 他のキーストロークは、与えられた文字を挿入し、(行折り返し付きで) 右に移動するコマンドとして扱われます。

