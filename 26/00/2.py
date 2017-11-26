#http://takemikami.com/2016/06/11/loggingconfigpython.html
import logging
import logging.config
# 設定ファイル読み込み
logging.config.fileConfig('logging.conf')
# rootロガーを取得
log = logging.getLogger()
log.debug('debugメッセージ')
log.info('infoメッセージ')
log.warn('warnメッセージ')
log.error('errorメッセージ')
log.critical('criticalメッセージ')
