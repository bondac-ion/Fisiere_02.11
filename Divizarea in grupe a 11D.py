with open('C:/Users/User/Desktop/Lista Clasei 11D.txt','rt',encoding='utf-8') as f:
    y=list(f)
    f.close()
print("    Nume        Prenume         Nota    Grupa","\n")
for i,linie in enumerate(y):
    print(i+1,".",linie,sep=" ")
n=suma=0
for linie in y:
    campuri=linie.split()
    nota=int(campuri[2])
    n+=1
    suma+=nota
suma1=suma2=0
print("Media celor",n,"studenti este",round(suma/n,2))
n1=n2=0
grupa1=[]
grupa2=[]
for linie in y:
    campuri=linie.split()
    if campuri[3]=="engl1":
        suma1+=int(campuri[2])
        n1+=1
        grupa1.extend([linie])
    if campuri[3]=="engl2":
        n2+=1
        suma2+=int(campuri[2])
        grupa2.extend([linie])
print("Media studentilor din grupa 1 este",round(suma1/n1,2))
print("Media studentilor din grupa 2 este",round(suma2/n2,2))
with open("c:/Users/User/Desktop/Grupa1.txt","w",encoding='utf-8') as f:
    for i in grupa1:    
        f.write(i)
        f.write("\n")
with open("c:/Users/User/Desktop/Grupa2.txt","w",encoding='utf-8') as f:
    for i in grupa2:    
        f.write(i)
        f.write("\n")