# backend/config/logging.py

import logging
from backend.config.settings import settings

def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(settings.logging_level)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Add console handler
    ch = logging.StreamHandler()
    ch.setLevel(settings.logging_level)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


logger = get_logger()