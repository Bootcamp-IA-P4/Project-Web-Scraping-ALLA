import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s',
        handlers=[
            logging.FileHandler('logs.log', mode='a', encoding='utf-8'),  # guardamos logs en logs.log
        ]
    )

setup_logging()

def get_logger(name):
    return logging.getLogger(name)
