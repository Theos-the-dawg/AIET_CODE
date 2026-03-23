#1.1Create an array and append three values to it.

my_array = [12,17,15,34,55,2,81,9,18,24]
my_array.append(70)
my_array.append(71)
my_array.append(72)
print(my_array)


#1.2Sort that array in ascending order.

my_array.sort()
print(my_array)

#1.3
smallest = min(my_array)
highest = max(my_array)

print(highest - smallest)




#1.3Find the largest element in the array then find the smallest array.
value = 0
for  number in my_array:
    value += number

print(value/ len(my_array))
#1.4Minus the highest value with the smallest value
#1.5Write down average of the array.
#(sum of values of the array/divided by how many elements are in the array) 