from logging import getLogger, FileHandler,Formatter,DEBUG

formatter=Formatter('[%(levelname)s]%(asctime)s (%(filename)s)')
logger = getLogger(__name__)
handler=FileHandler('log.txt')
handler.setLevel(DEBUG)
handler.setFormatter(formatter)
logger.setLevel(DEBUG)
logger.addHandler(handler)


logger.debug('入力値は1000です')
logger.error('ファイルが存在していません')