Practise No 3.1
a)
age = eval(input('Enter your age:'))
if age > 62:
    print('You can get your pension benefits')
b)
name = (input('Enter the name of any baseball player name:'))
list= ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
if name in list:
    print('One of the top 5 baseball players,ever!')
print('Thank You...')
c)
hit = eval(input('Enter the number of hits:'))
shield = eval(input('Enter the number of shields:'))
if hit > 10 and shield == 0:
    print('You are dead...')
d)
north = input("Can you see a way through north..?:")
south = input("Can you see a way through south..?:")
east = input("Can you see a way through east..?:")
west = input("Can you see a way through west..?:")
if north == 'Yes':
    print ('I can escape north....')
else:
    print ('I cannot escape north....')
if south == 'Yes':
    print ('I can escape south.....')
else:
    print('I cannot escape south....')
if east == 'Yes':
    print ('I can escape east....')
else:
    print ('I cannot escape east....')
if west == 'Yes':
    print ('I can escape west....')
else:
    print ('I cannot escape west....')
    
Practise No 3.3
a)
>>>year = eval(input('Enter the year:'))
#Finding Leap year
if year%4==0:
    print('Could be a leap year')
else:
    print('Definitely not a leap year')
b)
>>>List_Ticket = eval(input('Enter the ticket number:'))
List_Lottery = eval(input('Enter the lottery number:'))
if List_Ticket == List_Lottery:
    print('You won!')
else:
    print('Better luck next time...')

Practise NO 3.4
a)
>>>User = input('Enter your login ID:')
list = ['Joe', 'Sue', 'Hani', 'Sophie']
if User in list:
    print('You are welcome!')
else:
    print('Unknown user')
print('Done.') 

Practise No 3.5
a)
word =  ['stop', 'desktop', 'top', 'post']
for words in word:
    if len(words) == 4:
        print(words)

Practise No 3.6
a)
for number in range(10):
    print(number)
b)
for number in range(2):
    print(number)

Practise No 3.7
a)
for number in range(3,13):
    print(number)
b)
for number in range(0,9,2):
    print(number)
c)
for number in range(0,24,3):
    print(number)
d)
for number in range(3,12,5):
    print(number)

PRACTICE PROBLEM 3.8
def perimeter(r):
    n = 2*3.142*r
    return(n)
b = perimeter(1)
b2 = perimeter(2)
print(b)
print(b2)

PRACTICE PROBLEM 3.9
def average(x, y):
    return(x+y)/2
A = average(1,3)
print(A)
B = average(2,3.5)
print(B)

PRACTICE PROBLEM 3.10
def novowel(x):
    for i in x:
        if i in "aeiouAEIOU":
            return False
    return True
v = noVowel('python')
print(v)

PRACTICE PROBLEM 3.11
def allEven(x):
    for num in x:
        if num % 2 != 0:
            return False
    return True
numbers = allEven([3,2,-8,-7,10])
print(numbers)

PRACTICE PROBLEM 3.12
def negatives(number):
    neg_num = []
    for i in number:
        if i < 0:
            neg_num.append(i)
    return neg_num

x = negatives([1,3,-9,-10,-6,-8])
print(*x, sep ="\n")

PRACTICE PROBLEM 3.13
def average(x, y):
    return(x+y)/2
    
help(average)


def negatives(number):
    neg_num = []
    for i in number:
        if i < 0:
            neg_num.append(i)
    return neg_num

help(negatives)

PRACTICE PROBLEM 3.17
a = eval('2*3+1')
print(a)

b = eval('hello')
print(b)
#it will give error because hello in not defined
"""Traceback (most recent call last):
  File "C:/Users/hp/Desktop/3.17.py", line 4, in <module>
    b = eval('hello')
  File "<string>", line 1, in <module>
NameError: name 'hello' is not defined"""
c = eval("'hello' + ' ' + 'world!'")
print(c)

d = eval("'ASCII'.count('I')")
print(d)

e = eval('x = 5')
print(e)
#it will give error due to syntax error
"""Traceback (most recent call last):
  File "C:/Users/hp/Desktop/3.17d).py", line 1, in <module>
    e = eval('x = 5')
  File "<string>", line 1
    x = 5
      ^
SyntaxError: invalid syntax"""

PRACTICE PROBLEM 3.18
a = 3
b = 4
c = 5

print('(a)')
if a < b:
    print('OK')

print('(b)')
if c < b:
    print('OK')

print('(c)')
if a + b == c:
    print('OK')

print('(d)')
if a**2 + b**2 == c**2:
    print('OK')

PRACTICE PROBLEM 3.19
a = 3
b = 4
c = 5

print('(a)')
if a < b:
    print('OK')
else:
    print('NOT OK')

print('(b)')
if c < b:
    print('OK')
else:
    print('NOT OK')
          
print('(c)')
if a + b == c:
    print('OK')
else:
    print('NOT OK')
          
print('(d)')
if a**2 + b**2 == c**2:
    print('OK')
else:
    print('NOT OK')
          
PRACTICE PROBLEM 3.20
list = ['January','February','March']
for a in list:
    print(a[0:3])

PRACTICE PROBLEM 3.21
num = [2,3,8,7,-1,-10,-6]
for i in num:
    if i % 2 == 0:
        print(i)

PRACTICE PROBLEM 3.22
numbers = [2,8,4,5,9,10]
for i in numbers:
    if i**2 % 8 == 0:
        print(i)

PRACTICE PROBLEM 3.23
print('(a)')
for i in range(0,2):
    print(i,end = ' ')

print('(b)')
for i in range(0,1):
    print(i,end = ' ')

print('(c)')
for i in range(3,7):
    print(i,end = ' ')

print('(d)')
for i in range(1,2):
    print(i, end = ' ')

print('(e)')
for i in range(0,4,3):
    print(i, end = ' ')

print ('(f)')
for i in range(5,22,4):
    print(i,end = ' ')

PRACTICE PROBLEM 3.24
x = input('Enter a list:').split()
for i in x:
    if i != 'secret':
        print(i)

PRACTICE PROBLEM 3.25
stu_names = input('Enter the names of students:').split()
stu_names.sort()
print(*stu_names,sep ='\n')

PRACTICE PROBLEM 3.26
L_element= eval(input('Enter a list:'))
print('The first list element is',L_element[0])
print('The last  last element is',L_element[-1])

PRACTICE PROBLEM 3.27
n = eval(input('Enter the postive integer:'))
for i in range(0,n*6,n):
    print(i)

PRACTICE PROBLEM 3.28
n = int(input('Enter number :'))
for i in range(0,n):
    if i != n:
        print(i**2)


PRACTICE PROBLEM 3.29
n = eval(input('Enter the positive integer:'))
for i in range(1,n+1):
    if (n % i == 0):
        print(i)

PRACTICE PROBLEM 3.30
num_1 = eval(input('Enter the first no.:'))
num_2 = eval(input('Enter the second no.:'))
num_3 = eval(input('Enter the third no.:'))
num_4 = eval(input('Enter the fourth no.:'))

avg_num = (num_1 + num_2 + num_3) / 3
if avg_num == num_4:
    print('Equal')
else:
    print('Not Equal')

PRACTICE PROBLEM 3.31
x = eval(input('Enter the X coordinates:'))
y = eval(input('Enter the Y coordinates:'))
r = 8

import math
calculation = math.sqrt(x**2 + y**2)

if calculation <= r:
    print('It is in!')
else:
    print('It is not in')

    
PRACTICE PROBLEM 3.32
num = eval(input('Enter the positive integer'))
a1 =(num%10)
num = num/10
a2 =(int(num%10))
num = num/10
a3 =(int(num%10))
num = num/10
a4 =(int(num%10))

print(a4)
print(a3)
print(a2)
print(a1)


PRACTIC PROBLEM 3.33
def reverse_string(word):
    return word[::-1]
    
i = reverse_string('abc')
print(i)

g = reverse_string('raw')
print(g)

PRACTICE PROBLEM 3.34
def pay(hourly,hours):
    print('hourly wage:',hourly,'hr')
    print('hourly pay:','10$')
    if hours >= 40:
        sal = 40*hourly 
        O_time = sal + hourly *(hours - 40) * 1.5
        return O_time
    else:
        Not_Otime = hours * hourly
        return Not_Otime
        
salary = pay(10,35)
print(salary)

salary2 = pay(10,45)
print(salary2)


PRACTICE PROBLEM 3.35
def prob(n):
    N = 2**-n
    return(N)

toss = prob(1)
print(toss)

toss2 = prob(2)
print(toss2)

PRACTICE PROBLEM 3.36
def reverse_int(integer):
    return integer[::-1]
x = reverse_int('908')
print(x)

PRACTICE PROBLEM 3.37
def points(x1,y1,x2,y2):
    import math
    d = math.sqrt(((x2 - x1)**2) +((y2 - y1)**2))
    if x2 == 0:
        print('The slope is infinity' + ' ' + 'and the distance is',d)
    else:
        s = ((y2 - y1) / (x2- x1))
        print('The slope is',s,'and the distance is',d)
coordinates = points(4,3,0,1)
print(coordinates)

coordinates2 = points(6,7,8,9)
print(coordinates2)

PRACTICE PROBLEM 3.38
def abbreviation(word):
    return word[0:2]

abb = abbreviation('tuesday')
print(abb)

PRACTICE PROBLEM 3.39
def collision(x1,y1,r1,x2,y2,r2):
    import math
    c_dist =((x2 - x1)**2 + (y1 - y2)**2)
    if c_dist <= (r1+r2)**2:
        return True
    else:
        return False
    
x = collision(0,0,1.4,2,2,1.4)
print(x)

x2 = collision(0,0,3,0,5,3)
print(x2)

PRACTICE PROBLEM 3.40
def partition(names):
    return[firstname for firstname in names
           if firstname[0].lower() in 'abcdefghijklm']

x = partition(['Yumna','Amna','Warisha','Yusra','Asma'])
x.sort()
print(*x,sep = '\n')

PRACTICE PROBLEM 3.41
def lastF(F_name,L_name):
    return (L_name,F_name[0])

name = lastF('Niha','Habib')
print(name)

PRACTICE PROBLEM 3.42
def avg(numbers):
    for i in numbers:
        b = [sum(i)/(len(i))]
        print(*b)
    
x = avg([[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]])
print(x)


PRACTICE PROBLEM 3.43
def hit(x1,y1,r1,x2,y2):
    import math
    dist = ((x2 - x1)**2 + (y1 - y2)**2)
    if dist <= (r1**2):
        return True
    else:
        return False
x = hit(0,0,3,0,0)
print(x)

x2 = hit(0,0,3,4,0)
print(x2)

PRACTICE PROBLEM 3.44
def distance(time):
    sound = 340.29*time
    ans = sound/1000
    return ans    
x = distance(3)
print('the distance to lightning strike is',x)


