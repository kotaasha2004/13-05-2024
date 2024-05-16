str1 = input()
str2 = input()
str1 = str1.replace(" ", "")
str2 = str2.replace(" ", "")
result = []
for char in str1:
    if char in str2 and char not in result:
            result.append(char)
    ans=''.join(result)
if result!=0:
    print(ans)
else:
    print("-1")
