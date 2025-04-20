from logging import getLogger,FileHandler, Formatter,DEBUG,ERROR

formatter=Formatter('[%(levelname)s] %(asctime)s-%(message)s (%(filename)s)')
logger=getLogger(__name__)

handler=FileHandler('log2.txt')
handler.setLevel(DEBUG)
handler.setFormatter(formatter)

error_handler=FileHandler('error.txt')
error_handler.setLevel(ERROR)
error_handler.setFormatter(formatter)

logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.addHandler(error_handler)

logger.info('プログラムが開始しました')
logger.debug('入力値は1000です')
logger.warning('ファイルの容量が2000を超えました')
logger.error('ファイルが存在していません')