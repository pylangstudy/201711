# [16.13. curses.panel — curses のためのパネルスタック拡張](https://docs.python.jp/3/library/curses.panel.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

> パネルは深さ (depth) の機能が追加されたウィンドウです。これにより、ウィンドウをお互いに重ね合わせることができ、各ウィンドウの可視部分だけが表示されます。パネルはスタック中に追加したり、スタック内で上下移動させたり、スタックから除去することができます。

## [16.13.1. 関数]()

> curses.panel では以下の関数を定義しています:

属性|概要
----|----
curses.panel.bottom_panel()|パネルスタックの最下層のパネルを返します。
curses.panel.new_panel(win)|与えられたウィンドウ win に関連付けられたパネルオブジェクトを返します。返されたパネルオブジェクトを参照しておく必要があることに注意してください。もし参照しなければ、パネルオブジェクトはガベージコレクションされてパネルスタックから削除されます。
curses.panel.top_panel()|パネルスタックの最上層のパネルを返します。
curses.panel.update_panels()|仮想スクリーンをパネルスタック変更後の状態に更新します。この関数では curses.doupdate() を呼ばないので、ユーザは自分で呼び出す必要があります。

## [16.13.2. Panel オブジェクト]()

> 上記の new_panel() が返す Panel オブジェクトはスタック順の概念を持つウィンドウです。ウィンドウはパネルに関連付けられており、表示する内容を決定している一方、パネルのメソッドはパネルスタック中のウィンドウの深さ管理を担います。

> Panel オブジェクトは以下のメソッドを持っています:

属性|概要
----|----
Panel.above()|現在のパネルの上にあるパネルを返します。
Panel.below()|現在のパネルの下にあるパネルを返します。
Panel.bottom()|パネルをスタックの最下層にプッシュします。
Panel.hidden()|Returns True if the panel is hidden (not visible), False otherwise.
Panel.hide()|パネルを隠します。この操作ではオブジェクトは消去されず、スクリーン上のウィンドウを不可視にするだけです。
Panel.move(y, x)|パネルをスクリーン座標 (y, x) に移動します。
Panel.replace(win)|パネルに関連付けられたウィンドウを win に変更します。
Panel.set_userptr(obj)|パネルのユーザポインタを obj に設定します。このメソッドは任意のデータをパネルに関連付けるために使われ、任意の Python オブジェクトにすることができます。
Panel.show()|(隠れているはずの) パネルを表示します。
Panel.top()|パネルをスタックの最上層にプッシュします。
Panel.userptr()|パネルのユーザポインタを返します。任意の Python オブジェクトです。
Panel.window()|パネルに関連付けられているウィンドウオブジェクトを返します。

