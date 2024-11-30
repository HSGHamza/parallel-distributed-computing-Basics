# Python Multithreading and Parallelism Examples

This repository contains Python code examples demonstrating concepts in inter-process communication, parallel programming, and multithreading. The examples are grouped into two chapters, each addressing different aspects of these programming paradigms.

## 📁 Folder Structure and Descriptions

### Chapter1: Parallelism and Inter-Process Communication (IPC)
This chapter focuses on running multiple processes in parallel, sharing data between them, and synchronizing their tasks. It also includes examples of task parallelism and solving computational problems like generating Fibonacci numbers.

#### Files and Explanations:
- **IPC.py**: Explores how processes can communicate with each other using mechanisms like pipes, queues, and shared memory.
- **Mpi.py**: Introduces Message Passing Interface (MPI), a protocol often used in distributed computing to coordinate processes.
- **Multi_process.py**: Demonstrates the basics of using Python's `multiprocessing` module to run multiple processes simultaneously.
- **PCnM.py**: Implements the producer-consumer problem using multiprocessing, showcasing how to manage shared resources effectively.
- **Parallelism.py**: Explains parallelism concepts with practical examples, highlighting the differences between concurrency and parallel execution.
- **Shared_mem.py**: Demonstrates how to use shared memory to exchange data between processes.
- **Sync.py**: Covers synchronization techniques, such as locks, to prevent race conditions when multiple processes access shared data.
- **Task_parallelism.py**: Shows how to distribute different tasks across multiple processes for faster execution.
- **fibonacci.py**: Uses multiprocessing to compute Fibonacci numbers in a parallel fashion, showcasing computational efficiency.
- **pipe.py**: Demonstrates communication between processes using Python's `Pipe` object.
- **hello.txt**: A supplementary text file for reference or notes related to the code in this chapter.

---

### Chapter2: Multithreading
This chapter explores threading, a way to achieve concurrency by running multiple threads within a single process. It covers synchronization primitives, thread-safe communication, and advanced threading techniques.

#### Files and Explanations:
- **Barrier.py**: Introduces barriers, a synchronization primitive used to block threads until all threads reach a specific point.
- **Condition.py**: Explains condition variables, which allow threads to wait until notified by another thread.
- **Event.py**: Shows how threads can communicate using event objects to signal readiness or completion.
- **MyThreadClass.py**: Defines a custom thread class to encapsulate thread behavior and functionality.
- **MyThreadClass_lock.py**: Demonstrates the use of locks to avoid race conditions when multiple threads access shared resources.
- **MyThreadClass_lock_2.py**: Expands on locking techniques with more complex examples of thread synchronization.
- **Rlock.py**: Introduces reentrant locks (`RLock`), which allow a thread to acquire the same lock multiple times without causing a deadlock.
- **Semaphore.py**: Explains semaphores, which limit the number of threads that can access a resource at the same time.
- **Thread_definition.py**: Provides a basic introduction to creating and starting threads.
- **Thread_determine.py**: Explores how to assign and determine specific tasks for individual threads.
- **Thread_name_and_processes.py**: Illustrates how to name threads and differentiate them from processes.
- **Threading_with_queue.py**: Demonstrates the use of thread-safe queues for inter-thread communication, ensuring data consistency.
- **hello.txt**: A supplementary text file for notes or references related to the multithreading examples.

---

## 🚀 How to Use

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/HSGHamza/parallel-distributed-computing-Basics