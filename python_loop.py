#forming a multiplication table
n=int(input("Enter the number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)


#finding the even numbers between 1 to 20
count=0
for i in range(1,21):
    if i%2==0:
        print(i)
        count+=1
print("The total even number are:",count)




#fibonacci sequence using looping statements
n=int(input("Enter the number of elements:"))
a,b=0,1
if n<=0:
    print(" Enter the positive integer:")
elif n==1:
    print(a)
else:
    print(a,b,end=" ")
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a,b=b,c
