import socket
import random
import logging
import asyncio
HEADERSIZE = 10

logger = logging.getLogger('globalLogger')


class server():
    def __init__(self, port=1234, loop=None):
        self.loop = loop or asyncio.get_event_loop()
        self.socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketObject.bind((socket.gethostname(), port))
        self.socketObject.listen()
        logging.info("server started")

    def add_header(self, msg):
        return f'{len(msg):<{HEADERSIZE}}' + msg

    def generate_message(self):
        return f"Welcome to the server random message is {random.randint(20, 30) * random.randint(20, 30)}"

    async def handle_request(self):
        logging.info(f"waiting for connections to come")
        while True:
            try:
                self.clientsocket, self.address = self.socketObject.accept()
                break
            except:
                logging.info(f"waiting even more")
                await asyncio.sleep(1)
        logging.info(f"recieved requeset form {self.address} connection established")

    def send_message(self):
        msg = self.add_header(self.generate_message())
        logging.info(f"attempting to send {msg}")
        self.clientsocket.send(bytes(msg, "utf-8"))

    async def serv(self):
        await self.handle_request()
        while True:
            try:
                self.send_message()
                await asyncio.sleep(1)
            except Exception as e:
                await asyncio.sleep(1)
                logging(f"server cannot send message:{e}")
