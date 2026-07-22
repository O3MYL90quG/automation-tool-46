import time

class PerformanceOptimizer:
    def __init__(self, threshold=0.1):
        self.threshold = threshold
        self.last_time = time.time()

    def monitor_performance(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > self.threshold:
                print(f"Performance Warning: '{func.__name__}' took {elapsed_time:.4f} seconds")
            return result
        return wrapper

    @staticmethod
    def optimize_data_structure(data):
        if isinstance(data, list) and len(data) > 1000:
            return set(data)
        return data

@PerformanceOptimizer().monitor_performance
def long_running_task(data):
    time.sleep(0.2)  # Simulated work
    return data

if __name__ == '__main__':
    result = long_running_task([i for i in range(1500)])
    optimized_data = PerformanceOptimizer.optimize_data_structure(result)
    print(optimized_data)