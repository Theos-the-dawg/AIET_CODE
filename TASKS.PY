#TASK 1 CREATE A SET AND POPULATE IT FOR LOOP THROGH IT AND AND DISPLAY THE LARGEST VALUE

#grades = {20,35,40,50,55,65,75,85,95,100}
#for grade in grades :
#    print(max(grades))

#TASK 2 CREATE A LIST AND ADD THAT LIST VALUE TO A SET

#my_fruits = ['oranges','apples','grapes','bananas','pears']
#tropics = set(my_fruits)
#print(tropics)

#TASK 3 CREATE AN ARRAY AND CHECK IF THE ARRAY HAS ANY VALUES IN THE LIST ABOVE 
#my_fruits2 = ['oranges', 'apples','grapes','guavas','leaches','mangos']
#for the_fruits in my_fruits2:
 #   if the_fruits in my_fruits:
  #      print(f"Matching fruit found:{my_fruits2}")
    

#TASK 4 CREATE A WHILE LOOP THAT RUNS UNTIL TEN IS THE DESIRED OUTPUT

#i = 0
#while i < 10:
 #i += 1
 #print(i)

 #TASK 5 DISPLAY A MESSAGE 'DONE' AFTER SUCCESSFUL EXECUTION OF FOR LOOP

 #for x in range(0,5):
   
  # print(x)
 #else:
  # print("DONE!")
   
#TASK 6 CALCULATE THE SUM OF ALL NUMBERS FROM 1 TO N

#sum = 0
#input("ENTER THE NUMBER:")
#for i in range(0,11):
#   sum = sum + i
#   print(sum)
  

#Practice Problem: Given a list of numbers, use a loop to count how many times a specific number (e.g., 10) appears.

# my_list = [5, 10, 15, 20, 25, 15, 22, 25, 30, 15,5]
# target = int(input("please input the number you ar elooking for "))
# count = 0
# #value_counter = []

# for each in my_list:
#    if each == target:
#      count+=1
# #     value_counter.append(each)
    
#      print(count)
     #print(f"{len(value_counter)} appears in the list.")

#Practice Problem: Given a Python list, use a loop to print only the elements that are located at odd index positions (index 1, 3, 5, etc.).

#Exercise Purpose: This exercise teaches Index-Based Iteration. It helps you distinguish between an item’s value in a list and its position (index), which is fundamental for data filtering.

the_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for item in range(1,len(the_list),2):
 print(item)
 print(the_list[item])
#print(len(the_list))

g_list = [10,20,30,40,50]
g_list.reverse()
print(g_list)

#Practice Problem: Write a program that counts the total number of vowels and consonants in a given sentence, ignoring spaces and special characters.

# Exercise Purpose: In this exercise, you will practice membership testing and data filtering. You will use the in operator to check if a value is in a collection, and try string methods like .isalpha() to quickly clean your data.
