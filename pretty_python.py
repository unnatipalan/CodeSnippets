#1. Separate large numbers 
ten_billion = 10_000_000_000

print(f'{ten_billion:,}')

#2. Using IF statements for assignment
# general
isHappy = True

if isHappy == True:
    result_string = 'Happy'
else:
    result_string = 'Not Happy'

print(f'General : {result_string}')


# IF statements
isHappy = True

result_string = 'Happy' if isHappy else 'Not Happy'

print(f'With IF statement : {result_string}')

# 3. Swapping values without temp variable
#Temp variable -
low = 10
high = 9

if low > high:
    temp = low
    low = high
    high = temp

print(f'With temp variables: {low, high}')


# Without Temp Variables
low = 10
high = 9

if low > high:
    low, high = high, low

print(f'Without temp variables: {low, high}')

#4. Enumerate
#When we need index value inside of for loop

# Without enumerate
grades = ['A', 'B', 'C', 'D', 'E', 'F']
print('Without Enumerate')

i = 1
for grade in grades:
    print(f'{i} : {grade}')
    i += 1


#with enumerate
grades = ['A', 'B', 'C', 'D', 'E', 'F']
print('With Enumerate')

for i, grade in enumerate(grades, 1):
    print(f'{i} : {grade}')

