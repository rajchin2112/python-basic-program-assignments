# 1.a area of a geometric shape

print('\n*** Area of a rectangle ***\n')

l = float(input("enter the 1st side value: "))
b = float(input("enter the 2nd side value; "))
area_of_value =  l * b
print("area_of_value rectangle is",area_of_value)

print('\n*** Area of a square ***\n')

l = float(input("enter the side value: "))
area_of_value =  l * l
print("square area is",area_of_value)


# 1.b. simple interest

print('\n*** simple interest ***\n')

p = int(input("initIal principle amount: "))
r = float(input("annul interest rate: ")) / 100 
t = float(input("year: "))
a = p * (1+r*t)
print("final amount is",a)

# 1.c. solve quadratic equation

print('\n*** slove quadratic eqn ***\n')

a = int(input('the coef of x2: '))
b = int(input('the coef of x: '))
c = int(input('the constant: '))
x = (-b+(((b**2)-(4*a*c))**.5))/(2*a)
y = (-b-(((b**2)-(4*a*c))**.5))/(2*a)
print(x)
print(y)

# 1.d net salary

print('\n*** Net salary ***\n')

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