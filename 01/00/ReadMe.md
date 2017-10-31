# [13.4. lzma — LZMA アルゴリズムを使用した圧縮](https://docs.python.jp/3/library/lzma.html)

< [13. データ圧縮とアーカイブ](https://docs.python.jp/3/library/archiving.html) < [Python 標準ライブラリ](https://docs.python.jp/3/library/index.html#the-python-standard-library) < [ドキュメント](https://docs.python.jp/3/index.html)

ソースコード: [Lib/lzma.py](https://github.com/python/cpython/tree/3.6/Lib/lzma.py)

> このモジュールは LZMA 圧縮アルゴリズムを使用したデータ圧縮および展開のためのクラスや便利な関数を提供しています。また、xz ユーティリティを使用した .xz およびレガシーな .lzma ファイル形式へのファイルインターフェイスの他、RAW 圧縮ストリームもサポートしています。

> このモジュールが提供するインターフェイスは bz2 モジュールと非常によく似ています。ただし、LZMAFile は (bz2.BZ2File と異なり) スレッドセーフではない点に注意してください。単一の LZMAFile インスタンスを複数スレッドから使用する場合は、ロックで保護する必要があります。

属性|概要
----|----
exception lzma.LZMAError|この例外は圧縮あるいは展開中にエラーが発生した場合、または圧縮/展開状態の初期化中に送出されます。

## [13.4.1. 圧縮ファイルへの読み書き](https://docs.python.jp/3/library/lzma.html#reading-and-writing-compressed-files)

属性|概要
----|----
lzma.open(filename, mode="rb", *, format=None, check=-1, preset=None, filters=None, encoding=None, errors=None, newline=None)|LZMA 圧縮ファイルをバイナリまたはテキストモードでオープンし、ファイルオブジェクト を返します。
class lzma.LZMAFile(filename=None, mode="r", *, format=None, check=-1, preset=None, filters=None)|LZMA 圧縮ファイルをバイナリモードで開きます。
    peek(size=-1)|    ファイル上の現在位置を変更せずにバッファのデータを返します。EOF に達しない限り、少なくとも 1 バイトが返されます。返される正確なバイト数は規定されていません (引数 size は無視されます)。

## [13.4.2. メモリ上での圧縮と展開](https://docs.python.jp/3/library/lzma.html#compressing-and-decompressing-data-in-memory)

属性|概要
----|----
class lzma.LZMACompressor(format=FORMAT_XZ, check=-1, preset=None, filters=None)|データをインクリメンタルに圧縮する圧縮オブジェクトを作成します。
    compress(data)|    data (bytes オブジェクト) を圧縮し、少なくともその一部が圧縮されたデータを格納する bytes オブジェクトを返します。data の一部は、後で compress() および flush() の呼び出しに使用するため内部でバッファされている場合があります。返すデータは以前の compress() 呼び出しの出力を連結したものです。
    flush()|    圧縮処理を終了し、コンプレッサの内部バッファにあるあらゆるデータを格納する bytes オブジェクトを返します。
class lzma.LZMADecompressor(format=FORMAT_AUTO, memlimit=None, filters=None)|データをインクリメンタルに展開するために使用できる展開オブジェクトを作成します。
    decompress(data, max_length=-1)|    data (bytes-like object) を展開し、未圧縮のデータを bytes で返します。 data の一部は、後で decompress() の呼び出しに使用するため内部でバッファされている場合があります。 返すデータは以前の decompress() 呼び出しの出力を全て連結したものです。
    check|    入力ストリームに使用されるインテグリティチェックの ID です。これは何のインテグリティチェックが使用されているか決定するために十分な入力がデコードされるまでは CHECK_UNKNOWN になることがあります。
    eof|    ストリーム終端記号に到達した場合 True を返します。
    unused_data|    圧縮ストリームの末尾以降に存在したデータを表します。
    needs_input|    decompress() メソッドが、新しい非圧縮入力を必要とせずにさらに展開データを提供できる場合、 False です。
lzma.compress(data, format=FORMAT_XZ, check=-1, preset=None, filters=None)|data (bytes オブジェクト) を圧縮し、圧縮データを bytes オブジェクトとして返します。
lzma.decompress(data, format=FORMAT_AUTO, memlimit=None, filters=None)|data (bytes オブジェクト) を展開し、展開データを bytes オブジェクトとして返します。


## [13.4.3. その他](https://docs.python.jp/3/library/lzma.html#miscellaneous)

属性|概要
----|----
lzma.is_check_supported(check)|指定したインテグリティチェックがシステムでサポートされていれば真を返します。

## [13.4.4. カスタムフィルタチェインの指定](https://docs.python.jp/3/library/lzma.html#specifying-custom-filter-chains)

> フィルタチェイン指定子は、辞書のシーケンスで、各辞書は ID と単一フィルタのオプションからなります。各辞書はキー "id" を持たなければならず、フィルタ依存のオプションを指定する追加キーを持つ場合もあります。有効なフィルタ ID は以下のとおりです:

* 圧縮フィルタ:
    * FILTER_LZMA1 (FORMAT_ALONE と共に使用)
    * FILTER_LZMA2 (FORMAT_XZ および FORMAT_RAW と共に使用)
* デルタフィルター:
    * FILTER_DELTA
* ブランチコールジャンプ (BCJ) フィルター:
    * FILTER_X86
    * FILTER_IA64
    * FILTER_ARM
    * FILTER_ARMTHUMB
    * FILTER_POWERPC
    * FILTER_SPARC

> 一つのフィルタチェインは 4 個までのフィルタを定義することができ、空にはできません。チェインの最後は圧縮フィルタでなくてはならず、その他のフィルタはデルタまたは BCJ フィルタでなければなりません。

> 圧縮フィルタは以下のオプション (追加エントリとしてフィルタを表す辞書に指定) をサポートしています:

* preset: 明示されていないオプションのデフォルト値のソースとして使用する圧縮プリセット。
* dict_size: 辞書のサイズのバイト数。これは、 4 KiB から 1.5 GiB の間にしてください (両端を含みます)。
* lc: リテラルコンテキストビットの数。
* lp: リテラル位置ビットの数。lc + lp で最大 4 までです。
* pb: 位置ビットの数。最大で 4 までです。
* mode: MODE_FAST または MODE_NORMAL。
* nice_len: マッチに "良い" とみなす長さ。273 以下でなければなりません。
* mf: 使用するマッチファインダ – MF_HC3、MF_HC4、MF_BT2、MF_BT3、または MF_BT4。
* depth: マッチファインダが使用する検索の最大深度。0 (デフォルト) では他のフィルタオプションをベースに自動選択します。

> デルタフィルターは、バイト間の差異を保存し、特定の状況で、コンプレッサーに対してさらに反復的な入力を生成します。 デルタフィルターは、1 つのオプション dist のみをサポートします。 これは差し引くバイトどうしの距離を示します。 デフォルトは 1 で、隣接するバイトの差異を扱います。

> The BCJ filters are intended to be applied to machine code. They convert relative branches, calls and jumps in the code to use absolute addressing, with the aim of increasing the redundancy that can be exploited by the compressor. These filters support one option, start_offset. This specifies the address that should be mapped to the beginning of the input data. The default is 0.

> (BCJフィルタは、機械コードに適用されることを意図しています。 コンプレッサーが利用できる冗長性を高める目的で、コード内の相対分岐、呼び出し、およびジャンプを絶対アドレッシングを使用して変換します。 これらのフィルタは、1つのオプションstart_offsetをサポートしています。 これは、入力データの先頭にマップするアドレスを指定します。 デフォルトは0です。)

## [13.4.5. 使用例](https://docs.python.jp/3/library/lzma.html#examples)

圧縮ファイルからの読み込み:

```python
import lzma
with lzma.open("file.xz") as f:
    file_content = f.read()
```

圧縮ファイルの作成:

```python
import lzma
data = b"Insert Data Here"
with lzma.open("file.xz", "w") as f:
    f.write(data)
```

メモリ上でデータを圧縮:

```python
import lzma
data_in = b"Insert Data Here"
data_out = lzma.compress(data_in)
```

逐次圧縮:

```python
import lzma
lzc = lzma.LZMACompressor()
out1 = lzc.compress(b"Some data\n")
out2 = lzc.compress(b"Another piece of data\n")
out3 = lzc.compress(b"Even more data\n")
out4 = lzc.flush()
# Concatenate all the partial results:
result = b"".join([out1, out2, out3, out4])
```

すでにオープンしているファイルへの圧縮データの書き出し:

```python
import lzma
with open("file.xz", "wb") as f:
    f.write(b"This data will not be compressed\n")
    with lzma.open(f, "w") as lzf:
        lzf.write(b"This *will* be compressed\n")
    f.write(b"Not compressed\n")
```

カスタムフィルタチェインを使った圧縮ファイルの作成:

```python
import lzma
my_filters = [
    {"id": lzma.FILTER_DELTA, "dist": 5},
    {"id": lzma.FILTER_LZMA2, "preset": 7 | lzma.PRESET_EXTREME},
]
with lzma.open("file.xz", "w", filters=my_filters) as f:
    f.write(b"blah blah blah")
```

私の環境では使えなかった。以下のエラーが出る。

```python
ModuleNotFoundError: No module named '_lzma'
```
