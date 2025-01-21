# Parallel-Processor

### Project Description
Parralel-Processor is a Python project that demonstrates complex parallel processing using multi-threading, multi-processing, task prioritization, dynamic worker allocation, and robust error handling. The project showcases efficient task management and advanced system-level optimizations for computationally intensive tasks.

### Features
- Multi-threading for concurrent task execution
- Multi-processing for parallel task execution
- Task prioritization using PriorityQueue
- Dynamic worker allocation based on system load
- Robust error handling with task retries
- Advanced logging for monitoring and debugging

### How It Works
- The `ComputeTask` class defines a computationally intensive task with a priority and retry mechanism.
- The `ParallelProcessor` class manages task execution using both multi-threading and multi-processing.
- The `TaskManager` class creates and manages tasks with priorities.
- The `dynamic_worker_allocation` function adjusts the number of workers based on system load using the `psutil` library.
- The `main` function demonstrates the creation of tasks, their prioritization, and execution using both multi-threading and multi-processing.


### Example Output
```
INFO: Task 0 with priority 9 attempt 1 started.
INFO: Task 0 completed successfully on attempt 1.
Task 0 result: 333283335000
INFO: Task 1 with priority 8 attempt 1 started.
INFO: Task 1 completed successfully on attempt 1.
Task 1 result: 333283335000
...

INFO: Executing tasks using multi-processing with dynamic worker allocation...
INFO: Task 0 with priority 9 attempt 1 started.
INFO: Task 0 completed successfully on attempt 1.
Task 0 result: 333283335000
INFO: Task 1 with priority 8 attempt 1 started.
INFO: Task 1 completed successfully on attempt 1.
Task 1 result: 333283335000
...
```

### License
This project is licensed under the MIT License
