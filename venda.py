CB=[10,20,30]
produto=['MOUSE','PENDRIVE','CD']
estoque=[25,45,12]
VDA=[]
quantidade=[]
def limpaTela():
    print("\n"*2)
def getche():
    x=input("ENTER para continuar...")

def menu():
    limpaTela()
    print("*********MENU***********")
    print("Escolha uma opçao:")
    print("1 - adicionar produto")
    print("2 - listar produtos")
    print("3 - realizar venda")
    print("4 - listar vendas ")
    print("5 - procura produto")
    print("6 - procurar vendas")
    print("9 - fim")
    print("opçao:",end="")
def incluir():
    print("@"*15,"INCLUIR","@"*15)
    nome=input("digite o nome do produto:")
    while (nome):
        try:
            nome=nome.upper()
            codigo=int(input("digite o codigo do produto:"))
            q=int(input("digite a quantidade para o estoque:"))
            CB.append(codigo)
            produto.append(nome)
            estoque.append(q)
        except:
            print("Use numero inteiros")
            print("@"*15,"INCLUIR","@"*15)
        nome=input("digite o nome do produto:")
    print("@"*15)
    getche()
def listarestoque():
    print("@"*15," LISTA ",len(CB),"@"*15)
    for i in range(len(produto)):
        print(produto[i],"|CODIGO|",CB[i],"|ESTOQUE|:",estoque[i])
    print("@"*15)
def ldv():
    print("@"*15," LISTA ",len(VDA),"@"*15)
    for i in range(len(VDA)):
        print(VDA[i],"|Vendidos|:",quantidade[i])
    print("@"*15)
def venda():
    for i in range(len(produto)):
        print(produto[i],"|CODIGO|:",CB[i])
    comprador=input("digite o nome do comprador:")
    while(comprador):
        try:
            cod=int(input("digite o CODIGO do produto:"))
            pos=CB.index(cod)
            qtv=int(input("digite a quantidade vendida:"))
            estoque[pos]=estoque[pos]- qtv
            quantidade.append(qtv)
            VDA.append(cod)
        except:
            print("digite apenas o codigo de barras")
            getche()
        comprador=input("digite o nome do comprador:")
def procurar():
    x=input("digite o nome do produto:")
    while(x):
        try:
            x=x.upper()
            pos=produto.index(x)
            print(produto[pos],"CODIGO",CB[pos],"ESTOQUE",estoque[pos])
        except:
            print("digite letras maisculas.")
            print("produto nao encontrado!")
        x=input("digite o nome do produto:")
def PROCvenda():
    x=int(input("digite o codigo do produto:"))
    for i in range(len(VDA)):
        try:
            pos=VDA.index(x)
            print(VDA[pos],"|QUANTIA VENDIDA|",quantidade[pos])
        except:
            print("produto nao encontrado!")
        


op=0
while op!=9:
    menu()
    try:
        op=int(input())
    except:
        print("digite opçoes listada a cima!")
        getche()
    if op==1:
        incluir()
    elif op==2:
        listarestoque()
    elif op==3:
        venda()
    elif op==4:
        ldv()
    elif op==5:
        procurar()
    elif op==6:
        PROCvenda()
