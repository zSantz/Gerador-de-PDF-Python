# bibliotecas
from fpdf import FPDF

#entrada de dados
projeto = input('Digite a descrição do projeto: ')
horas_previstas = input('Digite a quantidade de horas previstas: ')
valor_hora = input('Digite o valor da hora trabalhada: ')
prazo = input('Digite o prazo do projeto: ')

# processamento
valor_total = int(horas_previstas) * int(valor_hora)

pdf = FPDF() # Criando um arquivo pdf
pdf.add_page() # Adicionei uma pagina ao pdf
pdf.set_font('Arial') # Definindo fonte do pdf
pdf.image("docs/template.png", x=0, y=0) # Adicionando backgroud img

# adiconando texto e alinhando
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_previstas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output('orcamentos/orçamento.pdf') #salvando o pdf

# Saida
print('Orçamento gerado com sucesso!!')