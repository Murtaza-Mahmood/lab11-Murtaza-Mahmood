# Intermediate programming practice: async and sockets.
#
# For EACH problem, work out your problem-solving OUTLINE first, then implement it (you
# may use an AI assistant to help - see the README). The async parts must actually run
# their work CONCURRENTLY (that's the whole point), not one after another.
#
# Do not rename the functions - the tests use these names.

import asyncio
import socket

async def gather_doubled(numbers):
    # Outline (write your plan here first):
    # Create an asynchronous function that takes a number and returns it multiplied by 2.
    # Create an empty list to store the coroutines.
    # Loop through each number and add its corresponding coroutine to the list.
    # Use asyncio.gather() to run all the coroutines concurrently.
    # Return the results as a list in the same order as the original numbers.
    # TODO (Part 1, async): run one async task per number that returns n * 2, all
    #   CONCURRENTLY with asyncio.gather, and return the results as a list in the same
    #   order as `numbers`.
    async def double_number(n):
        return n * 2
    tasks = []
    for number in numbers:
        tasks.append(double_number(number))
    results = await asyncio.gather(*tasks)
    return results

async def fastest(jobs):
    # Outline:
    # Create an asynchronous function that takes a label and delay.
    # Use await asyncio.sleep(delay) to pause the job for the given amount of time.
    # Return the label once the job finishes.
    # Create an empty list to store the coroutines.
    # Loop through each job and add its corresponding coroutine to the list.
    # Use asyncio.as_completed() to run the jobs concurrently and get them in completion order.
    # Return the label of the first job to finish.
    # TODO (Part 2, async): `jobs` is a list of (label, delay) pairs. Start them all
    #   concurrently - each one just does `await asyncio.sleep(delay)` - and return the
    #   label of the FIRST job to finish. (Hint: asyncio.as_completed.)
    async def run_job(label, delay):
        await asyncio.sleep(delay)
        return label
    tasks = []
    for label, delay in jobs:
        tasks.append(run_job(label, delay))
    for task in asyncio.as_completed(tasks):
        result = await task
        return result

def echo_once(host, port, message):
    # Outline:
    # Create a socket to establish a connection with the server.
    # Connect to the server using the given host and port.
    # Encode the message into bytes and send it to the server.
    # Receive the server's reply as bytes.
    # Decode the reply into a string.
    # Return the decoded reply.
    # TODO (Part 3, sockets): open a TCP socket and connect to (host, port). Send
    #   `message` (encode it to bytes first), receive the server's reply, and return it
    #   as a string. (Hint: socket.socket, .connect, .sendall, .recv, .decode.)
    with socket.socket() as client:
        client.connect((host, port))
        client.sendall(message.encode())
        reply = client.recv(1024)
        return reply.decode()

def main():
    # Optional scratch space - try the async parts here, e.g.:
    # print(asyncio.run(gather_doubled([1, 2, 3, 4])))   # [2, 4, 6, 8]
    pass

if __name__ == "__main__":
    main()