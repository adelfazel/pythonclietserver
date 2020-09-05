import logging
import socket
from time import sleep

class client():
    def __init__(self, port=1234, header_size=10):
        logging.info("client:init the client")
        self.header_size = header_size
        self.port = port
        self.socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        attempt = 1
        while True:
            try:
                self.socketObject.connect((socket.gethostname(), self.port))
                break
            except Exception as e:
                logging.info(f"client attempting to connect {attempt}:{e}")
                attempt += 1
                sleep(1)
        logging.info("client: client init successful")

    def get_message_size(self, msg):
        return int(msg[:self.header_size])

    def handle_request(self):
        header = self.socketObject.recv(self.header_size).decode('utf-8')
        message_size = self.get_message_size(header)
        logging.info(f"client: message size is {message_size}")
        msg = self.socketObject.recv(message_size).decode('utf-8')
        logging.info(f"client: msg: {msg} of size {message_size} received")

    def recv(self):
        self.connect_to_server()
        while True:
            try:
                self.handle_request()
            except Exception as e:
                logging.info(f"client: unable to receive messgae, {e}")
            sleep(1)
