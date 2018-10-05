# -*- coding: iso-8859-1 -*-

import logging

logger = logging.getLogger('logger_principal')


def someFunction(someArg):
	logger.debug('Estoy adentro de someFunction()')
	return someArg
