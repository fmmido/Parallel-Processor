# Parallel-Processor

### Project Description
Parallel-Processor is a Python project that demonstrates complex parallel processing techniques using multi-threading and multi-processing, combined with task prioritization, dynamic worker allocation, and robust error handling. This project showcases how to efficiently manage and execute computationally intensive tasks using advanced system-level optimizations. It also includes implementations of common sorting algorithms (bubble sort and quick sort) and a divide-and-conquer summation algorithm for the computational tasks.

### Features
- Multi-threading for concurrent task execution using ThreadPoolExecutor.
- Multi-processing for parallel task execution using multiprocessing.Pool.
- Task prioritization using PriorityQueue, implementing a Shortest Job First (SJF) approach.
- Dynamic worker allocation based on system load using the `psutil` library.
- Robust error handling with task retries.
- Advanced logging for monitoring and debugging.
- Includes sorting algorithms: bubble sort and quick sort.
- Includes a divide-and-conquer summation algorithm.

### How It Works
- The `ComputeTask` class defines a computational task that uses sorting or a divide-and-conquer approach, with a priority and retry mechanism.
- The `ParallelProcessor` class manages task execution using both multi-threading and multi-processing.
- The `TaskManager` class creates and manages tasks with priorities, using a Shortest Job First logic.
- The `dynamic_worker_allocation` function adjusts the number of workers based on system load using the `psutil` library.
- The `main` function demonstrates the creation of tasks, their prioritization, and execution using both multi-threading and multi-processing.
- The tasks utilize either a sorting algorithm (quick sort or bubble sort - though bubble sort is not actively used, the function is there for potential modifications) or a divide-and-conquer based summation for its computations.

### Example Output
content_copy
download
Use code with caution.
Markdown

INFO: Executing tasks using multi-threading with 3 workers...
INFO: Task 1 with priority 6 attempt 1 started.
INFO: Task 1: Data sum computed successfully.
Task 1 sum result: 5197
INFO: Task 2 with priority 6 attempt 1 started.
INFO: Task 2: Data sum computed successfully.
Task 2 sum result: 5045
INFO: Task 3 with priority 1 attempt 1 started.
INFO: Task 3: Data sorted successfully.
Task 3 sorted data: [11, 12, 14, 14, 18]...
...

INFO: Executing tasks using multi-processing with dynamic worker allocation...
INFO: Task 1 with priority 6 attempt 1 started.
INFO: Task 1: Data sum computed successfully.
Task 1 sum result: 5197
INFO: Task 2 with priority 6 attempt 1 started.
INFO: Task 2: Data sum computed successfully.
Task 2 sum result: 5045
INFO: Task 3 with priority 1 attempt 1 started.
INFO: Task 3: Data sorted successfully.
Task 3 sorted data: [11, 12, 14, 14, 18]...
...

### License
This project is licensed under the MIT License.
content_copy
download
Use code with caution.
