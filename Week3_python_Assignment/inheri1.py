import numpy as np

# Base class
class TestReport:
    def __init__(self, execution_times):
        self.execution_times = execution_times

    def average_time(self):
        return np.mean(self.execution_times)

    def max_time(self):
        return np.max(self.execution_times)

# Subclass
class RegressionReport(TestReport):
    def __init__(self, execution_times):
        super().__init__(execution_times)

    def slow_tests(self, threshold):
        return self.execution_times[self.execution_times > threshold]


# Main section
if __name__ == "__main__":
    # Create a NumPy array with 10 execution times
    times = np.array([1.2, 3.5, 2.8, 4.0, 5.6, 0.9, 7.2, 6.3, 2.1, 3.9])

    # Create a RegressionReport object
    report = RegressionReport(times)

    # Display average, max, and slow tests
    print("Execution Times:", times)
    print("Average Execution Time:", report.average_time())
    print("Maximum Execution Time:", report.max_time())
    print("Slow Tests (> 4.0):", report.slow_tests(4.0))
