#http://lab.hde.co.jp/2008/02/pythonlogging.html
import logging
import logging.config
# 設定ファイル読み込み
logging.config.fileConfig('logging_file.conf')
# rootロガーを取得
log = logging.getLogger('sub2')
log.debug('debugメッセージ')
log.info('infoメッセージ')
log.warn('warnメッセージ')
log.error('errorメッセージ')
log.critical('criticalメッセージ')
