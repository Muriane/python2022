from tkinter import N


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
print("Suite de Syracuse pour n =" + str(N) , syracuse(N), sep='\n')


