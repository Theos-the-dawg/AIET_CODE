#TASK  1
#CREATE A WHILE LOOP THAT CONTINUES TO RUN UNTI THE UNSER INSERTS THE LETTER 'q' IN THE INPUT
checker = False
while checker ==False:
    user_input = input("please input any text else if you wwant to quit type 'q' ")
    if user_input == 'q':
        checker=True
    else:
        print(user_input)


# TASK 2 
# CREATE A DICTIONARY AND LOOP THROUGH THE KEYS IF A USER GETS A KEY THAT MATCHS A RANGE DISPLAY THE KEY

grade_sys = {"A":range(80,100),"B":range(70,79),"C":range(50,69)}
user_grade = input("Please input a insert mark")

for each in grade_sys:
    print(grade_sys.keys())
    if user_grade == "A":
        grade_sys.get("A")

    elif user_grade == "B":
        grade_sys.get("B")

    elif user_grade=="C":
         grade_sys.get("C")
      

# #TASK 3 
# CREATE A LOOP THROUGH THE ARRAY AND MULTIPY THE NUMBER IN THE ARRAY BY THEMSELVES
num1= '100'
print(int(num1))
num1 = int(num1)
print(type(num1))
print(type(num1))