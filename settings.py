import logging

settings = {
    'api_id': '',
    'email': '',
    'password': '',
    'user_id': ''
}

LOG_FORMAT = '%(asctime)s\n\n --- %(del_len)s %(deletions)s\n +++ %(ins_len)s %(insertions)s\n'
logger = logging.getLogger('main')

logger.setLevel(logging.INFO)
hdlr = logging.FileHandler('main.log')
formatter = logging.Formatter(LOG_FORMAT)
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
