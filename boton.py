from twilio.rest import Client
from flask import Flask, request
import sqlite3
from docx import Document
from fpdf import FPDF
import os

app = Flask(__name__)

TWILIO_ACCOUNT_SID = 'ACb9140f0f642b28fb02e42ad733e06008' 
TWILIO_AUTH_TOKEN = '326395d77a17983aee08b368e0aa5858'  
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  
TO_WHATSAPP_NUMBER = 'whatsapp:+573132648545'  

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def obtener_respuesta(pregunta, estado_usuario):

    saludos = ['hola', 'buenos días', 'buenas tardes', 'buenas noches', 'qué tal', 'hey','ola','buenas','buen día']
    despedidas = ['adiós', 'hasta luego', 'nos vemos', 'chau', 'bye', 'hasta pronto','gracias','gracias por tu ayuda','chao','adios']
    
    if 'volver' in pregunta or 'volver al menú principal' in pregunta or 'menú principal' in pregunta or 'regresar' in pregunta or 'atras' in pregunta or 'menu' in pregunta:
        return ("¿en qué te puedo ayudar?😊\n"
            "\n"
            "1. Solicitar Paz y Salvo\n"
            "2. Estado de Cuenta\n"
            "3. Medios De Pago\n"
            "4. Solicitar Crédito LiliPink & Yoi\n"
            "5. Suplantacion\n"
            "6. Otro motivo\n"
            "\n"
            "Recuerda nuestro horario de Lunes a Viernes de 7:00 am a 5:00 pm\n"
            "\n"
            "Quedo Atento a tu Solicitud\n")
    
    if any(saludo in pregunta for saludo in saludos):
        return ("Bienvenido a Credipink. Hablas con CrediBot en qué te puedo ayudar?😊\n"
                "\n"
                "1. Solicitar Paz y Salvo\n"
                "2. Estado de Cuenta\n"
                "3. Medios De Pago\n"
                "4. Solicitar Crédito LiliPink & Yoi\n"
                "5. Suplantacion\n"
                "6. Otro motivo\n"
                "\n"
                "Recuerda nuestro horario de Lunes a Viernes de 7:00 am a 5:00 pm\n"
                "\n"
                "Quedo Atento a tu Solicitud\n")
        
    if any(opcion in pregunta for opcion in ['1', 'solicitar paz y salvo', 'paz y salvo']):
        return ("Por favor, ingresa tu número de cédula para verificar tu estado.\n"
                "\n"
                "Volver al menú principal")
        
         
         
    if any(opcion in pregunta for opcion in ['2', 'estado de cuenta','cuanto debo']):
        return ("Para solicitar el ESTADO DE CUENTA debe enviar su solicitud a esta dirección de correo  electronico gestiondecobrocartera@fastmoda.com.co\n"
                 "\n"
                "Volver al menú principal")
    
    if any(opcion in pregunta for opcion in ['3', 'medios de pago','como puedo pagar','link de pago','pse']):
        return ("Los medios de pago disponibles son:\n"
                "\n"
                "1. Pagos PSE en el siguiente link: https://www.lilipink.com.co/\n"
                "\n"
                "2. En Tiendas Lili Pink o Yoi Directamente con tu número de Cédula puedes ir tu o un tercero a generar el pago\n"
                 "\n"
                "Volver al menú principal")
    
    if any(opcion in pregunta for opcion in ['4', 'solicitar credito','credito liliPink','credito Yoi','credito','como solicitar credito']):
        return ("Puedes solicitar tu credito lilipink en cualquier tienda LILI PINK & YOI a nivel nacional"
                "tan solo presentando tu cédula de ciudadanía y diligenciando el formulario de solicitud de crédito"
                "consultados y verificados en centrales de riesgo, es importante que tengas tu celular a la mano"
                "ya que te enviaran la confirmación por este medio\n"
                "\n"
                "Nota: No generamos validación online\n"
                 "\n"
                "Volver al menú principal")
        
    if any(opcion in pregunta for opcion in ['5', 'suplantacion','suplantación','estafa','fraude']):
        return ("para proceder con el escalamiento por suplantacion es tan amable de enviar los siguientes documentos al correo electronico gestiondecobrocartera@fastmoda.com.co\n"
                 "\n"
                'Cedula al 150 a Color\n'
                'Foto Del Rostro\n'
                'Copia de la Denuncia Ante las Fiscalía por Suplantación\n'
                 "\n"
                "Volver al menú principal")
   
    if any(opcion in pregunta for opcion in ['6', 'otro motivo','otro','ayuda','información']):
        return ("Para cualquier otra solicitud o información adicional, por favor comunícate con nosotros a través de los "
               'siguientes canales de atención al cliente:\n'
                "\n"
                'Correo: gestiondecobrocartera@fastmoda.com.co\n'
                "Telefono: 3241000017 Ext 1011 - 1003 en horario de Lunes a Viernes de 7:00 am a 5:00 pm\n"
                '\n'
                "Volver al menú principal")

    if any(despedida in pregunta for despedida in despedidas):
        return ("¡Gracias por contactarnos! 😊 Si necesitas algo más no dudes en escribir.\n"
                'CrediBot te Desea un excelente Dia\n')
    
    return "Lo siento, no entiendo tu pregunta. ¿Intenta Nuevamente?"

@app.route("/webhook", methods=['POST'])
def webhook():
    
    incoming_msg = request.values.get('Body', '').lower()
    from_number = request.values.get('From', '')
 
    estado_usuario = {}  # El estado del usuario se puede almacenar en una base de datos real
    
    # Obtener la respuesta del chatbot
    respuesta = obtener_respuesta(incoming_msg, estado_usuario)

    client.messages.create(
        body=respuesta,
        from_=TWILIO_WHATSAPP_NUMBER,
        to=from_number
    )
    
    return '', 200

# Iniciar el servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
