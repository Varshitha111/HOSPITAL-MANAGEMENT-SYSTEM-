# #pattern printing
# #square pattern
# #outer loop row inner looop column
# n=int(input("enter num of rows and coulmns"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*", end=" ")
#     # print()


def rightangletrianglepattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*", end=" ")
        print()
n=int(input("enter num of rows"))
rightangletrianglepattern(n)