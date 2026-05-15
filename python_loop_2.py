#sum of its digits using loops
n=int(input("Enter the positive integer:"))
def digit_sum(n):
    total=0
    while n>0:
        digit = n%10
        total+=digit
        n=n//10
    return total
print("Original digit is:",n)
print("Sum of digit :",digit_sum(n))



#hackerrank problem based on looping statement
if __name__ == '__main__':
    n = int(input("Enter the n numbers:"))
    for i in range(n):
        print(i**2)



#finding the square roots by using looping statement

n=int(input("Enter the n value:"))
for n in range(n):
    square=n*n
    print(f"The square of {n} is {square}")