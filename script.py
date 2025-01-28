import concurrent.futures
import multiprocessing
import time
import random
import logging
import os
import psutil
from queue import PriorityQueue

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Sorting Algorithms
def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [x for x in data[1:] if x < pivot]
    right = [x for x in data[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Divide and Conquer Algorithm
def divide_and_conquer_sum(data):
    if len(data) == 1:
        return data[0]
    mid = len(data) // 2
    left_sum = divide_and_conquer_sum(data[:mid])
    right_sum = divide_and_conquer_sum(data[mid:])
    return left_sum + right_sum

# Task class
class ComputeTask:
    def __init__(self, task_id, priority=0, retries=3, data=None):
        self.task_id = task_id
        self.priority = priority
        self.retries = retries
        self.data = data or [random.randint(1, 100) for _ in range(100)]

    def run(self):
        attempt = 0
        while attempt < self.retries:
            try:
                attempt += 1
                logging.info(f"Task {self.task_id} with priority {self.priority} attempt {attempt} started.")
                
                # Choose a computation type (sorting or summing)
                if random.choice(["sort", "sum"]) == "sort":
                    sorted_data = quick_sort(self.data)
                    logging.info(f"Task {self.task_id}: Data sorted successfully.")
                    return f"Task {self.task_id} sorted data: {sorted_data[:5]}..."
                else:
                    result = divide_and_conquer_sum(self.data)
                    logging.info(f"Task {self.task_id}: Data sum computed successfully.")
                    return f"Task {self.task_id} sum result: {result}"
            except Exception as e:
                logging.error(f"Task {self.task_id} failed on attempt {attempt}: {e}")
        logging.error(f"Task {self.task_id} failed after {self.retries} attempts.")
        return None

# Parallel Processing Class
class ParallelProcessor:
    def __init__(self, max_workers=None):
        self.max_workers = max_workers or multiprocessing.cpu_count()

    def execute_tasks(self, tasks):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = list(executor.map(self._execute_task, tasks))
        return results

    def _execute_task(self, task):
        return task.run()

    def execute_tasks_multiprocessing(self, tasks):
        with multiprocessing.Pool(processes=self.max_workers) as pool:
            results = pool.map(self._execute_task, tasks)
        return results

# Task Manager with Shortest Job First
class TaskManager:
    def __init__(self, num_tasks):
        self.num_tasks = num_tasks
        self.task_queue = PriorityQueue()

    def create_tasks(self):
        for i in range(self.num_tasks):
            # Assign priority based on "shortest job first" logic (lower = higher priority)
            priority = random.randint(1, 10)
            data_size = random.randint(50, 500)  # Simulate job size
            task = ComputeTask(i, priority, data=[random.randint(1, 100) for _ in range(data_size)])
            self.task_queue.put((priority, task))

    def get_tasks(self):
        tasks = []
        while not self.task_queue.empty():
            tasks.append(self.task_queue.get()[1])
        return tasks

# Dynamic Worker Allocation
def dynamic_worker_allocation():
    load = psutil.getloadavg()[0]
    cpu_count = multiprocessing.cpu_count()
    max_workers = max(1, int(cpu_count / (load + 1)))
    return max_workers

# Main Function
def main():
    num_tasks = 20
    task_manager = TaskManager(num_tasks)
    task_manager.create_tasks()
    tasks = task_manager.get_tasks()

    max_workers = dynamic_worker_allocation()
    processor = ParallelProcessor(max_workers=max_workers)

    logging.info(f"Executing tasks using multi-threading with {max_workers} workers...")
    results = processor.execute_tasks(tasks)
    for result in results:
        if result:
            print(result)

    logging.info("\nExecuting tasks using multi-processing with dynamic worker allocation...")
    results_mp = processor.execute_tasks_multiprocessing(tasks)
    for result in results_mp:
        if result:
            print(result)

if __name__ == "__main__":
    main()
