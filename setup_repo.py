import os

def create_structure():
    # Carpetas y archivos base para un proyecto de IA profesional
    folders = ['data', 'notebooks', 'src']
    files = {
        'src/clima.py': '# Script para consultar el clima\n',
        '.env': '# Aquí irán tus API Keys (NO SUBIR A GITHUB)\n',
        'requirements.txt': 'requests\npython-dotenv\n'
    }

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    for file_path, content in files.items():
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(content)
    
    print("✅ Estructura de IA Architect creada con éxito.")

if __name__ == "__main__":
    create_structure()