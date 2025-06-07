# src/logger.py

import logging
import os

# Ensure the logs directory exists
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Setup the logger
logger = logging.getLogger("superhero_logger")
logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler(os.path.join(log_dir, "superhero.log"))
file_handler.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)
