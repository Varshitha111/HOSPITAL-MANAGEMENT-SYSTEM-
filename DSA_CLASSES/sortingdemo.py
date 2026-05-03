# # l=list(map(int,input("enter").split()))
# # s=""
# # for i in l:
# #     s+=str(i)
# # s=str(int(s)+1)
# # res=[]
# # for i in s:
# #     res.append(int(i))
# # print(res)
# # l=[1,2,3]
# # s=0
# # for i in l:
# #     s=s*10+i
# # s+=1
# # res=[]
# # while s>0:
# #     r=s%10
# #     res.append(r)
# #     s//=10
# # print(res[::-1])
    
# # n=100
# # choc=n
# # wrap=n
# # while wrap>=3:
# #     wrap1=wrap//3
# #     choc+=wrap1
# #     wrap=wrap1+wrap%3
# # print(choc)

# # st="aabbaaccaa"
# # count={}
# # for ch in st:
# #     if ch in count:
# #         count[ch]+=1
# #     else:
# #         count[ch]=1

# # print(count)



# s="aabbaaccaabb"
# res=""
# for i in s:
#     if i not in res:
#         res+=i+str(s.count(i))
# print(res)


# a="aaabbaaccdd"
# res=""
# for i in a:
#     if i not in res:
#         res+=i+str(a.count(i))
# print(res)
#addition of 2 numbers
# Write a program to print the sum of the digits in the number.
# num=int(input())
# sum=0
# while num!=0:
#     temp=num%10
#     num//=10
#     sum+=temp
# print(sum)
# #  Write a program to print reverse of the given number.  
# num=int(input())
# rev=0
# while num!=0:
#     temp=num%10
#     rev=rev*10+temp
#     num//=10
# print(rev)

# Write a program that takes a string, string should be of even length. Divide the string into two equals parts, check the number of vowels in both the parts of the string. If both parts of string have same number of vowels then return true otherwise return false.

# Testcase1	:  rebels
# Output     	:  true
# stri=input()
# if len(stri)%2==0:
#     str1=stri(0,len(stri)/2)
#     str
def nearestprime(n):
    backc=n-1
    frontc=n+1
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
print(nearestprime(5))