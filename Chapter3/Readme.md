# Chapter 3

## Communication with pipe
### Explanation:
in this code their are two functions, first function takes a pipe and fills it with 0-9 numbers,second funtion takes two pipes, it takes input from first pipe and squares them and sends it second pipe as output pipe
in last main function 2 pipes and 2 process are made first pipe and process call the first function and second pipe and process call second function and both unused ends of pipes are closed and then pipes the output pipe values are printed

### Output
![Communication with pipe](Chapter3/images/CommunicationWithPipe.PNG "image1")

## Communication with queue
### Explanation:
In this code, there are two classes and a main function. The first class, `producer`, inherits from `multiprocessing.Process`. It takes a queue as input and appends 10 random integers (between 0 and 256) to the queue. Each addition is printed along with the queue size, and it sleeps for 1 second after each operation. 

The second class, `consumer`, also inherits from `multiprocessing.Process`. It takes the same queue as input and continuously removes and prints items from the queue until the queue is empty. It checks if the queue is empty and breaks the loop if true, sleeping for 1 second between operations.

In the main function, a shared multiprocessing queue is created. Two processes, `process_producer` and `process_consumer`, are created from the `producer` and `consumer` classes, respectively. Both processes are started and joined, ensuring they complete their tasks before the program ends.

### Output
![Communication with pipe](Chapter3/images/CommunicationWithPipe.PNG "image1")
