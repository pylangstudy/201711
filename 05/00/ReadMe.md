# [14.2. configparser — 設定ファイルのパーサー](https://docs.python.jp/3/library/configparser.html)

< [14. ファイルフォーマット](https://docs.python.jp/3/library/fileformats.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/configparser.py](https://github.com/python/cpython/tree/3.6/Lib/configparser.py)

> このモジュールは、 Microsoft Windows の INI ファイルに似た構造を持ったベーシックな設定用言語を実装した ConfigParser クラスを提供します。このクラスを使ってユーザーが簡単にカスタマイズできる Python プログラムを作ることができます。

> 注釈

> このライブラリでは、Windowsのレジストリ用に拡張された INI 文法はサポート していません 。

> 参考

モジュール|概要
----------|----
[shlex](https://docs.python.jp/3/library/shlex.html#module-shlex)|アプリケーション設定ファイルのフォーマットとして使える、Unix シェルに似たミニ言語の作成を支援します。
[json](https://docs.python.jp/3/library/json.html#module-json)|json モジュールは、同じ目的に利用できる JavaScript の文法のサブセットを実装しています。

## [14.2.1. クイックスタート](https://docs.python.jp/3/library/configparser.html#quick-start)

> 次のような、非常に簡単な設定ファイルを例に考えましょう:

```ini
[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[bitbucket.org]
User = hg

[topsecret.server.com]
Port = 50022
ForwardX11 = no
```

> INI ファイルの構造は 下のセクション で解説します。 基本的に、ファイルは複数のセクションからなり、各セクションは複数のキーと値を持ちます。 configparser のクラス群はそれらのファイルを読み書きできます。 まずは上のような設定ファイルをプログラムから作成してみましょう。

```python
>>> import configparser
>>> config = configparser.ConfigParser()
>>> config['DEFAULT'] = {'ServerAliveInterval': '45',
...                      'Compression': 'yes',
...                      'CompressionLevel': '9'}
>>> config['bitbucket.org'] = {}
>>> config['bitbucket.org']['User'] = 'hg'
>>> config['topsecret.server.com'] = {}
>>> topsecret = config['topsecret.server.com']
>>> topsecret['Port'] = '50022'     # mutates the parser
>>> topsecret['ForwardX11'] = 'no'  # same here
>>> config['DEFAULT']['ForwardX11'] = 'yes'
>>> with open('example.ini', 'w') as configfile:
...   config.write(configfile)
...
```

> この例でわかるように、config parser は辞書のように扱うことができます。辞書との違いは 後に 説明しますが、このインターフェイスは辞書に対して期待するのととても近い動作をします。

> これで設定ファイルを作成して保存できました。次はこれを読み込み直して、中のデータを取り出してみましょう。

```python
>>> import configparser
>>> config = configparser.ConfigParser()
>>> config.sections()
[]
>>> config.read('example.ini')
['example.ini']
>>> config.sections()
['bitbucket.org', 'topsecret.server.com']
>>> 'bitbucket.org' in config
True
>>> 'bytebong.com' in config
False
>>> config['bitbucket.org']['User']
'hg'
>>> config['DEFAULT']['Compression']
'yes'
>>> topsecret = config['topsecret.server.com']
>>> topsecret['ForwardX11']
'no'
>>> topsecret['Port']
'50022'
>>> for key in config['bitbucket.org']: print(key)
...
user
compressionlevel
serveraliveinterval
compression
forwardx11
>>> config['bitbucket.org']['ForwardX11']
'yes'
```

> 上の例からわかるように、API はとても直感的です。唯一の魔術は、DEFAULT セクションが他の全てのセクションのためのデフォルト値を提供していることです [1]。 また、セクション内の各キーは大文字小文字を区別せず、全て小文字で保存されていることにも注意してください [1]。

## [14.2.2. サポートされるデータ型](https://docs.python.jp/3/library/configparser.html#supported-datatypes)

> Config parser は値のデータ型について何も推論せず、常に文字列のまま内部に保存します。他のデータ型が必要な場合は自分で変換する必要があります:

```python
>>> int(topsecret['Port'])
50022
>>> float(topsecret['CompressionLevel'])
9.0
```

> このタスクはとても一般的なため、設定パーサーでは整数、浮動小数点数、真偽値を扱うための手頃なゲッターメソッドが提供されています。真偽値の扱いは一筋縄ではいきません。文字列を bool() に渡しても、 bool('False') が True になってしまいます。そこで config parser は getboolean() を提供しています。このメソッドは大文字小文字を区別せず、 'yes'/'no'、'on'/'off'、'true'/'false'、'1'/'0' を真偽値として認識します [1]。例えば:

```python
>>> topsecret.getboolean('ForwardX11')
False
>>> config['bitbucket.org'].getboolean('ForwardX11')
True
>>> config.getboolean('bitbucket.org', 'Compression')
True
```

> config parser では、 getboolean() 以外に getint() と getfloat() メソッドも提供されています。独自のコンバーターの登録、提供されたメソッドのカスタマイズもできます。 [1]

## [14.2.3. 代替値](https://docs.python.jp/3/library/configparser.html#fallback-values)

> 辞書と同じように、セクションの get() メソッドは代替値を提供しています:

```python
>>> topsecret.get('Port')
'50022'
>>> topsecret.get('CompressionLevel')
'9'
>>> topsecret.get('Cipher')
>>> topsecret.get('Cipher', '3des-cbc')
'3des-cbc'
```

> デフォルト値は代替値よりも優先されることに注意してください。例えば上の例では、'CompressionLevel' キーは 'DEFAULT' セクションにしか存在しません。その値を 'topsecret.server.com' から取得しようとした場合、代替値を指定しても常にデフォルト値を返します:

```python
>>> topsecret.get('CompressionLevel', '3')
'9'
```

> もう一つ注意すべき点は、パーサーレベルの(訳注: ConfigParserクラスの) get() メソッドは、後方互換性のために、カスタムのより複雑なインターフェースを提供します。このメソッドを使用する際には、フォールバック値はキーワード引数としてのみ指定できる fallback 引数を介して提供されます:

```python
>>> config.get('bitbucket.org', 'monster',
...            fallback='No such things as monsters')
'No such things as monsters'
```

> 同様の fallback 引数を、getint() 、 getfloat() と getboolean() メソッドでも使えます。例えば:

```python
>>> 'BatchMode' in topsecret
False
>>> topsecret.getboolean('BatchMode', fallback=True)
True
>>> config['DEFAULT']['BatchMode'] = 'no'
>>> topsecret.getboolean('BatchMode', fallback=True)
False
```

## [14.2.4. サポートするINI ファイルの構造](https://docs.python.jp/3/library/configparser.html#supported-ini-file-structure)

> 設定ファイルは複数のセクションから構成されます。セクションは、[section] ヘッダに続いた、特定の文字列(デフォルトでは = または : [1] )で区切られたキーと値のエントリです。デフォルトでは、セクション名は大文字と小文字を区別しますが、キーはそうではありません [1]。キーと値、それぞれの先頭と末尾の空白は取り除かれます。値は省略することができ、その際でも、キーと値の区切り文字は残しておけます。値はまた、値の先頭の行より深くインデントされていれば、複数の行にまたがっても構いません。パーサーのモードによって、空白行は、複数行からなる値の一部として扱われるか、無視されます。

> 設定ファイルには先頭に特定の文字 (デフォルトでは # および ; [1]) をつけてコメントをつけることができます。コメントは、他の内容がない行に置くことができ、インデントされていても構いません。[1]

> 例えば:

```ini
[Simple Values]
key=value
spaces in keys=allowed
spaces in values=allowed as well
spaces around the delimiter = obviously
you can also use : to delimit keys from values

[All Values Are Strings]
values like this: 1000000
or this: 3.14159265359
are they treated as numbers? : no
integers, floats and booleans are held as: strings
can use the API to get converted values directly: true

[Multiline Values]
chorus: I'm a lumberjack, and I'm okay
    I sleep all night and I work all day

[No Values]
key_without_value
empty string value here =

[You can use comments]
# like this
; or this

# By default only in an empty line.
# Inline comments can be harmful because they prevent users
# from using the delimiting characters as parts of values.
# That being said, this can be customized.

    [Sections Can Be Indented]
        can_values_be_as_well = True
        does_that_mean_anything_special = False
        purpose = formatting for readability
        multiline_values = are
            handled just fine as
            long as they are indented
            deeper than the first line
            of a value
        # Did I mention we can indent comments, too?
```

## [14.2.5. 値の補間](https://docs.python.jp/3/library/configparser.html#interpolation-of-values)

> コア機能に加えて、 ConfigParser は補間(interpolation, 内挿とも)をサポートします。これは get() コールが値を返す前に、その値に対して前処理を行えることを意味します。

属性|概要
----|----
class configparser.BasicInterpolation|ConfigParser が使用するデフォルト実装です。値に、同じセクションか特別なデフォルトセクション中 [1] の他の値を参照するフォーマット文字列を含めることができます。追加のデフォルト値を初期化時に提供できます。
class configparser.ExtendedInterpolation|zc.buildout で使用されるような、より高度な文法を実装した補間ハンドラの別の選択肢です。拡張された補間は、他のセクション中の値を示すのに ${section:option} と書けます。補間は複数のレベルに及べます、利便性のために、もし section: の部分が省略されると、現在のセクションがデフォルト値となります(スペシャルセクション中のデフォルト値を使用することもできます)。

## [14.2.6. マップ型プロトコルアクセス](https://docs.python.jp/3/library/configparser.html#mapping-protocol-access)

> バージョン 3.2 で追加.

> マップ型プロトコルアクセスは、カスタムオブジェクトを辞書であるかのように使うための機能の総称です。 configparser の場合、マップ型インタフェースの実装は parser['section']['option'] 表記を使います。

> とくに、parser['section'] はパーサー内のそのセクションのデータへのプロキシを返します。つまり、値はコピーされるのではなく必要に応じてオリジナルのパーサーから取られます。さらに重要なことに、セクションのプロキシの値が変更されると、オリジナルのパーサー中の値が実際に変更されます。

> configparser は可能な限り実際の辞書と近い振る舞いをします。マップ型インタフェースは MutableMapping を矛盾なく完成します。しかし、考慮するべき違いがいくつかあります:

* デフォルトでは、セクション内の全てのキーは大文字小文字の区別なくアクセスできます [1]。例えば、for option in parser["section"] は optionxform されたオプションキー名のみを yield します。つまり小文字のキーがデフォルトです。同時に、キー 'a' を含むセクションにおいて、どちらの式も True を返します: `"a" in parser["section"]`, `"A" in parser["section"]`

* 全てのセクションは DEFAULTSECT 値を持ち、すなわちセクションで .clear() してもセクションは見た目上空になりません。これは、デフォルト値は (技術的にはそこにないので) セクションから削除できないためです。デフォルト値が上書きされた場合、それが削除されるとデフォルト値が再び見えるようになります。デフォルト値を削除しようとすると KeyError が発生します。

*  DEFAULTSECT はパーサーから取り除けません:
    * 削除しようとすると ValueError が発生します。
    * parser.clear() はこれをそのまま残し、
    * parser.popitem() がこれを返すことはありません。

* parser.get(section, option, **kwargs) - 第二引数は代替値では ありません。ただし、セクションごとの get() メソッドはマップ型プロトコルと旧式の configparser API の両方に互換です。

* parser.items() はマップ型プロトコルと互換です (DEFAULTSECT を含む section_name, section_proxy 対のリストを返します)。ただし、このメソッドは parser.items(section, raw, vars) のようにして引数を与えることでも呼び出せます。後者の呼び出しは指定された section の option, value 対のリストを、(raw=True が与えられない限り) 全ての補間を展開して返します。

> マップ型プロトコルは、既存のレガシーな API の上に実装されているので、オリジナルのインタフェースを上書きする派生クラスもまたは期待どおりにはたらきます。

## [14.2.7. パーサーの振る舞いをカスタマイズする](https://docs.python.jp/3/library/configparser.html#customizing-parser-behaviour)

> INI フォーマットの変種は、それを使うアプリケーションの数と同じくらい多く存在します。 configparser は、可能な限り広い範囲の INI スタイルを集めた集合をサポートするために、非常に役立ちます。デフォルトの機能は主に歴史的背景によって決められたので、機能によってはカスタマイズしてお使いください。

> 特定の設定パーサーのはたらきを変える最も一般的な方法は __init__() オプションを使うことです:

* defaults, デフォルト値: None

    このオプションは最初に DEFAULT セクションに加えられるキー-値の対の辞書を受け付けます。

    ヒント: 特定のセクションにデフォルト値を指定したいなら、実際のファイルを読み込む前に read_dict() を使ってください。

* dict_type, デフォルト値: collections.OrderedDict

    このオプションはマップ型プロトコルの振る舞い方や書き込まれる設定ファイルの見た目に大きく影響します。デフォルトの順序付き辞書では、全てのセクションはパーサーに加えられた順に並びます。同じことがセクション内のオプションにも言えます。

    セクションとオプションをライトバック時にソートするためなどに、別の辞書型も使えます。パフォーマンスの理由のために普通の辞書を使うこともできます。

    注意: 一度の操作でキー-値の対を複数追加する方法もあります。そのような操作に普通の辞書を使うと、キーの並び順はランダムになります。例えば:

    ```python
    >>> parser = configparser.ConfigParser()
    >>> parser.read_dict({'section1': {'key1': 'value1',
    ...                                'key2': 'value2',
    ...                                'key3': 'value3'},
    ...                   'section2': {'keyA': 'valueA',
    ...                                'keyB': 'valueB',
    ...                                'keyC': 'valueC'},
    ...                   'section3': {'foo': 'x',
    ...                                'bar': 'y',
    ...                                'baz': 'z'}
    ... })
    >>> parser.sections()
    ['section3', 'section2', 'section1']
    >>> [option for option in parser['section3']]
    ['baz', 'foo', 'bar']
    ```
    
    このような操作には、順序付き辞書を使用する方がよいです:

    ```python
    >>> from collections import OrderedDict
    >>> parser = configparser.ConfigParser()
    >>> parser.read_dict(
    ...   OrderedDict((
    ...     ('s1',
    ...      OrderedDict((
    ...        ('1', '2'),
    ...        ('3', '4'),
    ...        ('5', '6'),
    ...      ))
    ...     ),
    ...     ('s2',
    ...      OrderedDict((
    ...        ('a', 'b'),
    ...        ('c', 'd'),
    ...        ('e', 'f'),
    ...      ))
    ...     ),
    ...   ))
    ... )
    >>> parser.sections()
    ['s1', 's2']
    >>> [option for option in parser['s1']]
    ['1', '3', '5']
    >>> [option for option in parser['s2'].values()]
    ['b', 'd', 'f']

    allow_no_value, デフォルト値: False

    一部の設定ファイルには値のない設定項目がありますが、それ以外は ConfigParser がサポートする文法に従います。コンストラクタの allow_no_value 引数で、そのような値を許可することができます。

    ```python
    >>> import configparser

    >>> sample_config = """
    ... [mysqld]
    ...   user = mysql
    ...   pid-file = /var/run/mysqld/mysqld.pid
    ...   skip-external-locking
    ...   old_passwords = 1
    ...   skip-bdb
    ...   # we don't need ACID today
    ...   skip-innodb
    ... """
    >>> config = configparser.ConfigParser(allow_no_value=True)
    >>> config.read_string(sample_config)

    >>> # Settings with values are treated as before:
    >>> config["mysqld"]["user"]
    'mysql'

    >>> # Settings without values provide None:
    >>> config["mysqld"]["skip-bdb"]

    >>> # Settings which aren't specified still raise an error:
    >>> config["mysqld"]["does-not-exist"]
    Traceback (most recent call last):
      ...
    KeyError: 'does-not-exist'
    ```

* delimiters, デフォルト値: ('=', ':')

    デリミタはセクション内でキーを値から区切る部分文字列です。行中で最初に現れた区切り部分文字列がデリミタと見なされます。つまり値にはデリミタを含めることができます (キーには含めることができません)。

    ConfigParser.write() の space_around_delimiters 引数も参照してください。

* comment_prefixes, デフォルト値: ('#', ';')

* inline_comment_prefixes, デフォルト値: None

    コメント接頭辞は設定ファイル中で有効なコメントの開始を示す文字列です。comment_prefixes は他の内容がない行 (インデントは自由) にのみ使用でき、inline_comment_prefixes は任意の有効な値 (例えば、セクション名、オプション、空行も可能) の後に使えます。デフォルトではインラインコメントは無効化されていて、'#' と ';' を行全体のコメントに使用します。

    バージョン 3.2 で変更: 以前のバージョンの configparser の振る舞いは comment_prefixes=('#',';') および inline_comment_prefixes=(';',) に該当します。

    設定パーサーはコメント接頭辞のエスケープをサポートしないので、inline_comment_prefixes はユーザーがコメント接頭辞として使われる文字を含むオプション値を指定するのを妨げる可能性があります。疑わしい場合には、inline_comment_prefixes を設定しないようにしてください。どのような状況でも、複数行にわたる値で、行の先頭にコメント接頭辞文字を保存する唯一の方法は、次の例のように接頭辞を補間することです:

    ```python
    >>> from configparser import ConfigParser, ExtendedInterpolation
    >>> parser = ConfigParser(interpolation=ExtendedInterpolation())
    >>> # the default BasicInterpolation could be used as well
    >>> parser.read_string("""
    ... [DEFAULT]
    ... hash = #
    ...
    ... [hashes]
    ... shebang =
    ...   ${hash}!/usr/bin/env python
    ...   ${hash} -*- coding: utf-8 -*-
    ...
    ... extensions =
    ...   enabled_extension
    ...   another_extension
    ...   #disabled_by_comment
    ...   yet_another_extension
    ...
    ... interpolation not necessary = if # is not at line start
    ... even in multiline values = line #1
    ...   line #2
    ...   line #3
    ... """)
    >>> print(parser['hashes']['shebang'])

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    >>> print(parser['hashes']['extensions'])

    enabled_extension
    another_extension
    yet_another_extension
    >>> print(parser['hashes']['interpolation not necessary'])
    if # is not at line start
    >>> print(parser['hashes']['even in multiline values'])
    line #1
    line #2
    line #3
    ```python

* strict, デフォルト値: True

    True に設定された場合、パーサーは単一のソースから (read_file(), read_string() または read_dict() を使って) 読み込むときにセクションやオプションの重複を許さなくなります。新しいアプリケーションには strict なパーサーを使うことが推奨されます。

    バージョン 3.2 で変更: 以前のバージョンの configparser の振る舞いは strict=False に該当します。

* empty_lines_in_values, デフォルト値: True

    設定パーサーでは、キーよりもその値を深くインデントするかぎり、複数行にまたがる値を使えます。デフォルトのパーサーはさらにその値の間に空行を置けます。同時に、キーは読みやすくするため任意にインデントできます。結果として、設定ファイルが大きく複雑になったとき、ユーザーがファイル構造を見失いやすいです。この例をご覧ください:

    ```ini
    [Section]
    key = multiline
      value with a gotcha

     this = is still a part of the multiline value of 'key'
    ```

    これは特にプロポーショナルフォントを使ってファイルを編集しているユーザーにとって問題になることがあります。だから、アプリケーションの値に空行が必要ないなら、空行を認めないべきです。これによって空行で必ずキーが分かれます。上の例では、2 つのキー、key および this が作られます。

* default_section, デフォルト値: configparser.DEFAULTSECT (すなわち: "DEFAULT")

    他のセクションのデフォルト値や補間目的での特別なセクションを認める慣行はこのライブラリの明確なコンセプトの一つで、ユーザーは複雑で宣言的な設定を作成できます。このセクションは通常 "DEFAULT" と呼ばれますが、任意の有効なセクション名を指すようにカスタマイズできます。典型的な値には "general" や "common" があります。与えられた名前はソースを読み込む際にデフォルトセクションを認識するのに使われ、設定をファイルに書き戻すときにも使われます。現在の値は parser_instance.default_section 属性から取り出すことができ、実行時 (すなわちファイルを別のフォーマットに変換するとき) に変更することもできます。

* interpolation, デフォルト値: configparser.BasicInterpolation

    補間の振る舞いは、 interpolation 引数を通してカスタムハンドラを与えることでカスタマイズできます。 None 引数を使うと補間を完全に無効にできます。 ExtendedInterpolation() は、 zc.buildout に影響を受けたより高度な補間を提供します。この話題に 特化したドキュメントのセクション をご覧ください。 RawConfigParser のデフォルト値は None です。

* converters, デフォルト値: 未設定

    設定パーサーは、型変換を実行するオプションの値ゲッターを提供します。デフォルトでは、 getint()、 getfloat()、 getboolean() が実装されています。他のゲッターが必要な場合、ユーザーはそれらをサブクラスで定義するか、辞書を渡します。辞書を渡す場合、各キーはコンバーターの名前で、値は当該変換を実装する呼び出し可能オブジェクトです。例えば、 {'decimal': decimal.Decimal} を渡すと、パーサーオブジェクトとすべてのセクションプロキシの両方に、 getdecimal() が追加されます。つまり、parser_instance.getdecimal('section', 'key', fallback=0) と parser_instance['section'].getdecimal('key', 0) の両方の方法で書くことができます。

    コンバーターがパーサーの状態にアクセスする必要がある場合、設定パーサーサブクラスでメソッドとして実装することができます。このメソッドの名前が get から始まる場合、すべてのセクションプロキシで、辞書と互換性のある形式で利用できます (上記の getdecimal() の例を参照)。

> これらのパーサー引数のデフォルト値を上書きすれば、さらに進んだカスタマイズができます。デフォルトはクラスで定義されているので、派生クラスや属性の代入で上書きできます。

configparser.BOOLEAN_STATES|デフォルトでは、 getboolean() を使うことで、設定パーサーは以下の値を True と見なします: '1', 'yes', 'true', 'on' 。以下の値を False と見なします: '0', 'no', 'false', 'off' 。文字列と対応するブール値のカスタム辞書を指定することでこれを上書きできます。
configparser.optionxform(option)|このメソッドは読み込み、取得、設定操作のたびにオプション名を変換します。デフォルトでは名前を小文字に変換します。従って設定ファイルが書き込まれるとき、すべてのキーは小文字になります。それがふさわしくなければ、このメソッドを上書きしてください。
configparser.SECTCRE|セクションヘッダを解析するのに使われる、コンパイルされた正規表現です。デフォルトでは [section] が "section" という名前にマッチします。空白はセクション名の一部と見なされるので、[  larch  ] は "  larch  " という名のセクションとして読み込まれます。これがふさわしくない場合、このメソッドを上書きしてください。

## [14.2.8. レガシーな API の例](https://docs.python.jp/3/library/configparser.html#legacy-api-examples)

> 主に後方互換性問題の理由から、 configparser は get/set メソッドを明示するレガシーな API も提供します。メソッドを以下に示すように使うこともできますが、新しいプロジェクトではマップ型プロトコルでアクセスするのが望ましいです。レガシーな API は時折高度で、低レベルで、まったく直感的ではありません。

> 設定ファイルを書き出す例:

```python
import configparser

config = configparser.RawConfigParser()

# Please note that using RawConfigParser's set functions, you can assign
# non-string values to keys internally, but will receive an error when
# attempting to write to a file or when you get it in non-raw mode. Setting
# values using the mapping protocol or ConfigParser's set() does not allow
# such assignments to take place.
config.add_section('Section1')
config.set('Section1', 'an_int', '15')
config.set('Section1', 'a_bool', 'true')
config.set('Section1', 'a_float', '3.1415')
config.set('Section1', 'baz', 'fun')
config.set('Section1', 'bar', 'Python')
config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

# Writing our configuration file to 'example.cfg'
with open('example.cfg', 'w') as configfile:
    config.write(configfile)
```

> 設定ファイルを読み込む例:

```python
import configparser

config = configparser.RawConfigParser()
config.read('example.cfg')

# getfloat() raises an exception if the value is not a float
# getint() and getboolean() also do this for their respective types
a_float = config.getfloat('Section1', 'a_float')
an_int = config.getint('Section1', 'an_int')
print(a_float + an_int)

# Notice that the next output does not interpolate '%(bar)s' or '%(baz)s'.
# This is because we are using a RawConfigParser().
if config.getboolean('Section1', 'a_bool'):
    print(config.get('Section1', 'foo'))
```

> 補間するには、 ConfigParser を使ってください:


```python
import configparser

cfg = configparser.ConfigParser()
cfg.read('example.cfg')

# Set the optional *raw* argument of get() to True if you wish to disable
# interpolation in a single get operation.
print(cfg.get('Section1', 'foo', raw=False))  # -> "Python is fun!"
print(cfg.get('Section1', 'foo', raw=True))   # -> "%(bar)s is %(baz)s!"

# The optional *vars* argument is a dict with members that will take
# precedence in interpolation.
print(cfg.get('Section1', 'foo', vars={'bar': 'Documentation',
                                       'baz': 'evil'}))

# The optional *fallback* argument can be used to provide a fallback value
print(cfg.get('Section1', 'foo'))
      # -> "Python is fun!"

print(cfg.get('Section1', 'foo', fallback='Monty is not.'))
      # -> "Python is fun!"

print(cfg.get('Section1', 'monster', fallback='No such things as monsters.'))
      # -> "No such things as monsters."

# A bare print(cfg.get('Section1', 'monster')) would raise NoOptionError
# but we can also use:

print(cfg.get('Section1', 'monster', fallback=None))
      # -> None
```

> どちらの型の ConfigParsers でもデフォルト値が利用できます。使われているオプションがどこにも定義されていなければ、そのデフォルト値が補間に使われます。

```python
import configparser

# New instance with 'bar' and 'baz' defaulting to 'Life' and 'hard' each
config = configparser.ConfigParser({'bar': 'Life', 'baz': 'hard'})
config.read('example.cfg')

print(config.get('Section1', 'foo'))     # -> "Python is fun!"
config.remove_option('Section1', 'bar')
config.remove_option('Section1', 'baz')
print(config.get('Section1', 'foo'))     # -> "Life is hard!"
```

## [14.2.9. ConfigParser オブジェクト](https://docs.python.jp/3/library/configparser.html#configparser-objects)

属性|概要
----|----
class configparser.ConfigParser(defaults=None, dict_type=collections.OrderedDict, allow_no_value=False, delimiters=('=', ':'), comment_prefixes=('#', ';'), inline_comment_prefixes=None, strict=True, empty_lines_in_values=True, default_section=configparser.DEFAULTSECT, interpolation=BasicInterpolation(), converters={})|主要な設定パーサーです。defaults が与えられれば、その辞書の持つ初期値で初期化されます。dict_type が与えられれば、それがセクションの一覧、セクション中のオプション、およびデフォルト値の辞書オブジェクトを作成するのに使われます。
    defaults()|    インスタンス全体で使われるデフォルト値の辞書を返します。
    sections()|    利用できるセクションのリストを返します。default section はリストに含まれません。
    add_section(section)|    section という名のセクションをインスタンスに追加します。与えられた名前のセクション名がすでに存在したら、 DuplicateSectionError が送出されます。 default section 名が渡されたら、 ValueError が送出されます。セクションの名前は文字列でなければなりません。そうでなければ、 TypeError が送出されます。
    has_section(section)|    指名された section が設定中に存在するかを示します。default section は認識されません。
    options(section)|    指定された section 中で利用できるオプションのリストを返します。
    has_option(section, option)|    与えられた section が存在し、与えられた option を含む場合、 True を返します。それ以外の場合には、 False を返します。指定された section が None または空文字列の場合、 DEFAULT が仮定されます。
    read(filenames, encoding=None)|    ファイル名のリストを読み込んでパースしようと試みます。正常にパースできたファイル名のリストを返します。
    read_file(f, source=None)|    設定データを f から読み込んで解析します。f は Unicode 文字列を yield するイテラブル (例えばテキストモードで開かれたファイル) です。
    read_string(string, source='<string>')|    設定データを文字列から解析します。
    read_dict(dictionary, source='<dict>')|    辞書的な items() メソッドを提供する任意のオブジェクトから設定を読み込みます。キーはセクション名で、値はそのセクションに現れるキーと値をもつ辞書です。使われた辞書型が順序を保存するなら、セクションおよびそのキーは順に加えられます。値は自動で文字列に変換されます。
    get(section, option, *, raw=False, vars=None[, fallback])|    指名された section の option の値を取得します。vars が提供されるなら、それは辞書でなければならず、(与えられたなら) vars, section, DEFAULTSECT 内からこの順で option が探索されます。fallback の値として None を与えられます。
    getint(section, option, *, raw=False, vars=None[, fallback])|    指定された section 中の option を整数に型強制する補助メソッドです。 raw, vars および fallback の説明は get() を参照してください。
    getfloat(section, option, *, raw=False, vars=None[, fallback])|    指定された section 中の option を浮動小数点数に型強制する補助メソッドです。 raw, vars および fallback の説明は get() を参照してください。
    getboolean(section, option, *, raw=False, vars=None[, fallback])|    指定された section 中の option をブール値に型強制する補助メソッドです。なお、このオプションで受け付けられる値はこのメソッドが True を返す '1', 'yes', 'true', および 'on',と、このメソッドが False を返す '0', 'no', 'false', and 'off' です。その他のいかなる値も ValueError を送出します。 raw, vars および fallback の説明は get() を参照してください。
    items(raw=False, vars=None), items(section, raw=False, vars=None)|section が与えられなければ、DEFAULTSECT を含めた section_name, section_proxy の対のリストを返します。
    set(section, option, value)|    与えられたセクションが存在すれば、与えられたオプションを指定された値に設定します。そうでなければ NoSectionError を送出します。 option および value は文字列でなければなりません。そうでなければ TypeError が送出されます。
    write(fileobject, space_around_delimiters=True)|    設定の表現を指定された file object に書き込みます。 fileobject は (文字列を受け付ける) テキストモードで開かれていなければなりません。この表現は後で read() を呼び出すことでパースできます。 space_around_delimiters が真なら、キーと値の間のデリミタはスペースで囲まれます。
    remove_option(section, option)|    指定された option を指定された section から削除します。セクションが存在しなければ、 NoSectionError を送出します。オプションが存在して削除されれば、 True を返します。そうでなければ False を返します。
    remove_section(section)|    指定された section を設定から削除します。セクションが実際に存在すれば、True を返します。そうでなければ False を返します。
    optionxform(option)|    入力ファイルに現れた、またはクライアントコードで渡されたオプション名 option を内部構造で実際に使われる形式に変換します。デフォルトの実装では option の小文字版を返します。派生クラスでこれを上書きするか、クライアントコードでインスタンス上のこの名前の属性を設定して、この動作に影響を与えることができます。
    readfp(fp, filename=None)|    バージョン 3.2 で撤廃: 代わりに read_file() を使ってください。
configparser.MAX_INTERPOLATION_DEPTH|get() の raw が偽であるときの再帰的な補間の最大の深さです。これはデフォルトの interpolation を使うときのみ関係します。

## [14.2.10. RawConfigParser オブジェクト](https://docs.python.jp/3/library/configparser.html#rawconfigparser-objects)

属性|概要
----|----
class configparser.RawConfigParser(defaults=None, dict_type=collections.OrderedDict, allow_no_value=False, *, delimiters=('=', ':'), comment_prefixes=('#', ';'), inline_comment_prefixes=None, strict=True, empty_lines_in_values=True, default_section=configparser.DEFAULTSECT[, interpolation])|補間や不安全 な add_section および set メソッドがデフォルトで無効化されている、レガシーな ConfigParser の別型です。
    add_section(section)|    インスタンスに section という名のセクションを追加します。与えられた名前のセクションがすでに存在すれば、 DuplicateSectionError が送出されます。 default section 名が渡されると、 ValueError が送出されます。
    set(section, option, value)|    与えられたセクションが存在していれば、オプションを指定された値に設定します。セクションが存在しなければ NoSectionError を発生させます。 RawConfigParser (あるいは raw パラメータをセットした ConfigParser) を文字列型でない値の 内部的な 格納場所として使うことは可能ですが、すべての機能 (置換やファイルへの出力を含む) がサポートされるのは文字列を値として使った場合だけです。

## [14.2.11. 例外](https://docs.python.jp/3/library/configparser.html#exceptions)

属性|概要
----|----
exception configparser.Error|他の全ての configparser 例外の基底クラスです。
exception configparser.NoSectionError|指定したセクションが見つからなかった時に起きる例外です。
exception configparser.DuplicateSectionError|add_section() がすでに存在するセクションの名前で呼び出された場合や、strict なパーサーで単一の入力ファイル、文字列、辞書中に同じセクションが複数回現れたときに送出される例外です。
exception configparser.DuplicateOptionError|strict なパーサーで、単一の入力ファイル、文字列、辞書中に同じオプションが複数回現れたときに送出される例外です。これはミススペルや大文字小文字の区別に関係するエラー、例えば辞書の二つのキーが同じ大文字小文字の区別のない設定キーを表すこと、を捕捉します。
exception configparser.NoOptionError|指定されたオプションが指定されたセクションに見つからないときに送出される例外です。
exception configparser.InterpolationError|文字列の補間中に問題が起きた時に発生する例外の基底クラスです。
exception configparser.InterpolationDepthError|繰り返しの回数が MAX_INTERPOLATION_DEPTH を超えたために文字列補間が完了しなかったときに送出される例外です。 InterpolationError の派生クラスです。
exception configparser.InterpolationMissingOptionError|InterpolationError の派生クラスで、値が参照しているオプションが見つからない場合に発生する例外です。
exception configparser.InterpolationSyntaxError|置換がなされるソーステキストが要求された文法を満たさないときに送出される例外です。 InterpolationError の派生クラスです。
exception configparser.MissingSectionHeaderError|セクションヘッダを持たないファイルを構文解析しようとした時に起きる例外です。
exception configparser.ParsingError|ファイルの構文解析中にエラーが起きた場合に発生する例外です。

