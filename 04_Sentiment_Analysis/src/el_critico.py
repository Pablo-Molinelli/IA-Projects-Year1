import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analizar_emociones():
    print("🧠 Descargando el diccionario de emociones de la IA...")
    # Descargamos el léxico necesario (solo tarda un segundo la primera vez)
    nltk.download('vader_lexicon', quiet=True)

    # Inicializamos nuestro cerebro lector
    analizador = SentimentIntensityAnalyzer()

    print("\n" + "="*40)
    print("🎭 EL CRÍTICO DE IA: Análisis de Sentimientos")
    print("="*40)

    # Textos de prueba (Reseñas de películas)
    textos = [
        "I absolutely LOVE this movie! It is a masterpiece 🎬",
        "This was the worst film I have ever seen. Terrible acting.",
        "It was okay. The visual effects were fine, but the story was boring.",
        "I am so angry right now! I demand a refund."
    ]

    for texto in textos:
        # La IA lee la frase y le asigna puntuaciones matemáticas
        resultado = analizador.polarity_scores(texto)
        puntuacion = resultado['compound'] # Va de -1 (muy negativo) a 1 (muy positivo)

        # Traducimos la matemática a emociones humanas
        if puntuacion >= 0.05:
            emocion = "🟢 POSITIVO"
        elif puntuacion <= -0.05:
            emocion = "🔴 NEGATIVO"
        else:
            emocion = "⚪ NEUTRAL"

        print(f"\n📝 Texto: '{texto}'")
        print(f"🤖 Veredicto: {emocion} (Puntuación matemática: {puntuacion:.2f})")

    # --- ✍️ PRUEBA EN VIVO ---
    print("\n" + "-"*40)
    print("🧪 ¡AHORA PRUEBA TÚ!")
    tu_frase = input("Escribe una frase en INGLÉS (ej. 'I am very happy'): ")
    
    if tu_frase:
        resultado_usuario = analizador.polarity_scores(tu_frase)
        puntos_usuario = resultado_usuario['compound']
        
        if puntos_usuario >= 0.05:
            emo_usuario = "🟢 POSITIVO"
        elif puntos_usuario <= -0.05:
            emo_usuario = "🔴 NEGATIVO"
        else:
            emo_usuario = "⚪ NEUTRAL"
            
        print(f"👉 La IA dice que tu frase es: {emo_usuario} ({puntos_usuario:.2f})")

if __name__ == "__main__":
    analizar_emociones()