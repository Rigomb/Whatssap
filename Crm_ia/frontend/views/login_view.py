from controllers.usuario_controller import login_usuario
from tkinter import messagebox

def verificar_login():
    email = entrada_email.get()
    password = entrada_password.get()

    resultado = login_usuario(email, password)

    if "error" in resultado:
        messagebox.showerror("Error", resultado["error"])
        else:
        messagebox.showinfo("exito", "Bienvenido") 