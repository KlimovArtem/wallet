import logging
from pathlib import Path

from logging import Logger, FileHandler

logger: Logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

SERVER_LOG_DIR = Path("/var/log")
DEFAULT_LOG_DIR = Path(__file__).resolve().parents[0] / "log"
debug_handler: FileHandler = logging.FileHandler(
        SERVER_LOG_DIR / "app_debug.log" if SERVER_LOG_DIR.exists() else LOG_DIR / "app_debug.log"
)
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s'))
logger.addHandler(debug_handler)
