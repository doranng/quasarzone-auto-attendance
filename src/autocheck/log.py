import logging


def create_log(results):
    for result in results:
        if result['result'] == 'fail':
            logging.error('[' + result['netloc'] + '] ' + result['msg'])