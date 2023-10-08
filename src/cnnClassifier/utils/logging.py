import logging
from datetime import datetime
from pathlib import Path


def log(file_object:Path, log_message:str) -> None:
    """
        Logs a message to a file using the Python logging module.

        Args:
            file_object (str): The name of the file to log the message to.
            log_message (str): The message to be logged.

        Raises:
            ValueError: If file_object or log_message is None or empty.

        Returns:
            None
    """
    if not file_object or not log_message:
        raise ValueError('file_object and log_message cannot be None or empty')
    try:
        now = datetime.now()
        date = now.date()
        current_time = now.strftime("%H:%M:%S")
        
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger()

        file_handler = logging.FileHandler(filename=file_object)
        logger.addHandler(file_handler)
        logging.info(f'{date}\t{current_time}\t{log_message}')
        
    except Exception as e:
        raise e
    