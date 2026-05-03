# #ARITHMETIC OPERATORS
# a=int(input("number1"))
# b=int(input("number2"))
# print("a+b",a+b)
# print("a-b",a-b)
# print("a*b",a*b)
# print("a/b",a/b)
# print("a//b",a//b)
# print("a%b",a%b)
# #RELATIONAL OPERATORS
# print("a==b",a==b,"\na!=b",a!=b,"\na>b",a>b,"\n a<b",a<b,"\na>=b",a>=b,"\na<=b",a<=b)
# #LOGICAL OPERATORS
# print(True and b)
# print(False or a)
# print(not a)
# #BITWISE OPERATORS
# print(6 & 5)
# print(a | b)
# print(1 ^ 2)
# print(a>>2)
# print(b<<2)
# #ASSIGNMENT OPERATORS
# z=2
# print("z",z)
# z+=1
# print("z",z)
# z-+1
# print("z",z)
# z*=2
# print("z",z)
# z/=2
# print("z",z)
# #MEMBERSHIP OPERATORS
# arr=[1,2,3,4,5]
# print("in operator",5 in arr)
# print("not in operator",6 not in arr)
# #INDENTITY OPERATORS
# a=2
# b=3
# print(a is b)
# print(a is not b)


#ELIGIBLE TO VOTE
# def vote(age):
#     if age>=18:
#         print("eligible to vote")
#     else:
#         print("not eligible to vote")
# age=int(input("enter age"))
# vote(age)
# def results(marks):
#     if marks<50:
#         print("fail")
#     elif marks>=50 and marks<69:
#         print("pass")
#     elif marks>=70 and marks<89:
#         print("good")
#     elif marks>=85:
#         print("excellent")
# marks=int(input("enter marks"))
# results(marks)



# def cal(num1,num2,operator):
#     if operator=="+":
#         print(num1+num2)
#     elif operator=="-":
#         print(num1-num2)
#     elif operator=="*":
#         print(num1*num2)
#     elif operator=="/":
#         print(num1/num2)
#     else:
#         print("invalid operator")
# num1=int(input("enter number1"))
# num2=int(input("enter number2"))
# operator=input("enter operator(+,/,*,-)")
# cal(num1,num2,operator)

# def leap_year(year):
#     if year%4==0 and (year%100!=0 or year%400==0):
#         print("leap year")
#     else:
#         print("not a leap year")
# year=int(input("enter year"))
# leap_year(year)

# def evenodd(num):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# num=int(input("enter number"))
# evenodd(num)
for i in range(-1,-101,-1):
    print(i)
for i in range(-100,0,1):
    print(i)

#WHILE LOOP
num=int(input("enter range"))
evensum=0
oddsum=0
while num!=0:
    if num%2==0:
        evensum+=num
    else:
        oddsum+=num
    num-=1
print("sum of even numbers",evensum)
print("sum of odd numbers",oddsum)


n=int(input("enter range"))
evenprod=1
oddprod=1
while n!=0:
    if n%2==0:
        evenprod*=n
    else:
        oddprod*=n
    n-=1
print("product of even numbers",evenprod)
print("product of odd numbers",oddprod)