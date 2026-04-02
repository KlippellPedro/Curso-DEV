from flask import Flask,render_template,request,request
from  funcionario import Funcionario
import os
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Table,TableStyle,Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
app=Flask(__name__)

# Define dados fixos da empresa
EMPRESA="Escola de Educação Profissional Senac Tech"
CNPJ="03.422.707/0044-14"
ENDERECO="Rua Vênancio Aires, 93 - Cidade Baixa - Porto Alegre - RS"

@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        # Recebe dados do formulário
        nome=request.form.get("nome")
        valor_hora=request.form.get("valor_hora")
        horas=request.form.get("horas")
        vale_alimentacao=request.form.get("vale_alimentacao")
        vale_transporte=request.form.get("vale_transporte")
        
        # Cria objeto funcionario
        funcionario=Funcionario(nome,valor_hora,horas,vale_alimentacao,vale_transporte)
        # Gera o PDF automaticamente
        gerar_contracheque(funcionario)
        
        return render_template("resultado.html", f=funcionario)
    return render_template("index.html")
# Função para gerar o PDF
def gerar_contracheque(funcionario):
    # Verifica se a pasta contracheque existe
    if not os.path.exists("contracheques"):
        # cria a pasta se não existir
        os.makedirs("contracheques")
        
    # Define o mês referência atual
    mes_referencia=datetime.now().strftime("%m/%Y")
    # Gera número unico para contracheque
    numero_contracheque=datetime.now().strftime("%Y%m%d%H%M")
    # Define o caminho do arquivo
    caminho= f"contracheques/contracheque_{funcionario.nome}_{numero_contracheque}.pdf"
    # Cria documento PDF
    doc=SimpleDocTemplate(caminho,pagesize=A4)
    # Lista que armazena os elementos do PDF    
    elementos=[]
    # Obtém estilos padrão
    estilos=getSampleStyleSheet()
    # Se existir logo da empresa
    if os.path.exists("static/logo.png"):
        # Insere imagem no PDF
        logo= Image ("static/logo.png", width=6*cm, height=2*cm)
        # Adiciona imagem aos elementos
        elementos.append(logo)
    
    # Adiciona informações da empresa
    elementos.append(Paragraph(f"{EMPRESA}", estilos["Title"]))
    elementos.append(Paragraph(f"{CNPJ}", estilos["Normal"]))
    elementos.append(Paragraph(f"{ENDERECO}", estilos["Normal"]))
    
    # Espaçamento
    elementos.append(Spacer(1,20))
    # Titulo do documento
    elementos.append(Paragraph("<b>CONTRACHEQUE</b>", estilos["Heading2"]))
    # Mostra mês de referência
    elementos.append(Paragraph(f"Mês de referência: {mes_referencia}", estilos["Normal"]))
    #Mostra número do contracheque
    elementos.append(Paragraph(f"N° Contracheque: {numero_contracheque}", estilos["Normal"]))
    
    # Dados do funcionario em tabela
    dados=[
        ["Funcionário: ", funcionario.nome],
        ["Matrícula: ", funcionario.matricula],
        ["Valor hora: ", funcionario.valor_hora],
        ["Horas trabalhadas: ", funcionario.horas],
    ]
    # Cria a tabela
    tabela_dados=Table(dados,colWidths=[5*cm,10*cm])
    # Aplica estilo
    tabela_dados.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey)
    ]))
    elementos.append(tabela_dados)
    elementos.append(Spacer(1,20))
    
    # Tabela financeira
    financeiro=[
        ["Descrição", "Proventos", "Descontos"],
        ["Salário bruto", f"{funcionario.salario_bruto:.2f}", ""],
        ["INSS", "", f"{funcionario.inss:.2f}"],
        ["IRRF", "", f"{funcionario.irrf:.2f}"],
        ["Vale alimentação", "", f"{funcionario.desconto_va:.2f}"],
        ["Vale transporte", "", f"{funcionario.desconto_vt:.2f}"],
        ["Total descontos", "", f"{funcionario.total_descontos:.2f}"],
        ["Salário Líquido", "", f"{funcionario.salario_liquido:.2f}"]
    ]
    # Cria a tabela financeira
    tabela_fin=Table(financeiro, colWidths=[6*cm, 4*cm, 4*cm])
    
    # Estiliza a tabela
    tabela_fin.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
        ("TEXTCOLOR", (0,0),(-1,0), colors.white),
        ("GRID", (0,0),(-1,-1), 0.5, colors.gray),
        ("ALIGN", (1,1),(-1,-1), "RIGHT"),
        ("BACKGROUND", (0,-1),(-1,-1), colors.lightgrey)
    ]))
    elementos.append(tabela_fin)
    # Espaço para assinatura
    elementos.append(Spacer(1,40))
    elementos.append(Paragraph("_________________________________________", estilos["Normal"]))
    elementos.append(Paragraph("Assinatura do funcionário", estilos["Normal"]))
    
    # Gera o PDF
    doc.build(elementos)
    
if __name__=="__main__":
    app.run(debug=True)