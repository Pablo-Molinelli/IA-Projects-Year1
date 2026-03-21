import pandas as pd
import os
import matplotlib.pyplot as plt  # Nuestra herramienta de dibujo

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

    # ==========================================
    # 🎨 NUEVO: Fase de Visualización
    # ==========================================
    print("\n🎨 Generando gráfico de temperaturas...")
    
    # 1. Ordenamos los datos de más frío a más calor (para que el gráfico parezca una escalera)
    df_ordenado = df.sort_values(by='Temperatura')

    # 2. Creamos el gráfico de barras (eje X = Ciudad, eje Y = Temperatura)
    df_ordenado.plot(kind='bar', x='Ciudad', y='Temperatura', color='skyblue', legend=False)
    
    # 3. Le ponemos título y nombres a los ejes
    plt.title('Temperaturas de las Ciudades Buscadas', fontsize=14)
    plt.xlabel('Ciudad', fontsize=12)
    plt.ylabel('Temperatura (°C)', fontsize=12)
    
    # 4. Ajustamos los márgenes para que los nombres de las ciudades no se corten
    plt.tight_layout()

    # 5. Guardamos el cuadro terminado en la carpeta "data"
    ruta_imagen = "data/grafico_temperaturas.png"
    plt.savefig(ruta_imagen)
    print(f"✅ ¡Gráfico guardado con éxito en: {ruta_imagen}!")

if __name__ == "__main__":
    analizar_datos()