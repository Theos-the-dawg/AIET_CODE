



# a =10
# b=20
# c =10
# if a==10 or c==11:
#     print(True)
# else:
#     print(False)
# elements = ["motheo","Gerald","Master"]
# #elements
# user_input = input("Insert name you are looking for ")

# for each in elements:
#     if each.lower() == user_input:
#      print(f"The name {user_input} is found")
#     else:
#        print(f"{user_input} not found")

#count based loop
# ranges = range(0,9)
# for i in ranges:
#     print("Hello World")

#condition based loop
user_input = input("please input a number ")
tester = True
while tester:
 try:
    user_input = input("Please insert a number that is not 0")
    converted_user_inpiut=int(user_input)
    if converted_user_inpiut == 0:
        print(f'exit  input:{user_input}')
        tester = False
        print(f"The value you have inputted are {converted_user_inpiut}")

 except:
    ValueError("")
       

    


