# m=[[1,2,3],[4,5,6],[7,8,9],[4,2,7]]
# add=0
# row=len(m)
# col=len(m[0])
# for i in range(row):
#     for j in range(col):
#         if i==0 or  j==0 or i==row-1 or j==col-1:
#             add+=m[i][j]
# print(add)
# count=0
# while True:
#     count+=0
# print(count)
n=5
#pyramid
# for i in range(1,n+1):
#     for j in range(n-i): print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print()


#diamond
for i in range(1,n+1):
    for j in range(n-i): print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i): print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end="")
    print()