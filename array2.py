#1.1Create an array and append 3 values to it

#1.2Sort that array in ascending order, afterwards find the largest element in the array
#1.3then find the smallest element in the array and minus the highest value with the smallest value in the array
#1.4Average of array 

#1.1 
array= [10,20,30,40,50,60,70,80,90,100]
print(array)
array.append(60)
array.append(50)
array.append(30)
print(array)

#1.2
array.sort()
print(array)

#1.3
smallest = min(array)
smallest_num = int(smallest)
largest = max(array)

largest_num = int(largest)
print(f"the largest value is :{largest_num} and the smallest {smallest_num}")
print(largest - smallest)

#1.4
value =0
for number in array:
    value+=number

print(value)
print(f"The avg is :{value / len(array)}")