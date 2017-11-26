#http://symfoware.blog68.fc2.com/blog-entry-885.html
import logging
import logging.handlers
#rootロガーを取得
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
#出力のフォーマットを定義
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#ログファイルをUDPソケット経由で出力するハンドラーを定義
dh = logging.handlers.DatagramHandler(
    host='localhost',
    port=12345
)
dh.setLevel(logging.DEBUG)
dh.setFormatter(formatter)
#rootロガーにハンドラーを登録する
logger.addHandler(dh)
logger.debug('debugメッセージ')
logger.info('infoメッセージ')
logger.warn('warnメッセージ')
logger.error('errorメッセージ')
logger.critical('criticalメッセージ')
