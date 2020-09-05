from client.client import client
from server.server import server
import asyncio
import logging
from datetime import datetime


def set_logging_params():
    log_time_format = "%Y%m%d_%H_%M_%S"
    log_format = '%(asctime)-15s %(message)s'
    log_filename = f'logs/{datetime.now().strftime(log_time_format)}.log'
    open(log_filename, 'w+')
    logging.basicConfig(filename=log_filename, format=log_format, level=logging.INFO)
    logging.getLogger('globalLogger')


async def create_server():
    logging.info("starting the server")
    this_server = server()
    await this_server.serv()


async def create_client():
    logging.info("starting the client")
    this_client = client()
    await this_client.recv()

async def main():
    tasks = (create_client(), create_server())
    await asyncio.wait(map(loop.create_task, tasks))

if __name__ == "__main__":
    set_logging_params()
    try:
        loop = asyncio.get_event_loop()
        loop.set_debug(1)
        loop.run_until_complete(main())
    except Exception as e:
        pass
    finally:
        loop.close()
