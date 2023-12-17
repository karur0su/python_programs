def find_n_largest_elements(lst, n):
	# sort the list in descending order
	sorted_lst = sorted(lst, reverse=True)

	# Get the first n elements
	largest_elements = sorted_lst[:n]

	return largest_elements

# sample list of numbers
numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34,]

# number of largest elemenents to find
N = int(input("N = "))

# find the N largest elements to find
result = find_n_largest_elements(numbers, N)

# print the n largest elements
print(f"the {N} largest elements in the list are:", result) 


