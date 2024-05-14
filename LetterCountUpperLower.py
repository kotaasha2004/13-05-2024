sentence=input()
upper=0
lower=0
for i in sentence:
    if i.isupper():
        upper=upper+1
    elif i.islower():
        lower=lower+1
print(f"Uppercase Letters : {upper}")
print(f"Lowercase Letters : {lower}")
