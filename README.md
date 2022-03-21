
# Reliable Transport Protocol

## High-Level Approach
I followed the implementation steps very closely. I set up a lot of my 
program's infrastructure to pass the level 2 tests, so the later steps were 
just a matter of adding additional fields to my packets and implementing 
additional check in my code.

In terms of program design, I have two primary classes: `Sender` and `Receiver` 
that contain most of the functionality in the program. Both have a run 
method that uses select to continuously detect new messages. When a message 
is received, helper methods verify the integrity, parse, and respond to each 
message.


## Challenges you faced
Originally, it was difficult to figure out how to get my sender and receiver 
programs to work together. I faced some issues getting my 
sender to respond to certain respond to certain events at the right time, 
and send out data packets when the window changed. However, after I 
completed the initial program infrastructure and got the level 2 tests to 
pass, implementing the later functionality didn't produce any major roadblocks.



## Features 
I implemented a highly simplified version of TCP with the following notable 
differences/features.

1. My program keeps track of the indices of packets for the sequence and ack 
   numbers instead of the number of bytes. This was more intuitive to me and 
   alleviated the needs to do calculations based on the length of the data.
2. My program sends and ACK for every individual packet. For example, 
   sending an ACK with index k implies that only packet k has been received, 
   not necessarily packets with indices < k. This allows my program to send 
   data packets in any order, and avoids the need to resend packets that 
   were successfully delivered by happen to come after a dropped packet. My 
   receiver caches out of order packets, only outputting a packet's data 
   after all other packets before have been outputted.
3. When a packet times out, the congestion window halves instead of dropping 
   to 1. Additionally, my initial slow start threshold is 15, since my 
   sender and receiver are the only devices communicating on the network. I 
   noticed that these parameters provided better performance with my tests.
4. I used the CRC-32 hashing algorithm to calculate the checksum for my 
   packets. This is the primary error detection method. Other indications of 
   corrupted packets are if the json data cannot be parsed, or json fields 
   are missing.
5. The packets that my program sends are all the same size. This might 
   result in a small performance decrease, but this was a reasonable 
   simplification in my opinion given the specifications of the simulator.



## Testing
I Just used the provided configuration files to test my code. I paid close 
attention to the total time, packets sent, and bytes sent metrics and 
adjusted some parameters of the sender program to optimize 
these to the best of my ability.
