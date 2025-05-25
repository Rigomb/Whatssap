import requests

def login_usuario(email, password):
    datos = {
        'email': email,
        'password': password
    }
    try:
        response = requests.post(http://localhost:8000/api/login, json=datos)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Error en la autenticación"}

    except requests.exceptions.ConnectionError:
        return {"error": "Error en la conexión con el servidor"}