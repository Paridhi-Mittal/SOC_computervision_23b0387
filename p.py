n = (input("enter a number"))
num = False
i=0
j=0
while i<=len(n) and j<=len(n):
    if i==j:
        j=j+1
if n[i]==n[j]:
     num = True
else:
    i=i+1
    j=j+1


m=0

if num==True or len(n)<3 or len(n)>5:
    print(0)
else:
     perms = permutations(n)
     for perm in perms:
        perm_num = "".join(perm)
        if len(perm_num) == len(n):
            print(perm_num)
    