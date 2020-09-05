from client.client import client
from server.server import server
import logging
import logging.handlers
from datetime import datetime
import threading


def set_logging_params():

    log_time_format = "%Y%m%d_%H_%M_%S"
    log_format = '%(asctime)-15s %(message)s'
    log_filename = f'logs/{datetime.now().strftime(log_time_format)}.log'
    handler = logging.handlers.RotatingFileHandler(
        log_filename, maxBytes=1*1024, backupCount=1)
    open(log_filename, 'w+')
    logging.basicConfig(filename=log_filename, format=log_format, level=logging.INFO)
    logger = logging.getLogger('globalLogger')
    logger.addHandler(handler)


def create_server():
    logging.info("starting the server")
    this_server = server()
    this_server.serv()


def create_client():
    logging.info("starting the client")
    this_client = client()
    this_client.recv()


def main():
    threads = (create_client, create_server)
    threads = list(map(lambda x:threading.Thread(target=x), threads))
    for thread in threads:
        thread.start()



if __name__ == "__main__":
    set_logging_params()
    main()
