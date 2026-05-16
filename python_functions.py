#fibonacci series concept
def fibonacci_series(n):
    a, b = 0, 1   
    series = []  
    for i in range(n):   
        series.append(a)   
        a, b = b, a + b   
    return series
print("Fibonacci series (7 terms):", fibonacci_series(7))




#sum of the digits
def sum_of_digits(n):
    total = 0
    while n > 0:          
        total += n % 10   
        n //= 10          
    return total          
print("Sum of digits of 234:", sum_of_digits(234))



#to check whether the given number is armstrong number

def is_armstrong(n):
    num_digits = len(str(n))
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10
    return total == n
print("Is 153 Armstrong?", is_armstrong(153))   
print("Is 9474 Armstrong?", is_armstrong(9474)) 
print("Is 123 Armstrong?", is_armstrong(123))   


#hackerrank problem based on functions
if __name__ == '__main__':
    n = int(input("Enter the n value:"))
    
for i in range(1,n+1):
   print(i,end="")
   

