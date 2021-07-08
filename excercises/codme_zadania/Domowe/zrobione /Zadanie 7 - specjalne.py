str = str(input("podaj dowolny tekst: "))
str2 = ()
#print(str)
for x in str:
    if x.isalnum() or x.isspace():
        pass
    else:
       str2 = str.replace(x, "")
print(str2)



