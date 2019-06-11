# python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Data Structure

week 1-3 Network packet processing simulation

In this problem you will implement a program to simulate the processing of network packets.

You are given a series of incoming network packets, and your task is to simulate their processing.
Packets arrive in some order. For each packet number 𝑖, you know the time when it arrived 𝐴𝑖 and the
time it takes the processor to process it 𝑃𝑖 (both in milliseconds). There is only one processor, and it
processes the incoming packets in the order of their arrival. If the processor started to process some
packet, it doesn’t interrupt or stop until it finishes the processing of this packet, and the processing of
packet 𝑖 takes exactly 𝑃𝑖 milliseconds.
The computer processing the packets has a network buffer of fixed size 𝑆. When packets arrive, they are stored in the buffer before being processed. However, if the buffer is full when a packet
arrives (there are 𝑆 packets which have arrived before this packet, and the computer hasn’t finished
processing any of them), it is dropped and won’t be processed at all. If several packets arrive at the
same time, they are first all stored in the buffer (some of them may be dropped because of that —
those which are described later in the input). The computer processes the packets in the order of
their arrival, and it starts processing the next available packet from the buffer as soon as it finishes
processing the previous one. If at some point the computer is not busy, and there are no packets in
the buffer, the computer just waits for the next packet to arrive. Note that a packet leaves the buffer
and frees the space in the buffer as soon as the computer finishes processing it.
"""

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def process(self, request):
        # write your code here
        reponse = ''

        while len(self.finish_time) > 0 and self.finish_time[0] <= request.arrived_at:
            self.finish_time.popleft()

        if len(self.finish_time) == 0:
            new_finish_time = request.arrived_at + request.time_to_process
            response = Response(False, request.arrived_at )
            if new_finish_time != 0:
                self.finish_time.append(new_finish_time)
        elif len(self.finish_time) < self.size:
            new_start_time = self.finish_time[-1]
            new_finish_time = new_start_time + request.time_to_process
            self.finish_time.append(new_finish_time)
            response = Response(False, new_start_time)
        else:
            response = Response(True, -1)
        #print(response)

        return response


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        #print(request)
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))
    #print(requests)

    buffer = Buffer(buffer_size)
    #print(buffer.finish_time)

    if n_requests == 0:
            responses = None
    else:
        responses = process_requests(requests, buffer)
    #print(responses)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()