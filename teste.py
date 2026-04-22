def escolha (a):
    if a == 0:
        s= "Sou 0"
    elif a == 1:
        s= "Sou 1"
    elif a == 2:
        s= "Sou 2"
    else :
        s="Nao sou nem 0 nem 1 nem 2"
    return (s)
a=int(input("Digite um numero :"))
print(escolha(a))

isinstance(2,type(escolha))
type
