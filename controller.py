from dal import InvestoryDAL
from model import Inventory
from fpdf import FPDF

class InventoryController:
    @classmethod
    def cadastrar(cls,categoria,nome,modelo,preco,quantidade):
        try:
            InvestoryDAL.salvar(Inventory(categoria,nome,modelo,preco,quantidade))
            return True
        except:
            return False
    
    @classmethod
    def converter_pdf(cls):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('arial')

        arquivo = input('DIGITE O NOME DO ARQUIVO COM A SUA EXTENSÃO ->>>>>> ')
        nome = input("NOME PARA SALVAR NO PDF: ")
        
        try:
            with open(f'{arquivo}','r') as a:
                for i in a:
                    t = f'{i}'
                    pdf.multi_cell(200,10,
                    txt=f'{t}',
                    border=0,
                    fill=0,
                    split_only=False)
                pdf.output(f'{nome}.pdf')
                print('Convertido para PDF com SUCESSO.')
        except:
            print('ERRO')
