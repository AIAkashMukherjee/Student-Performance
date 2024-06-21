import os
import logging
from datetime import datetime

# Format datetime for log file name
LOG_FILE = f'{datetime.now().strftime("%m %d %Y %H %M")}.log'

log_path=os.path.join(os.getcwd(),'logs',LOG_FILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO

)

logger=logging.getLogger(__name__)


if __name__ == '__main__':
    logging.info('Logging Started')
