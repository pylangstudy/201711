# [16.10. curses — 文字セル表示を扱うための端末操作](https://docs.python.jp/3/library/curses.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> curses モジュールは、可搬性のある高度な端末操作のデファクトスタンダードである、curses ライブラリへのインタフェースを提供します。

> curses が最も広く用いられているのは Unix 環境ですが、Windows、DOS で利用できるバージョンもあり、おそらく他のシステムで利用できるバージョンもあります。この拡張モジュールは Linux および BSD 系の Unixで動作するオープンソースの curses ライブラリである ncurses の API に合致するように設計されています。

> 注釈

> Whenever the documentation mentions a character it can be specified as an integer, a one-character Unicode string or a one-byte byte string.

> Whenever the documentation mentions a character string it can be specified as a Unicode string or a byte string.

> 注釈

> version 5.4 から、ncurses ライブラリは nl_langinfo 関数を利用して非 ASCII データをどう解釈するかを決定するようになりました。これは、アプリケーションは locale.setlocale() 関数を呼び出して、Unicode 文字列をシステムの利用可能なエンコーディングのどれかでエンコードする必要があることを意味します。この例では、システムのデフォルトエンコーディングを利用しています:

import locale
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()

> この後、str.encode() を呼び出すときに code を利用します。

> 参考

モジュール|概要
----------|----
[curses.ascii](https://docs.python.jp/3/library/curses.ascii.html#module-curses.ascii)|ロケール設定に関わらず ASCII 文字を扱うためのユーティリティ。
[curses.panel](https://docs.python.jp/3/library/curses.panel.html#module-curses.panel)|curses ウィンドウにデプス機能を追加するパネルスタック拡張。
[curses.textpad](https://docs.python.jp/3/library/curses.html#module-curses.textpad)|Emacs ライクなキーバインディングをサポートする編集可能な curses 用テキストウィジェット。
[Python で Curses プログラミング](https://docs.python.jp/3/howto/curses.html#curses-howto)|Andrew Kuchling および Eric Raymond によって書かれた、curses を Python で使うためのチュートリアルです。

> Python ソースコードの Tools/demo/ ディレクトリには、このモジュールで提供されている curses バインディングを使ったプログラム例がいくつか収められています。

## [16.10.1. 関数](https://docs.python.jp/3/library/curses.html#functions)

> curses モジュールでは以下の例外を定義しています:

属性|概要
----|----
exception curses.error|curses ライブラリ関数がエラーを返した際に送出される例外です。
curses.baudrate()|端末の出力速度をビット/秒で返します。ソフトウェア端末エミュレータの場合、これは固定の高い値を持つことになります。この関数は歴史的な理由で入れられています; かつては、この関数は時間遅延を生成するための出力ループを書くために用いられたり、行速度に応じてインタフェースを切り替えたりするために用いられたりしていました。
curses.beep()|注意を促す短い音を鳴らします。
curses.can_change_color()|端末に表示される色をプログラマが変更できるか否かによって、True または False を返します。
curses.cbreak()|cbreak モードに入ります。cbreak モード ("rare" モードと呼ばれることもあります) では、通常の tty 行バッファリングはオフにされ、文字を一文字一文字読むことができます。ただし、raw モードとは異なり、特殊文字 (割り込み:interrupt、終了:quit、一時停止:suspend、およびフロー制御) については、tty ドライバおよび呼び出し側のプログラムに対する通常の効果をもっています。まず raw() を呼び出し、次いで cbreak() を呼び出すと、端末を cbreak モードにします。
curses.color_content(color_number)|Return the intensity of the red, green, and blue (RGB) components in the color color_number, which must be between 0 and COLORS. Return a 3-tuple, containing the R,G,B values for the given color, which will be between 0 (no component) and 1000 (maximum amount of component). (カーソルの状態を設定します。 可視性は、不可視、正常、または非常に見えるように、0,1または2に設定できます。 端末が要求された可視性をサポートしている場合は、前のカーソル状態を返します。 それ以外の場合は例外を発生させます。 多くの端末では、「可視」モードはアンダーラインカーソルであり、「非常に目に見える」モードはブロックカーソルである。)
curses.color_pair(color_number)|指定された色の表示テキストにおける属性値を返します。属性値は A_STANDOUT, A_REVERSE 、およびその他の A_* 属性と組み合わせられています。pair_number() はこの関数の逆です。
curses.curs_set(visibility)|Set the cursor state. visibility can be set to 0, 1, or 2, for invisible, normal, or very visible. If the terminal supports the visibility requested, return the previous cursor state; otherwise raise an exception. On many terminals, the "visible" mode is an underline cursor and the "very visible" mode is a block cursor.
curses.def_prog_mode()|現在の端末属性を、稼動中のプログラムが curses を使う際のモードである "プログラム" モードとして保存します。(このモードの反対は、プログラムが curses を使わない "シェル" モードです。) その後 reset_prog_mode() を呼ぶとこのモードを復旧します。
curses.def_shell_mode()|現在の端末属性を、稼動中のプログラムが curses を使っていないときのモードである "シェル" モードとして保存します。(このモードの反対は、プログラムが curses 機能を利用している "プログラム" モードです。) その後 reset_shell_mode() を呼ぶとこのモードを復旧します。
curses.delay_output(ms)|出力に ms ミリ秒の一時停止を入れます。
curses.doupdate()|物理スクリーンを更新します。curses ライブラリは、現在の物理スクリーンの内容と、次の状態として要求されている仮想スクリーンをそれぞれ表す、2 つのデータ構造を保持しています。doupdate() は更新を適用し、物理スクリーンを仮想スクリーンに一致させます。
curses.echo()|echo モードに入ります。echo モードでは、各文字入力はスクリーン上に入力された通りにエコーバックされます。
curses.endwin()|ライブラリの非初期化を行い、端末を通常の状態に戻します。
curses.erasechar()|Return the user’s current erase character as a one-byte bytes object. Under Unix operating systems this is a property of the controlling tty of the curses program, and is not set by the curses library itself. (ユーザーの現在の消去文字を1バイトのバイトオブジェクトとして返します。 Unixオペレーティングシステムの場合、これはcursesプログラムの制御ttyのプロパティであり、cursesライブラリ自体では設定されません。)
curses.filter()|The filter() routine, if used, must be called before initscr() is called. The effect is that, during those calls, LINES is set to 1; the capabilities clear, cup, cud, cud1, cuu1, cuu, vpa are disabled; and the home string is set to the value of cr. The effect is that the cursor is confined to the current line, and so are screen updates. This may be used for enabling character-at-a-time line editing without touching the rest of the screen. (filter（）ルーチンを使用する場合は、initscr（）を呼び出す前に呼び出す必要があります。 結果として、これらの呼び出し中にLINESが1に設定されます。 キュー、cud、cud1、cuu1、cuu、vpaは無効です。 ホーム文字列はcrの値に設定されます。 カーソルが現在の行に限定され、画面の更新が行われるという効果があります。 これは、画面の他の部分に触れることなく、一度に1行の文字を編集できるようにするために使用されます。)
curses.flash()|スクリーンを点滅します。すなわち、画面を色反転して、短時間でもとにもどします。人によっては、beep() で生成される注意音よりも、このような "目に見えるベル" を好みます。
curses.flushinp()|すべての入力バッファをフラッシュします。この関数は、ユーザによってすでに入力されているが、まだプログラムによって処理されていないすべての先行入力文字を破棄します。
curses.getmouse()|After getch() returns KEY_MOUSE to signal a mouse event, this method should be call to retrieve the queued mouse event, represented as a 5-tuple (id, x, y, z, bstate). id is an ID value used to distinguish multiple devices, and x, y, z are the event’s coordinates. (z is currently unused.) bstate is an integer value whose bits will be set to indicate the type of event, and will be the bitwise OR of one or more of the following constants, where n is the button number from 1 to 4: BUTTONn_PRESSED, BUTTONn_RELEASED, BUTTONn_CLICKED, BUTTONn_DOUBLE_CLICKED, BUTTONn_TRIPLE_CLICKED, BUTTON_SHIFT, BUTTON_CTRL, BUTTON_ALT. (getch（）はマウスイベントを通知するためにKEY_MOUSEを返した後、このメソッドは5タプル（id、x、y、z、bstate）で表される、キューに入れられたマウスイベントを取得するために呼び出されます。 idは複数のデバイスを区別するためのID値で、x、y、zはイベントの座標です。 （zは現在使用されていません）bstateは、イベントのタイプを示すビットが設定され、次の定数の1つ以上のビット単位の論理和になります。nは1〜4のボタン番号です。 BUTTONn_PRESSED、BUTTONn_RELEASED、BUTTONn_CLICKED、BUTTONn_DOUBLE_CLICKED、BUTTONn_TRIPLE_CLICKED、BUTTON_SHIFT、BUTTON_CTRL、BUTTON_ALT。)
curses.getsyx()|Return the current coordinates of the virtual screen cursor as a tuple (y, x). If leaveok is currently True, then return (-1, -1). (仮想スクリーンカーソルの現在の座標をタプル（y、x）として返します。 leaveokが現在Trueなら、（-1、-1）を返します。)
curses.getwin(file)|以前の putwin() 呼び出しでファイルに保存されている、ウィンドウ関連データを読み出します。次に、このルーチンはそのデータを使って新たなウィンドウを生成し初期化して、その新規ウィンドウオブジェクトを返します。
curses.has_colors()|端末が色表示を行える場合には True を返します。そうでない場合には False を返します。
curses.has_ic()|端末が文字の挿入/削除機能を持つ場合に True を返します。最近の端末エミュレータはどれもこの機能を持っており、この関数は歴史的な理由のためだけに存在しています。
curses.has_il()|端末が行の挿入/削除機能を持つ場合に True を返します。最近の端末エミュレータはどれもこの機能を持っていて、この関数は歴史的な理由のためだけに存在しています。
curses.has_key(ch)|キー値 ch をとり、現在の端末タイプがその値のキーを認識できる場合に True を返します。
curses.halfdelay(tenths)|Used for half-delay mode, which is similar to cbreak mode in that characters typed by the user are immediately available to the program. However, after blocking for tenths tenths of seconds, raise an exception if nothing has been typed. The value of tenths must be a number between 1 and 255. Use nocbreak() to leave half-delay mode.(ハーフディレイモードに使用されます。これは、ユーザが入力した文字がプログラムですぐに使用できる点で、cbreakモードに似ています。 ただし、10分の1秒間ブロックした後は、何も入力されていなければ例外が発生します。 10分の1の値は、1〜255の数値でなければなりません。nocbreak（）を使用して、半遅延モードを終了します。)
curses.init_color(color_number, r, g, b)|Change the definition of a color, taking the number of the color to be changed followed by three RGB values (for the amounts of red, green, and blue components). The value of color_number must be between 0 and COLORS. Each of r, g, b, must be a value between 0 and 1000. When init_color() is used, all occurrences of that color on the screen immediately change to the new definition. This function is a no-op on most terminals; it is active only if can_change_color() returns True.(色の定義を変更し、変更する色の番号に3つのRGB値（赤、緑、青の成分の量）を加えます。 color_numberの値は、0とCOLORSの間でなければなりません。 r、g、bはそれぞれ0から1000の間の値でなければなりません。init_color（）が使用されると、画面上のその色のすべての出現が直ちに新しい定義に変わります。 この機能はほとんどの端末では動作しません。 can_change_color（）がTrueを返す場合にのみアクティブになります。)
curses.init_pair(pair_number, fg, bg)|色ペアの定義を変更します。3 つの引数: 変更したい色ペア、前景色の色番号、背景色の色番号、をとります。pair_number は 1 から COLOR_PAIRS -1 の間でなければなりません (0 色ペアは黒色背景に白色前景となるように設定されており、変更することができません)。fg および bg 引数は 0 と COLORS の間でなければなりません。色ペアが以前に初期化されていれば、スクリーンを更新して、指定された色ペアの部分を新たな設定に変更します。
curses.initscr()|Initialize the library. Return a window object which represents the whole screen.(ライブラリを初期化します。 画面全体を表すウィンドウオブジェクトを返します。)
curses.is_term_resized(nlines, ncols)|resize_term() によってウィンドウ構造が変更されている場合に True を、そうでない場合は False を返します。
curses.isendwin()|endwin() がすでに呼び出されている (すなわち、curses ライブラリが非初期化されてしまっている) 場合に True を返します。
curses.keyname(k)|Return the name of the key numbered k as a bytes object. The name of a key generating printable ASCII character is the key’s character. The name of a control-key combination is a two-byte bytes object consisting of a caret (b'^') followed by the corresponding printable ASCII character. The name of an alt-key combination (128–255) is a bytes object consisting of the prefix b'M-' followed by the name of the corresponding ASCII character.(kという番号のキーの名前をバイトオブジェクトとして返します。 印刷可能なASCII文字を生成するキーの名前がキーの文字です。 コントロールキーの組み合わせの名前は、対応する印字可能なASCII文字が続くキャレット（b '^'）で構成される2バイトのバイトオブジェクトです。 altキーの組み合わせ（128-255）の名前は、接頭辞b'M- 'とそれに続く対応するASCII文字の名前で構成されたバイトオブジェクトです。)
curses.killchar()|Return the user’s current line kill character as a one-byte bytes object. Under Unix operating systems this is a property of the controlling tty of the curses program, and is not set by the curses library itself.(ユーザーの現在の行削除文字を1バイトのバイトオブジェクトとして返します。 Unixオペレーティングシステムの場合、これはcursesプログラムの制御ttyのプロパティであり、cursesライブラリ自体では設定されません。)
curses.longname()|Return a bytes object containing the terminfo long name field describing the current terminal. The maximum length of a verbose description is 128 characters. It is defined only after the call to initscr().(現在のターミナルを記述するterminfo long nameフィールドを含むbytesオブジェクトを返します。 冗長な記述の最大長は128文字です。 initscr（）の呼び出しの後でのみ定義されます。)
curses.meta(flag)|If flag is True, allow 8-bit characters to be input. If flag is False, allow only 7-bit chars.(flagがTrueの場合は、8ビット文字を入力します。 flagがFalseの場合、7ビットの文字のみを許可します。)
curses.mouseinterval(interval)|ボタンが押されてから離されるまでの時間をマウスクリック一回として認識する最大の時間間隔をミリ秒で設定します。返り値は以前の内部設定値になります。デフォルトは 200 ミリ秒 (5 分の 1 秒) です。
curses.mousemask(mousemask)|Set the mouse events to be reported, and return a tuple (availmask, oldmask). availmask indicates which of the specified mouse events can be reported; on complete failure it returns 0. oldmask is the previous value of the given window’s mouse event mask. If this function is never called, no mouse events are ever reported.(報告されるマウスイベントを設定し、タプル（availmask、oldmask）を返します。 availmaskは、指定されたマウスイベントのどれを報告できるかを示します。 完全な失敗時には0を返します。oldmaskは、指定されたウィンドウのマウスイベントマスクの以前の値です。 この関数が呼び出されない場合、マウスイベントは一度も報告されません。)
curses.napms(ms)|ms ミリ秒間スリープします。
curses.newpad(nlines, ncols)|Create and return a pointer to a new pad data structure with the given number of lines and columns. Return a pad as a window object.(指定された数の行と列を持つ新しいパッドデータ構造体へのポインタを作成して返します。 パッドをウィンドウオブジェクトとして返します。)
curses.newwin(nlines, ncols), curses.newwin(nlines, ncols, begin_y, begin_x)|Return a new window, whose left-upper corner is at (begin_y, begin_x), and whose height/width is nlines/ncols.(指定された数の行と列を持つ新しいパッドデータ構造体へのポインタを作成して返します。 パッドをウィンドウオブジェクトとして返します。
curses.newwin（nlines、ncols）、curses.newwin（nlines、ncols、begin_y、begin_x）|左上隅が（begin_y、begin_x）にあり、高さ/幅がnlines / ncolsである新しいウィンドウを返します。) デフォルトでは、ウィンドウは指定された位置からスクリーンの右下まで広がります。
curses.nl()|newlime モードに入ります。このモードはリターンキーを入力中の改行として変換し、出力時に改行文字を復帰 (return) と改行 (line-feed) に変換します。newline モードは初期化時にはオンになっています。
curses.nocbreak()|cbreak モードを終了します。行バッファリングを行う通常の "cooked" モードに戻ります。
curses.noecho()|echo モードを終了します。入力のエコーバックはオフにされます。
curses.nonl()|newline モードを終了します。入力時のリターンキーから改行への変換、および出力時の改行から復帰/改行への低レベル変換を無効化します (ただし、addch('\n') の振る舞いは変更せず、仮想スクリーン上では常に復帰と改行に等しくなります)。変換をオフにすることで、curses は水平方向の動きを少しだけ高速化できることがあります; また、入力中のリターンキーの検出ができるようになります。
curses.noqiflush()|When the noqiflush() routine is used, normal flush of input and output queues associated with the INTR, QUIT and SUSP characters will not be done. You may want to call noqiflush() in a signal handler if you want output to continue as though the interrupt had not occurred, after the handler exits.(noqiflush（）ルーチンを使用すると、INTR、QUITおよびSUSP文字に関連付けられた入出力キューの通常のフラッシュは実行されません。 ハンドラが終了した後も、割り込みが発生していないかのように出力を続けるには、シグナルハンドラでnoqiflush（）を呼び出すとよいでしょう。)
curses.noraw()|raw モードから離れます。行バッファリングを行う通常の "cooked" モードに戻ります。
curses.pair_content(pair_number)|要求された色ペアの色を含むタプル (fg, bg) を返します。pair_number は 1 から COLOR_PAIRS - 1 の間でなければなりません。
curses.pair_number(attr)|attr に対する色ペアセットの番号を返します。color_pair() はこの関数の逆に相当します。
curses.putp(str)|tputs(str, 1, putchar) と等価です; 現在の端末における、指定された terminfo 機能の値を出力します。putp() の出力は常に標準出力に送られるので注意して下さい。
curses.qiflush([flag])|flag が False なら、noqiflush() を呼ぶのとと同じ効果です。flag が True か、引数が与えられていない場合、制御文字が読み出された最にキューはフラッシュされます。
curses.raw()|raw モードに入ります。raw モードでは、通常の行バッファリングと割り込み (interrupt)、終了 (quit)、一時停止 (suspend)、およびフロー制御キーはオフになります; 文字は curses 入力関数に一文字づつ渡されます。
curses.reset_prog_mode()|端末を "program" モードに復旧し、あらかじめ def_prog_mode() で保存した内容に戻します。
curses.reset_shell_mode()|端末を "shell" モードに復旧し、あらかじめ def_shell_mode() で保存した内容に戻します。
curses.resetty()|端末モードの状態を最後に savetty() を呼び出した時の状態に戻します。
curses.resize_term(nlines, ncols)|Backend function used by resizeterm(), performing most of the work; when resizing the windows, resize_term() blank-fills the areas that are extended. The calling application should fill in these areas with appropriate data. The resize_term() function attempts to resize all windows. However, due to the calling convention of pads, it is not possible to resize these without additional interaction with the application.(resizeterm（）が使用するバックエンド関数で、ほとんどの作業を実行します。 ウィンドウのサイズを変更すると、resize_term（）は拡張された領域を空白で埋めます。 呼び出し元のアプリケーションは、これらの領域に適切なデータを入力する必要があります。 resize_term（）関数はすべてのウィンドウのサイズを変更しようとします。 ただし、パッドの呼び出し規約のために、アプリケーションとの追加の対話なしにこれらのサイズを変更することはできません。)
curses.resizeterm(nlines, ncols)|現在の標準ウィンドウのサイズを指定された寸法に変更し、curses ライブラリが使用する、その他のウィンドウサイズを記憶しているデータ (特に SIGWINCH ハンドラ) を調整します。
curses.savetty()|resetty() で使用される、バッファ内の端末モードの現在の状態を保存します。
curses.setsyx(y, x)|Set the virtual screen cursor to y, x. If y and x are both -1, then leaveok is set True.(仮想スクリーンカーソルをy、xに設定します。 yとxが両方とも-1の場合、leaveokがTrueに設定されます。)
curses.setupterm(term=None, fd=-1)|Initialize the terminal. term is a string giving the terminal name, or None; if omitted or None, the value of the TERM environment variable will be used. fd is the file descriptor to which any initialization sequences will be sent; if not supplied or -1, the file descriptor for sys.stdout will be used.(端末を初期化します。 termは、端末名を指定する文字列です。 省略するかNoneを指定すると、TERM環境変数の値が使用されます。 fdは、初期化シーケンスが送信されるファイル記述子です。 指定されていない場合、または-1の場合、sys.stdoutのファイル記述子が使用されます。)
curses.start_color()|プログラマがカラーを利用したい場合で、かつ他の何らかのカラー操作ルーチンを呼び出す前に呼び出さなくてはなりません。この関数は initscr() を呼んだ直後に呼ぶようにしておくとよいでしょう。
curses.termattrs()|端末がサポートするすべてのビデオ属性を論理和した値を返します。この情報は、curses プログラムがスクリーンの見え方を完全に制御する必要がある場合に便利です。
curses.termname()|Return the value of the environment variable TERM, as a bytes object, truncated to 14 characters.(環境変数TERMの値をバイトオブジェクトとして14文字に切り捨てて返します。)
curses.tigetflag(capname)|Return the value of the Boolean capability corresponding to the terminfo capability name capname as an integer. Return the value -1 if capname is not a Boolean capability, or 0 if it is canceled or absent from the terminal description.(terminfo機能名capnameに対応する論理機能の値を整数として返します。 capnameがブール値でない場合は-1を、そうでない場合は0を返します。)
curses.tigetnum(capname)|Return the value of the numeric capability corresponding to the terminfo capability name capname as an integer. Return the value -2 if capname is not a numeric capability, or -1 if it is canceled or absent from the terminal description.(terminfo機能名capnameに対応する数値機能の値を整数として返します。 capnameが数値ケーパビリティでない場合は-2を返し、それがキャンセルされた場合や端末の説明にない場合は-1を返します。)
curses.tigetstr(capname)|Return the value of the string capability corresponding to the terminfo capability name capname as a bytes object. Return None if capname is not a terminfo "string capability", or is canceled or absent from the terminal description.(terminfo機能名capnameに対応する文字列機能の値をバイトオブジェクトとして返します。 capnameがterminfo "文字列機能"でない場合、または端末記述から取り消された場合、または存在しない場合は、Noneを返します。)
curses.tparm(str[, ...])|Instantiate the bytes object str with the supplied parameters, where str should be a parameterized string obtained from the terminfo database. E.g. tparm(tigetstr("cup"), 5, 3) could result in b'\033[6;4H', the exact result depending on terminal type.(指定されたパラメータでbytesオブジェクトstrをインスタンス化します。strは、terminfoデータベースから取得したパラメータ化された文字列でなければなりません。 例えば。 tparm（tigetstr（ "cup"）、5,3）はb '\ 033 [6; 4H'、端末のタイプに応じた正確な結果になります。)
curses.typeahead(fd)|先読みチェックに使うためのファイル記述子 fd を指定します。fd が -1 の場合、先読みチェックは行われません。
curses.unctrl(ch)|Return a bytes object which is a printable representation of the character ch. Control characters are represented as a caret followed by the character, for example as b'^C'. Printing characters are left as they are.(文字chの印刷可能な表現であるbytesオブジェクトを返します。 制御文字は、文字が続くキャレット、たとえばb '^ C'で表されます。 印刷文字はそのまま残します。)
curses.ungetch(ch)|Push ch so the next getch() will return it.(chchを押すと、次のgetch（）がそれを返します。)
curses.update_lines_cols()|LINES と COLS についての更新。マニュアルでスクリーンのサイズを変更したことを検知するために有用です。
curses.unget_wch(ch)|Push ch so the next get_wch() will return it.(次のget_wch（）が返すようにchをプッシュします。)
curses.ungetmouse(id, x, y, z, bstate)|与えられた状態データが関連付けられた KEY_MOUSE イベントを入力キューにプッシュします。
curses.use_env(flag)|この関数を使う場合、initscr() または newterm を呼ぶ前に呼び出さなくてはなりません。flag が False の場合、環境変数 LINES および COLUMNS の値 (デフォルトで使用されます) の値が設定されていたり、curses がウィンドウ内で動作して (この場合 LINES や COLUMNS が設定されていないとウィンドウのサイズを使います) いても、terminfo データベースに指定された lines および columns の値を使います。
curses.use_default_colors()|Allow use of default values for colors on terminals supporting this feature. Use this to support transparency in your application. The default color is assigned to the color number -1. After calling this function, init_pair(x, curses.COLOR_RED, -1) initializes, for instance, color pair x to a red foreground color on the default background.(この機能をサポートする端末の色にデフォルト値を使用できるようにします。 これを使用して、アプリケーションの透過性をサポートします。 デフォルトの色は、色番号-1に割り当てられます。 この関数を呼び出した後、init_pair（x、curses.COLOR_RED、-1）は、デフォルトのバックグラウンドで例えばxの色を赤の前景色に初期化します。)
curses.wrapper(func, ...)|Initialize curses and call another callable object, func, which should be the rest of your curses-using application. If the application raises an exception, this function will restore the terminal to a sane state before re-raising the exception and generating a traceback. The callable object func is then passed the main window 'stdscr' as its first argument, followed by any other arguments passed to wrapper(). Before calling func, wrapper() turns on cbreak mode, turns off echo, enables the terminal keypad, and initializes colors if the terminal has color support. On exit (whether normally or by exception) it restores cooked mode, turns on echo, and disables the terminal keypad. (cursesを初期化し、cursesを使用するアプリケーションの残りの部分である別の呼び出し可能なオブジェクトfuncを呼び出します。 アプリケーションが例外を発生させた場合、この関数は、例外を再発生させてトレースバックを生成する前に、端末を正常な状態に戻します。 呼び出し可能オブジェクトfuncは、最初の引数としてメインウィンドウ 'stdscr'に渡され、その後にwrapper（）に渡される他の引数が続きます。 funcを呼び出す前に、ラッパー（）はcbreakモードをオンにし、エコーをオフにし、ターミナルキーパッドを有効にし、ターミナルがカラーをサポートしていればカラーを初期化します。 終了時（通常か例外かにかかわらず）、cookedモードを復元し、エコーをオンにし、ターミナルキーパッドを無効にします。)

## [16.10.2. Window オブジェクト](https://docs.python.jp/3/library/curses.html#window-objects)

> 上記の initscr() や newwin() が返すウィンドウは、以下のメソッドと属性を持ちます:

属性|概要
----|----
window.addch(ch[, attr]), window.addch(y, x, ch[, attr])|(y, x) にある文字 ch を属性 attr で描画します。このときその場所に以前描画された文字は上書きされます。デフォルトでは、文字の位置および属性はウィンドウオブジェクトにおける現在の設定になります。
window.addnstr(str, n[, attr]), window.addnstr(y, x, str, n[, attr])|Paint at most n characters of the character string str at (y, x) with attributes attr, overwriting anything previously on the display.
window.addstr(str[, attr]), window.addstr(y, x, str[, attr])|Paint the character string str at (y, x) with attributes attr, overwriting anything previously on the display.
window.attroff(attr)|現在のウィンドウに書き込まれたすべての内容に対し "バックグラウンド" に設定された属性 attr を除去します。
window.attron(attr)|現在のウィンドウに書き込まれたすべての内容に対し "バックグラウンド" に属性 attr を追加します。
window.attrset(attr)|Set the "background" set of attributes to attr. This set is initially 0 (no attributes).
window.bkgd(ch[, attr])|ウィンドウ上の背景プロパティを、attr を属性とする文字 ch に設定します。変更はそのウィンドウ中のすべての文字に以下のようにして適用されます:|    ウィンドウ中のすべての文字の属性が新たな背景属性に変更されます。以前の背景文字が出現すると、常に新たな背景文字に変更されます。
window.bkgdset(ch[, attr])|ウィンドウの背景を設定します。ウィンドウの背景は、文字と何らかの属性の組み合わせから成り立ちます。背景情報の属性の部分は、ウィンドウ上に描画されている空白でないすべての文字と組み合わされ (OR され) ます。空白文字には文字部分と属性部分の両方が組み合わされます。背景は文字のプロパティとなり、スクロールや行/文字の挿入/削除操作の際には文字と一緒に移動します。
window.border([ls[, rs[, ts[, bs[, tl[, tr[, bl[, br]]]]]]]])|Draw a border around the edges of the window. Each parameter specifies the character to use for a specific part of the border; see the table below for more details.|注釈|どの引数も、0 を指定した場合デフォルトの文字が使われるようになります。キーワード引数は使うことが できません。デフォルトはテーブル内で示しています:
window.box([vertch, horch])|border() と同様ですが、ls および rs は共に vertch で、ts および bs は共に horch です。この関数では、角に使われるデフォルト文字が常に使用されます。
window.chgat(attr), window.chgat(num, attr), window.chgat(y, x, attr), window.chgat(y, x, num, attr)|Set the attributes of num characters at the current cursor position, or at position (y, x) if supplied. If num is not given or is -1, the attribute will be set on all the characters to the end of the line. This function does not move the cursor. The changed line will be touched using the touchline() method so that the contents will be redisplayed by the next window refresh. (現在のカーソル位置または指定された位置（y、x）のnum文字の属性を設定します。 numが指定されていないか-1である場合、属性は行末までのすべての文字に設定されます。 この機能はカーソルを移動しません。 変更された行はtouchline（）メソッドを使用してタッチされ、次のウィンドウの更新時に内容が再表示されます。)
window.clear()|erase() に似ていますが、次に refresh() が呼び出された際にすべてのウィンドウを再描画するようにします。
window.clearok(flag)|If flag is True, the next call to refresh() will clear the window completely.
window.clrtobot()|カーソルの位置からウィンドウの端までを消去します: カーソル以降のすべての行が削除されるため、clrtoeol() と等価です。
window.clrtoeol()|カーソル位置から行末までを消去します。
window.cursyncup()|ウィンドウのすべての親ウィンドウについて、現在のカーソル位置を反映するよう更新します。
window.delch([y, x])|(y, x) にある文字を削除します。
window.deleteln()|カーソルの下にある行を削除します。後続の行はすべて 1 行上に移動します。
window.derwin(begin_y, begin_x), window.derwin(nlines, ncols, begin_y, begin_x)|"derive window (ウィンドウを派生する)" の短縮形です。derwin() は subwin() と同じですが、begin_y および begin_x はスクリーン全体の原点ではなく、ウィンドウの原点からの相対位置です。派生したウィンドウオブジェクトが返されます。
window.echochar(ch[, attr])|文字 ch に属性 attr を付与し、即座に refresh() をウィンドウに対して呼び出します。
window.enclose(y, x)|与えられた文字セル座標をスクリーン原点から相対的なものとし、ウィンドウの中に含まれるかを調べて、True または False を返します。スクリーン上のウィンドウの一部がマウスイベントの発生場所を含むかどうかを調べる上で便利です。
window.encoding|encode メソッドの引数 (Unicode 文字列および文字) で使用されるエンコーディングです。例えば window.subwin() などでサブウィンドウを生成した時、エンコーディング属性は親ウィンドウから継承します。デフォルトでは、そのロケールのエンコーディングが使用されます (locale.getpreferredencoding() 参照)。|バージョン 3.3 で追加.
window.erase()|ウィンドウをクリアします。
window.getbegyx()|左上の角の座標をあらわすタプル (y, x) を返します。
window.getbkgd()|与えられたウィンドウの現在の背景文字と属性のペアを返します。
window.getch([y, x])|Get a character. Note that the integer returned does not have to be in ASCII range: function keys, keypad keys and so on are represented by numbers higher than 255. In no-delay mode, return -1 if there is no input, otherwise wait until a key is pressed.(文字を取得します。 返される整数は、ASCIIの範囲である必要はないことに注意してください。ファンクションキー、キーパッドキーなどは255より大きい数字で表されます。遅延なしモードでは、入力がない場合は-1を返し、そうでない場合はキー が押された。)
window.get_wch([y, x])|Get a wide character. Return a character for most keys, or an integer for function keys, keypad keys, and other special keys. In no-delay mode, raise an exception if there is no input. (ワイド文字を取得します。 ほとんどのキーの場合は文字を返し、ファンクションキー、キーパッドキー、その他の特殊キーの場合は整数を返します。 無遅延モードでは、入力がない場合に例外を発生させます。)
window.getkey([y, x])|Get a character, returning a string instead of an integer, as getch() does. Function keys, keypad keys and other special keys return a multibyte string containing the key name. In no-delay mode, raise an exception if there is no input. (getch（）のように、文字の代わりに整数の代わりに文字列を返します。 ファンクションキー、キーパッドキー、およびその他の特殊キーは、キー名を含むマルチバイト文字列を返します。 無遅延モードでは、入力がない場合に例外を発生させます。)
window.getmaxyx()|ウィンドウの高さおよび幅を表すタプル (y, x) を返します。
window.getparyx()|Return the beginning coordinates of this window relative to its parent window as a tuple (y, x). Return (-1, -1) if this window has no parent. (タプル（y、x）として親ウィンドウを基準にしたこのウィンドウの開始座標を返します。 このウィンドウに親がない場合は（-1、-1）を返します。)
window.getstr(), window.getstr(n), window.getstr(y, x), window.getstr(y, x, n)|Read a bytes object from the user, with primitive line editing capacity. (基本的な行編集機能を使用して、バイトオブジェクトをユーザーから読み取ります。)
window.getyx()|ウィンドウの左上角からの相対で表した現在のカーソル位置をタプル (y, x) で返します。
window.hline(ch, n), window.hline(y, x, ch, n)|(y, x) から始まり、n の長さを持つ、文字 ch で作られる水平線を表示します。
window.idcok(flag)|flag が False の場合、curses は端末のハードウェアによる文字挿入/削除機能を使おうとしなくなります; flag が True ならば、文字挿入/削除は有効にされます。curses が最初に初期化された際には文字挿入/削除はデフォルトで有効になっています。
window.idlok(flag)|If flag is True, curses will try and use hardware line editing facilities. Otherwise, line insertion/deletion are disabled. (flagがTrueの場合、cursesはハードウェア行編集機能を使用します。 それ以外の場合、行の挿入/削除は無効になります。)
window.immedok(flag)|flag が True ならば、ウィンドウイメージ内における何らかの変更があるとウィンドウを更新するようになります; すなわち、refresh() を自分で呼ばなくても良くなります。とはいえ、wrefresh を繰り返し呼び出すことになるため、この操作はかなりパフォーマンスを低下させます。デフォルトでは無効になっています。
window.inch([y, x])|ウィンドウの指定の位置の文字を返します。下位 8 ビットが本来の文字で、それより上のビットは属性です。
window.insch(ch[, attr]), window.insch(y, x, ch[, attr])|(y, x) に文字 ch を属性 attr で描画し、行の x からの内容を 1 文字分右にずらします。
window.insdelln(nlines)|nlines 行を指定されたウィンドウの現在の行の上に挿入します。その下にある nlines 行は失われます。負の nlines を指定すると、カーソルのある行以降の nlines を削除し、削除された行の後ろに続く内容が上に来ます。その下にある nlines は消去されます。現在のカーソル位置はそのままです。
window.insertln()|カーソルの下に空行を 1 行入れます。それ以降の行は 1 行づつ下に移動します。
window.insnstr(str, n[, attr]), window.insnstr(y, x, str, n[, attr])|文字列をカーソルの下にある文字の前に (一行に収まるだけ) 最大 n 文字挿入します。n がゼロまたは負の値の場合、文字列全体が挿入されます。カーソルの右にあるすべての文字は右に移動し、行の左端にある文字は失われます。カーソル位置は (y, x が指定されていた場合はそこに移動しますが、その後は) 変化しません。
window.insstr(str[, attr]), window.insstr(y, x, str[, attr])|キャラクタ文字列を (行に収まるだけ) カーソルより前に挿入します。カーソルの右側にある文字はすべて右にシフトし、行の右端の文字は失われます。カーソル位置は (y, x が指定されていた場合はそこに移動しますが、その後は) 変化しません。
window.instr([n]), window.instr(y, x[, n])|Return a bytes object of characters, extracted from the window starting at the current cursor position, or at y, x if specified. Attributes are stripped from the characters. If n is specified, instr() returns a string at most n characters long (exclusive of the trailing NUL). (現在のカーソル位置から始まるウィンドウ、または指定されている場合はy、xで抽出されたバイトオブジェクトの文字を返します。 属性は文字から取り除かれます。 nが指定された場合、instr（）は最大でn文字（NULを除く）の文字列を返します。)
window.is_linetouched(line)|指定した行が、最後に refresh() を呼んだ時から変更されている場合に True を返します; そうでない場合には False を返します。line が現在のウィンドウ上の有効な行でない場合、curses.error 例外を送出します。
window.is_wintouched()|指定したウィンドウが、最後に refresh() を呼んだ時から変更されている場合に True を返します; そうでない場合には False を返します。
window.keypad(flag)|If flag is True, escape sequences generated by some keys (keypad, function keys) will be interpreted by curses. If flag is False, escape sequences will be left as is in the input stream. (flagがTrueの場合、一部のキー（キーパッド、ファンクションキー）によって生成されるエスケープシーケンスはcursesによって解釈されます。 flagがFalseの場合、エスケープシーケンスはそのまま入力ストリームに残されます。)
window.leaveok(flag)|If flag is True, cursor is left where it is on update, instead of being at "cursor position." This reduces cursor movement where possible. If possible the cursor will be made invisible.|If flag is False, cursor will always be at "cursor position" after an update. (flagがTrueの場合、カーソルは「カーソル位置」にあるのではなく、更新時の位置に残されます。 これにより、カーソルの移動が可能な限り少なくなります。 可能であれば、カーソルは非表示になります。| flagがFalseの場合、更新後カーソルは常に「カーソル位置」になります。)
window.move(new_y, new_x)|カーソルを (new_y, new_x) に移動します。
window.mvderwin(y, x)|ウィンドウを親ウィンドウの中で移動します。ウィンドウのスクリーン相対となるパラメタ群は変化しません。このルーチンは親ウィンドウの一部をスクリーン上の同じ物理位置に表示する際に用いられます。
window.mvwin(new_y, new_x)|ウィンドウの左上角が (new_y, new_x) になるように移動します。
window.nodelay(flag)|If flag is True, getch() will be non-blocking. (flagがTrueの場合、getch（）は非ブロック化されます。)
window.notimeout(flag)|If flag is True, escape sequences will not be timed out.|If flag is False, after a few milliseconds, an escape sequence will not be interpreted, and will be left in the input stream as is. (flagがTrueの場合、エスケープシーケンスはタイムアウトしません。| flagがFalseの場合、数ミリ秒後にエスケープシーケンスは解釈されず、そのまま入力ストリームに残されます。)
window.noutrefresh()|更新をマークはしますが待機します。この関数はウィンドウのデータ構造を表現したい内容を反映するように更新しますが、物理スクリーン上に反映させるための強制更新を行いません。更新を行うためには doupdate() を呼び出します。
window.overlay(destwin[, sminrow, smincol, dminrow, dmincol, dmaxrow, dmaxcol])|ウィンドウを destwin の上に重ね書き (overlay) します。ウィンドウは同じサイズである必要はなく、重なっている領域だけが複写されます。この複写は非破壊的です。これは現在の背景文字が destwin の内容を上書きしないことを意味します。|複写領域をきめ細かく制御するために、overlay() の第二形式を使うことができます。sminrow および smincol は元のウィンドウの左上の座標で、他の変数は destwin 内の矩形を表します。
window.overwrite(destwin[, sminrow, smincol, dminrow, dmincol, dmaxrow, dmaxcol])|destwin の上にウィンドウの内容を上書き (overwrite) します。ウィンドウは同じサイズである必要はなく、重なっている領域だけが複写されます。この複写は破壊的です。これは現在の背景文字が destwin の内容を上書きすることを意味します。|複写領域をきめ細かく制御するために、overwrite() の第二形式を使うことができます。sminrow および smincol は元のウィンドウの左上の座標で、他の変数は destwin 内の矩形を表します。
window.putwin(file)|ウィンドウに関連付けられているすべてのデータを与えられたファイルオブジェクトに書き込みます。この情報は後に getwin() 関数を使って取得することができます。
window.redrawln(beg, num)|beg 行から始まる num スクリーン行の表示内容が壊れており、次の refresh() 呼び出しで完全に再描画されなければならないことを通知します。
window.redrawwin()|ウィンドウ全体を更新 (touch) し、次の refresh() 呼び出しで完全に再描画されるようにします。
window.refresh([pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol])|ディスプレイを即時更新し (実際のウィンドウとこれまでの描画/削除メソッドの内容とを同期し) ます。|6 つのオプション引数はウィンドウが newpad() で生成された場合にのみ指定することができます。追加の引数はパッドやスクリーンのどの部分が含まれるのかを示すために必要です。pminrow および pmincol にはパッドが表示されている矩形の左上角を指定します。sminrow, smincol, smaxrow, および smaxcol には、スクリーン上に表示される矩形の縁を指定します。パッド内に表示される矩形の右下角はスクリーン座標から計算されるので、矩形は同じサイズでなければなりません。矩形は両方とも、それぞれのウィンドウ構造内に完全に含まれていなければなりません。pminrow, pmincol, sminrow, または smincol に負の値を指定すると、ゼロを指定したものとして扱われます。
window.resize(nlines, ncols)|curses ウィンドウの記憶域を、指定値のサイズに調整するため再割当てします。サイズが現在の値より大きい場合、ウィンドウのデータは現在の背景設定 (bkgdset() で設定) で埋められマージされます。
window.scroll([lines=1])|スクリーンまたはスクロール領域を上に lines 行スクロールします。
window.scrollok(flag)|Control what happens when the cursor of a window is moved off the edge of the window or scrolling region, either as a result of a newline action on the bottom line, or typing the last character of the last line. If flag is False, the cursor is left on the bottom line. If flag is True, the window is scrolled up one line. Note that in order to get the physical scrolling effect on the terminal, it is also necessary to call idlok(). (一番下の行の改行アクションの結果として、または最後の行の最後の文字を入力することで、ウィンドウのカーソルがウィンドウの端またはスクロール領域から移動したときの動作を制御します。 flagがFalseの場合、カーソルは一番下の行に残ります。 flagがTrueの場合、ウィンドウは1行上にスクロールされます。 端末上で物理的なスクロール効果を得るためには、idlok（）も呼び出す必要があることに注意してください。)
window.setscrreg(top, bottom)|スクロール領域を top から bottom に設定します。スクロール動作はすべてこの領域で行われます。
window.standend()|A_STANDOUT 属性をオフにします。端末によっては、この操作ですべての属性をオフにする副作用が発生します。
window.standout()|A_STANDOUT 属性をオンにします。
window.subpad(begin_y, begin_x), window.subpad(nlines, ncols, begin_y, begin_x)|左上の角が (begin_y, begin_x) にあり、幅/高さがそれぞれ ncols / nlines であるようなサブウィンドウを返します。
window.subwin(begin_y, begin_x), window.subwin(nlines, ncols, begin_y, begin_x)|左上の角が (begin_y, begin_x) にあり、幅/高さがそれぞれ ncols / nlines であるようなサブウィンドウを返します。|デフォルトでは、サブウィンドウは指定された場所からウィンドウの右下角まで広がります。
window.syncdown()|このウィンドウの上位のウィンドウのいずれかで更新(touch)された各場所をこのウィンドウ内でも更新します。このルーチンは refresh() から呼び出されるので、手動で呼び出す必要はほとんどないはずです。
window.syncok(flag)|If flag is True, then syncup() is called automatically whenever there is a change in the window.
window.syncup()|ウィンドウ内で更新 (touch) した場所を、上位のすべてのウィンドウ内でも更新します。
window.timeout(delay)|Set blocking or non-blocking read behavior for the window. If delay is negative, blocking read is used (which will wait indefinitely for input). If delay is zero, then non-blocking read is used, and getch() will return -1 if no input is waiting. If delay is positive, then getch() will block for delay milliseconds, and return -1 if there is still no input at the end of that time. (ウィンドウのブロックまたは非ブロックの読み取り動作を設定します。 delayが負の場合、ブロック読み出しが使用されます（入力が無限に待機します）。 delayが0の場合、非ブロック読み取りが使用され、待機中の入力がない場合、getch（）は-1を返します。 delayが正の場合、getch（）は遅延ミリ秒でブロックし、その時間の最後にまだ入力がない場合は-1を返します。)
window.touchline(start, count[, changed])|Pretend count lines have been changed, starting with line start. If changed is supplied, it specifies whether the affected lines are marked as having been changed (changed=True) or unchanged (changed=False). (線の始まりから始まるふりがなの数の行が変更されました。 変更が提供されている場合は、影響を受けた行が変更済み（変更あり= True）または変更なし（変更済み= False）としてマークされるかどうかを指定します。)
window.touchwin()|描画を最適化するために、すべてのウィンドウが変更されたかのように振舞わせます。
window.untouchwin()|ウィンドウ内のすべての行を、最後に refresh() を呼んだ際から変更されていないものとしてマークします。
window.vline(ch, n), window.vline(y, x, ch, n)|(y, x) から始まり、n の長さを持つ、文字 ch で作られる垂直線を表示します。

* window.border([ls[, rs[, ts[, bs[, tl[, tr[, bl[, br]]]]]]]])

引数|説明|デフォルト値
----|----|------------
ls|左側|ACS_VLINE
rs|右側|ACS_VLINE
ts|上側|ACS_HLINE
bs|下側|ACS_HLINE
tl|左上の角|ACS_ULCORNER
tr|右上の角|ACS_URCORNER
bl|左下の角|ACS_LLCORNER
br|右下の角|ACS_LRCORNER

## [16.10.3. 定数](https://docs.python.jp/3/library/curses.html#constants)

> curses モジュールでは以下のデータメンバを定義しています:

属性|概要
----|----
curses.ERR|getch() のような整数を返す curses ルーチンのいくつかは、失敗した際に ERR を返します。
curses.OK|napms() のような整数を返す curses ルーチンのいくつかは、成功した際に OK を返します。
curses.version|A bytes object representing the current version of the module. Also available as __version__.

> Some constants are available to specify character cell attributes. The exact constants available are system dependent.

属性|意味
----|----
A_ALTCHARSET|Alternate character set mode
A_BLINK|Blink mode
A_BOLD|Bold mode
A_DIM|Dim mode
A_INVIS|Invisible or blank mode
A_NORMAL|Normal attribute
A_PROTECT|Protected mode
A_REVERSE|Reverse background and foreground colors
A_STANDOUT|Standout mode
A_UNDERLINE|Underline mode
A_HORIZONTAL|Horizontal highlight
A_LEFT|Left highlight
A_LOW|Low highlight
A_RIGHT|Right highlight
A_TOP|Top highlight
A_VERTICAL|Vertical highlight
A_CHARTEXT|Bit-mask to extract a character

> Several constants are available to extract corresponding attributes returned by some methods.

Bit-mask|意味
--------|----
A_ATTRIBUTES|Bit-mask to extract attributes
A_CHARTEXT|Bit-mask to extract a character
A_COLOR|Bit-mask to extract color-pair field information

> キーは KEY_ で始まる名前をもつ整数定数です。利用可能なキーキャップはシステムに依存します。

キー定数|キー
--------|----
KEY_MIN|最小のキー値
KEY_BREAK|ブレークキー (Break, 信頼できません)
KEY_DOWN|下矢印
KEY_UP|上矢印
KEY_LEFT|左矢印
KEY_RIGHT|右矢印
KEY_HOME|ホームキー (Home, または上左矢印)
KEY_BACKSPACE|バックスペース (Backspace, 信頼できません)
KEY_F0|ファンクションキー。64 個までサポートされています。
KEY_Fn|ファンクションキー n の値
KEY_DL|行削除 (Delete line)
KEY_IL|行挿入 (Insert line)
KEY_DC|文字削除 (Delete char)
KEY_IC|文字挿入、または文字挿入モードへ入る
KEY_EIC|文字挿入モードから抜ける
KEY_CLEAR|画面消去
KEY_EOS|画面の末端まで消去
KEY_EOL|行末端まで消去
KEY_SF|前に 1 行スクロール
KEY_SR|後ろ (逆方向) に 1 行スクロール
KEY_NPAGE|次のページ (Page Next)
KEY_PPAGE|前のページ (Page Prev)
KEY_STAB|タブ設定
KEY_CTAB|タブリセット
KEY_CATAB|すべてのタブをリセット
KEY_ENTER|入力または送信 (信頼できません)
KEY_SRESET|ソフトウェア (部分的) リセット (信頼できません)
KEY_RESET|リセットまたはハードリセット (信頼できません)
KEY_PRINT|印刷 (Print)
KEY_LL|下ホーム (Home down) または最下行 (左下)
KEY_A1|キーパッドの左上キー
KEY_A3|キーパッドの右上キー
KEY_B2|キーパッドの中央キー
KEY_C1|キーパッドの左下キー
KEY_C3|キーパッドの右下キー
KEY_BTAB|Back tab
KEY_BEG|開始 (Beg)
KEY_CANCEL|キャンセル (Cancel)
KEY_CLOSE|Close [閉じる]
KEY_COMMAND|コマンド (Cmd)
KEY_COPY|Copy [コピー]
KEY_CREATE|生成 (Create)
KEY_END|終了 (End)
KEY_EXIT|Exit [終了]
KEY_FIND|検索 (Find)
KEY_HELP|ヘルプ (Help)
KEY_MARK|マーク (Mark)
KEY_MESSAGE|メッセージ (Message)
KEY_MOVE|移動 (Move)
KEY_NEXT|次へ (Next)
KEY_OPEN|開く (Open)
KEY_OPTIONS|オプション
KEY_PREVIOUS|前へ (Prev)
KEY_REDO|Redo [やり直し]
KEY_REFERENCE|参照 (Ref)
KEY_REFRESH|更新 (Refresh)
KEY_REPLACE|置換 (Replace)
KEY_RESTART|再起動 (Restart)
KEY_RESUME|再開 (Resume)
KEY_SAVE|Save [保存]
KEY_SBEG|シフト付き Beg
KEY_SCANCEL|シフト付き Cancel
KEY_SCOMMAND|シフト付き Command
KEY_SCOPY|シフト付き Copy
KEY_SCREATE|シフト付き Create
KEY_SDC|シフト付き Delete char
KEY_SDL|シフト付き Delete line
KEY_SELECT|選択 (Select)
KEY_SEND|シフト付き End
KEY_SEOL|シフト付き Clear line
KEY_SEXIT|シフト付き Exit
KEY_SFIND|シフト付き Find
KEY_SHELP|シフト付き Help
KEY_SHOME|シフト付き Home
KEY_SIC|シフト付き Input
KEY_SLEFT|シフト付き Left arrow
KEY_SMESSAGE|シフト付き Message
KEY_SMOVE|シフト付き Move
KEY_SNEXT|シフト付き Next
KEY_SOPTIONS|シフト付き Options
KEY_SPREVIOUS|シフト付き Prev
KEY_SPRINT|シフト付き Print
KEY_SREDO|シフト付き Redo
KEY_SREPLACE|シフト付き Replace
KEY_SRIGHT|シフト付き Right arrow
KEY_SRSUME|シフト付き Resume
KEY_SSAVE|シフト付き Save
KEY_SSUSPEND|シフト付き Suspend
KEY_SUNDO|シフト付き Undo
KEY_SUSPEND|一時停止 (Suspend)
KEY_UNDO|Undo [元に戻す]
KEY_MOUSE|マウスイベント通知
KEY_RESIZE|端末リサイズイベント
KEY_MAX|最大キー値

> VT100 や、X 端末エミュレータのようなソフトウェアエミュレーションでは、通常少なくとも 4 つのファンクションキー (KEY_F1, KEY_F2, KEY_F3, KEY_F4) が利用可能で、矢印キーは KEY_UP, KEY_DOWN, KEY_LEFT および KEY_RIGHT が対応付けられています。計算機に PC キーボードが付属している場合、矢印キーと 12 個のファンクションキー (古い PC キーボードには 10 個しかファンクションキーがないかもしれません) が利用できると考えてよいでしょう; また、以下のキーパッド対応付けは標準的なものです:

キーキャップ|定数
------------|----
Insert|KEY_IC
Delete|KEY_DC
Home|KEY_HOME
End|KEY_END
Page Up|KEY_PPAGE
Page Down|KEY_NPAGE

> 代替文字セットを以下の表に列挙します。これらは VT100 端末から継承したものであり、X 端末のようなソフトウェアエミュレーション上で一般に利用可能なものです。グラフィックが利用できない場合、curses は印字可能 ASCII文字による粗雑な近似出力を行います。

> 注釈

> これらは initscr() が呼び出された後でしか利用できません。

ACS コード|意味
----------|----
ACS_BBSS|右上角の別名
ACS_BLOCK|黒四角ブロック
ACS_BOARD|白四角ブロック
ACS_BSBS|水平線の別名
ACS_BSSB|左上角の別名
ACS_BSSS|上向き T 字罫線の別名
ACS_BTEE|下向き T 字罫線
ACS_BULLET|黒丸(bullet)
ACS_CKBOARD|チェッカーボードパタン (点描)
ACS_DARROW|下向き矢印
ACS_DEGREE|度記号
ACS_DIAMOND|ダイアモンド
ACS_GEQUAL|大なりイコール
ACS_HLINE|水平線
ACS_LANTERN|ランタン(lantern) シンボル
ACS_LARROW|左向き矢印
ACS_LEQUAL|小なりイコール
ACS_LLCORNER|左下角
ACS_LRCORNER|右下角
ACS_LTEE|左向き T 字罫線
ACS_NEQUAL|不等号
ACS_PI|パイ記号
ACS_PLMINUS|プラスマイナス記号
ACS_PLUS|大プラス記号
ACS_RARROW|右向き矢印
ACS_RTEE|右向き T 字罫線
ACS_S1|スキャンライン 1
ACS_S3|スキャンライン 3
ACS_S7|スキャンライン 7
ACS_S9|スキャンライン 9
ACS_SBBS|右下角の別名
ACS_SBSB|垂直線の別名
ACS_SBSS|右向き T 字罫線の別名
ACS_SSBB|左下角の別名
ACS_SSBS|下向き T 字罫線の別名
ACS_SSSB|左向き T 字罫線の別名
ACS_SSSS|交差罫線または大プラス記号の別名
ACS_STERLING|ポンドスターリング記号
ACS_TTEE|上向き T 字罫線
ACS_UARROW|上向き矢印
ACS_ULCORNER|左上角
ACS_URCORNER|右上角
ACS_VLINE|垂直線

> 以下のテーブルは定義済みの色を列挙したものです:

定数|色
----|--
COLOR_BLACK|黒
COLOR_BLUE|青
COLOR_CYAN|シアン (薄く緑がかった青)
COLOR_GREEN|緑
COLOR_MAGENTA|マゼンタ (紫がかった赤)
COLOR_RED|赤
COLOR_WHITE|白
COLOR_YELLOW|黄色

