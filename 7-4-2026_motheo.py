# n= 6
# while n>0:
#     print(n, end="," if n>1 else "")
#     if n ==1 :
#         break
#     n = n //2 if n % 2 == 0 else 3*n+1


# for i in range(1,6):
#     print(str(i) * i )


def excercise_19():
    income  = int(input("Please input your salary"))
    payable_tax = 0 
    if income >10000:
        print(payable_tax)
    elif income >= 20000:
        payable_tax = (income - 10000) *10 /100
    if income >=20000:
        payable_tax = (income - 20000) * 20 /100 + 10000 * 10 /100
    print(int(payable_tax))
excercise_19()   


# First $10,000: 0% tax
# Next $10,000: 10% tax
# Remaining income: 20% 