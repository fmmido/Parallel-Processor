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

class ComputeTask:
    def __init__(self, task_id, priority=0, retries=3):
        self.task_id = task_id
        self.priority = priority
        self.retries = retries

    def run(self):
        attempt = 0
        while attempt < self.retries:
            try:
                attempt += 1
                # Simulate a computationally intensive task
                logging.info(f"Task {self.task_id} with priority {self.priority} attempt {attempt} started.")
                time.sleep(random.uniform(0.1, 0.5))
                result = sum(i * i for i in range(10000))
                logging.info(f"Task {self.task_id} completed successfully on attempt {attempt}.")
                return f"Task {self.task_id} result: {result}"
            except Exception as e:
                logging.error(f"Task {self.task_id} failed on attempt {attempt}: {e}")
        logging.error(f"Task {self.task_id} failed after {self.retries} attempts.")
        return None

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

class TaskManager:
    def __init__(self, num_tasks):
        self.num_tasks = num_tasks
        self.task_queue = PriorityQueue()

    def create_tasks(self):
        for i in range(self.num_tasks):
            priority = random.randint(1, 10)
            task = ComputeTask(i, priority)
            self.task_queue.put((priority, task))

    def get_tasks(self):
        tasks = []
        while not self.task_queue.empty():
            tasks.append(self.task_queue.get()[1])
        return tasks

def dynamic_worker_allocation():
    # Simulate dynamic worker allocation based on system load
    load = psutil.getloadavg()[0]  # Get the 1-minute load average
    cpu_count = multiprocessing.cpu_count()
    max_workers = max(1, int(cpu_count / (load + 1)))
    return max_workers

def main():
    num_tasks = 20  # Increase the number of tasks to demonstrate robustness
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
    main(
