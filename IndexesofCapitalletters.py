def cap(s):
    index_list=[]
    for char in s:
        if char.isupper():
            index_list.append(s.index(char))
    x=str(index_list)[1:-1]
    x=x.replace(",","")
    print(x)
input_String=input()
cap(input_String)
        
