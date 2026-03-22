import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# 1. PREPARAR LA IA (Usamos caché para que no descargue el diccionario cada vez que pulsas un botón)
@st.cache_resource
def cargar_analizador():
    nltk.download('vader_lexicon', quiet=True)
    return SentimentIntensityAnalyzer()

analizador = cargar_analizador()

# 2. DISEÑAR LA PÁGINA WEB
st.title("🎭 El Crítico de IA")
st.subheader("Analizador de Sentimientos de Texto (NLP)")

st.write("Escribe una reseña, un tweet o simplemente cómo te sientes hoy (en inglés), y nuestra Inteligencia Artificial adivinará tu emoción.")

# 3. INTERACCIÓN CON EL USUARIO
# Creamos una caja de texto gigante
texto_usuario = st.text_area("Escribe tu texto aquí:", "I absolutely love building Artificial Intelligence apps!")

# Creamos el botón de acción
if st.button("Analizar Emoción"):
    if texto_usuario:
        # La IA lee el texto de la web
        resultado = analizador.polarity_scores(texto_usuario)
        puntuacion = resultado['compound']
        
        # Mostramos los resultados con colores bonitos
        st.write("---")
        st.write("### 🤖 Veredicto de la IA:")
        
        if puntuacion >= 0.05:
            st.success(f"🟢 EMOCIÓN POSITIVA (Puntuación: {puntuacion:.2f})")
            st.balloons() # ¡Una sorpresa visual de Streamlit!
        elif puntuacion <= -0.05:
            st.error(f"🔴 EMOCIÓN NEGATIVA (Puntuación: {puntuacion:.2f})")
        else:
            st.info(f"⚪ NEUTRAL / ROBÓTICO (Puntuación: {puntuacion:.2f})")
    else:
        st.warning("⚠️ Por favor, escribe un texto antes de analizar.")