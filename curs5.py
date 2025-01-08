# # # # # clienti=[]
# # # # # n=int(input("Cati clienti are firma dumneavoastra?"))
# # # # # for i in range (1, n+1):
# # # # #     client=input(f"Introduceti cliemtul cu numarul{i}")
# # # # #     clienti.append(client)
# # # # # print(clienti)
# # # # it = ['Rares' , 'Radu' , 'Cristina']
# # # # marketing = ['Victor' , 'Ioana']
# # # # meeting=[]
# # # # meeting.extend(it)
# # # # meeting.extend(marketing)
# # # # meeting.remove('Radu')
# # # # print(meeting)
# # # numere=[9,4,1,12,5,4]
# # # numere.sort()
# # # print(numere)
# # # numere.pop(1)
# # # numere.pop()
# # # print (max(numere))
# # # print(len(numere))
# #
# # # __EXERCIȚIU__ Creează o funcție care ia ca și parametru o listă de numere
# # # și returenază POZIȚIA celui mai MIC număr.
# # # Apelează funcția cu parametrul [12, 64, 21, 7, 323, 125] și printează
# # # rezultatul.
# #
# # # HINT: Putem folosi o funcție asociată listelor pentru a determina cel mai mic
# # # număr.
# # # numere=[12,64,21,7,323,125]
# # # def cel_mai_mic(numere):
# # #     for n in numere:
# # #         print(numere.index(min(numere)))
# # #         break
# # # print(cel_mai_mic(numere))
# # # a= "Pisica e in casa."
# # # b="Cainele e in curte"
# # # c= a+b
# # # print(c)
# # # print(len(c))
# # # print(c[0:6])
# # # print(c[::-1])
# #
# # # __EXERCIȚIU__ Un palindrom este un cuvânt care se scrie la fel și de la cap
# # # la coadă, și de la coadă la cap. Exemplu: apa, rotitor, elevele
# #
# # # Să se definească o funcție care ia ca parametru un șir de caractere și
# # # returnează „True" dacă este palindrom, și „False" dacă nu.
# #
# # # Să se apele funcția pe exemplele următoare:
# # # 1. „elefac cafele"
# # # 2. „elefant"
# # # 3. „potop"
# # # n=input("Sa se intoduca un cuvan: ")
# # # def sir(n):
# # #     if n[::-1] == n:
# # #         return True
# # #     else:
# # #         return False
# # # print(sir(n))
# #
# # # __EXERCIȚIU_ Se dă propoziția „masina mare cara fructe multe"
# #
# # # Să se despartă propoziția în cuvinte.
# # # Să se parcurgă lista de cuvinte. Pentru fiecare cuvânt care începe cu litera
# # # „m", să se transforme toate caracterele sale în majuscule.
# # # Să se formeze la loc propoziția și să se afișeze.
# # # n="Masina mare cara fructe multe"
# # # m=(n.split( ))
# # # for i in range(len(m)):
# # #     if m[i].startswith("m"):
# # #         m[i]=(m[i].upper())
# # # print(" ".join(m))
# # # print(m)
# #
# # # __EXERCIȚIU__ Să se definească o funcție „adauga_x( )" care ia un parametru
# # # și returnează o funcție de tip „closure" care adaugă o valoare dată la
# # # parametrul funcției.
# #
# # # def adauga_x(x):
# # #     def adauga_la_y(y):
# # #         return x+y
# # #     return adauga_la_y
# # # creste_cu_5=adauga_x(5)
# # # print(creste_cu_5(10))
# #
# # # __EXERCIȚIU__ Să se definească o funcție „plural( )" care ia ca parametru
# # # o listă de șiruri de caractere și adaugă litera „e" la finalul fiecărui șir
# # # din listă. În rezolvarea problemei veți folosi o funcție imbricată pentru a
# # # adăuga e la finalul cuvintelor.
# #
# # # __EXERCIȚIU__ Fie dicționarul următor, care stochează dacă un client și-a
# # # făcut cont pe platforma noastră sau nu (True = Da, False = Nu):
# # clienti = {
# #     "Andrei": True,
# #     "Maria": False,
# #     "George": True,
# #     "Andra": False,
# #     "Matei": True
# # }
# #
# # # Să se definească o funcție care ia un număr variabil de perechi cheie valoare
# # # și returnează numărul clienților care au cont pe platforma noastră.
# # # Puteți apela funcția atât prin apel normal, cât și prin adăugarea parametrului
# # # **clienti la apel.
# # def  client(**clienti):
# #     s=0
# #     for i, j in clienti.items():
# #         if j==True:
# #             s=s+1
# #     return (s)
# # print(client(**clienti))
# patrat = lambda x: x**2
# print(patrat(4))
# print(patrat(2))
# #
# nume = lambda nume,prenume: nume+ " "+prenume
# print(nume("Ana","Popescu"))
# print(nume("Gigel","Florea"))
#
# cuvinte = ["albina", "CAInE","Pisica","LuP","CAL"]
# print(list(map(lambda cuvant:cuvant.lower(), cuvinte)))

# cuvinte = ["Mare", "munte", "Plaja","Nisip","copaci"]
# rezultat=list(filter(lambda cuvant:cuvant[0].isupper(), cuvinte))
# print(rezultat)

# studenti = [("Andrei","prezent",9.50),("Ana","absent",7.0),("Rares","prezent",8.5)]
# media_sort = sorted(studenti, key=lambda x:x[2])
# media_cea_mai_mare =list(max(studenti, key=lambda x:x[2]))
# print(f"Studentul cu media cea mai mare este: {media_cea_mai_mare[0]}")

# __EXERCIȚIU__ Se dă lista următoare:

angajati = ["Ana Popescu", "Ana Ionescu", "Albert Ioan", "Bogdan Codrea", "Ana Ursache"]

# Să se filtreze lista de angajați și să se stocheze în variabila rez1 strict
# angajații cu prenumele „Ana".
# Apoi, să se modifice scrierea cuvintelor din rez1 pentru a conține doar
# majuscule.

rez1=list(filter(lambda x: x.startswith("Ana"), angajati))
print(rez1)
majuscule=list(map(lambda x:x.upper(), rez1))
print(majuscule)