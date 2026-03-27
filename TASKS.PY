#TASK 1 CREATE A SET AND POPULATE IT FOR LOOP THROGH IT AND AND DISPLAY THE LARGEST VALUE

grades = {20,35,40,50,55,65,75,85,95,100}
for grade in grades :
    print(max(grades))

#TASK 2 CREATE A LIST AND ADD THAT LIST VALUE TO A SET

my_fruits = ['oranges','apples','grapes','bananas','pears']
tropics = set(my_fruits)
print(tropics)

#TASK 3 CREATE AN ARRAY AND CHECK IF THE ARRAY HAS ANY VALUES IN THE LIST ABOVE 
my_fruits2 = ['oranges', 'apples','grapes','guavas','leaches','mangos']
for the_fruits in my_fruits2:
    if the_fruits in my_fruits:
        print(f"Matching fruit found:{my_fruits2}")
    

