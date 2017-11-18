# [16.3. time — 時刻データへのアクセスと変換](https://docs.python.jp/3/library/time.html)

< [16. 汎用オペレーティングシステムサービス](https://docs.python.jp/3/library/allos.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

32bitマシン上でのエポックタイムには、いわゆる2038年問題がある。

> このモジュールでは、時刻に関するさまざまな関数を提供します。関連した機能について、datetime, calendar モジュールも参照してください。

> このモジュールは常に利用可能ですが、すべての関数がすべてのプラットフォームで利用可能なわけではありません。このモジュールで定義されているほとんどの関数は、プラットフォーム上の同名の C ライブラリ関数を呼び出します。これらの関数に対する意味付けはプラットフォーム間で異なるため、プラットフォーム提供のドキュメントを読んでおくと便利でしょう。

> まずいくつかの用語の説明と慣習について整理します。

* エポック (epoch) は時刻の起点のことで、これはプラットフォーム依存です。 Unix では、エポックは (UTC で) 1970 年 1 月 1 日 0 時 0 分 0 秒です。 与えられたプラットフォームでエポックが何なのかを知るには、 time.gmtime(0) の値を見てください。

* エポック秒 (seconds since the epoch) は、エポックからの総経過秒数を示していますが、たいていはうるう秒 (leap seconds) は含まれていません。 全ての POSIX 互換のプラットフォームで、うるう秒はこの総秒数には含まれません。

* このモジュールの中の関数は、エポック以前あるいは遠い未来の日付や時刻を扱うことができません。将来カットオフ（関数が正しく日付や時刻を扱えなくなる）が起きる時点は、C ライブラリによって決まります。32-bit システムではカットオフは通常 2038 年です。

* 2000年問題 (Y2K): Python はプラットフォームの C ライブラリに依存しています。C ライブラリは日付および時刻をエポックからの経過秒で表現するので、一般的に 2000 年問題は存在しません。関数 strptime() は %y 書式コードが与えられた時に 2 桁の年表記を解析できます。2 桁の年を解析する場合、それらは POSIX および ISO C 標準に従って変換されます: 69-99 の西暦年は 1969-1999 となり、0–68 の西暦年は 2000–2068 になります。

* UTC は協定世界時 (Coordinated Universal Time) のことです (以前はグリニッジ標準時または GMT として知られていました)。UTC の頭文字の並びは誤りではなく、英仏の妥協によるものです。

* DST は夏時間 (Daylight Saving Time) のことで、一年のうちの一定期間に 1 時間タイムゾーンを修正することです。DST のルールは不可思議で (地域ごとに法律で定められています)、年ごとに変わることもあります。C ライブラリはローカルルールを記したテーブルを持っており (柔軟に対応するため、たいていはシステムファイルから読み込まれます)、この点に関しては唯一の真実の知識の源です。

* 多くの現時刻を返す関数 (real-time functions) の精度は、値や引数を表現するために使う単位から想像されるよりも低いかも知れません。例えば、ほとんどの Unix システムにおいて、クロックの 1 ティックの精度は 50 から 100 分の 1 秒に過ぎません。

* 一方、time() および sleep() は Unix の同等の関数よりましな精度を持っています。時刻は浮動小数点数で表され、time() は可能なかぎり最も正確な時刻を (Unix の gettimeofday() があればそれを使って) 返します。また sleep() にはゼロでない端数を与えることができます (Unix の select() があれば、それを使って実装しています)。

* gmtime(), localtime(), strptime() が返す時刻値、および asctime(), mktime(), strftime() がとる時刻値は 9 個の整数からなるシーケンスです。gmtime(), localtime(), strptime() の戻り値は個々の値を属性名で取得することもできます。

* これらのオブジェクトについての解説は struct_time を参照してください。

* バージョン 3.3 で変更: struct_time オブジェクトは、プラットフォームが、対応する struct tm メンバーをサポートしている場合、tm_gmtoff および tm_zone 属性が拡張されるようになりました。

* バージョン 3.6 で変更: struct_time の属性 tm_gmtoff および tm_zone が全てのプラットフォームで利用できるようになりました。


> 時間の表現を変換するには、以下の関数を利用してください:

対象|変換先|関数
----|------|----
エポックからの秒数|UTC の struct_time|gmtime()
エポックからの秒数|ローカル時間の struct_time|localtime()
UTC の struct_time|エポックからの秒数|calendar.timegm()
ローカル時間の struct_time|エポックからの秒数|mktime()

## [16.3.1. 関数]()

属性|概要
----|----
time.asctime([t])|gmtime() や localtime() が返す時刻を表現するタプルまたは struct_time を、'Sun Jun 20 23:21:05 1993' といった書式の文字列に変換します。t が与えられていない場合には、localtime() が返す現在の時刻が使われます。asctime() はロケール情報を使いません。
time.clock()|Unix では、現在のプロセッサー時間秒を浮動小数点数で返します。時刻の精度および "プロセッサー時間" の定義そのものは同じ名前の C 関数に依存します。
time.clock_getres(clk_id)|Return the resolution (precision) of the specified clock clk_id. Refer to Clock ID Constants for a list of accepted values for clk_id.
time.clock_gettime(clk_id)|Return the time of the specified clock clk_id. Refer to Clock ID Constants for a list of accepted values for clk_id.
time.clock_settime(clk_id, time)|Set the time of the specified clock clk_id. Currently, CLOCK_REALTIME is the only accepted value for clk_id.
time.ctime([secs])|エポックからの経過秒数で表現された時刻を、ローカルの時刻を表現する文字列に変換します。secs を指定しないか None を指定した場合、time() が返す値を現在の時刻として使用します。ctime(secs) は asctime(localtime(secs)) と等価です。ローカル情報は ctime() には使用されません。
time.get_clock_info(name)|指定されたクロックの情報を名前空間オブジェクトとして取得します。サポートされているクロック名およびそれらの値を取得する関数は以下の通りです: 'clock': time.clock(), 'monotonic': time.monotonic(), 'perf_counter': ime.perf_counter(), 'process_time': time.process_time(), 'time': time.time()
time.gmtime([secs])|エポックからの経過時間で表現された時刻を、UTC で struct_time に変換します。このとき dst フラグは常にゼロとして扱われます。secs を指定しないか None を指定した場合、time() が返す値を現在の時刻として使用します。秒の端数は無視されます。struct_time オブジェクトについては前述の説明を参照してください。calendar.timegm() はこの関数と逆の変換を行います。
time.localtime([secs])|gmtime() に似ていますが、ローカル時間に変換します。secs を指定しないか None を指定した場合、time() が返す値を現在の時刻として使用します。DST が適用されている場合は dst フラグには 1 が設定されます。
time.mktime(t)|localtime() の逆を行う関数です。引数は struct_time か 9 個の要素すべての値を持つ完全なタプル (dst フラグも必要です; 時刻に DST が適用されるか不明の場合は -1 を使用してください) で、UTC ではなく ローカル 時間を指定します。戻り値は time() との互換性のために浮動小数点数になります。入力した値を正しい時刻として表現できない場合、例外 OverflowError または ValueError が送出されます (どちらが送出されるかは、無効な値を受け取ったのが Python と下層の C ライブラリのどちらなのかによって決まります)。この関数で時刻を生成できる最も古い日付はプラットフォームに依存します。
time.monotonic()|モノトニッククロックの値 (小数点以下がミリ秒) を返します。戻り値の基準点は定義されていませんが、このクロックは値が後戻りすることはなく、システムクロックの更新の影響も受けません。すなわち、モノトニック時間の重要な点はその値ではなく、値が厳密に増加していくことが保証されている点です。このため、正しい利用法は、呼び出した 2 点間の時間差を計測することです。
time.perf_counter()|パフォーマンスカウンターの値 (小数点以下がミリ秒) を返します。クロックは短期間の計測が行えるよう、可能な限り高い分解能をもちます。これにはスリープ中の経過時間も含まれ、システム全体で一意です。
time.process_time()|現在のプロセスのシステムおよびユーザー CPU 時間の合計値 (小数点以下はミリ秒) を返します。プロセスごとに定義され、スリープ中の経過時間は含まれません。戻り値の参照点は定義されていないため、正しい利用法は、呼び出した 2 点間の時間差を計測することです。
time.sleep(secs)|与えられた秒数の間、呼び出したスレッドの実行を停止します。より精度の高い実行停止時間を指定するために、引数は浮動小数点にしてもかまいません。何らかのシステムシグナルがキャッチされた場合、それに続いてシグナル処理ルーチンが実行され、sleep() を停止します。従って実際の実行停止時間は要求した時間よりも短くなるかもしれません。また、システムが他の処理をスケジュールするために、実行停止時間が要求した時間よりも多少長い時間になることもあります。
time.strftime(format[, t])|gmtime() や localtime() が返す時刻値タプルまたは struct_time を、format で指定した文字列形式に変換します。t が与えられていない場合、localtime() が返す値を現在の時刻として使用します。format は文字列でなくてはなりません。t のいずれかのフィールドが許容範囲外の数値であった場合、ValueError を送出します。
time.strptime(string[, format])|時刻を表現する文字列を書式に従って解釈します。返される値は gmtime() や localtime() が返すような struct_time です。
class time.struct_time|gmtime(), localtime() および strptime() が返す時刻値シーケンスの型です。これは名前付きタプル (named tuple) のインタフェースをもったオブジェクトです。値はインデックスでも属性名でもアクセス可能です。以下の値があります:
time.time()|エポック からの秒数を浮動小数点数で返します。 エポックの具体的な日付とうるう秒 (leap seconds) の扱いはプラットフォーム依存です。 Windows とほとんどの Unix システムでは、エポックは (UTC で) 1970 年 1 月 1 日 0 時 0 分 0 秒で、うるう秒はエポック秒の時間の勘定には入りません。 これは一般に Unix 時間 と呼ばれています。 与えられたプラットフォームでエポックが何なのかを知るには、 time.gmtime(0) の値を見てください。
time.tzset()|ライブラリで使われている時刻変換規則をリセットします。どのように行われるかは、環境変数 TZ で指定されます。


class time.struct_timeは、gmtime(), localtime() および strptime() が返す時刻値シーケンスの型です。

インデックス|属性|値
------------|----|--
0|tm_year|(例えば 1993)
1|tm_mon|[1,12] の間の数
2|tm_mday|[1,31] の間の数
3|tm_hour|[0,23] の間の数
4|tm_min|[0,59] の間の数
5|tm_sec|[0,61] の間の数 strftime() の説明にある (2) を読んで下さい
6|tm_wday|[0,6] の間の数、月曜が 0 になります
7|tm_yday|[1,366] の間の数
8|tm_isdst|0, 1 または -1; 以下を参照してください
N/A|tm_zone|タイムゾーンの短縮名
N/A|tm_gmtoff|UTC から東方向へのオフセット (秒)

> time.strftime(format[, t])のformat 文字列には以下のディレクティブ (指示語) を埋め込むことができます。

ディレクティブ|意味|注釈
--------------|----|----
%a|ロケールの短縮された曜日名になります。| 
%A|ロケールの曜日名になります。| 
%b|ロケールの短縮された月名になります。| 
%B|ロケールの月名になります。| 
%c|ロケールの日時を適切な形式で表します。| 
%d|月中の日にちの 10 進表記になります [01,31]。| 
%H|時 (24 時間表記) の 10 進表記になります [00,23]。| 
%I|時 (12 時間表記) の 10 進表記になります [01,12]。| 
%j|年中の日にちの 10 進表記になります [001,366]。| 
%m|月の 10 進表記になります [01,12]。| 
%M|分の 10 進表記になります [00,59]。| 
%p|ロケールの AM もしくは PM と等価な文字列になります。|(1)
%S|秒の 10 進表記になります [00,61]。|(2)
%U|年の初めから何週目か (日曜を週の始まりとします) を表す 10 進数になります [00,53]。年が明けてから最初の日曜日までのすべての曜日は 0 週目に属すると見なされます。|(3)
%w|曜日の 10 進表記になります [0 (日曜日),6]。| 
%W|年の初めから何週目か (月曜を週の始まりとします) を表す 10 進数になります [00,53]。年が明けてから最初の月曜日までの全ての曜日は 0 週目に属すると見なされます。|(3)
%x|ロケールの日付を適切な形式で表します。| 
%X|ロケールの時間を適切な形式で表します。| 
%y|西暦の下 2 桁の 10 進表記になります [00,99]。| 
%Y|西暦 ( 4桁) の 10 進表記を表します。| 
%z|タイムゾーンと UTC/GMT との時差を表す正または負の時間を +HHMM、-HHMM で表します。H は時間の、M は分の 10 進表記になります [-23:59, +23:59]。| 
%Z|タイムゾーンの名前を表します (タイムゾーンがない場合には空文字列)。| 
%%|文字 '%' を表します。| 

## [16.3.2. Clock ID Constants](https://docs.python.jp/3/library/time.html#clock-id-constants)

> These constants are used as parameters for clock_getres() and clock_gettime().

属性|概要
----|----
time.CLOCK_HIGHRES|The Solaris OS has a CLOCK_HIGHRES timer that attempts to use an optimal hardware source, and may give close to nanosecond resolution. CLOCK_HIGHRES is the nonadjustable, high-resolution clock.
time.CLOCK_MONOTONIC|設定不可で、モノトニック時刻 (不特定のエポックからの単調増加な時刻) を表します。
time.CLOCK_MONOTONIC_RAW|CLOCK_MONOTONIC と似ていますが、NTP の影響を受けていない、ハードウェアベースの時刻へのアクセスを提供します。
time.CLOCK_PROCESS_CPUTIME_ID|CPU による高分解能のプロセスごとのタイマーです。
time.CLOCK_THREAD_CPUTIME_ID|スレッド固有の CPU タイムクロックです。
time.CLOCK_REALTIME|システム全体のリアルタイムクロックです。このクロックを設定するには適切な権限が必要です。

## [16.3.3. Timezone Constants](https://docs.python.jp/3/library/time.html#timezone-constants)

タイムゾーンに関してはサードパーティ製ライブラリ pytz を使ったほうが良さそう。

属性|概要
----|----
time.altzone|The offset of the local DST timezone, in seconds west of UTC, if one is defined. This is negative if the local DST timezone is east of UTC (as in Western Europe, including the UK). Only use this if daylight is nonzero. See note below.
time.daylight|Nonzero if a DST timezone is defined. See note below.
time.timezone|The offset of the local (non-DST) timezone, in seconds west of UTC (negative in most of Western Europe, positive in the US, zero in the UK). See note below.
time.tzname|A tuple of two strings: the first is the name of the local non-DST timezone, the second is the name of the local DST timezone. If no DST timezone is defined, the second string should not be used. See note below.

### 注釈

> For the above Timezone constants (altzone, daylight, timezone, and tzname), the value is determined by the timezone rules in effect at module load time or the last time tzset() is called and may be incorrect for times in the past. It is recommended to use the tm_gmtoff and tm_zone results from localtime() to obtain timezone information.

### 参考

モジュール|概要
----------|----
[datetime](https://docs.python.jp/3/library/datetime.html#module-datetime)|日付と時刻に対する、よりオブジェクト指向のインタフェースです。
[locale](https://docs.python.jp/3/library/locale.html#module-locale)|国際化サービスです。ロケールの設定は strftime() および strptime() の多くの書式指定子の解釈に影響を及ぼします。
[calendar](https://docs.python.jp/3/library/calendar.html#module-calendar)|一般的なカレンダーに関する関数群です。timegm() はこのモジュールの gmtime() の逆を行う関数です。

### 脚注

> [1]	%Z の使用は現在非推奨です。ただし、ここで実現したい時間および分オフセットへの展開を行ってくれる %z エスケープはすべての ANSI C ライブラリでサポートされているわけではありません。また、1982 年に提出されたオリジナルの RFC 822 標準では西暦の表現を 2 桁とするよう要求している (%Y でなく%y ) ものの、実際には 2000 年になるだいぶ以前から 4 桁の西暦表現に移行しています。その後 RFC 822 は撤廃され、4 桁の西暦表現は RFC 1123 で初めて勧告され、RFC 2822 において義務付けられました。
