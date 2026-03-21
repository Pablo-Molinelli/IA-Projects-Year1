import os
import requests
from dotenv import load_dotenv
import datetime

load_dotenv()
llave_cruda = os.getenv('OPENWEATHER_API_KEY')

if llave_cruda is None:
    print("🛑 ERROR FATAL: Python no está leyendo el archivo .env")
    exit()

API_KEY = str(llave_cruda).strip()

# ==========================================
# La memoria de la IA
# ==========================================

def guardar_historial(ciudad, temp, humedad, desc):
    # 1. Definimos dónde se guarda el archivo
    ruta_archivo = "data/historial_clima.csv"
    
    # 2. Capturamos el momento exacto (Año-Mes-Día Hora:Minuto:Segundo)
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 3. Preparamos la línea de texto separada por comas
    linea_datos = f"{fecha_hora},{ciudad.capitalize()},{temp},{humedad},{desc}\n"
    
    # 4. Abrimos el archivo en modo "a" (Append = Añadir al final) y escribimos
    with open(ruta_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(linea_datos)

# ==========================================
# 🌍 FUNCIÓN PRINCIPAL 
# ==========================================

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
            
            print(f"\n--- 🌤️ Reporte para {ciudad.capitalize()} ---")
            print(f"Temperatura: {temp}°C")
            print(f"Sensación térmica: {sensacion}°C")
            print(f"Humedad: {humedad}%")
            print(f"Estado: {desc.capitalize()}")
            
            #Llamamos a la función de memoria justo después de imprimir
            guardar_historial(ciudad, temp, humedad, desc)
            print("💾 Datos guardados en data/historial_clima.csv")
            
        else:
            mensaje_error = datos.get('message', 'Error desconocido')
            print(f"❌ Error {respuesta.status_code}: {mensaje_error.capitalize()}")
            
    except Exception as e:
        print(f"⚠️ Ocurrió un error de conexión: {e}")
        

# ==========================================
# 🚀 MOTOR PRINCIPAL (El bucle)
# ==========================================
if __name__ == "__main__":
    print("🌟 ¡Bienvenido al rastreador climático de IA!")
    print("Escribe 'salir' en cualquier momento para cerrar el programa.\n")
    
    # Este bucle se repetirá para siempre hasta que usemos "break"
    while True:
        ciudad_usuario = input("Introduce el nombre de una ciudad (o 'salir'): ")
        
        # 1. Limpiamos espacios extra y lo pasamos a minúsculas para evitar errores
        texto_limpio = ciudad_usuario.strip().lower()
        
        # 2. Condición de salida (El botón de apagado)
        if texto_limpio == 'salir':
            print("👋 ¡Programa terminado! Tus datos están a salvo en la carpeta 'data/'.")
            break # <--- Esto rompe el bucle y termina el programa
            
        # 3. Evitar que el usuario le dé a Enter sin escribir nada
        elif texto_limpio == '':
            print("⚠️ Por favor, escribe una ciudad válida.\n")
            continue # <--- Esto salta a la siguiente vuelta del bucle sin hacer la búsqueda
            
        # 4. Si no ha escrito "salir" ni está vacío, buscamos el clima
        else:
            obtener_clima(ciudad_usuario)
            print("-" * 40) # Imprime una línea separadora para que se vea bonito