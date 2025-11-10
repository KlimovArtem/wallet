import logging
from logging import FileHandler, Logger

logger: Logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

debug_handler: FileHandler = logging.FileHandler("logs/app_debug.log")
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s'))

logger.addHandler(debug_handler)