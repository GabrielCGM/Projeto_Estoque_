from model import Inventory

def criar_or_conectar():
    arqtxt = str(input("Digite o nome do arquivo pra abrir-lo: "))
    return arqtxt

class InvestoryDAL:
    @classmethod
    def salvar(cls,estoque:Inventory):
        with open(f'{criar_or_conectar()}.txt','a') as arq:
            arq.writelines(f'CATEGORIA: {estoque.categoria} | NOME: {estoque.nome} | MODELO: {estoque.modelo} | PREÇO: {estoque.preco} | QUANTIDADE: {estoque.quantidade}\n')
    
    @classmethod
    def ler(cls):
        with open(f'{criar_or_conectar()}.txt','r') as arq:
            for i in arq:
                print(i)
