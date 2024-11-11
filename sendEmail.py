import os
import smtplib
from email.message import EmailMessage
from pw import senha

#Configurar e-mail e senha 

EMAIL_ADDRESS = 'alertadeburacos@gmail.com'
EMAIL_PASSWORD = senha

#Criar um e-mail

msg = EmailMessage()
msg['Subject'] = 'Buraco encontrado!'
msg['From'] = 'alertadeburacos@gmail.com'
msg['To'] = 'alerta.buracos@gmail.com'
msg['Cc'] = 'exampleFormControlInput1'
msg['nome'] = 'nomeUsuario'
msg['Image'] = 'exampleFormControlFile1'

#Enviar e-mail

with smtplib.SMTP('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

