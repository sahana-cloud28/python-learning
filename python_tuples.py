#stydents marks tracker
students_marks = (85, 90, 78, 92, 88)

print("Highest mark:", max(students_marks))   # 92
print("Lowest mark:", min(students_marks))    # 78

average = sum(students_marks) / len(students_marks)
print("Average marks:", average)              # 86.6

#coordinates system
import math
points = ((2, 3), (4, 5), (6, 7))
print("Points:")
for p in points:
    print(p)
x1, y1 = points[0]
x2, y2 = points[1]
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance between {points[0]} and {points[1]} is {distance:.2f}")



#tuple frequency counter

numbers = (1, 2, 2, 3, 4, 2, 5)
for num in set(numbers):   # set() removes duplicates
    count = numbers.count(num)
    print(f"{num} → {count} time(s)")


#hackerrank problem
if __name__ == '__main__':
    n = int(input("Enter:"))
    integer_list =tuple(map(int, input().split()))
    print(hash(integer_list))



