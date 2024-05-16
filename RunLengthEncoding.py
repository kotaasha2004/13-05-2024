def run_length_encoding(s):
    s2=""
    count=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count=count+1
        else:
            s2=s2+str(count)+s[i-1]
            count=1
    s2=s2+str(count)+s[-1]
    print(s2)
str1=input()
run_length_encoding(str1)
