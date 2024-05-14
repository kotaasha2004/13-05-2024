def checkLucky(a):
    sum=0
    for i in a:
        sum=sum+ord(i)
    if sum%2==0:
        return 1
    else:
        return 0
s=input()
if checkLucky(s):
    print(f"lucky")
else:
    print(f"not lucky")
    
