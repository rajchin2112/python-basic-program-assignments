# 1.b. simple interest

p = int(input("initIal principle amount: "))
r = float(input("annul interest rate: ")) / 100 
t = float(input("year: "))
a = p * (1+r*t)
print("final amount is",a)

# 1.c. solve quadratic equation

a = int(input('the coef of x2: '))
b = int(input('the coef of x: '))
c = int(input('the constant: '))
x = (-b+(((b**2)-(4*a*c))**.5))/(2*a)
y = (-b-(((b**2)-(4*a*c))**.5))/(2*a)
print(x)
print(y)

# 1.d net salary

BA = int(input("Basic Salary: "))
CA = int(input("Conveyance_Allowance: "))
EPF = int(input("Epf: "))
OVERTIME = int(input("Overtime_Pay: "))
BONUS = int(input("bonus: "))
DA = int(input("Dearness_Allowance: "))
gross_salary = (BA + CA + EPF + OVERTIME + BONUS + DA)
PT = int(input("Professional_Tax: "))
PF = int(input("employee_contribution: ")) 
IT = int(input("Income Tax: "))
deduction = (PT+PF+IT)
net_salary = (gross_salary - deduction)
print("the employee salary is ",net_salary)

def x(values):
    values[0] = 1
v = [2,3,4]
x(v)

def print_sai(text):
    print(text)
    print(text)
    print(text)

print_sai("sai") 

def movie_rating(name,rating):
        if rating < 5 :
            print("the movie name is", name , "and its rating", rating,"and avg movie")
        elif rating == 5 :
            print("the movie name is", name , "and its rating", rating,"and gud movie")
        else :
            print("the movie name is", name , "and its rating", rating,"and too gud movie")


movie_rating("valimai",6)
print("while")

x=0
while (x<5):
    print(x)
#     x=x+1
n = int(input("Enter the value "))

for i in range(1,n+1):
    print(' ' * (n-i) + " *" * i)

def break_fruits():
    fruits = ['apple','orange','lemon']
    x,y,z = fruits
    print(x)
    print(y)
    print(z)
break_fruits()

def z(): 
    x = 10e2
    y = 5e2
    z = x+y
    print(z)
z()

import random 
print(random.randrange(1,5))

for x in "raj":
    print(x)

x = "krishna"
print(x[2])


x = "krishna"
print(len(x))

txt = ("your time is limited")
print('limited' in txt)

txt = ("your time is limited")
if 'limited' in txt : 
    print('yes,'"limited presented in txt")

a = "i am in real world"
print(a[2:5])
print(a[:5])
print(a[-5:-2])
print(a.upper())
print(a.strip())
print(a.replace('r', 'R'))
print(a.split(","))

a = "hello"
b = "raj" 
c = a+b
print(a,"",b)

age = 24 
txt = "my name is Raj, i am {} years old"
print(txt.format(age)) 

import numpy as np

a = float(10e2)
print(a)

num1 = float(input("enter the valie"))
num2 = int(input('enter the val;ue 2 '))
print(num1+num2)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist.insert(1,"orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
    
    
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

