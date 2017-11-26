#http://symfoware.blog68.fc2.com/blog-entry-885.html
import logging
import logging.handlers
#rootロガーを取得
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
#出力のフォーマットを定義
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#メールを送信するハンドラーを定義
"""
sh = logging.handlers.SMTPHandler(
    mailhost='mailhost.example.com',
    fromaddr='from@example.com',
    toaddrs=['toadmin@example.com'],
    subject='SMTPHandlerから送信されるメールのタイトル'
)
"""
#https://www.yahoo-help.jp/app/answers/detail/p/622/a_id/80574/~/%E3%83%A1%E3%83%BC%E3%83%AB%E3%82%BD%E3%83%95%E3%83%88%E3%81%A7%E9%80%81%E5%8F%97%E4%BF%A1%E3%81%99%E3%82%8B%E3%81%AB%E3%81%AF%EF%BC%88yahoo%21%E3%83%A1%E3%83%BC%E3%83%AB%E3%82%A2%E3%83%89%E3%83%AC%E3%82%B9%E3%81%AE%E5%A0%B4%E5%90%88%EF%BC%89
sh = logging.handlers.SMTPHandler(
    mailhost='smtp.mail.yahoo.co.jp',
    fromaddr='*********@yahoo.co.jp',
    toaddrs=['*********@yahoo.co.jp'],
    subject='SMTPHandlerから送信されるメールのタイトル'
)

sh.setLevel(logging.DEBUG)
sh.setFormatter(formatter)
#rootロガーにハンドラーを登録する
#OSError: [Errno 113] No route to host
logger.addHandler(sh)
logger.debug('debugメッセージ')
logger.info('infoメッセージ')
logger.warn('warnメッセージ')
logger.error('errorメッセージ')
logger.critical('criticalメッセージ')
