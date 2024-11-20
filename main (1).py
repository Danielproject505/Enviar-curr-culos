
import requests
import smtplib
from email.mime.text import MIMEText
import os
import time

# Configurações para envio de e-mail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USUARIO = os.getenv("EMAIL_USUARIO", "williandaniel789@gmail.com")
EMAIL_SENHA = os.getenv("EMAIL_SENHA", "cambridge2021@")

# Configurações de busca de vagas
PALAVRAS_CHAVE = [
    "Oracle Cloud",
    "EPM Consultant",
    "Business System Analyst",
    "Oracle Financial Cloud",
    "Oracle EBS",
    "Gerente de Projetos",
    "Assistente de Projetos"
]
LOCALIZACAO = "Remoto"

# Simulação de uma API de vagas (substituir pelo scraping ou API real)
API_VAGAS_SIMULADA = "https://api.exemplo.com/vagas"  # API fictícia

# Função para buscar vagas (simulação de API ou scraping)
def buscar_vagas():
    print("Buscando novas vagas...")
    vagas_encontradas = []
    for palavra_chave in PALAVRAS_CHAVE:
        parametros = {"q": palavra_chave, "location": LOCALIZACAO}
        resposta = requests.get(API_VAGAS_SIMULADA, params=parametros)  # Substituir por scraping ou API real
        if resposta.status_code == 200:
            vagas_encontradas.extend(resposta.json())
    return vagas_encontradas

# Função para enviar currículo
def enviar_curriculo(vaga_email):
    mensagem = MIMEText("Segue em anexo meu currículo para avaliação.")
    mensagem["Subject"] = "Candidatura à vaga"
    mensagem["From"] = EMAIL_USUARIO
    mensagem["To"] = vaga_email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as servidor:
            servidor.starttls()
            servidor.login(EMAIL_USUARIO, EMAIL_SENHA)
            servidor.sendmail(EMAIL_USUARIO, vaga_email, mensagem.as_string())
        print(f"Currículo enviado para: {vaga_email}")
    except Exception as e:
        print(f"Erro ao enviar currículo para {vaga_email}: {e}")

# Monitoramento contínuo
def monitorar_vagas():
    vagas_processadas = set()  # Armazena IDs das vagas já processadas
    while True:
        vagas = buscar_vagas()
        for vaga in vagas:
            vaga_id = vaga.get("id")  # Substituir pelo identificador único da vaga
            if vaga_id not in vagas_processadas:
                vagas_processadas.add(vaga_id)
                enviar_curriculo(vaga.get("email"))
        time.sleep(600)  # Aguarda 10 minutos antes de verificar novamente

# Execução do script
if __name__ == "__main__":
    try:
        monitorar_vagas()
    except KeyboardInterrupt:
        print("Monitoramento encerrado pelo usuário.")
    except Exception as e:
        print(f"Erro no monitoramento: {e}")
