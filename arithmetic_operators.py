#Smart shopping bill calculator
print("-----------Smart shopping bill-------------")
price=int(input("Enter the price of the item:"))
quantity=int(input("Enter the quantity of the item:"))
total_amount=price*quantity
discount_applied=25
after_discount=total_amount - discount_applied
final_payable_amount=after_discount
print("Total before discount:",total_amount)
print("Discount applied:",discount_applied)
print("After discount:",after_discount)
print("Final payable amount:",final_payable_amount)
print("---------------------------------------------")




#Theme park ticket calculator
print("----------Theme park ticket bill--------------")
adults=int(input("Enter the the number of adults:" ))
children=int(input("Enter the number of children:"))
adult_ticket=500
child_ticket=300
total_charge=adults*500+children*300
discount_applied=200
after_discount=total_charge-discount_applied
print("Adults:",adults)
print("Children:",children)
print("Total charge:",total_charge)
print("Discount applied:",discount_applied)
print("After discount:",after_discount)
print("Final payable amount:",after_discount)
print("---------------------------------------------")




#Hackerrank arithmetic operation problem solving
if __name__ == '__main__':
    a = int(input("Enter the value: "))
    b = int(input("Enter the value:"))
    print(a+b)
    print(a-b)
    print(a*b)



