import os
from collections import Counter

def principal():
    directorio_etiquetas = 'train/labels' 
    nombres_clases = ['boots', 'gloves', 'goggles', 'helmet', 'person', 'vest']

    if not os.path.exists(directorio_etiquetas):
        print(f"Error: No se encuentra la carpeta -> {directorio_etiquetas}")
        return

    conteo = Counter()
    total_imagenes = 0

    for archivo in os.listdir(directorio_etiquetas):
        if archivo.endswith('.txt'):
            total_imagenes += 1
            with open(os.path.join(directorio_etiquetas, archivo), 'r') as f:
                for linea in f:
                    id_clase = int(linea.split()[0])
                    conteo[id_clase] += 1

    print(f"--- Resultados (Total de imágenes: {total_imagenes}) ---")
    for i, nombre in enumerate(nombres_clases):
        print(f"{nombre}: {conteo[i]} instancias")

if __name__ == '__main__':
    principal()
    
    '''
    --- Resultados (Total de imágenes: 13949) ---
            boots: 9920 instancias
            gloves: 4878 instancias
            goggles: 7557 instancias
            helmet: 11108 instancias
            person: 5897 instancias
            vest: 12192 instancias
    
    '''