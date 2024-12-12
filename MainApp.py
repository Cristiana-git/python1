# # # n = int(input("Introdu un numar: "))
# # # if not n > 0:
# # #     print("Numarul trebuie sa fie pozitiv")
# # # else:
# # #     for i in range (n):
# # #         litera = input("Introdu o litera: ")
# # #         if litera == "z":
# # #             litera = "a"
# # #         elif litera == "Z":
# # #             litera = "A"
# # #         else:
# # #             valoare_ascii = ord(litera)
# # #             valoare_ascii += 1
# # #             litera = chr(valoare_ascii)
# # #
# # #         print(f"Litera urmatoare in alfabet este:{litera}")
# # #
# # def factorial(x):
# #     if x<0:
# #         return 0
# #     if x==0:
# #         return 1
# #     else:
# #         fact=1
# #         for i in range (1, x+1):
# #             fact=i*fact
# #         return fact
# # a=int(input("Alege un numar a: "))
# # b=int(input("Alege un numar b: "))
# # print(factorial(a)+ factorial(b))
#
# # Fie trei numere mai mari decât 0: a, b, c. Puteți să le dați
# # ce valori doriți.
# # Să se definească funcția produs_3( ) care ia ca parametri trei
# # numere și returnează produsul lor. Să se apeleze funcția cu parametri
# # a, b și c și să se afișeze rezultatul pe ecran.
#
# # produs_3(a,b,c)
#
#
# def produs_3(a,b,c):
#     if a!=0 and b!=0 and c!=0:
#         return a*b*c
#     else:
#         print("Numerele trebuie sa fie pozitive")
# a = 3
# b = 5
# c = 7
# d=produs_3(a,b,c)
# print(d)

def conversie_kilometraj(producator_masina , kilometri=0):
    if kilometri==0:
        print("Masina este noua")
        return "0"
    mile =kilometri*0.62
    return str(mile)
print("Masina are " + conversie_kilometraj("BMW", 100000) + " mile.")
print("Masina are " + conversie_kilometraj("Mercedes Benz") + " mile.")
