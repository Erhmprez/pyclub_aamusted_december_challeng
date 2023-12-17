#Erhmprez
#Find the largest number in a list

numbers = [5, 2, 10, 4, 20, 6, 3 ,12]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print('The largest element is: ',max)        