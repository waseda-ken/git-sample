from logging import getLogger, StreamHandler,Formatter,DEBUG

formatter=Formatter('[%(levelname)s]%(asctime)s (%(filename)s)')
logger = getLogger(__name__)
handler=StreamHandler()
handler.setLevel(DEBUG)
handler.setFormatter(formatter)
logger.setLevel(DEBUG)
logger.addHandler(handler)


logger.debug('入力値は1000です')
logger.error('ファイルが存在していません')