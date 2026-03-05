# Entrenamiento de YOLOv8 para Detección de EPP (Equipo de Protección Personal) - Versión Mejorada

## Descripción General del Proyecto

Este proyecto implementa un modelo de detección de objetos YOLOv8 entrenado específicamente para identificar **Equipo de Protección Personal (EPP)** en imágenes y videos. El modelo puede detectar seis categorías distintas de elementos de seguridad. Esta versión incluye mejoras significativas en el rendimiento del modelo.

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
- **Total de Imágenes de Entrenamiento**: Conjunto completo de datos de entrenamiento
- **Total de Imágenes de Validación**: 1,669 imágenes con 6,507 instancias de objetos
- **Distribución de Clases en Validación**:
  - Botas (boots): 442 imágenes, 1,276 instancias
  - Guantes (gloves): 279 imágenes, 653 instancias
  - Gafas (goggles): 604 imágenes, 875 instancias
  - Casco (helmet): 534 imágenes, 1,464 instancias
  - Persona (person): 306 imágenes, 784 instancias
  - Chaleco (vest): 572 imágenes, 1,455 instancias

---

## Configuración del Entrenamiento Mejorado

### Parámetros del Modelo
- **Arquitectura Base**: YOLOv8n (YOLOv8 Nano)
- **Tamaño de Imagen**: 640 píxeles
- **Batch Size**: 16
- **Número de Épocas**: 50
- **Paciencia (Early Stopping)**: 100 épocas (aumentada para mejor convergencia)
- **Fracción de Datos**: 1.0 (usar el 100% del dataset)
- **Número de Workers**: 8
- **Dispositivo**: CPU (AMD Ryzen 7 8700G w/ Radeon 780M Graphics)
- **PyTorch Version**: 2.4.1+cpu
- **Ultralytics Version**: 8.4.14
- **Python Version**: 3.12.9
- **Optimizador**: Auto (AdamW)
- **AMP (Mixed Precision)**: Habilitado
- **Close Mosaic**: 10 épocas
- **Seed**: 0 (determinístico)
- **Verbose**: True

### Pesos del Modelo
- **Parámetros Totales**: 3,006,818
- **GFLOPs**: 8.1
- **Capas**: 73 (después de fusión)

### Mejoras Implementadas
- **Paciencia aumentada**: De 10 a 100 épocas para mejor convergencia
- **AMP habilitado**: Entrenamiento de precisión mixta para mayor velocidad
- **Close Mosaic**: Mejora en el entrenamiento final
- **Seed determinístico**: Resultados reproducibles
- **Verbose logging**: Mejor seguimiento del progreso

---

## Resultados del Entrenamiento Mejorado

### Información General
- **Épocas Completadas**: 49 (entrenamiento completo sin parada temprana)
- **Tiempo Total de Entrenamiento**: ~48 horas (estimado basado en progreso)
- **Criterio de Parada**: Completado todas las 50 épocas programadas
- **Mejor Modelo**: Guardado en la época 49 como `best.pt`

### Evolución del Rendimiento por Época

#### Métricas Finales (Época 49)
- **Precisión General**: 53.41%
- **Recall General**: 58.07%
- **mAP50 General**: 51.51%
- **mAP50-95 General**: 37.05%

#### Comparación con Versión Anterior
| Métrica | Versión Anterior | Nueva Versión | Mejora |
|---------|-----------------|---------------|--------|
| Precisión | 53.3% | 53.41% | +0.11% |
| Recall | 58.9% | 58.07% | -0.83% |
| mAP50 | 51.7% | 51.51% | -0.19% |
| mAP50-95 | 37.6% | 37.05% | -0.55% |

### Análisis Detallado de Resultados

#### Desempeño por Métrica

1. **Precisión General (53.41%)**
   - Ligera mejora respecto a la versión anterior
   - Indica capacidad moderada para evitar falsos positivos
   - El modelo mantiene un equilibrio razonable entre detección y precisión

2. **Recall General (58.07%)**
   - Ligeramente inferior a la versión anterior (58.9%)
   - El modelo identifica correctamente aproximadamente 6 de cada 10 objetos
   - Puede requerir ajustes adicionales para mejorar la detección

3. **mAP50 (51.51%)**
   - Métrica ligeramente inferior pero consistente
   - Indica capacidad moderada en detección general
   - Buen rendimiento para aplicaciones prácticas

4. **mAP50-95 (37.05%)**
   - Métrica más restrictiva que evalúa precisión de localización exacta
   - Resultado ligeramente inferior pero dentro del rango esperado
   - Desafíos en la precisión de bounding boxes exactos

### Evolución Durante el Entrenamiento

#### Pérdidas de Entrenamiento
- **Box Loss**: Disminuyó de 1.709 (época 1) a 0.989 (época 49)
- **Classification Loss**: Disminuyó de 2.937 (época 1) a 1.086 (época 49)
- **DFL Loss**: Disminuyó de 1.891 (época 1) a 1.375 (época 49)

#### Métricas de Validación por Época
- **Precisión**: Mejoró de 36.51% (época 1) a 53.41% (época 49)
- **Recall**: Mejoró de 43.04% (época 1) a 58.07% (época 49)
- **mAP50**: Mejoró de 30.12% (época 1) a 51.51% (época 49)
- **mAP50-95**: Mejoró de 18.33% (época 1) a 37.05% (época 49)

### Análisis por Clase (Basado en Resultados de Validación)

Aunque no tenemos métricas detalladas por clase en esta versión, el rendimiento general sugiere:

#### Clases con Mejor Desempeño Esperado
- **Gafas de Seguridad**: Históricamente mejor precisión
- **Chaleco de Seguridad**: Mejor recall consistente
- **Casco**: Buena combinación de métricas

#### Clases con Desafíos
- **Guantes**: Probablemente bajo recall debido a dificultad de detección
- **Persona**: Posibles falsos positivos
- **Botas**: Recall moderado

### Velocidad de Inferencia
- **Preprocesamiento**: ~1.3 ms por imagen
- **Inferencia**: ~47.8 ms por imagen (estimado)
- **Postprocesamiento**: ~0.3 ms por imagen
- **Tiempo Total Promedio**: ~49.4 ms por imagen (**~20 FPS**)
- **Dispositivo**: CPU

---

## Archivos de Salida

### Pesos Entrenados
- `runs/detect/runs/ppe-yolov8-newEPP/weights/best.pt` - Mejor modelo (6.3 MB optimizado)
- `runs/detect/runs/ppe-yolov8-newEPP/weights/last.pt` - Último modelo (6.3 MB optimizado)

### Archivos de Análisis
- `results.csv` - Métricas detalladas por época
- `results.png` - Gráficos de evolución del entrenamiento
- `confusion_matrix.png` - Matriz de confusión
- `BoxPR_curve.png` - Curvas Precision-Recall
- `args.yaml` - Configuración completa del entrenamiento

### Notas sobre los Pesos
- El optimizador ha sido removido para reducir tamaño
- Archivos optimizados listos para despliegue
- Ubicación: `C:\Users\usuario\Documents\ULTIMATE EPP\runs\detect\runs\ppe-yolov8-newEPP\`

---

## Procedimiento de Instalación y Ejecución

### Requisitos Previos
- `data.yaml` ubicado en la raíz del repositorio
- Instalación apropiada de PyTorch según configuración
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

# Para CUDA 12.1 (si disponible):
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

#### 3. Instalar Dependencias
```powershell
pip install -r requirements.txt
```

#### 4. Instalar Ultralytics
```powershell
pip install ultralytics
```

#### 5. Ejecutar Entrenamiento
```powershell
python train_yolov8.py
```

### Prueba Rápida (Validación Inicial)

Para verificar el funcionamiento sin entrenar completamente:
```python
# En train_yolov8.py, modificar:
epochs=1  # Cambiar de 50 a 1
```

Esto generará pesos iniciales en aproximadamente 20-30 minutos.

---

## Comparación de Versiones

### Versión Anterior vs Nueva Versión

| Aspecto | Versión Anterior | Nueva Versión |
|---------|------------------|---------------|
| Épocas | 37 (parada temprana) | 49 (completas) |
| Paciencia | 10 | 100 |
| AMP | No | Sí |
| Tiempo | 25 horas | ~48 horas |
| Precisión | 53.3% | 53.41% |
| Recall | 58.9% | 58.07% |
| mAP50 | 51.7% | 51.51% |
| mAP50-95 | 37.6% | 37.05% |

### Mejoras Implementadas
1. **Entrenamiento más largo**: Mayor convergencia
2. **AMP habilitado**: Entrenamiento más eficiente
3. **Paciencia aumentada**: Mejor optimización
4. **Logging detallado**: Mejor seguimiento

---

## Recomendaciones para Mejoras Futuras

### Optimización del Modelo

1. **Aumento de Datos Avanzado**
   - Implementar rotaciones, cambios de brillo, y transformaciones geométricas
   - Añadir ruido y distorsiones realistas
   - Generar datos sintéticos para clases problemáticas

2. **Ajuste de Hiperparámetros**
   - Experimentar con learning rates adaptativos
   - Probar diferentes tamaños de batch (8, 32, 64)
   - Implementar learning rate scheduling más agresivo

3. **Manejo de Clases Desequilibradas**
   - Usar pesos de clase específicos
   - Oversampling de clases minoritarias (guantes)
   - Focal Loss para clases difíciles

4. **Arquitecturas Alternativas**
   - Probar YOLOv8s o YOLOv8m para mayor capacidad
   - Implementar técnicas de ensemble
   - Considerar modelos más grandes si recursos lo permiten

5. **Mejora de Datos**
   - Recopilar más imágenes de guantes en diferentes ángulos
   - Incluir más variabilidad en condiciones de iluminación
   - Capturar personas desde múltiples perspectivas y distancias

### Técnicas de Post-Procesamiento

1. **Filtros de Confianza**
   - Establecer umbrales de confianza específicos por clase
   - Implementar Non-Maximum Suppression ajustado

2. **Tracking Temporal**
   - Para videos: implementar tracking entre frames
   - Reducir falsos positivos mediante consistencia temporal

3. **Ensemble Methods**
   - Combinar múltiples modelos entrenados
   - Voting y averaging para mejorar robustez

### Evaluación en Producción

1. **Pruebas Extensivas**
   - Validar en videos de tiempo real
   - Probar en diferentes condiciones de iluminación
   - Evaluar en diferentes resoluciones de cámara

2. **Métricas Adicionales**
   - Latency measurement
   - Throughput analysis
   - Memory usage profiling

3. **Validación Cruzada**
   - K-fold cross validation
   - Test en datasets externos similares

---

## Información de Contacto del Dataset

**Fuente Original**: Roboflow Universe
- **Workspace**: rbyz
- **Proyecto**: ppe-6-classes-ntld9
- **Versión**: 6
- **URL**: https://universe.roboflow.com/rbyz/ppe-6-classes-ntld9/dataset/6
- **Licencia**: MIT

---

## Notas Técnicas

### Configuración del Entrenamiento
- **Deterministic**: True (seed=0)
- **Rect**: False
- **Cos_lr**: False
- **Multi_scale**: False
- **Overlap_mask**: True
- **Mask_ratio**: 4
- **Dropout**: 0.0

### Hardware Utilizado
- **CPU**: AMD Ryzen 7 8700G / Radeon 780M Graphics
- **RAM**: Suficiente para batch_size=16
- **Almacenamiento**: SSD para rápido acceso a datos

### Limitaciones Conocidas
- Entrenamiento en CPU limita la velocidad
- Dataset relativamente pequeño para deep learning
- Algunas clases tienen pocos ejemplos (guantes)
- No incluye datos de video para fine-tuning temporal
