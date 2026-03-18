import os
import requests
from dotenv import load_dotenv

load_dotenv()
# Capturamos la llave
llave_cruda = os.getenv('OPENWEATHER_API_KEY')

# Freno de emergencia
if llave_cruda is None:
    print("🛑 ERROR FATAL: Python no está leyendo el archivo .env")
    exit()

API_KEY = str(llave_cruda).strip()

def obtener_clima(ciudad):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        
        if respuesta.status_code == 200:
            temp = datos['main']['temp']
            sensacion = datos['main']['feels_like'] 
            humedad = datos['main']['humidity']     
            desc = datos['weather'][0]['description']
            
            print(f"\n--- 🌤️ Reporte para {ciudad} ---")
            print(f"Temperatura: {temp}°C")
            print(f"Sensación térmica: {sensacion}°C")
            print(f"Humedad: {humedad}%")
            print(f"Estado: {desc.capitalize()}")
        else:
            mensaje_error = datos.get('message', 'Error desconocido')
            print(f"❌ Error {respuesta.status_code}: {mensaje_error.capitalize()}")
            
    except Exception as e:
        print(f"⚠️ Ocurrió un error de conexión: {e}")

if __name__ == "__main__":
    ciudad_usuario = input("Introduce el nombre de una ciudad: ")
    obtener_clima(ciudad_usuario)