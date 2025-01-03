# Chapter 5

## concurrent_futures_pooling

### Explaination:
This code compares the performance of sequential execution, thread pool execution, and process pool execution using the `concurrent.futures` module. It defines a `count` function, which performs a CPU-intensive operation (an empty loop) for each item in a list, and an `evaluate` function that calls `count` and prints the result. First, the tasks are executed sequentially by iterating through the list. Next, a `ThreadPoolExecutor` is used to run the tasks concurrently in multiple threads, and a `ProcessPoolExecutor` is employed to run them in multiple processes. The execution time for each method is measured and printed, highlighting the speed differences between sequential, threaded, and multiprocessing approaches.

### Output:
![Ergonomic](images/chair.png "Ergonomic ")


## coroutine

### Explaination:
This code simulates a Finite State Machine (FSM) using Python's `asyncio` library with coroutines to handle state transitions asynchronously. It defines five asynchronous functions (`start_state`, `state1`, `state2`, `state3`, and `end_state`), where each function represents a state in the FSM. When `start_state` is called, it randomly decides whether to transition to `state1` or `state2`. Each state function generates an output message and randomly decides the next state based on the transition value (0 or 1), eventually leading to the `end_state` where the process halts. The `time.sleep(1)` calls simulate time delays, but they should ideally be replaced with `await asyncio.sleep(1)` to avoid blocking the event loop, allowing other tasks to run concurrently. The `asyncio.get_event_loop()` is used to run the FSM starting from the `start_state` and orchestrates the state transitions.

### Output:
![Ergonomic](images/chair.png "Ergonomic ")

## dealing

### Explaination:
This script demonstrates using `asyncio` with `Future` objects to run two asynchronous tasks concurrently. The `first_coroutine` computes the sum of the first `num` integers, while the `second_coroutine` calculates the factorial of `num`. The script takes two command-line arguments (`num1` and `num2`) which are passed to the coroutines. Each coroutine uses `await asyncio.sleep()` to simulate a time delay and makes the computation non-blocking. The results of the computations are set into `Future` objects (`future1` and `future2`). After the coroutines are executed, `add_done_callback` is used to invoke `got_result`, which prints the result from the `Future`. The `asyncio.get_event_loop()` manages the event loop, and `loop.run_until_complete()` ensures both tasks run concurrently. The script terminates once both tasks are complete and the results are printed.

### Output:
![Ergonomic](images/chair.png "Ergonomic ")


## concurrent_futures_pooling

### Explaination:
This code compares the performance of sequential execution, thread pool execution, and process pool execution using the `concurrent.futures` module. It defines a `count` function, which performs a CPU-intensive operation (an empty loop) for each item in a list, and an `evaluate` function that calls `count` and prints the result. First, the tasks are executed sequentially by iterating through the list. Next, a `ThreadPoolExecutor` is used to run the tasks concurrently in multiple threads, and a `ProcessPoolExecutor` is employed to run them in multiple processes. The execution time for each method is measured and printed, highlighting the speed differences between sequential, threaded, and multiprocessing approaches.

### Output:
![Ergonomic](images/chair.png "Ergonomic ")


## concurrent_futures_pooling

### Explaination:
This code compares the performance of sequential execution, thread pool execution, and process pool execution using the `concurrent.futures` module. It defines a `count` function, which performs a CPU-intensive operation (an empty loop) for each item in a list, and an `evaluate` function that calls `count` and prints the result. First, the tasks are executed sequentially by iterating through the list. Next, a `ThreadPoolExecutor` is used to run the tasks concurrently in multiple threads, and a `ProcessPoolExecutor` is employed to run them in multiple processes. The execution time for each method is measured and printed, highlighting the speed differences between sequential, threaded, and multiprocessing approaches.

### Output:
![Ergonomic](images/chair.png "Ergonomic ")


## concurrent_futures_pooling

### Explaination:
This code compares the performance of sequential execution, thread pool execution, and process pool execution using the `concurrent.futures` module. It defines a `count` function, which performs a CPU-intensive operation (an empty loop) for each item in a list, and an `evaluate` function that calls `count` and prints the result. First, the tasks are executed sequentially by iterating through the list. Next, a `ThreadPoolExecutor` is used to run the tasks concurrently in multiple threads, and a `ProcessPoolExecutor` is employed to run them in multiple processes. The execution time for each method is measured and printed, highlighting the speed differences between sequential, threaded, and multiprocessing approaches.

### Output:
![Ergonomic](images/chair.png "Ergonomic ")


## concurrent_futures_pooling

### Explaination:
This code compares the performance of sequential execution, thread pool execution, and process pool execution using the `concurrent.futures` module. It defines a `count` function, which performs a CPU-intensive operation (an empty loop) for each item in a list, and an `evaluate` function that calls `count` and prints the result. First, the tasks are executed sequentially by iterating through the list. Next, a `ThreadPoolExecutor` is used to run the tasks concurrently in multiple threads, and a `ProcessPoolExecutor` is employed to run them in multiple processes. The execution time for each method is measured and printed, highlighting the speed differences between sequential, threaded, and multiprocessing approaches.

### Output:
![Ergonomic](images/chair.png "Ergonomic ")
