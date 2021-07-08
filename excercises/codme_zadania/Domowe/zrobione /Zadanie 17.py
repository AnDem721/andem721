
def sal_diff():
    sal_list = []
    sal1 = input("podaj wysokoś pierwszej pensji: ")
    sal_list.append(int(sal1))
    sal2 = input("podaj wysokoś drugiej pensji: ")
    sal_list.append(int(sal2))
    sal3 = input("podaj wysokoś trzeciej pensji: ")
    sal_list.append(int(sal3))
    sal_diff  = max(sal_list) - min(sal_list)
    print(f"różnica między największą a najmniejszą wynosi: {sal_diff}")

sal_diff()

# def sal_diff_mid():    #wersja ze środkową
#     sal_list = []
#     mid_sal = []
#     sal1 = input("podaj wysokoś pierwszej pensji: ")
#     sal_list.append(int(sal1))
#     sal2 = input("podaj wysokoś drugiej pensji: ")
#     sal_list.append(int(sal2))
#     sal3 = input("podaj wysokoś trzeciej pensji: ")
#     sal_list.append(int(sal3))
#     mid_sal = sal_list
#     mid_sal.remove(max(mid_sal))
#     sal_diff_mid  = max(mid_sal) - min(mid_sal)
#     print(f"różnica między największą a najmniejszą wynosi: {sal_diff_mid}")
#
# sal_diff_mid()
