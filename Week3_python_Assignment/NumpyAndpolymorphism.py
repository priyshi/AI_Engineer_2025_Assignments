import numpy as np

class ManualTester:
    def analyze(self, data):
        """Prints the first 5 test execution times"""
        print(f"Manual Tester Analysis - First 5 execution times: {data[:5]}")

class AutomationTester:
    def analyze(self, data):
        """Prints the fastest test case"""
        print(f"Automation Tester Analysis - Fastest execution time: {data.min():.2f} seconds")

class PerformanceTester:
    def analyze(self, data):
        """Prints the 95th percentile execution time"""
        percentile_95 = np.percentile(data, 95)
        print(f"Performance Tester Analysis - 95th percentile: {percentile_95:.2f} seconds")

def show_analysis(tester, data):
    """Calls the analyze() method on the given tester object"""
    tester.analyze(data)

def main():
    # Create a NumPy array with at least 12 execution times (in seconds)
    execution_times = np.array([
        2.5, 1.8, 3.2, 4.1, 2.9,  # First 5 tests
        5.6, 2.3, 3.8, 4.5, 1.5,  # Next 5 tests  
        6.2, 3.1                   # Last 2 tests
    ])
    
    print("Test Execution Times Array:", execution_times)
    print("Array Shape:", execution_times.shape)
    print("=" * 50)
    
    # Create objects of all three tester roles
    manual_tester = ManualTester()
    automation_tester = AutomationTester()
    performance_tester = PerformanceTester()
    
    # Call show_analysis() for each tester object (demonstrating polymorphism)
    show_analysis(manual_tester, execution_times)
    show_analysis(automation_tester, execution_times)
    show_analysis(performance_tester, execution_times)

if __name__ == "__main__":
    main()