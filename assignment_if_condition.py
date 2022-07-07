# 2.A leap year

print('\n*** leap year ***\n')


year = int(input("enter a year: "))
if (year % 400) == 0 and (year % 100) == 0 :
 print(year ,"is leap year ")
elif ( year % 4 == 0) and (year % 100 != 0) :
 print(year ,"is leap year")
else :
    print(year ,"is not leap year")

# 2.B maximum of 2 numbers

print('\n*** maximum of 2 numbers ***\n')


num1 = int(input("enter the first number " ))
num2 = int(input("enter the second number " ))
a = num1
b = num2
if a>b :
    print("A is greater") 
elif a<b : 
    print("B is greater")
else :
    print("both are equal") 



# 2.C maximum of 3 numbers


print('\n*** maximum of 3 numbers ***\n')


num1 = int(input("enter the first number " ))
num2 = int(input("enter the second number " ))
num3 = int(input("enter the third number " ))
a = num1
b = num2
c = num3
if a>b and a>c:
    print("A is greater") 
elif b>a and b>c : 
    print("B is greater")
elif c>a and c>b :
    print("C is greater")
else :
    print("two or three values are equal") 


# 2.D simple calculator 


print('\n*** simple calculator ***\n')


num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
select = (input("choice anyone +, -, *, / : "))
if select == "+":
    print(num1+num2)
elif select == "-":
    print(num1-num2)
elif select == "*":
    print(num1*num2)
elif select == "/":
    print(num1/num2)
else:
    print("invalid")



# 2.E grade of the total mark



print('\n*** grade of the total mark ***\n')


print("enter the marks obtained in 6 subjects ")
SUBJECT_1  = float(input("SUBJECT_1: "))
SUBJECT_2  = float(input("SUBJECT_2: "))
SUBJECT_3  = float(input("SUBJECT_3: "))
SUBJECT_4  = float(input("SUBJECT_4: "))
SUBJECT_5  = float(input("SUBJECT_5: "))
sum = (SUBJECT_1 + SUBJECT_2 + SUBJECT_3 + SUBJECT_4 + SUBJECT_5)
avg = (sum / 5) 
if avg >= 91 and avg <= 100 :
    print("student grade is 'S' ") 
elif  avg >= 81 and avg <= 90 :
    print("student grade is 'A' ") 
elif  avg >= 71 and avg <= 80 :
    print("student grade is 'B' ") 
elif  avg >= 61 and avg <= 70 :
    print("student grade is 'C' ") 
elif  avg >= 51 and avg <= 60 :
    print("student grade is 'D' ") 
elif  avg >= 41 and avg <= 50 :
    print("student grade is 'E' ") 
elif  avg >= 31 and avg <= 40 :
    print("student grade is 'U1' ") 
elif  avg >= 21 and avg <= 30 :
    print("student grade is 'U2' ") 
elif  avg >= 11 and avg <= 20 :
    print("student grade is 'U3' ") 
elif  avg >= 0 and avg <= 10 :
    print("student grade is 'U4' ") 
else :
    print("invalid")

