# [16.7. logging.config — ロギングの環境設定](https://docs.python.jp/3/library/logging.config.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/logging/config.py](https://github.com/python/cpython/tree/3.6/Lib/logging/config.py)

> この節は、logging モジュールを設定するための API を解説します。

## Important

* [基本チュートリアル](https://docs.python.jp/3/howto/logging.html#logging-basic-tutorial)
* [上級チュートリアル](https://docs.python.jp/3/howto/logging.html#logging-advanced-tutorial)
* [ロギングクックブック](https://docs.python.jp/3/howto/logging-cookbook.html#logging-cookbook)

## [16.7.1. 環境設定のための関数](https://docs.python.jp/3/library/logging.config.html#configuration-functions)

> 以下の関数は logging モジュールの環境設定をします。これらの関数は、 logging.config にあります。これらの関数の使用はオプションです — logging モジュールはこれらの関数を使うか、 (logging 自体で定義されている) 主要な API を呼び出し、 logging か logging.handlers で宣言されているハンドラを定義することで設定できます。

属性|概要
----|----
logging.config.dictConfig(config)|辞書からロギング環境設定を取得します。この辞書の内容は、以下の 環境設定辞書スキーマ で記述されています。
logging.config.fileConfig(fname, defaults=None, disable_existing_loggers=True)|ログ記録の環境設定を configparser 形式ファイルから読み出します。そのファイルの形式は 環境設定ファイルの書式 で記述されているとおりにしなければなりません。この関数はアプリケーションから何度も呼び出すことができ、これによって、 (設定を選択し、選択された設定を読み出す機構をデベロッパが提供していれば) 複数の準備済みの設定からエンドユーザが選択するようにできます。
logging.config.listen(port=DEFAULT_LOGGING_CONFIG_PORT, verify=None)|指定されたポートでソケットサーバを起動し、新しい設定を待ち受けます。ポートが指定されなかった場合は、モジュールのデフォルトの DEFAULT_LOGGING_CONFIG_PORT が使用されます。ロギング設定は dictConfig() あるいは fileConfig() で処理できるファイルとして送信されます。 Thread インスタンスを返し、このインスタンスの start() を呼び出してサーバを起動し、適切なところで join() を呼び出すことができます。サーバを停止するには、 stopListening() を呼び出します。
logging.config.stopListening()|listen() を呼び出して作成された、待ち受け中のサーバを停止します。通常 listen() の戻り値に対して join() が呼ばれる前に呼び出します。

## [16.7.2. 環境設定辞書スキーマ](https://docs.python.jp/3/library/logging.config.html#configuration-dictionary-schema)

> ロギング設定を記述するには、生成するさまざまなオブジェクトと、それらのつながりを列挙しなければなりません。例えば、 'console' という名前のハンドラを生成し、'startup' という名前のロガーがメッセージを 'console' ハンドラに送るというようなことを記述します。これらのオブジェクトは、 logging モジュールによって提供されるものに限らず、独自のフォーマッタやハンドラクラスを書くことも出来ます。このクラスへのパラメータは、 sys.stderr のような外部オブジェクトを必要とすることもあります。これらのオブジェクトとつながりを記述する構文は、以下の オブジェクトの接続 で定義されています。

### [16.7.2.1. 辞書スキーマの詳細](https://docs.python.jp/3/library/logging.config.html#dictionary-schema-details)

> dictConfig() に渡される辞書は、以下のキーを含んでいなければなりません:

キー|説明
----|----
version|スキーマのバージョンを表す整数値に設定されます。現在有効な値は 1 だけですが、このキーがあることで、このスキーマは後方互換性を保ちながら発展できます。
formatters|対応する値は辞書で、そのそれぞれのキーがフォーマッタ id になり、それぞれの値が対応する Formatter インスタンスをどのように環境設定するかを記述する辞書になります。環境設定辞書から、 (デフォルトが None の) キー format と datefmt を検索し、それらが Formatter インスタンスを構成するのに使われます。
filters|対応する値は辞書で、そのそれぞれのキーがフィルタ id になり、それぞれの値が対応する Filter インスタンスをどのように環境設定するかを記述する辞書になります。環境設定辞書は、(デフォルトが空文字列の) キー name を検索され、それらが logging.Filter インスタンスを構成するのに使われます。
handlers|対応する値は辞書で、そのそれぞれのキーがハンドラ id になり、それぞれの値が対応する Handler インスタンスをどのように環境設定するかを記述する辞書になります。
loggers|対応する値は辞書で、そのそれぞれのキーがロガー名になり、それぞれの値が対応する Logger インスタンスをどのように環境設定するかを記述する辞書になります。
root|これは、ルートロガーへの設定になります。この環境設定の進行は、propagate 設定が適用されないことを除き、他のロガーと同じです。
incremental|この環境設定が既存の環境設定に対する増分として解釈されるかどうかです。この値のデフォルトは False で、指定された環境設定は、既存の fileConfig() API によって使われているのと同じ意味上で、既存の環境設定を置き換えます。指定された値が True なら、環境設定は 増分設定 の節で記述されているように進行します。
disable_existing_loggers|既存のロガーをすべて無効にするべきかどうかです。この設定は、 fileConfig() における同じ名前のパラメータと同じです。設定されていなければ、このパラメータのデフォルトは True です。この値は、 incremental が True なら無視されます。
> versionの他すべてのキーは省略可能ですが、与えられたなら以下に記述するように解釈されます。以下のすべての場合において、 '環境設定辞書' と記載されている所では、その辞書に特殊な '()' キーがあるかを調べることで、カスタムのインスタント化が必要であるか判断されます。その場合は、以下の ユーザ定義オブジェクト で記述されている機構がインスタンス生成に使われます。そうでなければ、インスタンス化するべきものを決定するのにコンテキストが使われます。

> `handlers`の環境設定辞書は、以下のキーを検索されます:

キー|必須|概要
----|----|----
class|(必須)|これはハンドラクラスの完全に修飾された名前です。
level|(任意)|ハンドラのレベルです。
formatter|(任意)|このハンドラへのフォーマッタの id です。
filters|(任意)|このハンドラへのフィルタの id のリストです。

> `loggers`の環境設定辞書は、以下のキーを検索されます:

キー|必須|概要
----|----|----
level|(任意)|ロガーのレベルです。
propagate|(任意)|ロガーの伝播の設定です。
filters|(任意)|このロガーへのフィルタの id のリストです。
handlers|(任意)|このロガーへのハンドラの id のリストです。

> その他の すべての キーは、ハンドラのコンストラクタにキーワード引数として渡されます。例えば、以下のコード片が与えられたとすると:

```yaml
handlers:
  console:
    class : logging.StreamHandler
    formatter: brief
    level   : INFO
    filters: [allow_foo]
    stream  : ext://sys.stdout
  file:
    class : logging.handlers.RotatingFileHandler
    formatter: precise
    filename: logconfig.log
    maxBytes: 1024
    backupCount: 3
```

### [16.7.2.2. 増分設定](https://docs.python.jp/3/library/logging.config.html#incremental-configuration)

> 増分設定に完全な柔軟性を提供するのは難しいです。例えば、フィルタやフォーマッタのようなオブジェクトは匿名なので、一旦環境設定がなされると、設定を拡張するときにそのような匿名オブジェクトを参照することができません。

> さらに、一旦環境設定がなされた後、実行時にロガー、ハンドラ、フィルタ、フォーマッタのオブジェクトグラフを任意に変えなければならない例もありません。ロガーとハンドラの冗長性は、レベル (または、ロガーの場合には、伝播フラグ) を設定することによってのみ制御できます。安全な方法でオブジェクトグラフを任意に変えることは、マルチスレッド環境で問題となります。不可能ではないですが、その効用は実装に加えられる複雑さに見合いません。

> 従って、環境設定辞書の incremental キーが与えられ、これが True であるとき、システムは formatters と filters の項目を完全に無視し、handlers の項目の level 設定と、loggers と root の項目の level と propagate 設定のみを処理します。

> 環境設定辞書の値を使うことで、設定は pickle 化された辞書としてネットワークを通してソケットリスナに送ることができます。これにより、長時間起動するアプリケーションのロギングの冗長性を、アプリケーションを止めて再起動する必要なしに、いつでも変更することができます。

### [16.7.2.3. オブジェクトの接続](https://docs.python.jp/3/library/logging.config.html#object-connections)

> このスキーマは、ロギングオブジェクトの一揃い - ロガー、ハンドラ、フォーマッタ、フィルタ - について記述します。これらは、オブジェクトグラフ上でお互い接続されます。従って、このスキーマは、オブジェクト間の接続を表現しなければなりません。例えば、環境設定で、特定のロガーが特定のハンドラに取り付けられたとします。この議論では、ロガーとハンドラが、これら 2 つの接続のそれぞれ送信元と送信先であるといえます。もちろん、この設定オブジェクト中では、これはハンドラへの参照を保持しているロガーで表されます。設定辞書中で、これは次のようになされます。まず、送信先オブジェクトを曖昧さなく指定する id を与えます。そして、その id を送信元オブジェクトの環境設定で使い、送信元とその id をもつ送信先が接続されていることを示します。

> ですから、例えば、以下の YAML のコード片を例にとると:

```yaml
formatters:
  brief:
    # configuration for formatter with id 'brief' goes here
  precise:
    # configuration for formatter with id 'precise' goes here
handlers:
  h1: #This is an id
   # configuration of handler with id 'h1' goes here
   formatter: brief
  h2: #This is another id
   # configuration of handler with id 'h2' goes here
   formatter: precise
loggers:
  foo.bar.baz:
    # other configuration for logger 'foo.bar.baz'
    handlers: [h1, h2]
```

> (注釈: YAML がここで使われているのは、辞書の等価な Python 形式よりもこちらのほうが少し読みやすいからです。)

> ロガーの id は、プログラム上でロガーへの参照を得るために使われるロガー名で、たとえば foo.bar.baz です。フォーマッタとフィルタの id は、(上の brief, precise のような) 任意の文字列値にできます。これらは一時的なもので、環境設定辞書の処理にのみ意味があり、オブジェクト間の接続を決定するのに使われます。また、これらは設定の呼び出しが完了したとき、どこにも残りません。

> 上記のコード片は、foo.bar.baz というの名ロガーに、ハンドラ id h1 と h2 で表される 2 つのハンドラを接続することを示します。h1 のフォーマッタは id brief で記述されるもので、h2 のフォーマッタは id precise で記述されるものです。
16.7.2.4. ユーザ定義オブジェクト(原文)

> このスキーマは、ハンドラ、フィルタ、フォーマッタのための、ユーザ定義オブジェクトをサポートします。(ロガーは、異なるインスタンスに対して異なる型を持つ必要はないので、この環境設定スキーマは、ユーザ定義ロガークラスをサポートしていません。)

> 設定されるオブジェクトは、それらの設定を詳述する辞書によって記述されます。場所によっては、あるオブジェクトがどのようにインスタンス化されるかというコンテキストを、ロギングシステムが推測できます。しかし、ユーザ定義オブジェクトがインスタンス化されるとき、システムはどのようにこれを行うかを知りません。ユーザ定義オブジェクトのインスタンス化を完全に柔軟なものにするため、ユーザは 'ファクトリ' - 設定辞書を引数として呼ばれ、インスタンス化されたオブジェクトを返す呼び出し可能オブジェクト - を提供する必要があります。これは特殊キー '()' で利用できる、ファクトリへの絶対インポートパスによって合図されます。ここに具体的な例を挙げます:

```yaml
formatters:
  brief:
    format: '%(message)s'
  default:
    format: '%(asctime)s %(levelname)-8s %(name)-15s %(message)s'
    datefmt: '%Y-%m-%d %H:%M:%S'
  custom:
      (): my.package.customFormatterFactory
      bar: baz
      spam: 99.9
      answer: 42
```

> 上記の YAML コード片は 3 つのフォーマッタを定義します。 1 つ目は、id が brief で、指定されたフォーマット文字列をもつ、標準 logging.Formatter インスタンスです。 2 つ目は、id が default で、長いフォーマットを持ち、時間フォーマットも定義していて、結果はその 2 つのフォーマット文字列で初期化された logging.Formatter になります。Python ソース形式で見ると、 brief と default フォーマッタは、それぞれ設定の部分辞書:

```json
{
  'format' : '%(message)s'
}
```

> および:

```json
{
  'format' : '%(asctime)s %(levelname)-8s %(name)-15s %(message)s',
  'datefmt' : '%Y-%m-%d %H:%M:%S'
}
```

を持ち、これらの辞書が特殊キー '()' を持たないので、インスタンス化はコンテキストから推測され、結果として標準の logging.Formatter インスタンスが生成されます。id が custom である、3 つ目のフォーマッタの設定をする部分辞書は:

```json
{
  '()' : 'my.package.customFormatterFactory',
  'bar' : 'baz',
  'spam' : 99.9,
  'answer' : 42
}
```

> で、ユーザ定義のインスタンス化が望まれることを示す特殊キー '()' を含みます。この場合、指定された呼び出し可能ファクトリオブジェクトが使われます。これが実際の呼び出し可能オブジェクトであれば、それが直接使われます - そうではなく、(この例でのように) 文字列を指定したなら、実際の呼び出し可能オブジェクトは、通常のインポート機構を使って検索されます。その呼び出し可能オブジェクトは、環境設定の部分辞書の、残りの 要素をキーワード引数として呼ばれます。上記の例では、id が custom のフォーマッタは、以下の呼び出しによって返されるものとみなされます:

```python
my.package.customFormatterFactory(bar='baz', spam=99.9, answer=42)
```

> キー '()' が特殊キーとして使われるのは、キーワードパラメータ名として不正で、呼び出しに使われるキーワード引数と衝突し得ないからです。'()' はまた、対応する値が呼び出し可能オブジェクトであると覚えやすくします。
16.7.2.5. 外部オブジェクトへのアクセス(原文)

> 環境設定が、例えば sys.stderr のような、設定の外部のオブジェクトへの参照を必要とすることがあります。設定辞書が Python コードで構成されていれば話は簡単ですが、これがテキストファイル (JSON, YAML 等) を通して提供されていると問題となります。テキストファイルでは、sys.stderr をリテラル文字列 'sys.stderr' と区別する標準の方法がありません。この区別を容易にするため、環境設定システムは、文字列中の特定の特殊接頭辞を見つけ、それらを特殊に扱います。例えば、リテラル文字列 'ext://sys.stderr' が設定中の値として与えられたら、この ext:// は剥ぎ取られ、この値の残りが普通のインポート機構で処理されます。

> このような接頭辞の処理は、プロトコルの処理と同じようになされます。どちらの機構も、正規表現 ^(?P<prefix>[a-z]+)://(?P<suffix>.*)$ にマッチする接頭辞を検索し、それによって prefix が認識されたなら、接頭辞に応じたやり方で suffix が処理され、その処理の結果によって文字列値が置き換えられます。接頭辞が認識されなければ、その文字列値はそのまま残されます。
16.7.2.6. 内部オブジェクトへのアクセス(原文)

> 外部オブジェクトと同様、環境設定内部のオブジェクトへのアクセスを必要とすることもあります。これは、その各オブジェクトを司る環境設定システムによって暗黙に行われます。例えば、ロガーやハンドラの level に対する文字列値 'DEBUG' は、自動的に値 logging.DEBUG に変換されますし、handlers, filters および formatter の項目は、オブジェクト id を取って、適切な送信先オブジェクトを決定します。

> しかし、ユーザ定義モジュールには、 logging モジュールには分からないような、より一般的な機構が必要です。例えば、 logging.handlers.MemoryHandler があって、委譲する先の別のハンドラである target 引数を取るとします。システムはこのクラスをすでに知っていますから、設定中で、与えられた target は関連するターゲットハンドラのオブジェクト id でさえあればよく、システムはその id からハンドラを決定します。しかし、ユーザが my.package.MyHandler を定義して、それが alternate ハンドラを持つなら、設定システムは alternate がハンドラを参照していることを知りません。これを知らせるのに、一般的な解析システムで、ユーザはこのように指定できます:

```yaml
handlers:
  file:
    # configuration of file handler goes here

  custom:
    (): my.package.MyHandler
    alternate: cfg://handlers.file
```

> リテラル文字列 'cfg://handlers.file' は、ext:// 接頭辞が付いた文字列と同じように分析されますが、インポート名前空間ではなく、環境設定自体が検索されます。この機構は str.format でできるのと同じようにドットやインデックスのアクセスができます。従って、環境設定において以下のコード片が与えられれば:

```yaml
handlers:
  email:
    class: logging.handlers.SMTPHandler
    mailhost: localhost
    fromaddr: my_app@domain.tld
    toaddrs:
      - support_team@domain.tld
      - dev_team@domain.tld
    subject: Houston, we have a problem.
```

> 文字列 'cfg://handlers' は、キー handlers をもつ辞書であると分析され、文字列 'cfg://handlers.email' は、handlers 辞書内の、email キーをもつ辞書であると分析されます。文字列 'cfg://handlers.email.toaddrs[1] は、'dev_team@domain.tld' と分析され、'cfg://handlers.email.toaddrs[0]' は値 'support_team@domain.tld' と分析されます。subject の値には、'cfg://handlers.email.subject' または等価な 'cfg://handlers.email[subject]' でアクセスできます。後者が必要なのは、キーがスペースや非アルファベット文字を含むときのみです。インデックス値が十進数字のみで構成されているなら、まず対応する整数値を使ってアクセスが試みられ、必要なら文字列値で代替します。

> 文字列 cfg://handlers.myhandler.mykey.123 が与えられると、これは config_dict['handlers']['myhandler']['mykey']['123'] と分析されます。文字列が cfg://handlers.myhandler.mykey[123] と指定されたら、システムは config_dict['handlers']['myhandler']['mykey'][123] から値を引き出そうとし、失敗したら config_dict['handlers']['myhandler']['mykey']['123'] で代替します。

### [16.7.2.7. インポート解決とカスタムインポーター](https://docs.python.jp/3/library/logging.config.html#import-resolution-and-custom-importers)

> インポート解決は、デフォルトではインポートを行うために __import__() 組み込み関数を使用します。これを独自のインポートメカニズムに置き換えたいと思うかもしれません: もしそうなら、 DictConfigurator あるいはその上位クラスである BaseConfigurator クラスの importer 属性を置換することができます。ただし、この関数はクラスからディスクリプタ経由でアクセスされる点に注意する必要があります。インポートを行うために Python callable を使用していて、それをインスタンスレベルではなくクラスレベルで定義したければ、 staticmethod() でそれをラップする必要があります。例えば:

```python
from importlib import import_module
from logging.config import BaseConfigurator

BaseConfigurator.importer = staticmethod(import_module)
```

> configurator インスタンス に対してインポート callable をセットする場合は、 staticmethod() でラップする必要はありません。

## [16.7.3. 環境設定ファイルの書式](https://docs.python.jp/3/library/logging.config.html#configuration-file-format)

> fileConfig() が解釈できる環境設定ファイルの形式は、 configparser の機能に基づいています。ファイルには、 [loggers], [handlers], [formatters] といったセクションが入っていなければならず、各セクションではファイル中で定義されている各タイプのエンティティを名前で指定しています。こうしたエンティティの各々について、そのエンティティをどう設定するかを示した個別のセクションがあります。すなわち、 log01 という名前の [loggers] セクションにあるロガーに対しては、対応する詳細設定がセクション [logger_log01] に収められています。同様に、 hand01 という名前の [handlers] セクションにあるハンドラは [handler_hand01] と呼ばれるセクションに設定をもつことになり、 [formatters] セクションにある form01 は [formatter_form01] というセクションで設定が指定されています。ルートロガーの設定は [logger_root] と呼ばれるセクションで指定されていなければなりません。

### 注釈

> fileConfig() API は dictConfig() API よりも古く、ロギングのある種の側面についてカバーする機能に欠けています。たとえば fileConfig() では数値レベルを超えたメッセージを単に拾うフィルタリングを行う Filter オブジェクトを構成出来ません。 Filter のインスタンスをロギングの設定において持つ必要があるならば、 dictConfig() を使う必要があるでしょう。設定の機能における将来の拡張は dictConfig() に対して行われることに注意してください。ですから、そうするのが便利であるときに新しい API に乗り換えるのは良い考えです。

> ファイルにおけるこれらのセクションの例を以下に示します。

```ini
[loggers]
keys=root,log02,log03,log04,log05,log06,log07

[handlers]
keys=hand01,hand02,hand03,hand04,hand05,hand06,hand07,hand08,hand09

[formatters]
keys=form01,form02,form03,form04,form05,form06,form07,form08,form09
```

> ルートロガーでは、レベルとハンドラのリストを指定しなければなりません。ルートロガーのセクションの例を以下に示します。

```ini
[logger_root]
level=NOTSET
handlers=hand01
```

> level エントリは DEBUG, INFO, WARNING, ERROR, CRITICAL のうちの一つか、 NOTSET になります。ルートロガーの場合にのみ、 NOTSET はすべてのメッセージがログ記録されることを意味します。レベル値は logging パッケージの名前空間のコンテキストにおいて eval() されます。

> handlers エントリはコンマで区切られたハンドラ名からなるリストで、[handlers] セクションになくてはなりません。また、これらの各ハンドラの名前に対応するセクションが設定ファイルに存在しなければなりません。

> ルートロガー以外のロガーでは、いくつか追加の情報が必要になります。これは以下の例のように表されます。

```ini
[logger_parser]
level=DEBUG
handlers=hand01
propagate=1
qualname=compiler.parser
```

> level および handlers エントリはルートロガーのエントリと同様に解釈されますが、非ルートロガーのレベルが NOTSET に指定された場合、ロギングシステムはロガー階層のより上位のロガーにロガーの実効レベルを問い合わせるところが違います。propagate エントリは、メッセージをロガー階層におけるこのロガーの上位のハンドラに伝播させることを示す 1 に設定されるか、メッセージを階層の上位に伝播 しない ことを示す 0 に設定されます。qualname エントリはロガーのチャネル名を階層的に表したもの、すなわちアプリケーションがこのロガーを取得する際に使う名前になります。

> ハンドラの環境設定を指定しているセクションは以下の例のようになります。

```ini
[handler_hand01]
class=StreamHandler
level=NOTSET
formatter=form01
args=(sys.stdout,)
```

> class エントリはハンドラのクラス (logging パッケージの名前空間において eval() で決定されます) を示します。 level はロガーの場合と同じように解釈され、 NOTSET は "すべてを記録する (log everything)" と解釈されます。

> formatter エントリはこのハンドラのフォーマッタに対するキー名を表します。空文字列の場合、デフォルトのフォーマッタ (logging._defaultFormatter) が使われます。名前が指定されている場合、その名前は [formatters] セクションになくてはならず、対応するセクションが設定ファイル中になければなりません。

> args エントリは、 logging パッケージの名前空間のコンテキストで eval() される際、ハンドラクラスのコンストラクタに対する引数からなるリストになります。典型的なエントリがどうやって作成されるかについては、対応するハンドラのコンストラクタか、以下の例を参照してください。

```ini
[handler_hand02]
class=FileHandler
level=DEBUG
formatter=form02
args=('python.log', 'w')

[handler_hand03]
class=handlers.SocketHandler
level=INFO
formatter=form03
args=('localhost', handlers.DEFAULT_TCP_LOGGING_PORT)

[handler_hand04]
class=handlers.DatagramHandler
level=WARN
formatter=form04
args=('localhost', handlers.DEFAULT_UDP_LOGGING_PORT)

[handler_hand05]
class=handlers.SysLogHandler
level=ERROR
formatter=form05
args=(('localhost', handlers.SYSLOG_UDP_PORT), handlers.SysLogHandler.LOG_USER)

[handler_hand06]
class=handlers.NTEventLogHandler
level=CRITICAL
formatter=form06
args=('Python Application', '', 'Application')

[handler_hand07]
class=handlers.SMTPHandler
level=WARN
formatter=form07
args=('localhost', 'from@abc', ['user1@abc', 'user2@xyz'], 'Logger Subject')

[handler_hand08]
class=handlers.MemoryHandler
level=NOTSET
formatter=form08
target=
args=(10, ERROR)

[handler_hand09]
class=handlers.HTTPHandler
level=NOTSET
formatter=form09
args=('localhost:9022', '/log', 'GET')
```

> フォーマッタの環境設定を指定しているセクションは以下のような形式です。

```ini
[formatter_form01]
format=F1 %(asctime)s %(levelname)s %(message)s
datefmt=
class=logging.Formatter
```

> format エントリは全体の書式文字列で、 datefmt エントリは strftime() 互換の日付/時刻書式文字列です。空文字列の場合、パッケージによって ISO8601 形式の日付/時刻に置き換えられ、日付書式文字列 '%Y-%m-%d %H:%M:%S' を指定した場合とほとんど同じになります。 ISO8601 形式ではミリ秒も指定しており、上の書式文字列の結果にカンマで区切って追加されます。 ISO8601 形式の時刻の例は 2003-01-23 00:29:50,411 です。

> class エントリはオプションです。これはフォーマッタクラスの名前を (モジュール名とクラス名をドットでつないだもので) 指し示すものです。このオプションは Formatter の子クラスをインスタンス化するのに便利です。 Formatter の子クラスが、展開もしくは要約された形式の例外トレースバックを表示することができます。

#### 注釈

> eval() を使用していることで、上述のようにソケット経由で設定を送受信するために listen() を使用していることに起因する潜在的なセキュリティリスクがあります。そのリスクは、相互に信頼できない多数のユーザが同じマシン上でコードを実行する場合に制限されています; 詳細は listen() ドキュメンテーションを参照してください。

#### 参考

モジュール|説明
----------|----
logging|logging モジュールの API リファレンス。
logging.handlers|logging モジュールに含まれる、便利なハンドラです。

