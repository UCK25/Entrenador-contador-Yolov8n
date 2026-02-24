import torch_directml
from ultralytics import YOLO

def main():
    dml = torch_directml.device()
    print(f"device: {dml}")
    
    model = YOLO('yolov8n.pt')

    model.train(
        data='data.yaml',
        imgsz=640,
        
        epochs=50, #30 - 50 
        
        batch=16,
        fraction=1,
        device='cpu',
        workers=8,
        patience=10,
        project='runs',
        name='ppe-yolov8-2',
        exist_ok=False
    )

    print('weights in runs/ppe-yolov8/weights')

if __name__ == '__main__':
    main()
