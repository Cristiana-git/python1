#__PROIECT__ Creează o clasă numită „CutieDeDate" care va fi responsabilă cu
# colectarea datelor și realizarea unor calcule statistice, cum ar fi media
# aritmetică, media geometrică și modul (valoarea cea mai frecventă).

# Clasa va avea următorul atribut:
# 1. date -- O listă care poate conține atât numere întregi cât și float-uri

# Clasa va avea următoarea variabilă de clasă:
# 2. cantitate_date -- Un număr care indică câte obiecte au fost creeate până
# în prezent

# Să se creeze următoarele metode:
# 1.	calculeaza_media_aritmetica(): o metodă care calculează media aritmetică
# a listei de date și o returnează
# 2.  calculeaza_media_geometrica(): o metodă care calculează media geometrică
# a datelor și o returnează
# 3.	get_numar_date(): o metodă care returnează numărul de date stocate în
# prezent în listă
# 4.  calculeaza_modul(): o metodă care calculează modul, adică valoarea care
# apare cel mai frecvent în lista de date
# 5.  calculeaza_mediana(): o metodă care calculează mediana datelor, adică
# valoarea care se află la poziția de mijloc dacă lista este ordonată crescător
# 6.	adauga_date(): o metodă care adaugă date obiectului. Argumentul său poate
# fi un număr sau o listă de numere. În primul caz, un număr va fi adăugat
# atributului self.date, iar în al doilea - toate numerele din lista dată vor
# fi adăugate în self.date
# 7.	sterge_date(): o metodă care elimină TOATE datele din listă.
# 8.	get_date(): o metodă care returnează lista de date pe care le stochează
# obiectul.
class CutieDeDate:
    cantitate_date= 0
    def __init__(self, date):
        self.date = date
        CutieDeDate.cantitate_date = CutieDeDate.cantitate_date + 1
    def media_aritmetica(self):
        media= sum(self.date) / len(self.date)
        return media
    def media_geometrica(self):
        if len(self.date)==0:
            return 0
        obiect =1
        for i in self.date:
            obiect = obiect * i
        return obiect**(1/ len(self.date))
    def get_numar_date(self):
        return len(self.date)
    def calculeaza_modul(self):
        frecventa = {}
        for numar in self.date:
            if numar in frecventa:
                frecventa[numar] = frecventa[numar] + 1
            else:
                frecventa[numar] = 1
        modul = None
        frecventa_maxima = 0
        for valoare, frecventa in frecventa.items():
            if frecventa > frecventa_maxima:
                frecventa_maxima = frecventa
                modul = valoare
        return modul
    def calculleaza_mediana(self):
        lista_sortata = sorted(self.date)
        n = len (self.date)
        if n % 2 !=0:
            return lista_sortata[n // 2]
        else:
            mij1 = lista_sortata[n // 2 -1]
            mij2 = lista_sortata[n //2]
            return (mij1 + mij2) /2
    def adauga_date(self,date):
        if isinstance(date, list):
            self.date.extend(date)
            return self.date
        else:
            self.date.append(date)
            return self.date
    def sterge_date(self):
        self.date.clear()
        return self.date
    def get_date(self):
        return self.date


cutie1 = CutieDeDate([1,2,2,3,2])
print (cutie1.media_aritmetica())
print (cutie1.media_geometrica())
print (cutie1.get_numar_date())
print (cutie1.calculeaza_modul())
print (cutie1.adauga_date([7,8,9]))
print (cutie1.sterge_date())
print (cutie1.get_date())