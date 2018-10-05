# -*- coding: iso-8859-1 -*-

import logging
from logging.handlers import RotatingFileHandler

import module_a

# Path con el nombre del archivo o solo el nombre
log_file_name = 'app.log'

logger = logging.getLogger('logger_principal')
logger.setLevel(logging.DEBUG)

# Revisar los distintos tipos y opciones en:
# https://docs.python.org/3/library/logging.handlers.html
rfh = RotatingFileHandler(log_file_name, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=False)
rfh.setLevel(logging.DEBUG)

# La lista de atributos completa está acá: https://docs.python.org/3/library/logging.html#logrecord-attributes
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
rfh.setFormatter(formatter)

logger.addHandler(rfh)


if __name__ == '__main__':
	logger.debug('Bienvenidos a la aplicación de log.')
	logger.info('Esta aplicación demuestra como se utiliza un logger al que se le aplica un ' + \
				'RotatingFileHandler, lo que provoca que los archivos de log roten en función ' + \
				'de su tamaño.')

	module_a.someFunction('Hola')
	logger.debug('Volví después de llamar a una función.')
