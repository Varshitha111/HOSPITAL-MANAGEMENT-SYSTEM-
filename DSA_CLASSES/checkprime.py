# def primecheck(num):
#     if num>1:
#         for j in range(2,num):
#         for i in range(2,num):
#             if num%i==0:
#                 return "False"
#         return "True"
# def primerange(n):
#     for i in range(2,n):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)
def nprimenumbers(n):
    count=0
    num=2
    while count<n:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
            count+=1
        num+=1
n=int(input("number"))
nprimenumbers(n)
