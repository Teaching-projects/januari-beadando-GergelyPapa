# Visnyei Gergely Téglalap, Kör, Négyzet területének/kerületének a kiszámítására szolgál a program.
lista=[]

#negyzetek kiszamitasa
def negyt():
    szam=int(input("Kérem a négyzet értékeit: "))
    eredmeny=szam*szam
    print(eredmeny)
    lista.append(eredmeny)
def negyk():
    szam=int(input("Kérem a kerületét a négyzetnek: "))
    eredmeny=4*szam
    print(eredmeny)
    lista.append(eredmeny)
#teglalapok kiszamitasa
def tegt():
    szam=int(input("Kérem a téglalap 'A' oldalának értékét: "))
    szam2=int(input("Kérem a téglalap 'B' oldalának értékét: "))
    eredmeny=szam*szam2
    print(eredmeny)
    lista.append(eredmeny)
def tegk():
    szam=int(input("Kérem a téglalap értékeit: "))
    szam2=int(input("Kérem a téglalap értékeit: "))
    eredmeny=2*(szam+szam2)
    print(eredmeny)
    lista.append(eredmeny)
#korok kiszamitasa
def kort():
    szam=int(input("Kérem a Kör sugarát: "))
    eredmeny=(szam*szam)*3.14
    print(eredmeny)
    lista.append(eredmeny)
def kork():
    szam=int(input("Kérem a Kör sugarát: "))
    eredmeny=2*szam*3.14
    print(eredmeny)
    lista.append(eredmeny)
#ki szeretne-e lepni kerdes
def kilep():
    kerdes=input("Ki szeretnél lépni(igen vagy nem?) ")
    if kerdes=="Igen" or kerdes=="igen":
        print("Elozo számok: ",lista)
        quit()
    elif kerdes=="Nem" or kerdes=="nem":
        return(asd())

def terulet():
    teruletkiszam=input("Mit szeretnék kiszámolni?(Négyzet, Téglalap, Kör) ")
    while True:
        if teruletkiszam=="Négyzet" or teruletkiszam=="négyzet":
                negyt()
                kilep()
                
        elif teruletkiszam=="Téglalap" or teruletkiszam=="téglalap":
                tegt()
                kilep()
        elif teruletkiszam== "Kör" or teruletkiszam=="kör":
                kort()
                kilep()
def kerulet():
    keruletkiszam=input("Mit szeretnék kiszámolni?(Négyzet, Téglalap, Kör) ")
    while True:
        if keruletkiszam=="Négyzet" or keruletkiszam=="négyzet":
            negyk()
            kilep()
        elif keruletkiszam=="Téglalap" or keruletkiszam=="téglalap":
            tegk()
            kilep() 
        elif keruletkiszam== "Kör" or keruletkiszam=="kör":
            kork()
            kilep()
def asd():
    print("Elozo szamok: ",lista)
    
    mitszeretne=input("Mit szeretnél kiszámolni?(Terület, Kerület) ")

    if mitszeretne=="Terület" or mitszeretne=="terület":
        terulet()

    if mitszeretne=="Kerület" or mitszeretne=="kerület":
        kerulet()
asd()