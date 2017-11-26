#http://symfoware.blog68.fc2.com/blog-entry-885.html
import logging
import logging.handlers
#rootロガーを取得
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
#出力のフォーマットを定義
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#ログファイルをTCPソケット経由で出力するハンドラーを定義
sh = logging.handlers.SocketHandler(
    host='localhost',
    port=12345
)
sh.setLevel(logging.DEBUG)
sh.setFormatter(formatter)
#rootロガーにハンドラーを登録する
logger.addHandler(sh)
logger.debug('debugメッセージ')
logger.info('infoメッセージ')
logger.warn('warnメッセージ')
logger.error('errorメッセージ')
logger.critical('criticalメッセージ')
