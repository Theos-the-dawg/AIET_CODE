#TASK 1 CREATE A SET AND POPULATE IT FOR LOOP THROGH IT AND AND DISPLAY THE LARGEST VALUE

#TASK 2 CREATE A LIST AND ADD THAT LIST VALUE TO A SET

#TASK 3 CREATE AN ARRAY AND CHECK IF THE ARRAY HAS ANY VALUES IN THE LIST ABOVE

#EXCERCISE 1
# i = 0
# while i is not  10:
#    i+=1
#    print(i) 

#EXCERCISE 2
# my_range = range(-10,0)
# for each in my_range:
#     print(each)
#EXCERCISE 3

# my_range = range(0,5)
# for each in my_range:
#     print(each)
# print("Done")

#EXCERCSIE 4
# values = [10,20,30]
# sum = 0 
# user_input = int(input("Please input a number"))
# values.append(user_input)
# print(values)
# for each in  values:
#     sum+=each
#     print(sum)
#EXCERCISE 5
#  
# user_input  = int(input("Please add the number you want to multiply with "))
# for each in range(0,11):
#     print(each * user_input)

#EXCERCISE 6
# user_input = int(input("Please input the number"))
# for each  in range(0,user_input+1):
#     print(each *each*each)

#EXCERCISE 7
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for each in numbers:
#  if each  % 5:
#     print()#f"{each} The number(s) that are not diviable by 5")
#  else:
#     if each <150 :
#         print(each)
#         continue
#     elif each>=500:
#         break
#         print(f"{each} numbers that are not divisble by 5")
#     else:
#         print(f"{each} number that are diviable by 5")
#         if each >=150:
#             continue
#         else:
#             if each >500:
#                 break
#EXCERCISE 8 
# list1 = [10, 20, 10, 30, 10, 40, 50]
# target = 10
# new_list = []
# for each in list1:
#     if each == target:
#         new_list.append(each)
# print(len(new_list))

#EXCERCISE 9
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for each in range(1,len(my_list),2):
#    print(my_list[each])

#EXCERCISE 10
# list1 = [10, 20, 30, 40, 50]
# list1.reverse()
# print(list1)

#EXCERCISE 11
# string = "Python"
# new_string = " "
# for each in string:
#   reversed_str = each + string
#   print(reversed_str)
#EXCERCISE 12
vowels = ["a","i","e","o","u"]
vowels_count = []
const_count = []
string = "Loops are Fun!"

for each in string.lower():
  if each.isalpha():
    if each in vowels:
        vowels_count.append(each)
        print(f"the total amount of vowels{len(vowels_count)} ")
        print(len(vowels_count))
        print(f"{len(each)} the amount of vowels is  ")

    else:
        const_count.append(each)
      #  print(len(const_count))
        #print(f"the total amount of conts{const_count}")
       # print(f"{len(each)} the amount of consts is ")
print(len(vowels_count))
print(len(const_count))