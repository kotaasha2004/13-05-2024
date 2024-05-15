input_string=input()
cleaned_chars=[]
for char in input_string:
    if char.isalpha():
        char=char.lower()
    cleaned_chars.append(char)
cleaned_string=''.join(cleaned_chars)
if cleaned_string==cleaned_string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
