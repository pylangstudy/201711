#http://symfoware.blog68.fc2.com/blog-entry-885.html
import logging
import logging.handlers
#rootロガーを取得
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
#出力のフォーマットを定義
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#ログファイルをHTTP通信で送信するハンドラーを定義
httph = logging.handlers.HTTPHandler(
    host='localhost:8080',
    url='/updatelog',
    method='POST'
)
httph.setLevel(logging.DEBUG)
httph.setFormatter(formatter)
#rootロガーにハンドラーを登録する
logger.addHandler(httph)
logger.debug('debugメッセージ')
logger.info('infoメッセージ')
logger.warn('warnメッセージ')
logger.error('errorメッセージ')
logger.critical('criticalメッセージ')
