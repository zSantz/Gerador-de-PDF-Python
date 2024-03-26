from fpdf import FPDF 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

while True:
    opcao = int(input('''
Bem vindo. Segue as atividades. \n
- Para criar relatorios e enviar[1]\n   
- Para sair [2]\n
Digite a sua atividade: '''))

    if opcao == 1:
        # entrada de dados
        cliente = input('Digite o nome do Cliente: ')
        projeto = input('Digite a descrição do projeto: ')
        horas_previstas = input('Digite a quantidade de horas previstas: ')
        valor_hora = input('Digite o valor da hora trabalhada: ')
        prazo = input('Digite o prazo do projeto: ')
        email = input('Digite o e-mail do cliente: ')
        print('\n[Orçamento gerado e enviado com sucesso!!]')
        
        # processamento
        valor_total = int(horas_previstas) * int(valor_hora)

        # gerando pdf
        pdf = FPDF() # Criando um arquivo pdf
        pdf.add_page() # Adicionei uma pagina ao pdf
        pdf.set_font('Arial') # Definindo fonte do pdf
        pdf.image("docs/template.png", x=0, y=0) # Adicionando backgroud img

        # adiconando texto e alinhando
        pdf.text(115, 145, projeto)
        pdf.text(115, 160, horas_previstas)
        pdf.text(115, 175, valor_hora)
        pdf.text(115, 190, prazo)
        pdf.text(115, 205, str(f'R$: {valor_total}'))

        pdf.output('orcamento.pdf') #salvando o pdf
        
        # Enviando e-mail
        from_address = 'you_email'
        to_address = f'{email}'
        subject = 'Orçamento'
        body = f'Olá, Sr(a). {cliente}, segue o Orçamento.'

        file_path = 'orcamento.pdf'

        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with open(file_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header('Content-Disposition', f'attachment; filename= "orcamento.pdf"')

        msg.attach(part)

        smtp_server = 'smtp_Server_link'
        smtp_port = 'you_port'

        smtp_username = 'user'
        smtp_password = 'password'

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(from_address, to_address, text)
        server.quit()
    elif opcao == 2:
        break
else:
    print('Até logo!')
