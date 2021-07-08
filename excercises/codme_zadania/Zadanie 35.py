#AssertionError

# while True:
#     x = int(input("podaj pierwsz aliczbe: "))
#     y = int(input("podaj druga liczbe"))
#     try:
#         assert y!=0
#         print(x/y)
#         break
#     except:
#         print("y nie moze byc 0 ")


#AttributeError

x = 567

try:
    print(x.upper())
except:
