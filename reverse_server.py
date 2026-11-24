# Part 4 (STRETCH) - a TCP server that sends back the REVERSED message.
#
# There is no automated test for this - run it, then connect with the provided
# client.py (in another terminal) to check it, and show it to your lab instructor.
#
# The socket setup is written for you; fill in the one TODO.

import socket

HOST, PORT = "127.0.0.1", 50011

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Listening on {HOST}:{PORT} (Ctrl-C to stop)")

    while True:
        conn, addr = server.accept()
        with conn:
            data = conn.recv(1024)
            if not data:
                continue
            # (optional) Outline:
            # Decode the received bytes into a string.
            # Reverse the string by using slicing to read the characters in reverse order.
            # Encode the reversed message into bytes.
            # Send the reversed message back to the client.
            # TODO: send the message back REVERSED. `data` is bytes, e.g. b"hello".
            #   Turn it into text, reverse it, and send the reversed text back with
            #   conn.sendall(...). Example: "hello" -> "olleh".
            message = data.decode()
            conn.sendall(message[::-1].encode())
            pass

if __name__ == "__main__":
    main()