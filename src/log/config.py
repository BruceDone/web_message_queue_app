# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger("message_app")
logger.setLevel(logging.INFO)
logging_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging_format)

logger.addHandler(console_handler)

logger.info("MESSAGE APP START NOW!")
