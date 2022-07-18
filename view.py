from multiprocessing.sharedctypes import Value
from model import Inventory
from dal import InvestoryDAL, criar_or_conectar
from controller import InventoryController

while True:
    while True:
        try:
            escolha_user = int(input("""Escolha umas das OPÇÔES ABAIXO
            [1] Cadastrar um PRODUTO
            [2] Vizualizar Estoque
            [3] CONVERTER PARA PDF
            [4] Sair
            -->>>>>> """))
        except ValueError:
            print("ESCOLHA UMA DAS OPÇÕES.")
            continue
        else:
            break
    match escolha_user:
        
        case 4:
            break

        case 1:
            categoria = str(input("Digite a CATEGORIA: "))
            nome = str(input("Digite o NOME: "))
            modelo = str(input("Digite o MODELO: "))
            preco = float(input("Digite o PREÇO:" ))
            quantidade = int(input("Digite a QUANTIDADE: "))
            if InventoryController.cadastrar(categoria,nome,modelo,preco,quantidade):
                print('Cadastrado com SUCESSO')
        
        case 2:
            InvestoryDAL.ler()
        
        case 3:
            InventoryController.converter_pdf()

