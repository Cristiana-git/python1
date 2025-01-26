# cuvinte = ["ana", "robert","detine","are","mere","papagali"]
# cuvinte_lungi=[x for x in cuvinte if len(x)>5]
# print(cuvinte_lungi)
# prop=" ".join(cuvinte_lungi)
# print(prop)

# __EXERCIȚIU__ Creează un set care conține doar primele litere ale cuvintelor
# dintr-o propoziție, INDIFERENT DE CAPITALIZARE.

# propozitie = "Putem folosi Python pentru diferinte functionalitati specifice."
# cuvinte=propozitie.split()
# print(cuvinte)
# cuvinte_modificate={cuvant[0].lower() for cuvant in cuvinte}
# print(cuvinte_modificate)

# __EXERCIȚIU__ Definește o FUNCȚIE care să ia ca parametru un șir de caractere
# (def itereaza(cuvant)). Funcția va converti șirul de caractere într-o listă
# și va returna un iterator pentru acea listă. Apelează funcția și stochează
# rezultatul într-o variabilă „iterator". Printează primele trei litere folosind
# funcția next.
# def itereaza(cuvant):
#   lista_cuvant = list(cuvant)
#   iteratoer_lista=iter(lista_cuvant)
#   return iteratoer_lista
#
# exemplu = "caine"
# iterator = itereaza(exemplu)
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# __EXERCIȚIU__	Definește o clasă Caine cu atribute rasa, nume și varsta.
# Creează un obiect al clasei Caine și afișează atributele acestuia.
# class Caine:
#     def __init__(self, rasa,nume,varsta):
#         self.rasa=rasa
#         self.nume=nume
#         self.varsta=varsta
# caine1=Caine("chow-chow","athos",3)
# print(f"rasa:{caine1.rasa}, nume:{caine1.nume}, varsta: {caine1.varsta}")

# __EXERCIȚIU__ Adaugă o metodă descriere în clasa Caine, care returnează o
# descriere completă a câinelui. Testează metoda pe două obiecte diferite ale
# clasei.

# class Caine:
#     def __init__(self, nume, varsta):
#         self.nume = nume
#         self.varsta = varsta
#
#     def descriere1(self):
#         return f"{self.nume} latra si are {self.varsta} ani!"
# caine1 = Caine ("Rex",5)
# caine2 = Caine("Puffy",3)
# print(caine1.descriere1())
# print(caine2.descriere1())

# __EXERCIȚIU__
#	Creează o clasă Student cu următoarele atribute:
#   •	nume
#   •	prenume
#   •	note (o listă de note).
# Adaugă următoarele metode:
#   •	adaugare_nota pentru a adăuga o notă în listă.
#   •	calcul_medie pentru a calcula media notelor.

#	Urmează exemplele următoare pentru a testa clasa creată:
# 1. Adaugă studentul Ana Ionescu cu notele [10, 8].
# 2. Adaugă studentul Marin Iancu cu notele [7, 6, 5].
# 3. Adaugă nota 9 pentru studentul Ana Ionescu.
# 4. Adaugă nota 5 pentru studentul Ana Ionescu.
# 5. Adaugă nota 9 pentru studentul Marin Iancu.
# 6. Calculează și afișează mediile celor doi studenți.

# class Student:
#     def __init__(self, nume,prenume,note):
#         self.nume = nume
#         self.prenume = prenume
#         self.note = note
#     def adaugare_nota(self, *notanoua):
#         for x in notanoua:
#             self.note.append(x)
#         return self.note
#     def calcul_medie(self):
#         return sum(self.note) / len(self.note)
# student1 = Student("Ana", "Ionescu", [10,8])
# student2 = Student("Marin","Iancu", [7,6,5])
# student1.adaugare_nota(9,5)
# student2.adaugare_nota(9)
# print(f"Medie student: {student1.calcul_medie()} ")
# print(f"Medie student: {student2.calcul_medie()} ")

# __EXERCIȚIU__ Creează o clasă Angajat cu atributul specific „numar_ore" și
# atributele următoare:
#   •	nume complet
#   •	salariu
# Adaugă următoarea metodă:
#   •	modifica_numar_ore pentru a modifica numărul de ore de muncă ale unui
# angajat (metodă de clasă)

#	Urmează exemplele următoare pentru a testa clasa creată:
# 1. Adaugă angajatul Sergiu Ionascu cu un salariu de 2500.
# 2. Adaugă angajatul Ioana Cozma cu un salariu de 5300.
# 3. Să se afișeze numărul de ore pentru angajatul Ioana Cozma.
# 4. Să se modifice numărul de ore pentru un angajat în firmă la 30.
# 5. Să se afișeze din nou numărul de ore pentru același angajat.
# 6. Sa se defineasca o metoda care sa returneze salariul / ora.

class Angajat:
  numar_ore = 160

  def __init__(self, nume_complet, salariu_pe_ora):
    self.nume_complet = nume_complet
    self.salariu_pe_ora = salariu_pe_ora

  @classmethod
  def modifica_numar_ore(cls, numar_nou):
    cls.numar_ore = numar_nou

  def descriere(self):
    return f"Numele angajatului: {self.nume_complet} | Salariul pe ora: {self.salariu_pe_ora} | Numarul de ore: {self.numar_ore}"

  def salariu_lunar(self):
    return self.salariu_pe_ora * self.numar_ore

a1 = Angajat("Sergiu Ionascu", 25)
print(a1.descriere())

Angajat.modifica_numar_ore(120)
print(a1.descriere())

print(a1.salariu_lunar())




# __EXERCIȚIU__ Creează o clasă Matematica care include metode statice pentru:
# 	•	Calcularea pătratului unui număr.
# 	•	Verificarea dacă un număr este par.
#	 Testează metodele cu diferite valori.

# class Matematica:
#   @staticmethod
#   def patrat(a):
#     return a ** 2
#
#   @staticmethod
#   def par(a):
#     return a % 2 == 0
#
# print(Matematica.par(15))
# print(Matematica.patrat(5))

# __EXERCIȚIU__ Creează o clasă „Laptop" care să conțină următoarele atribute
# de instanță:
# 1. furnizor
# 2. preț_net
# 3. memorie_ram

# Adaugă două metode:
# 1. calcul_pret_brut -- Calculează și returnează prețul brut prin adăugarea
# unui TVA (19%)
# 2. adaugare_ram -- Primește un parametru și adaugă numărul primit la memoria
# RAM a laptop-ului





