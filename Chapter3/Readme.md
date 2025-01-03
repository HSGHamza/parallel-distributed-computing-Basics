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

## derom
### Explanation:
In this code there is one function foo and a main function. The foo function is executed by each process and behaves differently based on the process name. The foo function first retrieves the current process name. If the process name is background_process it prints numbers from 0 to 4 with a 1-second delay between prints. If the process name is non_background_process it prints numbers from 5 to 8 with a 1-second delay. The function announces when the process starts and ends. In the main function two processes are created background_process with the name 'background_process' set as a daemon process and non_background_process with the name 'non_background_process' set as a non-daemon process. Both processes are started. The non-background process continues to run independently until completion while the background process runs briefly and terminates when the main program ends due to its daemon nature. A delay time.sleep(2) is added to allow the daemon process to execute briefly before the program exits.
### Output
![Communication with pipe](Chapter3/images/CommunicationWithPipe.PNG "image1")


## killing_processes
### Explanation:
In this code there is a function foo and a main function. The foo function prints a starting message and then iterates through numbers 0 to 9 printing each number with a 1-second delay between iterations. It ends with a finished message. In the main function a process p is created with the target function foo. The state of the process is printed before starting it. The process is started and its running state is printed. The process is then terminated and its state is printed again. After termination the process is joined and its state is printed once more. Finally the process's exit code is printed to indicate its termination status.
### Output
![Communication with pipe](Chapter3/images/CommunicationWithPipe.PNG "image1")


## naming_processes
### Explanation:
In this code there is a function myFunc and a main function. The myFunc function retrieves the name of the current process and prints a starting message with the process name. It then sleeps for 3 seconds before printing an exiting message with the process name. In the main function two processes are created. The first process, process_with_name, is explicitly given the name 'myFunc process' and targets the myFunc function. The second process, process_with_default_name, uses the default naming scheme and also targets the myFunc function. Both processes are started, and the program waits for each process to complete using the join method.
### Output
![Communication with pipe](Chapter3/images/CommunicationWithPipe.PNG "image1")


## process_in_subclass
### Explanation:
In this code there is a class MyProcess and a main function. The MyProcess class inherits from multiprocessing.Process and overrides the run method. The run method prints a message indicating it has been called along with the name of the process. In the main function a loop runs 10 times. In each iteration a new process is created using the MyProcess class. The process is started which triggers the run method and then the program waits for the process to complete using the join method.
### Output
![Communication with pipe](Chapter3/images/CommunicationWithPipe.PNG "image1")
