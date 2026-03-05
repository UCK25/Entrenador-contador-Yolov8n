import os
import cv2
import numpy as np
from pathlib import Path

def rotate_label(label_line, angle):
    """
    YOLOv8: class_id x_center y_center width height
    """
    parts = label_line.strip().split()
    class_id = parts[0]
    x_center = float(parts[1])
    y_center = float(parts[2])
    width = float(parts[3])
    height = float(parts[4])
    
    if angle == 90:
        
        new_x = 1 - y_center
        new_y = x_center
        new_w = height
        new_h = width
    elif angle == 180:
        
        new_x = 1 - x_center
        new_y = 1 - y_center
        new_w = width
        new_h = height
    elif angle == 270:
        
        new_x = y_center
        new_y = 1 - x_center
        new_w = height
        new_h = width
    else:
        return label_line
    
    return f"{class_id} {new_x:.6f} {new_y:.6f} {new_w:.6f} {new_h:.6f}\n"

def has_gloves(label_path):
    """
    gloves（ID=1）
    """
    try:
        with open(label_path, 'r') as f:
            for line in f:
                class_id = int(line.split()[0])
                if class_id == 1:  # gloves = 1
                    return True
    except:
        pass
    return False

def get_image_path(label_path):
    
    label_filename = os.path.basename(label_path)
    base_name = label_filename.rsplit('.', 1)[0]
    
    
    image_dir = os.path.join(os.path.dirname(label_path), '../images')
    for ext in ['.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG']:
        
        img_path = os.path.join(image_dir, base_name + ext)
        if os.path.exists(img_path):
            return img_path
        
        
        for file in os.listdir(image_dir):
            if file.startswith(base_name) and file.endswith(ext):
                return os.path.join(image_dir, file)
    
    return None

def main():
    
    labels_dir = 'train/labels'
    images_dir = 'train/images'
    
    if not os.path.exists(labels_dir):
        print(f"Error: {labels_dir} no encuentra en la ruta especificada")
        return
    
    if not os.path.exists(images_dir):
        print(f"Error: {images_dir} no encuentra en la ruta especificada")
        return
    
    angles = [90, 180, 270]
    processed_count = 0
    augmented_count = 0
    
    print("=== Gloves Augmentation ===")
    print(f"処理対象: {labels_dir}")
    
    
    for label_file in os.listdir(labels_dir):
        if not label_file.endswith('.txt'):
            continue
        
        label_path = os.path.join(labels_dir, label_file)
        
        # gloves
        if not has_gloves(label_path):
            continue
        
        processed_count += 1
        image_path = get_image_path(label_path)
        
        if image_path is None:
            print(f"⚠ 画像が見つかりません: {label_file}")
            continue
        
        
        img = cv2.imread(image_path)
        if img is None:
            print(f"⚠ 画像を読み込めません: {image_path}")
            continue
        
        # Etiqueta
        with open(label_path, 'r') as f:
            label_lines = f.readlines()
        
        base_name = label_file.rsplit('.', 1)[0]
        image_ext = os.path.splitext(image_path)[1]
        
        
        for angle in angles:
            
            if angle == 90:
                rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            elif angle == 180:
                rotated_img = cv2.rotate(img, cv2.ROTATE_180)
            elif angle == 270:
                rotated_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            
            
            new_image_name = f"{base_name}_rot{angle}{image_ext}"
            new_image_path = os.path.join(images_dir, new_image_name)
            cv2.imwrite(new_image_path, rotated_img)
            
            
            new_label_name = f"{base_name}_rot{angle}.txt"
            new_label_path = os.path.join(labels_dir, new_label_name)
            
            with open(new_label_path, 'w') as f:
                for label_line in label_lines:
                    rotated_label = rotate_label(label_line, angle)
                    f.write(rotated_label)
            
            augmented_count += 1
        
        if processed_count % 100 == 0:
            print(f"Proceso {processed_count}files")
    
    print(f"\n=== 処理完了 ===")
    print(f"Gloves を含む画像: {processed_count}個")
    print(f"生成された拡張データ: {augmented_count}個 (各画像×3回転)")
    print(f"新しい画像ファイル: {images_dir} に保存されました")
    print(f"新しいラベルファイル: {labels_dir} に保存されました")

if __name__ == '__main__':
    main()
