from PyQt6.QtGui import QFontDatabase
import os
# Esto sirve para cargar las fuentes, asi se pueden usar fuentes personalizadas, añadiendose en la cartepa "Fonts"
def cargar_fuentes():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fonts_dir = os.path.join(base_dir, "fonts")
    
    if not os.path.exists(fonts_dir):
        print(f"Carpeta de fuentes no encontrada! (La carpeta debe estar en esta posicion: {fonts_dir})")
        return
    
    print("Cargando fuentes...")
    
    for filename in os.listdir(fonts_dir):
        if filename.endswith(('.ttf', '.otf')):
            font_path = os.path.join(fonts_dir, filename)
            font_id = QFontDatabase.addApplicationFont(font_path)
            
            if font_id != -1:
                families = QFontDatabase.applicationFontFamilies(font_id)
                for family in families:
                    print(f"Fuente cargada! {family}")
            else:
                print(f"No se pudo cargar... {filename}")
    
    print("Fuentes cargadas correctamente!\n")