import io
import torch
from torchvision import transforms
from PIL import Image
from ultralytics import YOLO

model = YOLO('best.pt')

def transform_image(image_bytes):
    transform = transforms.Compose([transforms.Grayscale(num_output_channels=1),
                                    transforms.Resize((640, 640)),
                                    transforms.ToTensor()])
    
    image = Image.open(io.BytesIO(image_bytes))
    grayscale_image = transform(image)
    
    # Expanding grayscale to 3 channels
    image_3channel = grayscale_image.repeat(3, 1, 1)
    return image_3channel.unsqueeze(0)

def get_prediction(image_tensor):
    with torch.no_grad():
        outputs = model(image_tensor)
        # Assuming the outputs follow the [boxes, pred_cls] format
        boxes = outputs[0]
        class_scores = outputs[1]

        # This part depends on the exact output format of your YOLOv8 model
        # Here's a simplistic way to get the class with the maximum score for each box
        _, predicted_classes = class_scores.max(2)
        
        # You would typically also apply a threshold and non-maximum suppression here
        # to filter and refine the detected boxes

    return boxes, predicted_classes