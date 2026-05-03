#AREA OF SQUARE
sides=int(input("enter side in cm"))
print("area id",sides*sides)
#AREA OF RECTANGLE
length=int(input("enter length"))
breadth=int(input("enter breadth"))
print("area of rectangle is ",length*breadth)
#AREA OF TRIANGLE
base,height=int(input("enter base")),int(input("enter height"))
print("area of triangle is ",0.5*base*height)
#PERIMETER OF SQUARE
side=int(input("enter side in cm"))
print("perimeter of square is ",4*side)
#PERIMETER OF RECTANGLE
len1=int(input("enter length"))
bre1=int(input("enter breadth"))
print("perimeter of rectangle is ",2*(len1+bre1))
#PERIMETER OF TRIANGLE
side1=int(input("enter side1"))
side2=int(input("enter side2"))
side3=int(input("enter side3"))
print("perimeter of triangle is ",side1+side2+side3)
#Break Amount into 1000s, 500s, and Remaining Change
amount=int(input("enter amount"))
thousands=amount//1000
amount=amount%1000
print("number of 1000s is ",thousands)
fivehundreds=amount//500
amount=amount%500
print("number of 500s is ",fivehundreds)
print("remaining change is ",amount)
#Convert Seconds into Hours, Minutes, and Seconds
seconds=int(input("enter seconds"))
hours=seconds//3600
seconds=seconds%3600
print("number of hours is ",hours)
minutes=seconds//60
seconds=seconds%60
print("number of minutes is ",minutes)
print("remaining seconds is ",seconds)
#Sum of Marks (Maths, Physics, Chemistry)
maths=int(input("enter marks in Maths"))
physics=int(input("enter marks in Physics"))
chemistry=int(input("enter marks in Chemistry"))
print("total marks is ",sum([maths, physics, chemistry]))
#Average of Marks (Maths, Physics, Chemistry)
print("average marks is ",sum([maths, physics, chemistry])/3)
