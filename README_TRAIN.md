# Entrenamiento de YOLOv8 para Detección de EPP (Equipo de Protección Personal)

## Descripción General del Proyecto

Este proyecto implementa un modelo de detección de objetos YOLOv8 entrenado específicamente para identificar **Equipo de Protección Personal (EPP)** en imágenes y videos. El modelo puede detectar seis categorías distintas de elementos de seguridad.

---

## Configuración del Dataset

El conjunto de datos está compuesto por tres particiones:

### Estructura del Dataset
```yaml
train: ../train/images        # Imágenes de entrenamiento
val: ../valid/images          # Imágenes de validación
test: ../test/images          # Imágenes de prueba

nc: 6                         # Número de clases
names:
  - boots (Botas)
  - gloves (Guantes)
  - goggles (Gafas de Seguridad)
  - helmet (Casco)
  - person (Persona)
  - vest (Chaleco de Seguridad)
```

### Características del Dataset
- **Fuente**: Roboflow - Proyecto "ppe-6-classes-ntld9" (Versión 6)
- **Licencia**: MIT
- **Total de Imágenes de Prueba**: 53 conjuntos de validación
- **Total de Instancias en Validación**: 1,669 imágenes con 6,507 instancias de objetos
- **Distribución de Clases en Validación**:
  - Botas (boots): 442 imágenes, 1,276 instancias
  - Guantes (gloves): 279 imágenes, 653 instancias
  - Gafas (goggles): 604 imágenes, 875 instancias
  - Casco (helmet): 534 imágenes, 1,464 instancias
  - Persona (person): 306 imágenes, 784 instancias
  - Chaleco (vest): 572 imágenes, 1,455 instancias

---

## Configuración del Entrenamiento

### Parámetros del Modelo
- **Arquitectura Base**: YOLOv8n (YOLOv8 Nano)
- **Tamaño de Imagen**: 640 píxeles
- **Batch Size**: 16
- **Número de Épocas**: 50
- **Paciencia (Early Stopping)**: 10 épocas
- **Fracción de Datos**: 1.0 (usar el 100% del dataset)
- **Número de Workers**: 8
- **Dispositivo**: CPU (AMD Ryzen 7 8700G w/ Radeon 780M Graphics)
- **PyTorch Version**: 2.4.1+cpu
- **Ultralytics Version**: 8.4.14
- **Python Version**: 3.12.9

### Pesos del Modelo
- **Parámetros Totales**: 3,006,818
- **GFLOPs**: 8.1
- **Capas**: 73 (después de fusión)

---

## Resultados del Entrenamiento

### Información General
- **Épocas Completadas**: 37 (parada temprana activada después de la época 27)
- **Tiempo Total de Entrenamiento**: 24.965 horas (~25 horas)
- **Criterio de Parada**: Sin mejora observada en las últimas 10 épocas
- **Mejor Modelo**: Guardado en la época 27 como `best.pt`

### Métricas de Validación por Clase

| Clase | Imágenes | Instancias | Precisión | Recall | mAP50 | mAP50-95 |
|-------|----------|-----------|-----------|--------|-------|----------|
| **Botas** | 442 | 1,276 | 57.0% | 49.1% | 53.3% | 38.1% |
| **Guantes** | 279 | 653 | 47.7% | 35.1% | 31.5% | 21.6% |
| **Gafas** | 604 | 875 | 65.0% | 62.2% | 65.2% | 46.0% |
| **Casco** | 534 | 1,464 | 56.8% | 73.0% | 59.2% | 43.7% |
| **Persona** | 306 | 784 | 38.8% | 65.3% | 36.4% | 26.0% |
| **Chaleco** | 572 | 1,455 | 54.6% | 68.7% | 64.7% | 49.9% |
| **PROMEDIO** | 1,669 | 6,507 | **53.3%** | **58.9%** | **51.7%** | **37.6%** |

### Análisis Detallado de Resultados

#### Desempeño por Métrica

1. **Precisión General**: 53.3%
   - Mejor resultado: Gafas de Seguridad (65.0%)
   - Resultado más bajo: Persona (38.8%)
   - El modelo tiene una capacidad moderada para evitar falsos positivos

2. **Recall (Recuperación)**: 58.9%
   - Mejor resultado: Casco (73.0%)
   - Resultado más bajo: Guantes (35.1%)
   - El modelo identifica correctamente aproximadamente 6 de cada 10 objetos

3. **mAP50 (Precisión Media @ IoU=0.50)**: 51.7%
   - Mejor clase: Gafas de Seguridad (65.2%)
   - Desempeño más bajo: Guantes (31.5%)
   - Indica capacidad moderada en detección general

4. **mAP50-95 (Precisión Media @ IoU=0.50:0.95)**: 37.6%
   - Mejor clase: Chaleco de Seguridad (49.9%)
   - Desempeño más bajo: Guantes (21.6%)
   - Métrica más restrictiva que muestra desafíos en precisión de localización exacta

#### Clases con Mejor Desempeño
- **Gafas de Seguridad**: Combinación balanceada de precisión (65.0%) y recall (62.2%)
- **Chaleco de Seguridad**: Excelente recall (68.7%) con buena precisión (54.6%)

#### Clases con Desafíos
- **Guantes**: Bajo recall (35.1%) y mAP50 bajo (31.5%) - difíciles de detectar
- **Persona**: Baja precisión (38.8%) - muchos falsos positivos
- **Botas**: Precisión moderada (57.0%) pero recall bajo (49.1%)

### Velocidad de Inferencia
- **Preprocesamiento**: 1.3 ms por imagen
- **Inferencia**: 47.8 ms por imagen
- **Pérdida**: 0.0 ms por imagen
- **Postprocesamiento**: 0.3 ms por imagen
- **Tiempo Total Promedio**: ~49.4 ms por imagen (**~20 FPS**)

---

## Archivos de Salida

### Pesos Entrenados
- `runs/detect/runs/ppe-yolov8/weights/best.pt` - Mejor modelo (6.3 MB después de optimización)
- `runs/detect/runs/ppe-yolov8/weights/last.pt` - Último modelo (6.3 MB después de optimización)

### Notas sobre los Pesos
- El optimizador ha sido removido de ambos archivos para reducir tamaño
- Los pesos originales incluían el optimizador (~más de 12 MB)
- Archivos optimizados almacenados en: `C:\Users\usuario\Documents\ULTIMATE EPP\runs\detect\runs\ppe-yolov8\`

---

## Procedimiento de Instalación y Ejecución

### Requisitos Previos
- `data.yaml` ubicado en la raíz del repositorio (ya existe)
- Instalación apropiada de `torch` según la configuración (CUDA/CPU)
- Python 3.8 o superior

### Pasos de Instalación (Windows PowerShell)

#### 1. Crear y Activar Entorno Virtual (Recomendado)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### 2. Instalar PyTorch
```powershell
# Para CPU:
pip install torch --index-url https://download.pytorch.org/whl/cpu

# Para CUDA 12.1:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

#### 3. Instalar Dependencias
```powershell
pip install -r requirements.txt
```

#### 4. Ejecutar Entrenamiento
```powershell
python train_yolov8.py
```

### Prueba Rápida (Validación Inicial)

Para verificar el funcionamiento sin entrenar completamente, modificar `train_yolov8.py`:
```python
epochs=1  # Cambiar de 50 a 1
```

Esto generará `best.pt` en `runs/ppe-yolov8/weights/` en aproximadamente 20-30 minutos.

---

## Recomendaciones para Mejoras Futuras

### Optimización del Modelo

1. **Aumento de Datos (Data Augmentation)**
   - Implementar rotaciones, cambios de brillo, y transformaciones geométricas
   - Aumentaría la robustez del modelo, especialmente para guantes

2. **Ajuste de Hiperparámetros**
   - Aumentar épocas a 100+ con paciencia de 20
   - Experimentar con batch sizes de 32 o 64
   - Probar learning rates más agresivos

3. **Manejo de Clases Desequilibradas**
   - Usar pesos de clase para clases con bajo desempeño (guantes)
   - Recopilar más datos para clases problemáticas

4. **Arquitectura Alternativa**
   - Probar YOLOv8s o YOLOv8m para mayor capacidad
   - Implementar técnicas de ensemble

5. **Mejora de Datos**
   - Recopilar más imágenes de guantes en diferentes ángulos
   - Incluir más variabilidad en condiciones de iluminación
   - Capturar personas desde múltiples perspectivas

### Evaluación en Producción

1. Realizar pruebas en videos en tiempo real
2. Validar desempeño en condiciones de luz variable
3. Establecer umbrales de confianza apropiados por clase
4. Implementar filtros post-procesamiento para reducir falsos positivos

---

## Información de Contacto del Dataset

**Fuente Original**: Roboflow Universe
- **Workspace**: rbyz
- **Proyecto**: ppe-6-classes-ntld9
- **URL**: https://universe.roboflow.com/rbyz/ppe-6-classes-ntld9/dataset/6
- **Licencia**: MIT
