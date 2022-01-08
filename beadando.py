# Visnyei Gergely Téglalap, Kör, Négyzet területének/kerületének a kiszámítására szolgál a program.
lista=[]

def asd():
    print(lista)
    # Itt a program választás elé állít minket és megkérdezi, hogy mit szeretnénk számolni, Területet vagy Kerületet
    mitszeretne=input("Mit szeretnél kiszámolni?(Terület, Kerület) ")
    # Ha a Terület opciót választottuk ebbe a ciklusba lép be
    if mitszeretne=="Terület" or mitszeretne=="terület":
        teruletkiszam=input("Kérem, hogy milyen alakzatnak szeretnéd kiszámolni a területét(Négyzet, Téglalap, Kör): ")
        while True:
            if teruletkiszam=="Négyzet" or teruletkiszam=="négyzet":
                szam=int(input("Kérem a négyzet értékeit: "))
                eredmeny=szam*szam
                print(eredmeny)
                lista.append(eredmeny)
                kerdestnegyzet=input("Ki szeretnél lépni(igen vagy nem?) ")
                if kerdestnegyzet== "igen":
                    print(lista)
                    
                elif kerdestnegyzet=="nem":
                    asd()    
                break
                
            elif teruletkiszam=="Téglalap" or teruletkiszam=="téglalap":
                szam=int(input("Kérem a téglalap 'A' oldalának értékét: "))
                szam2=int(input("Kérem a téglalap 'B' oldalának értékét: "))
                eredmeny=szam*szam2
                print(eredmeny)
                lista.append(eredmeny)
                kerdestteglalap=input("Ki szeretnél lépni(igen vagy nem?) ")
                if kerdestteglalap== "igen":
                    print(lista)
                    break
                elif kerdestteglalap=="nem":
                    asd()      
                    break
            elif teruletkiszam== "Kör" or teruletkiszam=="kör":
                szam=int(input("Kérem a Kör sugarát: "))
                eredmeny=(szam*szam)*3.14
                print(eredmeny)
                lista.append(eredmeny)
                kerdestkor=input("Ki szeretnél lépni(igen vagy nem?) ")
                if kerdestkor== "igen":
                    print(lista)
                    break
                elif kerdestkor=="nem":
                    asd()      
                break
    # Ha a Kerület opciót választottuk, ebbe a ciklusba lép be
    if mitszeretne=="Kerület" or mitszeretne=="kerület":
        keruletkiszam=input("Kérem hogy milyen alakzatnak szeretnéd kiszámolni a kerületét(Négyzet, Téglalap, Kör): ")
        while True:
            if keruletkiszam=="Négyzet" or keruletkiszam=="négyzet":
                szam=int(input("Kérem a kerületét a négyzetnek: "))
                eredmeny=4*szam
                print(eredmeny)
                lista.append(eredmeny)
    
                kerdesknegyzet=input("Ki szeretnél lépni(igen vagy nem?) ")
             
                if kerdesknegyzet== "igen":
                    print(lista)
                    break
                elif kerdesknegyzet=="nem":
                    asd()      
                break
            elif keruletkiszam=="Téglalap" or keruletkiszam=="téglalap":
                szam=int(input("Kérem a téglalap értékeit: "))
                szam2=int(input("Kérem a téglalap értékeit: "))
                eredmeny=2*(szam+szam2)
                print(eredmeny)
                lista.append(eredmeny) 
                kerdeskteglalap=input("Ki szeretnél lépni(igen vagy nem?) ")
                if kerdeskteglalap== "igen":
                    print(lista)
                    break
                elif kerdeskteglalap=="nem":
                    asd()      
                    break  
            elif keruletkiszam== "Kör" or keruletkiszam=="kör":
                szam=int(input("Kérem a Kör sugarát: "))
                eredmeny=2*szam*3.14
                print(eredmeny)
                lista.append(eredmeny)
                kerdeskkor=input("Ki szeretnél lépni(igen vagy nem?) ") 
                if kerdeskkor== "igen":
                    print(lista)
                    break
                elif kerdeskkor=="nem":
                    asd()      
                break    
asd()