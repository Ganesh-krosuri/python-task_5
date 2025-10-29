def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements using tuple unpacking
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def find_sequence(arr):
    bubble_sort(arr)  # Ensure the array is sorted
    smallest = arr[0]
    largest = arr[-1]
    print("Sequence of integers:", smallest, "to", largest)
    # If you want to print all numbers in the sequence:
    print("Complete sequence:", list(range(smallest, largest + 1)))

# Get input from the user
n = int(input("Enter the number of integers: "))
integers = []

print("Enter the integers:")
for _ in range(n):  # Fixed from "for_in range(n)" to "for _ in range(n):"
    integers.append(int(input()))

bubble_sort(integers)
print("Sorted integers:", integers)
find_sequence(integers)
