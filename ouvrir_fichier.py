from ast import Str


print("Entrez un nombre")
N = int(input())
def syracuse(n):
    syr = [n]                     
    while syr[-1] != 1:           
        if syr[-1] % 2 == 0:      
            syr.append(syr[-1] // 2)  
        else:                    
            syr.append(syr[-1] * 3 + 1)

    return syr
chaine=Str(N)
fichier = open('exemple.txt', "a")
contenu=fichier.write("chaine")
contenu = fichier.read()
print(contenu)
fichier.close()