import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def predecir_supervivencia():
    print("🚢 Cargando datos históricos del Titanic...")
    # Cargamos los datos directamente de un repositorio de datasets
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    
    # --- LIMPIEZA DE DATOS (Data Cleaning) ---
    # La IA no entiende "male/female", necesita números: hombre=0, mujer=1
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    # Rellenamos las edades que faltan con la media de edad de todo el barco
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    
    # Elegimos nuestras "pistas": Clase del billete, Sexo, Edad, Hermanos, Padres
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
    X = df[features]
    y = df['Survived'] # 0 = No sobrevive, 1 = Sobrevive

    # Dividimos en entrenamiento (80%) y examen (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # --- ENTRENAMIENTO ---
    print("🌲 Entrenando un Bosque de 100 Árboles de Decisión...")
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    # --- EVALUACIÓN ---
    predicciones = modelo.predict(X_test)
    precision = accuracy_score(y_test, predicciones)
    print(f"\n✅ ¡Examen completado! Precisión de la IA: {precision:.2%}")

    # --- TU SIMULACIÓN ---
    print("\n--- 🧪 TEST DE SUPERVIVENCIA PERSONALIZADO ---")
    # Prueba con un perfil: 3ª Clase, Hombre (0), 25 años, 0 hermanos, 0 padres
    sujeto = [[3, 0, 25, 0, 0]]
    resultado = modelo.predict(sujeto)
    
    if resultado[0] == 1:
        print("🟢 Resultado: La IA predice que esta persona SOBREVIVIRÍA.")
    else:
        print("🔴 Resultado: La IA predice que esta persona NO SOBREVIVIRÍA.")

if __name__ == "__main__":
    predecir_supervivencia()