# -----------------------------------------------
# Assignment: List Slicing and Indexing Operations
# -----------------------------------------------

#Part	Meaning	Default Value

#start	Index where the slice begins (inclusive)	0
#end	Index where the slice stops (exclusive)	len(list)
#step	Interval between elements (can be negative)	1

# Given list of first ten prime numbers
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# (a) Extract the middle five primes (indexes 2 to 6)
middle_five = prime_numbers[2:7]

# (b) Get every second prime (step = 2)
every_second = prime_numbers[::2]

# (c) Use negative indexing to get the last three primes
last_three = prime_numbers[-3:]

# (d) Reverse the list using slicing
reversed_list = prime_numbers[::-1]

# (e) Sort the list in descending order
descending_order = sorted(prime_numbers, reverse=True)

# Display the results
print("Original List:      ", prime_numbers)
print("a) Middle Five:     ", middle_five)
print("b) Every Second:    ", every_second)
print("c) Last Three:      ", last_three)
print("d) Reversed List:   ", reversed_list)
print("e) Descending Order:", descending_order)
