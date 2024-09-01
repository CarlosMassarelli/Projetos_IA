"""
Fazendo tabuada...
"""
coluna=1
linha=1
while linha<=10:
    while coluna<=10:
        print(linha*coluna, end = "\t")
        coluna += 1
    linha += 1
    print ()
    coluna = 1

#contador dentro
cont=0
fora = 5
while fora > 0:
    dentro = 0  
    while dentro < fora:
        print("oi")
        dentro += 1
        cont +=1
    fora -= 1
print(cont)
