# list_basics.py

#  Creating a list
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

#  Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

#  Adding elements
numbers.append(6)
print("After append:", numbers)

#  Removing elements
numbers.remove(3)
print("After remove:", numbers)

#  Iterating through a list
for num in numbers:
    print("Element:", num)

#  Slicing
print("Slice [1:3]:", numbers[1:3])

#  Built-in functions
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))

#  Sorting
numbers.sort()
print("Sorted list:", numbers)

#hackerrank problem 
if __name__ == '__main__':
    x = int(input("Enter the number:"))
    y = int(input("Enter the number:"))
    z = int(input("Enter the number:"))
    n = int(input("Enter the number:"))
    myList = [[i, j, k] 
              for i in range(x + 1) 
              for j in range(y + 1) 
              for k in range(z + 1) 
              if (i + j + k) != n]
    print(myList)
