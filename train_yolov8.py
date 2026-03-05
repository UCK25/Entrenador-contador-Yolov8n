import torch_directml
from ultralytics import YOLO
import os

def main():
    dml = torch_directml.device()
    print(f"device: {dml}")
    
    resume_checkpoint = 'runs/ppe-yolov8-newEPP/weights/last.pt'

    if os.path.exists(resume_checkpoint):
        print(f"Checking for checkpoint: {resume_checkpoint} -> Found! Resuming...")
        model = YOLO(resume_checkpoint)
        model.train(resume=True)
    else:
        print("No checkpoint found. Starting a new training...")
        
        model = YOLO('yolov8n.pt')
        model.train(
            data='data.yaml',
            imgsz=640,
            epochs=50,
            batch=16,
            fraction=1,
            device='cpu',
            workers=8,
            project='runs',
            name='ppe-yolov8-newEPP',
            exist_ok=True
        )

    print('Training process finished.')

if __name__ == '__main__':
    main()
'''
            all       1669       6507      0.521      0.611       0.52      0.373
                 boots        442       1276       0.56       0.52      0.541      0.388
                gloves        279        653      0.469      0.354      0.322      0.215
               goggles        604        875      0.632      0.642      0.646      0.449
                helmet        534       1464      0.558      0.764      0.596      0.437
                person        306        784      0.365      0.691      0.366      0.257
                  vest        572       1455       0.54      0.693      0.649      0.496
'''