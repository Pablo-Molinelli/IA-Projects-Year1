import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def entrenar_ia_inmobiliaria():
    print("🌍 1. Cargando base de datos de California...")
    
    # Cargamos el dataset oficial de casas
    datos = fetch_california_housing()
    df = pd.DataFrame(datos.data, columns=datos.feature_names)
    df['Precio'] = datos.target # El precio es lo que queremos predecir

    print(f"✅ Cargadas {len(df)} casas para estudiar.")

    # 2. PREPARAR LOS DATOS (X = pistas, y = respuesta)
    X = df.drop('Precio', axis=1) 
    y = df['Precio'] 

    # Dividimos: 80% para estudiar, 20% para el examen sorpresa
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. CREAR Y ENTRENAR EL MODELO (Machine Learning real)
    print("🧠 2. Entrenando a la IA (esto son matemáticas puras)...")
    modelo = LinearRegression()
    modelo.fit(X_train, y_train) # Aquí la IA busca patrones entre las pistas y el precio
    print("✅ ¡Entrenamiento completado!")

    # 4. PRUEBA DE FUEGO (Predicción)
    print("\n--- 🔮 EXAMEN DE LA IA ---")
    # Cogemos una casa del grupo de examen que la IA nunca ha visto
    casa_ejemplo = X_test.iloc[[0]] 
    precio_real = y_test.iloc[0] * 100000 
    
    # Le pedimos a la IA que use lo aprendido para adivinar el precio
    prediccion = modelo.predict(casa_ejemplo)
    precio_ia = prediccion[0] * 100000

    print(f"🏠 Precio real:       {precio_real:,.2f} $")
    print(f"🤖 Predicción IA:     {precio_ia:,.2f} $")
    print(f"📊 Diferencia:        {abs(precio_real - precio_ia):,.2f} $")

if __name__ == "__main__":
    entrenar_ia_inmobiliaria()