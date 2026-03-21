import pandas as pd
import os

ruta_archivo = "data/historial_clima.csv"

def analizar_datos():
    if not os.path.exists(ruta_archivo):
        print("❌ Todavía no hay datos. Ejecuta src/clima.py primero.")
        return

    print("📊 Despertando a Pandas...\n")
    
    nombres_columnas = ['Fecha', 'Ciudad', 'Temperatura', 'Humedad', 'Descripcion']
    df = pd.read_csv(ruta_archivo, names=nombres_columnas)

    print("--- 📝 Tus datos en bruto ---")
    print(f"Total de registros encontrados: {len(df)}")
    print(df.tail()) 
    print("\n" + "="*40 + "\n")

    print("--- 🧠 Conclusiones de la IA ---")
    temp_media = df['Temperatura'].mean()
    print(f"🌡️ Temperatura media global: {temp_media:.2f}°C")

    fila_max = df.loc[df['Temperatura'].idxmax()]
    print(f"🔥 Récord de calor: {fila_max['Ciudad']} con {fila_max['Temperatura']}°C ({fila_max['Descripcion']})")

    fila_min = df.loc[df['Temperatura'].idxmin()]
    print(f"❄️ Récord de frío: {fila_min['Ciudad']} con {fila_min['Temperatura']}°C ({fila_min['Descripcion']})")

if __name__ == "__main__":
    analizar_datos()