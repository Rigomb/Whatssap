import tkinter as tk
import pyautogui
import webbrowser
import pandas as pd
from time import sleep
import urllib.parse
import tkinter.messagebox as messagebox 
from tkinter import filedialog  

# Función que se ejecuta cuando se hace clic en el botón
def enviar_mensaje_whatsapp(numero, mensaje): 
    """Enviar mensaje a través de WhatsApp Web"""
    mensaje_codificado = urllib.parse.quote(mensaje)
    url = f"https://api.whatsapp.com/send?phone=+57{numero}&text={mensaje_codificado}"
    webbrowser.open(url)

    sleep(6) 
    
    
    pyautogui.hotkey('ctrl', 'l')  
    sleep(2)
    pyautogui.press('enter')  # Asegura que se active la ventana

    sleep(3) 

    # Escribir el mensaje en el campo de texto (asegúrate de que el chat esté abierto)
    pyautogui.write(mensaje)  # Escribe el mensaje que se quiere enviar
    pyautogui.press('enter')  # Enviar el mensaje
    
    sleep(1)  # Dar tiempo para el envío del mensaje
    
    # Cerrar la ventana de WhatsApp Web
    pyautogui.hotkey('Alt', 'F4')  # Cerrar la ventana
    sleep(2)
    pyautogui.hotkey('Ctrl', 'w')  # Cerrar la pestaña de WhatsApp Web
    sleep(2)
    
    # Marcar como "Enviado" si se envió el mensaje correctamente
    return True  # Aquí puedes incluir una validación si fuera necesario

def seleccionar_archivo():
    """Abrir un cuadro de diálogo para seleccionar el archivo Excel"""
    archivo = filedialog.askopenfilename(title="Selecciona el archivo de Excel", filetypes=[("Archivos Excel", "*.xlsx")])
    return archivo

def enviar_mensajes_masivos():
    """Función para enviar mensajes a todos los contactos de un archivo Excel"""
    archivo = seleccionar_archivo()  # Pedir al usuario seleccionar el archivo de Excel
    if archivo:  # Verificar si el archivo fue seleccionado
        df = pd.read_excel(archivo, usecols="B,C", skiprows=0)

        # Limpiar los nombres de las columnas
        df.columns = df.columns.str.strip()  
        df.columns = df.columns.str.lower()

        # Agregar una nueva columna para almacenar el estado del mensaje
        df['estado'] = 'No enviado'

        # Iterar sobre cada fila del DataFrame
        for key, row in df.iterrows():
            numero = row["telefono"]  # Verifica el nombre correcto de la columna
            mensaje = row["texto"]  # Verifica el nombre correcto de la columna
            msj = f"{mensaje}" 
            print(msj)
            
            # Intentar enviar el mensaje
            enviado = enviar_mensaje_whatsapp(numero, mensaje)
            
            # Actualizar el estado en la columna "estado"
            if enviado:
                df.at[key, 'estado'] = 'Enviado'
            else:
                df.at[key, 'estado'] = 'No enviado'
            
            sleep(5)  # Aumentar el tiempo de espera entre mensajes

        # Guardar el DataFrame actualizado con el estado de los mensajes
        df.to_excel("whatsApp_actualizado.xlsx", index=False)
        print("Mensajes enviados correctamente.")
    else:
        print("No se seleccionó un archivo.")

def mostrar_notificacion():
    """Mostrar una notificación cuando el proceso de envío termine"""
    messagebox.showinfo("Proceso terminado", "Todos los mensajes han sido enviados exitosamente.")

# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Whatsapp Masivo")
ventana.geometry("300x300")

# Etiqueta de bienvenida
etiqueta = tk.Label(ventana, text="BIENVENIDO")
etiqueta.pack(pady=40)

# Función que se ejecutará al presionar el botón "Enviar"
def click():
    """Función para iniciar el envío masivo de mensajes"""
    print("Enviando mensajes masivos...")
    enviar_mensajes_masivos()  # Llamar a la función de envío masivo de mensajes
    print("Mensajes enviados.")
    mostrar_notificacion()  # Mostrar la notificación después de enviar los mensajes

# Crear el botón que ejecutará la función 'click'
boton = tk.Button(ventana, text="Enviar", command=click, width=15, height=3)
boton.pack()

# Función para cerrar la ventana cuando se presiona el botón "Salir"
def salir():
    """Función para salir de la aplicación"""
    ventana.quit()  # Cerrar la ventana

# Crear el botón de "Salir"
boton_salir = tk.Button(ventana, text="Salir", command=salir, width=15, height=3)  # Botón más grande
boton_salir.pack(pady=10)

# Ejecutar el ciclo principal de la ventana
ventana.mainloop()