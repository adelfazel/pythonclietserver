import logging
import socket
from time import sleep
import asyncio


class client():
    def __init__(self, port=1234, header_size=10):
        logging.info("init the client")
        self.header_size = header_size
        self.port = port
        self.socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    async def connect_to_server(self):
        attempt = 1
        while True:
            try:
                self.socketObject.connect((socket.gethostname(), self.port))
                break
            except Exception as e:
                logging.info(f"client attempting to connect {attempt}:{e}")
                attempt += 1
                await asyncio.sleep(1)
        logging.info("client init successful")

    def get_message_size(self, msg):
        return int(msg[:self.header_size])

    def handle_request(self):
        header = self.socketObject.recv(self.header_size).decode('utf-8')
        logging.info(f"reciever- header: {header}")
        message_size = self.get_message_size(header)
        msg = self.socketObject.recv(message_size).decode('utf-8')
        logging.log(f"msg: {msg} of size {message_size} received")

    async def recv(self):
        try:
            await self.connect_to_server()
            await self.handle_request()

        except:
            print("unable to receive messgae")

