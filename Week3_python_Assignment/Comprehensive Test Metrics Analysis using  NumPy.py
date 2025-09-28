import numpy as np

# ------------------------------
# a) Generate Synthetic Data
# ------------------------------
np.random.seed(50)   # for reproducibility
data = np.random.randint(5, 51, size=(5, 50))   # 5 cycles × 50 tests
print("Dataset (5x50):\n", data)

# ------------------------------
# 1. Statistical Analysis
# ------------------------------
# Average execution time per cycle
avg_per_cycle = np.mean(data, axis=1)
print("\nAverage execution time per cycle:", avg_per_cycle)

# Test case with maximum execution time in entire dataset
max_value = np.max(data)
max_position = np.unravel_index(np.argmax(data), data.shape)
print("Maximum execution time:", max_value, "at (cycle, test):", max_position)

# Standard deviation of execution times for each cycle
std_per_cycle = np.std(data, axis=1)
print("Standard deviation per cycle:", std_per_cycle)

# ------------------------------
# 2. Slicing Operations
# ------------------------------
cycle1_first10 = data[0, :10]
cycle5_last5 = data[4, -5:]
cycle3_alternate = data[2, ::2]

print("\nCycle 1 - first 10 tests:", cycle1_first10)
print("Cycle 5 - last 5 tests:", cycle5_last5)
print("Cycle 3 - alternate tests:", cycle3_alternate)

# ------------------------------
# 3. Arithmetic Operations
# ------------------------------
addition = data[0] + data[1]
subtraction = data[0] - data[1]
multiplication = data[3] * data[4]
division = data[3] / data[4]

print("\nElement-wise addition (Cycle1+Cycle2):", addition[:10], "...")
print("Element-wise subtraction (Cycle1-Cycle2):", subtraction[:10], "...")
print("Element-wise multiplication (Cycle4*Cycle5):", multiplication[:10], "...")
print("Element-wise division (Cycle4/Cycle5):", division[:10], "...")

# ------------------------------
# 4. Power Functions
# ------------------------------
squared = np.power(data, 2)
cubed = np.power(data, 3)
sqrted = np.sqrt(data)
logged = np.log(data + 1)

print("\nSquared sample:\n", squared[0, :5])
print("Cubed sample:\n", cubed[0, :5])
print("Square root sample:\n", sqrted[0, :5])
print("Log transform sample:\n", logged[0, :5])

# ------------------------------
# 5. Copy Operations
# ------------------------------
# Shallow copy
shallow_copy = data.view()
shallow_copy[0, 0] = 999   # modifying one element
print("\nAfter shallow copy modification, data[0,0]:", data[0, 0])

# Deep copy
deep_copy = data.copy()
deep_copy[0, 1] = 888
print("After deep copy modification, original data[0,1]:", data[0, 1])

# Reset changed value
data[0, 0] = np.random.randint(5, 51)

# ------------------------------
# 6. Filtering with Conditions
# ------------------------------
# Cycle 2 > 30
cycle2_gt30 = data[1, data[1] > 30]
print("\nCycle 2 execution times > 30:", cycle2_gt30)

# Tests consistently > 25 across all cycles
consistently_gt25 = np.all(data > 25, axis=0)
consistent_tests = data[:, consistently_gt25]
print("Tests consistently > 25 across all cycles:\n", consistent_tests)

# Replace all execution times < 10 with 10
thresholded = data.copy()
thresholded[thresholded < 10] = 10
print("Data after minimum thresholding:\n", thresholded)
