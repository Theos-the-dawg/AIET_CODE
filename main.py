#1.1 CREATE AN ARRAY AND APPEND 3 VALUES

array = [2,3,5,7,1,2,9,0,214,10,23]

array.append(50)
array.append(20)
array.append(10)

print(array)
array.sort()
print(array)
#1.2 FIND THE LARGEST ELEMENT IN THE ARRAY
maximum=max(array)
print(maximum)
#1.3 FIND THE SMALLEST ELEMENT IN THE ARRAY 
minimum = min(array)
print(minimum)


#1.4 FIND MINUS THE MAX - MIN OF THE ARRAY
print(maximum-minimum)
value = 0 
for number in array:
   value+=number
   print(value)

print(f"the avg is : {value/len(array)}") 