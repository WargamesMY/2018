
import os
import sys
from Crypto.Cipher import AES

import socketserver


flag         = <HIDDEN>
aes_key      = <HIDDEN>
PADDING_SIZE = <HIDDEN>


def padding(string):
    mod = len(string) % PADDING_SIZE
    pad = PADDING_SIZE - (PADDING_SIZE if mod == 0 else mod)
    return string + "\x41"*pad


class TCPHandler(socketserver.BaseRequestHandler):

    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):

        print('[+] {} connected..'.format(self.client_address[0]))

        global aes_key
        global flag

        self.request.sendall("\n".encode())
        self.request.sendall("\n".encode())
        self.request.sendall("   ___                 _          ___     _ _ \n".encode())
        self.request.sendall("  / __\ __ _   _ _ __ | |_ ___   / __\_ _(_) |\n".encode())
        self.request.sendall(" / / | '__| | | | '_ \| __/ _ \ / _\/ _` | | |\n".encode())
        self.request.sendall("/ /__| |  | |_| | |_) | || (_) / / | (_| | | |\n".encode())
        self.request.sendall("\____/_|   \__, | .__/ \__\___/\/   \__,_|_|_|\n".encode())
        self.request.sendall("           |___/|_|                           \n".encode())
        self.request.sendall("\n".encode())
        self.request.sendall("\n".encode())
        self.request.sendall("Welcome to our service!\n".encode())
        self.request.sendall("Type anything, and we will give you encrypted version of your text.\n".encode())
        self.request.sendall("It is secure (using AES-ECB 128-bit encryption), so.... no worries!!!\n".encode())
        self.request.sendall("\n".encode())

        while True:

            # get user input
            self.request.sendall("Enter your input : ".encode())
            self.data = self.request.recv(16384).strip()

            if not self.data:
                print("[-] {} disconnected.".format(self.client_address[0]))
                break

            print("[+] {} sent '{}'..".format(self.client_address[0], self.data.decode('utf-8')))
            
            aes_input = self.data.decode('utf-8') + flag        # magic!
            aes_input = padding(aes_input)                      # pad if not within PADDING_SIZE block-size

            # encrypt your input with the most secure algorithm ever!
            cipher = AES.new(aes_key.encode(), AES.MODE_ECB)
            encrypted_text = cipher.encrypt(aes_input.encode())

            str_data = "Your encrypted text (in hex): {}\n\n".format(encrypted_text.hex())

            self.request.sendall(str_data.encode())


def main():

    DEFAULT_PORT = 5000

    if len(sys.argv) > 1:
        DEFAULT_PORT = sys.argv[1]

    HOST, PORT = "0.0.0.0", DEFAULT_PORT

    # Create the server, binding to all interface on port specified by DEFAULT_PORT or sys.argv[1]
    server = socketserver.TCPServer((HOST, PORT), TCPHandler)

    print('Listening on port {}..'.format(PORT))

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()


if __name__ == '__main__':
    main()
